for i in range(100):
    try:
        s = input()
        print(s)
    except EOFError:
        break