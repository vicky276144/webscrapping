#display top 10 ODI Mens cricket team
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

teams = []

for team in soup.select("tbody tr"):
    name = team.select("td")[1].text.strip()
    matches = team.select("td")[2].text.strip()
    points = team.select("td")[3].text.strip()
    rating = team.select("td")[4].text.strip()
    teams.append((name, matches, points, rating))

df = pd.DataFrame(teams, columns=["Team", "Matches", "Points", "Rating"])
df = df.head(10)  # get only top 10 teams
print(df)