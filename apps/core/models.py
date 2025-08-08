from django.db import models
from django.utils.text import slugify
from django.utils import timezone



class Project(models.Model):
    CATEGORY_CHOICES = [
        ('youth_empowerment', 'Youth Empowerment'),
        ('women_empowerment_child_care', 'Women Empowerment And Child Care'),
        ('health_care', 'Health Care'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Project Title", 
                             help_text="Enter the project title (max 200 chars)")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=35, choices=CATEGORY_CHOICES, default='other')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class EventAndNews(models.Model):
    TYPE_CHOICES = [
        ('event', 'Event'),
        ('news', 'News'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='event')
    location = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class EventAndNewsImage(models.Model):
    event_and_news = models.ForeignKey(EventAndNews, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_and_news_images/')
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.event_and_news.title}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class BlogImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.blog_post.title}"

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image in {self.gallery.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"

class StaffMember(models.Model):
    ROLE_CHOICES = [
        ('board_member', 'Board Member'),
        ('our_team', 'Our Team'),
        ('volunteer', 'Volunteer'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='other')
    photo = models.ImageField(upload_to='staff_photos/')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partner_logos/')
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






