import pygame
from tower import Tower
from soldier import Soldier

def main():
    pygame.init()
    # initial setups
    WIDTH, HEIGHT = 1200, 500
    FPS = 60
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Game")
    ROTATE = True  # right team
    NO_ROTATE = False  # left team

    # basic colors rgb black white
    WHITE = (255, 255, 255)

    run = True
    clock = pygame.time.Clock()

    left_group = pygame.sprite.Group()
    right_group = pygame.sprite.Group()

    all_left = []
    all_right = []

    left_tower = Tower(NO_ROTATE, WINDOW)
    right_tower = Tower(ROTATE, WINDOW)

    right_group.add(right_tower)
    left_group.add(left_tower)
    all_right.append(right_tower)
    all_left.append(left_tower)

    while run:
        clock.tick(FPS)
        WINDOW.fill(WHITE)
        #pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_1:  # summon left side soldier
                    left_soldier = Soldier(NO_ROTATE, WINDOW)
                    left_group.add(left_soldier)
                    all_left.append(left_soldier)

                if event.key == pygame.K_LEFT:  # summon right side soldier
                    right_soldier = Soldier(ROTATE, WINDOW)
                    right_group.add(right_soldier)
                    all_right.append(right_soldier)
                
                if event.key == pygame.K_r:
                    main()

        # draw_window(left_group, right_group)


        for entity in all_left:
            entity.summon()
            if entity.type == "soldier":
                entity.collision_detector(right_group)
                if entity.collide == False:
                    entity.move()
                elif entity.collide == True:
                    entity.stop()
                    entity.attack(right_group, all_right)
               
            
        for entity in all_right:
            entity.summon()
            if entity.type == "soldier":
                entity.collision_detector(left_group)
                if entity.collide == False:
                    entity.move()
                elif entity.collide == True:
                    entity.stop()
                    entity.attack(left_group, all_left)
                       
                            
        
        
        pygame.display.update()


if __name__ == "__main__":
    main()