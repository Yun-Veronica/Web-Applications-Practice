# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext
from qa.models import Question, QuestionManager
from django.core.paginator import Paginator
from django.template import loader


def test(request, *args, **kwargs):
    # response_body = b'Answer is 42'.encode('utf-8')
    return HttpResponse('Answer is 42', headers={'Content-Type': 'text/plain', 'status_code': 200})


def handler404(request, *args, **argv):
    response = render('templates/404.html', {}, context=RequestContext(request))
    response.status_code = 404
    return response


def question_page(request):
    try:
        id = request.GET.get('id')
        question = Question.objects.get(pk=id)
    except :
        raise Http404
    return render(request, 'question_page_pattern.html', {'posts': question, })


def main_page(request):
    posts = Question.objects.new()
    try:
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page')
        paginator = Paginator(posts, limit)
        template = loader.get_template('main_page.html')
        paginator.base_url = '/?page='
        page = paginator.page(page)  # Page
    except :
        raise Http404(Exception)
    return render(request, 'popular_questions_page.html', {'posts': page.object_list, 'paginator': paginator, 'page': page, })
    # return HttpResponse(
    #     template.render({'posts': page.object_list, 'paginator': paginator, 'page': page, 'request': request}))


def popular_pages(request, *args, **kwargs):
    page_num = request.GET.get('page')
    try:
        page_num=request.split('/')[1]
        posts = Question.objects.popular()
        limit = request.GET.get('limit', 10)
        page = request.GET.get(1)
        paginator = Paginator(posts, limit)
        paginator.base_url = '/popular/?page='
        page = paginator.page(page)

    except :
        raise Http404(page_num)

    return render(request, 'popular_questions_page.html', {'posts': page.object_list, 'paginator': paginator, 'page': page, })

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
