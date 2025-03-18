# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set()  # vazio
s2 = set('Talles')
s1 = {'Luiz', 1, 2, 3}  # com dados
print(s1, type(s1))
print(s2, type(s2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
set_numeros = {1, 2, 3, 3, 3, 3, 3, 1}
print(set_numeros)
for numero in set_numeros:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Talles')
s1.update('Madi')
# s1.clear()
s1.discard('a')
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
uniao = set_1 | set_2
interseccao = set_1 & set_2
diferenca = set_1 - set_2
diferenca_simetrica = set_1 ^ set_2

print(uniao)
print(interseccao)
print(diferenca)
print(diferenca_simetrica)
