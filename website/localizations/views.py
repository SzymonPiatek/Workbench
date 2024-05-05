from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Room, Address
from items.models import Item


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


def addresses(request):
    addresses = Address.objects.all()
    addresses_list = [
        {'name': address.name,
         'id': address.id} for address in addresses]
    return JsonResponse(addresses_list, safe=False)


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
            "url": "room_page",
            "kwargs": str(room.id),
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


def room_view(request, room_id):
    room = Room.objects.get(id=room_id)
    items = Item.objects.filter(room=room).order_by('item_type')

    item_type_icons = {
        "biurko": "fa-solid fa-desktop",
        "pc": "fa-solid fa-desktop",
        "komputer": "fa-solid fa-desktop",
        "laptop": "fa-solid fa-desktop",
        "tablet": "fa-solid fa-desktop",
        "monitor": "fa-solid fa-desktop",
        "telewizor": "fa-solid fa-desktop",
        "szafa": "fa-solid fa-box-archive",
        "regał": "fa-solid fa-box-archive",
        "komoda": "fa-solid fa-box-archive",
        "krzesło": "fa-solid fa-chair",
        "fotel": "fa-solid fa-chair",
        "lampa": "fa-solid fa-lightbulb",
        "lampka": "fa-solid fa-lightbulb",
        "telefon": "fa-solid fa-phone"
    }

    blocks = []
    block = {"title": "Przedmioty", "elements": []}
    if items:
        for item in items:
            item_type = item.item_type.name.lower()
            icon = "fa-solid fa-question"
            for word, icon_class in item_type_icons.items():
                if word in item_type:
                    icon = icon_class
                    break

            block["elements"].append({
                "icon": icon,
                "name": item.name,
                "class": "element",
                "url": "main_panel_page",
                "groups": ["admin"],
                "active": True,
            })
    blocks.append(block)

    context = {
        'blocks': blocks,
        'page_title': room.name,
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


@csrf_exempt
def room_save_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            room_name = data["name"]
            address_id = data["address"]
            localization = Address.objects.filter(id=address_id).first()
            if localization is None:
                return JsonResponse({'success': False, 'error': 'Nie znaleziono lokalizacji o podanej nazwie'})
            else:
                room = Room.objects.filter(name=room_name, address=localization).first()
                if room is None:
                    new_room = Room(
                        name=data["name"],
                        room_type=data["room_type"],
                        floor=data["floor"],
                        address=localization,
                    )
                    new_room.save()
                    return JsonResponse({'success': True})
                else:
                    return JsonResponse({'success': False, 'error': 'Pomieszczenie o tej nazwie już istnieje'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Dozwolone są tylko żądania typu POST'})
