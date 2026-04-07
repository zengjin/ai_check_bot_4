import os
SCENE_MAP = {"财务审核": "finance_audit", "人事入职": "hr_onboarding", "通用校验": "default_rules"}
CONFIG_DIR = "config"
class RuleFileManager:
    @staticmethod
    def get_scenes(): return list(SCENE_MAP.keys())
    @staticmethod
    def read_rule(display_name: str) -> str:
        fid = SCENE_MAP.get(display_name, "default_rules")
        path = os.path.join(CONFIG_DIR, f"{fid}.txt")
        if not os.path.exists(path):
            os.makedirs(CONFIG_DIR, exist_ok=True)
            return "请在规则维护页面输入规则。"
        with open(path, 'r', encoding='utf-8') as f: return f.read()
    @staticmethod
    def save_rule(display_name: str, content: str):
        fid = SCENE_MAP.get(display_name, "default_rules")
        os.makedirs(CONFIG_DIR, exist_ok=True)
        path = os.path.join(CONFIG_DIR, f"{fid}.txt")
        with open(path, 'w', encoding='utf-8') as f: f.write(content)