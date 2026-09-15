# 再実行・照合ログ

このページには、「昔の結果をそれらしく再現した」ではなく、**保存していた数値と再実行結果を実際に突き合わせた記録**を残します。

## 2026-09-16

再構築したコードを以下の環境で実行しました。

- Python 3.13.5
- NumPy 2.3.5
- pandas 2.2.3

比較対象は、実験時に保存していたCSVです。

GitHub Actions上では、V3.1の一部の値が `0.53275` と `0.5327500000000001` のように、CSV読み込み後の浮動小数点表現の最下位桁だけ異なることが確認されました。これは実験値の差ではなく、IEEE 754浮動小数点表現とCSV round-tripによる差です。

そのため検証は、列・行・文字列を同一としたうえで、数値について `rtol=1e-12`, `atol=1e-12` の機械精度に近い許容幅を使います。これを超える差はFAILとします。

### V3.1 — 怒り様の対人反応（修正版）

- 再構築コード: `experiments/v3_1/reproduce_v3_1.py`
- 保存済み結果: `experiments/v3_1/preserved_summary.csv`
- 判定: **RECONSTRUCTED_AND_VALIDATED**
- 照合結果: 保存済み20行 × 7列と、再実行CSVが機械精度内で一致
- 注意: 元ソースそのものではない。保存されていたV3のfull-precision utility値から線形式を復元し、V3.1で記録された「自然障害から対人行動を除外する」修正を適用した再構築版。

### V5.1 — 改心後の持続と探索

- 再構築コード: `experiments/v5_1/reproduce_v5_1.py`
- 保存済み結果: `experiments/v5_1/preserved_metrics.csv`
- 判定: **RECONSTRUCTED_AND_VALIDATED**
- 照合結果: 保存済み12行 × 8列と、再実行CSVが機械精度内で一致

### V6 — 裏切りと期待誤差

- 再構築コード: `experiments/v6/reproduce_v6.py`
- 保存済み結果: `experiments/v6/preserved_metrics.csv`
- 判定: **RECONSTRUCTED_AND_VALIDATED**
- 照合結果: 保存済み3行 × 10列と、再実行CSVが機械精度内で一致

### V7.1 — 自己モデル損傷

- 再構築コード: `experiments/v7_1/reproduce_v7_1.py`
- 保存済み結果: `experiments/v7_1/preserved_summary.csv`
- 判定: **RECONSTRUCTED_AND_VALIDATED**
- 照合結果: 保存済み5行 × 9列と、再実行CSVが機械精度内で一致

### V8.1 — 身体状態を含む閉ループ

- 再構築コード: `experiments/v8_1/reproduce_v8_1.py`
- 保存済み結果: `experiments/v8_1/preserved_metrics.csv`
- 判定: **RECONSTRUCTED_AND_VALIDATED**
- 照合結果: 保存済み3行 × 12列と、再実行CSVが機械精度内で一致

## V1についての訂正

V1には、エージェント1個体を実行するコアスクリプト `attachment_emotion_experiment.py` が保存されています。

一方、公開レポートの「1000試行平均」を生成した集計ドライバそのものは、現時点で独立した元ファイルとして確認できていません。

したがって、以前の整理でV1を `EXACT_REPRODUCIBLE` としていた表現は強すぎました。V1は当面、

**`CORE_SOURCE_PRESERVED_AGGREGATOR_PENDING`**

として扱います。

元の平均値や個別試行CSVは保存されていますが、1000試行平均を同じ手順で再生成できることを確認するまでは「完全再現済み」とは書きません。

## まだ残っているもの

V2、V4については結果とレポートが残っていますが、元の実行コードを独立した形でまだ検証できていません。

V3、V5、V7、V8は途中版・修正前版として履歴に残します。最終的な主張では、原則として修正版（V3.1、V5.1、V7.1、V8.1）を優先します。

一致しなかった実験を、後から数値を書き換えて「一致したこと」にすることはしません。差が出た場合は、その差自体を記録します。
