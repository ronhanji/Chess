import pygame

def draw_text(surf, text, size, x, y, font, color=(0,0,0)):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    surf.blit(text_surface, text_rect)

def zero_checker(x):
    if x<10:
        return '0'+str(x)
    else:
        return str(x)

class Timer():
    def __init__(self,pos,font_size,start,font=pygame.font.match_font("Arial"),text_color=(255,255,255)):
        self.x,self.y=pos
        self.font_size=font_size
        self.font=font
        self.time=start
        self.text_color=text_color

    def update(self):
        self.time-=1


    def draw(self,screen):
        if self.time >=3600:
            hours=self.time//(60**2)
            minutes=(self.time-hours*3600)//60
            seconds=self.time-minutes*60-hours*(60**2)
            time=zero_checker(hours)+':'+zero_checker(minutes)+':'+zero_checker(seconds)
        else:
            minutes=self.time//60
            seconds=self.time-minutes*60
            time=zero_checker(minutes)+':'+zero_checker(seconds)
        draw_text(screen,time,self.font_size,self.x,self.y,self.font,self.text_color)
