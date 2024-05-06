from django.utils.deprecation import MiddlewareMixin


class SidebarMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_groups = request.user.groups.values_list('name', flat=True)

        sidebar_items_top = [
            {"icon": "fa-solid fa-star", "name": "Panel główny", "class": "item",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-star", "name": "Panel administratora", "class": "item",
             "url": "admin:login", "groups": ["admin"], "active": True},
            {"icon": "fa-solid fa-bell", "name": "Powiadomienia", "class": "item",
             "url": "notifications_page", "groups": ["admin"], "active": True},
            {"icon": "fa-solid fa-bookmark", "name": "Rezerwacje", "class": "item",
             "url": "main_panel_page", "groups": ["worker"], "active": False},
            {"icon": "fa-solid fa-computer", "name": "Przedmioty", "class": "item",
             "url": "items_page", "groups": ["admin", "building_admin"], "active": True},
            {"icon": "fa-solid fa-user-group", "name": "Pracownicy", "class": "item",
             "url": "users_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-location-dot", "name": "Lokalizacje", "class": "item",
             "url": "localizations_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-calendar-days", "name": "Kalendarz", "class": "item",
             "url": "main_panel_page", "groups": ["worker"], "active": False},
            {"icon": "fa-solid fa-life-ring", "name": "Helpdesk", "class": "item",
             "url": "main_panel_page", "groups": ["helpdesk", "admin"], "active": False},
        ]

        sidebar_items_bottom = [
            {"icon": "fa-solid fa-triangle-exclamation", "name": "Zgłoś problem", "class": "item",
             "url": "main_panel_page", "groups": ["worker"], "active": False},
            {"icon": "fa-solid fa-user", "name": request.user.username, "class": "item",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
        ]

        filtered_sidebar_items_top = []
        for item in sidebar_items_top:
            if item["active"]:
                if any(group in user_groups for group in item.get("groups", [])):
                    filtered_sidebar_items_top.append(item)

        filtered_sidebar_items_bottom = []
        for item in sidebar_items_bottom:
            if item["active"]:
                if any(group in user_groups for group in item.get("groups", [])):
                    filtered_sidebar_items_bottom.append(item)

        request.sidebar_items = [filtered_sidebar_items_top, filtered_sidebar_items_bottom]
