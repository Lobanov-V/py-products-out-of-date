import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products

REAL_DATE = datetime.date


@patch("app.main.datetime.date")
def test_multiple_outdated(mock_date: MagicMock) -> None:
    mock_date.side_effect = (
        lambda *a, **kw: REAL_DATE(*a, **kw)
    )
    mock_date.today.return_value = REAL_DATE(2022, 2, 10)

    products = [
        {
            "name": "a",
            "expiration_date": REAL_DATE(2022, 2, 1),
            "price": 1,
        },
        {
            "name": "b",
            "expiration_date": REAL_DATE(2022, 2, 5),
            "price": 1,
        },
        {
            "name": "c",
            "expiration_date": REAL_DATE(2022, 2, 20),
            "price": 1,
        },
    ]

    assert outdated_products(products) == ["a", "b"]


@patch("app.main.datetime.date")
def test_expired_yesterday(mock_date: MagicMock) -> None:
    mock_date.side_effect = (
        lambda *a, **kw: REAL_DATE(*a, **kw)
    )
    mock_date.today.return_value = REAL_DATE(2022, 2, 10)

    products = [
        {
            "name": "milk",
            "expiration_date": REAL_DATE(2022, 2, 9),
            "price": 1,
        },
    ]

    assert outdated_products(products) == ["milk"]


@patch("app.main.datetime.date")
def test_expiration_today_not_outdated(
    mock_date: MagicMock,
) -> None:
    mock_date.side_effect = (
        lambda *a, **kw: REAL_DATE(*a, **kw)
    )
    mock_date.today.return_value = REAL_DATE(2022, 2, 10)

    products = [
        {
            "name": "bread",
            "expiration_date": REAL_DATE(2022, 2, 10),
            "price": 1,
        },
    ]

    assert outdated_products(products) == []


@patch("app.main.datetime.date")
def test_future_not_outdated(mock_date: MagicMock) -> None:
    mock_date.side_effect = (
        lambda *a, **kw: REAL_DATE(*a, **kw)
    )
    mock_date.today.return_value = REAL_DATE(2022, 2, 10)

    products = [
        {
            "name": "cheese",
            "expiration_date": REAL_DATE(2022, 2, 11),
            "price": 1,
        },
    ]

    assert outdated_products(products) == []
