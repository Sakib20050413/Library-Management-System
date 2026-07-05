from django.shortcuts import render, get_object_or_404
from .models import BorrowRecord

def borrowing_list(request):
    records = BorrowRecord.objects.all()
    return render(request, 'borrowing.html', {'records': records})

def borrowing_detail(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk)
    return render(request, 'borrowing_detail.html', {'record': record})