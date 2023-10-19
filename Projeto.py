from Funcoes import *

quest = int(input("Olá seja bem vindo ao banco, por favor selecione uma das opções disponiveis para continuarmos: \n 1 - Criar conta \n 2 - Já sou cliente \n"))
while(True):

    if quest == 1:
        creat()
        quest = 2
        
    else:
        x = int(input("Digite qual opção queira seguir: \n 1 - Criar nova conta \n 2 - Deletar uma conta \n 3 - Listar todas as contas \n 4 - Debitar valores \n 5 - Depositar \n 6 - Extrato da conta \n 7 - Transferir valores \n 8 - Alterar senha \n 9 - Sair \n"))

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
            editar_senha()
        elif x == 9:
            break
