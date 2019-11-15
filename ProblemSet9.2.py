stacks = int(input("Height: "))
if 1 <= stacks <= 8:
    for i in range(0, stacks):
        for j in range(0, i+1):
            print("# ", end="")
        print("\r")
else:
    print("Error: Not a positive integer between 1 and 8")