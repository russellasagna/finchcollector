from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('finches/<int:finch_id>/assoc_treat/<int:treat_id>/', views.assoc_treat, name='assoc_treat'),
  path('finches/<int:finch_id>/unassoc_treat/<int:treat_id>/', views.unassoc_treat, name='unassoc_treat'),
  path('treats/', views.TreatList.as_view(), name='treats_index'),
  path('treats/<int:pk>/', views.TreatDetail.as_view(), name='treats_detail'),
  path('treats/create/', views.TreatCreate.as_view(), name='treats_create'),
  path('treats/<int:pk>/update/', views.TreatUpdate.as_view(), name='treats_update'),
  path('treats/<int:pk>/delete/', views.TreatDelete.as_view(), name='treats_delete'),
] 