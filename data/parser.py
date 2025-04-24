import requests
from bs4 import BeautifulSoup


def extract_clean_paragraphs(url):
    # Set headers to mimic a real browser request
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the <article> section that contains the essay content
    article = soup.find("article")
    if not article:
        return ""

    # Find all paragraph elements within the article
    paragraphs = article.find_all("p")
    collected = []
    strong_hit_count = 0  # Track how many <p> tags contain <strong>

    for p in paragraphs:
        if p.find("strong"):
            strong_hit_count += 1
            if strong_hit_count == 2:
                # Stop collecting if this is the second <p> containing <strong>
                break
            continue  # Skip the first <p> containing <strong> (usually the title)

        # Extract clean text from <p>, with internal tags joined by space
        text = p.get_text(separator=" ", strip=True)
        if text:
            collected.append(text)

    # Combine all collected paragraphs into one string separated by newlines
    return "\n".join(collected)


# Example usage
if __name__ == "__main__":
    url = "https://www.ielts-blog.com/ielts-writing-samples/ielts-essays-band-8/ielts-essay-topic-senior-managers-should-have-higher-salaries-than-other-employees-agree-disagree/"
    content = extract_clean_paragraphs(url)
    print(content)
