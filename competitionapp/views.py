from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re


# Create your views here.
def current_competitions_view(request):

    if request.method == "GET":

        URL = "https://zawodykonne.com/zawody/aktualne"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) '
                                 'Chrome/114.0.0.0 Safari/537.36'}
        response = requests.get(url=URL, headers=headers)

        soup = BeautifulSoup(response.content, "html.parser")

        competitions = soup.find_all(name="strong")

        competitions_list = [s.getText().strip() for s in competitions[1:]]

        dates = [elem for elem in competitions_list[::3]]
        places = [elem for elem in competitions_list[1::3]]
        names = [elem for elem in competitions_list[2::3]]

        elements = soup.find_all('a')
        list_of_links = []

        for elem in elements:
            item = elem.get("href")
            if item.startswith(
                    "/zawody/") and 'zgloszenia' not in item and 'aktualne' not in item and 'wyniki' not in item:
                list_of_links.append(item)

        wanted_links = list(dict.fromkeys(list_of_links))

        full_details_list = []
        for idx in range(100):
            full_details_list.append(dates[idx] + ' ' + places[idx] + ' ' + names[idx])

        all = zip(full_details_list, wanted_links)

        return render(
            request,
            'competitions/competitions.html',
            context={
                "full_details_list": full_details_list,
                "wanted_links": wanted_links,
                "all": all,
            }
        )