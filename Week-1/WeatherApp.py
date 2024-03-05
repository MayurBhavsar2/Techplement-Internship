import requests
import json
import time

API_KEY = "ab2dd9c5fffc42f49d965518242802"
BASE_URL = "https://api.weatherapi.com/v1/"

def get_weather_by_city(city):
    """
    Fetches weather data for a given city.
    
    Args:
    - city: Name of the city
    
    Returns:
    - Weather data (JSON) if successful, None otherwise
    """
    try:
        url = f"{BASE_URL}current.json?key={API_KEY}&q={city}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any error status
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def add_favorite(favorite_cities):
    """
    Adds a city to the favorite list.
    
    Args:
    - favorite_cities: List of favorite cities
    
    Returns:
    - Updated list of favorite cities
    """
    while True:
        city = input("Enter city name to add to favorites (or 'done' to stop adding): ")
        if city.lower() == 'done':
            break
        favorite_cities.append(city)
    
    print("Favorite cities added:", favorite_cities)
    return favorite_cities

def remove_favorite(favorite_cities):
    """
    Removes a city from the favorite list.
    
    Args:
    - favorite_cities: List of favorite cities
    
    Returns:
    - Updated list of favorite cities
    """
    while(True):
        city = input("Enter city name to remove from favorites (or 'done' to stop removing): ")
        print(favorite_cities)
        if city.lower() == 'done':
            print(favorite_cities)
            break
            #return favorite_cities


        if city in favorite_cities:
            favorite_cities.remove(city)
            print(f"{city} removed from favorites.")
            print(favorite_cities)
        else:
            print(f"{city} is not in your favorites.")

    return favorite_cities

def list_favorites(favorite_cities):
    """
    Lists all cities in the favorite list.
    
    Args:
    - favorite_cities: List of favorite cities
    """
    if favorite_cities:
        print("Favorite cities:", favorite_cities)
    else:
        print("No favorite cities added yet.")

def auto_refresh(city):
    """
    Continuously fetches and displays weather data with a 30-second interval.
    
    Args:
    - city: Name of the city
    """
    print(f"Auto-refresh enabled. Press Ctrl+C to stop.")
    try:
        while True:
            weather_data = get_weather_by_city(city)
            if weather_data:
                print(json.dumps(weather_data, indent=4))
            else:
                print("Error fetching weather data.")
            time.sleep(30)  # Auto-refresh every 30 seconds
    except KeyboardInterrupt:
        print("Auto-refresh stopped.")

def main():
    """
    Entry point of the application.
    """
    favorite_cities = []  # Initialize an empty list to store favorite cities
    
    print("Welcome to Weather Checking Application!")
    city = input("Enter city name: ")
    weather_data = get_weather_by_city(city)
    if weather_data:
        print(json.dumps(weather_data, indent=4))
    else:
        print("Enter a Proper City name")
        main()
    
    while True:
        print("\nOptions:")
        print("1. Add city to favorites")
        print("2. Remove city from favorites")
        print("3. List favorite cities")
        print("4. Enable auto-refresh")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            favorite_cities = add_favorite(favorite_cities)
        elif choice == '2':
            favorite_cities = remove_favorite(favorite_cities)
        elif choice == '3':
            list_favorites(favorite_cities)
        elif choice == '4':
            auto_refresh(city)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
