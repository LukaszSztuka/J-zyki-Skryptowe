def cos(a, *b):
    str = ""
    for i in b[:-1]:
        str += i+a
    str += b[len(b)-1]
    print(str)


cos(".", "cxcvxv", "fasdfasdf", "asdfadf", "xczcvzcv")