"""
    一个名为 Monkey 的编程语言及其 Interpreter 的实现
"""

from Monkey.tokens import *
from Monkey.text import Text


class Lexer(object):
    def __init__(self):
        self.tokens = []

    def tokenize(self, input_text):
        """

        :param t: an object of string
        :return: tokens
        """
        t = Text(input_text)
        while (t.currentChar != -1):
            # t.skipSpace() 和下面的 t.moveNext() 保证每次循环中的 char 都是有效的(不是\n," "等无意义的Token)
            t.skipSpace()
            char = t.currentChar
            if char == "+":
                self.tokens.append(Token(ADD, char))
            elif char == "-":
                self.tokens.append(Token(SUB, char))
            elif char == "*":
                self.tokens.append(Token(MUL, char))
            elif char == "/":
                self.tokens.append(Token(DIV, char))
            elif char == "[":
                self.tokens.append(Token(LBRACKET, char))
            elif char == "]":
                self.tokens.append(Token(RBRACKET, char))
            elif char == "(":
                self.tokens.append(Token(LPAREN, char))
            elif char == ")":
                self.tokens.append(Token(RPAREN, char))
            elif char == "{":
                self.tokens.append(Token(LBRACE, char))
            elif char == "}":
                self.tokens.append(Token(RBRACE, char))
            elif char == ";":
                self.tokens.append(Token(SEMIC, char))
            elif char == ",":
                self.tokens.append(Token(COMMA, char))
            # 检查下一个字符 是否是 '='
            elif char in ("=", "<", ">", "!"):
                temp = t.checkNext_EQ()
                self.tokens.append(Token(temp, temp))
            # 必须检测此情况, 因为运行t.skipSpace()后可能导致text后都是无意义字符而使 char=-1， 即 text扫描完毕
            elif char == -1:
                break
            else:
                # isIdentifier, isDigit 不能执行下面的 moveNext, so continue
                # currentChar is keyword or identifier
                if t.isIdentifier():
                    iden = t.readIdentifier()
                    k = KeyWord.get(iden, IDENTIFIER)
                    self.tokens.append(Token(k, iden))
                    continue
                # currentChar is digit
                elif t.isDigit():
                    digit = t.readDigit()
                    self.tokens.append(Token(NUM, digit))
                    continue
                # currentChar is illegal
                else:
                    self.tokens.append(Token(ILLEGAL, char))
            t.moveNext()
        self.tokens.append(Token(EOF, -1))


l = Lexer()
input_text = "let a= func(a,b){};"
l.tokenize(input_text)

print(f">>>{input_text}")
for i  in l.tokens:
    print(i)
