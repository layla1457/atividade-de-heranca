from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

class Movimentacao:
    def __init__(self, descricao: str, valor: float, saldo_resultante: float):
        self.data = datetime.now()
        self.descricao = descricao
        self.valor = valor
        self.saldo_resultante = saldo_resultante

    def __str__(self):
        return f"{self.data.strftime('%d/%m %H:%M:%S')} | {self.descricao}: R$ {self.valor:.2f} | Saldo: R$ {self.saldo_resultante:.2f}"

class Conta(ABC):
    def __init__(self, numero: str, titular: str, saldo: float = 0.0):
        if not numero or not numero.strip():
            raise ValueError("Número da conta inválido.")
        if not titular or not titular.strip():
            raise ValueError("Titular inválido.")
        if saldo < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")

        self.numero = numero.strip()
        self.titular = titular.strip()
        self.saldo = saldo
        self.data_criacao = datetime.now()
        self._extrato: List[Movimentacao] = []

    def _registrar(self, descricao: str, valor: float):
        mov = Movimentacao(descricao, valor, self.saldo)
        self._extrato.append(mov)

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def depositar(self, valor: float) -> bool:
        pass

    def extrato(self) -> List[str]:
        return [str(m) for m in self._extrato[-10:]]

    def __str__(self):
        return f"Conta {self.numero} - {self.titular}: R$ {self.saldo:.2f}"

class ContaCorrente(Conta):
    def __init__(self, numero: str, titular: str, saldo: float = 0.0, limite: float = 500.0):
        super().__init__(numero, titular, saldo)
        if limite < 0:
            raise ValueError("Limite não pode ser negativo.")
        self.limite = limite

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self._registrar("Saque", -valor)
            return True
        return False

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        self.saldo += valor
        self._registrar("Depósito", valor)
        return True

class ContaPoupanca(Conta):
    def __init__(self, numero: str, titular: str, saldo: float = 0.0, taxa_juros: float = 0.05):
        super().__init__(numero, titular, saldo)
        if taxa_juros < 0:
            raise ValueError("Taxa de juros inválida.")
        self.taxa_juros = taxa_juros

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        if valor <= self.saldo:
            self.saldo -= valor
            self._registrar("Saque", -valor)
            return True
        return False

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        self.saldo += valor
        self._registrar("Depósito", valor)
        return True

    def render_juros(self) -> float:
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self._registrar("Rendimento", juros)
        return juros
