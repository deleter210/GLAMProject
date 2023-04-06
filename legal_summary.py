import requests
from bs4 import BeautifulSoup


def get_legal_summary(law_id):
    """Get summary of a specific Greek law based on its ID."""
    url = f"https://www.e-nomothesia.gr/nea-nomothesia/{law_id}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    summary = soup.find("p", class_="summary-text")
    if summary is None:
        return None
    return summary.get_text().strip()
