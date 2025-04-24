from data.parser import extract_clean_paragraphs
from data.scratch import get_band8_essay_links

essay_links = get_band8_essay_links()
for essay_link in essay_links:
    print(essay_link)
# content = extract_clean_paragraphs(url)