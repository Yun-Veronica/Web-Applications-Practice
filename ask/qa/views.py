# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext
from ask.qa.models import Question, QuestionManager
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    # response_body = b'Answer is 42'.encode('utf-8')
    return HttpResponse('Answer is 42', headers={'Content-Type': 'text/plain', 'status_code': 200})


def handler404(request, *args, **argv):
    response = render('templates/404.html', {}, context=RequestContext(request))
    response.status_code = 404
    return response


def question_page(request,page_id):
    'Example: URL = /question/5/'
    try:
        id = request.GET.get('id')
        question = Question.objects.get(pk=page_id)
    except Question.objects.DoesNotExist():
        raise Http404
    return render(request, 'qa/question_page_pattern.html', {'posts': question, })


def main_page(request):
    'Example: URL = /?page=2'
    '''Главная страница. Список "новых" вопросов.
     Т.е. последний заданный вопрос - первый в списке. 
     Необходимо использовать метод new менеджера QuestionManager.
     На этой странице должна работать пагинация. Номер страницы указывается в GET параметре page. 
    На страницу выводится по 10 вопросов.
    В списке вопросов должны выводится заголовки (title) вопросов и ссылки на страницы отдельных вопросов.'''
    # Постраничное    отображение
    posts = Question.objects.new()
    try:
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page')
        paginator = Paginator(posts, limit)
        paginator.base_url = '/?page='
        page = paginator.page(page)  # Page
    except posts.DoesNotExist():
        raise Http404
    return render(request, 'qa/main_page.html', {posts: page.object_list, paginator: paginator, page: page, })


def popular_pages(request, page_id, *args, **kwargs):
    'Example: URL = /popular/?page=3'
    '''Cписок "популярных" вопросов. 
    Сортировка по убыванию поля rating. 
    Необходимо использовать метод popular менеджера QuestionManager. 
    На этой странице должна работать пагинация. Номер страницы указывается в GET параметре page.  
    На страницу выводится по 10 вопросов.
    В списке вопросов должны выводится заголовки (title) вопросов и ссылки на страницы отдельных вопросов.'''
    try:
        posts = Question.objects.popular()
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', page_id)
        paginator = Paginator(posts, limit)
        paginator.base_url = '/popular/?page='
        page = paginator.page(page)

    except Question.objects.DoesNotExist():
        raise Http404
    return render(request, 'qa/main_page.html', {posts: page.object_list, paginator: paginator, page: page, })

# Base view  as example
# Model - model name of  app (example)
#
# # from django.http import Http404
# # from django.shortcuts import render
# #
# # def post_details(request, slug):
# #     try:
# #         post = Model.objects.get(slug=slug)
# #     except Model.DoesNotExist:
# #         raise Http404
# #     return render(request, 'blog/post_details.html', {'post': post})
#
# Same simple example, but through the use of django.shortcuts
# # from django.shortcuts import render, get_object_or_404
# # from django. views.decorators. http import require_GET
# # @require_GET
# # def post_details(request, slug):
# #     post = get_object_or_404(Model, slug=slug)
# #     return render(request, 'blog/post_details.html', { 'post':post })
#
