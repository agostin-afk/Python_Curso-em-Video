def notas(*num, sit=False):
    r = dict()
    r['Total'] = len(num)
    r['Média'] = sum(num)/len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] > 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
        return r


resp = notas(4, 7, 5, sit=True)
print(resp)
