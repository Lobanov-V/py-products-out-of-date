import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


REAL_DATE = datetime.date


@patch("app.main.datetime.date")
def test_multiple_outdated(mock_date: MagicMock) -> None:
    mock_date.side_effect = lambda *a, **kw: REAL_DATE(*a, **kw)
    mock_date.today.return_value = REAL_DATE(2022, 2, 10)

    products = [
        {"name": "a", "expiration_date": REAL_DATE(2022, 2, 1), "price": 1},
        {"name": "b", "expiration_date": REAL_DATE(2022, 2, 5), "price": 1},
        {"name": "c", "expiration_date": REAL_DATE(2022, 2, 20), "price": 1},
    ]

    result = outdated_products(products)

    assert result == ["a", "b"]
