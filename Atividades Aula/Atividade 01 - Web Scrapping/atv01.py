import scrapy

#Busca por bicicletas aro 29
'''
class netshoes(scrapy.Spider):
    name = 'Netshoes Bot Bicicletas'
    start_urls = ['https://www.netshoes.com.br/busca?nsCat=Natural&q=bicicleta+aro+29']

    def parse(self, response):
        self.log('Visitei o site: %s' % response.url)
        SELECTOR = ".search-list search-list--3"
        bicicletas = []
        for lista in response.css(SELECTOR):
            bikes = {}
            NOME_SELECTOR = ".item-card__description__product-name ::text"
            VALOR_SELECTOR = ".full-mounted-price :: text"

            bikes['Nome'] = lista.css(NOME_SELECTOR).extract_first()
            bikes['Valor'] = lista.css(VALOR_SELECTOR).extract_first()
            print(bikes)

            bicicletas.append(bikes)

        print("Total de buscas realizadas:" + len(bicicletas))
'''

class netshoes(scrapy.Spider):
    name = 'Netshoes Bot Bicicletas'
    start_urls = ['https://www.netshoes.com.br']

    def parse(self, response):
        self.log('Visitei o site: %s' % response.url)
        SELECTOR = ".horizontal netshoes-br pt-br mostpopular no-touch page-home desktop"
        bicicletas = []
        for lista in response.css(SELECTOR):
            bikes = {}
            NOME_SELECTOR = ".details product-name ::text"
            VALOR_SELECTOR = ".full-mounted-price :: text"

            bikes['Nome'] = lista.css(NOME_SELECTOR).extract_first()
            bikes['Valor'] = lista.css(VALOR_SELECTOR).extract_first()
            print(bikes)

            bicicletas.append(bikes)

        print("Total de buscas realizadas:" + len(bicicletas))




