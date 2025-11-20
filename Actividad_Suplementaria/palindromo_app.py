class PalindromoApp:
    def __init__(self):
        pass  # No necesitamos guardar nada al inicio

    def es_palindromo(self, texto):
        # Convertimos a minúsculas
        t = texto.lower()
        # Nos quedamos solo con letras y números
        t = "".join(c for c in t if c.isalnum())
        # Comparamos con su reverso
        return t == t[::-1]

    def iniciar(self):
        print("👋 Bienvenido al comprobador de palíndromos")
        print("Escribe una palabra o frase para comprobar.")
        print('Escribe "salir" para terminar.\n')

        while True:
            texto = input("👉 Ingresa un texto: ")

            if texto.strip().lower() == "salir":
                print("👋 Adiós, gracias por usar el programa.")
                break

            if not texto.strip():
                print("⚠️ No escribiste nada. Intenta de nuevo.\n")
                continue

            if self.es_palindromo(texto):
                print(f'✅ "{texto}" ES un palíndromo.\n')
            else:
                print(f'❌ "{texto}" NO es un palíndromo.\n')


if __name__ == "__main__":
    app = PalindromoApp()
    app.iniciar()

