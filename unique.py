import main
# Access the datasets
assets = main.assets
prices = main.asset_price
headline = main.headline
headline_tag = main.headline_tag
sentiment = main.historical_sentiment
sparkline = main.sparkline_point


# Count unique assets in each table
print("ASSETS:", assets["id"].nunique())

print("ASSET PRICE:", prices["assetId"].nunique())

print("SPARKLINE POINTS:", sparkline["assetId"].nunique())

print("HISTORICAL SENTIMENT:", sentiment["assetId"].nunique())

print("HEADLINE TAGS:", headline_tag["assetId"].nunique())

# Get the unique asset IDs in SparklinePoint
price_asset_ids = sparkline["assetId"].unique()

# Match them to the Assets table
price_assets = assets[
    assets["id"].isin(price_asset_ids)
][["id", "name", "symbol", "market_cap_rank"]]
print(price_assets)