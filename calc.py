res = 0.0
w = int(input("Enter number of wickets lost : "))
for i in range(w+1,12):
    bave = float(input("Enter "+str(i)+" batsman average : "))
    bmax = float(input("Enter "+str(i)+" maximum average : "))
    bmin = float(input("Enter "+str(i)+" minimum average : "))
    res = res +  bave/(bmax-bmin)
vave = 1/(11-w)*res;
print("Result is Vave.: ",vave)