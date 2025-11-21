from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from core.forms import ExpenseForm
from core.models import Expense, Category, Tag

from django.contrib.auth.decorators import login_required

from .utils.pdf_utils import generate_pdf_response, default_style
from reportlab.platypus import Paragraph

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

def list_categories(request):
    categories = Category.objects.all().order_by('name')
    context = {'categories': categories}
    return render(request, 'core/list_categories.html', context)

def list_tags(request):
    tags = Tag.objects.all().order_by('name')
    context = {'tags': tags}
    return render(request, 'core/list_tags.html', context)

def download_expenses_pdf(request):
    expenses = Expense.objects.all().order_by('-created_at')

    data = []

    for i, expense in enumerate(expenses, start=1):
        tags_paragraph = Paragraph(
            "<br/>".join([f"- {tag.name}" for tag in expense.tags.all()]) if expense.tags.exists() else "-",
            default_style
        )
        data.append([
            i,
            expense.name,
            str(expense.amount),
            expense.category.name if expense.category else "-",
            tags_paragraph,
            expense.created_at.strftime("%Y-%m-%d %H:%M"),
        ])

    headers = ["S.No", "Expense Name", "Amount", "Category", "Tags", "Created At"]
    col_widths = [30, 90, 55, 110, 180, 85]

    return generate_pdf_response("expenses.pdf", headers, data, col_widths)

def download_categories_pdf(request):
    categories = Category.objects.all().order_by('name')

    data = []
    for i, category in enumerate(categories, start=1):
        data.append([
            i,
            Paragraph(category.name, default_style),
            category.created_at.strftime("%Y-%m-%d %H:%M"),
            category.updated_at.strftime("%Y-%m-%d %H:%M"),
        ])

    headers = ["S.No", "Category Name", "Created At", "Updated At"]
    col_widths = [40, 200, 120, 120]

    return generate_pdf_response("categories.pdf", headers, data, col_widths)

def download_tags_pdf(request):
    tags = Tag.objects.all().order_by('name')

    data = []
    for i, tag in enumerate(tags, start=1):
        # Wrap tag name in Paragraph for safety if very long
        tag_paragraph = Paragraph(tag.name, default_style)
        data.append([
            i,
            tag_paragraph,
            tag.created_at.strftime("%Y-%m-%d %H:%M"),
            tag.updated_at.strftime("%Y-%m-%d %H:%M"),
        ])

    headers = ["S.No", "Tag Name", "Created At", "Updated At"]
    col_widths = [40, 200, 120, 120]

    return generate_pdf_response("tags.pdf", headers, data, col_widths)