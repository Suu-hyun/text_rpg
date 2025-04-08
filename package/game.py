import random
import time

from package.constants import shop_items

def basic_atk(player): # 기본공격
    if random.randint(1, 100) <= player.cri_luk: # 1, 100까지 퍼센트 메커니즘을 넣은 것
        damage = player.attack * 2
        print("치명타!!!")
    else:
        damage = player.attack
    print(f"{player.nickname}의 기본공격!!, {damage}!")
    return damage

def skill_attack(player):
    print("사용 가능한 스킬")
    for idx, skill in enumerate(player.skills):
        print(f"{idx + 1}. {skill["name"]} (MP소모:{skill["mp_cost"]}, 데미지 배수:{skill["damage_multiple"]})")
    skill_choice = int(input("사용할 스킬을 선택해주세요:")) - 1

    if 0 <= skill_choice < len(player.skills):
        skill = player.skills[skill_choice]
        if player.mp >= skill["mp_cost"]:
            player.mp -= skill["mp_cost"]
            damage = int(player.attack * skill["damage_multiple"])
            print(f"{player.nickname}가 {skill["name"]}을 시전하였습니다. {damage} 데미지!")
            return damage
        else:
            print("MP가 부족합니다. 기본 공격을 수행합니다.")
            return basic_atk(player)
    else:
        print("잘못된 입력입니다. 기본 공격을 수행합니다.")
        return basic_atk(player)

def player_turn(player):
    print("행동을 선택하세요")
    print("1. 기본 공격")
    print("2. 스킬 사용")
    action = input("선택:")

    if action == "1":
        return basic_atk(player)
    elif action == "2":
        return skill_attack(player)
    else:
        print("잘못된 입력입니다. 기본 공격을 수행합니다.")
        return basic_atk(player)



def battle(player, monster):
    print(f"{player.nickname} vs {monster.name}")
    while player.hp > 0 and monster.hp > 0: # 둘 중 하나가 죽어야 while이 끝나기 때문에
        print(f"[{player.nickname} HP:{player.hp}, MP{player.mp}] vs [{monster.name} HP{monster.hp}]")

        # 플레이어 턴
        damage = player_turn(player)
        monster.hp -= damage
        time.sleep(2)

        if monster.hp <= 0:
            print(f"{monster.name}을 처치했습니다.")
            exp_reward_multiple = random.uniform(0.9,1.1)
            gold_reward_multiple = random.uniform(0.9, 1.1)
            exp_reward = int(monster.exp_reward * exp_reward_multiple)
            gold_reward = int(monster.gold_reward * gold_reward_multiple)
            player.gain_exp(exp_reward)
            player.gold += gold_reward
            print(f"경험치-{exp_reward}, 골드-{gold_reward} 획득!")

            #몬스터의 데이터와 플레이어의 데이터 초기화
            monster.hp = monster.max_hp
            player.hp = player.max_hp
            player.mp = player.max_mp
            break

        #몬스터의 턴
        player.hp -= monster.attack
        print(f"{monster.name}의 반격! {monster.attack} 데미지!")
        time.sleep(2)

        mp_recovery_amount = 5
        player.mp_recovery(mp_recovery_amount)

        if player.hp <= 0:
            print("패배했습니다. 게임 오버!")
            player.player_dead()
            break


def shop(player):
    print("\n[상점]")
    print(f"\n보유골드: {player.gold}")
    for idx, item in enumerate(shop_items):
        print(f"{idx + 1}. {item["name"]} (추가 공격력: {item["attack"]}, 추가 HP: {item["hp"]}, 추가 치명타 확률: {item["cri_luk"]}, 가격: {item["price"]}")
    choice = int(input("구매할 아이템 번호를 입력해주세요(취소: 0):"))-1
    if 0 <= choice <len(shop_items):
        item = shop_items[choice]
        if player.gold >= item["price"]:
            player.gold -= item["price"]
            player.items.append(item)
            player.apply_item(item)
            print(f"{item["name"]}을/를 구매했습니다!")
        else:
            print("골드가 부족합니다.")
    elif choice == -1:
        print("구매를 취소했습니다.")
    else:
        print("잘못된 입력입니다.")