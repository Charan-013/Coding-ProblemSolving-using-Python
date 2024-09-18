def spell_check(d1,st1):
    if st1 in d1:
        return True
    return False

d1 = eval(input())
st1 = input()
print(spell_check(d1,st1))