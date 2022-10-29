import pygame
from pygame import mixer
import sys
import random


def main(self):

    self.init()
    mixer.init()
    clock = self.time.Clock()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN = self.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.display.set_caption("DVD Logo Screensaver")

    bg_color = (0, 255, 255)

    chosen_speed = int(random.randint(3, 6))

    initial_speed_x = chosen_speed
    initial_speed_y = chosen_speed

    dvd_logo_image = self.image.load('dvd_logo_transparent.png')
    image_rect = dvd_logo_image.get_rect()

    wall_hit_sound = pygame.mixer.Sound('wall_hit_beep_sound.wav')

    mixer.music.set_volume(1)

    while True:

        for event in self.event.get():
            if event.type == self.QUIT:
                self.quit()
                sys.exit()

        image_rect.x += initial_speed_x
        image_rect.y += initial_speed_y

        if image_rect.top <= 0 or image_rect.bottom >= SCREEN_HEIGHT:
            initial_speed_y *= -1
            pygame.mixer.Sound.play(wall_hit_sound).set_volume(0.15)

        if image_rect.left <= 0 or image_rect.right >= SCREEN_WIDTH:
            initial_speed_x *= -1
            pygame.mixer.Sound.play(wall_hit_sound).set_volume(0.15)

        # visual stuff
        SCREEN.fill(bg_color)
        SCREEN.blit(dvd_logo_image, image_rect)

        self.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main(pygame)
