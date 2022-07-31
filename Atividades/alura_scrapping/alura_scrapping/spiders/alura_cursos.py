import scrapy
from ..items import AluraScrappingItem

#Retorna a lista de cursos e duração dos mesmos na Alura
class AluraCursosSpider(scrapy.Spider):
    name = 'alura_cursos'
    start_urls = ['https://www.alura.com.br/cursos-online-programacao']

    def parse(self, response):
        items = AluraScrappingItem()

        nome_curso = response.css('.card-curso__nome::text').extract()
        duracao_curso = response.css('.card-curso__carga::text').extract()

        items['nome'] = nome_curso
        items['duracao'] = duracao_curso

        yield items
