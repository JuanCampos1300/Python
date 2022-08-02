"""
 * Criar variáveis  para nome (str), idade (int),
 * Altura (float) e peso (float ) de uma pessoa,
 * Criar variável com o ano atul (int),
 * Obter o ano de nascimento de pessoa (baseado na idade e no ano atual),
 * Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa),
 * Exibir um texto com todos os valores na tela usado F-string (com as chaves)


"""
nome = 'Juan Campos' #str
anos = 20 #int 
altura = 1.73  #float
ano_anual = 2022
nascimento = ano_anual - anos
peso = 66
imc= peso / (altura**2)

print(f'meu nome é {nome}, tenho {anos} anos, nasci em { nascimento}, tenho {peso} peso e possuo um imc de {imc:.2f} ')
