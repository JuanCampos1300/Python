
def achar_tudo(substring: str, string: str) -> list:
    '''Acha todos as substrings dentro de uma string'''
    resultado = []
    k = 0
    while k < len(string):
        k = string.find(substring, k)
        if k == -1:
            return resultado
        else:
            resultado.append(k)
            k += len(substring)
    return resultado

'''
def ler_zpl(caminho_arquivo):
    #Função que lê um arquivo ZPL
    # Abro o arquivo
    try:
        with open(file=caminho_arquivo, mode='r') as file:
            arquivo = file.read()
    except FileNotFoundError:
        print("\nERRO: Arquivo não encontrado. Abortando.\n")
        return
    except UnicodeDecodeError:
        print("\nERRO: Arquivo não está salvo em ANSI. Abortando.\n")
        return

    # Variáveis pra executar o loop abaixo
    item = []
    pedido = []
    inicio = 0
    # Dou um loop que itera entre as linhas do arquivo
    for linha in arquivo.splitlines():

        # Se achar "^XZ" na linha, então terminou o item
        if "^XZ" in linha:
            # Acrescento a var 'item' no 'pedido'
            pedido.append(list(item))
            # Se esse item estiver vazio, então apago ele
            if pedido[-1] == []:
                pedido.pop(-1)
            # Limpo a var 'item' para acrescentar novos itens nela
            item.clear()



        # Procuro pela substring '^FD' (INÍCIO do campo zebra)
        inicio = linha.find("^FD", 0) + 3
        if inicio < 3:
            # Se não achar o início, então zero a variável e volto pro começo do próximo loop
            inicio = -1
            continue

        # Procuro pela substring '^FS' (FINAL do campo zebra)
        fim = linha.find("^FS", 0)
        if fim < 3 and inicio < fim:
            # Se não achar o fim, então zero as variáveis e volto pro começo do próximo loop
            inicio = -1
            fim = -1
            continue

        # Var 'conteudo' é o que existe entre vars 'inicio' e 'fim'
        conteudo = linha[inicio:fim]
        # Se 'conteudo' ainda não existir dentro da lista 'item', então acrescento
        if conteudo not in item:
            item.append(conteudo)

    for x in pedido:
        print(x, "\n")

    print("Quantidade de itens:", len(pedido), "\n")

ler_zpl("havan.txt")
'''

def ler_zpl_v2(caminho_arquivo: str):
    '''Função que lê um arquivo ZPL (de forma melhorada)'''
    # Abro o arquivo
    try:
        with open(file=caminho_arquivo, mode='r') as file:
            arquivo = file.read()
    except FileNotFoundError:
        print("\nERRO: Arquivo não encontrado. Abortando.\n")
        return
    except UnicodeDecodeError:
        print("\nERRO: Arquivo não está salvo em ANSI. Abortando.\n")
        return
    
    # QTD de vezes que vou dar loop nesse arquivo
    qtd_de_loops = achar_tudo("^FD", arquivo)
    print(len(qtd_de_loops))

ler_zpl_v2("renner.txt")