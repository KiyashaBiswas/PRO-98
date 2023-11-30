def swapFileData():
    input1 = input("Enter file 1 name")
    input2 = input("Enter file 2 name")
    with open(input1,"r") as a:
        data_a = a.read()
    with open(input2,"r") as b:
        data_b = b.read()
    with open(input1,"w") as a:
        a.write(data_b)
    with open(input2, "w") as b:
        b.write(data_a)
swapFileData()