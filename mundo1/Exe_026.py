stg = input('Insira uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes'.format(stg.count('A')))
print('Ela aparece pela primeira vez no caracter {} e na ultima vez no {}'. format(stg.find('A')+1, stg.rfind('A')+1))
