##INPUTS
#recieve number of tests
#recieve N for each test

def CheckIfStuck(branch):
    if branch[::-1] == sorted(branch):
        return False
    else:
        return True

T = int(input())
for test in range(T):
    mountain = []
    branch = []
    NextInLine = 1
    IsStuck = False
    N = int(input())
    #Accept cart numbers in order
    for carts in range(N):
        mountain.append(int(input()))

    #Cart manager
    while len(mountain) != 0 and IsStuck == False:
        if mountain[-1] == NextInLine:
            mountain.pop()
            NextInLine += 1
        elif len(branch) != 0 and branch[-1] == NextInLine:
            branch.pop()
            NextInLine += 1
        else:
            branch.append(mountain.pop())
            IsStuck = CheckIfStuck(branch)
        #print(mountain)
        #print(branch)
        #print(IsStuck)

    if IsStuck == True:
        print("N")
    else:
        print("Y")


##Per test
#recieve carts in order for N
#Store "Next in Line"(for lake) and Initialize Branch list
#Loop: Check if end of branch or end of mountain have next in line -- if so, pop it and update next in line
#If not, send the mountain cart to branch, and check if the branch order is in a stuck order -- if stuck then return NO
#Repeat loop until no carts remain (YES) or branch gets stuck (NO)
