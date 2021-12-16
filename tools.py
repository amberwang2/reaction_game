import random
import constants

def new_map(n):
    points = [(random.randint(150, 1130), random.randint(150, 570))]

    for i in range(n - 1):
        temp = True
        while temp:
            point = (random.randint(150, 1130), random.randint(150, 570))
            dist = ((point[0] - points[-1][0])**2 + (point[1] - points[-1][1])**2)**0.5
            if dist > 400 and dist < 600:
                points.append(point)
                temp = False

    return points

def render_text(text, font):
    return font.render(text, True, constants.WHITE)

def get_rating(score):
    if score < 250:
        return 0
    elif score < 350:
        return 1
    elif score < 600:
        return 2
    else:
        return 3
