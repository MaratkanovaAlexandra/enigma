from random import randrange

sizeOfBlock = 128
sizeOfChar = 16
shiftKey = 2
quantityOfRounds = 16
blocks = []


def stringToRightLength(value):
    while (((len(value) * sizeOfChar) % sizeOfBlock) != 0):
        value += "*"
    return value


def generateRandomBlock():
    bin = ''
    for i in range(0, sizeOfBlock):
        bin += str(randrange(1))

    return bin

    # // Удалить блоки со случайными битами


def deleteRandomBlocks():
    for i in range(0, int(len(blocks) / 2)):
        blocks[i * 2 + 1] = ''

    for i in range(0, int(len(blocks) / 2)):
        if (blocks[i] == ''):
            del blocks[i: i + 1]


def сutStringIntoBlocks(value):
    blocksLength = int((len(value) * sizeOfChar) / sizeOfBlock)
    blocks = []
    lengthOfBlock = int(len(value) / blocksLength)

    for i in range(0, blocksLength):
        blocks.append(stringToBinaryFormat(
            value[i * lengthOfBlock: (i + 1) * lengthOfBlock]))
        blocks.append(generateRandomBlock())

    return blocks


def cutBinaryStringIntoBlocks(value):
    blocksLength = int(len(value) / sizeOfBlock)
    blocks = []
    lengthOfBlock = int(len(value) / blocksLength)

    for i in range(0, blocksLength):
        blocks[i] = value[i * lengthOfBlock: (i + 1) * lengthOfBlock]

    return blocks


def stringToBinaryFormat(value):
    output = ""
    for i in range(0, len(value)):
        char_binary = format(ord(value[i]), 'b')
        while (len(char_binary) < sizeOfChar):
            char_binary = "0" + char_binary

        output += char_binary

    return output


def stringFromBinaryToNormalFormat(value):
    output = ""
    for i in range(0, int(len(value) / sizeOfChar)):
        char_binary = value[i * sizeOfChar: (i + 1) * sizeOfChar]
        output += chr(int(char_binary, 2))

    return output


def correctKeyWord(value, keyLength):
    if (len(value) > keyLength):
        value = value[0: keyLength]
    else:
        while (len(value) < keyLength):
            value = "0" + value

    return value


def XOR(s1, s2):
    result = ""
    for i in range(0, len(s1)):
        a = int(s1[i]) - 0
        b = int(s2[i]) - 0
        if (a ^ b):
            result += "1"
        else:
            result += "0"

    return result


def f(s1, s2):
    return XOR(s1, s2)


def encodeDES_OneRound(value, key):
    L = value[: int(len(value) / 2)]
    R = value[int(len(value) / 2):]
    return (R + XOR(L, f(R, key)))


def decodeDES_OneRound(value, key):
    L = value[: int(len(value) / 2)]
    R = value[int(len(value) / 2):]

    return (XOR(f(L, key), R) + L)


def keyToNextRound(key):
    for i in range(0, shiftKey):
        key = key[len(key) - 1] + key
        key = key[: -1]

    return key


def keyToPrevRound(key):
    for i in range(0, shiftKey):
        key = key + key[0]
        key = key[1:]

    return key


def encrypt(text, key):
    text = stringToRightLength(text)
    blocks = сutStringIntoBlocks(text)

    key = correctKeyWord(key, int(len(text) / (2 * len(blocks))))
    key = stringToBinaryFormat(key)
    for j in range(0, quantityOfRounds):
        for i in range(0, len(blocks)):
            blocks[i] = encodeDES_OneRound(blocks[i], key)

        key = keyToNextRound(key)

    key = keyToPrevRound(key)
    key = stringFromBinaryToNormalFormat(key)

    code = ""
    for i in range(0, len(blocks)):
        code += blocks[i]

    code = stringFromBinaryToNormalFormat(code)

    return [key, code]


def decrypt(key, code):
    key = stringToBinaryFormat(key)
    code = stringToBinaryFormat(code)
    blocks = cutBinaryStringIntoBlocks(code)
    deleteRandomBlocks()

    for j in range(0, quantityOfRounds):
        for i in range(0, len(blocks)):
            blocks[i] = decodeDES_OneRound(blocks[i], key)

        key = keyToPrevRound(key)

    key = keyToNextRound(key)
    key = stringFromBinaryToNormalFormat(key)
    text = ""
    for i in range(0, len(blocks)):
        text += blocks[i]

    text = stringFromBinaryToNormalFormat(text)
    return [text, key]
