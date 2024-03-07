za = input('查询ACSCII码输入1，ASCII码转字符输入2，退出输入0:')
za = int(za)
x = 0
while za != 0:
    if x == 1:
        za = input('查询ACSCII码输入1，ASCII码转字符输入2，退出输入0:')
        za = int(za)
    if za == 1:
        zhifu = input('输入需要转ASCII值的字符:')
        ordinal = ord(zhifu)
        print(ordinal)
        x = 1
    if za == 2:
        Ascii = input('输入需要转字符的ASCII:')
        Ascii = int(Ascii)
        chrinal = chr(Ascii)
        print(chrinal)
        x = 1
