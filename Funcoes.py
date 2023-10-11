todos = []

def creat(): # Está função é responsável pelo cadastro de novos clientes
    cliente = {}

    # Aqui estão todos os dados necessários para criação de uma nova conta
    nome = input("Digite a razão social da sua empresa: ")
    while(True): # Valida se CNPJ digitado tem 14 digitos como o oficial
        cnpj = int(input("Digite o seu CNPJ: \n"))

        if len(str(cnpj)) < 14:
            print("Digite um valor válido para CNPJ")
    
        if len(str(cnpj)) == 14:
            break

    tipo = input("Digite o tipo de conta da sua empresa: \n 1 - Comum \n 2 - Plus \n")
    valor = float(input("Digite o valor inicial que quer ter em conta: "))
    senha = input("Digite uma senha para sua conta: ")

    # Aqui os dados solicitados estão entrando em uma lista de clientes para serem levados ao arquivo de dado
    cliente["nome"] = nome
    cliente["cnpj"] = cnpj
    cliente["tipo"] = tipo
    cliente["valor"] = valor
    cliente["senha"] = senha

    # Exibição dos dados informados
    # print(*cliente)

    todos.append(cliente)
    print("Sucesso!")
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

def debito(): # Função necessária para debitar um valor em uma conta
    cnpj = input("Digite o seu CNPJ: ") # CNPJ que irá receber o valor
    senha = input("Digite a senha da sua conta: ") # Senha desta conta
    valor = float(input("Digite o valor a ser debitado: ")) # Valor a ser debitado

    print(cnpj)
    print(senha)
    print(valor)

def deposito(): # Função necessária para depositar um valor em uma determinada conta
    cnpj = input("Digite o seu CNPJ: ") # CNPJ da conta titular
    valor = int(input("Digite o valor a ser depositado: ")) # Valor a ser recebido

    print(cnpj)
    print(valor)

def extrato(): # Função necessária para exibir o extrato de uma conta 
    cnpj = input("Digite o seu CNPJ: ") # CNPJ do titular da conta
    senha = input("Digite a senha da sua conta: ") # Senha do titular da conta

    print(cnpj)
    print(senha)

def transf(): # Função necessária para fazer transferencia entre contas
    cnpj_origem = input("Digite o seu CNPJ: ") # CNPJ da origem da transferencia
    senha_origem = input("Digite a senha da sua conta: ") # senha da origem da transferencia
    cnpj_destino = input("Digite o CNPJ do representante da outra conta: ") # CNPJ de destino da transferencia
    valor = float(input("Digite o valor a ser transferido: ")) # valor a ser transferido

    print(cnpj_origem)
    print(senha_origem)
    print(cnpj_destino)
    print(valor)

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