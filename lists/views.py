from django.shortcuts import render


def home_page(request):
    # files in ./templates
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
