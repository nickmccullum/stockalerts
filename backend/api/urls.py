from rest_framework.routers import SimpleRouter
from api.views import UserView, LoginView, RegisterView


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginView, basename='auth-login')
routes.register(r'auth/register', RegisterView, basename='auth-register')
# routes.register(r'auth/refresh', RefreshView, basename='auth-refresh')

# USER
routes.register(r'user', UserView, basename='user')


urlpatterns = [
    *routes.urls
]