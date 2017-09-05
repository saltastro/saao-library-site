from flask_login import UserMixin


'''The User class is used to represent users and contains the properties:

is_authenticated
This returns true if the user is authenticated and they have provided valid credentials
which gives access to pages that contain login required permission
                
is_active
This returns true if the user have active account, not suspended for any reason
             
s_anonymous
This property should return True if this is an anonymous user
          
get_id()
This method must return a unicode that uniquely identifies this user 
 '''

class User(UserMixin):
    def get_id(self):
        return 42

