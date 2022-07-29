from django.shortcuts import render,redirect
from .models import contact_me,Post
from .forms import insertdata
# Create your views here.
from django.views import generic
from django.shortcuts import get_object_or_404




def firstpage(request ):
    return render(request, 'firstpage.html')

def contact_me(request):
    if request.method == "POST":
        form = insertdata(request.POST)
        if form.is_valid():#The is_valid() method is used to perform validation for each field of the form, it is defined in Django Form class. It returns True if data is valid and place all data into a cleaned_data attribute.
            f=form.save(commit=False)
            f.save()
        else:
            form.errors
    else:
        form = insertdata()
    return render(request, 'form.html', {'form': form})
    
def mywork(request ):
    return render(request, 'mywork.html')

def blog(request ):
    return render(request, 'base.html')


def aboutus(request ):
    return render(request, 'aboutus.html')

def index(request ):
    return render(request, 'index.html')


def postdetai(request ):
    return render(request, 'post_details.html')
# def PostDetail(request,slug):
#     context={}
#     try:
#             postobj=Post.objects.filter(slug=slug).first()
#             context['postobj'] = postobj
#     except Exception as e:
#             print(e)

#     return render(request, 'post_details.html',context)
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_details.html'

def post_Detail(request, slug):
    post= Post.objects.filter(slug=slug).first()
    # return HttpResponse(f"You are viewing {slug}")
    return render(request, 'post_details.html',{'post':post})

# class PostList(generic.ListView):
#     queryset = Post.objects.all().order_by('-created_on')
#     template_name = 'index.html'

def frontpage(request):
	posts = Post.objects.all()

	return render(request, 'index.html', {'posts': posts})
    
