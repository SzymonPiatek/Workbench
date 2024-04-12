from django.shortcuts import render


def main_panel(request):
    blocks = {
        "Panel administratora": {"Statystyki"},
        "Rezerwacje": {"Pokój", "Biurko", "Sala"},
        "Przedmioty": {"Sprawdź stan", "Przeprowadź inwentaryzację"},
        "Pracownicy": {"Wyświetl wszystkich pracowników",
                       "Wyświetl wszystkie grupy"},
        "Lokalizacje": {"Podgląd budynku", "Podgląd lokalizacji"},
        "Kalendarz": {"Zobacz najbliższe wydarzenia", "Dodaj wydarzenie"}
    }

    context = {
        "page_title": "Strona główna",
        "blocks": blocks,
    }
    return render(request, "main_panel.html", context)
