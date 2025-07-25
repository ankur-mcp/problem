def indian_currency_format(number):
    integer, _, decimal = str(number).partition('.')
    if len(integer) <= 3:
        formatted = integer
    else:
        last_three = integer[-3:]
        rest = integer[:-3]
        formatted = ','.join([rest[max(i-2, 0):i] for i in range(len(rest), 0, -2)][::-1]) + ',' + last_three
    return formatted + ('.' + decimal if decimal else '')

# Example usage
print(indian_currency_format(123456.7891))  # Output: 1,23,456.7891
