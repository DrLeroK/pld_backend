from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from .models import (
    Project, ProjectImage,
    EventAndNews, EventAndNewsImage,
    BlogPost, BlogImage,
    Gallery, GalleryImage,
    ContactMessage, StaffMember,
    Partner
)

# ===== Project =====
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption', 'created_at']
        read_only_fields = ['created_at']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'category',
            'start_date', 'end_date', 'is_ongoing', 'created_at',
            'updated_at', 'images'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

class AdminProjectSerializer(ProjectSerializer):
    # uploaded_images = serializers.ListField(
    #     child=serializers.ImageField(max_length=100000, 
    #                                  allow_empty_file=False, 
    #                                  use_url=False),
    #     write_only=True,
    #     required=False
    # )

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=100000,
            allow_empty_file=False,
            use_url=False,
            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]
        ),
        write_only=True,
        required=False
    )

    class Meta(ProjectSerializer.Meta):
        fields = ProjectSerializer.Meta.fields + ['uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        project = super().create(validated_data)
        
        for image in uploaded_images:
            ProjectImage.objects.create(project=project, image=image)
            
        return project

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        project = super().update(instance, validated_data)
        
        for image in uploaded_images:
            ProjectImage.objects.create(project=project, image=image)
            
        return project

# ===== EventAndNews =====
class EventAndNewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAndNewsImage
        fields = ['id', 'image', 'caption', 'created_at']
        read_only_fields = ['created_at']

class EventAndNewsSerializer(serializers.ModelSerializer):
    images = EventAndNewsImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = EventAndNews
        fields = [
            'id', 'title', 'slug', 'description', 'type',
            'location', 'start_datetime', 'end_datetime', 'is_featured',
            'created_at', 'updated_at', 'images'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

class AdminEventAndNewsSerializer(EventAndNewsSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta(EventAndNewsSerializer.Meta):
        fields = EventAndNewsSerializer.Meta.fields + ['uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        event = super().create(validated_data)
        
        for image in uploaded_images:
            EventAndNewsImage.objects.create(event_and_news=event, image=image)
            
        return event

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        event = super().update(instance, validated_data)
        
        for image in uploaded_images:
            EventAndNewsImage.objects.create(event_and_news=event, image=image)
            
        return event

# ===== BlogPost ===== 
class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'caption', 'created_at']
        read_only_fields = ['created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content',
            'author', 'published_date', 'is_published',
            'created_at', 'updated_at', 'images'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

class AdminBlogPostSerializer(BlogPostSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta(BlogPostSerializer.Meta):
        fields = BlogPostSerializer.Meta.fields + ['uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        post = super().create(validated_data)
        
        for image in uploaded_images:
            BlogImage.objects.create(blog_post=post, image=image)
            
        return post

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        post = super().update(instance, validated_data)
        
        for image in uploaded_images:
            BlogImage.objects.create(blog_post=post, image=image)
            
        return post

# ===== Gallery =====
class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'caption', 'is_featured', 'created_at']
        read_only_fields = ['created_at']

class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Gallery
        fields = [
            'id', 'title', 'description', 'created_at',
            'updated_at', 'images'
        ]
        read_only_fields = ['created_at', 'updated_at']

class AdminGallerySerializer(GallerySerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta(GallerySerializer.Meta):
        fields = GallerySerializer.Meta.fields + ['uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        gallery = super().create(validated_data)
        
        for image in uploaded_images:
            GalleryImage.objects.create(gallery=gallery, image=image)
            
        return gallery

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        gallery = super().update(instance, validated_data)
        
        for image in uploaded_images:
            GalleryImage.objects.create(gallery=gallery, image=image)
            
        return gallery

# ===== StaffMember =====
class AdminStaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = [
            'id', 'name', 'position', 'role', 'photo',
            'email', 'phone_number', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

# ===== ContactMessage =====
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'is_read', 'submitted_at']
        read_only_fields = ['is_read', 'submitted_at']


class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = [
            'id', 'name', 'position', 'role', 'photo',
            'email', 'phone_number', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'logo', 'website', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class AdminPartnerSerializer(PartnerSerializer):
    class Meta(PartnerSerializer.Meta):
        pass  # You can add admin-specific fields here if needed


