txt = input()
def writeshort(txt):
    result = []
    for word in txt:
        if len(word) > 4:
            continue
        result.append(word)
    return result
result = []
for word in txt:
    if len(word) < 5:
        result.append(word)
def writeshort(txt):
    return [word for word in txt if len(word) < 5]












