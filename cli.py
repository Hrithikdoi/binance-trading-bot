import typer
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

app = typer.Typer()

# Start logging
setup_logger()


@app.command()
def order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):

    try:
        # Validate inputs
        validate_side(side)
        validate_order_type(order_type)

        print("\n----- ORDER REQUEST -----")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Order Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        # MARKET order
        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)

        # LIMIT order
        else:
            if price is None:
                raise ValueError("Price is required for LIMIT order")

            response = place_limit_order(symbol, side, quantity, price)

        print("\n----- ORDER RESPONSE -----")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response['executedQty']}")

        print("\n✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    app()