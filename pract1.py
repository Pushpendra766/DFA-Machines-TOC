def check_dfa(str):
    length = len(str)
    count = 0
    if length == 1 or length == 0 or str[0] != 'c':
        print("String is rejected.")
        return
    for i in range(1, length-1):
        if str[i] == 'a' or str[i] == 'b':
            count += 1
    if count == length-1:
        print("String is accepted.")
    else:
        print("String is rejected.")


if __name__ == '__main__':
    str = input("Enter string : ").lower()
    print(str)
    check_dfa(str)
