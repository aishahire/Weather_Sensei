# 🌡️ Weather Sensei – Smart Temperature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def give_advice(temp_c):
    """Takes Celsius value and gives weather advice with emojis"""
    if temp_c < 0:
        return "❄️ It's freezing cold! Wear thermal clothes. 🧥"
    elif 0 <= temp_c < 15:
        return "🧊 Chilly weather! Don’t forget a jacket. 🧣"
    elif 15 <= temp_c < 25:
        return "🌤️ Pleasant weather. Enjoy your day! 😊"
    elif 25 <= temp_c < 35:
        return "☀️ It's warm out there! Stay hydrated. 💧"
    else:
        return "🔥 It's hot! Avoid the sun and drink water. 🥵"

def main():
    print("\n===== 🌡️ WEATHER SENSEI =====")
    
    try:
        temp_input = float(input("Enter temperature value: "))
    except ValueError:
        print("❌ Invalid number. Please enter a valid temperature.")
        return

    print("\nConvert from:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        result = celsius_to_fahrenheit(temp_input)
        print(f"\n🌡️ {temp_input}°C = {result:.2f}°F")
        print(give_advice(temp_input))

    elif choice == "2":
        result = fahrenheit_to_celsius(temp_input)
        print(f"\n🌡️ {temp_input}°F = {result:.2f}°C")
        print(give_advice(result))  # Advice based on converted Celsius

    elif choice == "3":
        result = celsius_to_kelvin(temp_input)
        print(f"\n🌡️ {temp_input}°C = {result:.2f}K")
        print(give_advice(temp_input))

    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")

    print("\nThank you for using Weather Sensei! ☁️\n")

if __name__ == "__main__":
    main()
