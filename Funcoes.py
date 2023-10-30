from datetime import datetime
import ast

# dados = {}

todos = []

def creat(): # Função necessária para cadastro de novos clientes
    clientes_dados = open("clientes.txt", "a") # Arquivo com os dados dos clientes
    cliente = {}

    # Aqui estão todos os dados necessários para criação de uma nova conta
    nome = input("Digite a razão social da sua empresa: ")

    if nome == "" or nome == " ": # Valida se o nome digitado foi preenchido
        nome = input("Por favor digite um nome válido: ")
    
    cnpj = int(input("Digite o seu CNPJ: \n"))

    if len(str(cnpj)) < 14: # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj = int(input("Digite um valor válido para CNPJ: \n"))

    tipo = input("Digite o tipo de conta da sua empresa: \n 1 - Comum \n 2 - Plus \n")
    if tipo != '1' and tipo != '2': # Valida se o tipo escolhido existe
        tipo = input("Digite um valor válido para tipo: \n 1 - Comum \n 2 - Plus \n")

    valor = float(input("Digite o valor inicial que quer ter em conta: "))
    if valor < 0: # Valida se o valor inicial da conta não é negativo
        valor = float(input("Digite um valor valido: "))

    senha = input("Digite uma senha para sua conta: ")
    if senha == "" or senha == " ": # Valida se a senha digitada foi preenchido
        senha = input("Por favor digite uma senha válido: ")

    # Aqui os dados solicitados estão entrando em uma lista de clientes para serem levados ao arquivo de dado
    cliente["nome"] = nome
    cliente["cnpj"] = cnpj
    cliente["tipo"] = tipo
    cliente["valor"] = valor
    cliente["senha"] = senha

    todos.append(cliente) # Adiciona os clientes a lista de todos os clientes
    clientes_dados.write(f"{cliente} \n") # Escreve o novo cliente no arquivo
    clientes_dados.close() # Fecha o arquivo e salva os dados
    print("\n Cadastrado com sucesso! \n") # Mensagem de retorno

def delet(): # Função necessária para deletar contas
    clientes_dados = open("clientes.txt", "r") # Arquivo com os dados dos clientes

    clientes_atualizado = [] # lista com os clientes que não serão deletados

    cnpj = int(input("Digite o seu CNPJ: "))
    if len(str(cnpj)) < 14: # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj = int(input("Digite um valor válido para CNPJ: \n")) 

    for a in clientes_dados.readlines(): # Percorre toda a lista de clientes
        dados = ast.literal_eval(a) # transforma a string "a" em dicionario
         
        if dados['cnpj'] != cnpj: # Verifica quais são os clientes com cnpj diferente do informado
            clientes_atualizado.append(a) # Adiciona a lista de clientes que não serão deletados

    clientes_dados.close() # Fecha o arquivo de leitura

    dados_novos = open("clientes.txt", "w") # Abre o arquivo de escrita
    dados_novos.writelines(clientes_atualizado) # Escreve os clientes atualizados
    dados_novos.close() # Fecha o arquivo de escrita
    print("Cliente deletado com sucesso!")        

def listar(): # Função necessária para listar todos os clientes 
    print("Clientes cadastrados: ")
    dados = open("clientes.txt", "r")

    for a in dados.readlines():  # Aqui percorre a lista de todos os clientes
        print(a)  # Exibe todos os clientes um por um

def debito(): # Função necessária para debitar um valor em uma conta
    cnpj = int(input("Digite o seu CNPJ: ")) # CNPJ do titular da conta
    if len(str(cnpj)) < 14: # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj = int(input("Digite um valor válido para CNPJ: \n")) 

    senha = input("Digite a senha da sua conta: ") # Senha desta conta
    if senha == "" or senha == " ": # Valida se a senha digitada foi preenchido
        senha = input("Por favor digite uma senha válido: ")

    valor = float(input("Digite o valor a ser debitado: ")) # Valor a ser debitado
    if valor < 0: # Valida se o valor a ser debitado não é negativo
        valor = float(input("Digite um valor valido: "))

    clientes_dados = open("clientes.txt", "r") # Arquivo com os dados dos clientes

    clientes_atualizado = [] # lista com os dados atualizados

    for a in clientes_dados.readlines(): # Percorre toda a lista de clientes
        dados = ast.literal_eval(a) # transforma a string "a" em dicionario
         
        if dados['cnpj'] == cnpj: # Localiza as infos do cliente
            if dados['senha'] == senha: # Valida senha
                dados['valor'] -= valor # Debita o valor
                clientes_atualizado.append(str(f"{dados} \n"))
        else:
            clientes_atualizado.append(a)

    clientes_dados.close() # Fecha o arquivo de leitura

    dados_novos = open("clientes.txt", "w") # Abre o arquivo de escrita
    dados_novos.writelines(clientes_atualizado)
    dados_novos.close() # Fecha o arquivo de escrita

    print("\n Dinheiro debitado com sucesso ! \n")


