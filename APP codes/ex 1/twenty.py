tn = int(input("Input third term of the series:"))
tln = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tln))
print("Length of the series: ", n)


if n-5 == 0:
    d = (s_sum-3*tn)//6
else:
    d = (tln-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
    print(int(a), end=" ")
    a += d
print(int(a), end=" ")
