def flights(*args):
    result = {}
    for key in range(0, len(args), 2):
        if args[key] == "Finish":
            return result

        for value in range(key + 1, len(args)):
            if not args[key] in result:
                result[args[key]] = int(args[value])
                break
            else:
                if args[key] in result:
                    result[args[key]] += int(args[value])
                    break

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
