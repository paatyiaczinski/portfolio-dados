class BaseScraper:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        raise NotImplementedError("Subclasses must implement the fetch method.")

    def parse(self, raw_html):
        raise NotImplementedError("Subclasses must implement the parse method.")

    def run(self):
        raw_html = self.fetch()
        return self.parse(raw_html)