#display AI articles of 90 days
import requests
r = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles.json")
print("90 days of visits broken down by browser for all sites:")
print(r.json()['totals']['browser'])
