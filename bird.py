import pygame,sys,random,math
screen_height=1000
screen_width=700
pygame.init()
screen= pygame.display.set_mode((screen_height,screen_width))
clock = pygame.time.Clock()

class bird():
    def __init__(bird,x,y,vx,vy):
        bird.x=x
        bird.y=y
        bird.vx=vx
        bird.vy=vy
        bird.ax=0
        bird.ay=0

birds=[]
count_bird=0
distance = 2000
random_list=[0,1,2,3,4,5,6,7,8,9,10]
random_lists=[-1,1]
points=[]

def draw_bird ():
    global birds
    global points

    for bird in birds :
        a_x=min(bird.x,screen_height-bird.x)
        a_y=min(bird.y,screen_width-bird.y)
        a_x=0.5/a_x
        a_y=0.5/a_y
        if bird.x>screen_height/2 :
           a_x=a_x*(-1)
        if bird.y>screen_width/2 :
           a_y=a_y*(-1)
        bird.vx=bird.vx+bird.ax+a_x
        bird.vy=bird.vy+bird.ay+a_y
        len=bird.vx*bird.vx+bird.vy*bird.vy
        len=math.sqrt(len)

        if len==0 : 
            len=1

        bird.vx=bird.vx/len
        bird.vy=bird.vy/len

        bird.x=bird.x+bird.vx
        bird.y=bird.y+bird.vy

        points.append((bird.x,bird.y))
    
    count =0 
    wide=1
    x_color=250

    for point in points :
        count +=1
        color = (x_color,200,200)
        pygame.draw.circle(screen,color,(point[0],point[1]),wide)
        if count % count_bird ==0 :
            wide+=0.005
            x_color-=1

    for point in points :
        if count > 200*count_bird :
           points.remove(point)
           count-=1

def update_bird():
    new_birds = []
    global birds
    global distance
    for bird1 in birds :
        sum_x=0
        sum_y=0
        count=0
        for bird2 in birds :
            x=bird2.x-bird1.x
            y=bird2.y-bird1.y
            bird_distance=x*x+y*y
            if bird1.vx*x + bird1.vy*y >=0 and bird_distance <= distance :
                sum_x+=bird2.vx
                sum_y+=bird2.vy
                count+=1
        sum_x/=count
        sum_y/=count

        sum_x=sum_x-bird1.vx
        sum_y=sum_y-bird1.vy
        
        ko=sum_x*sum_x+sum_y*sum_y
        ko=math.sqrt(ko)

        if ko==0 :
            ko=5

        new_bird=bird1

        new_bird.ax=sum_x/5*ko
        new_bird.ay=sum_y/5*ko

        new_birds.append(new_bird)

    birds=new_birds 

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            vx=random.choice(random_list)/10
            vy=math.sqrt(1-vx*vx)
            vx*=random.choice(random_lists)
            vy*=random.choice(random_lists)
            birds.append(bird(x,y,vx,vy))
            count_bird +=1

    update_bird()
    screen.fill("black")
    draw_bird()

    pygame.display.update()   
    clock.tick(200)