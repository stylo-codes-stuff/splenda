from lark import Lark

from lark.indenter import PythonIndenter
from transformer import desugar
# Official Python grammar by Lark
python = Lark.open_from_package('lark', 'python.lark', ['grammars'],parser='earley', postlex=PythonIndenter(), start='file_input',maybe_placeholders=False,keep_all_tokens=True)


file = open("samples/python_test1.py","r")

