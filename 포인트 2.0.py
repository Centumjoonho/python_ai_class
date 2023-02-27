import time

prompt = '''
==================
1. 포인트 조회
2. 포인트 추가
3. 포인트 수정
4. 포인트 사용
5. 포인트 저장
6. 포인트 갱신
    (파일업로드)
7. 회원등록
    (등록포인트:100)
0. 종료
===================
'''

# 변수선언/주화면 보여주기
menu = True
welcome_point = 100
dtPoint = {"01000000000": 100}
dtPoint_copy = dtPoint.copy()
last_add_point = 0
print(prompt)

# menu 선택
while menu != "0":
    menu = input("메뉴를 선택하세요>>  ")
    if menu == "0":
        break

    elif menu == "1":
        if not len(dtPoint):
            print("# 포인트 데이터가 없습니다.", "\n")
            continue
        for tel, get_point in dtPoint.items():
            print(f"{tel} 고객님의 보유 포인트 : {get_point}")

    elif menu == "2":  # 전화번호 알고리즘 - 010-0000-0000 (-) 기호없이
        tel = input(" 전화번호를 입력하세요 :  ")
        if len(tel) >= 10:
            if dtPoint.get(tel) == None:
                print("# 비회원으로 확인되어 회원 등록으로 넘어 갑니다 . ", "\n")
                time.sleep(1)
                if dtPoint.get(tel) == None:
                    dtPoint[tel] = welcome_point
                    print(f"# 회원 등록을 되었습니다. ")
                    print(f"# 등록 축하 포인트 : {dtPoint[tel]}point \n")
                    continue
            else:
                price = int(input(" 주문 금액을 입력하세요 : "))

                newPoint = int(price*0.01)
                last_add_point = newPoint
                dtPoint[tel] = dtPoint.get(
                    tel) + newPoint  # 수정 (기존 포인트에서 업데이트)
                # 가장 마지막에 추가된 포인트만 계속 업데이트 !
                dtPoint_copy.update({tel: newPoint})
                print(
                    f"# {newPoint} point가 추가적립되어 현재 {dtPoint[tel]} point 입니다.", "\n")
        else:
            print("전화번호를 다시 한번 확인해 주세요 ! ")

    elif menu == "3":
        tel = input("  point 수정이 필요한 전화번호를 입력하세요 : ")

        if dtPoint.get(tel):
            print(f"{tel}님이 현재까지 보유중인 point : {dtPoint[tel]} ")
            # 마지막으로 들어가 포인트 -> 수정하는게 맞는 거잖아
            if dtPoint_copy.get(tel) == None:
                print(f" 마지막 추가 point : 0 ")
            else:
                print(f" 마지막 추가 point : {dtPoint_copy.get(tel)} ")
            # 마지막 추가 포인트 : copy -> update
            change_point = int(input("수정할 포인트를 입력해주세요 : "))  # 0 입력 예외 처리
            if change_point > 0:
                dtPoint[tel] = dtPoint.get(
                    tel) - dtPoint_copy.get(tel) + change_point
                print(
                    f"#기존 추가 된 {dtPoint_copy.get(tel)} point 입력하신 {change_point} point 로 수정되었습니다.", "\n")
                dtPoint_copy.update({tel: change_point})
            elif change_point == 0:
                print(f"기존 포인트 {dtPoint.get(tel)} 유지됩니다.")
                pass
            else:
                print("0 이상의 정확한 숫자를 입력하세요")

        else:
            print(f"# {tel}님은 등록되어 있지 않습니다. ", "\n")

    elif menu == "4":
        tel = input("  사용하실 분의 전화번호를 입력하세요 :  ")

        if dtPoint.get(tel):
            print(f"현재 point : {point} point ")
            usePoint = int(input(" 사용하실 point를 적어주세요. :"))
            dtPoint[tel] = point - usePoint
            print(f"# {usePoint} point를 사용하였습니다. ")
            print(f"# {dtPoint[tel]} point가 남아있습니다. ", "\n")
        else:
            print(f"# {tel}님은 등록되어 있지 않습니다. ", "\n")

    elif menu == "5":  # 파일 저장하기
        with open("dodoPoint.txt", "w", encoding="utf8") as f:
            for k, v in dtPoint.items():
                f.write(k+" "+str(v)+"\n")
            print("# 포인트 데이터를 백업(저장)했습니다.!", "\n")

    elif menu == "6":  # 파일 불러오기
        with open("dodoPoint.txt", "r", encoding="utf8") as f:
            while True:
                line = f.readline().replace("\n", "")
                if not line:
                    break
                line = line.split(" ")
                line[1] = int(line[1])
                print(line)
                # 예외처리
                try:
                    dtPoint[line[0]] = line[1]  # 중요!
                except:
                    dtPoint = {line[0]: line[1]}
            print("# 이전 포인트데이터를 가져왔습니다.!", "\n")

    elif menu == "7":  # 동일한 전화 번호가 존재 하면 이미 존재하는 번호라고 고지 하기
        tel = input("전화번호를 입력하세요: ")

        if len(tel) >= 10:
            if dtPoint.get(tel) == None:

                dtPoint[tel] = welcome_point
                print(f"# 회원 등록을 되었습니다. ")
                print(f"# 등록 축하 포인트 : {dtPoint[tel]}point \n")
            else:
                print(f"이미 회원이시네요!! {tel} 회원님의 포인트 : {dtPoint[tel]}")

        else:  # 번호가 인증 되면
            print(f"정확한 연락처를 확인해주세요 : {tel} 잘못 입력하셨습니다.")

    else:
        print("잘못 입력했습니다. 다시 입력해주세요. \n")

print("\n다음에 또 이용해주세요.")
