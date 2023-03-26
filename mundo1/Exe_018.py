import math
ang = float(input('Informe um angulo: '))
angulo = math.radians(ang)
seno = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)
print('O seno, cosseno e tangente de {}° são respectivamente: {:.2f}, {:.2f} e {:.2f}'.format(ang, seno, cos, tang))
