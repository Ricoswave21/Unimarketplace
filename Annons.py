class Advertisement:
    def __init__(self, content):
        self.content = content  # Attribut för texten i annonsen.

    # Metod för att validera att texten inte överskrider 150 tecken.
    def validate_character_count(self):
        if len(self.content) <= 150:
            return True
        else:
            return False

# Underklass för textannons, ärver från Advertisement.
class TextAdvertisement(Advertisement):
    def __init__(self, content):
        super().__init__(content)  # Anropa föräldersklassens __init__-metod.

# Underklass för bildannons, ärver från Advertisement.
class ImageAdvertisement(Advertisement):
    def __init__(self, content):
        super().__init__(content)  # Anropa föräldersklassens __init__-metod.

# Klassen för att hantera skapandet av olika typer av annonser.
class AdvertisementManager:
    # Metod för att skapa textannons.
    def create_text_advertisement(self, text):
        if len(text) <= 150:  # Kontrollera att texten inte överskrider max tecken.
            return TextAdvertisement(text)  # Skapa en ny textannons.
        else:
            print("Text is too long. Maximum character count is 150.")
            return None

    # Metod för att skapa bildannons. Implementering saknas här.
    def create_image_advertisement(self, image):
        # Implementera skapandet av bildannons här.
        return ImageAdvertisement(image)  # Tillfälligt returnera en nytt ImageAdvertisement-objekt.

# Exempelanvändning av AdvertisementManager för att skapa annonser.
advertisement_manager = AdvertisementManager()

# Skapa en textannons och kontrollera om den skapades framgångsrikt.
text_advertisement = advertisement_manager.create_text_advertisement("This is a text advertisement.")
if text_advertisement:
    print("Text advertisement created successfully.")
else:
    print("Failed to create text advertisement.")

# Skapa en bildannons och kontrollera om den skapades framgångsrikt.
image_advertisement = advertisement_manager.create_image_advertisement("path/to/image.jpg")
if image_advertisement:
    print("Image advertisement created successfully.")
else:
    print("Failed to create image advertisement.")
