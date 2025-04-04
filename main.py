import os.path


def main():
    print("턴제 RPG 게임")
    if os.path.exists("save.json"):
        choice = input("1. 기존 캐릭터 불러오기\n2. 새로 시작하기\n선택:")
        if choice == "1":
            pass # 저장 파일 불러오기
        else:
            nickname = input("닉네임을 입력해 주세요 : ")

if __name__ == "__main__": # 다른 파일들을 실행하는게 아닌 불러오는 것이기 때문에 실행할 파일을 정해둠
    main()