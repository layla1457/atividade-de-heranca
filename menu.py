from banco import Banco
from contas import ContaCorrente, ContaPoupanca

def exibir_menu_principal():
    print("\n" * 3)
    print("🏦" + "="*50 + "🏦")
    print("         SISTEMA BANCÁRIO INTERATIVO")
    print("🏦" + "="*50 + "🏦")
    print("[1] Listar Bancos")
    print("[2] Criar Banco")
    print("[3] Selecionar Banco")
    print("[4] Saldo Total Sistema")
    print("[0] Sair")
    print("="*55)

def exibir_menu_banco(nome_banco):
    print("\n" * 3)
    print(f"🏦 BANCO {nome_banco.upper()} 🏦")
    print("="*45)
    print("[1] Listar Contas")
    print("[2] Criar Conta Corrente")
    print("[3] Criar Conta Poupança")
    print("[4] Buscar Conta")
    print("[5] Operações na Conta")
    print("[0] Voltar")
    print("="*45)

def criar_banco_interativo():
    nome = input("Nome do banco: ").strip().title()
    if nome:
        banco = Banco(nome)
        print(f"Banco '{nome}' criado com sucesso! ✓")
    else:
        print("Nome inválido!")
    input("\nPressione Enter para continuar...")

def menu_operacoes_conta(conta):
    while True:
        print("\n" * 3)
        print(f"CONTA: {conta.numero} - {conta.titular}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        print("="*40)
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Render Juros (Poupança)")
        print("[0] Voltar")
        print("="*40)
        
        op = input("Escolha: ").strip()
        
        if op == "1":
            try:
                valor = float(input("Valor do depósito: R$ "))
                if conta.depositar(valor):
                    print("Depósito realizado!")
                else:
                    print("Falha no depósito!")
            except ValueError:
                print("Valor inválido!")
                
        elif op == "2":
            try:
                valor = float(input("Valor do saque: R$ "))
                if conta.sacar(valor):
                    print("Saque realizado!")
                else:
                    print("Falha no saque!")
            except ValueError:
                print("Valor inválido!")
                
        elif op == "3":
            print("\n📋 EXTRATO (últimas 5 movimentações):")
            for mov in conta.extrato():
                print(f"> {mov}")
            if not conta.extrato():
                print("Nenhuma movimentação.")
                
        elif op == "4":
            if hasattr(conta, 'render_juros'):
                juros = conta.render_juros()
                print(f"Juros rendidos: R$ {juros:.2f}")
            else:
                print("Operação disponível apenas para Poupança!")
                
        elif op == "0":
            break
            
        input("\nPressione Enter para continuar...")

def main():
    print("Iniciando Sistema Bancário...")
    
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            print("\nBancos cadastrados:")
            bancos = Banco.listar_bancos()
            if bancos:
                for i, banco in enumerate(bancos, 1):
                    contas = Banco._bancos.get(banco, [])
                    print(f"  {i}. {banco} ({len(contas)} contas)")
            else:
                print("Nenhum banco cadastrado.")
                
        elif opcao == "2":
            criar_banco_interativo()
            
        elif opcao == "3":
            bancos = Banco.listar_bancos()
            if not bancos:
                print("Nenhum banco disponível!")
                input("\nPressione Enter...")
                continue
                
            print("\nSelecione o banco:")
            for i, banco in enumerate(bancos, 1):
                print(f"  {i}. {banco}")
            
            try:
                idx = int(input("Número: ")) - 1
                banco_nome = bancos[idx]
                banco = Banco(banco_nome)
                
                while True:
                    exibir_menu_banco(banco_nome)
                    op_banco = input("Escolha: ").strip()
                    
                    if op_banco == "1":
                        contas = banco.listar_contas()
                        if contas:
                            for i, conta in enumerate(contas, 1):
                                print(f"  {i}. {conta}")
                        else:
                            print("Nenhuma conta neste banco.")
                            
                    elif op_banco == "2":
                        numero = input("Número da conta: ")
                        titular = input("Titular: ")
                        saldo = float(input("Saldo inicial: R$ ") or 0)
                        limite = float(input("Limite (padrão 500): R$ ") or 500)
                        cc = ContaCorrente(numero, titular, saldo, limite)
                        banco.adicionar_conta(cc)
                        
                    elif op_banco == "3":
                        numero = input("Número da conta: ")
                        titular = input("Titular: ")
                        saldo = float(input("Saldo inicial: R$ ") or 0)
                        cp = ContaPoupanca(numero, titular, saldo)
                        banco.adicionar_conta(cp)
                        
                    elif op_banco == "4":
                        numero = input("Número da conta: ")
                        conta = banco.buscar_conta(numero)
                        if conta:
                            print(f"Conta encontrada: {conta}")
                        else:
                            print("Conta não encontrada!")
                            
                    elif op_banco == "5":
                        numero = input("Número da conta: ")
                        conta = banco.buscar_conta(numero)
                        if conta:
                            menu_operacoes_conta(conta)
                        else:
                            print("Conta não encontrada!")
                            
                    elif op_banco == "0":
                        break
                        
                    else:
                        print("Opção inválida!")
                    
                    input("\nPressione Enter para continuar...")
                    
            except (ValueError, IndexError):
                print("Opção inválida!")
                input("\nPressione Enter...")
                
        elif opcao == "4":
            total = Banco.saldo_total_todos_bancos()
            print(f"Saldo total do sistema: R$ {total:.2f}")
            
        elif opcao == "0":
            print("Obrigado por usar o Sistema Bancário!")
            break
            
        else:
            print("Opção inválida!")
            
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()

