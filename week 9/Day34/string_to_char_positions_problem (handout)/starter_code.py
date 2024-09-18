def string_to_char_positions(s: str) -> dict:
    letter_positions = {}

    for i in range(len(s)):

        letter = s[i]
        if letter not in letter_positions:
            letter_positions[letter] = []
        letter_positions[letter].append(i)

    return letter_positions


s = input().strip()

print(string_to_char_positions(s))
