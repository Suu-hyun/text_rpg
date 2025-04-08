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


    def to_dict(self):
        return self.__dict__ # 클래스(인스턴스)의 내부 상태로 딕셔너리로 변환


    @classmethod
    def from_dict(cls, data):
        return cls(**data) # 언패킹 => 딕셔너리를 키값을 하나하나 빼내서 키값을 넣어주는 것, 'cls(**data)'가 하나의 객체가 되는 것

    def apply_item(self, item):
        self.attack += item["attack"]
        self.max_hp += item["hp"]
        self.max_mp += item["mp"]
        self.cri_luk += item["cri_luk"]
        print(f"<{item["name"]}> \n공격력 +{item["attack"]} => {self.attack}\n최대 HP +{item["hp"]} => {self.max_hp}\n최대 MP +{item["mp"]} => {self.max_mp}\n추가 치명타 확률 +{item["cri_luk"]}% => {self.cri_luk}%")
        print(f"남은 골드:{self.gold}")

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.max_exp:
            left_amount = amount - self.max_exp
            self.level_up(left_amount)

    def level_up(self, amount):
        self.level += 1
        self.attack += 5
        self.max_hp += 10
        self.max_mp += 10
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp += amount
        self.max_exp = int(self.max_exp * 1.5)
        print(f"레벨 업! {self.level} 레벨이 되었습니다! 공격력 + 5, 최대 HP + 10, 최대 MP + 10")

    def mp_recovery(self, mp):
        self.mp = min(self.max_mp, self.mp + mp) # min은 두 인자 중에서 가장 작은 인자를 사용한다.
        print(f"현재 MP:{self.mp}")

    def player_dead(self):
        self.items = []


    """
    인스턴스 메소드 => 우리가 기본적으로 알고 있는 메소드
    스태틱 메소드 => 클래스 내에 유틸성 메소드, 즉 인스턴스나 클래스의 속성에 접근할 수 없음
    클래스 메소드 => 인스턴스를 생성하지 않고 클래스에 직접적으로 접근함
    첫번째 인자로 해당 클래스(기본값) 두번째 인자 데이터로 넣어서 딕셔너리 언패킹
    """


# 몬스터 클래스
class Monster:
    def __init__(self, name, max_hp, attack, exp_reward, gold_reward):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward