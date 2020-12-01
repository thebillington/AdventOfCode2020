def solution_one(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x = int(data[i])
            y = int(data[j])
            total = x + y
            if total == 2020:
                print("{} + {} = 2020, {} * {} = {}".format(x, y, x, y, (x*y)))
                return

def solution_two(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                x = int(data[i])
                y = int(data[j])
                z = int(data[k])
                total = x + y + z
                if total == 2020:
                    print("{} + {} + {} = 2020, {} * {} * {} = {}".format(x, y, z, x, y, z, (x*y*z)))
                    return
                
if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    solution_one(data)
    solution_two(data)