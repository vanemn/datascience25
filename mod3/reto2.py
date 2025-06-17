import statistics as stats

def balancear_reaccion(coeficientes):
    if len(coeficientes) < 4:
        return "Lista de coeficientes inválida."
    
    reactivos = sum(coeficientes[:len(coeficientes)//2])
    productos = sum(coeficientes[len(coeficientes)//2:])
    
    if abs(reactivos - productos) < 0.01:
        return f"Reacción balanceada. Media: {stats.mean(coeficientes):.2f}"
    else:
        return "Reacción no balanceada."


coeficientes = [2, 1, 1, 2]  
print(balancear_reaccion(coeficientes))  