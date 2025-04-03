import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 10
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 350
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('arial', 30)
WORD_FONT = pygame.font.SysFont('arial', 50)
TITLE_FONT = pygame.font.SysFont('arial', 60)
CLUE_FONT = pygame.font.SysFont('arial', 20)

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = {
    "easy": {
        "COMPUTER": "A programmable electronic device.",
        "SOFTWARE": "Programs used to operate computers.",
        "STUDENT": "A person who is studying."
    },
    "medium": {
        "PYTHON": "A popular programming language.",
        "VISUALSTUDIO": "An IDE for software development."
    },
    "hard": {
        "BONNYRIGG": "A suburb in Sydney, Australia.",
        "ENGINEERING": "The application of scientific principles to design and build machines or structures."
    }
}
word = ""
clue = ""
guessed = []
clue_revealed = False

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# buttons
HINT_BUTTON = pygame.Rect(850, 450, 100, 30)
SHOW_CLUE_BUTTON = pygame.Rect(750, 450, 100, 30)

def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "

    text = WORD_FONT.render(display_word, 1, BLACK)
    text_rect = text.get_rect(center=(WIDTH / 2, 200))
    win.blit(text, text_rect.topleft)

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))

    # draw hint button
    pygame.draw.rect(win, BLACK, HINT_BUTTON, 2)
    hint_text = LETTER_FONT.render("HINT", 1, BLACK)
    win.blit(hint_text, (HINT_BUTTON.centerx - hint_text.get_width() / 2, HINT_BUTTON.centery - hint_text.get_height() / 2))

    # draw show clue button
    pygame.draw.rect(win, BLACK, SHOW_CLUE_BUTTON, 2)
    show_clue_text = LETTER_FONT.render("CLUE", 1, BLACK)
    win.blit(show_clue_text, (SHOW_CLUE_BUTTON.centerx - show_clue_text.get_width() / 2, SHOW_CLUE_BUTTON.centery - show_clue_text.get_height() / 2))

    # display clue if revealed
    if clue_revealed:
        display_clue()

    pygame.display.update()

def display_clue():
    text = CLUE_FONT.render("Clue: " + clue, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT - 50))

def display_message(message, show_word=False):
    pygame.time.delay(1000)
    win.fill(WHITE)

    if show_word:
        final_message = f"{message} The word was: {word}"
    else:
        final_message = message

    text = WORD_FONT.render(final_message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def start_menu():
    win.fill(WHITE)
    text = TITLE_FONT.render("SELECT DIFFICULTY", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 150))

    easy_button = pygame.Rect(WIDTH / 2 - 150, 250, 300, 50)
    medium_button = pygame.Rect(WIDTH / 2 - 150, 325, 300, 50)
    hard_button = pygame.Rect(WIDTH / 2 - 150, 400, 300, 50)

    pygame.draw.rect(win, BLACK, easy_button, 2)
    pygame.draw.rect(win, BLACK, medium_button, 2)
    pygame.draw.rect(win, BLACK, hard_button, 2)

    easy_text = WORD_FONT.render("EASY", 1, BLACK)
    medium_text = WORD_FONT.render("MEDIUM", 1, BLACK)
    hard_text = WORD_FONT.render("HARD", 1, BLACK)

    win.blit(easy_text, (easy_button.centerx - easy_text.get_width() / 2, easy_button.centery - easy_text.get_height() / 2))
    win.blit(medium_text, (medium_button.centerx - medium_text.get_width() / 2, medium_button.centery - medium_text.get_height() / 2))
    win.blit(hard_text, (hard_button.centerx - hard_text.get_width() / 2, hard_button.centery - hard_text.get_height() / 2))

    pygame.display.update()

    run = True
    difficulty = None
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if easy_button.collidepoint(m_x, m_y):
                    difficulty = "easy"
                    run = False
                if medium_button.collidepoint(m_x, m_y):
                    difficulty = "medium"
                    run = False
                if hard_button.collidepoint(m_x, m_y):
                    difficulty = "hard"
                    run = False
    return difficulty

def reveal_hint():
    global hangman_status

    # Find a letter that hasn't been guessed yet
    not_guessed = [ltr for ltr in word if ltr not in guessed]
    if not not_guessed:
        return

    hint_letter = random.choice(not_guessed)
    guessed.append(hint_letter)
    hangman_status += 1

def toggle_clue():
    global clue_revealed
    clue_revealed = not clue_revealed

def main():
    global hangman_status, word, clue

    difficulty = start_menu()
    if not difficulty:
        pygame.quit()
        return

    word, clue = random.choice(list(words[difficulty].items()))

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if HINT_BUTTON.collidepoint(m_x, m_y):
                    reveal_hint()
                elif SHOW_CLUE_BUTTON.collidepoint(m_x, m_y):
                    toggle_clue()
                else:
                    for letter in letters:
                        x, y, ltr, visible = letter
                        if visible:
                            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                            if dis < RADIUS:
                                letter[3] = False
                                guessed.append(ltr)
                                if ltr not in word:
                                    hangman_status += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!")
            run = False

        if hangman_status == 6:
            display_message("You LOST!", show_word=True)
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
