"""
    handle the input
"""


class Text(object):
    def __init__(self, text=""):
        self.text = text
        self.length = len(text)
        self.position = -1
        self.nextPosition = 0
        self.currentChar = ""
        self.moveNext()

    def moveNext(self):
        if self.nextPosition >= self.length:
            self.currentChar = -1
        else:
            self.position += 1
            self.nextPosition = self.position + 1
            self.currentChar = self.text[self.position]

    def getNextChar(self):
        if self.nextPosition >= self.length:
            return None
        else:
            return self.text[self.nextPosition]


    def skipSpace(self):
        while self.currentChar in ("\n", "\t", " ", "\r"):
            self.moveNext()



    def isIdentifier(self):
        return (self.currentChar >= 'a' and self.currentChar <= 'z') or (
                    self.currentChar >= 'A' and self.currentChar <= 'Z') or self.currentChar == '_'

    def isDigit(self):
        return self.currentChar >= '0' and self.currentChar <= '9'

    def readDigit(self):
        pis = self.position
        while self.isDigit():
            self.moveNext()
        return self.text[pis:self.position]

    def readIdentifier(self):
        pis = self.position
        while self.isIdentifier():
            self.moveNext()
        return self.text[pis:self.position]

    def checkNext_EQ(self):
        if self.getNextChar() == "=":
            c = self.currentChar
            self.moveNext()
            return c + "="
        else:
            return self.currentChar
