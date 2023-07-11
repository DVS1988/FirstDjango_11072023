from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def home(request):
    text = '''<h1>"Изучаем django"</h1>
          <strong>Автор</strong>: <i>Иванов И.П.</i>'''
    return HttpResponse(text)

author ={
    "name" : "Иван",
    "middle" : "Петрович",
    "surname" : "Иванов",
    "phone" : "8-926-600-01-02",
    "email" : "vasya@mail.ru"}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

#def about(request): 
#    text = ''' Имя:  <i><b>Иван</b></i> <br>
#               Отчество:  <i><b>Петрович</b></i> <br>
#               Фамилия: <i><b>Иванов</b></i> <br>
#               Телефон: <i><b>8-926-600-01-02</b></i> <br>
#               email: <i><b>vasya@mail.ru</b></i>
#    '''
#    return HttpResponse(text)

def about(request):
    result = f'''
        Имя: <b>{author["name"]}</b><br>
        Отчество: <b>{author["middle"]}</b><br>
        Фамилия: <b>{author["surname"]}</b><br>
        телефон: <b>{author["phone"]}</b><br>
        email: <b>{author["email"]}</b><br>'''
    return HttpResponse(result)

def get_item(request, id):
    #print(f'{id =}, {type(id) = }')
    for item in items:
        if item['id'] == id:
            result = f'''
            <h2>Имя: {item['quantity']}</h2>
            <p>Количество: {item['quantity']}'''
            return HttpResponse(result)
        else:
            return HttpResponseNotFound(f'Item with id={id} not found')


def item_list(request):
    result = "<h2>Список товаров</h2><ol>"
    for item in items:
        result += f"<li>{item['name']}</li>"
    #result += '</ol>'
    return HttpResponse(result)
