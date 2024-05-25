def cash(change: int) -> int:
    if change < 0:
        raise ValueError("Change cannot be negative")
    result = 0
    quarterValue = 25
    dimeValue = 10
    nickelValue = 5
    penneValue = 1
    while change - quarterValue >= 0:
        change -= quarterValue
        result += 1
    while change - dimeValue >= 0:
        change -= dimeValue
        result += 1
    while change - nickelValue >= 0:
        change -= nickelValue
        result += 1
    while change - penneValue >= 0:
        change -= penneValue
        result += 1
    return result