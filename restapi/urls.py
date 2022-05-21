from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('', views.ApiOverview.as_view(), name="api-overview"),
	path('api/product-list/', views.ProductListView.as_view(), name="product-list"),
	path('api/product-detail/<str:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
	path('api/product-create/', views.ProductCreateView.as_view(), name="product-create"),

	path('api/product-update/<str:pk>/', views.ProductUpdateView.as_view(), name="product-update"),
	path('api/product-delete/<str:pk>/', views.ProductDeleteView.as_view(), name="product-delete"),

	path('api/category-list/', views.CategoryListView.as_view(), name="category-list"),

	path('api/cart-list/', views.CartListView.as_view(), name="cart-list"),
	path('api/cart-detail/<str:pk>/', views.CartDetail.as_view(), name="cart-detail"),

	path('api/token/', TokenObtainPairView.as_view(), name="token"),
	path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
]