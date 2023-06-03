from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create', views.FinchCreate.as_view(), name="finches_create"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finches_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finches_delete"),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('sponsors/', views.SponsorList.as_view(), name='sponsors_list'),
    path('sponsors/<int:pk>/', views.SponsorDetail.as_view(), name='sponsors_detail'),
    path('sponsors/create/', views.SponsorCreate.as_view(), name='sponsors_create'),
    path('sponsors/<int:pk>/update/', views.SponsorUpdate.as_view(), name='sponsors_update'),
    path('sponsors/<int:pk>/delete/', views.SponsorDelete.as_view(), name='sponsors_delete'),
    path('finches/<int:finch_id>/assoc_sponsor/<int:sponsor_id>/', views.assoc_sponsor, name='assoc_sponsor'),
    path('finches/<int:finch_id>/unassoc_sponsor/<int:sponsor_id>/', views.unassoc_sponsor, name='unassoc_sponsor'),
]