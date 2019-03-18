"""
    token生成器的 repl 交互式文件
"""
from Monkey.lexer import Lexer


def repl():

    print("{:*^100}".format("REPL --Version1.0"))
    while True:
        l = Lexer()
        try:
            input_text = input(">>> ")
            l.tokenize(input_text)
        except (KeyboardInterrupt, TypeError, Exception) as e:
            print(f"Error: {e}\nEnd...!")
            return
        else:
            for i in l.tokens:
                print(i)


if __name__ == "__main__":
    repl()