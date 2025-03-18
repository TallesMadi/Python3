class Produto:
    '''Classe que cria e gerencia o produto'''
    nome: str
    descricao: str
    valor: float | int
    disponivel: bool
    def __init__(self, nome, descricao, valor, disponivel) -> None:
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.disponivel = disponivel

    def listar(self):
        '''Função para listar o produto no terminal'''
        return f'Nome: {self.nome} - R${self.valor:.2f}'

def listar_classe(classe: list[Produto]):
    '''Função para salvar os produtos em uma lista
    e listá-los em ordem alfabética'''
    produtos_ordenados = sorted(classe, key=lambda x: x.valor)
    return [item.listar() for item in produtos_ordenados]

def criar_produto(lista_de_produtos: list) -> list:
    '''Função para que o usuário possa criar um produto direto do terminal'''
    resposta_nome = input('Nome do produto: ')
    resposta_descricao = input('Descrição do produto: ')
    resposta_valor = input('Valor do produto: ')
    resposta_disponivel = input('Disponibilidade do produto: (1 para disponivel, 0 para indisponivel) ')
    try:
        resposta_valor_float = float(resposta_valor)
        if resposta_disponivel == '1':
            resposta_disponivel_bool = True
        elif resposta_disponivel == '0':
            resposta_disponivel_bool = False 
        else:
            print(f'Por favor, digite o valor 0 ou 1 ao invés de {resposta_disponivel}')
            pass

    except ValueError:
        print(f'Algum valor não está correto!')
        pass

    lista_de_produtos.append(Produto(resposta_nome, resposta_descricao, resposta_valor_float, resposta_disponivel_bool))
    return listar_classe(lista_de_produtos)

lista_de_produtos = []
while True:
    resposta_cadastro_produto = input('Deseja cadastrar um produto? s/n ')
    if resposta_cadastro_produto == 's':
        print(criar_produto(lista_de_produtos))
    else:
        print('Fechando o programa!')
        break
