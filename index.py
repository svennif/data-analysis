from bs4 import BeautifulSoup

# Load and parse the HTML file
html_file = './BPD.html'

print(test)

with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract the table
table = soup.find('table')

# Extract rows
rows = table.find_all('tr')[1:]  # Skip header row

# Player stats
players = []

for row in rows:
    cells = row.find_all('td')
    player_data = {
        "Name": cells[3].text.strip(),
        "Tackles/90": float(cells[15].text.strip()),
        "Clearances/90": float(cells[16].text.strip()),
        "Interceptions/90": float(cells[17].text.strip()),
        "Shots Blocked/90": float(cells[18].text.strip()),
        "Progressive Passes/90": float(cells[19].text.strip()),
    }
    # Calculate total score
    player_data["Total Score"] = (
        player_data["Tackles/90"]
        + player_data["Clearances/90"]
        + player_data["Interceptions/90"]
        + player_data["Shots Blocked/90"]
        + player_data["Progressive Passes/90"]
    )
    players.append(player_data)

# Find the best player
best_player = max(players, key=lambda x: x["Total Score"])

# Print the results
print(f"The best player overall is {best_player['Name']} with a total score of {best_player['Total Score']:.2f}.")
