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

    font = pygame.font.Font('freesansbold.ttf', 14)

    bg_color = (0, 0, 0)

    chosen_speed = 5

    random_initial_x_pos = random.randint(0, (SCREEN_WIDTH - 240))
    random_initial_y_pos = random.randint(0, (SCREEN_HEIGHT - 113))

    initial_speed_x = chosen_speed
    initial_speed_y = chosen_speed

    dvd_logo_image = self.image.load('dvd_logo_transparent_white_small.png')
    image_rect = dvd_logo_image.get_rect().move(random_initial_x_pos, random_initial_y_pos)

    wall_hit_sound = pygame.mixer.Sound('wall_hit_beep_sound.wav')

    mixer.music.set_volume(1)

    walls_hit_counter = 0
    corners_hit_counter = 0

    temporary_corner_buffer_counter = 0

    frame_counter_up_to_ten = 0

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
            walls_hit_counter += 1
            temporary_corner_buffer_counter += 1

        elif image_rect.left <= 0 or image_rect.right >= SCREEN_WIDTH:
            initial_speed_x *= -1
            pygame.mixer.Sound.play(wall_hit_sound).set_volume(0.15)
            walls_hit_counter += 1
            temporary_corner_buffer_counter += 1

        if frame_counter_up_to_ten <= 10:

            if temporary_corner_buffer_counter >= 2:
                corners_hit_counter += temporary_corner_buffer_counter % 2
                temporary_corner_buffer_counter = 0

        elif frame_counter_up_to_ten >= 10:
            frame_counter_up_to_ten = 0
            temporary_corner_buffer_counter = 0

        frame_counter_up_to_ten += 1

        # visual stuff
        SCREEN.fill(bg_color)
        SCREEN.blit(dvd_logo_image, image_rect)
        walls_hit_counter_text = font.render(f"Walls hit: {walls_hit_counter}", True,
                                             (255, 255, 255), (0, 0, 0))

        wall_counter_rect = walls_hit_counter_text.get_rect()

        SCREEN.blit(walls_hit_counter_text, wall_counter_rect)

        corners_hit_counter_text = font.render(f"Corners hit: {corners_hit_counter}", True,
                                               (255, 255, 255), (0, 0, 0))

        corner_counter_rect = corners_hit_counter_text.get_rect().move(0, 24)

        SCREEN.blit(corners_hit_counter_text, corner_counter_rect)

        self.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main(pygame)
