# github-Gym

**Optimizing Your Gym Visit at UC Davis**  
A tool that finds the optimal time to visit the UC Davis Gym by analyzing occupancy data.

## Overview

The **github-Gym** project is designed to help students plan their gym visits by determining the best time to go based on real-time occupancy data scraped from the UC Davis Recreation page. The system collects occupancy data periodically, visualizes trends using bar plots, and identifies the time slot with the lowest crowding—making it easier for you to have a stress-free workout session.

### Key Features

- **Real-Time Data Scraping:** Uses a web scraper to collect current gym occupancy data from the UC Davis Recreation website.
- **Automated Data Collection:** Utilizes background scheduling to fetch and update data every minute at specific intervals (e.g., on the hour and half-hour).
- **Data Visualization:** Generates bar plots to display occupancy trends over time.
- **Optimal Time Identification:** Processes the data to pinpoint the best time (lowest occupancy) to visit the gym.
- **Flask Backend & JSON API:** Provides a web interface and an API endpoint for accessing current occupancy data.
- **Next.js Frontend:** A modern, user-friendly interface bootstrapped with Create Next App.

## Project Structure
```bash
github-Gym/
├── backend/
│   ├── app.py              # Main Flask application handling routing, data scraping, plotting, and API endpoints.
│   ├── webscraper.py       # Contains functions to scrape occupancy data and fetch the current time.
│   ├── graph.py            # (Optional) Additional plotting utilities.
│   ├── templates/          # HTML templates for the web interface.
│   └── static/
│       └── images/         # Directory where generated plots are saved.
└── frontend/
    ├── public/             # Public assets.
    ├── src/                # Frontend source files.
    ├── package.json        # Frontend dependencies and scripts.
    ├── tsconfig.json       # TypeScript configuration.
    └── README.md           # Next.js project documentation.
```    
# Getting Started

## Prerequisites

- **Backend:**
  - Python 3.7+
  - pip
- **Frontend:**
  - Node.js 14+
  - npm or yarn

## Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/munneth/github-Gym.git
   cd github-Gym/backend

2. **Install Dependencies:**

     ```bash
     Copy
     pip install -r requirements.txt

This installs necessary Python packages such as Flask, requests, BeautifulSoup, APScheduler, and matplotlib.

3. **Start the Development Server:**

```bash
Copy
python app.py
The application should run on http://localhost:5000.
```

## Frontend Setup
1. **Navigate to the Frontend Directory:**

```bash
Copy
cd ../frontend
```
2. **Install Dependencies:**

```bash
Copy
npm install
```
3.**Start the Development Server:**

```bash
npm run dev
```
The Next.js app will be available at http://localhost:3000.

## Usage
Web Interface:
Visit the React app's URL to view real-time occupancy data, the generated occupancy plot, and the best time to visit the gym.

API Endpoint:
Access /api/info to receive a JSON response containing:

Current occupancy data.

Historical time-occupancy data.

The optimal time to visit based on the lowest occupancy.

Frontend:
The Next.js frontend fetches data from the Flask API and displays it in a modern UI.




License
This project is licensed under the MIT License.

