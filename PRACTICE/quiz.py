import pygame
import sys
import random
import json
import os

pygame.init()

# Window
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Quiz Game")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,100,255)
GREEN = (0,200,100)
RED = (255,80,80)
GRAY = (180,180,180)

# Fonts
title_font = pygame.font.SysFont("Arial", 40)
question_font = pygame.font.SysFont("Arial", 28)
button_font = pygame.font.SysFont("Arial", 24)

# Clock
clock = pygame.time.Clock()

# Leaderboard file
LEADERBOARD_FILE = "leaderboard.json"

# Quiz Data
quiz_data = {
    "Science": [
        {
            "question": "Which planet is Red Planet?",
            "options": ["Earth", "Mars", "Venus", "Jupiter"],
            "answer": "Mars"
        },
        {
            "question": "What gas do plants absorb?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide"
        }
    ],
    "Technology": [
        {
            "question": "Who created Python?",
            "options": ["Guido", "Bill Gates", "Steve Jobs", "Elon Musk"],
            "answer": "Guido"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Processing Unit",
                "Control Processing Unit",
                "Central Program Unit"
            ],
            "answer": "Central Processing Unit"
        }
    ]
}

# Functions
def draw_text(text, font, color, x, y):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))


def save_score(score):
    scores = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            scores = json.load(f)

    scores.append(score)
    scores.sort(reverse=True)

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f)


def load_scores():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []


def button(text, x, y, w, h, color):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect)
    draw_text(text, button_font, WHITE, x + 20, y + 15)
    return rect


def start_screen():
    while True:
        screen.fill(BLACK)
        draw_text("QUIZ GAME", title_font, WHITE, 330, 150)

        start_btn = button("START", 350, 300, 200, 60, BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    return

        pygame.display.update()


def category_screen():
    while True:
        screen.fill(BLACK)
        draw_text("Choose Category", title_font, WHITE, 280, 100)

        buttons = []
        y = 220
        for category in quiz_data.keys():
            btn = button(category, 300, y, 300, 60, BLUE)
            buttons.append((btn, category))
            y += 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn, category in buttons:
                    if btn.collidepoint(event.pos):
                        return category

        pygame.display.update()


def quiz_screen(category):
    questions = quiz_data[category][:]
    random.shuffle(questions)

    score = 0

    for q in questions:
        timer = 15
        answered = False
        start_ticks = pygame.time.get_ticks()

        while not answered:
            screen.fill(BLACK)

            draw_text(q["question"], question_font, WHITE, 100, 80)

            buttons = []
            y = 200
            for option in q["options"]:
                btn = button(option, 200, y, 500, 50, GRAY)
                buttons.append((btn, option))
                y += 80

            seconds = timer - (pygame.time.get_ticks() - start_ticks) // 1000
            draw_text(f"Time: {seconds}", button_font, GREEN, 700, 30)
            draw_text(f"Score: {score}", button_font, BLUE, 50, 30)

            if seconds <= 0:
                answered = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for btn, option in buttons:
                        if btn.collidepoint(event.pos):
                            if option == q["answer"]:
                                score += 10
                            answered = True

            pygame.display.update()
            clock.tick(60)

    return score


def game_over(score):
    save_score(score)
    leaderboard = load_scores()

    while True:
        screen.fill(BLACK)

        draw_text("GAME OVER", title_font, RED, 300, 80)
        draw_text(f"Your Score: {score}", question_font, WHITE, 320, 180)

        draw_text("Leaderboard", question_font, GREEN, 350, 250)

        y = 300
        for i, s in enumerate(leaderboard[:5]):
            draw_text(f"{i+1}. {s}", button_font, WHITE, 380, y)
            y += 40

        replay_btn = button("PLAY AGAIN", 320, 500, 250, 60, BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_btn.collidepoint(event.pos):
                    return
#this part of code is used for score
        pygame.display.update()


# Main Loop
while True:
    start_screen()
    category = category_screen()
    final_score = quiz_screen(category)
    game_over(final_score) 
