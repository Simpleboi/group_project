import pygame
import random
import time

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
FPS = 60
DICE_SIZE = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dice Game")

def draw_dice(value, x, y):
    pygame.draw.rect(screen, WHITE, (x, y, DICE_SIZE, DICE_SIZE))
    dice_font = pygame.font.Font(None, 36)
    text_surface = dice_font.render(str(value), True, BLACK)
    text_rect = text_surface.get_rect(center=(x + DICE_SIZE // 2, y + DICE_SIZE // 2))
    screen.blit(text_surface, text_rect)

def roll_dice():
    return random.randint(1, 6)

def display_winner(winner):
    winner_text = pygame.font.Font(None, 48).render(f"{winner} won!", True, WHITE)
    screen.blit(winner_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)

def main():
    player_score = 0
    opponent_scores = [0, 0, 0]
    dice_values = [0, 0, 0, 0]

    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Player's turn
                    player_roll = roll_dice()
                    player_score += player_roll
                    print(f"Player rolled: {player_roll}. Player score: {player_score}")

                    # Opponents' turns
                    for i in range(3):
                        opponent_scores[i] += roll_dice()

                    # Display all dice values together
                    dice_values = [player_roll] + [roll_dice() for _ in range(3)]

                    # Check for a winner
                    if player_score >= 50 or max(opponent_scores) >= 50:
                        if player_score >= 50:
                            display_winner("Player")
                        else:
                            display_winner("Opponent")
                        player_score = 0
                        opponent_scores = [0, 0, 0]

        # Draw dice and scores on the screen
        for i, value in enumerate(dice_values):
            draw_dice(value, 50 + i * 120, 200)

        # Display player score and opponent scores on the screen
        player_score_text = pygame.font.Font(None, 36).render(f"Player Score: {player_score}", True, WHITE)
        screen.blit(player_score_text, (20, 20))

        for i, score in enumerate(opponent_scores):
            opponent_score_text = pygame.font.Font(None, 36).render(f"Opponent {i+1} Score: {score}", True, WHITE)
            screen.blit(opponent_score_text, (20, 60 + i * 30))

        # Game over message and play again prompt
        if player_score >= 50 or max(opponent_scores) >= 50:
            game_over_text = pygame.font.Font(None, 48).render("Game Over!", True, WHITE)
            play_again_text = pygame.font.Font(None, 24).render("Press SPACE to play again", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))
            screen.blit(play_again_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()