import urllib.request

def getDolar():
#     # content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
#     content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").read()
    content = urllib.request.urlopen("https://www.ig.com.br/#home").read()
    content = str(content)
#     print(content)
    find = '<span class="wd_p2048">' #'<a title="Ju'
#     # find = '<input id="q" aria-hidden="'
    posicao = int(content.index(find) + len(find))
#     # posicao = content.index(find) + len(find)
    dolar = content[ posicao : posicao  + 4]
    return dolar

# def getEuro():
#     content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
#     content = str(content)
#     find = '<input type="hidden" value="'
#     posicao = int(content.index(find) + len(find))
#     euro = content[ posicao : posicao  + 4]
#     return euro

# def getTemperatura():
#     content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").read()
#     content = str(content)
#     find = 'tempMax0">'
#     posicao = int(content.index(find) + len(find))
#     maxima = content[ posicao : posicao  + 2]

    # find = 'Min0">'
    # posicao = int(content.index(find) + len(find))
    # minima = content[ posicao : posicao  + 2]
    # return [minima, maxima]

print(getDolar())


