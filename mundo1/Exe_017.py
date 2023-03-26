import math
ca = float(input('informe o cateto adjacente:\n'))
co = float(input('informe o cateto oposto:\n'))
hi = math.hypot(ca, co)
print('O trinangulo ce catetos {} e {} tem um ahipotenusa {}'.format(ca, co, hi))
