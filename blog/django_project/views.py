from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


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

@login_required
def blog_post(request):
    # Create an empty form
    form = BlogForm()

    # Handle form submission
    if request.method == "POST":
        # Put the submitted data into the form
        form = BlogForm(request.POST)
        if form.is_valid():# Check if the form is valid
            post = form.save(commit=False)
            post.author = request.user
            post.save()# Save the form data to the database
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

@login_required
def delete_blog(request, pk):
    #this finds the post by its primary key or return error if not found
    post = Blog.objects.filter(pk = pk)
    #function to delete from the db
    post.delete()
    #redirect to home
    return redirect('home')

@login_required
def edit_blog(request, pk):
    # Find the blog post, or send the user to not-found
    blog = Blog.objects.filter(pk=pk).first()
    if not blog:
        return redirect("/not-found")

    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "django_project/edit-blog.html", {
        "form": form,
        "blog": blog
    })

def not_found(request, exception=None):
    return render(request, "django_project/404.html", status=404)



def login(request):
    error = None
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        error = "Username or password is incorrect."
    return render(request, "django_project/login.html", {"error": error})


def register(request):
    error = None
    if request.method == "POST":
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        if password != confirm_password:
            error = "Passwords do not match."
        else:
            form = UserCreationForm({
                "username": request.POST.get("username", ""),
                "password1": password,
                "password2": confirm_password,
            })
            if form.is_valid():
                user = form.save(commit=False)
                user.email = request.POST.get("email", "")
                user.save()
                auth_login(request, user)
                return redirect("home")
            error = " ".join(
                message
                for messages in form.errors.values()
                for message in messages
            )
    return render(request, "django_project/signup.html", {"error": error})