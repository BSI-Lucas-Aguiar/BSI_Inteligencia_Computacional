import scrapy


class PapelSpider(scrapy.Spider):
    name = 'papel'
    start_url = 'https://www.alura.com.br/'
    start_urls = [start_url+'cursos-online-programacao/']
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response): 
        SELECTOR = ".subcategoria_item"
        #cursos = []
        for categoria in response.css(SELECTOR):
            curso = {}

            NOME_SELECTOR = ".card-curso__nome"

            curso["Nome"] = categoria.css(NOME_SELECTOR).extract_first()
            print(curso)
            #cursos.append(curso)

