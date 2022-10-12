import pygame
import random
pygame.init()


def game_loop():
    #win = 0
    turn = 0
    display_width = 800
    display_height = 600
    color1 = (255,248,56)
    color2 = (255	,231,158,255)
    color3 = (0,0,0)

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Test Game")
    clock = pygame.time.Clock()
    gameDisplay.fill(color1)
    
    number_0 = pygame.image.load("0.png")
    number_1 = pygame.image.load("1.png")
    number_2 = pygame.image.load("2.png")
    number_3 = pygame.image.load("3.png")
    number_4 = pygame.image.load("4.png")
    number_5 = pygame.image.load("5.png")
    number_6 = pygame.image.load("6.png")
    number_7 = pygame.image.load("7.png")
    number_8 = pygame.image.load("8.png")
    number_9 = pygame.image.load("9.png")
    carpi_ = pygame.image.load("carpi.png")
    listt = [number_0,number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9]
    
    tr_rand = random.randint(0,3)
    w1  = -30 
    w2  = 150 
    w3  = 340 
    w4  = 520
    w_list = [w1,w2,w3,w4]
    truew = w_list[tr_rand]
    
    
    def number_generator():
        if turn == 0 :
            
                    
            x = random.randint(0,9)
            y = random.randint(0,9)
                
            first_num = pygame.transform.scale(listt[x],(300,300))
            second_num = pygame.transform.scale(listt[y],(300,300))
            carpi = pygame.transform.scale(carpi_,(200,200))
            gameDisplay.blit(first_num,(80,50))
            gameDisplay.blit(carpi,(290,90))
            gameDisplay.blit(second_num,(400,50))
            
            true_ans = y * x
            
            true_list = list(str(true_ans))
            first_dig = pygame.transform.scale(listt[int(true_list[0])],(240,240))
            if len(true_list) == 1:
                gameDisplay.blit(first_dig,(truew + 40,350))
            elif len(true_list) == 2:
                second_dig = pygame.transform.scale(listt[int(true_list[1])],(240,240))
                gameDisplay.blit(first_dig,(truew,350))
                gameDisplay.blit(second_dig,(truew + 80,350))
                
            w_list.remove(w_list[tr_rand])
            
            tr2_rand = random.randint(0,2)
            x_wr1 = random.randint(2,9)
            y_wr1 = random.randint(2,9)
            wrong1 = x_wr1 * y_wr1
            while wrong1 == true_ans:
                x_wr1 = random.randint(2,9)
                y_wr1 = random.randint(2,9)
                wrong1 = x_wr1 * y_wr1
            wrong_1 = list(str(wrong1))
            w_first_dig = pygame.transform.scale(listt[int(wrong_1[0])],(240,240))
            if len(wrong_1) == 1:
                gameDisplay.blit(w_first_dig,(w_list[tr2_rand] + 30,350))
            elif len(wrong_1) == 2:
                w_second_dig = pygame.transform.scale(listt[int(wrong_1[1])],(240,240))
                gameDisplay.blit(w_first_dig,(w_list[tr2_rand],350))
                gameDisplay.blit(w_second_dig,(w_list[tr2_rand] + 80,350))
                
            w_list.remove(w_list[tr2_rand])
            tr3_rand = random.randint(0,1)
            
            x_wr2 = random.randint(2,9)
            y_wr2 = random.randint(2,9)
            wrong2 = x_wr2 * y_wr2
            
            while wrong2 == true_ans or wrong2 == wrong1:
                x_wr2 = random.randint(2,9)
                y_wr2 = random.randint(2,9)
                wrong2 = x_wr2 * y_wr2
            wrong_2 = list(str(wrong2))
            w2_first_dig = pygame.transform.scale(listt[int(wrong_2[0])],(240,240))
            if len(wrong_2) == 1:
                gameDisplay.blit(w2_first_dig,(w_list[tr3_rand] + 40,350))
            elif len(wrong_2) == 2:
                w2_second_dig = pygame.transform.scale(listt[int(wrong_2[1])],(240,240))
                gameDisplay.blit(w2_first_dig,(w_list[tr3_rand],350))
                gameDisplay.blit(w2_second_dig,(w_list[tr3_rand] + 80,350))
                
            w_list.remove(w_list[tr3_rand])
            tr4_rand = w_list[0]
            
            x_wr3 = random.randint(2,9)
            y_wr3 = random.randint(2,9)
            wrong3 = x_wr3 * y_wr3
            
            while wrong3 == true_ans or wrong3 == wrong1 or wrong3 == wrong2:
                x_wr3 = random.randint(2,9)
                y_wr3 = random.randint(2,9)
                wrong3 = x_wr3 * y_wr3
            wrong_3 = list(str(wrong3))
            w3_first_dig = pygame.transform.scale(listt[int(wrong_3[0])],(240,240))
            if len(wrong_3) == 1:
                gameDisplay.blit(w3_first_dig,(tr4_rand + 40,350))
            elif len(wrong_3) == 2:
                w3_second_dig = pygame.transform.scale(listt[int(wrong_3[1])],(240,240))
                gameDisplay.blit(w3_first_dig,(tr4_rand,350))
                gameDisplay.blit(w3_second_dig,(tr4_rand + 80,350))
                
            
            
    
            

    lost = False
    while not lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lost = True
                
            
        mouse = pygame.mouse.get_pos()
        
        if 226 < mouse[0] < 393 and 370 < mouse[1] < 524:
            pygame.draw.rect(gameDisplay,color2,(226,375,168,150),10)
        elif 32 < mouse[0] < 213 and 370 < mouse[1] < 524:
            pygame.draw.rect(gameDisplay,color2,(40,375,168,150),10)
        elif 406 < mouse[0] < 584 and 370 < mouse[1] < 524:
            pygame.draw.rect(gameDisplay,color2,(413,375,168,150),10)
        elif 597 < mouse[0] < 758 and 370 < mouse[1] < 524:
            pygame.draw.rect(gameDisplay,color2,(600,375,168,150),10)
            
        else:
            pygame.draw.rect(gameDisplay,color3,(40,375,168,150),15)
            pygame.draw.rect(gameDisplay,color3,(226,375,168,150),15)
            pygame.draw.rect(gameDisplay,color3,(413,375,168,150),15)
            pygame.draw.rect(gameDisplay,color3,(600,375,168,150),15)
            
        if truew + 80 < mouse[0] < truew + 255 and 370 < mouse[1] < 524:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #turn = 0
                #win += 1
                game_loop()
                
                
            
        #print(mouse)
        number_generator()        
        pygame.display.update()
        clock.tick(60)
        turn += 1

game_loop()       
pygame.quit()
