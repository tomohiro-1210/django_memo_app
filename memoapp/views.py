from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import MemoModel
from django.urls import reverse_lazy


# Create your views here.
def memo(request):
    HttpResponse('ミミック')
    
# 一覧
class TodoList(ListView):
    template_name = 'list.html'
    model = MemoModel
    
# 詳細
class TodoDetails(DetailView):
    template_name = 'detail.html'
    model = MemoModel
    
# 登録
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = MemoModel
    # フォームに表示するデータ
    fields = ('title', 'memo', 'priority' ,'duedate')
    success_url = reverse_lazy('list')
    
# 削除
class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = MemoModel
    success_url = reverse_lazy('list')

# 更新
class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = MemoModel
    # フォームに表示するデータ
    fields = ('title', 'memo', 'priority' ,'duedate')
    success_url = reverse_lazy('list')    