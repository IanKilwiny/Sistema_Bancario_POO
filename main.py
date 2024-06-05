from cliente import Cliente
from conta_corrente import ContaCorrente

print("########## SISTEMA BANCARIO ##########")


def menu():
    return """
    [1] - Sacar
    [2] - Depositar
    [3] - Mostra Transação
    [4] - Criar Usuário
    [5] - Criar conta
    [6] - Sair
    """

def criar_cliente(nome, cpf, data_nasc, endereco):
    cliente = Cliente(nome,cpf,data_nasc, endereco)
    return cliente


def criar_conta(numero, cliente, saldo):
    contas = ContaCorrente(numero,cliente, saldo)
    return contas

def sacar(valor, conta):
    resultado = conta.sacar(valor)
    return resultado

def depositar(valor, conta):
    resultado = conta.depositar(valor)

    return True

def extrato(conta):
   
    print("#############EXTRATO###############")
    for value in conta.historico_transacao:
        print("\n-------------------------")
        print("Tipo:",value["tipo"])
        print("Valor:",value["valor"])
        print("data-hora:",value["data"])
        print("\n------------------------")

    print("Saldo:",conta.saldo)

    print("####################################")

def main():
    cliente = None
    contas = None
    opcao = 0
    num_contas =1

    while True:
        print(menu())
        opcao = int(input("Escolha uma das opcões: "))
        match opcao:
            case 1:
                valor = float(input("Digite o valor de saque: "))
                sacar(valor, contas)
                #print(resultado)
            case 2:
                valor = float(input("Digite o valor de depósito"))
                resultado = depositar(valor, contas)
                print("Sucesso no deposito" if resultado else "Error no depósito")
            case 3:      
<<<<<<< HEAD
                
=======
        
>>>>>>> main
                extrato(contas)
            case 4:
                nome = input("Digite o seu nome: ")
                cpf = input("Digite seu cpf: ")
                data_nasc= input("Digite sua data de nascimento: ")
                endereco = input("Digite seu endereço: ")
<<<<<<< HEAD
                cliente = criar_cliente(nome, cpf, data_nasc, endereco)
=======
                cliente = criar_cliente("Ian","12345","13/09/2004", "rua jose sá")
>>>>>>> main
                print("Cliente criado")
                
            case 5:
                saldo = float(input("Digite o saldo dessa nova conta: "))
                contas = criar_conta(num_contas, cliente, saldo)
                print("Conta criada!")

            case 6:
                print("FIM DO PROGRAMA")
                break

    
main()
