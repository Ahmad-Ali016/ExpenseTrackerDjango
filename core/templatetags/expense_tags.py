from decimal import Decimal
from django import template
from django.db.models import Sum
from core.models import Expense

register = template.Library()

@register.simple_tag(takes_context=True)
def total_expense(context, user=None, fmt=False):
    """
    Returns the total amount of expenses for the current user.
    Usage in template:
      - total_expense as total %}            -> total for request.user
      - total_expense request.user as total %} -> total for given user
      - total_expense as total fmt=True %}   -> formatted string (2 decimal places)

    - takes_context=True so it can access request and request.user
    - If user argument is passed it will use that user instead of request.user
    """
    request = context.get('request')
    if user is None:
        if not request or not hasattr(request, 'user') or not request.user.is_authenticated:
            return Decimal('0.00') if not fmt else "0.00"
        user = request.user

    total = Expense.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    return f"{total:.2f}" if fmt else total

    #
    # if fmt:
    #     # Ensure it's a Decimal and format to 2 dp
    #     return f"{total:.2f}"
    # return total
