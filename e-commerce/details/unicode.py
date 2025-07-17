import requests
from bs4 import BeautifulSoup

def fetch_and_print_grid(doc_url):
    # Fetch the published HTML
    response = requests.get(doc_url)
    if response.status_code != 200:
        print("Failed to fetch the document.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    points = []

    for row in rows[1:]:  # skip header row
        cols = row.find_all(['td', 'th'])
        if len(cols) < 3:
            continue
        try:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            points.append((x, y, char))
        except ValueError:
            continue

    if not points:
        print("No valid data found.")
        return

    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))

doc_url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub" 
fetch_and_print_grid(doc_url)