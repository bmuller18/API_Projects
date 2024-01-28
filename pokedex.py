import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pokedex import *

#Obtiene informacion del pokemon desde la api
class Pokedex(ttk.Frame):
    def __init__(self, master, nombre_pokemon):
        super().__init__(master, width=800, height=600)
        self.pokemon = self.obtener_pokemon(nombre_pokemon)

    def obtener_pokemon(self, nombre):
        url = f"http://pokeapi.co/api/v2/pokemon/{nombre}"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            pokemon = respuesta.json()
            return pokemon
        else:
            print(f"No se encontró el Pokémon: {nombre}")
            return None


if __name__ == "__main__":
    root = ttk.Window("Pokedex", themename="superhero")
    pokedex = Pokedex(root, "pikachu")

    pokelbl = ttk.Label(root, text="Name: " + str(pokedex.pokemon["name"]))
    pokelbl.pack()
    
    pokedex.pack(fill=BOTH, expand=YES)
    root.mainloop()
