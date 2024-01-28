import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pokedex import *

# Define la clase Pokedex que hereda de ttk.Frame
class Pokedex(ttk.Frame):
    # El método constructor de la clase
    def __init__(self, master, nombre_pokemon):
        # Llama al constructor de la clase padre
        super().__init__(master, width=800, height=600)
        # Obtiene la información del Pokémon y la almacena en la propiedad pokemon
        self.pokemon = self.obtener_pokemon(nombre_pokemon)

    # Método para obtener la información del Pokémon desde la API
    def obtener_pokemon(self, nombre):
        # Define la URL de la API
        url = f"http://pokeapi.co/api/v2/pokemon/{nombre}"
        # Realiza una petición GET a la API
        respuesta = requests.get(url)
        # Si la respuesta es exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Convierte la respuesta a JSON y la retorna
            pokemon = respuesta.json()
            return pokemon
        else:
            # Si la respuesta no es exitosa, imprime un mensaje de error y retorna None
            print(f"No se encontró el Pokémon: {nombre}")
            return None

# Si este archivo se está ejecutando como el principal
if __name__ == "__main__":
    # Crea una ventana con el tema "superhero"
    root = ttk.Window("Pokedex", themename="superhero")
    # Crea una instancia de Pokedex con "pikachu" como el nombre del Pokémon
    pokedex = Pokedex(root, "pikachu")

    # Crea una etiqueta con el nombre del Pokémon y la añade a la ventana
    pokelbl = ttk.Label(root, text="Name: " + str(pokedex.pokemon["name"]))
    pokelbl.pack()
    
    # Añade la instancia de Pokedex a la ventana y la expande para llenarla
    pokedex.pack(fill=BOTH, expand=YES)
    # Inicia el bucle principal de la ventana
    root.mainloop()