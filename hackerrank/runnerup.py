def swap_case(s):
    for i in s:
        if i in 'A-Z':
            x=i.lowercase()
    return

if __name__ == '__main__':
    s= input()
    result = swap_case(s)
    print(result)