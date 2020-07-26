from django.shortcuts import render, get_object_or_404
from .models import Meeting


def detail(request, id):
    print(90 * "-")
    meeting = get_object_or_404(Meeting, pk=10)
    print(request)
    print(id)
    print(90 * "-")
    return render(request, "meetings/detail.html", {"meeting": meeting})
