dash = '-' * 42
for i in range(1,11):
    print(dash)
    print("Tabla del {}".format(i))
    print(dash)
    for j in range(1,11):
      print("{} x {} = {}".format(i, j, 3 * j))
