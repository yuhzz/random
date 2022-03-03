p = int(input('Digite o primeiro termo da P.A:\n'))
r = int(input('Digite a razão da P.A:\n'))
y = int(input('Digite o número de termos da P.A:\n'))
l = p + (y - 1) * r
S = ((p + l) * y) / 2
print('O termo geral é {}'.format(l))
print ('A soma dos termos é {}'.format(S))
