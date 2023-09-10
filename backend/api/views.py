from django.shortcuts import render
from rest_framework.response import Response
from datetime import datetime
from django.http import JsonResponse
# Create your views here.

def My_endpoints(request):
        slack_name = request.GET.get('slack_name', 'Adeniji Ridwan')
        track = request.GET.get('track', 'backend')
        current_day = datetime.now().strftime('%A')
        utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        github_file_url = 'https://github.com/adenijiridwan43/Endpoint-Track/blob/main/api/views.py'
        github_repo_url = 'https://github.com/adenijiridwan43/Endpoint-Track'
        status_code = 200
        
        
        response_data = {
            "slack_name" : slack_name,
            "current_day" : current_day,
            "utc_time" : utc_time,
            "track" : track,
            "github_file_url" : github_file_url,
            "github_repo_url" : github_repo_url,
            "status_code" : status_code
        }
        
        return JsonResponse(response_data)
        


