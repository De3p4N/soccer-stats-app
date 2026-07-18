#  StrikeStat

StrikeStat is a web application that provides soccer fans with live scores, league standings, top scorers, and upcoming fixtures across major club and international competitions. The application retrieves real-time football data from the Football-Data.org REST API and presents it through a responsive, user-friendly interface.

Whether you're following domestic leagues or international tournaments, StrikeStat makes it easy to stay updated with the latest match information and statistics.

---

# Live Demo

**Website:** https://strikestat.onrender.com/

---
# Project Screenshots
<img width="944" height="472" alt="Screenshot 2026-07-18 163333" src="https://github.com/user-attachments/assets/c1affa9d-da50-40f2-954d-2722f5cb899b" />

<img width="944" height="470" alt="Screenshot 2026-07-18 163351" src="https://github.com/user-attachments/assets/af877933-b3f4-4c31-87d9-91a7d5b9a33f" />

<img width="943" height="473" alt="Screenshot 2026-07-18 163420" src="https://github.com/user-attachments/assets/d4c0e8d0-56b6-4b67-b1ea-20bc510a1ec7" />

<img width="940" height="473" alt="Screenshot 2026-07-18 163306" src="https://github.com/user-attachments/assets/e87bdf93-53f1-49fd-ad7a-9741be91ecc6" />



# Features

* View league standings for supported competitions
* Display the top 10 goalscorers for each competition
* View live match scores
* Browse upcoming fixtures up to one month in advance
* Automatic conversion of kickoff times from UTC to Central Time (CT)
* Responsive interface built with Bootstrap
* Support for both club and international competitions

---

#  Supported Competitions

* Premier League
* La Liga
* Bundesliga
* Serie A
* Ligue 1
* Eredivisie
* Primeira Liga
* EFL Championship
* Campeonato Brasileiro Série A
* UEFA Champions League
* UEFA European Championship
* FIFA World Cup
* Copa Libertadores

---

# Technologies Used

# Languages

* Python
* HTML5
* CSS3
* Jinja2

# Frameworks & Libraries

* Flask
* Bootstrap 5
* Requests
* python-dotenv
* Flask-Caching

# API

* Football-Data.org REST API

# Tools & Platforms

* Git
* GitHub
* Render
---

# Installation

These instructions are only necessary if you would like to run StrikeStat locally 

### 1. Clone the repository

```bash
git clone https://github.com/De3p4N/soccer-stats-app.git
```

### 2. Navigate to the project directory

```bash
cd https://github.com/De3p4N/soccer-stats-app.git
```

### 3. Create a virtual environment (recommended)

**Windows Users**

```bash
python -m venv venv
```

**macOS/Linux Users**

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**Windows Users**

```bash
venv\Scripts\activate
```

**macOS/Linux Users**

```bash
source venv/bin/activate
```

### 5. Install the project requirements

```bash
pip install -r requirements.txt
```

### 6. Obtain a Football-Data.org API key

StrikeStat retrieves live football data directly from the Football-Data.org API. To run the project locally, create a free account on Football-Data.org and generate an API key.

Here is the link: https://www.football-data.org/

### 7. Create a `.env` file

In the project root directory, create a file named `.env` and add the following 
to the file:

```text
Football_API_KEY=YOUR_API_KEY_HERE
```

### 8. Run the application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5555
```

---

# 📁 Project Structure

```text
StrikeStat/
│
├── app.py                  # Flask application and routes
├── footballClient.py       # Handles API requests and data processing
├── requirements.txt        # Requirements to run the project locally
├── .env                    # API key (not included in repository)
│
├── templates/
│   ├── base.html # Navigation Bar display
│   ├── index.html # Home Page
│   ├── about.html # Information about me
│   ├── matches.html # Shows match info for each league
│   └── leaguedata.html # Shows league standings for each league
│
├── static/
│   └── images/ # images for league logos
│
└── README.md
```

---

## 📝 Notes

* Football data is provided by the Football-Data.org REST API.
* Upcoming fixtures are displayed for approximately one month beyond the current date.
* Live match scores may be delayed by up to five minutes due to API limitations.
* Match availability depends on the current soccer season and the data provided by the API.
* A free Football-Data.org API key is only required to run the project locally. Visitors to the deployed website do not need an API key.

---

## 📄 License

This project was created for educational and portfolio purposes.
Football data is provided by Football-Data.org and remains subject to their Terms of Service.
