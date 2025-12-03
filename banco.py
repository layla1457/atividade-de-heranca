from contas import ContaCorrente, ContaPoupanca
from typing import List, Dict

class Banco:
    _bancos: Dict[str, List] = {}
    
    def __init__(self, nome: str):
        self.nome = nome
        if nome not in Banco._bancos:
            Banco._bancos[nome] = []
    
    @classmethod
    def listar_bancos(cls) -> List[str]:
        return list(cls._bancos.keys())
    
    def adicionar_conta(self, conta) -> None:
        self._bancos[self.nome].append(conta)
        print(f"Conta {conta.numero} adicionada ao banco {self.nome}")
    
    def listar_contas(self) -> List:
        return self._bancos.get(self.nome, [])
    
    def buscar_conta(self, numero_conta: str) -> object:
        contas = self._bancos.get(self.nome, [])
        for conta in contas:
            if conta.numero == numero_conta:
                return conta
        return None
    
    @classmethod
    def saldo_total_todos_bancos(cls) -> float:
        total = 0.0
        for contas in cls._bancos.values():
            for conta in contas:
                total += conta.saldo
        return total
