import numpy as np
import pandas as pd
from pathlib import Path

OUT=Path(__file__).resolve().parent/"generated"
OUT.mkdir(exist_ok=True)
rng=np.random.default_rng(20260916+71)
N=5000

BASE={"competence":.85,"regard":.82,"integrity":.88}
SC={
"external_loss":({"competence":0,"regard":0,"integrity":0},0,0,0),
"private_failure":({"competence":-.70,"regard":0,"integrity":0},0,0,0),
"public_failure":({"competence":-.70,"regard":-.55,"integrity":0},1,0,0),
"false_public_insult":({"competence":0,"regard":-.70,"integrity":0},1,1,0),
"own_moral_violation":({"competence":0,"regard":-.25,"integrity":-.80},0,0,1),
}
ACTIONS=["ignore","improve","withdraw","defend","repair"]
COST={"ignore":0,"improve":.12,"withdraw":.10,"defend":.16,"repair":.15}

def val(st,dims=("competence","regard","integrity")):
    return sum(st[d] for d in dims)

def apply_event(ev):
    return {d:float(np.clip(BASE[d]+ev[d],-1,1)) for d in BASE}

def action_effect(state, scenario, action):
    ev,pub,false,own=SC[scenario]
    ns=dict(state)
    bonus=pen=0.0
    if action=="improve":
        if ev["competence"]<0:
            ns["competence"]=min(1.0,ns["competence"]+.45)
            ns["regard"]=min(1.0,ns["regard"]+.05)
        else:
            pen+=.05
    elif action=="defend":
        if false:
            ns["regard"]=min(1.0,ns["regard"]+.45)
            bonus+=.25
        else:
            pen+=.08
    elif action=="repair":
        if own:
            ns["integrity"]=min(1.0,ns["integrity"]+.50)
            ns["regard"]=min(1.0,ns["regard"]+.18)
            bonus+=.25
        else:
            pen+=.08
    elif action=="withdraw":
        if pub:
            bonus+=.10
        else:
            pen+=.05
    return ns,bonus,pen

def utility(state,scenario,action,dims=("competence","regard","integrity")):
    ns,b,p=action_effect(state,scenario,action)
    return val(ns,dims)+b-p-COST[action]

def softmax(utils,temp=.24):
    ks=list(utils); x=np.array([utils[k] for k in ks]); x-=x.max()
    p=np.exp(x/temp); p/=p.sum()
    return dict(zip(ks,p))

rows=[]
for name,(ev,pub,false,own) in SC.items():
    st=apply_event(ev)
    before=val(BASE); after=val(st)
    pr=softmax({a:utility(st,name,a) for a in ACTIONS})
    draws=rng.choice(ACTIONS,size=N,p=[pr[a] for a in ACTIONS])
    vc=pd.Series(draws).value_counts(normalize=True)
    for a in ACTIONS:
        rows.append([name,a,float(vc.get(a,0)),after-before,ev["competence"],ev["regard"],ev["integrity"]])
rates=pd.DataFrame(rows,columns=["scenario","action","rate","self_delta","pe_competence","pe_regard","pe_integrity"])

summary=[]
for name in SC:
    d=rates[rates.scenario==name].sort_values("rate",ascending=False)
    top=d.iloc[0]
    summary.append({
        "scenario":name,
        "self_value_delta":top.self_delta,
        "top_action":top.action,
        "top_action_rate":top.rate,
        "ignore_rate":float(d[d.action=="ignore"].rate.iloc[0]),
        "improve_rate":float(d[d.action=="improve"].rate.iloc[0]),
        "withdraw_rate":float(d[d.action=="withdraw"].rate.iloc[0]),
        "defend_rate":float(d[d.action=="defend"].rate.iloc[0]),
        "repair_rate":float(d[d.action=="repair"].rate.iloc[0]),
    })
summary=pd.DataFrame(summary)

def probs_for_dims(name,dims):
    ev,*_=SC[name]
    st=apply_event(ev)
    return softmax({a:utility(st,name,a,dims) for a in ACTIONS})

abl_rows=[]
for name in SC:
    full=probs_for_dims(name,("competence","regard","integrity"))
    no_regard=probs_for_dims(name,("competence","integrity"))
    no_integrity=probs_for_dims(name,("competence","regard"))
    for a in ACTIONS:
        abl_rows.append([name,a,full[a],no_regard[a],no_integrity[a]])
abl=pd.DataFrame(abl_rows,columns=["scenario","action","full","no_regard","no_integrity"])

summary.to_csv(OUT/"attachment_emotion_v7_1_summary.csv",index=False)
rates.to_csv(OUT/"attachment_emotion_v7_1_action_rates.csv",index=False)
abl.to_csv(OUT/"attachment_emotion_v7_1_ablations.csv",index=False)
