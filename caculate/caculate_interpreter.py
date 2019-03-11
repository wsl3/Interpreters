"""
    一个计算器的 Small interpreters
"""


# 基本的表达式 like 'add(1,2)'
class Expr(object):
    def __init__(self, operator, num_list):
        self.operator = operator
        self.num_list = num_list

    def __repr__(self):
        return "Expr({}, {})".format(repr(self.operator), repr(self.num_list))

    def __str__(self):
        num_str = ", ".join(map(str, self.num_list))
        return "{}({})".format(str(self.operator), num_str)


class Interpreter(object):
    def __init__(self, text=None, symbols=[]):
        self.text = text
        self.symbols = symbols
        self.tokens = []

    def parse(self):
        first_token = self.next_token()
        token = self.eat(first_token)
        if first_token == token:
            self.next_token()  # remove (
            num_list = []
            while len(self.tokens)>0 and self.get_next_token()!="," and self.get_next_token()!=")":
                temp = self.parse()
                num_list.append(temp)
            if len(self.tokens) != 0:
                self.next_token()
            return Expr(token, num_list)
        else:
            self.next_token()
            return token

    # it'll return int or float if token is digit, else it'll return token self
    def eat(self, token):
        try:
            return int(token)
        except:
            try:
                return float(token)
            except:
                return token

    # this function produce tokens, whose type is list
    def tokenize(self):
        text = self.text.replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
        self.tokens = text.split()
        # return self.tokens

    def next_token(self):
        if len(self.tokens) > 0:
            return self.tokens.pop(0)
        raise Exception("index is error!")

    def get_next_token(self):
        if len(self.tokens) > 0:
            return self.tokens[0]
        raise Exception("index is error!")



i = Interpreter("add(mul(1,2), mul(2,sub(3,4)))")
i.tokenize()
print(i.parse())
