from django.shortcuts import render,HttpResponse
from . models import Device

from django.http import JsonResponse
import bluetooth


# Create your views here.
def home(request):
     if request.method == 'POST':
          name = request.POST['name']
          address = request.POST['address']
          
          # create a new device instance
          device = Device(name = name, address = address)
          device.save()
          
          # Attempt to connect to the device
          try:
               sock = bluetooth.BluetoothSocket(blutooth.RFCOMM)
               sock.connect((address,1))
               sock.close()
               return JsonResponse({'status':'success'})
          except bluetooth.BluetoothError as e:
               return JsonResponse({'status':'error','message':str(e)})
     else:
          return JsonResponse(
               {
                'status':'error',
                'message': 'invalid request method'
                
                
                }
          )
          
          
          
     return render(request, 'home.html')
