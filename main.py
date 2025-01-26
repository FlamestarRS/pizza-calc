import pygame
from constants import *
from pizza import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Pizza Time")

    first_pizza = Pizza(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    second_pizza = Pizza(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    third_pizza = Pizza(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    first_area = first_pizza.area(float(input("How big is the first pizza?")))
    print(first_area)

    second_area = second_pizza.area(float(input("How big is the second pizza?")))
    print(second_area)

    difference = round(first_area - second_area, 2)
    third_area = round(third_pizza.diameter(difference), 2)

    print(f"The first pizza is {difference} square inches bigger than the second pizza")
    print(f"This is equivalent to another {third_area} inch pizza")


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))




if __name__ == "__main__":
    main()