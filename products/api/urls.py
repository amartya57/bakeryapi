from django.urls import path, include
from products.api import views

urlpatterns = [
    path('list/', views.ProductListAV.as_view(), name="watchlist-list"),
    path('<int:pk>/', views.ProductDetailsAV.as_view(), name='watchlist-detail'),
    
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('<int:pk>/reviews-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]

