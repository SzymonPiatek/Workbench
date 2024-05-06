from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser


def users_list(request):
    all_users = CustomUser.objects.all()

    context = {
        "page_title": "Pracownicy",
        "users": all_users,
        "sidebar_items": request.sidebar_items,
    }

    return render(request, 'pages/users/main.html', context)


def get_all_users(request):
    search_text = request.GET.get('search', '')
    users = CustomUser.objects.filter(username__icontains=search_text)
    user_list = [
        {'username': user.username,
         'full_name': user.full_name if user.full_name else user.username,
         'email': user.email} for user in users]
    return JsonResponse(user_list, safe=False)
