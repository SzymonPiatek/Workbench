from django.http import JsonResponse
from users.models import CustomUser


def get_all_users(request):
    search_text = request.GET.get('search', '')
    users = CustomUser.objects.filter(username__icontains=search_text)
    user_list = [{'username': user.username} for user in users]
    return JsonResponse(user_list, safe=False)
