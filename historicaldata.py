import requests

def fetch_historical_events(year, month, day):
    url = f"http://history.muffinlabs.com/date/{month:02d}/{day:02d}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            events = data['data']['Events']
            filtered_events = [event for event in events if event['year'].startswith(str(year))]
            return filtered_events
        except KeyError:
            print("Unexpected response format. Unable to retrieve historical events.")
    else:
        print(f"Failed to retrieve historical events. Status code: {response.status_code}")

if __name__ == "__main__":
    # Prompt the user for input
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day (1-31): "))

    # Validate input
    if not (1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
        print("Invalid input for year, month, or day.")
    else:
        # Fetch historical events for the specified date
        events = fetch_historical_events(year, month, day)

        if events:
            # Display the filtered events
            print(f"Historical events for {month:02d}/{day:02d}/{year}:")
            for idx, event in enumerate(events, start=1):
                print(f"{idx}. {event['year']}: {event['text']}")
        else:
            print("No events found for the specified date.")
