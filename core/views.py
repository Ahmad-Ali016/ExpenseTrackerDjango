from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from core.forms import ExpenseForm
from core.models import Expense, Category

from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    return HttpResponse("Expense Tracker Django — Home Page")

def list_expenses_view(request):
    if request.GET.get('category'):
        category = Category.objects.get(name=request.GET.get('category'))
        expenses = Expense.objects.filter(category=category).order_by('-created_at')
    else:
        expenses = Expense.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'expenses': expenses,
        'categories': categories
    }
    return render(request, 'core/list_expenses.html', context)

@login_required
def add_expense_view(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')  # go back to expenses list after adding
    else:
        form = ExpenseForm()

    return render(request, 'core/add_expense.html', {'form': form})

@login_required
def edit_expense(request, expense_id):
    # hotel = Hotel.objects.get(pk=hotel_id)
    expense = get_object_or_404(Expense, pk=expense_id)
    print(f'Expense: {expense} ')
    form_errors = None
    if request.method == 'POST':
        print(f'Hotel: {expense}')
        form = ExpenseForm(request.POST, instance=expense)
        print(f'form {form}')
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('list_expenses')
        else:
            print(f"Error in form, {form.errors}")
        # If invalid, fall through to render the same form with errors
    else:
        form = ExpenseForm(instance=expense)
    context = {'form': form}
    return render(request, 'core/edit_hotel.html', context)

@login_required
def delete_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    # print(f'expense deleted: {expense} ')
    expense.delete()
    return redirect('list_expenses')
