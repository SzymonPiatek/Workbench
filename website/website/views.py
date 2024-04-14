from django.shortcuts import render


def statistics(request):
    context = {
        "page_title": "Statystyki"
    }

    return render(request, 'pages/statistics.html', context)


def main_panel(request):
    blocks = [
        {
            "title": "Panel administratora",
            "elements": [
                {"icon": "fa-chart-pie", "name": "Statystyki", "url": "statistics_page"},
                {"icon": "fa-bell", "name": "Powiadomienia", "url": "notifications_page"},
                {"icon": "fa-plus", "name": "Dodaj powiadomienie", "on_click": "toggleOverlay(this, 'addNotification')"},
            ]
        },
        {
            "title": "Rezerwacje",
            "elements": [
                {"icon": "fa-car", "name": "Parking", "url": "main_panel_page"},
                {"icon": "fa-display", "name": "Biurko", "url": "main_panel_page"},
                {"icon": "fa-people-roof", "name": "Sala", "url": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj rezerwację", "url": "main_panel_page"}
            ]
        },
        {
            "title": "Przedmioty",
            "elements": [
                {"icon": "fa-list", "name": "Lista przedmiotów", "url": "main_panel_page"},
                {"icon": "fa-magnifying-glass", "name": "Inwentaryzacja", "url": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj pozycję", "url": "main_panel_page"}
            ]
        },
        {
            "title": "Pracownicy",
            "elements": [
                {"icon": "fa-user", "name": "Lista pracowników", "url": "main_panel_page"},
                {"icon": "fa-users", "name": "Lista grup", "url": "main_panel_page"},
                {"icon": "fa-user-plus", "name": "Dodaj pracownika", "url": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj grupę", "url": "main_panel_page"}
            ]
        },
        {
            "title": "Lokalizacje",
            "elements": [
                {"icon": "fa-building", "name": "Podgląd budynku", "url": "main_panel_page"},
                {"icon": "fa-door-closed", "name": "Podgląd pomieszczeń", "url": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj pomieszczenie", "url": "main_panel_page"}
            ]
        },
        {
            "title": "Kalendarz",
            "elements": [
                {"icon": "fa-calendar-check", "name": "Najbliższe wydarzenia", "url": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj wydarzenie", "url": "main_panel_page"}
            ]
        },
        {
            "title": "Helpdesk",
            "elements": [
                {"icon": "fa-life-ring", "name": "Zgłoś problem", "url": "main_panel_page"},
                {"icon": "fa-eye", "name": "Zobacz zgłoszenia", "url": "main_panel_page"},
                {"icon": "fa-question-circle", "name": "FAQ", "url": "main_panel_page"}
            ]
        }
    ]

    context = {
        "page_title": "Strona główna",
        "blocks": blocks,
    }

    return render(request, "pages/main_panel.html", context)
