from bs4 import BeautifulSoup
from transformers import pipeline
import requests

BASE_URL = "https://coinmarketcap.com/currencies/"
summarizer = pipeline("summarization", model="t5-small")


def get_paragraphs(coin: str):
    r = requests.get(f"{BASE_URL}/{coin}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all(["h1", "p"])
    article = " ".join([result.text for result in results])
    for c in [".", "?", "!"]:
        article = article.replace(c, f"{c}<eos>")
    sentences = article.split('<eos>')
    max_chunk = 500
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(" ")) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(" "))
            else:
                current_chunk += 1
                chunks.append(sentence.split(" "))
        else:
            chunks.append(sentence.split(" "))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = " ".join(chunks[chunk_id])
    res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)
    summaries = [s["summary_text"] for s in res]
    return chunks, summaries
