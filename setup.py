import pygame
import os
import constants
import assets

pygame.init()
WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
CURSOR_RECT = assets.CURSOR.get_rect()
pygame.display.set_caption('reaction')
pygame.mouse.set_visible(False)
FONT_L = pygame.font.Font(os.path.join('assets', 'FiraCode-Regular.ttf'), 48)
FONT_S = pygame.font.Font(os.path.join('assets', 'FiraCode-Regular.ttf'), 24)
ratings = {
    "Legendary!" : constants.GOLD,
    "Great!" : constants.GREEN,
    "Good" : constants.BLUE,
    "Okay" : constants.PURPLE
    }
rating_renders = [FONT_S.render(i, True, ratings[i]) for i in ratings]
rating_renders_large = [FONT_L.render(i, True, ratings[i]) for i in ratings]
begin_render = FONT_L.render("Click the circle to begin!", True, constants.GOLD)
end_render = FONT_S.render("Press enter to play again", True, constants.GOLD)
