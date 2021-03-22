from django.shortcuts import render

def index(request):
    """The Home Page"""
    return render(request, 'tcg_cards/index.html')

def overview(request):
    """Overviews for Cards"""
    return render(request, 'tcg_cards/overview.html')

def totals(request):
    """Totals page for tcg_cards"""
    return render(request, 'tcg_cards/totals.html')

def gen1(request):
    """Gen1 page for tcg_cards"""
    return render(request, 'tcg_cards/gen1.html')

def gen2(request):
    """Gen2 page for tcg_cards"""
    return render(request, 'tcg_cards/gen2.html')

def gen3(request):
    """Gen3 page for tcg_cards"""
    return render(request, 'tcg_cards/gen3.html')

def gen4(request):
    """Gen4 page for tcg_cards"""
    return render(request, 'tcg_cards/gen4.html')

def gen5(request):
    """Gen5 page for tcg_cards"""
    return render(request, 'tcg_cards/gen5.html')

def gen6(request):
    """Gen6 page for tcg_cards"""
    return render(request, 'tcg_cards/gen6.html')

def gen7(request):
    """Gen7 page for tcg_cards"""
    return render(request, 'tcg_cards/gen7.html')

def gen8(request):
    """Gen8 page for tcg_cards"""
    return render(request, 'tcg_cards/gen8.html')

