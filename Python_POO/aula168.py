# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields

@dataclass(init=False)
class Pessoa:
    _nome: str = field(
        default= 'Missing', repr=False
    )
    _sobrenome: str = 'Not Sent'
    _idade: int = 0
    # _enderecos: list[str] = field(default_factory=list)

    def __init__(self, nome, sobrenome) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self.nome_completo = f'{self._nome} {self._sobrenome}'

    def __post_init__(self):
        self.nome_completo = f'{self._nome} {self._sobrenome}'

    # @property
    # def nome(self):
    #     return self._nome
    
    # @nome.setter
    # def nome(self, novo_nome):
    #     self._nome = novo_nome
    #     return self._nome

    # def nome_completo(self):
    #     return f'{self._nome} {self._sobrenome}'


if __name__ == '__main__':
    lista = [Pessoa('Z', 'B'), Pessoa('K', 'D'), Pessoa('E', 'F')]
    ordenadas = sorted(lista, key=lambda x: x._nome)
    p1 = Pessoa('Talles', 'Madi')
    p2 = Pessoa('Raquel', 'Manzato')
    print(fields(p1))
    print(p1)
    print(p2.nome_completo)
    print(ordenadas)
    print(asdict(p1))
    print(astuple(p1))
