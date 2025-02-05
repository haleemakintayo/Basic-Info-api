
from django.http import JsonResponse
from django.utils import timezone

def info(request):
    data = {
        "email": "haleemakintayo@gmail.com",  
        "current_datetime": timezone.now().isoformat(), 
        "github_url": "https://github.com/haleemakintayo/Basic-Info-api"  
    }
    return JsonResponse(data, status=200)
