from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def w_csv(data):
    with open("lenta_news.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow([
            data["title"],
            data["url"]
        ])

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    news = soup.find_all("a")

    for item in news:
        try:
            title = item.text.strip()
            url = item.get("href")

            if title and url:
                data = {"title": title, "url": url}

                w_csv(data)

        except AttributeError:
            pass

def main():
    url = "https://www.lenta.ru/"
    get_data(get_html(url))

if __name__ == "__main__":
    main()