n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[1;31mREPROVADO! ,voçê não atingiu a nota necessária\033[m')
elif media >= 5 and  media <= 6.9:
    print('\033[1;35mRECUPERAÇÃO!, voçê ficou de reuperação.\033[m')
else:
    print('\033[1;36mAPROVADO!, voçê obteve média suficiente\033[m')