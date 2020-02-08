# Bitcoin Bubble Index

## 我做的一些修改

1. 使用爬虫直接获取需要的数据... 见 `original_data/getdata.py`
2. 使用github actions每天5点更新数据 见 `.github/workflows/pythonapp.yml`
3. 使用了github page,所以每天5点以后 会自动更新数据到 https://igaojin.me/bitcoin-bubble-index/  这个页面

### What's this?

This project provides a visualization analysis tool for price bubble of Bitcoin, including basic price information, 60-days accumulative increase, hot keywords index, and bubble index. We accumulated the original data (`2010/07/17` - `2019/12/06`) and put them into `/original_data` folder, and we visualize our analysis result using [echarts][1].

### Datasets

We provide the following dataset:

 - *price.txt:* The bitcoin price in USD per day. 
 - *sentaddr.txt:* Number of unique active addresses per day. 
 - *transaction.txt:* Number of transactions in BTC blockchain per day. 
 - *difficulty.txt:* Average mining difficulty per day. 
 - *gtrend.txt:* Google Trends to "Bitcoin".
 - *tweets.txt:* Tweets per day #Bitcoin.

You can get the lastest data from [bitinfocharts.com][2]

### How to use

Open `index.html` in your browser directly and you will see the following page:

<img src="https://github.com/aksnzhy/bitcoin-bubble-index/blob/master/index.png" width = "800"/>

In `original_data` folder, you can run the command:

```
python process_data.py
```

to get the analysis result, which will be stored in `data.json`.


  [1]: https://github.com/apache/incubator-echarts
  [2]: https://bitinfocharts.com/comparison/bitcoin-transactions.html