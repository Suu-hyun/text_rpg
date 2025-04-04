# 유틸리스성 클래스 관리(저장하기 불러오기)
import json
import os.path

from package.models import Player


def load_game():
    if os.path.exists("./save.json"):
        with open("./save.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return Player.from_dict(data)
    return None

