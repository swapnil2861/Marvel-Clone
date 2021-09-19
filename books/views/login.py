from django.shortcuts import redirect, render, HttpResponseRedirect
from books.models.costomer import Costomer
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    return_url = None
    def get (self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html') 

    def post (self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        costomer = Costomer.get_costomer_by_email(email)
        error_message = None
        if costomer:
            flag = check_password(password, costomer.password)
            if flag:
                request.session['costomer'] = costomer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('comicpage')
            else:
                error_message = 'Invalid Email or Password'
        else:
            error_message = 'Invalid Email or Password'
        return render(request, 'login.html', {'error' : error_message})

def Logout(request):
    request.session.clear()
    return redirect ('login')