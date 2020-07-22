from rest_framework import status  #status=status.HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import BlogPost
from account.models import Account

from blog.api.serializers import BlogPostSerializer


@api_view(['GET',])
def api_blog_detail_view(request,slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug) #fetch the blog post
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogPostSerializer(blog_post) #serialize it,now our data is ready in json,xml format
    return Response(serializer.data)    #return the response

@api_view(['GET','PUT',])
def api_blog_update_view(request,slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogPostSerializer(blog_post,data=request.data)
    data ={}
    if serializer.is_valid():
        serializer.save()
        data['success'] ='update successful'
        return Response(data=data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE',])
def api_blog_delete_view(request,slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = blog_post.delete()
    data ={}
    if operation:
        data['success'] ='delete successful'
    else:
        data['failure'] ='delete failed'

    return Response(data=data)
  


@api_view(['POST',])
def api_blog_create_view(request):
    account = Account.objects.get(pk=1)#query about a random user
    print(account)
    blog_post = BlogPost(author=account)#pass the author to BlogPost since it is a required field

    if request.method =='POST':
        serializer = BlogPostSerializer(blog_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





  







