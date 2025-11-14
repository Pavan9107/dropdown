lines = ["check\n", "error\n", "test\n"]

with open("test.txt", "w+") as f:
    f.writelines(lines)
    f.seek(0)
    line_number = 0
    for line in f:
        line_number += 1
        if "error" in line:
            print(line_number, line)



