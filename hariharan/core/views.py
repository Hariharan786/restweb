from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    # example food list
    foods = [
        {'name': 'Biryani', 'image': 'menu/biryani.jpg'},
        {'name': 'Pizza', 'image': 'menu/pizza.jpg'},
        {'name': 'Pasta', 'image': 'menu/pasta.jpg'},
        # add up to 12 ...
    ]
    return render(request, 'menu.html', {'foods': foods})

def admin_view(request):
    # team members list
    team = [
        {'name': 'Raj', 'role': 'Head Chef', 'image': 'team/raj.jpg'},
        {'name': 'Anjali', 'role': 'Manager', 'image': 'team/anjali.jpg'},
        # add 4 more ...
    ]
    return render(request, 'administration.html', {'team': team})

def contact_view(request):
    contact_info = {
        'address': '123 Spice Street, Chennai City',
        'phone': '+91-9876543210',
        'email': 'contact@spicedelight.com',
    }
    return render(request, 'contact.html', {'contact': contact_info})
