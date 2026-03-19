import logging

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        logging.info(f"Request: {symbol} {side} {order_type} {quantity} price={price} stop_price={stop_price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT order requires price")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP":
            if stop_price is None:
                raise ValueError("STOP order requires stop_price")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=stop_price,
                quantity=quantity
            )

        else:
            raise ValueError("Invalid order type")

        logging.info(f"Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise