import os
import pickle
import datetime
import calendar
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Scopes required for the application
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the credentials JSON file relative to this script
CREDENTIALS_FILE = os.path.join(script_dir, 'credentials.json')

def authenticate_google_calendar():
    creds = None
    token_path = os.path.join(script_dir, 'token.pickle')
    
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def fetch_israel_holidays(service):
    # Israel holidays calendar ID
    calendar_id = 'en.il#holiday@group.v.calendar.google.com'
    
    # Define the time range for the events (2023)
    time_min = '2023-01-01T00:00:00Z'
    time_max = '2023-12-31T23:59:59Z'
    
    # Fetch events
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = events_result.get('items', [])
    holidays = {event['start'].get('date'): event['summary'] for event in events}
    return holidays

def get_days_of_year(year):
    days_of_year = []
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            date = datetime.date(year, month, day)
            day_of_week = date.strftime('%A')
            days_of_year.append({
                'date': date.isoformat(),
                'day_of_week': day_of_week,
                'event': None  # Placeholder for holiday/event
            })
    return days_of_year

def populate_events(days, holidays):
    for day in days:
        if day['date'] in holidays:
            day['event'] = holidays[day['date']]
    return days

if __name__ == '__main__':
    service = authenticate_google_calendar()
    holidays = fetch_israel_holidays(service)
    days_of_year = get_days_of_year(2023)
    days_with_events = populate_events(days_of_year, holidays)
    
    for day in days_with_events:
        print(f"Date: {day['date']}, Day: {day['day_of_week']}, Event: {day['event']}")
