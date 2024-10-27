from flask import render_template, request, redirect, url_for, flash
from app import app

from .utils import calculate_total_sales, calculate_daily_average, sales_projection

daily_sales = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sale_amount = request.form.get('sale')
        if sale_amount:
            daily_sales.append(float(sale_amount))
            flash(f"Sale recorded: ${sale_amount}")
    return render_template('index.html', sales=daily_sales)

@app.route('/report')
def report():
    total_sales = calculate_total_sales(daily_sales)
    daily_average = calculate_daily_average(daily_sales)
    return render_template('report.html', total=total_sales, average=daily_average, sales=daily_sales)

@app.route('/projection', methods=['GET', 'POST'])
def projection():
    if request.method == 'POST':
        days = int(request.form.get('days'))
        projected_sales = sales_projection(daily_sales, days)
        return render_template('projection.html', projection=projected_sales)
    return render_template('projection.html')
