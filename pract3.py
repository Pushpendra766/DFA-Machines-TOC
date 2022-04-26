def check_dfa(str):
    length = len(str)
    count = 0
    if length == 0:
        print("String is rejected.")
        return

    for i in range(0, length):
        if str[i] == 'a':
            count += 1

    if count == length:
        print("String is accepted.")
        return
    else:
        print("String is rejected.")
        return


if __name__ == '__main__':
    str = input("Enter string : ").lower()
    print(str)
    check_dfa(str)
