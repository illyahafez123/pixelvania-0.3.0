import pygame
import random

pygame.init()

y = 50
x = 50

picture = pygame.image.load("guy1.png")


pygame.display.set_caption("pixelvania version(1.0.0)")
back6 = pygame.transform.scale(pygame.image.load("backno1.png"),(1920, 1840))
inventory_im = pygame.image.load("inventory_ui.png")
tree_im = pygame.transform.scale(pygame.image.load("tree.png"), (142, 250))
wood_im = pygame.transform.scale(pygame.image.load("wood_inventory.png"), (20, 25))

inventory_arr = {"wood":0}


pygame.mixer.init()
pygame.mixer.music.load('a-sinister-power-rising-epic-dark-gothic-soundtrack-15021.mp3')
pygame.mixer.music.play()

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.damage = 5
        self.image = pygame.image.load("guy1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 270
        self.rect.y = 230
        self.wood = 0
    
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x +=8
        if keys[pygame.K_a]:
            self.rect.x -=8
        if keys[pygame.K_w]:
            self.rect.y -=8
        if keys[pygame.K_s]:
            self.rect.y +=8


# класс дерева 
# можна добувати;
# має випадкову прочність та дає випадкову кількість деревини
class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = tree_im
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200
        self.durabillity = random.randint(5, 15)
        self.win = self.durabillity #*5
        
    def extract(self):
        self.durabillity -= 1
        if self.durabillity <= 0:
            hero.wood += self.win
            inventory_arr["wood"] += 1
            wood = Wood()
            woods.add(wood)
            self.kill()
            
# клас деревини
# об'єкти з'являються після того як герой зрубив дерево;
# для того, щоб підійняти, треба дійти до об'єкту
class Wood(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = wood_im
        self.rect = self.image.get_rect()
        self.rect.x = tree.rect.x + 30
        self.rect.y = tree.rect.bottom - 10
        
    def update(self):
        if self.rect.colliderect(hero.rect):
            self.kill()
        
                
tree = Tree()
trees = pygame.sprite.Group()
woods = pygame.sprite.Group()
trees.add(tree)
        
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
back1 = (back6)

backgrounds = [back1]
backcount = 0

blocks = []

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.flip()
hero = Hero()

font = pygame.font.Font(None, 20)
def inventory():
    window.fill((168, 133, 109))
    window.blit(inventory_im, (85, 60))
    if hero.wood > 0:
        window.blit(wood_im, (125, 115))
        text = font.render(str(hero.wood), True, (0, 0, 0))
        window.blit(text, (140, 130))
    
def running():
    window.blit(back6, (0, 0))
    hero.update()
    window.blit(hero.image, (hero.rect.x, hero.rect.y))

    for i in blocks:
        pygame.draw.rect(window, (125, 88, 70), i)
    
    woods.update()    
    trees.draw(window)
    woods.draw(window)
    

game_on = True
run = 1
menu = -1



while game_on:
    clock.tick(64)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                run *= -1
                menu *= -1
        
        
        if event.type == pygame.MOUSEBUTTONDOWN and run == 1:
            x, y = pygame.mouse.get_pos()
            if not tree.rect.collidepoint((x, y)):
                if event.button == 3 and hero.wood > 0:
                    hero.wood -= 1
                    block = pygame.Rect(x, y, 25, 25)
                    blocks.append(block)
                if event.button == 1:
                    for i in blocks:
                        if i.collidepoint((x, y)):
                            hero.wood += 1
                            blocks.remove(i)
            else:
                if event.button == 1 and hero.rect.colliderect(tree.rect):
                    tree.extract()
                        
        
            
    if menu == 1:
        inventory()
    if run == 1:
        running()
            

    pygame.display.update()
    

        
        



