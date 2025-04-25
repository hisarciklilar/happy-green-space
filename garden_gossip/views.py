from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gossip_corner(request):
    return HttpResponse("Welcome to the Garden Gossip Corner! Share your gardening tips and tricks here.")