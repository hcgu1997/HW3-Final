import pandas as pd

file = pd.read_csv("/Users/gu/Desktop/submitted_orders.csv")

file = pd.concat(
        [file, pd.DataFrame({
            "timestamp": ["time"],
            "order_id": ["orderid"],
            "client_id": ["client_id"],
            "perm_id": ["permid"],
            "con_id": ["permid"],
            "symbol": ["symbol"],
            "action": ["action"],
            "size": ["size"],
            "order_type": ["ordertype"],
            "lmt_price": ["ordertype"]
        })])

file.to_csv("/Users/gu/Desktop/submitted_orders.csv")