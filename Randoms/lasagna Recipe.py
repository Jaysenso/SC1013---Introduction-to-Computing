def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
    pass


def get_change(budget, exchanging_value):
    return budget - exchanging_value
    pass


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    pass


def get_number_of_bills(budget, denomination):

    return float(budget) // denomination
    pass


def get_leftover_of_bills(budget, denomination):
    return float(budget) % denomination
    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):

    return int( ((float(budget) * exchange_rate) + (float(budget) * 10/100)) // 20 )
    pass
