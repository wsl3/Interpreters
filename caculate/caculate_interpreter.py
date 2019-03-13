"""
    一个计算器的 Small interpreters
"""
from functools import reduce

# 基本的表达式 like 'add(1,2)'
class Expr(object):
    def __init__(self, operator, num_list):
        self.operator = operator
        self.num_list = num_list
        self._result = None

    def __repr__(self):
        return "Expr({}, {})".format(repr(self.operator), repr(self.num_list))

    def __str__(self):
        num_str = ", ".join(map(str, self.num_list))
        return "{}({})".format(str(self.operator), num_str)

    # return the result of a Expr
    @property
    def result(self):
        try:
            self.num_list = [self.generate_result(sym) for sym in self.num_list]
            if self.operator in ("add", "+"):
                return reduce(lambda x,y: x+y, self.num_list)
            elif self.operator in ("sub", "-"):
                return reduce(lambda x,y: x-y, self.num_list)
            elif self.operator in ("mul", "*"):
                return reduce(lambda x,y: x*y, self.num_list)
            elif self.operator in ("div", "/"):
                try:
                    return reduce(lambda x,y: x/y, self.num_list)
                except ZeroDivisionError:
                    print("Error:除数不能为0!\n")
                    return
        except:
            print("Caculate Error!")
            return


    def generate_result(self, sym):
        if(isinstance(sym, Expr)):
            return sym.result
        else:
            return sym



class Interpreter(object):
    def __init__(self, text=None):
        self.text = text
        self.tokens = []

    def parse(self):
        """
        parse函数中 first_token假定有两种情况
        1. 为数字 则返回 数字本身,然后去掉数字后面的字符, 可能是 , ), 这样下一个first_token 可能为数字或者 add 之类的操作符
        2. 为add之类的操作符,则返回 一个Expr 对象
        :return: 数字或者Expr对象
        """
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


def repl():
    print("Caculate version 1.0\n")
    prompt = ">>> "
    i = Interpreter()
    while(True):
        try:
            i.text = input(prompt)
            i.tokenize()
            expr = i.parse()
            print("parser result: {}".format(expr))
            print("Caculate result: {}".format(expr.result))
        except InterruptedError:
            print("Caculate Interpreter end!")
            return None


if __name__ == "__main__":
    repl()