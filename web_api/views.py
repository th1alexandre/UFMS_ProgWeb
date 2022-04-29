from django.shortcuts import redirect
from django.contrib.auth.models import User
from web_routes.views import sign_in, sign_up
from uuid import uuid4

def login(request):
    pass

def logout(request):
    pass

def user_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password_1': password_1,
            'password_2': password_2
        }

        if _user_create_validate(data):
            user = User.objects.create(
                    username = uuid4(),
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    email = data['email'],
                    password = data['password_1']
                )
            user.save()
            return redirect(sign_in)
        return redirect(sign_up)

def user_delete(request):
    pass

def user_update(request):
    pass


def _user_create_validate(args):
    if User.objects.filter(email = args['email']).exists():
        return False

    password = _user_create_validate_password(
        args['password_1'],
        args['password_2']
    )
    
    return password

def _user_create_validate_password(password_1, password_2):
    if password_1 == password_2:
        return True
    else:
        return False
