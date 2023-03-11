from django.urls import path
from .views import dates, HomeListView, PostDetailView, CategoryListView, AuthorListView, PostCreateView, PostUpdateView,PostDeleteView,AboutPageView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('author/', AuthorListView.as_view(), name='author'),
    path('dates/<int:month_id>/<int:year_id>',dates, name='dates'),
    path('post/<pk>',PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name= 'create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name= 'update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name= 'delete'),
    path('about/',AboutPageView.as_view(), name='about' )
]
