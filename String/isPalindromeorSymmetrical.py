def isPalorsymm(strs):
    n = int(len(strs) / 2)

    first = strs[:n]
    second = strs[n:]

    if first == second:
        print("String is Symmetrical")
    else:
        print("Not symmetrical")

    if first == second[::-1]:
        print("Palindrome yes")
    else:
        print("palindrome NO")

isPalorsymm("amaama")