def camel_snake(s):
    return


s = (
    input()
    .replace("A", "_a")
    .replace("B", "_b")
    .replace("C", "_c")
    .replace("D", "_d")
    .replace("E", "_e")
    .replace("F", "_f")
    .replace("G", "_g")
    .replace("H", "_h")
    .replace("I", "_i")
    .replace("J", "_j")
    .replace("K", "_k")
    .replace("L", "_l")
    .replace("M", "_m")
    .replace("N", "_n")
    .replace("O", "_o")
    .replace("P", "_p")
    .replace("Q", "_q")
    .replace("R", "_r")
    .replace("S", "_s")
    .replace("T", "_t")
    .replace("U", "_u")
    .replace("V", "_v")
    .replace("W", "_w")
    .replace("X", "_x")
    .replace("Y", "_y")
    .replace("Z", "_z")
)
s2 = s
if s2[0] == "_" and s2[-1] == "_":
    s3 = s2[1:-1]
elif s2[0] == "_":
    s3 = s2[1:]
elif s2[-1] == "_":
    s3 = s2[:-1]
else:
    s3 = s2

print(s3)
# # if s2[0] == "_":
# #     s2.removeprefix()

# # if s2[-1] == "_":
# #     s2.removesuffix()
# print(s2)