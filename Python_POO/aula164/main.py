import uma_linha, varias_linhas, doc_func, doc_class

# print(dir(uma_linha))
print(uma_linha.__doc__)
print(uma_linha.__name__)
print(uma_linha.__file__)
print('*'*40)
print(varias_linhas.__doc__)
print(varias_linhas.__name__)
print(varias_linhas.__file__)

print(doc_func.soma(1, 6))
print(doc_func.multiplica(11, 6))

print(doc_class.Classuda.retornar(1))