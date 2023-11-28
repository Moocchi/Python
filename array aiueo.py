import os


def count_vowels(text):
    counts = {"a": 0, "i": 0, "u": 0, "e": 0, "o": 0}
    for char in text:
        char_lower = char.lower()
        if char_lower in counts:
            counts[char_lower] += 1

    return counts


os.system("cls")
input_text = input("Enter a text: ")
result = count_vowels(input_text)

print("Vowel counts:")
for vowel, count in result.items():
    print(f"{vowel}: {count}")
