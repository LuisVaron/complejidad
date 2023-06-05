from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home.html')


def bkg_menu_optimo(calorias_minimas, menu_actual, platos):
    if sum(menu_actual.values()) >= calorias_minimas:
        return menu_actual, sum(menu_actual.values())

    mejor_menu = None
    mejor_diferencia = float('inf')

    for plato, calorias in platos.items():
        if plato not in menu_actual:
            nuevo_menu = menu_actual.copy()
            nuevo_menu[plato] = calorias
            resultado = bkg_menu_optimo(
                calorias_minimas, nuevo_menu, platos)

            if resultado[0] is not None:
                diferencia = abs(resultado[1] - calorias_minimas)

                if diferencia < mejor_diferencia:
                    mejor_menu = resultado[0]
                    mejor_diferencia = diferencia

    return mejor_menu, sum(mejor_menu.values())


def calorias(request):
    if request.method == 'GET':
        return render(request, 'calorias.html')
    else:
        try:
            
            plato = request.POST.getlist('plato[]')

            calorias = request.POST.getlist('calorias[]')

            calorias_m = int(request.POST['c_minimas'])

            platos = {i: int(j) for i, j in zip(plato, calorias)}

            menu = bkg_menu_optimo(calorias_m, {}, platos)

            return render(request, 'calorias.html', {
                'calorias': menu[1],
                'menu': menu[0]})
        except AttributeError:
            return render(request, 'calorias.html', {
                'error': '''<div class="alert alert-danger" role="alert">
                    El menu no cumple con el minimo de calorias.
                    </div>'''})
        except ValueError:
            return render(request, 'calorias.html', {
                'error': '''<div class="alert alert-danger" role="alert">
                    Inserta de nuevo los platos y sus calorias.
                    </div>'''})


def jueces(request):
    ancho = 2
    largo = 2   
    return render(request, 'jueces.html', {'ancho': ancho, 'largo': largo})


def conejos(request):
    return render(request, 'conejos.html')
