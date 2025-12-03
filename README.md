# atividade-de-heranca
O sistema é dividido em 3 arquivos que trabalham juntos, seguindo POO com herança, abstração e polimorfismo. Cada arquivo tem uma responsabilidade específica.

# ARQUIVO CONTAS
Responsabilidade: Define todos os tipos de conta e suas regras de negócio.

- Conta(ABC): Classe abstrata (modelo base)Atributos comuns: numero, titular, saldo, data_criacao, _extrato
      Métodos obrigatórios: sacar() e depositar() (sem implementação)
      Métodos comuns: extrato() (últimas 5 movimentações)
- ContaCorrente(Conta): Herda de Conta
      Regra especial: Saque até saldo + limite (padrão R$500)
      Exemplo: Saldo R$100 + limite R$500 = pode sacar até R$600
- ContaPoupanca(Conta): Herda de Conta
      Regra especial: Saque apenas até o saldo (sem limite)
      Método extra: render_juros() (5% ao ano por chamada)
  
# ARQUIVO BANCO
Responsabilidade: Controla múltiplos bancos e suas contas.
Estrutura interna: _bancos = { "BancoX": [conta1, conta2], "BancoY": [...] }

- Métodos:
  listar_bancos()
  adicionar_conta(conta)
  listar_contas()
  buscar_conta(numero)
  saldo_total_todos_bancos()
  
# ARQUIVO MENU
Responsabilidade: Menu interativo com input() e print().
