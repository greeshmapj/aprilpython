from models import users,posts

def authenticate(username,email):      #kwargs:"username:"django","email":".....
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data


#user=(authenticate(username="Bret",email="Sincere@april.biz"))
#if user:
#    print("login successful")
#else:
#    print("invalid credentials")

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username,email=email)
        if user:
            print("success")
        else:
            print("invalid credentials")


sv=SignInView()
sv.post(username="Bret",email="Sincere@april.biz")
