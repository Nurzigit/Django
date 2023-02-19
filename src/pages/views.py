from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
        context = {}
#     context['some_string'] = 'this is some string I am passing'
#       context = {
#                 'some_string': "this is some string I am passing"
#         }

        list_of_value = []
        list_of_value.append("first")
        list_of_value.append("second")
        list_of_value.append("third")
        list_of_value.append("fouth")

        context['list_of_value'] = list_of_value
        
        return render(request, 'pages/home.html', context)



# ERRORS LOGIC
def error_404(request, exception):

        return render(request,'errors/404.html')

def error500(request, *args, **argv):
    return render(request, '500.html')
          
def error_403(request, exception):

        return render(request,'403.html')

def error_400(request,  exception):
        data = {}
        return render(request,'400.html', data) 