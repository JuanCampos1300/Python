# para facilitar o uso de string é só colocar um f primeiro ex:

nome = 'Juan Campos' #str
anos = 19  #int 
altura = 1.73  #float
e_maior = anos >= 18  #bool
peso = 66
imc= peso / (altura**2)

print('nome: ', nome)
print('anos: ', anos )
print('altura: ', altura )
print('é maior: ', e_maior)

  #podemos cálcular váviaves;
print(anos * altura)

 # Cálcule o imc da pessoa; 
print(nome, 'tem', anos, 'anos  e seu imc é', imc)

# de vez de fazermos igual está em cima só colocar um f antes:
 
print(f' {nome } tem {anos} anos de idade e seu imc é {imc}')

# para que imc ou qualquer valor flutuante exiba duas casas decimais é so colocar a "variave ou resultado:.2f" exemplo
print(f'{nome} tem {anos } anos de iadade e seu imc é {imc:.2f}')
print(f'juan campos do nascimento', 'oi', sep='-')