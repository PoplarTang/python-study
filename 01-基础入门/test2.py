import time

def draw_cube(frame):
    for i in range(7, -8, -1):
        for j in range(-7, 8):
            for k in range(-7, 8):
                if abs(j) <= 7 - abs(i) and abs(k) <= 7 - abs(i):
                    if j == 7 - abs(i) or j == -7 + abs(i) or k == 7 - abs(i) or k == -7 + abs(i):
                        print("* ", end="")
                    else:
                        print("  ", end="")
                else:
                    print("  ", end="")
            print("")
        print("")

for frame in range(0, 361, 10):
    print("frame:", frame)
    draw_cube(frame)
    print("\n\n")
    time.sleep(1)