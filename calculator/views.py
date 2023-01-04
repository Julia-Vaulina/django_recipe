from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe_omlet(request):
    recipe = {}
    serving = int(request.GET.get("servings", 1))
    for item, key in DATA['omlet'].items():
        recipe[item] = round(float(float(key) * serving), 2)
    context = {'recipe': recipe}
    return render(request, f'calculator/omlet.html', context)

def recipe_pasta(request):
    recipe = {}
    serving = int(request.GET.get("servings", 1))
    for item, key in DATA['pasta'].items():
        recipe[item] = round(float(float(key) * serving), 2)
    context = {'recipe': recipe}
    return render(request, f'calculator/pasta.html', context)

def recipe_buter(request):
    recipe = {}
    serving = int(request.GET.get("servings", 1))
    for item, key in DATA['buter'].items():
        recipe[item] = round(float(float(key) * serving), 2)
    context = {'recipe': recipe}
    return render(request, f'calculator/buter.html', context)


def home_view(request):
    template_name = 'calculator/index.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)