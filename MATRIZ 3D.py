# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 63},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 47},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 67},
            {"day": "Martes", "temp": 84},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 69},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 69},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 78}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 59},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 70},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 69}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 97},
            {"day": "Martes", "temp": 60},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 89}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 90},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 58},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 87}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 86},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 60}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad = no_ciudad + 1
    print(f'CIUDAD No. {no_ciudad}')
    no_semana = 0
    suma_promedio = 0
    for semana in ciudad:
        no_semana += 1
        suma = 0
        for dia in semana:
            suma = suma + dia['temp']
        promedio = round(suma / len(semana), 1)
        suma_promedio += promedio
        print(f'El promedio semana No. {no_semana} es: {promedio}')
    promedio_ciudad = round(suma_promedio / len(ciudad), 1)
    print(f'El promedio mensual es: {promedio_ciudad}')