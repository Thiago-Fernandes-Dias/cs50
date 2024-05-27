def credit(number_string: str) -> str:
    sum = i = 0
    number = parse_credit_number(number_string)
    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        if i % 2 == 0:
            sum += digit
        else:
            double_digit = digit * 2
            sum += double_digit % 10 + double_digit // 10   
        number_copy -= digit
        number_copy //= 10
        i += 1
    if sum % 10 != 0: 
        return "INVALID"
    valid_length = False
    for j in [15, 16, 13]:
        valid_length = valid_length or number // 10 ** j != 0
    if not valid_length:
        return "INVALID"
    card_provider_number = number // 10 ** (i - 2)
    if card_provider_number // 10 == 4:
        return "VISA"
    elif card_provider_number in [34, 37]:
        return "AMEX"
    elif card_provider_number in [51, 52, 53, 54, 55]:
        return "MASTERCARD"
    return "OTHER"

def parse_credit_number(number_string: str) -> int:
    if not number_string.isnumeric():
        raise ValueError("The number string must contain only the digits!")
    number_parsed = int(number_string)
    return number_parsed


