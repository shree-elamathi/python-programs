import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import pandas as pd
pd.set_option('future.no_silent_downcasting', True)


def visualize_domain_growth(domain_name):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([domain_name], cat=0, timeframe='today 5-y', geo='', gprop='')
    data = pytrends.interest_over_time()
    if data.empty:
        print(f"No data found for the domain: {domain_name}")
        return
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])
    data = data.fillna(False)
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data[domain_name], label=domain_name, color='blue')
    plt.title(f'Growth of {domain_name} over the Past 5 Years')
    plt.xlabel('Year')
    plt.ylabel('Interest')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()



domain = 'web development'  # Replace with your desired domain name
visualize_domain_growth(domain)