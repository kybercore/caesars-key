from collections import Counter
import sys
from freq import FREQ_EN, FREQ_DE, FREQ_FR, FREQ_IT, FREQ_ES, FREQ_PT, FREQ_SE, FREQ_NL

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

LETTER_FREQUENCY = {
    "en": FREQ_EN,
    "de": FREQ_DE,
    "fr": FREQ_FR,
    "it": FREQ_IT,
    "es": FREQ_ES,
    "pt": FREQ_PT,
    "se": FREQ_SE,
    "nl": FREQ_NL
}

# Calculates the difference between the encrypted text frequency and the language frequency

def difference(text: str, language: str) -> float:
    counter = Counter(text)
    return (
        sum(
            abs(
                counter.get(letter, 0) * 100 / len(text)
                - LETTER_FREQUENCY[language].get(letter, 0)
            )
            for letter in ALPHABET
        )
        / ALPHABET_SIZE
    )

def decrypt(cipher_text: str, key: int) -> str:
    decrypted_text = ""

    for char in cipher_text:
        # If the character is not in the alphabet (ignoring case), keep it as it is

        if char not in ALPHABET and char.lower() not in ALPHABET:
            decrypted_text += char
            continue
        # If the character is uppercase, decrypt it and keep the case

        if char.isupper():
            decrypted_char = ALPHABET[
                (ALPHABET.index(char.lower()) - key) % ALPHABET_SIZE
            ].upper()
            decrypted_text += decrypted_char
            continue
        # If the character is lowercase, decrypt it

        decrypted_char = ALPHABET[(ALPHABET.index(char.lower()) - key) % ALPHABET_SIZE]
        decrypted_text += decrypted_char
    return decrypted_text

def main() -> int:

    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python main.py <filename>.txt")
        return 1
    filename = args[0]
    with open(filename, "r") as file:
        cipher_text = file.read()

    # Decrypting the cipher text for each language and finding the key that gives the minimum difference

    language_outputs = (
        (
            min(
                (
                    difference(decrypt(cipher_text, key), language),
                    key,
                    decrypt(cipher_text, key),
                )
                for key in range(1, ALPHABET_SIZE)
            ),
            language,
        )
        for language in ["en", "de", "fr", "it", "es", "pt", "se", "nl"]
    )

    # Finding the best guess (that is the language with the minimum difference)
    # Map structure: language -> (difference, key, decrypted_text)

    best_guess = min(language_outputs, key=lambda x: x[0][0])

    print(best_guess[0][2].strip())
    print(
        f"\033[34m\nBest guess: {best_guess[1].upper()} (proximity {best_guess[0][0]} with key {best_guess[0][1]})\033[0m"
    )

    return 0

if __name__ == "__main__":
    main()
