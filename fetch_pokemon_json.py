import requests


def fetch_pokemon_data(pokemon_name):

    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    else:
        print(f"Error: Could not get data for {pokemon_name}. {response.status_code}")
        return None
    
def calculate_average_weight(pokemon_list):
    total_weight = 0
    valid_pokemon_count = 0

    for name in pokemon_list:
        data = fetch_pokemon_data(name)
        if data:
            total_weight += data['weight']
            valid_pokemon_count += 1
    if valid_pokemon_count > 0:
        return total_weight/valid_pokemon_count
    else:
        print("No valid data to give average weight.")
        return None

def display_pokemon_details(pokemon_name):

    data = fetch_pokemon_data(pokemon_name)
    if data:
        print(f"Whos That Pokemon: {data['name'].capitalize()}")
        types = [t['type']['name']for t in data['types']]
        abilities = [a["ability"]['name'] for a in data['abilities']]
        weight = data['weight']

        print(f"Types: {','.join(types)}")
        print(f"Abilities: {','.join(abilities)}")
        print(f"Weight: {weight}")
    else:
        print(f"No data available for {pokemon_name}")





display_pokemon_details("pikachu")
display_pokemon_details("bulbasaur")
display_pokemon_details("charmander")

pokemon_list = ["pikachu", "bulbasaur", "charmander"]
average_weight = calculate_average_weight(pokemon_list)
if average_weight:
    print(f"\nThe Average Weight of {','.join(pokemon_list)} is {average_weight:.2f}.")