from lark import Lark
import lark
from lark.indenter import PythonIndenter
from transformer import desugar,statements,tokens
import rich
# Official Python grammar by Lark
python = Lark.open_from_package('lark', 'python.lark', ['grammars'],parser='lalr', postlex=PythonIndenter(), start='file_input',keep_all_tokens=True)
transformer = statements()
out = open('samples/test.js','w')

file = open("samples/python_test1.py","r")
tree = python.parse(file.read())

tree = transformer.transform(tree)


