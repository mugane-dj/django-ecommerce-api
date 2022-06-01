from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('user-register/', views.UserRegisterView.as_view(), name='user-register'),

	path('product-list/', views.ProductListView.as_view(), name="product-list"),
	path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
	path('product-create/', views.ProductCreateView.as_view(), name="product-create"),
	path('product-update/<int:pk>/', views.ProductUpdateView.as_view(), name="product-update"),
	path('product-delete/<int:pk>/', views.ProductDeleteView.as_view(), name="product-delete"),

	path('review-detail/<int:pk>/', views.ReviewDetailView.as_view(), name="review-detail"),
	path('review-create/', views.ReviewCreateView.as_view(), name="review-create"),
	path('review-delete/<int:pk>/', views.ReviewDeleteView.as_view(), name="review-delete"),

	path('category-list/', views.CategoryListView.as_view(), name="category-list"),
	path('order-list/', views.OrderListView.as_view(), name="order-list"),
	path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name="order-detail"),

	path('address-detail/<int:pk>/', views.AddressDetailView.as_view(), name="address-detail"),
	path('address-create/', views.AddressCreateView.as_view(), name="address-create"),
	path('address-update/<int:pk>/', views.AddressUpdateView.as_view(), name="address-update"),
	path('address-delete/<int:pk>/', views.AddressDeleteView.as_view(), name="address-delete"),

	path('token/', TokenObtainPairView.as_view(), name="token"),
	path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
]