from django.utils.deprecation import MiddlewareMixin


class SidebarMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_groups = request.user.groups.values_list('name', flat=True)

        sidebar_items_top = [
            {"icon": "fa-solid fa-star", "name": "Panel główny",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-star", "name": "Panel administratora",
             "url": "admin:login", "groups": ["admin"], "active": True},
            {"icon": "fa-solid fa-bell", "name": "Powiadomienia",
             "url": "notifications_page", "groups": ["admin"], "active": True},
            {"icon": "fa-solid fa-bookmark", "name": "Rezerwacje",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-computer", "name": "Przedmioty",
             "url": "main_panel_page", "groups": ["admin", "building_admin"], "active": True},
            {"icon": "fa-solid fa-user-group", "name": "Pracownicy",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-location-dot", "name": "Lokalizacje",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-calendar-days", "name": "Kalendarz",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-life-ring", "name": "Helpdesk",
             "url": "main_panel_page", "groups": ["helpdesk", "admin"], "active": True},
        ]

        sidebar_items_bottom = [
            {"icon": "fa-solid fa-triangle-exclamation", "name": "Zgłoś problem",
             "url": "main_panel_page", "groups": ["worker"], "active": True},
            {"icon": "fa-solid fa-user", "name": request.user.username,
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
