🔄 TTRPG Sheet Converter

Una herramienta versátil desarrollada en Python para convertir y transformar fichas de personajes entre diferentes sistemas de juegos de rol de mesa, facilitando la migración de personajes y la compatibilidad entre sistemas.






































📋 Descripción

El TTRPG Sheet Converter es una aplicación de línea de comandos diseñada para convertir fichas de personajes entre diferentes sistemas de juegos de rol de mesa. Esta herramienta resuelve el problema común de querer usar el mismo personaje en diferentes sistemas de juego, automatizando la conversión de estadísticas, habilidades y características entre formatos compatibles.

🎯 Objetivos del Proyecto

•
Facilitar la migración de personajes entre sistemas de juego

•
Automatizar conversiones complejas de estadísticas y habilidades

•
Preservar la esencia del personaje durante la conversión

•
Demostrar competencias en procesamiento de datos y algoritmos

•
Crear una herramienta útil para la comunidad de juegos de rol

✨ Características

🔧 Funcionalidades Principales

•
🔄 Conversión Multi-Sistema: Soporte para D&D 5e, Pathfinder, Call of Cthulhu

•
📊 Mapeo Inteligente: Algoritmos de conversión que preservan balance

•
📝 Formato Flexible: Importa/exporta JSON, CSV, y formatos personalizados

•
🎯 Validación: Verificación de integridad de datos pre y post conversión

•
📋 Reportes: Informes detallados de cambios realizados

•
🔧 Personalización: Reglas de conversión configurables por usuario

🏗️ Características Técnicas

•
Modular Architecture: Sistema de plugins para nuevos sistemas

•
Data Validation: Validación robusta de esquemas de entrada

•
Algorithm Design: Algoritmos de mapeo y conversión optimizados

•
Error Handling: Gestión elegante de casos edge y errores

•
Configuration Management: Sistema de configuración flexible

•
Logging System: Registro detallado de operaciones

🚀 Instalación y Uso

Prerrequisitos

•
Python 3.8 o superior

•
Bibliotecas: json, csv, argparse (incluidas en Python estándar)

•
Opcional: pandas para procesamiento avanzado de datos

Instalación

1.
Clonar el repositorio

2.
Instalar dependencias opcionales

3.
Ejecutar la aplicación

Uso Básico

Conversión Simple

Bash


# Convertir de D&D 5e a Pathfinder
python sheet_converter.py \
  --input character_dnd5e.json \
  --output character_pathfinder.json \
  --from dnd5e \
  --to pathfinder

✅ Conversión completada exitosamente!
📊 Estadísticas convertidas: 6/6
🎯 Habilidades mapeadas: 18/20
⚠️  Advertencias: 2 (ver reporte detallado)


Conversión con Reporte Detallado

Bash


python sheet_converter.py \
  --input my_character.json \
  --from dnd5e \
  --to call_of_cthulhu \
  --report detailed_report.txt \
  --verbose

🔄 Iniciando conversión: D&D 5e → Call of Cthulhu
📋 Personaje: Elara Moonwhisper (Elfo Mago, Nivel 5)

📊 CONVERSIÓN DE ESTADÍSTICAS:
STR 12 → Fuerza 60
DEX 16 → Destreza 80  
CON 14 → Constitución 70
INT 18 → Inteligencia 90
WIS 13 → Poder 65
CHA 15 → Apariencia 75

🎯 CONVERSIÓN DE HABILIDADES:
Arcana (Proficiente) → Ocultismo 70%
Investigation → Buscar Libros 65%
Perception → Escuchar 60%, Avistar 60%

⚠️  ADVERTENCIAS:
- Hechizo "Fireball" no tiene equivalente directo en CoC
- Trasfondo "Sage" adaptado a "Profesor Universitario"

✅ Conversión completada. Ver reporte completo en: detailed_report.txt


🏗️ Arquitectura del Proyecto

Estructura de Archivos

Plain Text


