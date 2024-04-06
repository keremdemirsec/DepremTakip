import requests
from flask import Flask, render_template, jsonify, json
from bs4 import BeautifulSoup

app = Flask(__name__)
json.provider.DefaultJSONProvider.ensure_ascii = False

AFAD_URL = "https://deprem.afad.gov.tr/last-earthquakes.html"

def get_earthquake_data():
    try:
        response = requests.get(AFAD_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table")
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")

        earthquakes = []

        for row in rows:
            cols = row.find_all("td")
            earthquake = {
                "Tarih": cols[0].text.strip(),
                "Enlem": cols[1].text.strip(),
                "Boylam": cols[2].text.strip(),
                "Derinlik": cols[3].text.strip(),
                "Tip": cols[4].text.strip(),
                "Büyüklük": cols[5].text.strip(),
                "Yer": cols[6].text.strip(),
            }
            earthquakes.append(earthquake)

        return earthquakes

    except requests.RequestException as e:
        return {"error": str(e)}

@app.route("/")
def home():
    return render_template("index.html", earthquakes=get_earthquake_data())

@app.route("/api/earthquakes")
def get_earthquakes_api():
    return jsonify({"earthquakes": get_earthquake_data()})

if __name__ == "__main__":
    app.run(debug=True)
