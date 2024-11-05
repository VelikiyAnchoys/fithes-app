from django.urls import path
from . import views
from .views import upload_image

urlpatterns= [
    path('', views.home_page, name='home_page'),
    path('clubs/', views.zal_page, name='zal_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('abonements/', views.abonement_page, name='abonements_page'),
    path('zals/detail<int:pk>', views.zal_detail_page, name='zal_detail_page'),
    path('treners/', views.trener_page, name='treners_page'),
    path('treners/detail<int:pk>', views.trener_detail_page, name='trener_detail_page'),
    path('pitanies/', views.pitanie_page, name='pitanies_page'),
    path('pitanies/detail<int:pk>', views.pitanie_detail_page, name='pitanie_detail_page'),
    path('trendoms/', views.trendom_page, name='trendoms_page'),
    path('spectrens/', views.spectren_page, name='spectrens_page'),
    path('category/post/<slug:slug>/', views.zals_by_category_page, name='zals-by-category_page'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('abon-purchase/', views.abon_purchase, name='abon_purchase'),
    path('logout/',views.logout_action, name='logout_action'),
    path('spectrens/detail<int:pk>', views.spectren_detail_page, name='spectren_detail_page'),
]