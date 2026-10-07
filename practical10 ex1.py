def price_engine(asset_costs):
    # Sort prices from highest to lowest
    sorted_costs = sorted(asset_costs, reverse=True)
    
    # Extract the top 3 highest prices
    top_three = sorted_costs[:3]
    
    print(f"Sorted Costs (Highest to Lowest): {sorted_costs}")
    print(f"Top 3 Priciest Entries: {top_three}")
    return sorted_costs, top_three

# Example Usage:
prices = [1299.99, 45.50, 850.00, 2300.75, 499.99, 150.25]
price_engine(prices)