def monkeyTroble(a_smile,b_smile):
    return (a_smile and b_smile) or (not(a_smile) and not(b_smile))


a_smile = input() == "True"
b_smile = input() == "True"

print(monkeyTroble(a_smile,b_smile))