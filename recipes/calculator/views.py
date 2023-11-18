from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

DATA = {
    'omlet': {
        'ingredients': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        }    
    },
    'pasta': {
        'ingredients': {
            'макароны, г': 0.3,
            'сыр, г': 0.1,
        }
    },
    'buter': {
        'ingredients': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        }
    },
}

class RecipeView(View):
    def get(self, request, recipe_name):
        servings = int(request.GET.get('servings', 1))
        recipe = DATA.get(recipe_name)
        if recipe is None:
            return HttpResponse('Рецепт не найден', status=404)
    
        ingredients = recipe.get('ingredients')
        if ingredients is None:
            return HttpResponse('Отсутствуют ингредиенты для рецепта', status=404)
    
        response_data = {}
        for ingredient, quantity in ingredients.items():
            response_data[ingredient] = quantity * servings
    
        context = {'recipe': response_data}
        return render(request, 'calculator/index.html', context)