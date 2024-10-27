def calculate_total_sales(sales):
    return sum(sales)

def calculate_daily_average(sales):
    return sum(sales) / len(sales) if sales else 0

def sales_projection(sales, days):
    daily_average = calculate_daily_average(sales)
    return daily_average * days
