import requests
from bs4 import BeautifulSoup


def get_band8_essay_links():
    base_url = "https://www.ielts-blog.com"
    list_url = base_url + "/ielts-writing-samples/ielts-essay-samples-of-band-8/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(list_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    strong_tags = soup.find_all('strong')

    for strong in strong_tags:
        a_tag = strong.find('a')
        if a_tag and "Sample essay" in a_tag.get_text():
            href = a_tag.get("href")
            if href and href.startswith("/"):
                href = base_url + href
            if href not in links:
                links.append(href)

    return links

if __name__ == "__main__":
    essay_links = get_band8_essay_links()
    print(f"Found {len(essay_links)} links.")
    for link in essay_links:
        print(link)
    print(essay_links)
