import pygame    # сначала установить модуль pygame для проэкта в настройках

#Создание окна игры
pygame.init()    #инициализация (тоесть запущена)

win = pygame.display.set_mode((500,500))   # переменная окна для игры со значением парметром дисплея

#Создали заголовок нашего окна
pygame.display.set_caption("Cubes game")   #заголовок окна

#Загружаем спрайты (картинки)
#анимации бега в право заключенные в список
walkRight = [pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'), pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'), pygame.image.load('pygame_right_6.png')]

#анимации бега в влево заключенные в список
walkLeft = [pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'), pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'), pygame.image.load('pygame_left_6.png')]

bg = pygame.image.load('pygame_bg.jpg')     #задний фон
playerStand = pygame.image.load('pygame_idle.png')    #анимация стояния (исходня)

clock = pygame.time.Clock()

# координаты расположения игрока
x = 50
y = 425             #с 50 изменили на 425 (nr 430 - 5)

#ширина и высота игрока
widht = 60   #ширина
height = 71   #высота

#скорость игрока
speed = 5

#Переменная прыжка
isJump = False
jumpCount = 10

#Для спрайтов (изображений , анимации)
left = False
right = False
animCount = 0
lastMove = "right"

class snaryad():         #снаряды в игре (орудие)
    def __init__(self, x, y, radius, color, fasing):            #конструктор
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = fasing
        self.vel = 8 * fasing

    def draw(self, win):
        pygame.draw.circle(win, self.color,(self.x , self.y), self.radius )


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    # нарисуем нашего игрока через pygame
    #pygame.draw.rect(win, (0,0,255), (x,y,widht,height))        #draw рисует обьект (rect-квадрат :указываем где будет находится,цвет,координта расположения)
    pygame.display.update()       #обновление окна благодаря чему появится игрок

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)


    pygame.display.update()  # обновление окна благодаря чему появится игрок
    # исправляем - удаляем прошлое расположение игрока (чтобы как бы не "рисовалось")


#Теперь создаем циклы (обызательно всегда , для проверки и тд)

run = True

bullets = []
while run:      #while - это цикл "пока" (те пока run = True игра продолжается или аналогично)
    #pygame.time.delay(50)    #метод delay позволяет установить кол-во милисекунд через которое будет выполняться этот цикл
# 100 милисекунд это 0.1 а значит каждую 0.1 секунд этот цикл будет выполнятся , ИЗМЕНИЛИ НА 50

    clock.tick(30)

# Отслеживание отдельных событий (курсора мышки,закрытие приложение или нажатие какой либо клавиши)
#перебираем массив с помощью цикла for , функция get для получения этого массива
    for event in pygame.event.get():         #переменную event можно назвать как угодно
        if event.type == pygame.QUIT:        #окно закроется если нажать на выход
            run = False                      #делается это путем изм значения переменной run

    for bullet in bullets:                 #передвижение и удаление снарядов
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #нарисуем нашего игрока через pygame
    # pygame.draw.rect(win, (0,0,255), (x,y,widht,height))        #draw рисует обьект (rect-квадрат :указываем где будет находится,цвет,координта расположения)
    # pygame.display.update()       #обновление окна благодаря чему появится игрок
    # исправляем - удаляем прошлое расположение игрока (чтобы как бы не "рисовалось")
    # win.fill((0, 0, 0))  # закрашивает прошлые позиции игрока (тела) в черный цвет
    #Передвижения игрока - управление   (ЕСЛИ НАЖИВАТЬ НА КНОПКУ И ЗАДЕРЖИВАТЬ ЕЕ)
    keys = pygame.key.get_pressed()     #список в котором помещаются все кнопки на которые мы будем наживать

    if keys[pygame.K_f]:
        if lastMove == "right":     #куда сейчас смотрит сам пользователь чтобы выстрелить
            fasing = 1
        else:
            fasing = -1

        if len(bullets) < 5:     #вылет и характеристика снаряда каким он должен быть
            bullets.append(snaryad(round(x + widht // 2), round(y + height // 2), 5, (255, 0, 0), fasing))

    if keys[pygame.K_LEFT] and x > 5:      #если наживаем на кнопку стрелка влево , то
        x -= speed               #берем координату x и отнимаем от нее speed тем самым перемещаясь на 5 пикселей влево
        left = True
        right = False
        lastMove = "left"

    elif keys[pygame.K_RIGHT] and x < 500 - widht -5:      #если нажимаем на кнопку стрелка вправо , elif дополнительная проверка
        x += speed
        left = False
        right = True
        lastMove = "right"

    else:                 #Уже 3 проверка начиная с того if
        left = False
        right = False
        animCount = 0
    if not (isJump):      # если мы сейчас не прыгаем
        # if keys[pygame.K_UP] and y > 5:         #кнопка вверх
        #     y -= speed              #он перемещается вверх
        #                                                            Удалил из за того что нереаличто со спрайтами
        # if keys[pygame.K_DOWN] and y < 500 - height -15:       #кнопка вниз      , -15 чтобы было 425 вверху
        #     y += speed

        if keys [pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            if jumpCount < 0:                 #делается чтобы игрок падал
                y += (jumpCount ** 2) / 2          #тут специально - заменили на +
            else:
                y -= (jumpCount ** 2) / 2       #уменьшили большое число поделив на 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()   #вызываем эту функцию





pygame.quit()  #функция quit позволит 100% закрыть приложение (если мы его захотим закрыть)






