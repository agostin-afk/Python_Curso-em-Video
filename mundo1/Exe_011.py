alt = float(input('informe a altura da parede a ser pintada: '))
larg = float(input('informe a largura da parede a ser pintada: '))
area = alt * larg
quant_tinta = area/2
print('Para pintar a sua parede de area {:.2f}m² são necessarios {:.1f} litros de tinta'.format(area, quant_tinta))
