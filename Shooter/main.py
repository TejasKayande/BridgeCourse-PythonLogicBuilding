# ===============================================================================
# @File:   main.py (Shooter)
# @Brief:  Implementation of a simple shooter game using Pygame
# @Author: Tejas
# @Date:   2026-09-27 Sun
# @Notice: 
# ===============================================================================

# TODO(Tejas):
# - [ ] Add Accuracy and Score
# - [ ] Add a way to increase difficulty over time or based on score
# - [ ] Limit the number of bullets on the screen at a time
# - [ ] Make it so that the player can heal: maybe after some time of not
#       getting hit or maybe by picking up a health kit
# - [ ] Add a camera so that player is alowed to move out of the screen and the
#       camera will follow the player

# NOTE(Tejas): See if you like this OOP pattern...
# I think it makes sense.

import pygame
import math
import random

# NOTE(Tejas): Remember we implemented this in the lecture on OOP. lets use it...
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clip(self, min_x, max_x, min_y, max_y):
        self.x = max(min_x, min(self.x, max_x))
        self.y = max(min_y, min(self.y, max_y))

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        length = self.length()

        if length == 0:
            return Vector2D(0, 0)

        return Vector2D(self.x / length, self.y / length)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

class Player:
    def __init__(self, x, y):
        self.pos = Vector2D(x, y)
        self.direction = Vector2D(0, -1)
        self.velocity = Vector2D(0, 0)
        self.acceleration = 1000.0
        self.max_velocity = 300.0
        self.friction = 800.0

        self.radius = 15

        self.health = 100

    def hit(self):
        self.health -= 10

    def is_dead(self):
        return self.health <= 0

    def apply_friction(self, velocity, dt):
        amount = self.friction * dt

        if velocity > 0:
            return max(0, velocity - amount)

        if velocity < 0:
            return min(0, velocity + amount)

        return 0

    def update_aim(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = Vector2D(mouse_x, mouse_y)

        direction = mouse_pos - self.pos
        self.direction = direction.normalize()

    def update(self, dt):

        # NOTE(Tejas): We can just update the player pos by just the input but
        # it will not look as smooth as it does with all the following code. I
        # think it looks better this way when the player has a bit of momentum.

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.velocity.y -= self.acceleration * dt
        if keys[pygame.K_s]:
            self.velocity.y += self.acceleration * dt
        if keys[pygame.K_a]:
            self.velocity.x -= self.acceleration * dt
        if keys[pygame.K_d]:
            self.velocity.x += self.acceleration * dt

        self.velocity.clip(-self.max_velocity, self.max_velocity, -self.max_velocity, self.max_velocity)

        # NOTE(Tejas): Apply friction
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.velocity.y = self.apply_friction(self.velocity.y, dt)

        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x = self.apply_friction(self.velocity.x, dt)

        self.pos += self.velocity * dt

    def render(self, screen):
        color = (0, 255, 0)
        pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.radius)

class Enemy:
    def __init__(self, x, y):
        self.pos = Vector2D(x, y)
        self.speed = 100.0
        self.radius = 15

    def update(self, player_pos, dt):
        # NOTE(Tejas): The enemy should move towards the player
        direction = player_pos - self.pos
        direction = direction.normalize()

        self.pos += direction * self.speed * dt

    def render(self, screen):
        color = (255, 0, 0)
        pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.radius)

class Bullet:
    def __init__(self, x, y, direction):
        self.pos = Vector2D(x, y)
        self.direction = direction.normalize()
        self.speed = 500.0

        self.radius = 5

        # NOTE(Tejas): we want to destroy bullet after 2 seconds (set it to whatever you want)
        # this is important because we dont want to keep the bullets in memory
        # even if they are off the screen.
        self.lifetime = 2.0

    def is_dead(self):
        return self.lifetime <= 0

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.lifetime -= dt

    def render(self, screen):
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.radius)


class GameManager:
    def __init__(self):
        self.running = True
        self.screen_width = 800
        self.screen_height = 600
        self.fps = 60.0

        # NOTE(Tejas): This is just so we can pass GameManager object around and
        # have functions access to the stuff that it will need. Now we could
        # keep all of this public (thats what I would do) but OOP...
        self.screen = None
        self.clock  = None

        self.game_over = False

        # NOTE(Tejas): game related stuff
        # we dont need to do this here, but we are just making sure that
        # reset_game_state() is called before the game is started.
        self.player  = None
        self.bullets = None
        self.enemies = None
        self.spawn_timer = None
        self.spawn_interval = None

    def reset_game_state(self):
        self.player = Player(400, 500)
        self.bullets = []

        self.enemies = [Enemy(400, 100), Enemy(200, 100), Enemy(600, 100)]
        self.spawn_timer = 0.0
        self.spawn_interval = 1.0

        self.game_over = False


