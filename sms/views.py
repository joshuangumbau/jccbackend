from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import africastalking
import json

africastalking.initialize(
    username='sandbox',
    api_key='59f919f1ef98c021f6dda40216f92185961ff7465705fc49208c7d475d31550a'
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
    




