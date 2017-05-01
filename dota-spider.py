import scrapy


def lst_url(url):
    name = url[0].rsplit('/')
    return ' '.join(name[4].rsplit('_'))


def get_name(node):
    return lst_url(node.xpath('@href').extract())


class DotaSpider(scrapy.Spider):
    name = 'dotaspider'
    start_urls = ['http://www.dota2.com/heroes/']

    def parse(self, response):
        heroes = []
        for strenght_heroes in response.css('.heroColLeft'):
            for hero in strenght_heroes.css('.heroIcons a'):
              heroes.append({ 'icon': hero.xpath('img/@src').extract()[0], 'main_attribute': 'strenght', 'name': get_name(hero) })

        for agility_heroes in response.css('.heroColMiddle'):
            for hero in agility_heroes.css('.heroIcons a'):
              heroes.append({ 'icon': hero.xpath('img/@src').extract()[0], 'main_attribute': 'agility', 'name': get_name(hero) })

        for intl_heroes in response.css('.heroColRight'):
            for hero in intl_heroes.css('.heroIcons a'):
              heroes.append({ 'icon': hero.xpath('img/@src').extract()[0], 'main_attribute': 'intelligence', 'name': get_name(hero) })

        yield {'heroes': heroes }
