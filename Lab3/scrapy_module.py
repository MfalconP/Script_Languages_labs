import scrapy


# scrapy runspider scrapy_module.py


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('span small::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }
            with open('quotes.txt', 'a') as f:
                f.write(f'Text: {text}\nAuthor: {author}\nTags: {", ".join(tags)}\n\n')

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)