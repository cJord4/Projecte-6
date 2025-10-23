num_user = input("Introdueix el nombre fins al que vols contar: ")

try:
    for i in range(0, num_user):
        print(i)


except Exception as str:
    print(f"Hi ha un Error:{str}")
