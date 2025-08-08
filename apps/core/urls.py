from django.urls import path
from .views import (
    # Public views
    PublicProjectListView, PublicProjectDetailView,
    PublicEventAndNewsListView, PublicEventAndNewsDetailView,
    PublicBlogPostListView, PublicBlogPostDetailView,
    PublicGalleryListView, PublicGalleryDetailView,
    PublicStaffMemberListView, PublicPartnerListView,
    
    # Admin views
    AdminProjectListCreateView, AdminProjectRetrieveUpdateDestroyView,
    AdminEventAndNewsListCreateView, AdminEventAndNewsRetrieveUpdateDestroyView,
    AdminBlogPostListCreateView, AdminBlogPostRetrieveUpdateDestroyView,
    AdminGalleryListCreateView, AdminGalleryRetrieveUpdateDestroyView,
    ContactMessageCreateView, AdminContactMessageListView, AdminContactMessageRetrieveDestroyView,
    AdminStaffMemberListCreateView, AdminStaffMemberRetrieveUpdateDestroyView, 
    AdminPartnerListCreateView, AdminPartnerRetrieveUpdateDestroyView
)

urlpatterns = [
    # ========== Public URLs ==========
    path('public/projects/', PublicProjectListView.as_view(), name='public-project-list'),
    path('public/projects/<slug:slug>/', PublicProjectDetailView.as_view(), name='public-project-detail'),
    
    path('public/events-and-news/', PublicEventAndNewsListView.as_view(), name='public-eventandnews-list'),
    path('public/events-and-news/<slug:slug>/', PublicEventAndNewsDetailView.as_view(), name='public-eventandnews-detail'),
    
    path('public/blog-posts/', PublicBlogPostListView.as_view(), name='public-blogpost-list'),
    path('public/blog-posts/<slug:slug>/', PublicBlogPostDetailView.as_view(), name='public-blogpost-detail'),
    
    path('public/galleries/', PublicGalleryListView.as_view(), name='public-gallery-list'),
    path('public/galleries/<int:pk>/', PublicGalleryDetailView.as_view(), name='public-gallery-detail'),
    
    path('public/staff-members/', PublicStaffMemberListView.as_view(), name='public-staffmember-list'),
    
    path('public/contact-messages/', ContactMessageCreateView.as_view(), name='contactmessage-create'),

     path('public/partners/', PublicPartnerListView.as_view(), name='public-partner-list'),
    
    # ========== Admin URLs ==========
    path('admin/projects/', AdminProjectListCreateView.as_view(), name='admin-project-list'),
    path('admin/projects/<slug:slug>/', AdminProjectRetrieveUpdateDestroyView.as_view(), name='admin-project-detail'),
    
    path('admin/events-and-news/', AdminEventAndNewsListCreateView.as_view(), name='admin-eventandnews-list'),
    path('admin/events-and-news/<slug:slug>/', AdminEventAndNewsRetrieveUpdateDestroyView.as_view(), name='admin-eventandnews-detail'),
    
    path('admin/blog-posts/', AdminBlogPostListCreateView.as_view(), name='admin-blogpost-list'),
    path('admin/blog-posts/<slug:slug>/', AdminBlogPostRetrieveUpdateDestroyView.as_view(), name='admin-blogpost-detail'),
    
    path('admin/galleries/', AdminGalleryListCreateView.as_view(), name='admin-gallery-list'),
    path('admin/galleries/<int:pk>/', AdminGalleryRetrieveUpdateDestroyView.as_view(), name='admin-gallery-detail'),
    
    path('admin/contact-messages/', AdminContactMessageListView.as_view(), name='admin-contactmessage-list'),
    path('admin/contact-messages/<int:pk>/', AdminContactMessageRetrieveDestroyView.as_view(), name='admin-contactmessage-detail'),
    
    path('admin/staff-members/', AdminStaffMemberListCreateView.as_view(), name='admin-staffmember-list'),
    path('admin/staff-members/<int:pk>/', AdminStaffMemberRetrieveUpdateDestroyView.as_view(), name='admin-staffmember-detail'),

    path('admin/partners/', AdminPartnerListCreateView.as_view(), name='admin-partner-list'),
    path('admin/partners/<int:pk>/', AdminPartnerRetrieveUpdateDestroyView.as_view(), name='admin-partner-detail'),
]


