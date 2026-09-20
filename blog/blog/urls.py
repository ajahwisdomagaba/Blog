from django.contrib import admin
from django.urls import path

# Import views from the django_project app
from django_project.views import (
    homepage,
    about,
    article,
    blog_post, 
    not_found,
    delete_blog
)


urlpatterns = [
    # Django admin site
    path("admin/", admin.site.urls),

    # Home page (added name='home')
    path("", homepage, name="home"),

    # About page
    path("about/", about, name="about"),

    # Article page (added trailing slash)
    path("article/<int:pk>/", article, name="article"),

    # Create blog page
    path("create_blog/", blog_post, name="create_blog"),

    # Page not found
    path("not_found/", not_found, name="not_found"),

    #delete
    path("article/<int:pk>/delete/", delete_blog, name = "delete_blog")
]

# Catches any missed or invalid route across your entire project:
handler404 = "django_project.views.not_found"