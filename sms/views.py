from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import africastalking
import json

africastalking.initialize(
    username='sandbox',
    api_key='e16f5a62576771c9a9a2e9ac5611ea00f82837759b1412ef1d804bfbce7d087d'
)

sms = africastalking.SMS

@csrf_exempt
def send_sms(request):
    if request.method == 'POST':
        # Parse raw data as JSON
        data = json.loads(request.body)
        recipients = data.get('recipients', '')
        message = data.get('message', '')
        sender = data.get('sender', '')

        try:
            response = sms.send(message, recipients, sender)
            return JsonResponse({'success': True, 'response': response})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    




