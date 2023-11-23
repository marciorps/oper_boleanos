# VAmos pensar por exemplo no seguinte:
idade = 21
possui_convite = False
filho_do_dono = True
print((idade >= 21) and (possui_convite == True))
print(idade >= 21 or possui_convite == True)
# maior que 21 e possui convite ou seja filho do dono
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

#exemplo
maior_de_idade = True
possui_carteira_de_trabalho = False
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
#você só pode trabalhar aqui se for maior de idade e possuir carteira de trabalho
print(maior_de_idade == True and possui_carteira_de_trabalho)
# Queremos contratar pessoas que ainda não posuem um veiculo proprio, mas já possuam uma carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)


# Exercicio
## Quero que você defina as seguintes variáveis, inicialmente todas com false, a ideia aqui é de se importar com os
##valores dentro dessas variáveis, mas sim como montar condicionais
possui_passaporte = True
passagem_comprada = True
menor_de_idade = False

##Crie as seguintes condições e imprima o resultado na tela

#1 Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade
print((possui_passaporte and passagem_comprada) and not menor_de_idade)

#2 Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

#3 Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)

#4 Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)


