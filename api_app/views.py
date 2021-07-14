# from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Post
from datetime import date, datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def validator(data):
    errors = []
    if data.get('title'):
        title = data.get('title')
        if len(title) < 20:
            errors.append({
                "title": "title minimal 20 karakter"
            })
    else:
        errors.append({"title": "title harus diisi"})

    if data.get('content') :
        content = data.get('content')
        if len(content) < 200:
            errors.append({"content": "content minimal 200 karakter"})
    else:
        errors.append({'content': 'content harus diisi'})

    if data.get('category'):
        category = data.get('category')
        if len(category) < 3:
            errors.append({"category": "category minimal 3 karakter"})
    else:
        errors.append({"category": "category harus diisi"})

    if data.get('status'):
        status = data.get('status')
        if status not in ['publish', 'draft', 'thrash']:
            errors.append({"status": "status harus memilih antara publish, draft, atau thrash"})
    else:
        errors.append({"status": 'status harus diisi'})

    return errors

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Article(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))

        # errors = validator(data)
        # if errors:
        #     data = {
        #         'error': errors
        #     }
        #     return JsonResponse(data, status=500)
        
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        status = data.get('status')

        post_data = {
            'title': title,
            'content': content,
            'category': category,
            'created_date':  datetime.now(),
            'updated_date': datetime.now(),
            'status': status
        }

        post_item = Post.objects.create(**post_data)

        data = {
            'message': f'New item added to post with id: {post_item.id}'
        }

        return JsonResponse(data, status=201)

    def get(self, request, limit, offset):
        items_count = Post.objects.count()
        items = Post.objects.all()

        items_data = []
        for item in items[offset:(offset+limit)]:
            items_data.append({
                'id': item.id,
                'title': item.title,
                'content': item.content,
                'category': item.category,
                'status': item.status
            })

        data = {
            'items': items_data,
            'count': items_count
        }

        return JsonResponse(data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ArticleById(View):
    def get(self, request, item_id):
        item = Post.objects.get(id=item_id)

        data = {
            'title': item.title,
            'content': item.content,
            'category': item.category,
            'status': item.status    
        }

        return JsonResponse(data, status=200)

    def post(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))

        errors = validator(data)
        if errors:
            data = {
                'error': errors
            }

            return JsonResponse(data, status=500)


        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        status = data.get('status')

        item = Post.objects.get(id=item_id)
        item.title = title,
        item.content = content,
        item.category = category,
        item.status = status,
        item.updated_date = datetime.now()
        item.save()

        data = {
            'message': f'Item with id {item.id} has been updated'
        }

        return JsonResponse(data, status=200)

    def delete(self, request, item_id):
        item = Post.objects.get(id=item_id)
        item.status = 'thrash'
        item.save(update_fields=['status'])

        data = {
            'message': f'item with id {item.id} has been deleted'
        }

        return JsonResponse(data, status=200)