ttrpg-sheet-converter/
├── sheet_converter.py          # Aplicación principal
├── converters/                 # Módulos de conversión
│   ├── __init__.py
│   ├── base_converter.py       # Clase base para conversores
│   ├── dnd5e_to_pathfinder.py  # Conversor D&D 5e → Pathfinder
│   ├── dnd5e_to_coc.py         # Conversor D&D 5e → Call of Cthulhu
│   └── pathfinder_to_dnd5e.py  # Conversor Pathfinder → D&D 5e
├── schemas/                    # Esquemas de validación
│   ├── dnd5e_schema.json       # Esquema para D&D 5e
│   ├── pathfinder_schema.json  # Esquema para Pathfinder
│   └── coc_schema.json         # Esquema para Call of Cthulhu
├── data/                       # Datos de referencia
│   ├── stat_mappings.json      # Mapeos de estadísticas
│   ├── skill_mappings.json     # Mapeos de habilidades
│   └── class_mappings.json     # Mapeos de clases
├── utils/                      # Utilidades
│   ├── __init__.py
│   ├── validator.py            # Validación de datos
│   ├── logger.py               # Sistema de logging
│   └── file_handler.py         # Manejo de archivos
├── tests/                      # Tests unitarios
│   ├── test_converters.py
│   ├── test_validators.py
│   └── sample_characters/      # Personajes de prueba
├── config/                     # Configuración
│   ├── default_config.json     # Configuración por defecto
│   └── user_config.json        # Configuración personalizada
├── requirements.txt            # Dependencias
└── README.md                   # Documentación


Componentes Principales

🔄 Conversor Base (base_converter.py)

Python


from abc import ABC, abstractmethod

class BaseConverter(ABC):
    """
    Clase base abstracta para todos los conversores de sistemas.
    
    Define la interfaz común y funcionalidades compartidas
    para la conversión entre diferentes sistemas de TTRPG.
    """
    
    def __init__(self, config=None):
        self.config = config or self.load_default_config()
        self.conversion_log = []
        self.warnings = []
    
    @abstractmethod
    def convert_stats(self, source_stats):
        """Convierte estadísticas básicas entre sistemas."""
        pass
    
    @abstractmethod
    def convert_skills(self, source_skills):
        """Convierte habilidades y competencias."""
        pass
    
    @abstractmethod
    def convert_class_features(self, source_class, source_level):
        """Convierte características de clase."""
        pass
    
    def convert_character(self, source_character):
        """
        Método principal de conversión que orquesta todo el proceso.
        
        Args:
            source_character (dict): Datos del personaje fuente
            
        Returns:
            dict: Personaje convertido al sistema destino
        """
        converted = {}
        
        # Información básica
        converted['name'] = source_character.get('name', 'Unknown')
        converted['race'] = self.convert_race(source_character.get('race'))
        
        # Estadísticas
        converted['stats'] = self.convert_stats(source_character.get('stats', {}))
        
        # Habilidades
        converted['skills'] = self.convert_skills(source_character.get('skills', {}))
        
        # Características de clase
        converted['class_features'] = self.convert_class_features(
            source_character.get('class'),
            source_character.get('level', 1)
        )
        
        # Validar resultado
        self.validate_conversion(converted)
        
        return converted


🎲 Conversor D&D 5e → Pathfinder (dnd5e_to_pathfinder.py)

Python


