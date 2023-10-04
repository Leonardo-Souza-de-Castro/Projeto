def creat(): # Está função é responsável pelo cadastro de novos clientes
    cliente = []

    # Aqui estão todos os dados necessários para criação de uma nova conta
    nome = input("Digite a razão social da sua empresa: ") 
    cnpj = input("Digite o seu CNPJ: ")
    tipo = input("Digite o tipo de conta da sua empresa: ")
    valor = float(input("Digite o valor inicial que quer ter em conta: "))
    senha = input("Digite uma senha para sua conta: ")

    # Aqui os dados solicitados estão entrando em uma lista de clientes para serem levados ao arquivo de dado
    cliente.append(nome)
    cliente.append(cnpj)
    cliente.append(tipo)
    cliente.append(valor)
    cliente.append(senha)

    # Exibição dos dados informados
    print(*cliente)

def delet(): # Função necessária para deletar contas
    cnpj = input("Digite o seu CNPJ: ") 

    print(cnpj)

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