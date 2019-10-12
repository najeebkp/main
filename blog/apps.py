from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #method just to import the signals
    	import users.signals
