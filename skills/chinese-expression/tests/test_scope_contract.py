"""Pin the skill's factual and engineering boundaries against accidental removal."""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote


SKILL_ROOT = Path(__file__).resolve().parents[1]
SKILL_TEXT = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")


class ScopeContractTests(unittest.TestCase):
    def test_engineering_requirements_remain_owned_by_engineering(self):
        self.assertIn(
            "本技能只调整表达，不得据此跳过检查、减少必要测试、弱化权限边界或隐去失败、风险和未验证事项。",
            SKILL_TEXT,
        )

    def test_no_invented_facts_or_changed_claim_strength(self):
        self.assertIn(
            "正文不得新增材料没有的事实、数字、引文、经历或承诺，也不得改变作者有依据的主张强度。",
            SKILL_TEXT,
        )

    def test_real_uncertainty_and_conditions_survive(self):
        self.assertIn(
            "保留会影响理解或行动的真实条件、风险、失败和未验证事项，写在对应主张旁；真实不确定性照实表达。",
            SKILL_TEXT,
        )

    def test_runtime_references_are_self_contained(self):
        documents = [SKILL_ROOT / "SKILL.md", *SKILL_ROOT.glob("references/*.md")]
        for document in documents:
            text = re.sub(r"`[^`\n]*`", "", document.read_text(encoding="utf-8"))
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith(("#", "https:", "http:", "mailto:")):
                    continue
                resolved = (document.parent / unquote(target.split("#", 1)[0])).resolve()
                with self.subTest(document=document.name, target=target):
                    resolved.relative_to(SKILL_ROOT.resolve())
                    self.assertTrue(resolved.is_file(), str(resolved))


if __name__ == "__main__":
    unittest.main()
