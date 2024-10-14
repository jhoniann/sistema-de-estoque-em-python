estoque = {}
def menu():
    print('Estoque na nossa loja')
    print('1 = adicionar produto')
    print('2 = atualizar produto')
    print('3 = visualizar estoque')
    print('4 = sair')
   
def adicionar_produto():
    print('adicionar produto')
    nome = input('qual seria o nome do produto?')
    if nome in estoque:
        print(f'produto {nome} ja cadastrado')
        return
    preco = float(input('Qual seria o preço do produto?'))
    quantidade = int(input('quantas quantidade?'))
    estoque[nome] = {'preço': preco, 'quantidade': quantidade}
    print(f'produto {nome} adicionado com sucesso')

def atualizar():
    print('Atualizando estoque')
    nome = input('Qual o nome do estoque que voce queria atualizar?')
    if nome not in estoque:
        print(f'o produto {nome} nao esta cadastrado no nosso estoque')
    novopreço = float(input('digite novo o preço'))
    novaaquantidade = int(input('digite nova quantidade'))
    estoque[nome]['preço'] = novopreço
    estoque[nome]['quantidade'] = novaaquantidade
    print(f"o produto '{nome}' foi atualizado!")

def visualizar ():
    print("Estoque atual:")
    print("PRODUTO\t\tPREÇO\t\tQUANTIDADE")
    for produto,info in  estoque.items():
        print(f"{produto}\t\tR$ {info['preço']:.2f}\t\t{info['quantidade']}")
while True:
    menu()
    opçao = int(input('digite a opção'))
    if opçao == 1:
        adicionar_produto()
    elif opçao == 2:
        atualizar()
    elif opçao == 3:
        visualizar()
    elif opçao == 4:
        print('saindo do sistema')
        break
    else:
        print('Numero errado! por favor digite de 1 a 4')
        