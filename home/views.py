from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render

def home(request):
    peoples = [
        {'name': 'Aditya Joshi', 'age': 19},
        {'name': 'Rohit Panta', 'age': 30},
        {'name': 'Satyarthi Krishnamurthy', 'age': 25},
        {'name': 'Sandeep', 'age': 17},
        {'name': 'Pukar', 'age': 22}
    ]


    vegetables = ['Tomato', 'Potato', 'Onion', 'Carrot', 'Cabbage']
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo debitis molestiae minus architecto aut accusamus alias quidem fugiat cupiditate dolorum, repellendus totam at ea voluptatem veritatis? Exercitationem id culpa optio recusandae blanditiis excepturi facilis, tenetur porro. Optio cum, odit labore quaerat possimus ad odio alias expedita aperiam iste amet, hic soluta similique fugit error ab aliquam ut, et accusantium! Ducimus a ea libero laborum distinctio excepturi consectetur magnam tempore. Cum vel est autem ratione adipisci? Repellat nemo alias reiciendis sint fugit inventore ut. Adipisci possimus exercitationem ducimus asperiores et soluta. Voluptas eaque nostrum optio sapiente doloribus. Ipsum voluptatibus repellat sapiente!"""
    context = {'peoples': peoples, 'vegetables': vegetables, 'text': text, 'page': 'home'}
    return render(request, "index.html", context)
def success_page(request):
    return render(request, "success.html")

def about(request):
    context = {'page' : 'about'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page' : 'contact'}
    return render(request, "contact.html", context)