
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    # example food list
    foods = [
        {'name': 'Biryani', 'image': 'menu/bir.jpg'},
        {'name': 'Pizza', 'image': 'menu/pizza.jpg'},
        
        {'name': 'Burger', 'image': 'menu/burger.jpg'},
        {'name': 'Dosa', 'image': 'menu/dosa.jpg'},
        {'name': 'Parotta', 'image': 'menu/parrota.jpg'},
        {'name': 'Chicken gravy', 'image': 'menu/gravy.jpg'},
        {'name': 'Meals', 'image': 'menu/meals.jpg'},
        {'name': 'Vareity Rice', 'image': 'menu/rice.jpg'},
        {'name': 'Naan', 'image': 'menu/naan.jpg'},
        {'name': 'Butter Chicken', 'image': 'menu/butter.jpg'},
        {'name': 'Roti', 'image': 'menu/roti.jpg'},
        {'name': 'Ice Cream', 'image': 'menu/icecream.jpg'},
        {'name': 'Pani puri', 'image': 'menu/pani.jpg'},
        
    ]
    return render(request, 'menu.html', {'foods': foods})

def admin_view(request):
    # team members list
    team = [
        {'name': 'Raj', 'role': 'Owner', 'image': 'team/raj.jpg'},
        {'name': 'Anjali', 'role': 'Head Chef', 'image': 'team/anjali.jpg'},
        {'name': 'Balaji', 'role': 'Manager', 'image': 'team/balaji.jpg'},
        {'name': 'Seema', 'role': 'Chef', 'image': 'team/seema.jpg'},
        {'name': 'Kumar', 'role': 'Chef', 'image': 'team/kumar.jpg'},
        {'name': 'Ravi', 'role': 'Chef', 'image': 'team/ravi.jpg'},
    
    ]
    return render(request, 'administration.html', {'team': team})

def contact_view(request):
    contact_info = {
        'address': '123 Spice Street, Chennai City',
        'phone': '+91-9876543210',
        'email': 'contact@spicedelight.com',
    }
    return render(request, 'contact.html', {'contact': contact_info})
