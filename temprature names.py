def get_temperature_category(temp_celsius):
    if temp_celsius < -40:
        return "Absolute Zero (Theoretical)"
    elif temp_celsius < -30:
        return "Deep Freeze (Pluto's Surface)"
    elif temp_celsius < -15:
        return "Bone-Chilling Cold (Antarctica)"
    elif temp_celsius < -5:
        return "Penguin Weather (South Pole)"
    elif temp_celsius < 0:
        return "Chilly (Fridge Temperature)"
    elif temp_celsius < 5:
        return "Cold (Icy)"
    elif temp_celsius < 10:
        return "Cold (Frosty)"
    elif temp_celsius < 15:
        return "Cold (Brisk)"
    elif temp_celsius < 20:
        return "Cold (Cool)"
    elif temp_celsius < 26:
        return "Hot (Melted)"
    elif temp_celsius < 31:
        return "Hot (Steamy)"
    elif temp_celsius < 36:
        return "Hot (Sizzling)"
    elif temp_celsius < 40:
        return "Hot (Scorching)"
    elif temp_celsius < 50:
        return "Hot (Volcanic)"
    elif temp_celsius < 60:
        return "Hot (Saharan)"
    elif temp_celsius < 75:
        return "Hot (Solar Flare)"
    elif temp_celsius < 100:
        return "Inferno Hot (Saturn's Surface)"
    else:
        return "Nuclear Hot (Center of the Sun)"

def main():
    print("Temperature Description Program")
    while True:
        try:
            temp_celsius = float(input("Enter the temperature in Celsius (or type 'exit' to quit): "))
            if temp_celsius == "exit":
                break

            category = get_temperature_category(temp_celsius)
            if -10 <= temp_celsius <= 30:
                print(f"The temperature {temp_celsius:.1f}°C is considered '{category}'. Well done!")
            else:
                print(f"The temperature {temp_celsius:.1f}°C is considered '{category}'.")

            # Humorous scenarios
            if temp_celsius >= 35:
                print("Popsicle-inator: It's so hot that everything is turning into popsicles, even boiling water!")
            elif temp_celsius <= -20:
                print("Frozen Brain: It's freezing outside! I feel like my brain has turned into a frozen ice cube.")
            elif temp_celsius >= 25:
                print("Toaster Tantrum: The toaster is on strike, and I'm playing a mini game of 'catch the toast'!")
            elif temp_celsius >= 15:
                print("Microwave Marathon: Waiting for my food, and it feels like the time goes slower than ever!")
            elif -5 <= temp_celsius <= 10:
                print("Thermostat Wars: The battle over the perfect temperature setting continues!")
            elif temp_celsius <= -10:
                print("Snow-Induced Memory Loss: I forgot where I parked my car in the sea of white cars!")
            elif -5 <= temp_celsius <= 5:
                print("Frosty's Mischief: Frosty the Snowman is playing pranks on the neighbors overnight!")
            elif temp_celsius <= 25:
                print("Sun's Hide-and-Seek: The weather is unpredictable, and the sun plays hide-and-seek!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
