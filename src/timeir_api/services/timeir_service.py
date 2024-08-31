from bs4 import BeautifulSoup
import httpx

URL = "https://www.time.ir/"


async def get_content():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
    return soup


async def get_current_date():
    scraper = await get_content()
    months = [m.text for m in scraper.select("div.dateType span")][:3]
    days = [d.text for d in scraper.select("div.dateText span")][:3]
    date_time = {months[num]: days[num] for num in range(len(days))}
    return date_time


async def get_random_quote():
    scraper = await get_content()
    quote_text = scraper.find("div", class_="randomQuote").find("span").text.strip()
    return quote_text
