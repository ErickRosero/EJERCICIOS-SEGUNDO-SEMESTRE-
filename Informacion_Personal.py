# Diccionario
informacion_personal = {
'nombre':'Erick Rosero',
'edad':23,
'ciudad':'Pichincha',
'provincia':'Quito',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Quito'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Militar/ Estudiante Universitario'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0995958878'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)