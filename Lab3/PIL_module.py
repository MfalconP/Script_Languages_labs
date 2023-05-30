from PIL import Image

# Otwórz plik obrazu
image = Image.open("mem.png")

# Wyświetl informacje o pliku
print(f"Format: {image.format}")
print(f"Rozmiar: {image.size}")
print(f"Tryb: {image.mode}")

# Wyświetl obraz
image.show()

# Zmień rozmiar obrazu
resized_image = image.resize((900, 400))

# Zapisz zmieniony obraz
resized_image.save("resized_mem.png")
