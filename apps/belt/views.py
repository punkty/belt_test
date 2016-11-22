from django.shortcuts import render


def session_check(request):
  if 'user' in request.session:
      return True
  else:
      return False

def index(request):
    if not session_check(request):
        return redirect('login:index')
    return render(request, 'belt/index.html')