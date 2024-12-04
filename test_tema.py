import unittest
from tema.tema import Tema
from tema.tema_director import TemaDirector


class TestTema(unittest.TestCase):
    def test_sanitize_attribute(self):
        # Crear una instancia de la clase Tema
        tema = Tema(
            "¡Bienvenido al mundo del código! @#$",
            "Homero Simpson @#@",
            "Matt Groening* ",
        )

        # Verificar que la sanitización funciona correctamente
        self.assertEqual(tema.tema, "Bienvenido al mundo del codigo")
        self.assertEqual(tema.personaje, "Homero Simpson")
        self.assertEqual(tema.author, "Matt Groening")

    def test_empty_string(self):
        # Probar con cadenas vacías
        tema = Tema("", "", "")
        self.assertEqual(tema.tema, "")
        self.assertEqual(tema.personaje, "")
        self.assertEqual(tema.author, "")

    def test_special_characters(self):
        # Probar con caracteres especiales
        tema = Tema(
            "Texto con caracteres especiales áéíóú", "Personaje_@!#", "Autor#_123"
        )
        self.assertEqual(tema.tema, "Texto con caracteres especiales aeiou")
        self.assertEqual(tema.personaje, "Personaje_")
        self.assertEqual(tema.author, "Autor _123")

    def test_tema_con_personaje_sin_author(self):
        # Caso normal: tema con personaje pero sin autor
        tema = TemaDirector.build_tema_con_personaje_sin_author(
            "Tema Principal", "Homero Simpson"
        )
        self.assertEqual(tema.tema, "Tema Principal")
        self.assertEqual(tema.personaje, "Homero Simpson")
        self.assertIsNone(tema.author)  # No debería tener autor

    def test_tema_con_personaje_y_author(self):
        # Caso normal: tema con personaje y autor
        tema = TemaDirector.build_tema_con_personaje_y_author(
            "Tema Principal", "Homero Simpson", "Matt Groening"
        )
        self.assertEqual(tema.tema, "Tema Principal")
        self.assertEqual(tema.personaje, "Homero Simpson")
        self.assertEqual(tema.author, "Matt Groening")

    def test_tema_con_datos_vacios(self):
        # Caso borde: Tema con personaje pero sin nombre
        tema = TemaDirector.build_tema_con_personaje_sin_author("", "Homero Simpson")
        self.assertEqual(tema.tema, "")  # Tema vacío
        self.assertEqual(tema.personaje, "Homero Simpson")  # Personaje debería estar
        self.assertIsNone(tema.author)  # No debería tener autor

        # Caso borde: Tema sin personaje y sin autor
        tema = TemaDirector.build_tema_con_personaje_y_author("", "", "")
        self.assertEqual(tema.tema, "")  # Tema vacío
        self.assertEqual(tema.personaje, "")  # Personaje vacío
        self.assertEqual(tema.author, "")  # Autor vacío

    def test_tema_con_caracteres_especiales(self):
        # Caso borde: Tema con caracteres especiales
        tema = TemaDirector.build_tema_con_personaje_sin_author(
            "Tema @123", "Homero-Simpson!"
        )
        self.assertEqual(
            tema.tema, "Tema  123"
        )  # El nombre del tema debería estar sanitizado
        self.assertEqual(
            tema.personaje, "Homero-Simpson!"
        )  # El personaje también debería ser sanitizado
        self.assertIsNone(tema.author)


if __name__ == "__main__":
    unittest.main()
