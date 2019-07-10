# StockQcrawler
python code for crawling stock market index data from StockQ
# Usage
因為資料是表格，比起beautifulsoup更適合用pandas
利用pandas從StockQ.org讀取特定國家的股市指數漲跌幅比例，存成dictionary做排序再以numpy.array輸出
（只抓2016&2017年的中國 新加玻 香港 日本 澳洲 紐西蘭 加拿大 瑞士 英國 土耳其 挪威 波蘭 俄國資料）
