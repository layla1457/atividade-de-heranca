# atividade-de-heranca
O sistema é dividido em 3 arquivos que trabalham juntos, seguindo POO com herança, abstração e polimorfismo. Cada arquivo tem uma responsabilidade específica.

# ARQUIVO CONTAS
Responsabilidade: Define todos os tipos de conta e suas regras de negócio.

- Conta(ABC): Classe abstrata (modelo base) Atributos comuns: numero, titular, saldo, data_criacao, _extrato
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

# Atualização após a análise do código feito pelo ChatGPT.

O código apresenta uma estrutura decente. Uma boa prática é o uso de classe abstrata (conta). Uma classe abstrata é como um modelo incompleto que não pode ser criado diretamente. Ela define métodos que suas subclasses precisam implementar, ajudando a manter um padrão comum e facilitando a reutilização do código, mesmo quando a estrutura é simples. Foi uma sugestão dada após refinamento do código original.

Porém, o código faz uma validação dinâmica parcial. Por exemplo, só é aceitado valores positivos no saque e depósito. No saque, só ocorre se houver saldo suficiente. E o menu trata de erros de ValueError em entradas numéricas. 

- Não tem validação:

	❌ Número de conta duplicado dentro do banco.
	❌ Titular vazio ou inválido.
	❌ Valor zero (0) é considerado inválido? Não está claro.
	❌ Tipo de dado dos campos não é validado no construtor.
	❌ Criar banco com nome repetido apenas reutiliza — isso pode ser intencional, mas é confuso.

	➡ Você faz verificações básicas, mas não há validação dos dados no nível das classes.

Criticas: 

      A) Banco._bancos é um atributo de classe — isso pode gerar confusão.
      Todas as instâncias do Banco compartilham os mesmos dados.

	Criar Banco("X") duas vezes não cria dois bancos — só retorna a 	mesma lista de contas.

	📌 Funciona, mas não é muito intuitivo para quem for manter o código.

	B) Validação ao criar contas

		- Antes de adicionar:
		- verificar se o número já existe,
		- se os tipos são certos,
		- se o saldo inicial é válido.

	C) Extrato é uma lista sem limite e sem timestamps

	D) Conta deveria ter métodos de validação centralizados

	E) Banco.listar_bancos expõe a estrutura interna

Após desse estudo, a IA reescreveu o código em uma maneira mais estruturada. Segue os próximos commits. 
