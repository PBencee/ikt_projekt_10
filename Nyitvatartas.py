ora = int(input('Mennyi az idő? '))

if (ora >= 8 and ora <= 16):

    print ('A Bolt Nyitva Van')
    print ('még ennyit van nyitva',16-ora,'órát')
else: 
    print('A bolt zárva van.')
if (8 > ora): 
    print ('A bolt ekkor nyit:',8 - ora)
elif ( 16 < ora ):
    print ('A bolt ekkor nyit:',24 - ora + 8)