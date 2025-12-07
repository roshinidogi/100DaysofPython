import requests
from bs4 import BeautifulSoup

def fetch_unicode_grid(url: str):
    """
    Fetches a grid of Unicode characters from a Google Doc and prints the grid.
    """

    # Send a GET request
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from the URL: {url}. Status code: {response.status_code}")

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all visible text lines
    lines = [line.strip() for line in soup.get_text().splitlines() if line.strip()]

    # Initialize dictionary for the grid
    grid = {}

    # Try to parse lines: some lines may not be valid, so skip them
    for line in lines:
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != 3:
            continue  # skip invalid lines
        try:
            char = parts[0]
            x = int(parts[1])
            y = int(parts[2])
            grid[(x, y)] = char
        except ValueError:
            continue

    if not grid:
        print("No valid grid data found.")
        return

    # Determine grid size
    max_x = max(key[0] for key in grid.keys())
    max_y = max(key[1] for key in grid.keys())

    # Create grid
    output_grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (x, y), char in grid.items():
        output_grid[y][x] = char

    # Print grid
    for row in output_grid:
        print(''.join(row))


# Example usage
fetch_unicode_grid("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")
