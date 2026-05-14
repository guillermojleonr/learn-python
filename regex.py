"""
Regular Expressions (Regex) Learning Module
============================================

A Regex is a character sequence representing a search pattern.
Generally used in text processing.

This module covers:
1. Basic methods (search, findall, match)
2. Match object properties
3. Metacharacters (^, $, ., [], etc.)
4. Flags and special sequences
"""


import re


class RegexLearning:
    """A class to learn and practice regular expressions in Python."""

    @staticmethod
    def basic_search():
        """Demonstrates re.search() - finds a string from anywhere in the text."""
        print("=== re.search() Basic Usage ===")

        cadena = "Vamos a aprender expresiones regulares"
        texto_buscar = "aprender"

        # search receives two strings, returns a match object
        resultado = re.search(texto_buscar, cadena)
        print(f"Search result: {resultado}")

        # Check if found
        if resultado is not None:
            print("Texto encontrado")
        else:
            print("Texto no encontrado")

        # Match object methods
        print(f"Start position: {resultado.start()}")  # Starting character position
        print(f"End position: {resultado.end()}")      # Ending character position
        print(f"Span (start, end): {resultado.span()}")  # Both together

    @staticmethod
    def findall_usage():
        """Demonstrates re.findall() - returns all occurrences as a list."""
        print("\n=== re.findall() Usage ===")

        cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje"
        texto_buscar = "Python"

        # findall returns a list with each occurrence of the searched string
        coincidencias = re.findall(texto_buscar, cadena)
        print(f"Found: {coincidencias}")

        # The length shows how many occurrences
        print(f"Number of occurrences: {len(coincidencias)}")

    @staticmethod
    def metachar_anchors():
        """Demonstrates anchors: ^ (starts with) and $ (ends with)."""
        print("\n=== Metacharacters: ^ and $ ===")

        lista_nombres = [
            'Ana Gomez',
            'María Martín',
            'Sandra López',
            'Santiago Martín',
            'Sandra Fernandez'
        ]

        print("Names starting with 'Sandra':")
        for elemento in lista_nombres:
            if re.findall('^Sandra', elemento):
                print(f"  - {elemento}")

        print("Names containing 'Martín':")
        for elemento in lista_nombres:
            if re.findall('Martín', elemento):
                print(f"  - {elemento}")

        # Useful for URLs and domains
        lista_urls = [
            'http://pildorasinformaticas.es',
            'ftp://pildorasinformaticas.es',
            'http://pildorasinformaticas.com',
            'ftp://pildorasinformaticas.com'
        ]

        print("\nURLs starting with 'ftp':")
        for elemento in lista_urls:
            if re.findall('^ftp', elemento):
                print(f"  - {elemento}")

        print("URLs ending with '.com':")
        for elemento in lista_urls:
            if re.findall('.com$', elemento):
                print(f"  - {elemento}")

    @staticmethod
    def metachar_character_classes():
        """Demonstrates character classes [...] to match specific characters."""
        print("\n=== Character Classes [...] ===")

        # Finding specific characters (like ñ)
        lista_con_español = [
            'http://informaticaenespaña.es',
            'ftp://pildorasinformaticas.es',
            'http://pildorasinformaticas.com',
            'ftp://pildorasinformaticas.com'
        ]

        print("URLs containing 'ñ':")
        for elemento in lista_con_español:
            if re.findall('[ñ]', elemento):
                print(f"  - {elemento}")

        # Character sets with alternation [oa]
        lista_nombres = ['hombres', 'mujeres', 'niños', 'niñas']
        print("\nWords matching 'niñ[oa]s' (niños or niñas):")
        for elemento in lista_nombres:
            if re.findall('niñ[oa]s', elemento):
                print(f"  - {elemento}")

    @staticmethod
    def metachar_ranges():
        """Demonstrates character ranges [a-z], [0-9], and negated ranges [^...].
        
        Note: Character ranges are case-sensitive by default.
        """
        print("\n=== Character Ranges ===")

        lista_nombres = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']

        print("Names containing letters from 'o' to 't':")
        for elemento in lista_nombres:
            if re.findall('[o-t]', elemento):
                print(f"  - {elemento}")

        print("\nNames starting with letters from 'O' to 'T' (case sensitive):")
        for elemento in lista_nombres:
            if re.findall('^[O-T]', elemento):
                print(f"  - {elemento}")

        # Combining numbers and letters
        lista_codigos = ['Ma1', 'Se1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'MaA', 'MaB', 'MaC']

        print("\nCodes matching 'Ma[0-3]' (Ma0 to Ma3):")
        for elemento in lista_codigos:
            if re.findall('Ma[0-3]', elemento):
                print(f"  - {elemento}")

        print("\nCodes matching 'Ma[^0-3]' (NOT Ma0 to Ma3):")
        for elemento in lista_codigos:
            if re.findall('Ma[^0-3]', elemento):
                print(f"  - {elemento}")

        print("\nCodes matching 'Ma[0-3A-B]' (Ma0-Ma3, MaA, MaB):")
        for elemento in lista_codigos:
            if re.findall('Ma[0-3A-B]', elemento):
                print(f"  - {elemento}")

    @staticmethod
    def match_vs_search():
        """Demonstrates the difference between re.match() and re.search().
        
        - re.match() looks at the BEGINNING of the string only
        - re.search() looks ANYWHERE in the string
        """
        print("\n=== re.match() vs re.search() ===")

        nombre1 = "Sandra López"
        nombre2 = "Antonio Gómez"
        nombre3 = "María Lopez"

        # match() finds only at the beginning
        if re.match("Sandra", nombre1):
            print("match: nombre encontrado (starts with 'Sandra')")
        else:
            print("match: nombre no encontrado")

        # With IGNORECASE flag
        if re.match("sandra", nombre1, re.IGNORECASE):
            print("match with IGNORECASE: nombre encontrado")
        else:
            print("match with IGNORECASE: nombre no encontrado")

    @staticmethod
    def special_sequences():
        """Demonstrates special sequences like \\d, and the escape character.
        
        Common special sequences:
        - \\d  - Any digit [0-9]
        - \\D  - Any non-digit
        - \\w  - Any alphanumeric character [a-zA-Z0-9_]
        - \\W  - Any non-alphanumeric
        - \\s  - Any whitespace
        - \\S  - Any non-whitespace
        - .   - Any character except newline
        """
        print("\n=== Special Sequences ===")

        cadena1 = "Sandra López"
        cadena2 = "555447855"
        cadena3 = "a55877455"

        # \d matches if string starts with a digit
        if re.match(r"\d", cadena2):
            print(f"'{cadena2}' starts with a digit")
        else:
            print(f"'{cadena2}' does not start with a digit")

        if re.match(r"\d", cadena3):
            print(f"'{cadena3}' starts with a digit")
        else:
            print(f"'{cadena3}' does not start with a digit")

        # Escape character example with .
        print("\nUsing dot (.) as metacharacter - matches ANY character:")
        if re.match(".Ara", nombre1, re.IGNORECASE):
            print("Found pattern '.Ara' (any char + 'ara')")

    @staticmethod
    def run_all_examples():
        """Run all regex learning examples."""
        print("=" * 50)
        print("REGULAR EXPRESSIONS LEARNING MODULE")
        print("=" * 50)

        RegexLearning.basic_search()
        RegexLearning.findall_usage()
        RegexLearning.metachar_anchors()
        RegexLearning.metachar_character_classes()
        RegexLearning.metachar_ranges()
        RegexLearning.match_vs_search()
        RegexLearning.special_sequences()

        print("\n" + "=" * 50)
        print("EXAMPLES COMPLETED")
        print("=" * 50)


# Run examples when script is executed directly
if __name__ == "__main__":
    RegexLearning.run_all_examples()