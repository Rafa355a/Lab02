from django.shortcuts import render

def index(request):
    context = {
        'titulo': "Calculadora",
    }
    return render(request, 'calcula/formulario.html', context)

def enviar(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    operacion = request.POST['operacion']
    resultado = None

    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2

    context = {
        'titulo': "Resultado",
        'num1': num1,
        'num2': num2,
        'operacion': operacion,
        'resultado': resultado,
    }
    return render(request, 'calcula/respuesta.html', context)
