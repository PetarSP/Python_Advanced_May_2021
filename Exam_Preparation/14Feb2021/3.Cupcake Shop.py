def stock_availability(inventory: list, command: str, *args):
    if command == "delivery":
        return inventory + list(args)
    elif command == "sell":
        if not args:
            return inventory[1:]
        elif isinstance(args[0], int):
            return inventory[args[0]:]
        else:
            for x in args:
                while x in inventory:
                    inventory.remove(x)
            return inventory

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
