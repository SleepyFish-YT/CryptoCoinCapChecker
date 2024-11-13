# i hate python

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager as Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

crypto_ids = [
    'bitcoin', 'ethereum', 'tether', 'ripple', 'cardano', 'dogecoin', 'binancecoin', 'solana', 'polkadot', 'litecoin',
    'chainlink', 'uniswap', 'usd-coin', 'avalanche-2', 'binance-usd', 'shiba-inu', 'terra-luna', 'near-protocol', 'algorand',
    'cosmos', 'vechain', 'filecoin', 'litecoin', 'hedera', 'fantom', 'aave', 'maker', 'sushiswap', 'decentraland',
    'the-graph', 'the-sand-box', 'compound-2', 'axie-infinity', 'tezos', 'yearn-finance', 'curve-dao-token', 'elrond',
    'theta', 'fantom', 'thorchain', 'chiliz', 'renrenbit', 'polkadot', 'kava', 'moonbeam', 'helium', 'bitcoin-cash',
    'flow', 'polygon', 'enjincoin', 'ethereum-classic', 'ravencoin', 'decentraland', 'maker', 'polygon', 'tether',
    'harmony', 'xmr', 'bnb', 'shiba', 'kraken', 'doge', 'uniswap', 'governance-token', 'truffle', 'gala', 'injective',
    'hollywood-downtown', 'glimmer', 'internet-computer', 'optimism', 'opensea', 'aave', 'terra-luna', 'dogecoin',
    'filecoin', 'pegasus-finance', 'solana', 'helio-network'
]

def get_crypto_price(driver, crypto_id, timeout):
    url = f'https://www.coinmarketcap.com/currencies/{crypto_id}/'
    driver.get(url)

    try:
        price = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.sc-65e7f566-0.WXGwg.base-text"))
        ).text

        percentage = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.change-text"))
        ).text.replace("(1d)", "").strip()

        return f"{price} ({percentage})"
    except Exception:
        print(f"|  Failed getting the price for: {crypto_id}")
        return None
    pass
pass

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-extensions')

    edgeService = Service(Edge().install())
    driver = webdriver.Edge(service=edgeService, options=options)

    driverName = driver.name.lower()
    print("|  Driver created: ", driverName)

    for crypto in crypto_ids:
        price = get_crypto_price(driver=driver, crypto_id=crypto, timeout=30)
        print(f"|  {crypto}: {price}")
        pass
    pass

    driver.quit()
    print("|  Driver closed: ", driverName)
pass

print("")
print("/ Main started")
main()
print("\\ Main ended")

exit(69)
pass
