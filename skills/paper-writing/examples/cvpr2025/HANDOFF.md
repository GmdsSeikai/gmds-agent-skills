# CVPR 2025 合成示例

采用稿是 [main.tex](main.tex)，实验结果在 [results.tex](results.tex)，文献在 [references.bib](references.bib)。本例用手工构造的数值演示从实验材料写入会议模板的过程，稿件正文标明数据为合成数据。

## 重建

在本目录执行。需要 Python 和 Matplotlib，以及含 CVPR 所需宏包的 TeX Live 或兼容发行版。使用 CVPR 2025 官方作者包 `CVPR2025-v3(latex)` 的页面布局与 BibTeX 样式。本项目保存适配后的稿件，构建前获取并校验原样的 `cvpr.sty` 和 `ieeenat_fullname.bst`。首次获取需要联网，后续可复用工作目录里的两个文件。[官方发布](https://github.com/cvpr-org/author-kit/releases/tag/CVPR2025-v3%28latex%29) · [固定版本](https://github.com/cvpr-org/author-kit/tree/1ce836777851be0386e3d3868e9cc6b3ca8b4d48)

实测环境为 Windows、Python 3.9.13、Matplotlib 3.5.2、TeX Live 2026（pdfTeX 1.40.29、BibTeX 0.99e）。便携 TinyTeX-1 v2026.11 补齐了 `silence`、`caption`、`enumitem`、`cleveref` 和 `grfext`。

```text
python -B fetch_template.py
python -B render.py
pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode -output-directory=build main.tex
bibtex build/main
pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode -output-directory=build main.tex
pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode -output-directory=build main.tex
```

每条命令成功后再执行下一条。论文为 `build/main.pdf`，图 1 为 `build/latency.pdf`。重建后检查 `build/main.log` 和 `build/main.blg`，打开 PDF 核对正文、图表和引用。可编辑稿件由 `main.tex`、`results.tex` 和 `references.bib` 组成，`build/metrics.tex` 随图重建。

## 证据与受影响位置

[实验说明](materials/experiment.md)定义样本和统计范围。[latency.csv](materials/latency.csv) 是唯一数值输入，每个样本的单位是 ms/图。[render.py](render.py) 按组计算算术平均值（组内数值之和除以组内样本数），并用同一批观测为图画出均值条和样本点。TeX 值显示至多两位小数，绘图使用未舍入的均值。

| 指标 | 样本 ID | 初始值 | 稿件位置 |
| --- | --- | --- | --- |
| Sequential 均值 | S01–S05 | 40 ms | 摘要、结果段、结果表、图 1 与图注 |
| Batched 均值 | B01–B05 | 30 ms | 摘要、结果段、结果表、图 1 与图注 |
| Reference 均值 | R01–R05 | 30 ms | 结果段、结果表、图 1 与图注 |
| Sequential 减 Batched | 以上两组均值相减 | 10 ms | 结果段 |

图 1 对应 `results.tex` 的 `fig:latency`，结果表对应 `tab:latency`。更正时按样本 ID 修改 CSV，再重建图和稿件。检查结果段里的比较和范围说明是否仍和数字一致。

`dean2013tail` 支持结果节首句关于延迟波动与交互服务响应的论述。作者公开全文第 74 页开篇讨论规模和利用率上升时维持低尾延迟的困难，以及偶发高延迟对服务性能的影响。Google Research 题录和全文核对了作者、题名、刊名、卷期页码及 DOI。样例的数字来自合成 CSV。[题录](https://research.google/pubs/the-tail-at-scale/) · [作者公开全文](https://barroso.org/publications/TheTailAtScale.pdf)
