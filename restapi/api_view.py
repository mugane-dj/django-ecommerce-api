@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create': '/product-create/',
        'Update': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>/',
        'Cart-list': '/cart-list/',
        'Cart-detail': '/cart-detail/<str:pk>/',
        'Category-list': '/category-list/'
    }
    return Response(api_urls)

@api_view(['GET'])
def categoryList(request):
    
    category = Category.objects.all().order_by('category_name')
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cartList(request):
    cart = Cart.objects.all().order_by('cartID')
    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data)

@api_view
def cartDetail(request, pk):
    cart = Cart.objects.get(cartID=pk)
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def productList(request):
    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
	products = Product.objects.get(productID=pk)
	serializer = ProductSerializer(products, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(productID=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(productID=pk)
    product.delete()
    return Response('Item deleted!')