# transformers written for the lark python 3 grammar spec
from lark import Transformer
reserved_words = ['abstract','boolean','catch','continue','do','eval','final','function','int','native','private','short','synchronized','transient','using','while','arguments','break','char','debugger','double','export','finally','goto','import','interface','new','protected','static','this','true','var','with']


#get rid of python syntactical sugar
class desugar(Transformer):
    def __init__(self):
        self.tokens = []



# used parse out statements from the original py script ignoring how the grammar blankets tokens under singular rules (i.e. flow_stmt)
class statements(Transformer):
    def __init__(self):
        self.tokens = []
    
    # non compound statements

    #variable declaration
    def assign(self,token):
        self.tokens.append(token)
        print(token)

    #delete statement
    def del_stmt(self,token):
        self.tokens.append(token)

    #pass statement
    def pass_stmt(self,token):
        self.tokens.append(token)

    #break statement
    def break_stmt(self,token):
        self.tokens.append(token)
    
    #continue statement
    def continue_stmt(self,token):
        self.tokens.append(token)

    #return statement
    def return_stmt(self,token):
        self.tokens.append(token)
    
    #yield statement
    def yield_stmt(self,token):
        self.tokens.append(token)
    
    #raise statement
    def raise_stmt(self,token):
        self.tokens()
    #compound statements
    
#transformer to transpile chunked statements from the above transformer
class tokens(Transformer):
    def __init__(self):
        self.tokens = []

    