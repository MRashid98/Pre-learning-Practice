num = int(input("Enter num: "))

def calc_divisors(num):
    a = []
    for i in range(1, num+1):
        if num % i == 0:
            a.append(i)
        if len(a) > 2:
            break
    return len(a)



check = calc_divisors(num)

if check == 2:
    print(num,"is prime")
else:
    print(num,"is not prime")
