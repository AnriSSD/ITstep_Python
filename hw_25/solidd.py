# Single Responsibility Principle
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_discount_price(self, discount):
        # Calculate and return the discounted price
        return self.price * (1 - discount)


# Open/Closed Principle
class PayPalPayment:
    def process_payment(self, amount):
        # Process payment using PayPal
        print(f"Processing PayPal payment for ${amount}")


class Payment:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def process_payment(self, amount):
        self.payment_processor.process_payment(amount)


# Liskov Substitution Principle
class Vehicle:
    def fuel_capacity(self):
        return "100 liters"


class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"


# Interface Segregation Principle
class AudioPlayer:
    def play_audio(self):
        print("Playing audio...")


class VideoPlayer:
    def play_video(self):
        print("Playing video...")


# Dependency Inversion Principle (DIP)
class ConsoleDisplay:
    def show(self, data):
        print(f"Displaying data: {data}")


class WeatherStation:
    def report(self, display):
        display.show("Weather Data")


# gamoyenebis magaliti
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(f"Discounted price: {book.get_discount_price(0.1)}")

paypal_payment = PayPalPayment()
payment = Payment(paypal_payment)
payment.process_payment(100)

electric_car = ElectricCar()
print(f"Fuel capacity: {electric_car.fuel_capacity()}")

audio_player = AudioPlayer()
audio_player.play_audio()

video_player = VideoPlayer()
video_player.play_video()

console_display = ConsoleDisplay()
weather_station = WeatherStation()
weather_station.report(console_display)
