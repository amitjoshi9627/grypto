import requests
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

url = "https://api.nomics.com/v1/currencies/ticker?key=ff5e8e5b3e26206a1f95a0fba9a68d89"

large = 22
med = 16
small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use(['seaborn-whitegrid'])
sns.set_style("white")
style.use('ggplot')

crypt_dictionary = {"Bitcoin": "BTC", "Ethereum": "ETH", "Ripple": "XRP", "Bitcoin Cash": "BCH",
                    "Litecoin": "LTC", "Stellar": "XLM", "Tether": "USDT", "Bitcoin SV": "BSV", "Dash": "DASH"}
crypt_arr = ['Bitcoin', 'Ethereum', 'Ripple', 'Bitcoin Cash',
             'Litecoin', 'Stellar', 'Tether', 'Bitcoin SV', 'Dash']
print("Choose a currency:")
for ind, crypt in enumerate(crypt_arr):
    print(ind+1, crypt)
choice = int(input())
currency = crypt_arr[choice - 1]
currency_symbol = crypt_dictionary[currency]
url = url + "&ids="+str(currency_symbol)

plt.ion()
x = []
y = []
for i in range(5):
    req = requests.get(url).json()[0]
    price = req['price']
    y_val = round(float(price), 2)
    x.append(i)
    y.append(y_val)
    plt.gca().cla()  # optionally clear axes
    plt.plot(x, y, color='b')
    plt.xlim(left=max(0, i-80), right=i+80)
    plt.title("Live", currency, "Price")
    plt.xticks(rotation=0, fontsize=12, horizontalalignment='center', alpha=.7)
    plt.yticks(fontsize=12, alpha=.7)
    plt.grid(axis='both', alpha=.3)
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)
    plt.plot(x, y, color='tab:blue')
    plt.draw()
    plt.pause(0.1)