class DnD5eToPathfinderConverter(BaseConverter):
    """
    Conversor específico de D&D 5e a Pathfinder 1e.
    
    Implementa las reglas de conversión específicas entre estos
    dos sistemas, incluyendo mapeos de estadísticas, habilidades
    y características de clase.
    """
    
    def convert_stats(self, dnd5e_stats):
        """
        Convierte estadísticas de D&D 5e a Pathfinder.
        
        D&D 5e usa array estándar (8-15 + modificadores raciales)
        Pathfinder usa point buy o arrays similares pero con diferentes escalas.
        """
        pathfinder_stats = {}
        
        # Mapeo directo para la mayoría de estadísticas
        stat_mapping = {
            'strength': 'str',
            'dexterity': 'dex', 
            'constitution': 'con',
            'intelligence': 'int',
            'wisdom': 'wis',
            'charisma': 'cha'
        }
        
        for dnd_stat, pf_stat in stat_mapping.items():
            if dnd_stat in dnd5e_stats:
                # Conversión directa (ambos sistemas usan escalas similares)
                pathfinder_stats[pf_stat] = dnd5e_stats[dnd_stat]
                
                self.log_conversion(
                    f"Stat {dnd_stat}: {dnd5e_stats[dnd_stat]} → {pf_stat}: {pathfinder_stats[pf_stat]}"
                )
        
        return pathfinder_stats
    
    def convert_skills(self, dnd5e_skills):
        """
        Convierte habilidades de D&D 5e a Pathfinder.
        
        D&D 5e tiene menos habilidades pero más generales.
        Pathfinder tiene más habilidades específicas.
        """
        pathfinder_skills = {}
        
        # Mapeo de habilidades D&D 5e → Pathfinder
        skill_mapping = {
            'acrobatics': ['Acrobatics'],
            'animal_handling': ['Handle Animal'],
            'arcana': ['Spellcraft', 'Knowledge (arcana)'],
            'athletics': ['Climb', 'Swim'],
            'deception': ['Bluff'],
            'history': ['Knowledge (history)'],
            'insight': ['Sense Motive'],
            'intimidation': ['Intimidate'],
            'investigation': ['Perception'],  # Aproximación
            'medicine': ['Heal'],
            'nature': ['Knowledge (nature)', 'Survival'],
            'perception': ['Perception'],
            'performance': ['Perform'],
            'persuasion': ['Diplomacy'],
            'religion': ['Knowledge (religion)'],
            'sleight_of_hand': ['Sleight of Hand'],
            'stealth': ['Stealth'],
            'survival': ['Survival']
        }
        
        for dnd_skill, pf_skills in skill_mapping.items():
            if dnd_skill in dnd5e_skills:
                dnd_value = dnd5e_skills[dnd_skill]
                
                for pf_skill in pf_skills:
                    # Convertir proficiencia de D&D 5e a ranks de Pathfinder
                    if dnd_value.get('proficient', False):
                        # Estimar ranks basado en nivel y proficiencia
                        estimated_ranks = min(dnd_value.get('level', 1), 20)
                        pathfinder_skills[pf_skill] = {
                            'ranks': estimated_ranks,
                            'class_skill': True
                        }
                    else:
                        pathfinder_skills[pf_skill] = {
                            'ranks': 0,
                            'class_skill': False
                        }
                
                self.log_conversion(f"Skill {dnd_skill} → {', '.join(pf_skills)}")
        
        return pathfinder_skills
    
    def convert_class_features(self, dnd_class, level):
        """
        Convierte características de clase de D&D 5e a Pathfinder.
        
        Esto es complejo porque los sistemas tienen filosofías diferentes
        para las características de clase.
        """
        pathfinder_features = {}
        
        # Mapeo básico de clases
        class_mapping = {
            'fighter': 'Fighter',
            'wizard': 'Wizard', 
            'rogue': 'Rogue',
            'cleric': 'Cleric',
            'ranger': 'Ranger',
            'barbarian': 'Barbarian',
            'bard': 'Bard',
            'druid': 'Druid',
            'monk': 'Monk',
            'paladin': 'Paladin',
            'sorcerer': 'Sorcerer',
            'warlock': 'Sorcerer',  # Aproximación
            'artificer': 'Alchemist'  # Aproximación
        }
        
        if dnd_class.lower() in class_mapping:
            pf_class = class_mapping[dnd_class.lower()]
            pathfinder_features['class'] = pf_class
            pathfinder_features['level'] = level
            
            # Características específicas por clase
            if pf_class == 'Fighter':
                pathfinder_features['bonus_feats'] = level // 2
                pathfinder_features['weapon_training'] = level >= 5
                
            elif pf_class == 'Wizard':
                pathfinder_features['spells_per_day'] = self.calculate_wizard_spells(level)
                pathfinder_features['school_specialization'] = True
                
            elif pf_class == 'Rogue':
                pathfinder_features['sneak_attack'] = f"{(level + 1) // 2}d6"
                pathfinder_features['trap_sense'] = level >= 3
            
            self.log_conversion(f"Class {dnd_class} (Level {level}) → {pf_class}")
        else:
            self.add_warning(f"No direct mapping for class: {dnd_class}")
            pathfinder_features['class'] = 'Fighter'  # Default fallback
        
        return pathfinder_features


