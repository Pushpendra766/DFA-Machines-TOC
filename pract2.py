def check_dfa(str):
    length = len(str)
    count_char = 0

    if length == 0:
        print("String is rejected")
        return

    for i in range(0, length):
        if str[i] == 'a' or str[i] == 'b':
            count_char += 1

    if count_char == length:
        strings = str.split('a')
        for string in strings:
            if len(string)>0 and string[0] == 'b':
                if len(string) % 2:
                    print("String is rejected")
                    return
        print("String is accepted")
        return
    else:
        print("String is rejected")
        return


if __name__ == '__main__':
    str = input("Enter string : ").lower()
    print(str)
    check_dfa(str)