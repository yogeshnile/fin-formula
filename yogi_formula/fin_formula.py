def get_valuation(latest_profit, expected_annual_growth_rate):
    value = round(latest_profit * (8.5 + (2 * (expected_annual_growth_rate))), 2)
    return value