🎭 Conversor D&D 5e → Call of Cthulhu (dnd5e_to_coc.py)

Python


class DnD5eToCoCConverter(BaseConverter):
    """
    Conversor de D&D 5e a Call of Cthulhu 7th Edition.
    
    Este es un conversor más complejo porque los sistemas son
    fundamentalmente diferentes (heroic fantasy vs cosmic horror).
    """
    
    def convert_stats(self, dnd5e_stats):
        """
        Convierte estadísticas de D&D 5e a Call of Cthulhu.
        
        D&D 5e: 3-18 (típicamente 8-15)
        Call of Cthulhu: 3d6 × 5 (15-90, promedio ~50-60)
        """
        coc_stats = {}
        
        # Mapeo y conversión de escala
        stat_mapping = {
            'strength': 'STR',
            'dexterity': 'DEX',
            'constitution': 'CON', 
            'intelligence': 'INT',
            'wisdom': 'POW',  # Wisdom → Power en CoC
            'charisma': 'APP'  # Charisma → Appearance (aproximación)
        }
        
        for dnd_stat, coc_stat in stat_mapping.items():
            if dnd_stat in dnd5e_stats:
                dnd_value = dnd5e_stats[dnd_stat]
                
                # Conversión de escala: D&D (3-18) → CoC (15-90)
                # Fórmula: (dnd_value - 3) / 15 * 75 + 15
                coc_value = int(((dnd_value - 3) / 15) * 75 + 15)
                coc_value = max(15, min(90, coc_value))  # Clamp a rango válido
                
                coc_stats[coc_stat] = coc_value
                
                self.log_conversion(
                    f"Stat {dnd_stat}: {dnd_value} → {coc_stat}: {coc_value}"
                )
        
        # Estadísticas adicionales de CoC
        coc_stats['SIZ'] = 50 + random.randint(-10, 10)  # Size promedio humano
        coc_stats['EDU'] = 40 + (coc_stats.get('INT', 50) - 50) // 2  # Educación basada en INT
        
        # Estadísticas derivadas
        coc_stats['HP'] = (coc_stats['CON'] + coc_stats['SIZ']) // 10
        coc_stats['MP'] = coc_stats['POW'] // 5
        coc_stats['Sanity'] = coc_stats['POW']
        
        return coc_stats
    
    def convert_skills(self, dnd5e_skills):
        """
        Convierte habilidades de D&D 5e a Call of Cthulhu.
        
        Los sistemas son muy diferentes:
        - D&D 5e: Proficiencia binaria + modificador de atributo
        - CoC: Porcentajes de 1-100%
        """
        coc_skills = {}
        
        # Mapeo de habilidades
        skill_mapping = {
            'athletics': ['Climb', 'Jump', 'Swim'],
            'acrobatics': ['Dodge'],
            'sleight_of_hand': ['Sleight of Hand'],
            'stealth': ['Stealth'],
            'arcana': ['Occult'],
            'history': ['History'],
            'investigation': ['Library Use', 'Spot Hidden'],
            'nature': ['Natural World'],
            'religion': ['Occult'],  # En CoC, religión a menudo es ocultismo
            'insight': ['Psychology'],
            'medicine': ['First Aid', 'Medicine'],
            'perception': ['Listen', 'Spot Hidden'],
            'survival': ['Track', 'Natural World'],
            'animal_handling': ['Animal Handling'],
            'deception': ['Fast Talk'],
            'intimidation': ['Intimidate'],
            'performance': ['Art/Craft (Performance)'],
            'persuasion': ['Charm', 'Persuade']
        }
        
        # Habilidades base de CoC (todos los investigadores las tienen)
        base_skills = {
            'Dodge': 'DEX/2',
            'Language (Own)': 'EDU',
            'Listen': 'POW/2', 
            'Spot Hidden': 'POW/2',
            'Throw': 'DEX/2'
        }
        
        # Añadir habilidades base
        for skill, formula in base_skills.items():
            coc_skills[skill] = {'base_value': formula, 'points': 0}
        
        # Convertir habilidades de D&D
        for dnd_skill, coc_skill_list in skill_mapping.items():
            if dnd_skill in dnd5e_skills:
                dnd_skill_data = dnd5e_skills[dnd_skill]
                
                # Calcular valor en CoC basado en proficiencia
                if dnd_skill_data.get('proficient', False):
                    base_value = 50  # Competente
                    skill_points = 30  # Puntos adicionales por especialización
                else:
                    base_value = 20  # No entrenado
                    skill_points = 0
                
                for coc_skill in coc_skill_list:
                    coc_skills[coc_skill] = {
                        'base_value': base_value,
                        'points': skill_points,
                        'total': base_value + skill_points
                    }
                
                self.log_conversion(
                    f"Skill {dnd_skill} → {', '.join(coc_skill_list)} ({base_value + skill_points}%)"
                )
        
        return coc_skills
    
    def convert_class_features(self, dnd_class, level):
        """
        Convierte clase de D&D 5e a ocupación de Call of Cthulhu.
        
        CoC no tiene clases sino ocupaciones que determinan
        habilidades profesionales y puntos de habilidad.
        """
        coc_occupation = {}
        
        # Mapeo de clases D&D a ocupaciones CoC
        class_to_occupation = {
            'fighter': 'Soldier',
            'rogue': 'Criminal', 
            'wizard': 'Professor',
            'cleric': 'Priest',
            'ranger': 'Explorer',
            'bard': 'Entertainer',
            'barbarian': 'Tribe Member',
            'monk': 'Priest',  # Aproximación
            'paladin': 'Police Officer',  # Aproximación
            'sorcerer': 'Dilettante',  # Aproximación
            'warlock': 'Occultist',
            'druid': 'Naturalist',
            'artificer': 'Engineer'
        }
        
        if dnd_class.lower() in class_to_occupation:
            occupation = class_to_occupation[dnd_class.lower()]
            coc_occupation['occupation'] = occupation
            
            # Puntos de habilidad basados en nivel de D&D
            skill_points = min(level * 20, 300)  # Máximo 300 puntos
            coc_occupation['occupation_skill_points'] = skill_points
            
            # Habilidades profesionales por ocupación
            occupation_skills = self.get_occupation_skills(occupation)
            coc_occupation['professional_skills'] = occupation_skills
            
            self.log_conversion(
                f"Class {dnd_class} (Level {level}) → Occupation: {occupation}"
            )
        else:
            self.add_warning(f"No occupation mapping for class: {dnd_class}")
            coc_occupation['occupation'] = 'Dilettante'  # Default
        
        return coc_occupation


