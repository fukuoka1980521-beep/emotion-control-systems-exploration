import numpy as np
import pandas as pd
from pathlib import Path

OUT=Path(__file__).resolve().parent/"generated"
OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(20260916)

N=250
HIST=["helper","neutral","hostile"]
HISTORY_STEPS=220
HARM_EVENTS=10
RECOVERY_STEPS=180
ACTIONS=["wait","repair","confront","sanction"]
COST={"wait":0.0,"repair":0.08,"confront":0.17,"sanction":0.26}
BASE_ALPHA=.04
SURPRISE_GAIN=.20

def hist_outcome(h,r):
    x=r.random()
    if h=="helper": return 1.0 if x<.92 else .2
    if h=="neutral":
        return .5 if x<.35 else (0.0 if x<.70 else -.4)
    return -1.0 if x<.88 else -.2

def upd(mu,y):
    pe=y-mu
    a=min(.45,BASE_ALPHA+SURPRISE_GAIN*abs(pe))
    return mu+a*pe, pe, a

def policy(mu,last_pe,unc=.2):
    hp=max(0,-mu); sp=max(0,-last_pe)
    u={
        "wait":.15*max(0,mu)-.05*unc,
        "repair":.45-.06*unc-COST["repair"],
        "confront":.10+.65*hp+.22*sp-COST["confront"],
        "sanction":-.05+.95*hp+.30*sp-COST["sanction"],
    }
    return max(u,key=u.get)

rows=[]
for h in HIST:
    for agent in range(N):
        mu=0.0
        errs=[]
        for _ in range(HISTORY_STEPS):
            y=hist_outcome(h,rng)
            mu,pe,a=upd(mu,y)
            errs.append(abs(pe))
        pre=mu
        for k in range(1,HARM_EVENTS+1):
            mu,pe,a=upd(mu,-1.0)
            act=policy(mu,pe,np.mean(errs[-20:]) if errs else .2)
            rows.append([h,agent,"harm",k,pre,mu,pe,a,act,int(act in ("confront","sanction")),int(act=="sanction")])
            errs.append(abs(pe))
        for k in range(1,RECOVERY_STEPS+1):
            mu,pe,a=upd(mu,1.0)
            act=policy(mu,pe,np.mean(errs[-20:]) if errs else .2)
            if k in [1,5,10,20,50,100,180]:
                rows.append([h,agent,"recovery",k,pre,mu,pe,a,act,int(act in ("confront","sanction")),int(act=="sanction")])
            errs.append(abs(pe))

df=pd.DataFrame(rows,columns=["history","agent","phase","step","pre_mu","mu","pe","alpha","action","actor_directed","sanction"])
agg=df.groupby(["history","phase","step"],as_index=False).agg(
    mean_mu=("mu","mean"), mean_pe=("pe","mean"), mean_alpha=("alpha","mean"),
    actor_rate=("actor_directed","mean"), sanction_rate=("sanction","mean")
)

metrics=[]
for h in HIST:
    hh=agg[(agg.history==h)&(agg.phase=="harm")]
    rr=agg[(agg.history==h)&(agg.phase=="recovery")]
    metrics.append({
        "history":h,
        "pre_mu":df[df.history==h].pre_mu.mean(),
        "first_harm_prediction_error":hh[hh.step==1].mean_pe.iloc[0],
        "first_harm_learning_rate":hh[hh.step==1].mean_alpha.iloc[0],
        "actor_after_1_harm":hh[hh.step==1].actor_rate.iloc[0],
        "actor_after_10_harms":hh[hh.step==10].actor_rate.iloc[0],
        "sanction_after_1_harm":hh[hh.step==1].sanction_rate.iloc[0],
        "recovery_actor_at_10":rr[rr.step==10].actor_rate.iloc[0],
        "recovery_actor_at_50":rr[rr.step==50].actor_rate.iloc[0],
        "recovery_actor_at_180":rr[rr.step==180].actor_rate.iloc[0],
    })
met=pd.DataFrame(metrics)

abl=[]
for _,r in met.iterrows():
    pre=r.pre_mu
    pe=-1-pre
    alpha=min(.45,BASE_ALPHA+SURPRISE_GAIN*abs(pe))
    mu1=pre+alpha*pe
    hp=max(0,-mu1)
    u={
        "wait":.15*max(0,mu1)-.01,
        "repair":.45-.012-COST["repair"],
        "confront":.10+.65*hp-COST["confront"],
        "sanction":-.05+.95*hp-COST["sanction"],
    }
    act=max(u,key=u.get)
    abl.append({"history":r.history,"pre_mu":pre,"pe":pe,"mu_after_first":mu1,"best_action_no_surprise":act})
abl=pd.DataFrame(abl)

met.to_csv(OUT/"attachment_emotion_v6_betrayal_metrics.csv",index=False)
agg.to_csv(OUT/"attachment_emotion_v6_curves.csv",index=False)
abl.to_csv(OUT/"attachment_emotion_v6_surprise_ablation.csv",index=False)
