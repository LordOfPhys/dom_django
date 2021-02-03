from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from farm_shop.models import UserProfile, ItemProfile, Category, Token, ItemNews
import json

def get_data(request):
    return json.loads(request.body.decode("utf-8"))

def type_request(request):
    if request.method != 'POST':
        return True
    else:
        return False

@csrf_exempt
def login(request):
    if type_request(request):
        return  HttpResponse('500')
    data = get_data(request)
    if User.objects.filter(username=data['login']).exists() is False:
        user = User.objects.create_user(data['login'], 'TypicalEmail@mail.ru', 'TypicalPassword1')
        user.is_active = True
        user.save()
        UserProfile.objects.create(user=user)
        Token.objects.get_or_create(user=user)
        return HttpResponse(json.dumps({'token': user.auth_token.key}))
    else:
        Token.objects.get_or_create(user=User.objects.filter(username=data['login'])[0])
        return HttpResponse(json.dumps({'token': User.objects.filter(username=data['login'])[0].auth_token.key}))

@csrf_exempt
def get_news(request):
    if type_request(request):
        return HttpResponse(500)
    news_array = ItemNews.objects.all()
    mas = []
    for i in range(len(news_array)):
        item = [news_array[i], news_array[i].get_date()]
        mas.append(item)
    mas = sorted(mas, key=lambda x:x[1], reverse=True)
    i = 0
    response = []
    while i < 10 and i < len(mas):
        response.append(news_array[i].get_label())
        response.append(news_array[i].get_description())
        response.append(news_array[i].get_image().url)
        i += 1
    return HttpResponse(json.dumps({'news': response}))

@csrf_exempt
def get_news_full(request):
    data = get_data(request)
    if type_request(request):
        return HttpResponse(500)
    item = ItemNews.objects.get(label = data['label'])
    response = json.dumps({'full_news': [item.get_label(), item.get_description(), item.get_image().url]})
    return HttpResponse(response)

@csrf_exempt
def check_token(request):
    data = get_data(request)
    if type_request(request):
        return HttpResponse(500)
    answer = "No"
    if Token.objects.filter(key = data['token']).exists():
        answer = "Yes"
    return HttpResponse(json.dumps({'answer': answer}))

@csrf_exempt
def get_profile(request):
    data = get_data(request)
    if type_request(request):
        return HttpResponse(500)
    user_profile = UserProfile.objects.get(user = Token.objects.get(key = data['token']).user)
    profile = [user_profile.get_first_name(), user_profile.get_last_name(), user_profile.get_phone(), user_profile.get_adress(),
               user_profile.get_firm_type(), user_profile.get_photo().url]
    return HttpResponse(json.dumps({'profile': profile}))

@csrf_exempt
def change_profile(request):
    data = request.POST['change_body']
    file = request.FILES['image']
    data = data.split(' ')
    UserProfile.objects.get(user = Token.objects.get(key = data[0]).user).set_profile(data[1], data[2], data[5], data[6], data[3] + " " + data[4], file)
    return HttpResponse(200)

@csrf_exempt
def newsell(request):
    data = request.POST['newsell'].split(";")
    file = request.FILES['image']
    user = Token.objects.get(key = data[0]).user
    ItemProfile.objects.get_or_create(user = user, category_type = Category.objects.get(label=data[1]), label = data[2], image = file,
                                      price = float(data[3]), description = data[4])
    return HttpResponse(200)

@csrf_exempt
def change_sell(requst):
    data = requst.POST['newsell'].split(";")
    file = requst.FILES['image']
    user = Token.objects.get(key = data[0]).user
    item = ItemProfile.objects.get(user = user, label = data[5])
    item.change_item(Category.objects.get(label = data[1]), label=data[2], image=file,
                     price=float(data[3]), desc=data[4])
    return HttpResponse(200)

@csrf_exempt
def find_items(request):
    data = get_data(request)
    items = ItemProfile.objects.filter(category_type=Category.objects.get(label=data['param']))
    result = []
    for i in items:
        result.append(i.get_label())
        result.append(i.get_desc())
        result.append(i.get_image().url)
    return HttpResponse(json.dumps({'items': result}))

@csrf_exempt
def item_info(request):
    data = get_data(request)
    item = ItemProfile.objects.get(label=data['item'])
    user = UserProfile.objects.get(user=item.get_user())
    response = {'label': item.get_label(), 'user_phone': UserProfile.objects.get(user = item.get_user()).get_phone(),
                'image': item.get_image().url, 'price': item.get_price(), 'user_owner': str(item.get_user()),
                'user_name': str(user.get_first_name() + " " + user.get_last_name()),
                'user_getter': str(Token.objects.get(key = data['token']).user), 'item_id': str(item.id),
                'category': item.get_category(), 'desc': item.get_desc()}
    return HttpResponse(json.dumps(response))

@csrf_exempt
def get_list_sells(request):
    data = get_data(request)
    sells_mas = ItemProfile.objects.all()
    result = []
    for i in range(len(sells_mas)):
        if sells_mas[i].get_user() == Token.objects.get(key = data['token']).user:
            result.append(sells_mas[i].get_label())
            result.append(sells_mas[i].get_price())
            result.append(sells_mas[i].get_image().url)
    return HttpResponse(json.dumps({'listSells': result}))

