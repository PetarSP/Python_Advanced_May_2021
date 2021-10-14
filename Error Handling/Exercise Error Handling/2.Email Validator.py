class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = {"com", "bg", "org", "net"}

while True:
    line = input()
    if line == "End":
        break

    email_parts = line.split("@")

    if len(email_parts) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = domain_name.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
