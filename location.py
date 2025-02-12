import requests

def get_device_location():
    # You can choose a service like ipinfo.io, ipapi.co, or some other equivalent
    try:
        response = requests.get('https://ipinfo.io/json')
        location_data = response.json()

        # Extracting latitude and longitude from location data
        # Note: The exact fields depend on the API used
        loc = location_data.get("loc", "No location found")
        city = location_data.get("city", "No city found")
        region = location_data.get("region", "No region found")
        country = location_data.get("country", "No country found")

        print(f"Coordinates: {loc}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")

    except requests.RequestException as e:
        print("Error fetching location information:", e)

if __name__ == "__main__":
    get_device_location()
