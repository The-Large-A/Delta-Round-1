#Tic tac toe grid
print("  ")
def GridMaker(size):
    if size<2:
        print("Size too small")
    
    sizer = size-1
    row = "￣　"
    column = "　｜"
    gridbit = "＿｜"
    #for i in range(sizer):
    #    print(column*(sizer) + "\n" + row*(size))
    
    for i in range(sizer):
        print(gridbit*(sizer) + "＿")
    print(column*(sizer))
     
try:
    num = int(input("Enter size of grid: cd"))
    GridMaker(num)
except TypeError:
    print("Enter a valid number")