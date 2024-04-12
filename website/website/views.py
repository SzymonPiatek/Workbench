from django.shortcuts import render


def main_panel(request):
    blocks = [
        {
            "title": "Panel administratora",
            "elements": [
                {"icon": "fa-chart-pie", "name": "Statystyki"},
                {"icon": "fa-bell", "name": "Powiadomienia"},
            ]
        },
        {
            "title": "Rezerwacje",
            "elements": [
                {"icon": "fa-car", "name": "Parking"},
                {"icon": "fa-display", "name": "Biurko"},
                {"icon": "fa-people-roof", "name": "Sala"},
                {"icon": "fa-plus", "name": "Dodaj pozycję"}
            ]
        },
        {
            "title": "Przedmioty",
            "elements": [
                {"icon": "fa-list", "name": "Lista przedmiotów"},
                {"icon": "fa-magnifying-glass", "name": "Inwentaryzacja"},
                {"icon": "fa-plus", "name": "Dodaj pozycję"}
            ]
        },
        {
            "title": "Pracownicy",
            "elements": [
                {"icon": "fa-user", "name": "Lista pracowników"},
                {"icon": "fa-users", "name": "Lista grup"},
                {"icon": "fa-user-plus", "name": "Dodaj pracownika"},
                {"icon": "fa-plus", "name": "Dodaj grupę"}
            ]
        },
        {
            "title": "Lokalizacje",
            "elements": [
                {"icon": "fa-building", "name": "Podgląd budynku"},
                {"icon": "fa-door-closed", "name": "Podgląd pomieszczeń"},
                {"icon": "fa-plus", "name": "Dodaj pomieszczenie"}
            ]
        },
        {
            "title": "Kalendarz",
            "elements": [
                {"icon": "fa-calendar-check", "name": "Najbliższe wydarzenia"},
                {"icon": "fa-plus", "name": "Dodaj wydarzenie"}
            ]
        },
        {
            "title": "Helpdesk",
            "elements": [
                {"icon": "fa-life-ring", "name": "Zgłoś problem"},
                {"icon": "fa-eye", "name": "Zobacz zgłoszenia"},
                {"icon": "fa-question-circle", "name": "FAQ"}
            ]
        }
    ]

    context = {
        "blocks": blocks,
    }

    return render(request, "main_panel.html", context)
