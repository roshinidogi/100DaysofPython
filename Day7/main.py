import requests
from bs4 import BeautifulSoup

def fetch_secret_message(url: str):
    """
    Fetches the Unicode grid from a Google Doc and prints only uppercase letters as the secret message.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data.txt from the URL. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    lines = [line.get_text().strip() for line in soup.find_all('p') if line.get_text().strip()]

    # Skip header labels
    headers = {'x-coordinate', 'character', 'y-coordinate'}
    lines = [line for line in lines if line.lower() not in headers]

    positions = []
    i = 0
    while i + 2 < len(lines):
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])
            positions.append((char, x, y))
            i += 3
        except ValueError:
            i += 1

    if not positions:
        print("No valid grid data.txt found.")
        return

    max_x = max(p[1] for p in positions)
    max_y = max(p[2] for p in positions)

    # Create grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for char, x, y in positions:
        grid[y][x] = char

    # Extract and print uppercase letters row by row
    secret_message = ''.join(
        char for row in grid for char in row if char.isupper()
    )
    print(secret_message)


# Example usage
fetch_secret_message("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")