def deposito(): # Função necessária para depositar um valor em uma determinada conta
    cnpj = int(input("Digite o seu CNPJ: ")) # CNPJ que irá receber o valor
    if len(str(cnpj)) < 14: # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj = int(input("Digite um valor válido para CNPJ: \n"))

    valor = float(input("Digite o valor a ser depositado: ")) # Valor a ser debitado
    if valor < 0: # Valida se o valor inicial da conta não é negativo
        valor = float(input("Digite um valor valido: "))

    clientes_dados = open("clientes.txt", "r") # Arquivo com os dados dos clientes

    clientes_atualizado = [] # lista com os dados atualizados

    for a in clientes_dados.readlines(): # Percorre toda a lista de clientes
        dados = ast.literal_eval(a) # transforma a string "a" em dicionario
         
        if dados['cnpj'] == cnpj: # Localiza as infos do cliente
            dados['valor'] += valor # Debita o valor
            clientes_atualizado.append(str(f"{dados} \n"))
        else:
            clientes_atualizado.append(a)

    clientes_dados.close() # Fecha o arquivo de leitura

    dados_novos = open("clientes.txt", "w") # Abre o arquivo de escrita
    dados_novos.writelines(clientes_atualizado)
    dados_novos.close() # Fecha o arquivo de escrita
    print("\n Dinheiro depositado com sucesso ! \n")

def extrato(): # Função necessária para exibir o extrato de uma conta 
    cnpj = int(input("Digite o seu CNPJ: ")) # CNPJ do titular da conta
    senha = input("Digite a senha da sua conta: ") # Senha do titular da conta

    print(cnpj)
    print(senha)

def transf(): # Função necessária para fazer transferencia entre contas
    cnpj_origem = int(input("Digite o seu CNPJ: ")) # CNPJ da origem da transferencia
    if len(str(cnpj_origem)) < 14: # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj_origem = int(input("Digite um valor válido para CNPJ: \n"))

    senha = input("Digite a senha da sua conta: ") # Senha da origem da transferencia
    if senha == "" or senha == " ": # Valida se a senha digitada foi preenchido
        senha = input("Por favor digite uma senha válido: ")

    cnpj_destino = int(input("Digite o CNPJ do representante da outra conta: ")) # CNPJ de destino da transferencia
    if len(str(cnpj_destino)) < 14: # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj_destino = int(input("Digite um valor válido para CNPJ: \n"))

    valor = float(input("Digite o valor a ser transferido: ")) # Valor a ser transferido
    if valor < 0: # Valida se o valor não é negativo
        valor = float(input("Digite um valor valido: "))

    cliente_origem = {} # Conta de origem da transação
    cliente_destino = {} # Conta de destino da transação

    for a in range(len(todos)): # Percorre toda a lista de clientes
        for _ in todos[a]: 
            if todos[a][_] == cnpj_origem: # Localiza a conta de origem
                if todos[a]['senha'] == senha: # Valida a senha para transação
                    cliente_origem = todos[a]

    for a in range(len(todos)): # Percorre toda a lista de clientes
        for _ in todos[a]: 
            if todos[a][_] == cnpj_destino: # Localiza a conta de destino
                cliente_destino = todos[a]

    valor_origem = cliente_origem['valor'] - valor # Remove o valor transferido da conta de origem 
    valor_destino = cliente_destino['valor'] + valor # Adiciona o valor transferido a conta de destino

    cliente_origem['valor'] = valor_origem
    cliente_destino['valor'] = valor_destino

    print("\n Valor transferido com sucesso! \n")


def editar_senha(): # Função necessária para alterar senha da conta
    cnpj = int(input("Digite o CNPJ da sua conta: "))
    senha = input("Digite sua senha atual: ")
    nova_senha = input("Digite a nova senha: ")

    for a in range(len(todos)): # Percorre toda a lista de clientes
        for _ in todos[a]: 
            if todos[a][_] == cnpj: # Verfiica se exite o CNPJ digitado
                if todos[a]['senha'] == senha: # Valida a senha do usuario
                    todos[a]['senha'] = nova_senha # Altera o campo senha pela nova senha

                    print("Senha alterada com sucesso!")