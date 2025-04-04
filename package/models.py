# 플레이어의 클래스

class Player:
    def __init__(self, nickname, level=1, gold=0, attack=10, exp=0, max_exp=100, hp=100, max_hp=100, mp=50, max_mp=50, cri_luk=0, skills=None, items=None):
        self.nickname = nickname
        self.level = level
        self.gold = gold
        self.attack = attack
        self.exp = exp
        self.max_exp = max_exp
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.cri_luk = cri_luk
        self.skills = skills if skills else [
            {"name": "달팽이 세마리", "mp_cost": 10, "damage_multiple": 1.2},
            {"name": "달팽이 네마리", "mp_cost": 18, "damage_multiple": 1.5},
            {"name": "달팽이 다섯마리", "mp_cost": 23, "damage_multiple": 1.8}
        ]
        self.items = items if items else []


# 몬스터 클래스
class Monster:
    def __init__(self, name, hp, attack, exp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward