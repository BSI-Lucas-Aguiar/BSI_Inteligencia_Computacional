import scrapy


class AluraSpiderSpider(scrapy.Spider):
    name = 'alura_spider'
    allowed_domains = ['www.alura.com.br']
    start_urls = ['https://www.alura.com.br/cursos-online-programacao']

    def parse(self, response):
        SELECTOR = ".subcategoria_item"
        cursos = []
        for categoria in response.css(SELECTOR):
            curso = {}

            NOME_SELECTOR = ".card-curso__nome"

            curso["Nome"] = categoria.css(NOME_SELECTOR).extract_first()
            print(curso)
            cursos.append(curso)

    
