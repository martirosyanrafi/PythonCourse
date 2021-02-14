a = [1, 4, 5, 7, 8, -2, 0, -1]

print("2)")
print(" 3:", a[3])
print(" 5:", a[5])

print("3)")
a_sorted = sorted(a, reverse=True)
print(" a:", a)
print(" a_sorted:", a_sorted)

print("4)")
print(" 1...3:", a_sorted[1:4])
print(" 2...6:", a_sorted[2:7])

del a_sorted[2:4]

print("6)", a_sorted)

b = ["grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted = sorted(b)
print("8)")
print(" b:", b)
print(" b_sorted:", b_sorted)

c = a[1:4] + b[4:7]
print("10)", c)