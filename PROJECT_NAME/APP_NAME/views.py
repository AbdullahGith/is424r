from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Define the tax rate
tax_rate = 0.15

def default_view(request):
    return HttpResponse("This is a site to calculate tax.")

def calculate_tax(request, number):
    try:
        number = float(number)
        total_price = number + (number * tax_rate)
        return HttpResponse(f"Total Price after 15% tax: ${total_price:.2f}")
    except ValueError:
        return HttpResponse("Invalid input. Please provide a valid number.")


def tax_rate_view(request):
    return render(request, 'tax_calculator/tax_rate.html', {'tax_rate': tax_rate})

