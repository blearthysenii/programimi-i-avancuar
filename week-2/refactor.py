def filter_items(items, t):
    return [item for item in items if item["t"] == t]

items = [ {"id": 1, "t": "book", "price": 20}, {"id": 2, "t": "food", "price": 10}, {"id": 3, "t": "book", "price": 15}, {"id": 4, "t": "food", "price": 5} ] 
books = filter_items(items, "book")
foods = filter_items(items, "food")


for book in books:
    print(f"Book: {book}")

for food in foods:
    print(f"Food: {food}")


