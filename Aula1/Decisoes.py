#Agora vamos ver um pouco da condição 'IF'
#Este comando será responsável por acrescentarmos ao nosso bloco de código a inteligência da tomada de decisão, tornando-o mais independente
#Podemos utilizar o if em três estruturas distintas:

#DECISÕES SIMPLES
#Desiçoes simples são casos mais comuns e corriqueiros que existão dentro de um código, veja este exemplo:
from email.errors import InvalidMultipartContentTransferEncodingDefect


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
prioridade = 'Não'
if idade>= 65:
    prioridade='Sim'
print('O paciente ' + nome + ' possui atendimento prioritario? ' + prioridade)


#Decisões compostas
#São formadas para o direcionamento caso a condição seja verdadeira e caso seja falsa, para isso usaremos o else:
nome= input('Digite um nome: ')
idade=int(input('Digite a idade: '))
if idade>=65:
    print('O paciente ' + nome + " Possui atendimento prioritario!")
else:
    print('O paciente ' + nome + ' Não possui atendimento prioritario!')

#Outra forma de exemplo seria se um paciente tivesse uma doença infecto contagiosa e não podesse ficar na mesma sala que os demais
nome= input('Digite um nome: ')
idade=int(input('Digite a idade: '))
doenca= input('Você possui alguma doença contagiosa?: ').upper
if idade>=65:
    print('O paciente ' + nome + " Possui atendimento prioritario!")
elif doenca == 'SIM':
    print('O paciente ' + nome + "Possui doença contagiosa e deve ir para uma sala reservada.") 
else:
    print('O paciente ' + nome + 'Não possui atendimento prioritario!')

#Porém vamos pensar na seguinte situação, e se o paciente tiver idade igual ou mairo a 65 anos e também pussuir suspeita de doença contagiosa?
#Nesse caso utilizaremos os operadores "And" ou "Or"
#Há uma diferença entre os operadores and e or, procure no google para mais informações
nome=input("Digite um nome: ")
idade= int(input('Digite sua idade: '))
doenca = input('Possui alguma doença contagiosa?: ').upper()
if idade>=65 and doenca=='SIM':
    print('O paciente será direcionado para a sala AMARELA - com prioridade')
elif idade < 65 and doenca == 'SIM':
    print('O Paciente será direcionado para a sala AMARELA - sem prioridade')
elif idade>=65 and doenca=='NAO':
    print('O paciente não sera direcionado para a sala AMARELA e sim para a BRANCA - com prioridade')
elif idade < 65 and doenca =='NAO':
    print('O paciente não será direcionado para a sala AMARELA e sim para a BRANCA - sem prioridade')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')

#DECISÕES ENCADEADAS
#As decisões encadeadas servem para avaliarmos uma situação e, dependendo da situação, serão tomadas algumas outras decisões
#O código com decisões encadeadas( Aninhadas ) ficara assim:
nome=input("Digite um nome: ")
idade= int(input('Digite sua idade: '))
doenca = input('Possui alguma doença contagiosa?: ').upper
if idade>=65:
    print('Paciente COM prioridade')
    if doenca=='SIM':
        print('Encaminhe o paciente para a sala AMARELA')
    elif doenca == 'NAO':
        print('Encaminhe o paciente para a sala BRANCA')
    else:
        print('Responda a pergunta da doença com SIM ou NAO')
else:
    print('Paciente SEM prioridade')
    if doenca == 'SIM':
        print('Encaminhe o paciente para a sala AMARELA')
    elif doenca ==  'NAO':
        print('Encaminhe o paciente para a sala BRANCA')
    else:
        print('Responda com SIM ou NÃO')

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca=="NAO":
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print('paciente COM prioridade')
else:
    genero= input('Digite o gênero do paciente: ').upper()
    if genero == 'FEMININO' and idade>10:
        gravidez=input('A Paciente está grávida?: ')
        if gravidez== 'SIM':
            print('Paciente COM prioridade!')
        else:
            print('Paciente SEM prioridade')
    else:
        print('Paciente SEM prioridade')
  