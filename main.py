import pygame
import constants
import assets
import tools
from setup import *

map_len = 30
game_status = True
curr_map = tools.new_map(map_len)
counter = 0 # which object is the user on?
timer = 0 # time in ms from last click
scores = []
avg_score = 0

def change_status():
    global game_status, curr_map, counter, timer, scores, avg_score
    game_status = not game_status
    counter = 0
    timer = 0
    if game_status:
        scores = []
        avg_score = 0
        curr_map = tools.new_map(map_len)

def draw():
    WIN.fill(constants.BLACK)
    if game_status:
        WIN.blit(tools.render_text(f"Average reaction time: {avg_score}ms", FONT_S), (5, 5))
        WIN.blit(assets.CIRCLE, (curr_map[counter][0] - 64, curr_map[counter][1] - 64))
        # blit previous reaction rating at previous location
        if counter > 1:
            render = rating_renders[tools.get_rating(scores[-1])]
            WIN.blit(render, render.get_rect(center = curr_map[counter - 1]))
        elif counter == 0:
            WIN.blit(begin_render, begin_render.get_rect(center = (constants.WIDTH / 2, constants.HEIGHT / 8)))
    else:
        render = rating_renders_large[tools.get_rating(avg_score)]
        render_2 = tools.render_text(f"Average reaction time: {avg_score}ms", FONT_L)
        WIN.blit(render, render.get_rect(center = (constants.WIDTH / 2, constants.HEIGHT / 3)))
        WIN.blit(render_2, render_2.get_rect(center = (constants.WIDTH / 2, constants.HEIGHT / 2)))
        WIN.blit(end_render, end_render.get_rect(center = (constants.WIDTH / 2, constants.HEIGHT * 2/3)))

    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_status:
            pos = pygame.mouse.get_pos()       
            if pygame.mouse.get_pressed() == (1,0,0):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ((pos[0] - curr_map[counter][0])**2 + (pos[1] - curr_map[counter][1])**2)**0.5 <= 64:
                        if counter:
                            scores.append(timer)
                            avg_score = round(sum(scores) / len(scores))
                        timer = 0
                        counter += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_status:
                change_status()

    if counter > map_len - 1:
        change_status()

    draw()

    if game_status:
        timer += 2

pygame.quit()
