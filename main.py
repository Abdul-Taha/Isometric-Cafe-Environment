from os import path,listdir
import time
import pygame

scalefactor = 4

for i in listdir(path.dirname(__file__)+"\Assets"):
    if i.endswith('.png'):
        globals()[i.replace('.png','').lower()] = pygame.transform.scale(pygame.image.load(path.dirname(__file__)+"\Assets\\"+i),(486/scalefactor,514/scalefactor))
        



tile_dict = {0:air,1:floor,2:paint,3:playerforward,4:shelf1,5:paint,6:shelf2,7:stool,8:table,9:playerbackward,10:playerleft,11:playerright,12:playeranimright,13:playeranimleft,14:playeranimforward,15:playeranimbackward,16:playerforwardsit,17:playerbackwardsit,18:playerrightsit,19:playerleftsit}
map1 = [[[1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1]],
        [[1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,7,8,7,0,7,8,7,1,0,0,0,0],
         [1,0,0,0,0,0,0,0,1,1,1,1,1],
         [1,7,8,7,0,7,8,7,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,3,0,0],
         [1,7,8,7,0,7,8,7,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,7,0,7,0,7,0,7,0,7,0,7,0],
         [1,8,0,8,0,8,0,8,0,8,0,8,0],
         [1,7,0,7,0,7,0,7,0,7,0,7,0]],
        [[1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,6,0,0,0,0,0,0,0,0,0,0,0],
         [1,4,0,0,0,0,0,0,0,0,0,0,0],
         [2,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,6,0,0,0,0,0,0,0,0,0,0,0],
         [1,6,0,0,0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,0,0,0]]]

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("SITHS Cafe")
frame = pygame.time.Clock()
height = screen.get_height()
width = screen.get_width()

offsetx = 220/scalefactor
offsety = 111/scalefactor
offsetz = 270/scalefactor
strt_x = 700
strt_y = 200
player_pos = [1,4,10]

def draw_map(strt_x,strt_y):
    tile_x = strt_x
    tile_y = strt_y
    for k in range(len(map1)):
        strt_y+=-offsetz
        for i in range(len(map1[k])):
            tile_x = strt_x - offsetx*i
            tile_y = strt_y + offsety*i             
            for j in range(len(map1[k][i])):
                screen.blit(tile_dict[map1[k][i][j]],(tile_x,tile_y))
                tile_x += offsetx
                tile_y += offsety
        


while True:
    draw_map(strt_x,strt_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                map1[player_pos[0]][player_pos[1]][player_pos[2]] = 3
                if player_pos[1]-1 > -1:
                    if map1[player_pos[0]][player_pos[1]-1][player_pos[2]] == 0:
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 14
                        draw_map(strt_x,strt_y)
                        pygame.display.update()
                        time.sleep(0.05)
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 0
                        map1[player_pos[0]][player_pos[1]-1][player_pos[2]] = 3
                        player_pos[1]+=-1
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 3
                        draw_map(strt_x,strt_y)
                        pygame.display.update()

                pygame.event.clear()

            elif event.key == pygame.K_s:
                map1[player_pos[0]][player_pos[1]][player_pos[2]] = 9
                if player_pos[1]+1 < 10:
                    if map1[player_pos[0]][player_pos[1]+1][player_pos[2]] == 0:
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 15
                        draw_map(strt_x,strt_y)
                        pygame.display.update()
                        time.sleep(0.05)
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 0
                        map1[player_pos[0]][player_pos[1]+1][player_pos[2]] = 3
                        player_pos[1]+=1
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 9
                        draw_map(strt_x,strt_y)
                        pygame.display.update()
                pygame.event.clear()

            elif event.key == pygame.K_d:
                map1[player_pos[0]][player_pos[1]][player_pos[2]] = 11
                if player_pos[2]+1 < 13:
                    if map1[player_pos[0]][player_pos[1]][player_pos[2]+1] == 0:
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 12
                        draw_map(strt_x,strt_y)
                        pygame.display.update()
                        time.sleep(0.05)
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 0
                        map1[player_pos[0]][player_pos[1]][player_pos[2]+1] = 3
                        player_pos[2]+=1
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 11
                        draw_map(strt_x,strt_y)
                        pygame.display.update()
                pygame.event.clear()

            elif event.key == pygame.K_a:
                map1[player_pos[0]][player_pos[1]][player_pos[2]] = 10
                if player_pos[2]-1 > -1:
                    if map1[player_pos[0]][player_pos[1]][player_pos[2]-1] == 0:
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 13
                        draw_map(strt_x,strt_y)
                        pygame.display.update()
                        time.sleep(0.05)
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 0
                        map1[player_pos[0]][player_pos[1]][player_pos[2]-1] = 3
                        player_pos[2]+=-1    
                        map1[player_pos[0]][player_pos[1]][player_pos[2]] = 10
                        draw_map(strt_x,strt_y)
                        pygame.display.update()

                pygame.event.clear()
            elif event.key == pygame.K_e:
                if map1[player_pos[0]][player_pos[1]][player_pos[2]] == 10:
                    print('facing left')
                    if player_pos[2]-1 > -1:
                        if map1[player_pos[0]][player_pos[1]][player_pos[2]-1] == 7:
                            print('there is a stool in front of you')
                            if map1[player_pos[0]][player_pos[1]][player_pos[2]-2] == 8:
                                map1[player_pos[0]+1][player_pos[1]][player_pos[2]-1] = 19

                            elif map1[player_pos[0]][player_pos[1]-1][player_pos[2]-1] == 8:
                                map1[player_pos[0]+1][player_pos[1]][player_pos[2]-1] = 16

                            elif map1[player_pos[0]][player_pos[1]+1][player_pos[2]-1] == 8:
                                map1[player_pos[0]][player_pos[1]][player_pos[2]-1] = 17

                elif map1[player_pos[0]][player_pos[1]][player_pos[2]] == 11:
                    print('facing right')
                    if player_pos[2]+1 < 13:
                        if map1[player_pos[0]][player_pos[1]][player_pos[2]+1] == 7:
                            print('there is a stool in front of you')

                elif map1[player_pos[0]][player_pos[1]][player_pos[2]] == 3:
                    print('facing forward')
                    if player_pos[1]-1 > -1:
                        if map1[player_pos[0]][player_pos[1]-1][player_pos[2]] == 7:
                            print('there is a stool in front of you')

                elif map1[player_pos[0]][player_pos[1]][player_pos[2]] == 9:
                    print('facing backward')
                    if player_pos[1]+1 < 10:
                        if map1[player_pos[0]][player_pos[1]+1][player_pos[2]-1] == 7:
                            print('there is a stool in front of you')

    pygame.display.update()
    frame.tick(60)