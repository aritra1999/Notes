from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.db.models import Q

from .models import Notes


def login_view(request):
    context = {
        "title": "Login",
    }
    if request.method == "POST":
        username = "oreo"
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/list/")
        else:
            return redirect("https://google.com/")
    return render(request, "notes/login.html", context)


def list_view(request):
    if request.user.is_authenticated:
        notes = Notes.objects.all().order_by('-timestamp')
        context = {
            "notes": notes,
            "title": "List",
        }
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            Notes.objects.create(title=title, description=description).save()
        return render(request, "notes/list.html", context)
    else:
        return redirect("/login/")


def edit_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get('job') == "edit":
                title = request.POST.get('title')
                description = request.POST.get('description')
                note = Notes.objects.get(title=title)
                note.description = description
                note.save()
            elif request.POST.get('job') == "delete":
                title = request.POST.get('title')
                return delete_view(request, title)
            return redirect("/list/")
    else:
        return redirect("/login/")


def search_view(request):
    if request.user.is_authenticated:
        key = request.POST.get('key')
        if key:
            results = Notes.objects.filter(
                Q(title__icontains=key) | Q(description__icontains=key) | Q(timestamp__icontains=key))
            context = {
                'results': results,
                'searched': key,
            }
            # context['results'] = results
            # context['searched'] = key
            return render(request, "notes/search.html", context)
        return redirect("/list/")
    else:
        return redirect("/login/")


def delete_view(request, title):
    if request.user.is_authenticated:
        Notes.objects.filter(title=title).delete()
        return redirect("/list/")
    return redirect("/login/")
