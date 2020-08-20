sol = str(input("Type in a if solution requires squared value not to exceed 200 or b if the input requires to be less than 200: "))

if sol == "a":
    opt = 200
elif sol == "b":
    opt = 15


num = int(input("Enter the end of loop: "))+1
if num < opt:
    lim = num
else:
    lim = opt

for i in range(1,lim):
    print(i, i*i)
 
