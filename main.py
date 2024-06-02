from cliente import Cliente
from conta_corrente import ContaCorrente
print("########## SISTEMA BANCARIO ##########")


def menu():
    return """
    [1] - Sacar
    [2] - Depositar
    [3] - Mostra Transação
    [4] - Sair
    """


def main():
    opcao = 0
    cliente = Cliente("Master Chief","3056930356","15/11/2001","Rua Jose Pacifico")
    conta = ContaCorrente("1",cliente, saldo=1200)
  
    while True:
        print(menu())
        opcao = int(input("Escolha uma das opcoes: "))
        match opcao:
            case 1:
                valor = float(input("Digite o valor de saque: "))
                resultado = conta.sacar(valor)
                print(resultado)
            case 2:
                valor = float(input("Digite o valor de deposito: "))
                resultado = conta.depositar(valor)

                print("Sucesso no deposito" if resultado else "Erro no deposito")
            case 3:      
                historico = conta.historico_transacao
                print(historico)
            case 4:
                print("FIM DO PROGRAMA")
                break



main()
