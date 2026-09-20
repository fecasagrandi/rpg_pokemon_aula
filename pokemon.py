class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return "{} ({})".format(self.especie, self.tipo)

    def atacar(self, pokemon):
        print("{} atacou o {}".format(self.especie, pokemon.especie))

meu_pokemon = Pokemon("Fogo", "Charmander")
pokemon_amigo = Pokemon("Elétrico", "Pikachu")

meu_pokemon.atacar(pokemon_amigo)
pokemon_amigo.atacar(meu_pokemon)
