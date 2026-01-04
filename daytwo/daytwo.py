total = 0 


with open("input2.txt", "r") as file:
    ids = file.read().split(",")


def find_matching(number):
    for i in range(1, len(number)+1):
        dupe = number[:i]

        dupe2 = number[i:i+(len(dupe))]
        # print(dupe)
        # print(len(dupe))
        # (4: 4:7)
        # print("dupe is " + dupe)
        # print(number[i:i+(len(dupe))])
        if dupe == dupe2:
            if (i+len(dupe) == len(number)):
                return True
            for j in range(i+len(dupe), len(number)+1, len(dupe)):
                # print(j >= len(number))
                # print(number[j:j+len(dupe)] != dupe)
                # print(number[j:j+len(dupe)])
                if number[j:j+len(dupe)] != dupe:
                    break
                if j+len(dupe) >= len(number):
                    return True
    return False

for id in ids:
    ranges = id.split("-")
    # print(ranges)
    for i in range(int(ranges[0]), int(ranges[1])+1):
        # print("number is " + str(i))
        # find_matching(str(i))
        # print(find_matching(str(i)))
        if find_matching(str(i)) == True:
            total += i
        # dupe = ""
        # dupe2 = ""
        # for j in range(1, len(str(i))):
        #     print(j)
        #     dupe = str(i)[:j]
        #     dupe2 = str(i)[j:j+len(str(dupe))]
        #     print("dupe one: " + str(dupe))
        #     print("dupe two: " + str(dupe2))
        #     # print(dupe2)
        #         if (j+len(dupe) == len(str(i))):
        #             total += i
        #         print(j+len(str(dupe)))
                # for k in range(j+len(dupe)-1, len(str(i)), len(dupe)):
                #     print("k is:" + str(k))

print(total)
# https://adventofcode.com/2025/day/2
