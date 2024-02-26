from django.shortcuts import render, redirect
from app.models import Food, Consume


# Displaying our model items
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']  # Getting the data from the post request
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:  # Consumed by user and saved
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'app/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete(request, id):  # Don't forget to pass the id of what you want to delete
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    else:
        return render(request, 'app/delete.html')


