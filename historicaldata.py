# Fetching Historical data
import requests


def fetch_historical_events(year, month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        events = data['data']['Events']
        filtered_events = [event for event in events if event['year'].startswith(str(year))]
        return filtered_events
    else:
        print("Failed to retrieve historical events.")
        return None


if __name__ == "__main__":
    # Specify the date and year for which you want historical events
    year = 2001
    month = 9
    day = 11

    # Fetch historical events for the specified date and year
    events = fetch_historical_events(year, month, day)

    if events:
        # Display the filtered events
        print(f"Historical events for the year {year}:")
        for idx, event in enumerate(events, start=1):
            print(f"{idx}. {event['year']}: {event['text']}")
    else:
        print("No events found for the specified date and year.")