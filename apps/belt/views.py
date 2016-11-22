from django.shortcuts import render, redirect
from models import Quote, User
from django.contrib import messages

def session_check(request):
  if 'user' in request.session:
      return True
  else:
      return False

def index(request):
    if not session_check(request):
        return redirect('login:index')
    context = {
        "all_quotes": Quote.objects.exclude(favorites__name=request.session['user']['name']),
        'your_faves': Quote.objects.filter(favorites=request.session['user']['user_id'])
    }
    return render(request, 'belt/index.html',context)

def create_quote(request):
    if session_check(request):
        print 'i made it to create'
        print '*'*80
        errors = Quote.objects.make_quote(request)

        if errors:
            print_errors(request,errors)
            return redirect('quotes:index')

        return redirect('quotes:index')
        
    return redirect('login:index')

def show_user(request, id):
    if session_check(request):
        context = {
            'user': User.objects.get(id=id),
            'all_faves': Quote.objects.filter(favorites=id)
        }

        return render(request, 'belt/user_page.html', context)

    return redirect('login:index')

def add_fave(request, id):
    user = User.objects.get(id=request.session['user']['user_id'])
    quote = Quote.objects.get(id=id)
    quote.favorites.add(user)
    return redirect('quotes:index')

def remove_quote(request, id):
    if not session_check(request):
        return redirect('login:index')

    user = request.session['user']['user_id']
    quote = Quote.objects.get(id=id)
    quote.favorites.remove(user)
    quote.save()

    return redirect('quotes:index')

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)
