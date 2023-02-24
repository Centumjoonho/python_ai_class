# 20201003_기술체크
# data = 전화번호, 금액, 포인트
# 1회당 금액의 10%씩 포인트 적립
# 도도포인트 ==> 글로벌 해짐!

import telnetlib


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

dtPoint = {"01000000000": 100}

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
        for tel, point in dtPoint.items():
            print(f"{tel} {point}")

    elif menu == "2":  # 전화번호 알고리즘 - 010-0000-0000 (-) 기호없이
        tel = input(" 전화번호를 입력하세요 :  ")
        if not len(dtPoint):
            print("# 회원등록을 해주세요. ", "\n")
        else:
            price = int(input(" 주문 금액을 입력하세요 : "))
            newPoint = int(price*0.1)
            dtPoint[tel] = point + newPoint  # 수정 (기존 포인트에서 업데이트)
            print(
                f"# {newPoint} point가 추가적립되어 현재 {dtPoint[tel]} point 입니다.", "\n")

    elif menu == "3":
        tel = input("  포인트 수정이 필요한 전화번호를 입력하세요 : ")

        if dtPoint.get(tel):
            point = int(input("  최종포인트를 입력해주세요 : "))
            dtPoint[tel] = point
            print(f"# {point} point 로 수정되었습니다.", "\n")
        else:
            print(f"# {tel}님은 등록되어 있지 않습니다. ", "\n")

    elif menu == "4":
        tel = input("  사용하실 분의 전화번호를 입력하세요 :  ")

        if dtPoint.get(tel):
            print(f"현재 point : {point} point ")
            usePoint = int(input(" 사용하실 포인트를 적어주세요. :"))
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
        dtPoint_copy = dtPoint.copy()
        print(dtPoint_copy)
        tel = input("  전화번호를 입력하세요: ")
        point = 100
        if len(tel) < 11 and len(tel) > 10:
            print(f"정확한 연락처를 확인해주세요 : {tel} 잘못 입력하셨습니다.")
        else:  # 번호가 인증 되면
            print(dtPoint_copy)
            for k, v in dtPoint_copy.items():
                print(f"check {k} , {v}")
                if tel in k:
                    print(f"# 이미 우리 회원이시네요 ! 현재 포인트는 {dtPoint[k]} ")
                    break
                else:
                    dtPoint[tel] = point
                    print(f"# 회원 등록을 되었습니다. ")
                    print(f"# 등록 축하 포인트 : {dtPoint[tel]}point \n")

    else:
        print("잘못 입력했습니다. 다시 입력해주세요. \n")

print("\n다음에 또 이용해주세요.")
