import os.path

from package.models import Player
from package.utils import load_game


def main():
    print("턴제 RPG 게임")
    if os.path.exists("save.json"):
        choice = input("1. 기존 캐릭터 불러오기\n2. 새로 시작하기\n선택:")
        if choice == "1":
            player = load_game()
            if not player:
                print("저장된 캐릭터가 없습니다.")
                return
        else:
            nickname = input("닉네임을 입력해 주세요 : ")
            player = Player(nickname)
    else:
        nickname = input("닉네임을 입력해 주세요 : ")
        player = Player(nickname)

    while True:
        print("\n[메뉴]")
        print("1. 배틀")
        print("2. 상점")
        print("3. 내 아이템 확인")
        print("4. 내 정보 확인")
        print("5. 게임 종료")
        choice = input("선택 : ")

        if choice == "1":
            print("[배틀]")
        elif choice == "2":
            print("\n[상점]")
        elif choice == "3":
            print("\n[내 아이템 확인]")
        elif choice == "4":
            print("\n[내 정보 확인]")
        elif choice == "5":
            print("\n[게임 종료]")
        else:
            print("잘못된 입력입니다")


if __name__ == "__main__": # 다른 파일들을 실행하는게 아닌 불러오는 것이기 때문에 실행할 파일을 정해둠
    main()