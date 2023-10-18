todos = []

def creat(): # Está função é responsável pelo cadastro de novos clientes
    cliente = {}

    # Aqui estão todos os dados necessários para criação de uma nova conta
    nome = input("Digite a razão social da sua empresa: ")

    if nome == "" or nome == " ":
        nome = input("Por favor digite um nome válido: ")

    cnpj = int(input("Digite o seu CNPJ: \n"))
    # while(True): # Valida se CNPJ digitado tem 14 digitos como o oficial
    #     cnpj = int(input("Digite o seu CNPJ: \n"))

    #     if len(str(cnpj)) < 14:
    #         print("Digite um valor válido para CNPJ")
    
    #     if len(str(cnpj)) == 14:
    #         break

    tipo = input("Digite o tipo de conta da sua empresa: \n 1 - Comum \n 2 - Plus \n")
    
    if tipo != "1" or tipo != '2':
        tipo = input("Por favor digite um tipo de conta válido: \n 1 - Comum \n 2 - Plus \n")


    valor = float(input("Digite o valor inicial que quer ter em conta: "))

    senha = input("Digite uma senha para sua conta: ")
    if senha == "" or senha == " ":
        senha = input("Por favor digite uma senha válido: ")

    # Aqui os dados solicitados estão entrando em uma lista de clientes para serem levados ao arquivo de dado
    cliente["nome"] = nome
    cliente["cnpj"] = cnpj
    cliente["tipo"] = tipo
    cliente["valor"] = valor
    cliente["senha"] = senha

    # Exibição dos dados informados
    # print(*cliente)

    todos.append(cliente)
    print("\n Sucesso! \n")
    return "sucesso"

def delet(): # Função necessária para deletar contas
    cnpj = input("Digite o seu CNPJ: ") 

    for a in range(len(todos)): # Percorre toda a lista de clientes
        for _ in todos[a]: 
            if todos[a][_] == cnpj: # Verfiica se exite o cnpj digitado e o remove
                todos.pop(a)
                print("Cliente deletado com sucesso!")
                

def listar(): # Função necessária para listar todos os clientes 
    print("Aqui serão listados todos os clientes cadastrados!")

    for a in range(len(todos)):
        print(todos[a])

def debito(): # Função necessária para debitar um valor em uma conta
    cnpj = input("Digite o seu CNPJ: ") # CNPJ que irá receber o valor
    senha = input("Digite a senha da sua conta: ") # Senha desta conta
    valor = float(input("Digite o valor a ser debitado: ")) # Valor a ser debitado

    for a in range(len(todos)): # Percorre toda a lista de clientes
        for _ in todos[a]: 
            if todos[a][_] == cnpj: # Verfiica se exite o cnpj digitado e o remove
                if todos[a]['senha'] == senha: # Valida a senha do usuario
                    valor_inicial = todos[a]['valor']
                    todos[a]['valor'] = valor_inicial - valor # Debita o valor do saldo da conta

                    print(todos[a])


def deposito(): # Função necessária para depositar um valor em uma determinada conta
    cnpj = input("Digite o seu CNPJ: ") # CNPJ que irá receber o valor
    valor = float(input("Digite o valor a ser depositado: ")) # Valor a ser debitado

    for a in range(len(todos)): # Percorre toda a lista de clientes
        for _ in todos[a]: 
            if todos[a][_] == cnpj: # Verfiica se exite o cnpj digitado
                valor_inicial = todos[a]['valor']
                todos[a]['valor'] = valor_inicial + valor # Adiciona o deposito ao saldo da conta

                print(todos[a])

def extrato(): # Função necessária para exibir o extrato de uma conta 
    cnpj = input("Digite o seu CNPJ: ") # CNPJ do titular da conta
    senha = input("Digite a senha da sua conta: ") # Senha do titular da conta

    print(cnpj)
    print(senha)

def transf(): # Função necessária para fazer transferencia entre contas
    cnpj_origem = input("Digite o seu CNPJ: ") # CNPJ da origem da transferencia
    senha = input("Digite a senha da sua conta: ") # senha da origem da transferencia
    cnpj_destino = input("Digite o CNPJ do representante da outra conta: ") # CNPJ de destino da transferencia
    valor = float(input("Digite o valor a ser transferido: ")) # valor a ser transferido

    cliente_origem = {} #Conta de origem da transação
    cliente_destino = {} #Conta de destino da transação

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


def pagar_funcionarios(): # Função necessária para pagar os funcionarios
    quant = int(input("Quantos funcionário deseja pagar: "))
    func = []
    info_func = []

    for i in range(0,quant):
        cnpj_destino = input("Digite o CNPJ do representante da outra conta: ") # CNPJ de destino da transferencia
        valor = float(input("Digite o valor a ser transferido: ")) # valor a ser transferido
        func.append(cnpj_destino)
        func.append(valor)

        info_func.append(func)


    cnpj_origem = input("Digite o seu CNPJ: ") # CNPJ da origem da transferencia
    senha_origem = input("Digite a senha da sua conta: ") # senha da origem da transferencia

    print(cnpj_origem)
    print(senha_origem)
    print(*info_func)