def initialize(game_manager):
    
    pygame.init()
    game_manager.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Shooter Game")
    game_manager.clock = pygame.time.Clock()

    game_manager.reset_game_state()

def check_collision(entity1, entity2):
    # NOTE(Tejas): This only works because all of our entities are circles!
    # Traditionlly we would need to check for collision based on the shape of
    # the entities 
    difference = entity1.pos - entity2.pos
    distance_squared = (difference.x * difference.x + difference.y * difference.y)
    radius = entity1.radius + entity2.radius

    return distance_squared <= radius * radius

def update_game(game_manager, dt):

    # NOTE(Tejas): Spawn enemies at random positions at the top of the screen
    game_manager.spawn_timer += dt

    if game_manager.spawn_timer >= game_manager.spawn_interval:
        game_manager.spawn_timer -= game_manager.spawn_interval

        x = random.randint(0, game_manager.screen_width)
        y = random.randint(0, game_manager.screen_height)

        game_manager.enemies.append(Enemy(x, y))


    game_manager.player.update(dt)
    game_manager.player.update_aim()

    for enemy in game_manager.enemies:
        enemy.update(game_manager.player.pos, dt)

    for bullet in game_manager.bullets:
        bullet.update(dt)


    # NOTE(Tejas): Check for Collisions, and update hit enemies.
    remaining_bullets = []
    remaining_enemies = game_manager.enemies.copy()

    for bullet in game_manager.bullets:
        hit = False

        for enemy in remaining_enemies:
            if check_collision(bullet, enemy):
                remaining_enemies.remove(enemy)
                hit = True
                break

        if not hit:
            remaining_bullets.append(bullet)

    game_manager.bullets = remaining_bullets
    game_manager.enemies = remaining_enemies

    # NOTE(Tejas): Check for collisions between player and enemies
    # TODO(Tejas): There is a very obious BAD thing Im doing here but it
    # works. Can you figure it out? and the reason why it works?
    for enemy in game_manager.enemies:
        if check_collision(game_manager.player, enemy):
            game_manager.player.hit()
            game_manager.enemies.remove(enemy)
            break

    # NOTE(Tejas): Remove dead bullets from the list
    game_manager.bullets = [ bullet for bullet in game_manager.bullets if not bullet.is_dead() ]

    if game_manager.player.is_dead():
        game_manager.game_over = True

def render_game(game_manager):

        game_manager.player.render(game_manager.screen)
        for bullet in game_manager.bullets:
            bullet.render(game_manager.screen)
        for enemy in game_manager.enemies:
            enemy.render(game_manager.screen)

        bar_width, bar_height = 200, 20

        x, y = 20, 20

        # Background
        pygame.draw.rect(game_manager.screen, (60, 60, 60), (x, y, bar_width, bar_height))

        health_width = bar_width * (game_manager.player.health / 100)

        pygame.draw.rect(game_manager.screen, (0, 200, 0), (x, y, health_width, bar_height))
        pygame.draw.rect(game_manager.screen, (255, 255, 255), (x, y, bar_width, bar_height), 2)

def render_ui(game_manager):
    game_manager.screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    text = font.render("Game Over", True, (255, 0, 0))
    restart_text = small_font.render("Hit R to restart the game", True, (255, 255, 255))

    text_rect = text.get_rect(center=(game_manager.screen_width / 2, game_manager.screen_height / 2 - 30))
    restart_rect = restart_text.get_rect(center=(game_manager.screen_width / 2, game_manager.screen_height / 2 + 30))

    game_manager.screen.blit(text, text_rect)
    game_manager.screen.blit(restart_text, restart_rect)

def main():

    game_manager = GameManager()
    initialize(game_manager)

    while game_manager.running:
    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_manager.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_manager.running = False

                elif event.key == pygame.K_r and game_manager.game_over:
                    game_manager.reset_game_state()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game_manager.bullets.append(
                        Bullet(
                            game_manager.player.pos.x,
                            game_manager.player.pos.y,
                            game_manager.player.direction
                        )
                    )

        dt = game_manager.clock.tick(game_manager.fps) / 1000.0

        # NOTE(Tejas): This is a very common pattern in games, you have update()
        # where after processing input from the OS you make changes to your game
        # in Update and after updating all the states in the game, you render
        # them in render()

        update_game(game_manager, dt)

        game_manager.screen.fill((0, 0, 0))

        if not game_manager.game_over:
            render_game(game_manager)
        else:
            render_ui(game_manager)

        pygame.display.flip()

if __name__ == "__main__":
    main()