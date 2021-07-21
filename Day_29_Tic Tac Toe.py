import pygame

pygame.init()


win = pygame.display.set_mode((550,550))


pygame.display.set_caption('PyGame Tic-Tac-Toe')

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


first = pygame.draw.rect(win, (255, 255, 255), (25,25,150,150))
second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))
fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))
fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))
seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))
eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))


draw_object = 'circle'

first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

def win_check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True
    

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True
    
    
    for tile in range(3):
        if board[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True

run = True
won = False
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True
                run = True
                won = False
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
                second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
                third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))
                fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))
                fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
                sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))
                seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))
                eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
                ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if won != True:
                if first.collidepoint(pos) and first_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (100,100),50)
                        draw_object = 'rect'
                        board[0][0] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (50,50,100, 100))
                        draw_object = 'circle'
                        board[0][0] = 2

                    first_open = False

                if second.collidepoint(pos) and second_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (275,100),50)
                        draw_object = 'rect'
                        board[0][1] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (225,50,100, 100))
                        draw_object = 'circle'
                        board[0][1] = 2
                    second_open = False

                if third.collidepoint(pos) and third_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (450,100),50)
                        draw_object = 'rect'
                        board[0][2] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (400,50,100, 100))
                        draw_object = 'circle'
                        board[0][2] = 2
                    third_open = False

                if fourth.collidepoint(pos) and fourth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (100,275),50)
                        draw_object = 'rect'
                        board[1][0] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (50,225,100, 100))
                        draw_object = 'circle'
                        board[1][0] = 2
                    fourth_open = False

                if fifth.collidepoint(pos) and fifth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (275,275),50)
                        draw_object = 'rect'
                        board[1][1] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (225,225,100, 100))
                        draw_object = 'circle'
                        board[1][1] = 2
                    fifth_open = False

                if sixth.collidepoint(pos) and sixth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (450,275),50)
                        draw_object = 'rect'
                        board[1][2] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (400,225,100, 100))
                        draw_object = 'circle'
                        board[1][2] = 2
                    sixth_open = False

                if seventh.collidepoint(pos) and seventh_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (100,450),50)
                        draw_object = 'rect'
                        board[2][0] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (50,400,100, 100))
                        draw_object = 'circle'
                        board[2][0] = 2
                    seventh_open = False

                if eighth.collidepoint(pos) and eighth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (275,450),50)
                        draw_object = 'rect'
                        board[2][1] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (225,400,100, 100))
                        draw_object = 'circle'
                        board[2][1] = 2
                    eighth_open = False

                if ninth.collidepoint(pos) and ninth_open:
                    if draw_object == 'circle':
                        pygame.draw.circle(win,(255,0,0), (450,450),50)
                        draw_object = 'rect'
                        board[2][2] = 1
                    else:
                        pygame.draw.rect(win,(0,255,0), (400,400,100, 100))
                        draw_object = 'circle'
                        board[2][2] = 2
                    ninth_open = False
    def displaywon(txt):
        pygame.init()
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        X = 400
        Y = 400
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(txt, True, green, blue)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
        while True:
            display_surface.fill(white)
            display_surface.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    if win_check(1):
        displaywon("Circle won")
        won = True
    elif win_check(2):
        won = True
        displaywon("Rectangle won")
    
    pygame.display.update()
pygame.quit()