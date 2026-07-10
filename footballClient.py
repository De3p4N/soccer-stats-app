# The footballClient.py accesses various data from the API. This file contains the functions 
# used to access each type of data. 

import requests 
import os # needed to use data from .env file
from dotenv import load_dotenv # this imports and uses the API key in the .env file
from datetime import date, datetime,timedelta # used in get_todays_matches()
from zoneinfo import ZoneInfo # used to convert timezones to Central Time.

# This function measures how many API requests are called when a user accesses data
# I used this to measure how many API calls were saved by implementing caching
api_call_count = 0
def log_api_call(func_name):
    global api_call_count
    api_call_count += 1
    print(f"[API CALL #{api_call_count}] {func_name}")

# This is used so people don't use your API key
load_dotenv()

base_url = "https://api.football-data.org/v4"
api_key = os.getenv("Football_API_KEY") # used the variable in the .env file

header = {
    "X-Auth-Token": api_key
}

# This function returns competitions
def get_competitions():
    response = requests.get(f"{base_url}/competitions", headers=header)
    if response.status_code == 200: # status code 200 means the data was retrieved successfully
        data = response.json()
        competitions = data["competitions"]
        return competitions
    else:
        print("Error fetching competitions:", response.status_code) 
        return []

# This returns league standings
def get_league_standings(league_code):
    log_api_call("get_league_standings") # if user views this data point, this shows how many API requests occured
    response = requests.get(f"{base_url}/competitions/{league_code}/standings", headers=header)
    if response.status_code == 200:
        data = response.json()
        return data.get("standings", [])
    else:
        print("Error fetching standings:", response.status_code)
        return []     

# returns all current live matches
def get_live_matches(league_code=None):
    log_api_call("get_live_matches")
    params = {
        "status": "LIVE",
    }

    response = requests.get(
        f"{base_url}/matches",
        headers=header,
        params=params
    )

    if response.status_code == 200:
        data = response.json()
        matches = data["matches"]
        # This filters all live matches by competition and then returns the filtered matches 
        filtered_matches = []

        for match in matches:
            if match["competition"]["code"] == league_code:
                filtered_matches.append(match)

        matches = filtered_matches
        return matches

    else:
        print("Error fetching Live Matches", response.status_code)
        return []

# returns matches scheduled for the date the program is accessed
def get_upcoming_matches(league_code):
    log_api_call("get_upcoming_matches")

    today = date.today()

    params = {
        "dateFrom": today.strftime("%Y-%m-%d"),
        "dateTo": (today + timedelta(days=30)).strftime("%Y-%m-%d"),
        "status": "SCHEDULED",
    }

    response = requests.get(
        f"{base_url}/competitions/{league_code}/matches",
        headers=header,
        params=params
    )

    if response.status_code == 200:
        data = response.json()
        matches = data["matches"]   

        # This loop returns all match times in Central Time. 
        central = ZoneInfo("America/Chicago")

        today_ct = datetime.now(central).date()
        tomorrow_ct = today_ct + timedelta(days=1)

        for match in matches:
            utc_str = match.get("utcDate")

            if utc_str:
                dt_utc = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
                dt_local = dt_utc.astimezone(central)

                match_date_ct = dt_local.date()
                if match_date_ct == today_ct:
                    match["match_date"] = "Today"
                elif match_date_ct == tomorrow_ct:
                    match["match_date"] = "Tomorrow"
                else:
                    match["match_date"] = dt_local.strftime("%b %d, %Y")

                match["kickoff_time"] = dt_local.strftime("%I:%M %p")
                match["timezone_label"] = "CT"
                
        return matches
    else:
        print("Error fetching today's Matches:", response.status_code)
        return []
    
# returns the top goalscoring players for their respective leagues
def get_top_scorers(league_code):
    log_api_call("get_top_scorers")
    response = requests.get(f"{base_url}/competitions/{league_code}/scorers", headers=header, params={"limit":10}) # API only gives top 10
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching top goalscorers", response.status_code)
        return []