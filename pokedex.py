import requests

def obtener_pokemon(nombre):
    url = f"http://pokeapi.co/api/v2/pokemon/{nombre}"
    respuesta = requests.get(url)
    pokemon = respuesta.json()
    return pokemon


pokemon = obtener_pokemon("pikachu")

print(pokemon.get('abilities'))