from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('user-register/', views.UserRegisterView.as_view(), name='user-register'),
	path('product-list/', views.ProductListView.as_view(), name="product-list"),
	path('product-detail/<str:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
	path('product-create/', views.ProductCreateView.as_view(), name="product-create"),

	path('product-update/<str:pk>/', views.ProductUpdateView.as_view(), name="product-update"),
	path('product-delete/<str:pk>/', views.ProductDeleteView.as_view(), name="product-delete"),

	path('category-list/', views.CategoryListView.as_view(), name="category-list"),

	path('cart-list/', views.CartListView.as_view(), name="cart-list"),
	path('cart-detail/<str:pk>/', views.CartDetail.as_view(), name="cart-detail"),

	path('token/', TokenObtainPairView.as_view(), name="token"),
	path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
]