def encrypt(text, key=1):
    if len(text) == 0:
        return ""
    if key <= 0:
        return text
    encrtext = []
    col = 0
    currentsymbol = col
    textlen = len(text)
    while True:
        encrtext.append(text[currentsymbol])
        currentsymbol += key
        if currentsymbol >= textlen:
            col += 1
            if col < key:
                currentsymbol = col
            else:
                return ''.join(encrtext)


def decrypt(text, key=1):
    if len(text) == 0:
        return ""
    if key <= 0:
        return text
    textlen = len(text)
    symbolstable = []
    rows = textlen // key
    addrows = textlen % key
    print(rows, addrows)
    row = []
    i = 0
    plusone = 0
    if addrows != 0:
        plusone = 1
        addrows -= 1
    for l in text:
        row.append(l)
        i += 1
        if i == rows + plusone:
            if addrows == 0:
                plusone = 0
            else:
                addrows -= 1
            i = 0
            symbolstable.append(row)
            row = []
    else:
        if row:
            symbolstable.append(row)
    print(symbolstable)
    res = []
    for i in range(len(symbolstable[0])):
        for sym in symbolstable:
            try:
                res.append(sym[i])
            except:
                pass
    return ''.join(res)


if __name__ == "__main__":
    print(encrypt('hello world, how are you?', 4))
    print(decrypt(encrypt('hello world, how are you? I ma ok)', 4), 4))
