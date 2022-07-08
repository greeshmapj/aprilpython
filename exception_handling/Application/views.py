from models import users,posts


session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return_fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper

def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user


class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("success")
        else:
            print("invalid")

class PostsView():
    @signin_required
    def get(self,*args,**kwargs):
        return posts

    def post(self,*args,**kwargs):
        print(kwargs)
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        print(kwargs)
        posts.append(kwargs)
        print("post added")
        print(posts)


class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        print(userId)
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts


class PostsDetailsView:
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=[post for post in posts if post["postId"]==post_id]
        if data:
           post=data[0]
           posts.remove(post)
           print("post removed")
           print(len(posts))

    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        value=self.get_object(post_id)
        post=value[0]
        post.update(data)
        print(post)

class LikeView:
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)

@signin_required
def signout(*args,**kwargs):
    user=session.pop("user")
    print(user["username"],"has been logged out")


log=SignInView()
log.post(username="richard",password="Password@123")
like=LikeView()
like.get(postid=6)

signout()

#data={
#    "title":"newtitle"
#}
#postdetails=PostsDetailsView()
#print(postdetails.put(post_id=4,data=data))

#log=SignInView()
#log.post(username="anu",password="Password@123")
#myposts=MyPostListView()
#print(myposts.get())

#post_detai=PostsDetailsView()
#post_detai.delete(post_id=6)













