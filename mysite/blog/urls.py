from django.urls import path
from . import views


urlpatterns = [
    path('',views.Post_List_View.as_view(),name='post_list'),
    path('about/',views.About_View.as_view(),name='about'),
    path('scrap/',views.Job_View.as_view(),name='scrap'),
    path('post/<int:pk>',views.Post_Detail_View.as_view(),name='post_detail'),
    path('post/new/',views.Create_Post_View.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.Post_Update_View.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',views.Post_Delete_View.as_view(),name='post_remove'),
    path('drafts/',views.Draft_List_View.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),


]
