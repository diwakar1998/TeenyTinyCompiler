from lex import *


def main():
    source="LET age = 25"
    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()

if __name__ == "__main__":
    main()