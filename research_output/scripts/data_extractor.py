import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def extract_table_from_url(url):
    """Extracts tables from webpages and returns a list of DataFrames."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        dfs = []
        for table in tables:
            df = pd.read_html(str(table))[0]
            dfs.append(df)
        return dfs
    except Exception as e:
        print(f"Error extracting table from {url}: {e}")
        return []

def save_to_csv(data, filename, headers):
    """Appends data to CSV. data should be a list of values matching headers."""
    file_path = os.path.join('/home/ubuntu/streaming-ott/research_output', filename)
    df = pd.DataFrame([data], columns=headers)
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

def score_source_credibility(url, content):
    """Returns Tier 1-4 based on URL and content analysis."""
    if any(domain in url for domain in ['sec.gov', 'ir.netflix.net', 'thewaltdisneycompany.com']):
        return "Tier 1"
    elif any(domain in url for domain in ['statista.com', 'cnbc.com', 'variety.com', 'bloomberg.com']):
        return "Tier 2"
    elif any(domain in url for domain in ['blog.', 'medium.com']):
        return "Tier 3"
    else:
        return "Tier 4"

def calculate_confidence(sources_list):
    """Returns HIGH/MEDIUM/LOW based on source tiers."""
    tiers = [score_source_credibility(s, "") for s in sources_list]
    if "Tier 1" in tiers:
        return "HIGH"
    if tiers.count("Tier 2") >= 2:
        return "HIGH"
    if "Tier 2" in tiers:
        return "MEDIUM"
    return "LOW"

if __name__ == "__main__":
    # Simple test
    print("Data Extractor Script Initialized")
