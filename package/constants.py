# 고유한 값들(아이템들, 몬스터 종류)
from package.models import Monster

monsters = [
    Monster("주황버섯", 30, 5, 30, 20),
    Monster("슬라임", 50, 10, 50, 40),
    Monster("핑크빈", 100, 30, 100, 100),
]

shop_items = [
    {"name": "도란의 검", "attack": 5, "hp":0, "mp": 0, "cri_luk": 0, "price": 50},
    {"name": "롱소드", "attack": 10, "hp":0, "mp": 0, "cri_luk": 0, "price": 80},
    {"name": "민첩성의 망토", "attack": 0, "hp":0, "mp": 0, "cri_luk": 10, "price": 60},
    {"name": "사파이어의 수정", "attack": 0, "hp":30, "mp": 0, "cri_luk": 0, "price": 80},
    {"name": "여신의 눈물", "attack": 0, "hp":0, "mp": 30, "cri_luk": 0, "price": 50},
    {"name": "삼위일체", "attack": 20, "hp":30, "mp": 30, "cri_luk": 20, "price": 333},
]

