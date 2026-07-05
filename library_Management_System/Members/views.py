from django.shortcuts import render, get_object_or_404
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'member_detail.html', {'member': member})