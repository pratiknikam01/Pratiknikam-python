text = input("Enter the text block: ")

symbols = ['@', '.', '!']

for symbol in symbols:
    count = text.count(symbol)
    print(f"'{symbol}' occurs {count} time(s)")
