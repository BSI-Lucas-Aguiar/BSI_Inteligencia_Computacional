import scrapy

class netshoes(scrapy.Spider):
    name = 'Netshoes Bot Bicicletas'
    start_urls = ['https://www.netshoes.com.br']
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

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



