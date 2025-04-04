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

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


    """
    인스턴스 메소드 => 우리가 기본적으로 알고 있는 메소드
    스태틱 메소드 => 클래스 내에 유틸성 메소드, 즉 인스턴스나 클래스의 속성에 접근할 수 없음
    클래스 메소드 => 인스턴스를 생성하지 않고 클래스에 직접적으로 접근함
    첫번째 인자로 해당 클래스(기본값) 두번째 인자 데이터로 넣어서 딕셔너리 언패킹
    """


# 몬스터 클래스
class Monster:
    def __init__(self, name, hp, attack, exp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward