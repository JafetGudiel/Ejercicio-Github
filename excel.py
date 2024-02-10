from openpyxl import Workbook
from openpyxl.styles import Font
import time

libro = Workbook()
sheet = libro.active

sheet["A1"] = 5
sheet["A2"] = 10

sheet["B1"] = "Rango"
sheet["B1"].font = Font(bold=True)
for i in range(1, 15):
    sheet[f'B{i}'] = i**1


libro.save("Prueba_escritura.xlsx")
