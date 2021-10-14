def get_info(name, age, town) -> str:
    return f"This is {name} from {town} and he is {age} years old"


print(
    get_info(**{"name": "George", "town": "Sofia", "age": 20})
)
