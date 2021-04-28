class NameTooShortError(Exception):
    """ It will be raised when the input username is 4 symbols or less"""
    pass


class MustContainAtSymbolError(Exception):
    """ It will be raised when the @ symbol is missing in the input email"""
    pass


class InvalidDomainError(Exception):
    """It will be raised when the input email has invalid domain """
    pass


def valid_name(text):
    username = text.split("@")[0]
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def has_it_at_symbol(text):
    if "@" not in text:
        raise MustContainAtSymbolError("Email must contain @")


def valid_domain(text, possible_domains):
    domain = text.split(".")[-1]
    if domain not in possible_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


line = input()
possible_domains = ("com", "net", "bg", "org")
while line != "End":
    valid_name(line)
    has_it_at_symbol(line)
    valid_domain(line, possible_domains)

    print("Email is valid")
    line = input()
