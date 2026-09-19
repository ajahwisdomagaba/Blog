from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog


# Create your views here.


def homepage(request):
    # Retrieve all the blog posts
    # from the database
    blog_posts = Blog.objects.all()

    return render(request, "django_project/homepage.html", {
        "blogs": blog_posts
    })


def about(request):
    return render(request, "django_project/about.html")


def article(request):
    return render(request, "django_project/article.html")


def blog_post(request):
    # Create an empty form
    form = BlogForm()

    # Handle form submission
    if request.method == "POST":
        # Put the submitted data into the form
        form = BlogForm(request.POST)
        if form.is_valid():# Check if the form is valid
            form.save()# Save the form data to the database
            return redirect("/")# Redirect to the homepage

    # Display the form
    return render(request, "django_project/create-blog.html", {
        "form": form
    })


# get the id 
# check the db to see if theres any blog post with the ID exist
# Conditionally check if it exists
    # Render the page with the blog post
# Else
    # Redirect the user to /not found

def article(request, pk):
    #scan  through the blog tables
    # and get the first blog_post whose its ID 
    # Is the same  as the primary key
    blog_posts = Blog.objects.filter(id=pk)  #use filters it doesn't raise error if page doesn't exist, gets goal is to retrieve a single objet unlike filter

    if  blog_posts.exists():
        return render(request, "django_project/article.html", {"blog": blog_posts.first()})
    else:
        return redirect("/not-found")

def not_found(request):
    return HttpResponse("Not found")