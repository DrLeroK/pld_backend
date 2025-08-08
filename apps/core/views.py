from rest_framework import generics, permissions
from .models import (
    Project, EventAndNews, BlogPost, Gallery,
    ContactMessage, StaffMember, Partner
)
from .serializers import (
    ProjectSerializer, EventAndNewsSerializer, BlogPostSerializer,
    GallerySerializer, ContactMessageSerializer, StaffMemberSerializer,
    AdminProjectSerializer, AdminEventAndNewsSerializer, 
    AdminBlogPostSerializer, AdminGallerySerializer, AdminStaffMemberSerializer,
    AdminPartnerSerializer, PartnerSerializer
)

# ========== Public Views (Read Only) ==========
class PublicProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

class PublicProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

class PublicEventAndNewsListView(generics.ListAPIView):
    serializer_class = EventAndNewsSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = EventAndNews.objects.all()
        
        # Filter by type if provided
        item_type = self.request.query_params.get('type', None)
        if item_type in ['event', 'news']:
            queryset = queryset.filter(type=item_type)
        
        # Apply ordering
        queryset = queryset.order_by('-start_datetime')
        
        # Limit results if requested
        limit = self.request.query_params.get('limit', None)
        if limit and limit.isdigit():
            queryset = queryset[:int(limit)]
            
        return queryset

class PublicEventAndNewsDetailView(generics.RetrieveAPIView):
    queryset = EventAndNews.objects.all()
    serializer_class = EventAndNewsSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

class PublicBlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

class PublicBlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

class PublicGalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]

class PublicGalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]

class PublicStaffMemberListView(generics.ListAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
    permission_classes = [permissions.AllowAny]

class PublicPartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.AllowAny]

# ========== Admin Views (CRUD) ==========
class AdminProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = AdminProjectSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = AdminProjectSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]

class AdminEventAndNewsListCreateView(generics.ListCreateAPIView):
    queryset = EventAndNews.objects.all()
    serializer_class = AdminEventAndNewsSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminEventAndNewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventAndNews.objects.all()
    serializer_class = AdminEventAndNewsSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]

class AdminBlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = AdminBlogPostSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminBlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = AdminBlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]

class AdminGalleryListCreateView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = AdminGallerySerializer
    permission_classes = [permissions.IsAdminUser]

class AdminGalleryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = AdminGallerySerializer
    permission_classes = [permissions.IsAdminUser]

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

class AdminContactMessageListView(generics.ListAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminContactMessageRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminStaffMemberListCreateView(generics.ListCreateAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = AdminStaffMemberSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminStaffMemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = AdminStaffMemberSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminPartnerListCreateView(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminPartnerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerSerializer
    permission_classes = [permissions.IsAdminUser]



