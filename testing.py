from tokenizer import tokenizer
from order import ordered_line
from ast_builder import AST_builder
token= tokenizer("4.3 + 'h';",["func"])
print(token)
ord_line = ordered_line(token)
print(AST_builder(ord_line))
