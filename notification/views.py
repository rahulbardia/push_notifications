from rest_framework.response import Response
from rest_framework.views import APIView
from notification.models import Person, notification

# Create your views here.

class subscriberView(APIView):
    def object_available(self, subscriber_id):
        obj = Person.objects.filter(subscriber_id=subscriber_id)
        if obj:
            return True
        else:
            return False
    def post(self, request, format=None):
        # Serializer to be added
        try:
            if self.object_available(request.data['subscriber_id']):
                return Response({'error': False, 'existing': True,
                                 'message':'You have already subscribed to this channel'})
            else:
                push = Person(subscriber_id=request.data['subscriber_id'], browser_name='chrome',
                              browser_engine='microsoft', device='Tablet')
                push.save()
            return Response({'error': False, 'existing': False, 'message':'subscribed channel Added'})
        except:
            return Response({'error': True})

class notifyView(APIView):
    def object_available(self, notification_url):
        obj = notification.objects.filter(notification_url=notification_url)
        if obj:
            return True
        else:
            return False

    def post(self, request, format=None):
        # Serializer to be added
        try:
            if self.object_available(request.data['notification_url']):
                return Response({'error': False, 'existing': True,
                                 'message':'You have already subscribed to this channel'})
            else:
                push = notification(notification_title=request.data['notification_title'], subscriber_id=request.data['subscriber_id'],
                                    notification_tag=request.data['notification_tag'], notification_url=request.data['notification_url'],
                                    notification_message=request.data['notification_message'])
                push.save()
            return Response({'error': False, 'existing': False, 'message':'subscribed channel Added'})
        except Exception as e:
            print e
            return Response({'error': True})

    def get(self, request, format=None):
        try:
            print request.GET['subscriber_id']
            if not request.GET['subscriber_id']:
                return Response({'No subscriber ID provided to see its notifications'})
            push_notifications = notification.objects.filter(subscriber_id=request.GET['subscriber_id'])
            dic = {'notified': push_notifications}
            # Serialization needs to done
            return Response(dic)
        except Exception as e:
            print e
            return Response({'error':'No such ID'})