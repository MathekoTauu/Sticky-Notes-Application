from django.shortcuts import render, redirect
from .models import StickyNote
from django.shortcuts import render

def home(request):
    return render(request, 'notes/home.html')

def note_list(request):
    notes = StickyNote.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        StickyNote.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'notes/note_form.html')

def note_update(request, pk):
    note = StickyNote.objects.get(pk=pk)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'note': note})

def note_delete(request, pk):
    note = StickyNote.objects.get(pk=pk)
    note.delete()
    return redirect('note_list')