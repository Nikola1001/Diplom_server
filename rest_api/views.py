from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Process
from .serializers import ProcessSerializer


class ProcessView(APIView):
    def get(self, request):
        articles = Process.objects.all()
        serializer = ProcessSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get("article")
        # Create an article from the above data
        serializer = ProcessSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Process '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Process.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ProcessSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Process '{}' updated successfully".format(article_saved.title)
        })




class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'status_auth': "access successful"
        })