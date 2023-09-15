from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from rest_framework import generics
from .models import personBio
from .serializers import personBioSerializer
from django.contrib.auth.models import User
# Create your views here.

class UserList(generics.ListCreateAPIView):
    serializer_class = personBio
    
    def get_queryset(self):
         queryset = personBio.objects.all()
         name = self.request.query.params.get('personBio')
         if name is not None:
             queryset = queryset.filter(personBio = 'name')
             
    
class UserId(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = personBioSerializer
    queryset = personBio.objects.all()


class UserName(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = personBioSerializer
    queryset = personBio.objects.all() 








# def My_endpoints(request):
#         slack_name = request.GET.get('slack_name', 'Adeniji Ridwan')
#         track = request.GET.get('track', 'backend')
#         current_day = datetime.now().strftime('%A')
#         utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
#         github_file_url = 'https://github.com/adenijiridwan43/Endpoint/blob/main/backend/api/views.py'
#         github_repo_url = 'https://github.com/adenijiridwan43/Endpoint'
#         status_code = 200
        
        
#         response_data = {
#             "slack_name" : slack_name,
#             "current_day" : current_day,
#             "utc_time" : utc_time,
#             "track" : track,
#             "github_file_url" : github_file_url,
#             "github_repo_url" : github_repo_url,
#             "status_code" : status_code
#         }
        
#         return JsonResponse(response_data)
        


