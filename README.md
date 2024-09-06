# Timeir Unofficial API ⏰🚀
**An efficient and unofficial API to interact with time.ir and fetch calendar and quote information.**

## Overview 🔎
The **Timeir API** is an unofficial API for interacting with the [time.ir](https://www.time.ir) website and fetching information from it. This API can be easily integrated into any Python project requiring date or quote information from time.ir.


## Features ✨
* Get current date in formats:
    * Solar
    * Lunar
    * Gregorian
* Get a random quote text with it's author


## Prerequisites 🛠️
- Python >= 3.9.x
- pytest
- pytest-asyncio
- FastAPI
- BeautifulSoup
- httpx
- uvicorn

> Note: You can easily install all requirement packages just using `pdm install` or `pip install -r requirements.txt`

## Run ⚡
First create virtual environment:
```bash
python -m venv venv
```


# Install pdm 📥
### **Active venv:**
Windows
```bash
venv\Scripts\activate
```
Linux
```bash
venv\bin\activate
```

### Then:
Go to main directory:
```bash
cd src\timeir_api\
```

Excecute using `uvicorn` :
```bash
uvicorn main:app --reload
```


# Example Usage 💡
### Here is a simple example of how to fetch the current date:

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/date/current"
```
### Expected response:
```json
{
    "date": {
        "solar": "سه شنبه - ۱۳ شهریور  ۱۴۰۳",
        "gregorian": "Tuesday - 2024 03 September",
        "lunar": "الثلاثاء - ٢٩ صفر ١٤٤٦"
    }
}

```
# License 🧾
#### This project is licensed under the MIT License.