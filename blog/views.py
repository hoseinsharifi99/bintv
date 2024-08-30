from celery.result import AsyncResult
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Rating
from .serializers import PostSerializer, RatingSerializer
from django.core.cache import cache
from .tasks import process_rating

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_protect
    @csrf_exempt
    def create_post(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            sumRate = 0
            sumVote = 0

            post = Post.objects.create(title=title, content=content, sumRate=sumRate, sumVote=sumVote)

            json = JsonResponse({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'sumRate': post.sumRate,
                'sumVote': post.sumVote,
            })
            return json

    def get_queryset(self):
        cachedPosts = cache.get('posts')
        if cachedPosts is None:
            cache.set('posts',Post.objects.all().order_by('-id'), timeout=30)
            cachedPosts = cache.get('posts')

        return cachedPosts


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @csrf_protect
    @csrf_exempt
    def submit_rating(request):
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            user_id = request.POST.get('user_id')
            score = int(request.POST.get('score'))

            # Queue the task
            task = process_rating.delay(post_id, user_id, score)

            return JsonResponse({'status': 'queued', 'task_id': task.id})
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


