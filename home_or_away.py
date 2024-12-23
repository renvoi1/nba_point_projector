import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Function to get the next game's location for a team
def get_loc(team_abbreviation):
    def get_next_game_location(team_abbreviation):
        url = f'https://www.basketball-reference.com/teams/{team_abbreviation}/2025_games.html'
        
        
        # Request the page content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table with the game schedule
        schedule_table = soup.find('table', {'id': 'games'})
        
        # Loop through the rows of the table to find the next game
        for row in schedule_table.find_all('tr')[1:]:  # Skip the header row
            # Extract the date, opponent, and game location
            columns = row.find_all('td')
            
            if len(columns) > 1:
                # Get the date and the opponent
                game_date = columns[0].get_text()
                opponent = columns[5].get_text()
                
                # Check for '@' in the opponent (indicating an away game)
                game_location = columns[4].get_text().strip()
                
                # Debugging: Print the exact content of game_location to check for issues

                if '@' in game_location:  # Away game: opponent's location
                    global is_game_away
                    is_game_away = True
                    game_location = 'AWAY GAME'
                elif game_location == "":  # Empty field: Home game
                    is_game_away = False
                    game_location = "HOME GAME"
                
                # Convert the date to a datetime object and check if it's in the future
                game_date = datetime.strptime(game_date, '%a, %b %d, %Y')
                
                # Only return the next game that is in the future
                if game_date > datetime.now():
                    return game_date, opponent, game_location

    # Example: Get the next game for specified team
    team_abbreviation = f'{team_abbreviation}'
    next_game_info = get_next_game_location(team_abbreviation)

    if next_game_info != "No upcoming games found":
        global location
        game_date, opponent, location = next_game_info
        print(f"{location}")
    else:
        print(next_game_info)
