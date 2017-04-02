from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,TemplateView
from rest_framework import views 
import rest_framework.response as rest
from django.core import serializers
from .models import Post, Blog
import json
from ast import literal_eval

class NetworkJSON(views.APIView):

    def get(self, request):

        def get_tags():
            tags = Post.objects.values('tags_1').distinct() 
            ret_dict = {}
            for i in range(len(tags)):
                try:
                    t = tags[i]['tags_1'][0]
                except:
                    t = 'None'
                ret_dict[t] = i
                i += 1
            return ret_dict

        queryset = Post.objects.filter(published=True)
        nodes = []
        links = []
        tag_dict = get_tags()

        for post in queryset:           
            #if type(post.tags_1) == 'list':
            try:
                x = str(post.tags_1[0])
                node_dict = {'name': post.title, 'group': tag_dict[x], 'extra_tags':str(post.tags_1)}
                
            except:
                #else:
                node_dict = {'name': post.title, 'group': 99}

            nodes.append(node_dict)
        n1_counter = 0
        for n1 in nodes:
            tag = n1['group']
            name = n1['name'] 
            if tag != 99:
                n1_list = literal_eval(n1['extra_tags'])
                n2_counter = 0
                for n2 in nodes:
                    n2_list = literal_eval(n2['extra_tags'])
                    if any(map(lambda v: v in n2_list, n1_list)) and name != n2['name']:
                    #tag == n2['group'] and name != n2['name']:
                        link = {'source':n1_counter, 'target':n2_counter, 'value':1}
                        links.append(link)
                    n2_counter +=1
            n1_counter += 1 
                         

        data = {'links': links,'nodes':nodes}
        return rest.Response(data)
    #serializers.serialize('json',data)

class NetworkView(TemplateView):
    context_object_name = 'network_view'
    template_name = 'main/network_graph.html'

class RidesharingMap(TemplateView):
    context_object_name = 'rideshare_view'
    template_name = 'main/seattle_viz.html'

    def get_context_data(self, **kwargs):
        context = super(RidesharingMap,self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, slug='colins_blog' )
        return context

class IndexView(ListView):
    context_object_name = 'index_view'
    template_name = 'main/index.html'
    queryset = Post.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, slug='colins_blog' )
        context['posts'] = Post.objects.filter(published=True)
        return context

class PostView(TemplateView):
    context_object_name = 'post_view'
    template_name = 'main./post.html'

    def get_context_data(self, slug, **kwargs):
        context = super(PostView,self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, slug='colins_blog' )
        context['post'] = get_object_or_404(Post, slug=slug)
        return context

class AboutView(TemplateView):
    context_object_name = 'about_view'
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView,self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, slug='colins_blog' )
        return context

""""
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    blog = get_object_or_404(Blog, slug='colins_blog' )
    return render(request, 'main/post.html', {'post': post})


get_object_or_404(Blog, slug='colins_blog' )

Blog.objects.filter(slug='colins_blog')[0]
def index(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'main/index.html', {'posts': posts})

def about(request, slug):
    blog = get_object_or_404(Blog, slug=tag)
    return render(request, 'main/about.html', {'blog:': blog})
 
    except Blog.DoesNotExist:
        raise Http404("About does not exist")

def about(request):
    blog = get_object_or_404(Blog, slug ='colins_blog')
    context = {'blog:': blog}
    return render(request, 'main/about.html', context)

"""
