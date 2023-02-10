s = input()
it, st = 0, 0

for i in s:
    if i.isdigit():
        it += 1
    elif i == " ":
        pass
    else:
        st += 1
print("Letters ", st)
print("Digits ", it)
