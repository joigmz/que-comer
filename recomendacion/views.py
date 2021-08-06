from django.shortcuts import render
import random

# Create your views here.
def index(request):
    comidas = {
        'desayuno' : ['1 porción de cereal tipo A',
                    '1 porción de carne baja en grasa desayuno',
                    '1 porción de lácteo'],
        'colacion' : [ '1 porción de lácteo',
                    '½ porción de alimento alto en lípidos'],

        'almuerzo' : ['1 porción de carne baja en grasa',
                    '1 porción de cereal tipo B',
                    ['1 Porción de verduras tipo A', '1 Porción de verduras tipo B']],
        'once' : ['1 porción de cereal tipo A',
                '1 porción de lácteo',
                '½ porción de alimento alto en lípidos'],

        'cena' : ['1 porción de carne baja en grasa',
                '1 porción de cereal tipo B',
                ['1 Porción de verduras tipo A', '1 Porción de verduras tipo B']]
    }

    Alimento = {
        '1 porción de cereal tipo A' : [
            '-2 rebanadas de pan molde',
            '- 1 pan pita',
            '-½ marraqueta ( 1 diente)',
            '- 3 cucharadas de avena',
            '- 3 cucharadas cereal sin azúcar',
            '-6 galletas de salvado',
            '- 50g pan hecho en casa o masa madre'
        ],
        
        '1 porción de cereal tipo B' : [
            '-100g ó ¾ taza de arroz, fideos, quínoa, cous cous (cocidos)',
            '-150g ó 1 papa',
            '-160g de choclo o arvejas',
            '- 1 fajita'
        ],

        '1 Porción de verduras tipo A' : [
            '-1 taza: lechuga (50g), repollo (50g), acelga (50g), berros, achicoria (50g), pepino (100g), zapallo italiano (100g), espinaca (50g), apio (70g), endivia (50g)',
            '-½ taza: pimentón (60g)',
            '-5 unid: rabanitos (50g)'
        ],

        '1 Porción de verduras tipo B' : [
            '-¼ taza: habas (30g)',
            '-½ taza: betarraga (90g), Bruselas (100g), zapallo camote (70g)',
            '-1 unid: tomate (120g), alcachofa (50g)',
            '-1 ½ taza: berenjena (100g)',
            '-1 taza: brócoli (100g), coliflor (110g), zanahoria(50g)',
            '-¾ taza: champiñón (100g), porotos verdes (70g)',
            '-5 unid: esparrago (100g)',
            '- 2 unid: palmitos'
        ],

        '1 porción de carne baja en grasa' : [
            '*100g:Posta, lomo liso, pollo ganso, asiento picana, pollo, pavo s/cuero, tártaro (en cocido= tamaño de la palma de la mano)',
            '-2 láminas→pechuga de pavo o pollo cocida',
            '-Legumbres en cocido: ¾ taza (150g)',
            '- Huevo: 1 entero + 1 clara',
            '- Atún en agua: ½ tarro',
            '*120g: congrio, corvina, lenguado, merluza, pejegallo, pejerrey, reineta, salmón',
            '- Jaiba: 120g',
            '- Ostras: 16 unidades',
            '- Machas: 10 unidades',
            '- Locos: 2 unidades',
            '- Choritos: 12 unidades',
            '- Camarones: 85 g'
        ],

        '1 porción de carne baja en grasa desayuno' : [
            '-2 láminas→pechuga de pavo o pollo cocida',
            '- Huevo: 1 entero + 1 clara',
            '- Atún en agua: ½ tarro'
        ],

        '1 porción de lácteo' : [
            '-Quesillo (cantidad: como el de una caja de fósforo ó 60g)',
            '- Queso cottage o ricotta: 2 cucharadas',
            '-Leche fluida o cultivada ( 1 taza: 200cc)',
            '-Yogurt ( 1 unid: 175g)'
        ],

        '½ porción de alimento alto en lípidos' : [
            '-26 unid: almendras (25g)',
            '-50 unid: avellanas (30g)',
            '-30 unid: maní SIN sal (30g)',
            '-5 unid: nuez (25g)',
            '-40 unid: pistacho (30g)',
            '-11 unid : aceitunas (115g)',
            '-3 cucharadas: palta (90g)',
            '- 30g de semillas'
        ]

    }

    recomendacion = {}
    for comida in comidas:
        recomendacion[comida] = []
        for opcion in comidas[comida]:
            if type(opcion) == type([]):
                comida_opcion = opcion[random.randint(0,len(opcion)-1)]
                recomendacion[comida].append(Alimento[comida_opcion][random.randint(0,len(Alimento[comida_opcion])-1)])
            else:
                recomendacion[comida].append(Alimento[opcion][random.randint(0,len(Alimento[opcion])-1)])

    
    

    return render(request, "index.html", {'recomendacion' : recomendacion })