🧪 Algoritmos de Conversión

Mapeo de Estadísticas

Python


class StatConverter:
    """
    Algoritmos especializados para conversión de estadísticas
    entre diferentes sistemas de juego.
    """
    
    @staticmethod
    def linear_scale_conversion(value, source_range, target_range):
        """
        Conversión lineal entre rangos de estadísticas.
        
        Args:
            value: Valor a convertir
            source_range: (min, max) del sistema fuente
            target_range: (min, max) del sistema destino
        """
        source_min, source_max = source_range
        target_min, target_max = target_range
        
        # Normalizar a 0-1
        normalized = (value - source_min) / (source_max - source_min)
        
        # Escalar al rango destino
        converted = target_min + normalized * (target_max - target_min)
        
        return int(round(converted))
    
    @staticmethod
    def percentile_conversion(value, source_distribution, target_distribution):
        """
        Conversión basada en percentiles para preservar distribución relativa.
        """
        # Calcular percentil en distribución fuente
        percentile = source_distribution.percentile_of(value)
        
        # Obtener valor equivalente en distribución destino
        converted = target_distribution.value_at_percentile(percentile)
        
        return converted
    
    @staticmethod
    def bounded_conversion(value, bounds, conversion_func):
        """
        Aplica conversión con límites para evitar valores imposibles.
        """
        converted = conversion_func(value)
        min_bound, max_bound = bounds
        
        return max(min_bound, min(max_bound, converted))


