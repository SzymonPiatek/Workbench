from django.shortcuts import render
from .models import Item


def items_view(request):
    items = Item.objects.all()

    context = {
        "items": items,
        "page_title": "Przedmioty",
        "sidebar_items": request.sidebar_items,
    }

    return render(request, 'pages/items/main.html', context)
