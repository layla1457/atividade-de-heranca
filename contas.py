from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

class Conta(ABC):
    def __init__(self, numero: str, titular: str, saldo: float = 0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.data_criacao = datetime.now()
        self._extrato = []
    
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass
    
    @abstractmethod
    def depositar(self, valor: float) -> bool:
        pass
    
    def extrato(self) -> List[str]:
        return self._extrato[-5:]
    
    def __str__(self):
        return f"Conta {self.numero} - {self.titular}: R$ {self.saldo:.2f}"

class ContaCorrente(Conta):
    def __init__(self, numero: str, titular: str, saldo: float = 0.0, limite: float = 500.0):
        super().__init__(numero, titular, saldo)
        self.limite = limite
    
    def sacar(self, valor: float) -> bool:
        if valor > 0 and (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self._extrato.append(f"Saque: -R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
            return True
        return False
    
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self._extrato.append(f"Depósito: +R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, numero: str, titular: str, saldo: float = 0.0, taxa_juros: float = 0.05):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros
    
    def sacar(self, valor: float) -> bool:
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self._extrato.append(f"Saque: -R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
            return True
        return False
    
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self._extrato.append(f"Depósito: +R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
            return True
        return False
    
    def render_juros(self) -> float:
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self._extrato.append(f"Juros: +R$ {juros:.2f} | Saldo: R$ {self.saldo:.2f}")
        return juros