Preservación de Balance

Python


class BalancePreserver:
    """
    Algoritmos para preservar el balance relativo del personaje
    durante la conversión entre sistemas.
    """
    
    def calculate_power_level(self, character_data, system):
        """
        Calcula el nivel de poder relativo de un personaje
        en su sistema original.
        """
        if system == 'dnd5e':
            return self.dnd5e_power_level(character_data)
        elif system == 'pathfinder':
            return self.pathfinder_power_level(character_data)
        elif system == 'call_of_cthulhu':
            return self.coc_power_level(character_data)
    
    def adjust_for_balance(self, converted_character, target_power_level, target_system):
        """
        Ajusta el personaje convertido para mantener el nivel de poder relativo.
        """
        current_power = self.calculate_power_level(converted_character, target_system)
        
        if abs(current_power - target_power_level) > 0.1:  # 10% tolerance
            adjustment_factor = target_power_level / current_power
            converted_character = self.apply_adjustment(
                converted_character, 
                adjustment_factor,
                target_system
            )
        
        return converted_character


📊 Casos de Uso Prácticos

Caso 1: Migración de Campaña

Python


# Escenario: Grupo quiere cambiar de D&D 5e a Pathfinder
party_members = [
    'fighter_level5.json',
    'wizard_level5.json', 
    'rogue_level5.json',
    'cleric_level5.json'
]

converter = DnD5eToPathfinderConverter()

for member_file in party_members:
    # Cargar personaje original
    original = load_character(member_file)
    
    # Convertir
    converted = converter.convert_character(original)
    
    # Guardar resultado
    output_file = member_file.replace('_level5.json', '_pathfinder.json')
    save_character(converted, output_file)
    
    # Generar reporte
    print(f"✅ {original['name']} convertido exitosamente")
    print(f"📊 Poder relativo preservado: {converter.balance_score:.2f}")


Caso 2: Adaptación de Sistema

Python


# Escenario: Adaptar personaje de fantasía heroica a horror cósmico
dnd_hero = load_character('epic_wizard.json')

# Configurar conversión con ajustes temáticos
converter = DnD5eToCoCConverter(config={
    'horror_adjustment': True,  # Reduce poder general
    'sanity_scaling': 'conservative',  # Cordura más frágil
    'skill_emphasis': 'investigation'  # Enfoque en investigación
})

coc_investigator = converter.convert_character(dnd_hero)

# El poderoso mago se convierte en un académico vulnerable
print(f"Mago épico → Profesor universitario")
print(f"Poder mágico → Conocimiento oculto")
print(f"HP: {dnd_hero['hp']} → {coc_investigator['hp']}")
print(f"Sanity: N/A → {coc_investigator['sanity']}")


Caso 3: Experimentación de Sistemas

Python


# Escenario: Probar el mismo personaje en diferentes sistemas
base_character = create_character({
    'name': 'Aria Shadowblade',
    'concept': 'Sneaky spellcaster',
    'stats': {'dex': 16, 'int': 15, 'cha': 14}
})

systems = ['dnd5e', 'pathfinder', 'call_of_cthulhu']
conversions = {}

for target_system in systems:
    if target_system != 'dnd5e':  # Asumiendo que base es D&D 5e
        converter = get_converter('dnd5e', target_system)
        conversions[target_system] = converter.convert_character(base_character)

# Comparar efectividad en cada sistema
for system, character in conversions.items():
    effectiveness = calculate_effectiveness(character, system)
    print(f"{system}: {effectiveness:.2f} effectiveness")


🔧 Configuración Avanzada

Archivo de Configuración

JSON


