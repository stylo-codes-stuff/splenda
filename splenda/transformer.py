from lark import Transformer

class desugar(Transformer):
    def DEF(self, token):
        return "function" # Replace 'TOKEN' with an opening curly brace
