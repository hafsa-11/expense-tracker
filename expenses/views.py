from django.shortcuts import render, redirect
from .models import Expense
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense

def index(request):
    if request.method == 'POST':
        Expense.objects.create(
            name=request.POST['name'],
            amount=request.POST['amount'],
            category=request.POST['category'],
            date=request.POST['date']
        )
        return redirect('index')

    expenses = Expense.objects.all()
    total = sum(exp.amount for exp in expenses)

    return render(request, 'expenses/index.html', {
        'expenses': expenses,
        'total': total
    })


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('index')
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == 'POST':
        expense.name = request.POST['name']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.save()
        return redirect('index')

    return render(request, 'expenses/edit.html', {'expense': expense})