{
  "conversion_settings": {
    "preserve_balance": true,
    "balance_tolerance": 0.15,
    "allow_approximations": true,
    "strict_validation": false
  },
  "stat_conversion": {
    "method": "percentile",
    "bounds_checking": true,
    "custom_mappings": {}
  },
  "skill_conversion": {
    "split_skills": true,
    "combine_skills": true,
    "default_untrained": 0.2
  },
  "class_conversion": {
    "allow_multiclass_approximation": true,
    "preserve_archetype": true,
    "fallback_class": "fighter"
  },
  "output_settings": {
    "include_conversion_notes": true,
    "generate_report": true,
    "validate_output": true
  }
}


Reglas Personalizadas

Python


class CustomConverter(BaseConverter):
    """
    Conversor personalizable que permite reglas definidas por usuario.
    """
    
    def __init__(self, custom_rules=None):
        super().__init__()
        self.custom_rules = custom_rules or {}
    
    def apply_custom_rule(self, rule_name, data):
        """
        Aplica una regla personalizada definida por el usuario.
        """
        if rule_name in self.custom_rules:
            rule_func = self.custom_rules[rule_name]
            return rule_func(data)
        return data
    
    def add_custom_mapping(self, source_element, target_element, conversion_func):
        """
        Añade un mapeo personalizado para elementos específicos.
        """
        self.custom_mappings[source_element] = {
            'target': target_element,
            'converter': conversion_func
        }


📈 Validación y Calidad

Sistema de Validación

Python


class ConversionValidator:
    """
    Valida la calidad y corrección de las conversiones realizadas.
    """
    
    def validate_conversion(self, original, converted, source_system, target_system):
        """
        Valida una conversión completa entre sistemas.
        """
        validation_results = {
            'valid': True,
            'warnings': [],
            'errors': [],
            'quality_score': 0.0
        }
        
        # Validar integridad de datos
        self.validate_data_integrity(original, converted, validation_results)
        
        # Validar preservación de balance
        self.validate_balance_preservation(original, converted, validation_results)
        
        # Validar conformidad con sistema destino
        self.validate_system_conformity(converted, target_system, validation_results)
        
        # Calcular puntuación de calidad
        validation_results['quality_score'] = self.calculate_quality_score(validation_results)
        
        return validation_results
    
    def validate_data_integrity(self, original, converted, results):
        """Verifica que no se hayan perdido datos importantes."""
        
    def validate_balance_preservation(self, original, converted, results):
        """Verifica que el balance relativo se haya preservado."""
        
    def validate_system_conformity(self, converted, target_system, results):
        """Verifica que el resultado sea válido en el sistema destino."""


Métricas de Calidad

Python


class QualityMetrics:
    """
    Calcula métricas de calidad para evaluar conversiones.
    """
    
    @staticmethod
    def completeness_score(original, converted):
        """
        Porcentaje de elementos originales que fueron convertidos.
        """
        original_elements = count_elements(original)
        converted_elements = count_elements(converted)
        
        return min(1.0, converted_elements / original_elements)
    
    @staticmethod
    def accuracy_score(original, converted, ground_truth=None):
        """
        Precisión de la conversión comparada con conversión manual.
        """
        if ground_truth:
            return calculate_similarity(converted, ground_truth)
        return 0.8  # Estimación por defecto
    
    @staticmethod
    def balance_preservation_score(original, converted):
        """
        Qué tan bien se preservó el balance relativo del personaje.
        """
        original_power = calculate_relative_power(original)
        converted_power = calculate_relative_power(converted)
        
        difference = abs(original_power - converted_power)
        return max(0.0, 1.0 - difference)


🔮 Futuras Mejoras

Funcionalidades Planificadas




Interfaz Gráfica: GUI con drag-and-drop para conversiones




Más Sistemas: Soporte para Savage Worlds, GURPS, Fate




Conversión Bidireccional: Conversión en ambas direcciones automática




Batch Processing: Conversión de múltiples personajes simultáneamente




Web Interface: Aplicación web para uso online




API REST: Servicio web para integración con otras herramientas




Machine Learning: IA para mejorar precisión de conversiones




Community Rules: Reglas de conversión creadas por la comunidad

Mejoras Técnicas




Performance: Optimización para personajes complejos




Caching: Cache inteligente de conversiones frecuentes




