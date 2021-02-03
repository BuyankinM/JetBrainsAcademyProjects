from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        todos = request.POST.get('todo')
        important = request.POST.get('important')
        if todos not in self.all_todos:
            if important == "false":
                self.all_todos.append(todos)
            else:
                self.all_todos.insert(0, todos)
        return redirect('/')