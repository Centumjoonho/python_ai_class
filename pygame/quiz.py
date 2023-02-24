import pygame
import random
################################################################
# 기본 초기화 (반드시 해야함)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Avoiding poop Game")

# FPS
clock = pygame.time.Clock()
################################################################

# 1. 사용자 게임 초기화 (배경화면 , 게임 이미지 , 좌표 ,속도 , 폰트 등 )
# 배경
background = pygame.image.load(
    "C:\\Users\\leejoonho\\Desktop\\python_ai_class\\pygame\\poop_img\\background.png")

# 캐릭터 만들기
character = pygame.image.load(
    "C:\\Users\\leejoonho\\Desktop\\python_ai_class\\pygame\\pygame_ch2.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
# 이동 위치
to_x = 0
character_speed = 10

# 똥만들기
ddong = pygame.image.load(
    "C:\\Users\\leejoonho\\Desktop\\python_ai_class\\pygame\\poop_img\\dong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트 ,크기 )

# 총 시간
total_time = 30

# 시간 계산
start_ticks = pygame.time.get_ticks()  # 시작 tick 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가 확인

while running:

    dt = clock.tick(30)  # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 프로세스(키보드 ,마우스 등 )
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT:  # 창이 딛히는 이벤트가 발생하였는가 ?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 케릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width
    # 똥 위치 정의
    ddong_y_pos += ddong_speed
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)

    # 4. 충돌 처리
    # 캐릭터
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    # 똥
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    # 타이머 추가
    # 경과시간계산
    elapesed_time = (pygame.time.get_ticks() - start_ticks)/1000
    # 경과 시간 (ms) 을 1000으로 나누어서 초(s) 단위로 표시
    timer = game_font.render(
        str(int(total_time-elapesed_time)), True, (192, 192, 192))
    # 출력할 시간 글자 , True , 글자 색상
    screen.blit(timer, (10, 10))
    # 만약 시간이 0 이하면 게임 종류
    if total_time-elapesed_time <= 0:
        print("end")
        running = False

    pygame.display.update()  # 게임 화면을 다시 그리기

pygame.time.delay(2000)  # 2초 대기
# pygame  종료
pygame.quit()