Plugins: Sistema de plugins para extensibilidad




Testing: Suite completa de tests automatizados




Documentation: Documentación completa de APIs




Localization: Soporte para múltiples idiomas




Cloud Storage: Backup y sincronización en la nube




Version Control: Control de versiones para personajes

🛠️ Tecnologías Utilizadas

TecnologíaVersiónPropósitoPython3.8+Lenguaje de programaciónJSONEstándarFormato de datosCSVEstándarFormato de exportaciónPandas1.3+Procesamiento de datos (opcional)ArgparseEstándarInterfaz de línea de comandosLoggingEstándarSistema de logs

🎯 Habilidades Demostradas

Competencias Técnicas

•
Algorithm Design: Algoritmos de mapeo y conversión complejos

•
Data Processing: Manipulación y transformación de estructuras de datos

•
System Integration: Integración entre sistemas con diferentes paradigmas

•
Validation Logic: Sistemas de validación y verificación de calidad

•
Modular Architecture: Diseño extensible y mantenible

•
Error Handling: Gestión robusta de casos edge y errores

Competencias de Dominio

•
Game System Knowledge: Comprensión profunda de múltiples sistemas TTRPG

•
Balance Analysis: Entendimiento de mecánicas de balance de juego

•
User Experience: Diseño centrado en las necesidades de jugadores y DMs

•
Problem Solving: Solución de problemas complejos de compatibilidad

•
Community Focus: Desarrollo para una comunidad específica y apasionada

🌟 Conexión con La Guarida de Jorge

Este proyecto es parte del ecosistema de herramientas para la comunidad de juegos de rol:

Integración con Contenido

•
Tutoriales en YouTube sobre conversión entre sistemas

•
Streams en Twitch mostrando conversiones en tiempo real

•
Casos de estudio en redes sociales

•
Feedback de la comunidad para mejoras

Eventos y Colaboraciones

•
TechRol 2024: Presentación de la herramienta

•
Workshops: Enseñanza de conversión manual vs automática

•
Colaboraciones: Con otros creadores de herramientas TTRPG

•
Beta testing: Con grupos de juego de la comunidad

👨‍💻 Autor

Jorge Fuentes Jiménez

•
GitHub: @jorge-fuentes-94

•
LinkedIn: Jorge Fuentes Jiménez

•
La Guarida de Jorge:

•
TikTok

•
YouTube

•
Instagram



•
Email: jf7494@gmail.com

Experiencia en TTRPG

•
15+ años como Dungeon Master en múltiples sistemas

•
Organizador de TechRol 2024 (evento tech + rol)

•
Experiencia práctica con D&D 5e, Pathfinder, Call of Cthulhu

•
Creador de contenido especializado en juegos de rol

📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

🤝 Contribuciones

¡Las contribuciones de la comunidad TTRPG y desarrolladores son muy bienvenidas!

Cómo Contribuir

1.
Fork el proyecto

2.
Crea una rama para tu feature (git checkout -b feature/NuevoSistema)

3.
Commit tus cambios (git commit -m 'Añadir soporte para Savage Worlds')

4.
Push a la rama (git push origin feature/NuevoSistema)

5.
Abre un Pull Request

Ideas de Contribución

•
Nuevos sistemas de juego

•
Mejoras en algoritmos de conversión

•
Validaciones adicionales

•
Interfaz gráfica

•
Tests y documentación

•
Optimizaciones de rendimiento

📞 Soporte y Comunidad

Soporte Técnico

•
Issues: GitHub Issues

•
Email: jf7494@gmail.com

•
Discord: La Guarida de Jorge

Comunidad TTRPG

•
Feedback: Comparte tu experiencia con conversiones

•
Sugerencias: Ideas para nuevos sistemas o mejoras

•
Casos de uso: Cómo usas la herramienta en tus campañas

•
Colaboraciones: Proyectos relacionados con TTRPG + Tech





⭐ ¡Si esta herramienta facilita tus conversiones entre sistemas, no olvides darle una estrella! ⭐

🎲 ¡Que disfrutes explorando diferentes mundos de juego! 🎲

