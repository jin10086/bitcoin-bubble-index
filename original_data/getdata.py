import requests
import re

s = requests.Session()
s.headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}


def getdata(url, fname):
    print("geturl:", url)
    z1 = s.get(url)
    raw_data = re.findall(r'container"\),(.*?), {', z1.text, re.DOTALL)
    data = raw_data[0][1:][:-1:]
    with open(fname, "w") as f:
        f.write(data)


def run():
    runlist = [
        {
            "url": "https://bitinfocharts.com/comparison/bitcoin-transactions.html",
            "fname": "transaction.txt",
        },
        {
            "url": "https://bitinfocharts.com/comparison/bitcoin-price.html",
            "fname": "price.txt",
        },
        {
            "url": "https://bitinfocharts.com/comparison/sentbyaddress-btc.html",
            "fname": "sentaddr.txt",
        },
        {
            "url": "https://bitinfocharts.com/comparison/tweets-btc.html",
            "fname": "tweets.txt",
        },
        {
            "url": "https://bitinfocharts.com/comparison/google_trends-btc.html",
            "fname": "gtrend.txt",
        },
        {
            "url": "https://bitinfocharts.com/comparison/bitcoin-difficulty.html",
            "fname": "difficulty.txt",
        },
    ]
    for i in runlist:

        getdata(i["url"], i["fname"])


if __name__ == "__main__":
    run()
