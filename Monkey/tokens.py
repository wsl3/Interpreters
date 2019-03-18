"""
 token's type
"""

class Token(object):
    def __init__(self, TokenType, Literal):
        self.TokenType = TokenType
        self.Literal = Literal
    def __str__(self):
        return "Token({}, {})".format(self.TokenType, self.Literal)
    __repr__ = __str__



# 算术符号
ADD = "add"
SUB = "sub"
MUL = "mul"
DIV = "div"


# 常量-> 数字, 字符串, [], {}, ;
NUM = "number"
SEMIC = ";"
LBRACE = "{"   #{ open brace, open curly 左花括号
RBRACE = "}"   #} close brace, close curly 右花括号
LPAREN = "("   #( open parenthesis, open paren 左圆括号
RPAREN = ")"   #) close parenthesis, close paren 右圆括号
LBRACKET = "[" #[ open bracket 左方括号
RBRACKET = "]" #]close bracket 右方括号
COMMA = ","

GT = ">"
LT = "<"
GT_EQ = ">="
LT_EQ = "<="
EQ = "="
NOT = "!"
DOUBLE_EQ = "=="
NOT_EQ = "!="

# 变量名 identifer
IDENTIFIER = "Identifier"

# Monkey的内置关键字 Keyword
KEYWORD = "keyword"
TRUE = "TRUE"
FALSE = "FALSE"
LET = "LET"
FUNC = "FUNC"
RETURN = "RETURN"
IF = "IF"
ELSE = "ELSE"


# error
EOF = "EOF"
ILLEGAL = "illegal"

KeyWord = {
    "let": LET,
    "func": FUNC,
    "true": TRUE,
    "false": FALSE,
    "return": RETURN,
    "if": IF,
    "else": ELSE

}