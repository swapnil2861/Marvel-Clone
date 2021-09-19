from django.shortcuts import redirect, render
from books.models.costomer import Costomer
from django.contrib.auth.hashers import make_password
from django.views import View
import re

class Signup(View):
    def get (self, request):
        return render(request, 'signup.html')

    def post (self, request):
        pdata = request.POST
        first_name = pdata.get('name')
        email = pdata.get('email')
        password = pdata.get('password')
        c_password = pdata.get('c-password')
        phone = pdata.get('number')
        # VALIDATION
        value = {
            'first_name' : first_name,
            'email' : email,
            'phone' : phone
        }
        error_message = None
        error_message1 = None
        error_message2 = None
        error_message3 = None
        costomer = Costomer(name = first_name,
                            email = email, 
                            password = password, 
                            confirm_password = c_password, 
                            number = phone)
        passreg_x = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        # NAME VALIDATION 
        if len(first_name) < 4:
            error_message1 = 'Name must be greater tahn 4 letters'

        if (re.search(passreg_x, password)):
            error_message = None
        else:
            error_message = 'password must contain atleast one UPPERCASE & lowercase, one numeric character and one special character '

         # EMAIL VALIDATION
        emailreg_x = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        if (re.match(emailreg_x, email)):
            error_message3
        else:
            error_message3 = 'Invalid email address'

        if Costomer.isExist(costomer):
            error_message2 = 'User already exist with entered email address'

        if not error_message:
            costomer.password = (make_password(costomer.password))
            Costomer.save(costomer) 
            return redirect('comicpage')
        else:
            data ={
                'error' : error_message,
                'error1' : error_message1,
                'error2' : error_message2,
                'error3' : error_message3,
                'values' : value
            }
            return render (request, 'signup.html', data) 