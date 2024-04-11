# quickly write to delete ' ' and digit at the start of history output
# file by George Zhang 4/11/2024
# save a copy here for future usage just in case
with open('temp.txt', 'r') as f:
    lines = f.readlines()

newlines = []

for line in lines:
    for ch in line:
        if ch == ' ' or ch.isdigit():
            pass
        else:
            ind = line.index(ch)
            line_mod = line[ind:]
            newlines.append(line_mod)
            break

with open('temp_mod.txt', 'w') as f:
    f.write(''.join(newlines))


