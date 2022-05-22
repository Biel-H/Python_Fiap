#Ola! este é mais um repositorio com anotações sobre python, porém desta vez usando uma outra metodologia de ensino
#Vamos começar usando as variáveis:

nome = "Humberto delegado"
empresa = 'Fiap'
qntde_funcionarios = 500
mediaMensalidade = 856.50
print(nome + " trabalha na empresa " + empresa)
print("possui :", qntde_funcionarios, " funcionarios.")
print('A méida da mensalidade é de: ' + str(mediaMensalidade))

#Aqui cada variável é usada separadamente por textos, assim como virgulas ou sinais de +
#Também pode ser feita de forma diferente usando os "Inputs":

nome = input('Digite um nome de funcionario: ')
empresa = input('Digite a intituição: ')
qntde_funcionarios = int(input('Digite a quantidade de funcionarios: '))
mediaMensalidade = float(input('Digite a média da mensalidade: '))
print(nome + " trabalha na empresa " + empresa)
print("possui :", qntde_funcionarios, " funcionarios.")
print('A méida da mensalidade é de: ' + str(mediaMensalidade))

#Agora usaremos outra importante função, o type()
#Ele retorna o tipo do dado do que estiver dentro dos seus parênteses, conforme obsevamos no código abaixo:
nome = input('Digite um nome de funcionario: ')
empresa = input('Digite a intituição: ')
qntde_funcionarios = int(input('Digite a quantidade de funcionarios: '))
mediaMensalidade = float(input('Digite a média da mensalidade: '))
print(nome + " trabalha na empresa " + empresa)
print("possui :", qntde_funcionarios, " funcionarios.")
print('A méida da mensalidade é de: ' + str(mediaMensalidade))
print(7 * '=' 'Verifique os tipos dos dados abaixo' 7*'=')
print('O tipo de dado da variavel [nome] é: ', type(nome))
print('O tipo de dado da variavel [empresa] é: ', type(empresa))
print('O tipo de dado da variabel [qntde_funcionarios] é: ', type(qntde_funcionarios))
print('O tipo de dado da variabel [mediaMensalidade] é: ', type(mediaMensalidade))

