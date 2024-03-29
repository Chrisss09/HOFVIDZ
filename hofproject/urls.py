from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from halls import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    # Auth
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('hall-of-fame/create', views.CreateHall.as_view(), name='create_hall'),
    # CRUD
    path('hall-of-fame/<int:pk>', views.DetailHall.as_view(), name='detail_hall'),
    path('hall-of-fame/<int:pk>/update', views.UpdateHall.as_view(), name='update_hall'),
    path('hall-of-fame/<int:pk>/delete', views.DeleteHall.as_view(), name='delete_hall'),
    # Video
    path('hall-of-fame/<int:pk>/addvideo', views.add_video, name='add_video'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)