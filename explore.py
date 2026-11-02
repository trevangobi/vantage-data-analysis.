import main

# Access the datasets
assets = main.assets
asset_price = main.asset_price
headline = main.headline
headline_tag = main.headline_tag
historical_sentiment = main.historical_sentiment
sparkline_point = main.sparkline_point


#Form datasets
datasets = {
    "assets" : assets,
    "asset price" : asset_price,
    "headline" : headline,
    "headline tag" : headline_tag,
    "historical Sentiment" : historical_sentiment,
    "sparkline point" : sparkline_point,
}
for name, df in datasets.items():
    print("__"*50)
    print(name.title())
    print("Number of Rows: ", len(df))
    print("number of Columns: ", len(df.columns))
    print("\nColumn Names:")
    print(df.columns.tolist())
    print("\nFirst Five records:")
    print(df.head())
    print("__"*50)
    print(df.info())
    print(df.shape)
    print(df.describe())
    print("**"*50)
    