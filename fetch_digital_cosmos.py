import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed To Fetch Data!")
        return
    
    planets = response.json()['bodies']
    planet_data = []
   
    for planet in planets:
        if planet.get('isPlanet'):
            name = planet.get("englishName", 'Unknown')
            
            mass = planet.get('mass', {}).get('massValue', 0)
            orbit_period = planet.get('sideralOrbit', "N/A")
            planet_data.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planet_data


def find_heaviest_planet(planets):
    if not planets:
        print("No planet data available")
        return None
    heaviest = max(planets, key=lambda p: p['mass'])
    print(f"\nThe heaviest planet is {heaviest['name']} with the mass of {heaviest['mass']}.")
    return heaviest



planet_list = fetch_planet_data()

if planet_list:
    find_heaviest_planet(planet_list)
