class Pokemon:

    def __init__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{}({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}!".format(self, pokemon))

class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print("{} Lançou um raio do trovão em: {}!".format(self, pokemon))

meu_pokemon = PokemonEletrico("Elétrico", "Pikachu")
amigo_pokemon = Pokemon("Fogo", "Charmander")

meu_pokemon.atacar(amigo_pokemon)
amigo_pokemon.atacar(meu_pokemon)
