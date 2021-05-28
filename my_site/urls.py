from django.urls import path
from my_site import views

app_name = 'my_site'
urlpatterns = [
    path('', views.list_of_post, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='detail'),
    path('post_list', views.PostView.as_view(), name='posts_list'),
]