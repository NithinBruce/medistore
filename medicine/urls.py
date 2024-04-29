from django.urls import path,include
from cure import views
urlpatterns = [
  path('',views.home,name='Home'),
  path('signup/', views.signup,name='signup'),
  path('login/',views.login_page,name='login'),
  path('logout/', views.logout_page,name='logout'),
   path('create/',views.product_create,name='createproduct'),
  path('welcome/',views.welcome,name='welcome'),
  path('list/',views.product_read,name='list'),
  path('update/<int:pk>/',views.product_update,name='updateproduct'),
  path('delete/<int:pk>',views.product_delete,name='deleteproduct'),
  path('search/',views.search,name='search'),    
  path('cureapi/',include('cureapi.urls'))       
  

]