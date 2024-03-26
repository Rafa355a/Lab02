from django.shortcuts import render

def formulario_cilindro(request):
    return render(request, 'cilindro/formulario_cilindro.html')

def calcular_volumen(request):
    if request.method == 'POST':
        altura = float(request.POST.get('altura', 0))
        diametro = float(request.POST.get('diametro', 0))
        radio = diametro / 2
        volumen = 3.14159 * radio**2 * altura

        context = {
            'altura': altura,
            'diametro': diametro,
            'volumen': volumen,
        }
        return render(request, 'cilindro/resultado.html', context)
    return render(request, 'cilindro/formulario_cilindro.html')
