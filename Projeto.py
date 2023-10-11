from Funcoes import *

quest = int(input("Olá seja bem vindo ao banco, por favor selecione uma das opções disponiveis para continuarmos: \n 1 - Criar conta \n 2 - Já sou cliente \n"))
while(True):

    if quest == 1:
        while(creat() == "sucesso"):
            x = int(input("Digite qual opção queira seguir: \n 1 - Criar nova conta \n 2 - Deletar uma conta \n 3 - Listar todas as contas \n 4 - Debitar valores \n 5 - Depositar \n 6 - Extrato da conta \n 7 - Transferir valores \n 8 - Pagar funcionários \n 9 - Sair \n"))

            if x == 2:
                delet()
                quest = 0
            elif x == 3:
                listar()
                quest = 0
            elif x == 4:
                debito()
                quest = 0
            elif x == 5:
                deposito()
                quest = 0
            elif x == 6:
                extrato()
                quest = 0
            elif x == 7:
                transf()
                quest = 0
            elif x == 8:
                pagar_funcionarios()
                quest = 0
            elif x == 9:
                quest = 0
                break
        quest = 0
        break
    else:
        x = int(input("Digite qual opção queira seguir: \n 1 - Criar nova conta \n 2 - Deletar uma conta \n 3 - Listar todas as contas \n 4 - Debitar valores \n 5 - Depositar \n 6 - Extrato da conta \n 7 - Transferir valores \n 8 - Pagar funcionários \n 9 - Sair \n"))

        if x == 1:
            creat()
        elif x == 2:
            delet()
        elif x == 3:
            listar()
        elif x == 4:
            debito()
        elif x == 5:
            deposito()
        elif x == 6:
            extrato()
        elif x == 7:
            transf()
        elif x == 8:
            pagar_funcionarios()
        elif x == 9:
            break
