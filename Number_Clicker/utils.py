import random
from number_object import NumberObject

# 数字の生成と配置
def generate_numbers(number_objects):
    for number in range(1, 21):
        while True:
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            overlap = False
            for obj in number_objects:
                distance = ((obj.x - x) ** 2 + (obj.y - y) ** 2) ** 0.5
                if distance <= 40:
                    overlap = True
                    break
            if not overlap:
                number_objects.append(NumberObject(number, x, y))
                break
