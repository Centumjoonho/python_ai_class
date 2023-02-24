import pygame

pygame.init()  # 초기화 반드시 필요

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Joonho Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load(
    "C:/Users/leejoonho/Desktop/python_ai_class/pygame/pygame_bg2.png")

# 캐릭터 (스프라이트 불러오기 )
character = pygame.image.load(
    "C:/Users/leejoonho/Desktop/python_ai_class/pygame/pygame_ch2.png")

character_size = character.get_rect().size  # 이미지의 크기
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기

character_x_pos = (screen_width/2) - \
    (character_width/2)  # 화면 가로의 절반 크기에 해당 하는 곳
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳

# 이동할 좌표
to_x = 0
to_y = 0
# 이동 속도
ch_speed = 0.5

# 이벤트 루프
running = True  # 게임이 진행중인가 확인

while running:

    dt = clock.tick(60)  # 게임 화면의 초당 프레임 수를 설정
    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT:  # 창이 딛히는 이벤트가 발생하였는가 ?
            running = False  # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= ch_speed
            elif event.key == pygame.K_RIGHT:
                to_x += ch_speed
            elif event.key == pygame.K_UP:
                to_y -= ch_speed
            elif event.key == pygame.K_DOWN:
                to_y += ch_speed
        if event.type == pygame.KEYUP:  # 방향키르 떼면 멈춰
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계 값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임 화면을 다시 그리기

# pygame  종료
pygame.quit()
