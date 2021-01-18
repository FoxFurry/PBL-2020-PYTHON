def getFields(raw):
    result = []

    start = raw.find('"generateLen":"') + len('"generateLen":"')
    end = raw.find('","source":"')

    generatedLen = raw[start:end]

    start = end + len('","source":"')
    end = raw.find('"}')

    source = raw[start:end]

    result.append(generatedLen)
    result.append(source)

    return result

# Example:
# print(getFields('{"generateLen":"1000","source":"   V        V    Í      Î  Í  Q    É           >Ç       F"}'))


def intArrayToString(data):
    result = ""
    intArr = data["source"]
    for it in intArr:
        result += chr(int(it))
    return result