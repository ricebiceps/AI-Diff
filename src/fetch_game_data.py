import requests
import time
import json
from datetime import datetime
from threading import Thread

def fetch_live_game_data():
    url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
    while True:
        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                game_data = response.json()
                save_data_to_file(game_data)
            else:
                print(f"Failed to get data: {response.status_code}")
        except requests.ConnectionError:
            print("Failed to connect to the game client. Make sure the League of Legends client is running.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(5)  # Fetch data every 5 seconds

def save_data_to_file(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"game_data_{timestamp}.json"
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Saved data to {filename}")
    except Exception as e:
        print(f"Failed to save data: {e}")

if __name__ == "__main__":
    fetch_thread = Thread(target=fetch_live_game_data)
    fetch_thread.start()
