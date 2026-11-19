# Paper Writing

使用订阅登录的 Codex，根据实验记录、文献和作者当前 LaTeX 稿件起草或核对实验结果。重建受影响的表格、统计图和 PDF，记录数值、引文和交接依据。

安装整个 `paper-writing` 文件夹后，在 Codex 调用：

```text
$paper-writing 根据实验记录和参考文献撰写实验结果。采用稿是 main.tex，请重建统计图和 PDF。
```

也可将技能目录放在稿件项目的 `.agents/skills/` 下，由 Codex 根据请求选择。[自动触发验收](docs/validation.md#skill-trigger)

- [技能入口](SKILL.md)
- [CVPR 2025 合成示例](examples/cvpr2025/HANDOFF.md)
- [首版规格](docs/skill-v1-spec.md) · [验收记录](docs/validation.md)
- [订阅环境能力](docs/research/p2-host-capabilities.md) · [已有 Skill 复用](docs/research/p3-skill-reuse.md) · [模块边界与交接](docs/research/p4-module-contracts.md)

写作和审阅使用当前订阅会话。示例用 Python、Matplotlib 和 LaTeX 工具链在本地重建。项目流程参考 [PaperOrchestra](https://github.com/google-research/paper-orchestra/tree/d9bae997e793a015ed38bb1605be9eb58c00284f)。
