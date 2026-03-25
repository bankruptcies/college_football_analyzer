# 🏈 College Football Team Analysis Tool

A Python-based data analysis project that uses the CollegeFootballData API to analyze team performance and player statistics for a given season.

Built to demonstrate API integration, data processing, and real-world analytics.

---

## 🚀 Features

* Retrieve game and player data from the CFBD API
* Shows the availabe years for whatever team you are interested in
* Analyze team performance:

  * Wins / Losses
  * Average points scored
  * Highest scoring game
* Identify team leaders (more to come):

  * Passing (TDs)
  * Rushing (Yards)
  * Receiving (Yards)
  * Tackles
  * Interceptions
  * Sacks
* Handles:

  * Invalid team inputs
  * Empty user input
  * API errors

---

## 🛠️ Tech Stack

* Python
* REST API (CollegeFootballData API)
* dotenv (environment variables)

---

## 📂 Project Structure

cfb_project/
│── main.py              # Entry point
│── config.py            # API configuration
│── data_fetcher.py      # API calls
│── analysis.py          # Data processing
│── display.py           # Output formatting
│── .env                 # API key (ignored)
│── .gitignore
│── requirements.txt

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/cfb_project.git
cd cfb_project

### 2. Install dependencies

pip install -r requirements.txt

### 3. Get an API Key

* Go to https://collegefootballdata.com
* Create a free account
* Copy your API key

### 4. Create a `.env` file

CFBD_API_KEY=your_api_key_here

### 5. Run the program

python main.py

---

## 💻 Example Usage

Enter a team: Michigan
Enter a season year: 2023

--- Team Analysis ---
Wins: 15
Losses: 0
Average Points: 35.4
Highest Scoring Game: 52

--- Team Leaders ---
Passing Leader (touchdowns): JJ McCarthy - 22
Rushing Leader (yards): Blake Corum - 1245

---

## ⚠️ Error Handling

This project handles:

* Missing API key
* Unauthorized API access (401 errors)
* Empty user input
* Invalid team names
* Missing stat categories

---

## 📈 Future Improvements

* Export results to CSV
* Add more leader categories

---

## ⭐ Why This Project Matters

This project demonstrates:

* Real-world API integration
* Data cleaning and processing
* Analytical thinking with sports data
* Debugging and handling edge cases

---

## 📜 License

This project is for educational purposes.
