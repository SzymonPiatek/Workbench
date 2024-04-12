from django.shortcuts import render


def main_panel(request):
    blocks = [
        ("Panel administratora", ["Statystyki"]),
        ("Rezerwacje", ["Pokój", "Biurko", "Sala", "Dodaj pozycję"]),
        ("Przedmioty", ["Sprawdź stan", "Przeprowadź inwentaryzację", "Dodaj pozycję"]),
        ("Pracownicy", ["Wyświetl wszystkich pracowników",
                        "Wyświetl wszystkie grupy",
                        "Dodaj pracownika",
                        "Dodaj grupę"]),
        ("Lokalizacje", ["Podgląd budynku", "Podgląd lokalizacji", "Dodaj lokalizację"]),
        ("Kalendarz", ["Zobacz najbliższe wydarzenia", "Dodaj wydarzenie"])
    ]

    context = {
        "blocks": blocks,
    }

    return render(request, "main_panel.html", context)
