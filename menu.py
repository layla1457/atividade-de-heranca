from banco import Banco
from contas import ContaCorrente, ContaPoupanca

def input_float(msg: str):
    try:
        return float(input(msg).replace(",", "."))
    except:
        return None

def menu_operacoes_conta(conta):
    while True:
        print(f"\nConta: {conta.numero} - {conta.titular}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        print("1) Depositar")
        print("2) Sacar")
        print("3) Extrato")
        if isinstance(conta, ContaPoupanca):
            print("4) Render Juros")
        print("0) Voltar")

        op = input("Escolha: ")
        if op == "1":
            valor = input_float("Valor: R$ ")
            if valor is None or not conta.depositar(valor):
                print("Falha no depósito.")
        elif op == "2":
            valor = input_float("Valor: R$ ")
            if valor is None or not conta.sacar(valor):
                print("Falha no saque.")
        elif op == "3":
            print("\nExtrato:")
            extr = conta.extrato()
            print("\n".join(extr) if extr else "Sem movimentações.")
        elif op == "4" and isinstance(conta, ContaPoupanca):
            juros = conta.render_juros()
            print(f"Juros aplicados: R$ {juros:.2f}")
        elif op == "0":
            break

def main():
    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1) Listar Bancos")
        print("2) Criar Banco")
        print("3) Selecionar Banco")
        print("4) Saldo Total do Sistema")
        print("0) Sair")

        op = input("Opção: ")

        if op == "1":
            bancos = Banco.listar_bancos()
            print("Bancos cadastrados:", bancos or "Nenhum")

        elif op == "2":
            nome = input("Nome do banco: ")
            Banco(nome)
            print("Banco criado.")

        elif op == "3":
            bancos = Banco.listar_bancos()
            if not bancos:
                print("Nenhum banco disponível.")
                continue

            print("Bancos:")
            for i, b in enumerate(bancos, 1):
                print(f"{i}) {b}")

            try:
                idx = int(input("Escolha: ")) - 1
                nome_banco = bancos[idx]
            except:
                print("Inválido.")
                continue

            banco = Banco(nome_banco)

            while True:
                print(f"\n=== BANCO {banco.nome} ===")
                print("1) Listar Contas")
                print("2) Criar Corrente")
                print("3) Criar Poupança")
                print("4) Buscar Conta")
                print("5) Operar Conta")
                print("0) Voltar")

                op2 = input("Escolha: ")

                if op2 == "1":
                    contas = banco.listar_contas()
                    print(*contas, sep="\n") if contas else print("Sem contas.")

                elif op2 == "2":
                    numero = input("Número: ")
                    titular = input("Titular: ")
                    saldo = input_float("Saldo inicial: ") or 0
                    limite = input_float("Limite: ") or 500
                    try:
                        banco.adicionar_conta(ContaCorrente(numero, titular, saldo, limite))
                    except Exception as e:
                        print("Erro:", e)

                elif op2 == "3":
                    numero = input("Número: ")
                    titular = input("Titular: ")
                    saldo = input_float("Saldo inicial: ") or 0
                    try:
                        banco.adicionar_conta(ContaPoupanca(numero, titular, saldo))
                    except Exception as e:
                        print("Erro:", e)

                elif op2 == "4":
                    num = input("Número: ")
                    conta = banco.buscar_conta(num)
                    print(conta if conta else "Não encontrada.")

                elif op2 == "5":
                    num = input("Número: ")
                    conta = banco.buscar_conta(num)
                    if not conta:
                        print("Conta não encontrada.")
                    else:
                        menu_operacoes_conta(conta)

                elif op2 == "0":
                    break

        elif op == "4":
            print(f"Saldo total: R$ {Banco.saldo_total():.2f}")

        elif op == "0":
            print("Encerrando...")
            break

if __name__ == "__main__":
    main()
