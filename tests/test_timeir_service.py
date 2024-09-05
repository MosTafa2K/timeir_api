from unittest.mock import AsyncMock, patch
import pytest
import httpx
from bs4 import BeautifulSoup
from timeir_api.services.timeir_service import (
    get_content,
    get_current_date,
    get_random_quote,
)
from timeir_api.exceptions import TimeOutExc, ConnectionExc


@pytest.mark.asyncio
async def test_get_content_success():
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response = AsyncMock()
        mock_response.text = "<html>Mock HTML</html>"
        mock_get.return_value = mock_response
        soup = await get_content()
        assert soup.name == "[document]"
        assert isinstance(soup, BeautifulSoup)
        assert soup.text == "Mock HTML"
        assert mock_response.text == "<html>Mock HTML</html>"


@pytest.mark.asyncio
async def test_get_content_timeout():
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.side_effect = httpx.TimeoutException("Mock timeout")
        with pytest.raises(TimeOutExc):
            await get_content()


@pytest.mark.asyncio
async def test_get_content_connection_error():
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.side_effect = httpx.ConnectError("Mock connection error")
        with pytest.raises(ConnectionExc):
            await get_content()


@pytest.mark.asyncio
async def test_get_current_date():
    mock_html_content = """
    <html>
        <div class="dateType">
            <span>خورشیدی</span><span>میلادی</span><span>قمری</span>
        </div>
        <div class="dateText">
            <span>یکشنبه - ۱۱ شهریور ۱۴۰۳</span><span>Sunday - 2024 01 September</span><span>الأحد - ٢٧ صفر ١٤٤٦</span>
        </div>
    </html>
    """

    with patch(
        "timeir_api.services.timeir_service.get_content", new_callable=AsyncMock
    ) as mock_get_content:
        mock_get_content.return_value = BeautifulSoup(mock_html_content, "html.parser")

        result = await get_current_date()

        assert result is not None
        assert result == {
            "solar": "یکشنبه - ۱۱ شهریور ۱۴۰۳",
            "gregorian": "Sunday - 2024 01 September",
            "lunar": "الأحد - ٢٧ صفر ١٤٤٦",
        }


@pytest.mark.asyncio
async def test_get_random_quote():
    mock_html_content = """
    <html>
        <div class="randomQuote">
            <span>این یک نقل قول است.</span>
        </div>
        <div class="reverseAlign">
            <a>نام نویسنده</a>
        </div>
    </html>
    """

    with patch(
        "timeir_api.services.timeir_service.get_content", new_callable=AsyncMock
    ) as mock_get_content:
        mock_get_content.return_value = BeautifulSoup(mock_html_content, "html.parser")

        result = await get_random_quote()

        assert result is not None
        assert isinstance(result, dict)
        assert result["text"] == "این یک نقل قول است."
        assert result["author"] == "نام نویسنده"
