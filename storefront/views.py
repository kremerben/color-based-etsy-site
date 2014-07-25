import json
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from models import Item


def home(request):
    items = Item.objects.all()
    data = {
        'items': items,
    }
    return render(request, 'etsy_base.html', items)

@csrf_exempt
def new_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # if data['runtime'] == "":
        #     runtime = 10
        # else:
        #     runtime = data['runtime']
        # poster = data['poster'].replace('tmb', 'det')
        item_info = {
            'item_info': {
            'title': data['title'],
            'etsy_id': data['etsy_id'],
            'image_url': data['image_url'],
            'price': data['price'],
            'listing_url': data['listing_url'],
            'category_path': data['category_path'],
            'tags': data['tags'],
            'style': data['style'],
            'description': data['description'],
            'etsy_color': data['etsy_color']
            },
        }
        # movie_info = [movie_info]
        # return HttpResponse(json.dumps(movie_info), content_type='application/json')
        return render_to_response('item_template.html', item_info)





def user_favorites(request):
    pass

def store(request, store_id):
    pass