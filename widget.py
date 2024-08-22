import tkinter as tk
import requests
from tkinter import ttk

def get_crypto_prices():
    url = 'https://api.binance.com/api/v3/ticker/24hr'
    symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT']
    data = requests.get(url).json()
    prices = {}
    for item in data:
        if item['symbol'] in symbols:
            prices[item['symbol']] = {
                'price': float(item['lastPrice']),
                'change': float(item['priceChangePercent'])
            }
    return prices

def update_prices():
    prices = get_crypto_prices()
    update_label(bitcoin_label, prices['BTCUSDT'])
    update_label(ethereum_label, prices['ETHUSDT'])
    update_label(solana_label, prices['SOLUSDT'])
    root.after(update_interval, update_prices)  # Schedule the next update

def update_label(label, data):
    price = data['price']
    change = data['change']
    color = 'green' if change >= 0 else 'red'
    label.config(text=f'{label.symbol}: ${price:.2f} ({change:.2f}%)', foreground=color)

def place_window_bottom_right():
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = root.winfo_screenwidth() - width
    y = root.winfo_screenheight() - height
    root.geometry(f'{width}x{height}+{x}+{y}')

# Set the update interval (in milliseconds)
# 10000 milliseconds = 10 seconds
# 30000 milliseconds = 30 seconds
# 60000 milliseconds = 1 minute
update_interval = 10000  # Adjust this value as needed

root = tk.Tk()
root.title('Crypto Prices')
root.attributes('-topmost', True)  # Keep the window on top
root.overrideredirect(True)  # Remove window decorations
root.config(bg='black')

main_frame = ttk.Frame(root, padding="5")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create and configure labels
bitcoin_label = ttk.Label(main_frame, font=('Helvetica', 12), background='black')
bitcoin_label.symbol = 'BTC'
bitcoin_label.grid(row=0, column=0, sticky=(tk.W, tk.E))

ethereum_label = ttk.Label(main_frame, font=('Helvetica', 12), background='black')
ethereum_label.symbol = 'ETH'
ethereum_label.grid(row=1, column=0, sticky=(tk.W, tk.E))

solana_label = ttk.Label(main_frame, font=('Helvetica', 12), background='black')
solana_label.symbol = 'SOL'
solana_label.grid(row=2, column=0, sticky=(tk.W, tk.E))

update_prices()
place_window_bottom_right()

root.mainloop()