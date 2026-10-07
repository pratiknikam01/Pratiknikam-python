def inventory_manager(catalog, item_to_search):
    # Case-insensitive search optimization
    normalized_catalog = [item.lower() for item in catalog]
    search_target = item_to_search.lower()
    
    if search_target in normalized_catalog:
        index_location = normalized_catalog.index(search_target)
        print(f"Item '{item_to_search}' found at index location: {index_location}")
        return index_location
    else:
        print(f"Item '{item_to_search}' was not found in the inventory.")
        return None

# Example Usage:
inventory = ["Laptop", "Monitor", "Keyboard", "Mouse", "Desk Lamp"]

# Test search
target = "Keyboard"
inventory_manager(inventory, target)