class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return "{} ({})".format(self.especie, self.tipo)

meu_pokemon = Pokemon("Fogo", "Charmander")
pokemon_amigo = Pokemon("Elétrico", "Pikachu")
pokemon_gelo = Pokemon("Terra", "Groudon")

print(meu_pokemon)
print(pokemon_amigo)
print(pokemon_gelo)
