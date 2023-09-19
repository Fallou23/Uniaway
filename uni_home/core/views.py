

from django.core.paginator import Paginator

from importlib.resources import path


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, PostImage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.conf import settings
from .presign import get_s3_presigned_url


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('host_landing')
    else:

        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)
        profile_url = get_s3_presigned_url(user_profile.profileimg.url)

        page = request.GET.get('page')
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 6)

        try:

            posts = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            posts = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            posts = paginator.page(page)

        for post in posts:
            # Retrieve all associated images for the post
            post_images = PostImage.objects.filter(post=post)

            # Store the image URLs in the dictionary
            image_urls = [get_s3_presigned_url(post_image.images.url) for post_image in post_images]

    return render(
        request, 'index.html',
        {'user_profile': user_profile, 'posts': posts, 'paginator': paginator,
         'profile_url': profile_url, 'post_image_urls': image_urls})


def host_index(request):
    page = request.GET.get('page')
    posts = Post.objects.all().order_by('created_at')
    paginator = Paginator(posts, 6)
    
    for post in posts:
        # Retrieve all associated images for the post
        post_images = PostImage.objects.filter(post=post)
        

        # Store the image URLs in the dictionary
        #image_urls = [get_s3_presigned_url(post_image.images.url) for post_image in post_images]

    try:

        posts = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    return render(
        request, 'index.html',
        {'posts': posts, 'paginator': paginator,
         'post_images': post_images})



def landing(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    profile_url = get_s3_presigned_url(user_profile.profileimg.url)
    posts = Post.objects.all()

    return render(
        request, 'landing.html',
        {'user_profile': user_profile, 'posts': posts, "user_object": user_object,
         "profile_url": profile_url})


def host_landing(request):
    return render(request, 'landing.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        seller = request.POST.get('seller', False) == 'on'

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email esistente')
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username esistente')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.seller = seller
                new_profile.save()
                return redirect('signin')
        else:

            messages.info(request, 'Le Password Sono Diverse')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credenziali non valide')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def settings(request):

    user_profile = Profile.objects.get(user=request.user)
    profile_url = get_s3_presigned_url(user_profile.profileimg.url)

    if request.method == 'POST':

        if request.FILES.get('image') is None:
            image = user_profile.profileimg
            name_surname = request.POST['name_surname']
            bio = request.POST['bio']
            location = request.POST['location']
            università = request.POST['università']

            user_profile.profileimg = image
            user_profile.name_surname = name_surname
            user_profile.bio = bio
            user_profile.location = location
            user_profile.università = università
            user_profile.save()

        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
            name_surname = request.POST['name_surname']
            bio = request.POST['bio']
            location = request.POST['location']
            università = request.POST['università']

            user_profile.profileimg = image
            user_profile.name_surname = name_surname
            user_profile.bio = bio
            user_profile.location = location
            user_profile.università = università
            user_profile.save()

        return redirect('/')

    return render(request, 'settings.html', {
                  'user_profile': user_profile, 'profile_url': profile_url})


@login_required(login_url='signin')
def seller_settings(request):

    user_profile = Profile.objects.get(user=request.user)
    profile_url = get_s3_presigned_url(user_profile.profileimg.url)

    if request.method == 'POST':

        if request.FILES.get('image') is None:
            image = user_profile.profileimg
            seller_name = request.POST['seller_name']
            bio = request.POST['bio']
            email = request.POST['email']
            phone_number = request.POST['phone_number']

            user_profile.profileimg = image
            user_profile.seller_name = seller_name
            user_profile.bio = bio
            user_profile.email = email
            user_profile.phone_number = phone_number
            user_profile.save()

        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
            seller_name = request.POST['seller_name']
            bio = request.POST['bio']
            email = request.POST['email']
            phone_number = request.POST['phone_number']

            user_profile.profileimg = image
            user_profile.seller_name = seller_name
            user_profile.bio = bio
            user_profile.email = email
            user_profile.phone_number = phone_number
            user_profile.save()

        return redirect('/')

    return render(request, 'settings.html', {
                  'user_profile': user_profile, "profile_url": profile_url})


@login_required(login_url='signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        images = request.FILES.getlist('image'),
        title = request.POST['title']
        position = request.POST['position']
        price = request.POST['price']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        caption = request.POST['caption']
        post = Post(user=user, title=title, position=position, price=price,
                    phone_number=phone_number, email=email, caption=caption)
        post.save()

        # You would have to make some iterations through the list images inorder to post
        # them to your database
        for i in images[0]:
            images = PostImage.objects.create(
                post=post,
                images=i
            )
            images.save()

        return redirect('/')

    else:
        return render(request, 'upload.html')


@login_required(login_url='signin')
def update(request):

    user_profile = Profile.objects.get(user=request.user)

    profile_url = get_s3_presigned_url(user_profile.profileimg.url)

    if request.method == 'POST':

        if request.FILES.get('image') is None:
            image = user_profile.profileimg
            name_surname = request.POST['name_surname']
            bio = request.POST['bio']
            location = request.POST['location']
            università = request.POST['università']

            user_profile.profileimg = image
            user_profile.name_surname = name_surname
            user_profile.bio = bio
            user_profile.location = location
            user_profile.università = università
            user_profile.save()

        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
            name_surname = request.POST['name_surname']
            bio = request.POST['bio']
            location = request.POST['location']
            università = request.POST['università']

            user_profile.profileimg = image
            user_profile.name_surname = name_surname
            user_profile.bio = bio
            user_profile.location = location
            user_profile.università = università
            user_profile.save()

        return redirect('profile')

    return render(request, 'profile.html', {
                  'user_profile': user_profile, "profile_url": profile_url})


def delete_post(request, pk):
    user_profile = Profile.objects.get(user=request.user)
    profile_url = get_s3_presigned_url(user_profile.profileimg.url)
    post = Post.objects.filter(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')

    return render(
        request, 'profile.html',
        {'post': post, 'user_profile': user_profile, 'profile_url': profile_url})


@login_required(login_url='signin')
def profile(request, pk):

    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)

    image_urls = [get_s3_presigned_url(post_image.images.url) for post_image in user_posts]

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_photos': image_urls,
        'profile_url': get_s3_presigned_url(user_profile.profileimg.url)
    }

    return render(request, 'profile.html', context)


def post(request, pk):
    user_profile = Profile.objects.get(user=request.user)
    post = get_object_or_404(Post, id=pk)
    photos = PostImage.objects.filter(post=post)
    image_urls = [get_s3_presigned_url(post_image.images.url) for post_image in photos]
    context = {
        'post': post,
        'photos': image_urls,
        'profile_url': get_s3_presigned_url(user_profile.profileimg.url)


    }

    return render(request, 'post.html', context)


def posts_list_url(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    profile_url = get_s3_presigned_url(user_profile.profileimg.url)
    posts = Post.objects.all()
    search_query = request.GET.get('search', '')
    for post in posts:
        # Retrieve all associated images for the post
        post_images = PostImage.objects.filter(post=post)

        # Store the image URLs in the dictionary
        image_urls = [get_s3_presigned_url(post_image.images.url) for post_image in post_images]

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) |
                                    Q(position__icontains=search_query))
    else:
        posts = Post.objects.all()
    return render(
        request, 'index.html',
        {'user_profile': user_profile, 'posts': posts, "profile_url": profile_url,
         'post_image_urls': image_urls})


def about(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Compose the email subject and body
        subject = f"New contact form submission from {username}"
        body = f"Name: {username}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage:\n{message}"

        # Send the email using the send_mail function
        send_mail(subject, body, email, ['help@uniaway.it'])

    return render(request, 'contact.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('host_landing')
