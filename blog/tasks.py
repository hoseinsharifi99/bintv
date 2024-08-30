from celery import shared_task
from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post, User, Rating

@shared_task(rate_limit='1/s')
def process_rating(post_id, user_id, score):
    post = get_object_or_404(Post, id=post_id)
    user = get_object_or_404(User, id=user_id)

    rating, created = Rating.objects.get_or_create(post=post, user=user)
    lastScore = rating.score
    rating.score = score

    if not created:
        post.sumRate += score - lastScore
    else:
        post.sumRate += score
        post.sumVote += 1

    rating.save()
    post.save()

    return {
        'status': 'success',
        'average_rating': post.average_rating(),
        'ratings_count': post.ratings_count()
    }

def check_task_status(request, task_id):
    task = AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return JsonResponse({'status': 'success', 'result': task.result})
    elif task.state == 'PENDING':
        return JsonResponse({'status': 'pending'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Task failed'})