import streamlit as st
from bot.client import get_client
from bot.orders import place_order

st.set_page_config(page_title="Trading Bot", layout="centered")

st.title("🚀 Trading Bot (Binance Futures Testnet)")
st.markdown("Simple UI for placing MARKET, LIMIT, and STOP orders")

# --- FORM ---
with st.form("order_form"):
    st.subheader("📊 Order Details")

    symbol = st.text_input("Symbol", "BTCUSDT")

    col1, col2 = st.columns(2)
    with col1:
        side = st.selectbox("Side", ["BUY", "SELL"])
    with col2:
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP"])

    quantity = st.number_input("Quantity", min_value=0.001, value=0.002, step=0.001)

    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = st.number_input("Limit Price", value=60000.0)

    if order_type == "STOP":
        stop_price = st.number_input("Stop Price", value=65000.0)

    submitted = st.form_submit_button("Place Order")

# --- ACTION ---
if submitted:
    try:
        client = get_client()

        order = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price
        )

        st.success("✅ Order Placed Successfully!")

        st.subheader("📄 Order Details")
        
        st.write("Order ID:", order.get("orderId"))
        st.write("Status:", order.get("status"))
        st.write("Executed Qty:", order.get("executedQty"))
        st.write("Avg Price:", order.get("avgPrice"))
        st.write("Symbol:", order.get("symbol"))
        st.write("Side:", order.get("side"))

    except Exception as e:
        st.error(f"❌ Error: {e}")