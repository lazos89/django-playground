from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(["GET", "POST"])
def article_list_create_api_view(request):

    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(request, pk):
    print("article_detail_api_view")
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        print("DoesNotExist")
        return Response(
            {"error": {"code": 404, "message": "Article not found!"}},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        print("GET")
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    if request.method == "PUT":
        print("PUT")
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            print("is_valid")
            serializer.save()
            return Response(serializer.data)
        print("is_not_valid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        print("DELETE")
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
