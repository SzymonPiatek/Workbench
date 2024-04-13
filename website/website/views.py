from django.shortcuts import render


def statistics(request):
    context = {
        "page_title": "Statistics"
    }

    return render(request, 'pages/statistics.html', context)


def notifications(request):
    context = {
        "page_title": "Notifications"
    }

    return render(request, 'pages/notifications.html', context)


def main_panel(request):
    blocks = [
        {
            "title": "Panel administratora",
            "elements": [
                {"icon": "fa-chart-pie", "name": "Statystyki", "view_name": "statistics_page"},
                {"icon": "fa-bell", "name": "Powiadomienia", "view_name": "notifications_page"},
            ]
        },
        {
            "title": "Rezerwacje",
            "elements": [
                {"icon": "fa-car", "name": "Parking", "view_name": "main_panel_page"},
                {"icon": "fa-display", "name": "Biurko", "view_name": "main_panel_page"},
                {"icon": "fa-people-roof", "name": "Sala", "view_name": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj pozycję", "view_name": "main_panel_page"}
            ]
        },
        {
            "title": "Przedmioty",
            "elements": [
                {"icon": "fa-list", "name": "Lista przedmiotów", "view_name": "main_panel_page"},
                {"icon": "fa-magnifying-glass", "name": "Inwentaryzacja", "view_name": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj pozycję", "view_name": "main_panel_page"}
            ]
        },
        {
            "title": "Pracownicy",
            "elements": [
                {"icon": "fa-user", "name": "Lista pracowników", "view_name": "main_panel_page"},
                {"icon": "fa-users", "name": "Lista grup", "view_name": "main_panel_page"},
                {"icon": "fa-user-plus", "name": "Dodaj pracownika", "view_name": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj grupę", "view_name": "main_panel_page"}
            ]
        },
        {
            "title": "Lokalizacje",
            "elements": [
                {"icon": "fa-building", "name": "Podgląd budynku", "view_name": "main_panel_page"},
                {"icon": "fa-door-closed", "name": "Podgląd pomieszczeń", "view_name": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj pomieszczenie", "view_name": "main_panel_page"}
            ]
        },
        {
            "title": "Kalendarz",
            "elements": [
                {"icon": "fa-calendar-check", "name": "Najbliższe wydarzenia", "view_name": "main_panel_page"},
                {"icon": "fa-plus", "name": "Dodaj wydarzenie", "view_name": "main_panel_page"}
            ]
        },
        {
            "title": "Helpdesk",
            "elements": [
                {"icon": "fa-life-ring", "name": "Zgłoś problem", "view_name": "main_panel_page"},
                {"icon": "fa-eye", "name": "Zobacz zgłoszenia", "view_name": "main_panel_page"},
                {"icon": "fa-question-circle", "name": "FAQ", "view_name": "main_panel_page"}
            ]
        }
    ]

    context = {
        "page_title": "Strona główna",
        "blocks": blocks,
    }

    return render(request, "pages/main_panel.html", context)
