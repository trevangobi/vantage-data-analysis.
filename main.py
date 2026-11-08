import pandas as pd

assets = pd.read_csv("data/_Asset__202610301406.csv")
asset_price = pd.read_csv("data/_AssetPrice__202610301406.csv")
headline = pd.read_csv("data/_Headline__202610301406.csv")
headline_tag = pd.read_csv("data/_HeadlineTag__202610301406.csv")
historical_sentiment = pd.read_csv("data/_HistoricalSentiment__202610301406.csv")
sparkline_point = pd.read_csv("data/_SparklinePoint__202610301406.csv")
