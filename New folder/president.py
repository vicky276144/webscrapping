# display the list of former president
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://presidentofindia.nic.in/former-presidents.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

presidents = []

for president in soup.select("tbody tr"):
    name = president.select("td")[0].text.strip()
    term = president.select("td")[1].text.strip()
    presidents.append((name, term))

df = pd.DataFrame(presidents, columns=["Name", "Term"])
print(df)