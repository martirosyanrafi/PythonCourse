market = {
    "dairy": ["yogurt", "cheese"],
    "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]
}

print("before changes:", market)

market["candies"] = ["mars", "kinder", "twix"]

market["fruits"] = sorted(set(market["fruits"]))

print("after changes:", market)
