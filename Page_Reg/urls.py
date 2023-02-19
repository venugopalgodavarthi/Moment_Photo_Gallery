from django.urls import path
from Page_Reg import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "Page_Reg"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('next/', views.next, name="next"),
    path('logout/', views.logout, name="logout"),
    path('category/', views.categoriesview.as_view(), name="category"),
    path('delete/<int:pk>/', views.DeleteImageview.as_view(), name="delete"),
    path('images/', views.Imagesview, name="images"),
    path('success/', views.successview, name="success"),
    path('gallary/', views.Gallaryview, name="gallary")


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
