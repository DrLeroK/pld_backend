from django.contrib import admin
from .models import (
    Project, ProjectImage,
    EventAndNews, EventAndNewsImage,
    BlogPost, BlogImage,
    Gallery, GalleryImage,
    ContactMessage, StaffMember,
    Partner
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'is_ongoing')
    list_filter = ('category', 'is_ongoing')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

class EventAndNewsImageInline(admin.TabularInline):
    model = EventAndNewsImage
    extra = 1

@admin.register(EventAndNews)
class EventAndNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'start_datetime', 'is_featured')
    list_filter = ('type', 'is_featured')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [EventAndNewsImageInline]

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlogImageInline]

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    inlines = [GalleryImageInline]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'submitted_at')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('submitted_at',)

@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'role', 'email')
    list_filter = ('role',)
    search_fields = ('name', 'position', 'email')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'logo')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )










# from django.contrib import admin
# from .models import (
#     Project, ProjectImage,
#     Event, EventImage,
#     BlogPost, BlogImage,
#     Gallery, GalleryImage,
#     ContactMessage,
#     Testimonial,
#     StaffMember
# )

# class ProjectImageInline(admin.TabularInline):
#     model = ProjectImage
#     extra = 1

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'start_date', 'end_date', 'is_ongoing')
#     search_fields = ('title', 'description')
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [ProjectImageInline]

# class EventImageInline(admin.TabularInline):
#     model = EventImage
#     extra = 1

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('title', 'event_type', 'start_datetime', 'end_datetime', 'is_featured')
#     list_filter = ('event_type', 'is_featured')
#     search_fields = ('title', 'description', 'location')
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [EventImageInline]

# class BlogImageInline(admin.TabularInline):
#     model = BlogImage
#     extra = 1

# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date', 'is_published')
#     list_filter = ('is_published',)
#     search_fields = ('title', 'content', 'author')
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [BlogImageInline]

# class GalleryImageInline(admin.TabularInline):
#     model = GalleryImage
#     extra = 1

# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title', 'description')
#     inlines = [GalleryImageInline]

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'subject', 'is_read', 'submitted_at')
#     list_filter = ('is_read',)
#     search_fields = ('name', 'email', 'subject', 'message')
#     readonly_fields = ('submitted_at',)

# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('author', 'role', 'is_featured', 'created_at')
#     list_filter = ('is_featured',)
#     search_fields = ('author', 'role', 'content')

# @admin.register(StaffMember)
# class StaffMemberAdmin(admin.ModelAdmin):
#     list_display = ('name', 'position', 'is_active', 'joined_date')
#     list_filter = ('position', 'is_active')
#     search_fields = ('name', 'position', 'bio')