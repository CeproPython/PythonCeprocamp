n1=float(input("1_número:"))
n2=float(input("2_ número:"))
n3=float(input("3_número:"))

mn=n1
if (n2 > mn):
    mn = n2
if (n3 > mn):
    mn = n3

print("Maior:", mn)

mn = n1

if (n2 < mn):
    mn = n2
if (n3 < mn):
    mn = n3

print("Menor: ", mn)
