alumno_1 = ['Ernesto', 'Saldivar', 'Martinez', 60, 70, 73, 90]
alumno_2 = ['Ana', 'Garcia', 'Lopez', 85, 92, 78, 88]
alumno_3 = ['Carlos', 'Rodriguez', 'Perez', 70, 65, 75, 80]
alumno_4 = ['Sofia', 'Martinez', 'Gomez', 95, 85, 90, 92]
alumno_5 = ['Luis', 'Perez', 'Sanchez', 78, 80, 88, 82]

alumnos = [alumno_1, alumno_2, alumno_3, alumno_4, alumno_5]

headers = ['Nombre', 'Apellido P', 'Apellido M', 'POO', 'SYSP', 'LDI', 'DAM','PROMEDIO']

for alumno in alumnos:
    prom = sum(alumno[3:]) / len(alumno[3:])
    alumno.append(prom)
    
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, alumno)]
    
    header_format = ' | '.join('{{:<{}}}'.format(length) for length in max_lengths)
    print(header_format.format(*headers))
    print('-' * sum(max_lengths) + ' ' + '-' * (len(headers) - 1) * 3)
    
    data_format = ' | '.join('{{:<{}}}'.format(length) for length in max_lengths)
    print(data_format.format(*alumno))
    print('Promedio:', prom)
    print()
