import pandas as pd

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
temperaturas = [20, 22, 19, 21, 23]

df = pd.DataFrame({
    "Día": dias,
    "Temperatura": temperaturas
})
print("\nDataFrame de días y temperaturas:\n", df)




#forma con series

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
temperaturas = [20, 22, 19, 21, 23]

serie = pd.Series(data=temperaturas, index=dias)

print("\nTemperaturas por día:\n", serie)