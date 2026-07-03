import urllib.request
import json
import time

def get_live_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    
    try:
        # Fetching the live data
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        
        # Extracting the exact latitude and longitude
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        
        print(f"🌍 LIVE: Latitude {lat} | Longitude {lon}")
        print(f"📍 Map: https://www.google.com/maps/place/{lat},{lon}")
        print("-" * 50)
        
    except Exception as e:
        print(f"Error connecting to satellite API: {e}")

if __name__ == "__main__":
    print("🚀 Tracking the International Space Station...")
    print("Press Ctrl+C in your terminal to stop tracking.\n")
    
    try:
        # The infinite loop that updates every 5 seconds
        while True:
            get_live_iss_location()
            time.sleep(5) 
            
    except KeyboardInterrupt:
        print("\nTracking stopped, bro. Ready to push to GitHub!")