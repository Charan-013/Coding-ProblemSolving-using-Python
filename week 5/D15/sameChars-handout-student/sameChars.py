def sameChars(s1, s2):
    def char_in_string(s, char):
        for ch in s:
            if ch == char:
                return True
        return False

    def all_chars_match(s1, s2):
        for ch in s1:
            if not char_in_string(s2, ch):
                return False
        for ch in s2:
            if not char_in_string(s1, ch):
                return False
        return True

    return all_chars_match(s1, s2)

print(sameChars(input(), input()))
