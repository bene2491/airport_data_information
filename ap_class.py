from bs4 import BeautifulSoup
import requests

class Airport:
    """
    Describes main airport attributes 
    """
    def __init__(self, ICAO, Airport, Coordinates, Runways, METAR):
        self.ICAO = ICAO
        self.Airport = Airport
        self.Coordinates = Coordinates 
        self.Runways = Runways
        self.METAR = METAR



def get_data(self, ICAO):
# get base data
# https://airportnavfinder.com/airport/
    main_url = "https://airportnavfinder.com/airport/"
    url = main_url + str(ICAO)
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("title")
    Airport = title.text
    raw_data = soup.find("tr")
    data = raw_data.text
    


