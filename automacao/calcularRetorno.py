import numpy as np
import matplotlib.pyplot as plt

from automacao.automatizarNegociacao import msft_data

close_price = msft_data[['Adj_Close']]
daily_return = close_price.pct_change()
daily_return.fillna(0, inplace=True)

print(daily_return)

adj_price = msft_data['Adj_Close']
mav = adj_price.rolling(window=50).mean()
print(mav[-10:])

adj_price.plot()
mav.plot()

