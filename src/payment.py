def process_payment(amount, method, authorized):
    if amount <= 0:
        raise ValueError("Valor inválido")

    if not authorized:
        return {"status": "denied", "amount": amount}

    if method == "credit_card":
        return {"status": "approved", "amount": amount}

    elif method == "pix":
        return {"status": "approved", "amount": amount}

    elif method == "boleto":
        return {"status": "pending", "amount": amount}

    else:
        raise ValueError("Método de pagamento inválido")