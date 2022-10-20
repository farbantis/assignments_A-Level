def max_denomination_withdrawal(required_amount, notes_available):
    """teller machine intended to give as few notes as possible"""
    result = {}
    for banknote in notes_available:
        if required_amount / banknote >= 1:
            number = required_amount // banknote
            print(f'{banknote} note * {number} pcs')
            result[banknote] = number
            required_amount -= number * banknote
    return result


notes = [1000, 500, 100, 50, 20, 10, 5, 1]
amount = int(input("how much do you want to withdraw? "))
print(max_denomination_withdrawal(amount, notes))


