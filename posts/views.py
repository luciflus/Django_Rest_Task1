import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import Tweet, Comment, Mark

@csrf_exempt
def create_tweet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Tweet.objects.create(**data)
        json_data = {
            "title": new_tweet.title,
            "body": new_tweet.body,
            "author": new_tweet.author
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'title': tweet.title,
                    'body': tweet.body,
                    'author': tweet.author
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)

@csrf_exempt
def create_comments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_comment = Comment.objects.create(**data)
        json_data = {
            "title": new_comment.title,
            "text": new_comment.text,
            "tweet_id": new_comment.tweet_id
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        comments = Comment.objects.all()
        data = []
        for comment in comments:
            data.append(
                {
                    "title": comment.title,
                    "text": comment.text,
                    "tweet_id": comment.tweet_id
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def create_marks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_mark = Mark.objects.create(**data)
        json_data = {
            "mark_value": new_mark.mark_value,
            "tweet_id": new_mark.tweet_id
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        marks = Mark.objects.all()
        data = []
        for mark in marks:
            data.append(
                {
                    'mark_value': mark.mark_value,
                    'tweet_id': mark.tweet_id,
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)