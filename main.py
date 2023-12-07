import random

# Konstanten
MAX_TRIES = 6
WORDS = ["Abgabe", "moderne", "software", "entwicklung", "hangman"]
STAGES = ["Noch 6 Versuche", "Noch 5 Versuche", "Noch 4 Versuche", "Noch 3 Versuche", "Noch 2 Versuche", "Noch 1 Versuch"]


def choose_random_word(word_list):
    """Wählt zufällig ein Wort aus der gegebenen Liste aus."""
    return random.choice(word_list)


def display_current_progress(word_completion):
    """Zeigt den aktuellen Fortschritt des Wortes an."""
    print("\nAktueller Wortfortschritt: " + word_completion + "\n")


def get_user_guess():
    """Fordert den Spieler auf, einen Buchstaben oder ein Wort zu raten."""
    return input("Bitte gib einen Buchstaben ein: ").lower()


def update_word_completion(word, word_completion, guess):
    """Aktualisiert den Fortschritt des Wortes basierend auf der Vermutung des Spielers."""
    return "".join([guess if word[i] == guess else word_completion[i] for i in range(len(word))])


def play_hangman():
    word = choose_random_word(WORDS)
    word_completion = "_" * len(word)
    guessed_letters = list()
    tries = MAX_TRIES

    print("Willkommen bei Hangman!")

    while tries > 0 and "_" in word_completion:
        print(STAGES[MAX_TRIES - tries])
        display_current_progress(word_completion)
        guess = get_user_guess()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"Du hast diesen Buchstaben schon geraten: {guess}")
            elif guess not in word:
                print(f"{guess} ist nicht im Wort.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Gut gemacht, {guess} ist im Wort!")
                word_completion = update_word_completion(word, word_completion, guess)
                guessed_letters.append(guess)
        else:
            print("Ungültige Eingabe.")

    if "_" not in word_completion:
        print("Glückwunsch, du hast das Wort erraten!")
    else:
        print(f"Leider hast du das Spiel verloren. Das Wort war '{word}'.")


if __name__ == "__main__":
    play_hangman()
