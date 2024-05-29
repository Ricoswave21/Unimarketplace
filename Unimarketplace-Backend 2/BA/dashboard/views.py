from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Uppdaterad import

from items.models import Items

@login_required
def index(request):
    items = Items.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })
