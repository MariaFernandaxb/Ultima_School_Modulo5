from requests_html import HTMLSession

sessao = HTMLSession()
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'
resposta1 = sessao.get(url)

anuncios = []
if(resposta1.status_code !=200):
    print('Falha ao conectar')

else:
    valores = resposta1.html.find('.olx-ad-card__link-wrapper')

    for v in valores:
        resposta2 = sessao.get(v.attrs['href'])
        valores2 = resposta2.html.find("h1", first =True)
        titulo = valores2.text
        valores2 = resposta2.html.find('span[class="ad__sc-1wimjbb-1 hoHpcC sc-jTzLTM kNahTW"]', first=True)       
        preco = valores2.text

        anuncios.append({
            'url': v.attrs['href'],
            'titulo': titulo,
            'preco': preco
        })

       
for a in anuncios:
    print(f"titulo: {a['titulo']} \n preco: {a['preco']}\n url: {a['url']}\n")