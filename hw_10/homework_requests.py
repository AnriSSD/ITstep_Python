import requests

# Ыутв ф куйгуые
response = requests.get("https://fakestoreapi.com/products")

# Checking the response status
if response.status_code == 200:
    # Convert the response to JSON
    products = response.json()

    # a) Сreate a list of product prices and display the maximum, minimum and average prices
    prices = [product["price"] for product in products]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    print("Max price:", max_price)
    print("Min price:", min_price)
    print("Average price:", avg_price)

    # b) Create a list of categories (without duplicates) and sort it
    categories = sorted(list(set(product["category"] for product in products)))
    print("Categories:", categories)

    # c) Create a list that will contain a product description (name) and id. Results are sorted by name
    products_desc = [
        {"title": product["title"], "id": product["id"]} for product in products
    ]
    products_desc_sorted = sorted(products_desc, key=lambda x: x["title"])
    print("Sorted products by title:", products_desc_sorted)

    # d) Return a list of ratings, sorted by rate in ascending order
    ratings = sorted([product["rating"]["rate"] for product in products])
    print("Sorted ratings:", ratings)

else:
    print("Failed to fetch data:", response.status_code)
