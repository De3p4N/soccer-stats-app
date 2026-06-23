# The app.py uses Flask, the python web framework, to connect the footballClient.py
# file to the html files. Running this will run the app 

from flask import Flask, render_template
from flask_caching import Cache
from footballClient import(get_league_standings, get_live_matches, 
                           get_top_scorers, get_upcoming_matches)

# This part of the code configures and initializes the caching method
config ={
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# These are the supported leagues given by the free version of the API. This dictionary is
# key:value pairs of {league_code : league_name}
LEAGUES = {
    "PL": "Premier League",
    "PD" : "Primera Division", # La Liga
    "BL1" : "Bundesliga",
    "SA" : "Serie A",
    "FL1" : "Ligue 1",
    "DED": "Eredivisie",
    "PPL": "Primeira Liga", # Portuguese League
    "EC" : "European Championship",  # Euros
    "ELC" : "Championship", # 2nd tier English football
    "BSA" : "Campeonato Brasileiro Série A",  # Brazilian League
    "CL" : "UEFA Champions League",
    "WC" :  "FIFA World Cup",
    "CLI" : "Copa Libertadores" # South American club competition
}

# images of competition logos
LEAGUE_IMAGES = {
    "PL" : "images/premierLeague.png",
    "PD" : "images/laliga.png",
    "BL1" : "images/Bundesliga.png",
    "SA" : "images/serieA.png",
    "FL1" : "images/Ligue_1.png",
    "DED" : "images/Eredivisie.png",
    "PPL" : "images/portuguese_league.png",
    "EC" : "images/euros.png",
    "ELC" : "images/EFL_Championship_Logo.png",
    "BSA" : "images/brazil_league.png",
    "CL" : "images/UEFA_Champions_League.png",
    "WC" : "images/worldcup.png",
    "CLI" : "images/Copa_Libertadores_logo.png",
}

# This app route is for the home page of the site
@app.route('/')
@cache.cached(timeout=600) # I cached the homepage for 600 seconds (10 minutes)
def index():
    return render_template('index.html',leagues=LEAGUES, league_images=LEAGUE_IMAGES)

# This app route is for the about page of the site
@app.route('/about')
@cache.cached(timeout=600) # I cached the homepage for 600 seconds (10 minutes)
def about():
    return render_template('about.html',leagues=LEAGUES, league_images=LEAGUE_IMAGES)


# The get_live_matches() and get_upcoming_matches() are both smaller functions
# that are split up to make the matches.html file work and display live and future
# matches. I split them to cache live responses for 5 minutes, and future matches for 15 minutes

# Live scores cached data
@cache.memoize(timeout=300)  # 5 minutes
def cache_live_matches(league_code):
    try:
        return get_live_matches(league_code)
    except Exception as e:
        print(f"API Error on live matches: {e}")
        return []


# Separate, longer cache for the upcoming matches only
@cache.memoize(timeout=900) # 15 minutes 
def cache_upcoming_matches(league_code):
    try:
        return get_upcoming_matches(league_code)
    except Exception as e:
        print(f"API Error on today's matches: {e}")
        return []


# The route calls the two cached helper functions.
@app.route('/matches/<league_code>')
def upcoming_matches(league_code):
    upcoming_matches_data = cache_upcoming_matches(league_code)
    live_matches = cache_live_matches(league_code)

    league_name = LEAGUES.get(league_code, league_code)
    return render_template('matches.html',
                            leagues=LEAGUES,
                            upcoming_matches=upcoming_matches_data,
                            live_matches=live_matches,
                            league_images=LEAGUE_IMAGES,
                            league_name=league_name)

# This app route is for league standings and top scorers
@app.route('/standings/<league_code>')
@cache.memoize(timeout=900) # Used cache.memoize() for dynamic URLs, cached for 15 minutes
def standings(league_code):
    standings_data = []
    scorer_list = []
    scorers_data = []
    try:
        standings_data = get_league_standings(league_code)
    except Exception as e:
        print(f"API Error on standings: {e}")
        
    try:
        scorers_data = get_top_scorers(league_code)
        
        if isinstance(scorers_data, dict):
            scorer_list = scorers_data.get("scorers", [])
                  
    except Exception as e:
        print(f"API Error on scorers: {e}")

    league_name = LEAGUES.get(league_code, league_code)

    return render_template('leaguedata.html',
                           standings=standings_data,
                           scorers=scorer_list,
                           current_league=league_code,
                           leagues=LEAGUES,
                           league_name=league_name,
                           league_images=LEAGUE_IMAGES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555,debug=False)