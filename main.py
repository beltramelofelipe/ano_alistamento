from datetime import date
data_atual = date.today()
data_em_texto = data_atual.strftime('%Y')
data_nascimento = int(input('Digite o ano de nascimento '))
idade = int(data_em_texto) - data_nascimento

if (idade < 18):
   print('Você ainda não precisa se alistarar')
   print('Ainda faltam {} anos '.format(18 - idade))
elif(idade == 18):
  print('Você já pode se alistar esse ano' )
else:
  print('Já passou o tempo para alistamento ')
  print('Você perdeu o prazo há {} anos!!!'.format(idade - 18))

 