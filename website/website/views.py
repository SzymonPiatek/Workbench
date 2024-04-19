from django.shortcuts import render


def statistics(request):
    context = {
        "page_title": "Statystyki"
    }

    return render(request, 'pages/statistics.html', context)


def main_panel(request):
    user_groups = request.user.groups.values_list('name', flat=True)

    blocks = [
        {
            "title": "Panel administratora",
            "elements": [
                {"icon": "fa-chart-pie", "name": "Statystyki",
                 "url": "statistics_page", "groups": ["admin"]},
                {"icon": "fa-bell", "name": "Powiadomienia",
                 "url": "notifications_page", "groups": ["admin"]},
                {"icon": "fa-plus", "name": "Dodaj powiadomienie",
                 "on_click": "toggleOverlay(this, 'addNotification')",
                 "groups": ["admin"]},
            ]
        },
        {
            "title": "Rezerwacje",
            "elements": [
                {"icon": "fa-car", "name": "Parking",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-display", "name": "Biurko",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-people-roof", "name": "Sala",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-plus", "name": "Dodaj rezerwację",
                 "url": "main_panel_page", "groups": ["worker"]}
            ]
        },
        {
            "title": "Przedmioty",
            "elements": [
                {"icon": "fa-list", "name": "Lista przedmiotów",
                 "url": "main_panel_page", "groups": ["building_admin"]},
                {"icon": "fa-magnifying-glass", "name": "Inwentaryzacja",
                 "url": "main_panel_page", "groups": ["building_admin"]},
                {"icon": "fa-plus", "name": "Dodaj pozycję",
                 "url": "main_panel_page", "groups": ["building_admin"]}
            ]
        },
        {
            "title": "Pracownicy",
            "elements": [
                {"icon": "fa-user", "name": "Lista pracowników",
                 "url": "main_panel_page", "groups": ["supervisor"]},
                {"icon": "fa-users", "name": "Lista grup",
                 "url": "main_panel_page", "groups": ["supervisor"]},
                {"icon": "fa-user-plus", "name": "Dodaj pracownika",
                 "url": "main_panel_page", "groups": ["supervisor"]},
                {"icon": "fa-plus", "name": "Dodaj grupę",
                 "url": "main_panel_page", "groups": ["supervisor"]}
            ]
        },
        {
            "title": "Lokalizacje",
            "elements": [
                {"icon": "fa-building", "name": "Podgląd budynku",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-door-closed", "name": "Podgląd pomieszczeń",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-plus", "name": "Dodaj pomieszczenie",
                 "url": "main_panel_page", "groups": ["worker"]}
            ]
        },
        {
            "title": "Kalendarz",
            "elements": [
                {"icon": "fa-calendar-check", "name": "Najbliższe wydarzenia",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-plus", "name": "Dodaj wydarzenie",
                 "url": "main_panel_page", "groups": ["worker"]}
            ]
        },
        {
            "title": "Helpdesk",
            "elements": [
                {"icon": "fa-life-ring", "name": "Zgłoś problem",
                 "url": "main_panel_page", "groups": ["worker"]},
                {"icon": "fa-eye", "name": "Zobacz zgłoszenia",
                 "url": "main_panel_page", "groups": ["helpdesk"]},
                {"icon": "fa-question-circle", "name": "FAQ",
                 "url": "main_panel_page", "groups": ["worker"]}
            ]
        }
    ]

    filtered_blocks = []
    for block in blocks:
        for element in block.get('elements', []):
            if any(group in user_groups for group in element.get('groups', [])):
                filtered_blocks.append(block)
                break

    context = {
        "page_title": "Strona główna",
        "blocks": filtered_blocks,
    }

    return render(request, "pages/main_panel.html", context)
