from bs4 import BeautifulSoup
import requests
import csv

#будет парсер разных плагинов из вордпресса

class MyParser:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def write_csv(self, data):
        with open(self.path, 'a', encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\r')
            writer.writerow([
                data["name"],
                data["url"]
            ])

    def get_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        plugins = soup.find_all("li", class_="wp-block-post")

        for plugin in plugins:
            try:
                name = plugin.find("h3", class_="entry-title").text

                url = plugin.find("h3", class_="entry-title").find("a")["href"]

                data = {"name": name, "url": url}

                self.write_csv(data)

            except AttributeError:
                pass

    def run(self):
        for i in range(1, 6):
            url = f"https://wordpress.org/plugins/browse/popular/page/{i}/"
            self.get_data(self.get_html(url))

def main():
    pars = MyParser(
        "https://wordpress.org/plugins/browse/popular/",
        "plugins.csv"
    )

    pars.run()

if __name__ == "__main__":
    main()