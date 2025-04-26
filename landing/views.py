from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):   return HttpResponse("Happy Green Space is a platform targeting allotment users, although people who do gardening may also use it. It is a platform where users can share their experiences, and learn about gardening. The platform aims to create a community of gardening enthusiasts who can connect and share their knowledge.")