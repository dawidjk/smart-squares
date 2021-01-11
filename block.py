import pygame
import colors
import pygame.freetype

pygame.freetype.init()

class Block:
    BLOCK_SIZE = 100
    MARGIN = 5
    FONT_SIZE = BLOCK_SIZE / 3
    font = pygame.freetype.Font(
        './droid-sans/DroidSans.ttf', FONT_SIZE)
    
    def __init__(self, val):
        self.val = val
        self.merged = False
    
    def merge(self):
        self.merged = True
        self.val *= 2
    
    def _font_margin_x(self):
        return self.BLOCK_SIZE / (len(str(self.val)) + 1)

    def _font_margin_y(self):
        return self.BLOCK_SIZE * 2 / 5

    def draw(self, screen: pygame.Surface, x: int, y: int):
        pygame.draw.rect(
            screen, colors.BLOCKS[self.val], (x, y, self.BLOCK_SIZE - self.MARGIN, self.BLOCK_SIZE - self.MARGIN))
        
        if self.val:
            color = colors.FONT_DARK

            if self.val > 4:
                color = colors.FONT_LIGHT

            self.font.render_to(
                screen, (x + self._font_margin_x(), y + self._font_margin_y()), str(self.val), color)
