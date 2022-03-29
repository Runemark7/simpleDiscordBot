import requests
from bs4 import BeautifulSoup as soup
from datetime import datetime

URLs = [
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z4104vQQ3wZ5759Y63yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z6104vQQ3wZ5759Y64yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z0104vQQ3wZ5759Y64yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z1104vQQ3wZ5759Y64yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5081Z5104vQQ3wZ5759Y60yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5081Z3104vQQ3wZ5759Y60yY5Y67QQ.html"
]
roomNames = [
    "R3144",
    "R3147",
    "R3145",
    "R3336",
    "R4145",
    "R4341"
]
currDayNumber = datetime.today().weekday()

def getAllRooms():
    allBookings = []

    for i in range(len(URLs)):
        page = requests.get(URLs[i])
        page_soup = soup(page.text, "html.parser")

        getcurrweekdaysHtml = page_soup.find_all("div", {"class": "weekDay"})
        currDaySoupHtml = getcurrweekdaysHtml[currDayNumber].find_all("div", {"class": "weekDiv"})[1]
        currDayTimeDivArr = currDaySoupHtml.find_all("div", {"class": "timeDiv"})

        bookingsToday = []

        bookingsToday.append(roomNames[i])

        for index in range(0, len(currDayTimeDivArr), 2):
            endTime = currDayTimeDivArr[index]
            startTime = currDayTimeDivArr[index+1]
            bookingsToday.append(startTime.text + " - " + endTime.text)

        allBookings.append(bookingsToday)

    returnStr = ""

    for i in range(len(allBookings)):
        returnStr += allBookings[i][0] + ": "
        for j in range(1, len(allBookings[i])):
            returnStr += allBookings[i][j] + ", "
        returnStr += "\n"

    return returnStr
