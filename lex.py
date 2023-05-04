class Lexer:
    def __init__(self,source):
        self.source = source+'\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nextChar(self):
        self.curPos +=1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]
            
    def peek(self):
        pass
    def abort(self,message):
        pass
    def skipWhitespace(self):
        pass
    def skipComment(self):
        pass
    def getToken(self):
        pass