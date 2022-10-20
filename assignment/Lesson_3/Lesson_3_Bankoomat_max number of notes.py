def max_notes(amount:int, notes:list, max_pcs_each:int=10):
    """bank teller gives max amount of bills based max allowed bill quantity"""
    quantity_notes = [max_pcs_each] * len(notes)
    suma = 0
    for i in notes:
        suma += i * max_pcs_each
        if suma >= amount:
            max_note = i
            break
    needed_index = notes.index(max_note)+1
    notes_new = notes[ : needed_index]
    quantity_notes = quantity_notes[ : needed_index]
    max_amount = sum(list(map(lambda x: x * max_pcs_each, notes_new)))
    amount_to_decrease = max_amount - amount
    notes_new.reverse()
    # amount to decrease must be given out in the smallest bill quantity
    for i in notes_new:
        if amount_to_decrease / i >= 1:
            quantity = amount_to_decrease // i
            amount_to_decrease -= quantity * i
            quantity_notes[notes.index(i)] -= quantity
    result = list(zip(notes, quantity_notes))
    print(result)
    print("you're loaded, get your wallet ready...")
    for i in result:
        print(f'{i[0]} $ bill - {i[1]} pcs')
    print(f'total: {sum([x * y for x, y in result])} $')
    print(f'total: {sum([x[1] for x in result])} bills')
    return result


notes = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
max_notes(18860, notes)
