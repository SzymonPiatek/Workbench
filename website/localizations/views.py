from django.shortcuts import render
from .models import Room, Address


def localizations_view(request):
    cities = Address.objects.values_list('city', flat=True).distinct()

    blocks = []
    for city in cities:
        block = {"title": city, "elements": []}
        addresses = Address.objects.filter(city=city)
        for address in addresses:
            block["elements"].append({
                "icon": "fa-solid fa-city",
                "name": address.name,
                "class": "element",
                "url": "main_panel_page",
                "groups": ["admin"],
                "active": True,
            })
        blocks.append(block)

    context = {
        'blocks': blocks,
        'page_title': 'Lokalizacje',
        "sidebar_items": request.sidebar_items,
    }

    return render(request, 'main_template.html', context)

