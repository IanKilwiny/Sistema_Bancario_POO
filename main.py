from cliente import Cliente
from conta_corrente import ContaCorrente
from datetime import datetime

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
    cliente = Cliente(nome, cpf, data_nasc, endereco)
    return cliente


def criar_conta(numero, cliente, saldo):
    contas = ContaCorrente(numero, cliente, saldo)
    return contas


def sacar(valor, conta):
    resultado = conta.sacar(valor)
    return resultado


def depositar(valor, conta):
    resultado = conta.depositar(valor)

    return True


def filtro_transacao(conta, data_atual, num_transacoes, limite_transacao):

    if num_transacoes == 0 or (
        conta.historico_transacao[0]["data"] == data_atual
        and num_transacoes < limite_transacao
    ):
        return True

    return False


def num_transacoes(conta):
    return len(conta.historico_transacao)


def extrato(conta):

    print("#############EXTRATO###############")
    for value in conta.historico_transacao:
        print("\n-------------------------")
        print("tipo:", value["tipo"])
        print("valor:", value["valor"])
        print("hora:", value["hora"])
        print("data:", value["data"])
        print("\n------------------------")

    print("Saldo:", conta.saldo)
    print("Número de transações:", num_transacoes(conta))

    print("####################################")


def main():
    cliente = None
    contas = None
    opcao = 0
    num_contas = 1
    data_atual = datetime.now().strftime("%d/%m/%y")
    LIMITE_TRANSACAO = 10

    while True:
        print(menu())
        opcao = int(input("Escolha uma das opcões: "))
        match opcao:
            case 1:

                if filtro_transacao(
                    contas, data_atual, num_transacoes(contas), LIMITE_TRANSACAO
                ):
                    valor = float(input("Digite o valor de saque: "))
                    saque = sacar(valor, contas)
                    print(saque)

                else:
                    print("Você atingiu o limite de transações diária")

            case 2:
                if filtro_transacao(
                    contas, data_atual, num_transacoes(contas), LIMITE_TRANSACAO
                ):
                    valor = float(input("Digite o valor de depósito: "))
                    resultado = depositar(valor, contas)
                    print("Sucesso no deposito" if resultado else "Error no depósito")
                else:
                    print("Você atingiu o limite de transacões possíveis")
            case 3:
                extrato(contas)
            case 4:
                nome = input("Digite o seu nome: ")
                cpf = input("Digite seu cpf: ")
                data_nasc = input("Digite sua data de nascimento: ")
                endereco = input("Digite seu endereço: ")

                cliente = criar_cliente(nome, cpf, data_nasc, endereco)
                print("Cliente criado")

            case 5:
                saldo = float(input("Digite o saldo dessa nova conta: "))
                contas = criar_conta(num_contas, cliente, saldo)
                print("Conta criada!")

            case 6:
                print("FIM DO PROGRAMA")
                break


main()
