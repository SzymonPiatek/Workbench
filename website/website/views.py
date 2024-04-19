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
            "title": "Zarządzanie",
            "elements": [
                {"icon": "fa-user-tie", "name": "Panel administratora",
                 "url": "admin:login", "groups": ["admin"], "active": True},
                {"icon": "fa-chart-pie", "name": "Statystyki",
                 "url": "statistics_page", "groups": ["admin"], "active": False},
                {"icon": "fa-bell", "name": "Powiadomienia",
                 "url": "notifications_page", "groups": ["admin"], "active": True},
                {"icon": "fa-plus", "name": "Dodaj powiadomienie",
                 "on_click": "toggleOverlay(this, 'addNotification')",
                 "groups": ["admin"], "active": True},
            ]
        },
        {
            "title": "Rezerwacje",
            "elements": [
                {"icon": "fa-car", "name": "Parking",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-display", "name": "Biurko",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-people-roof", "name": "Sala",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-plus", "name": "Dodaj rezerwację",
                 "url": "main_panel_page", "groups": ["worker"], "active": False}
            ]
        },
        {
            "title": "Przedmioty",
            "elements": [
                {"icon": "fa-list", "name": "Lista przedmiotów",
                 "url": "main_panel_page", "groups": ["building_admin"], "active": False},
                {"icon": "fa-magnifying-glass", "name": "Inwentaryzacja",
                 "url": "main_panel_page", "groups": ["building_admin"], "active": False},
                {"icon": "fa-plus", "name": "Dodaj pozycję",
                 "url": "main_panel_page", "groups": ["building_admin"], "active": False}
            ]
        },
        {
            "title": "Pracownicy",
            "elements": [
                {"icon": "fa-user", "name": "Lista pracowników",
                 "url": "main_panel_page", "groups": ["supervisor"], "active": False},
                {"icon": "fa-users", "name": "Lista grup",
                 "url": "main_panel_page", "groups": ["supervisor"], "active": False},
                {"icon": "fa-user-plus", "name": "Dodaj pracownika",
                 "url": "main_panel_page", "groups": ["supervisor"], "active": False},
                {"icon": "fa-plus", "name": "Dodaj grupę",
                 "url": "main_panel_page", "groups": ["supervisor"], "active": False}
            ]
        },
        {
            "title": "Lokalizacje",
            "elements": [
                {"icon": "fa-building", "name": "Podgląd budynku",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-door-closed", "name": "Podgląd pomieszczeń",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-plus", "name": "Dodaj pomieszczenie",
                 "url": "main_panel_page", "groups": ["admin", "building_admin"], "active": False}
            ]
        },
        {
            "title": "Kalendarz",
            "elements": [
                {"icon": "fa-calendar-check", "name": "Najbliższe wydarzenia",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-plus", "name": "Dodaj wydarzenie",
                 "url": "main_panel_page", "groups": ["worker"], "active": False}
            ]
        },
        {
            "title": "Helpdesk",
            "elements": [
                {"icon": "fa-life-ring", "name": "Zgłoś problem",
                 "url": "main_panel_page", "groups": ["worker"], "active": False},
                {"icon": "fa-eye", "name": "Zobacz zgłoszenia",
                 "url": "main_panel_page", "groups": ["helpdesk", "admin"], "active": False},
                {"icon": "fa-question-circle", "name": "FAQ",
                 "url": "main_panel_page", "groups": ["worker"], "active": False}
            ]
        }
    ]

    filtered_blocks = []
    for block in blocks:
        visible_elements = []
        for element in block.get('elements', []):
            if element["active"]:
                if any(group in user_groups for group in element.get('groups', [])):
                    visible_elements.append(element)
        if visible_elements:
            filtered_blocks.append({"title": block["title"], "elements": visible_elements})

    context = {
        "page_title": "Strona główna",
        "blocks": filtered_blocks,
    }

    return render(request, "pages/main_panel.html", context)
