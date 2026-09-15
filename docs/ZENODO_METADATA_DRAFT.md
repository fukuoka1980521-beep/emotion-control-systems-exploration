# Zenodo登録用メタデータ（公開前ドラフト）

この文書は、Zenodoへ手動登録するときにそのまま転記できるようにしたものです。

## 登録方式

GitHub連携によるsoftware releaseではなく、**研究レポートを主成果物とする手動deposit**を第一候補とします。

理由：このプロジェクトで外部から引用してほしい主成果は、コード単体ではなく、V1〜V8.1の探索系列・失敗・修正・限界をまとめた研究レポートだからです。GitHubはコードと再現性の正本として関連付けます。

## Resource type

**Publication → Technical report / Report**

Zenodo UIで完全に同じ名称がない場合は、Publication系のうち最も近いReportを選ぶ。

## Title

**From Attachment to Emotion-Like Control: An AI-Assisted Exploratory Computational Study of Value, Memory, Prediction Error, Self-Models, and Body-State Feedback**

## Additional / Japanese title

**感情は「執着」から生まれるのか？ — AIシミュレーションで分解した価値・記憶・期待・自己モデル・身体状態**

## Creator

**Shinobu Fukuoka / 福岡 忍**

Affiliation: **Independent Researcher**

ORCID: 未登録なら空欄でよい。

## Publication date

実際にZenodoでPublishする日を使用する。

## Version

**1.0.0**

## Language

**Japanese**

本文は日本語。英語タイトル・英語abstractもメタデータとして併記する。

## Abstract / Description

This AI-assisted exploratory computational study began with the hypothesis that attachment to valued targets may be a primary route to emotion-like behavior. Across V1–V8.1, simple artificial agents were used to separate value, attachment, identity-specific memory, prediction, prediction error, learning/update dynamics, information sampling, self-models, and body-state feedback. Attachment amplified several protective, search, and restoration-related behaviors, but failed to generate jealousy-specific behavior by itself. Actor-directed intervention required identity-specific experience; persistence after an actor reformed depended partly on access to disconfirming evidence; equal objective harm produced different prediction errors depending on prior expectations; damage to different self-model dimensions produced different repair policies; and dynamically generated body states altered later defensive responses. The simulations do not demonstrate subjective feeling or consciousness. They are presented as hypothesis-generating computational experiments, including negative findings, design errors, corrective experiments, and explicit reproducibility limits.

The project was conducted with substantial ChatGPT assistance in hypothesis decomposition, simulation implementation, error detection, literature-search support, analysis, and drafting. Shinobu Fukuoka originated the research question, directed the experimental sequence, required null and failed results to be retained, and is responsible for the published claims and interpretation.

## Keywords

- computational emotion
- affective computing
- reinforcement learning
- appraisal
- attachment
- prediction error
- self-model
- interoception
- emotion-like behavior
- AI-assisted research

## License

レポート本体・図表・研究データ：**Creative Commons Attribution 4.0 International (CC BY 4.0)**

コードはGitHub側で **MIT License**。

## Related identifier

GitHub repository:
https://github.com/fukuoka1980521-beep/emotion-control-systems-exploration

Relation: **is supplemented by / has source code at** に相当する選択肢を使う。

## DOI

既存DOI：**No**

公開前に **Get a DOI now!** でDOIを予約する。

予約されたDOIを最終PDFへ追記してからファイルをアップロード・Publishする。

## Zenodoへ最終的に入れるファイル

1. DOI記載済みの最終PDF v1.0
2. v1.0時点のGitHubソース・検証データの凍結ZIP
3. 必要に応じてREADMEまたはmanifest

Word版は保存用には有用だが、主たる公開ファイルは長期可読性を考えてPDFを優先する。

## 公開前に絶対に確認すること

- DOIがPDF表紙・Zenodoメタデータで一致
- 著者名が Shinobu Fukuoka / 福岡 忍 で一致
- versionが1.0.0で一致
- GitHub URLが正しい
- AI利用開示がPDFとGitHub双方に存在
- V2/V4を再現済みと誤記していない
- 「AIが感情を感じた」「人間感情を証明した」と書いていない
