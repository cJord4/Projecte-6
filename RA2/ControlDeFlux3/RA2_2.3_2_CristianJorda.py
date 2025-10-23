try:
    num_user = int(input("Introdueix el nombre fins al que vols contar: "))

    for i in range(0, num_user):
        print(i + 1)

except ValueError:
    print("Error: Has de introduir un nombre sencer.")
