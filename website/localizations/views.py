from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
                "url": "localizations_rooms_page",
                "kwargs": str(address.id),
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


def localizations_rooms_view(request, localization_id):
    localization = Address.objects.filter(id=localization_id).first()

    blocks = []
    block = {"title": localization.name, "elements": []}

    rooms = Room.objects.filter(address=localization)
    for room in rooms:
        block["elements"].append({
            "icon": "fa-solid fa-door-open",
            "name": room.name,
            "class": "element",
            "url": "main_panel_page",
            "groups": ["admin"],
            "active": True,
        })
    blocks.append(block)

    context = {
        'blocks': blocks,
        'page_title': localization.name,
        "sidebar_items": request.sidebar_items,
    }

    return render(request, 'main_template.html', context)


@csrf_exempt
def localization_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            localization_name = data["name"]
            localization = Address.objects.filter(name=localization_name).first()
            if localization is None:
                new_localization = Address.objects.create(
                    name=data["name"],
                    city=data["city"],
                    house_number=data["houseNumber"],
                    apartment_number=data["apartmentNumber"],
                    zip_code=data["zipCode"],
                    zip_code_city=data["zipCodeCity"],
                    voivodeship=data["voivodeship"],
                    country=data["country"],
                )
                new_localization.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Lokalizacja o tej nazwie już istnieje'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Dozwolone są tylko żądania typu POST'})
