import pytest
from src.payment import process_payment


def test_payment_credit_card_success():
    result = process_payment(100, "credit_card", True)

    assert result["status"] == "approved"
    assert result["amount"] == 100


def test_payment_pix_success():
    result = process_payment(200, "pix", True)

    assert result["status"] == "approved"
    assert result["amount"] == 200


def test_payment_boleto_pending():
    result = process_payment(150, "boleto", True)

    assert result["status"] == "pending"


def test_payment_invalid_amount():
    with pytest.raises(ValueError):
        process_payment(-50, "credit_card", True)


def test_payment_not_authorized():
    result = process_payment(100, "credit_card", False)

    assert result["status"] == "denied"
