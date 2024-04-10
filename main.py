def encode(num):
    numlist = list(str(num))
    intlist = []
    final = []
    for i in numlist:
        x = int(i)
        intlist.append(x)
    for i in intlist:
        x = i+3
        final.append(x)
    return("".join(str(num) for num in final))


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

if __name__ == "__main__":
    while True:
        menu()
        opt = input("Please enter an option: ")
        if opt == "1":
            num = int(input("Please enter your password to encode: "))
            stored_pass = encode(num)
            print("Your password has been encoded and stored!\n")
        elif opt == "2":
            pass
        elif opt == "3":
            break
        else:
            print("Invalid Option")