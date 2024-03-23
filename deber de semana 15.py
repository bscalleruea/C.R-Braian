# Diccionario
informacion_personal = {
'nombre':'Braian Stiven Calle Rodriguez',
'edad':27,
'ciudad':'Armenia',
'Departamento':'Quindio',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Armenia Quindio Colombia'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Estudiante Universitario'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0982966403'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)