from tema.tema_builder import TemaBuilder


class TemaDirector:
    @staticmethod
    def build_tema_con_personaje_sin_author(tema: str, personaje: str):
        tema_builder = TemaBuilder(tema)
        tema_builder.add_personaje(personaje)
        return tema_builder.build()

    @staticmethod
    def build_tema_con_personaje_y_author(tema: str, personaje: str, author: str):
        tema_builder = TemaBuilder(tema)
        tema_builder.add_personaje(personaje)
        tema_builder.add_author(author)
        return tema_builder.build()
