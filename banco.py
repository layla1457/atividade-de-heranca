from typing import Dict, List
from contas import Conta

class Banco:
    _registro_bancos: Dict[str, "Banco"] = {}

    def __new__(cls, nome: str):
        nome = nome.strip().title()
        if nome in cls._registro_bancos:
            return cls._registro_bancos[nome]
        instancia = super().__new__(cls)
        cls._registro_bancos[nome] = instancia
        return instancia

    def __init__(self, nome: str):
        nome = nome.strip().title()
        if not hasattr(self, "_inicializado"):
            self.nome = nome
            self.contas: Dict[str, Conta] = {}
            self._inicializado = True

    @classmethod
    def listar_bancos(cls) -> List[str]:
        return list(cls._registro_bancos.keys())

    def adicionar_conta(self, conta: Conta):
        if conta.numero in self.contas:
            raise ValueError("Conta já existe neste banco.")
        self.contas[conta.numero] = conta
        print(f"Conta {conta.numero} adicionada ao banco {self.nome}")

    def listar_contas(self) -> List[Conta]:
        return list(self.contas.values())

    def buscar_conta(self, numero: str) -> Conta:
        return self.contas.get(numero)

    @classmethod
    def saldo_total(cls) -> float:
        total = 0.0
        for banco in cls._registro_bancos.values():
            for conta in banco.contas.values():
                total += conta.saldo
        return total
