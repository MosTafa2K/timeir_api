from bs4 import BeautifulSoup
import httpx
from timeir_api.exceptions import TimeOutExc, ConnectionExc

URL = "https://www.time.ir/"


async def get_content():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(URL, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup
        except httpx.TimeoutException:
            raise TimeOutExc()
        except httpx.ConnectError:
            raise ConnectionExc()


async def get_current_date():
    scraper = await get_content()
    months = ["solar", "gregorian", "lunar"]
    days = [d.text for d in scraper.select("div.dateText span")][:3]
    date_time = {months[num]: days[num] for num in range(len(days))}
    return date_time


async def get_random_quote():
    scraper = await get_content()
    quote_text = scraper.find("div", class_="randomQuote").find("span").text.strip()
    quote_author = scraper.find("div", class_="reverseAlign").find("a").text.strip()
    return {"text": quote_text, "author": quote_author}
