from django.contrib import admin
from django.urls import path
from django.urls.conf import include 

# Import views from the django_project app
from django_project.views import (
    homepage,
    about,
    article,
    blog_post, 
    not_found,
    delete_blog,
    edit_blog,
    register,
    login
)


urlpatterns = [
    # Django admin site
    path("admin/", admin.site.urls),

    # Login and signup pages (registered before the auth include
    path("accounts/login/", login, name="login"),

    path("accounts/signup/", register, name="signup"),

    #accounts
    path("accounts/", include('django.contrib.auth.urls')),

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
    path("article/<int:pk>/delete/", delete_blog, name = "delete_blog"),

    #edit
    path("article/<int:pk>/edit/", edit_blog, name="edit_blog")
]

# Catches any missed or invalid route across your entire project:
handler404 = "django_project.views.not_found"