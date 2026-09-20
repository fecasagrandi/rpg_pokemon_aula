class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return "{} ({})".format(self.especie, self.tipo)

    def atacar(self, pokemon):
        print("{} atacou o {}".format(self.especie, pokemon.especie))

    def defender(self, pokemon):
        print("{} defendeu o `{}".format(pokemon.especie, pokemon.tipo))

meu_pokemon = Pokemon("Fogo", "Charmander")
pokemon_amigo = Pokemon("Elétrico", "Pikachu")

meu_pokemon.defender(pokemon_amigo)

