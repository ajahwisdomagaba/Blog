from django.contrib import admin
from django.urls import path

# Import views from the django_project app
from django_project.views import (
    homepage,
    about,
    article,
    blog_post, 
    not_found
)


urlpatterns = [

    # Django admin site
    path("admin/", admin.site.urls),

    # Home page
    path("", homepage),

    # About page
    path("hello/", about, name="about"),

    # Article page
    path("article/<int:pk>", article, name="article"),

    # Create blog page
    path("create_blog/", blog_post, name="create_blog"),

    #Page not found
    path("not_found/", not_found,)

]