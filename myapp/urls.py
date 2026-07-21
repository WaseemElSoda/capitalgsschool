# myapp/urls.py
from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateAndUpdateView
# from .views import BankCreateView


urlpatterns = [
    path('', views.index, name='index'),  
    path('profile-settings/', views.pages_profile_settings, name='profile-settings'),  
    path('chat/', views.app_chat, name='chat'), 
    path('tasks-kanban/', views.apps_tasks_kanban, name='tasks-kanban'), 
    path('faqs/', views.pages_faqs, name='faqs'), 
    path('profile/', views.profile_page, name='profile'), 
    path('lockscreen/', views.auth_lockscreen_basic, name='lockscreen'), 
    path('logout/', views.auth_logout_basic, name='logout'), 
    path('pages-search-results/', views.pages_search_results, name='pages-search-results'), 
    path('institute/', CreateAndUpdateView.as_view(), name='institute_list'),
    path('institute/<int:pk>/', CreateAndUpdateView.as_view(), name='institute_CreateUpdate'),
    
    
    

   

] 
