import re
import math
from fractions import Fraction

"""
@luis ortega
"""
class Funciones:

    def __init__(self):
        pass

    def out_diameter(self, pulgada) -> float:
        """
        Devuleve el diametro exterior de la tubería con el uso de diccionario
        """
        od: float = 0.0
        str_pulgada = str(pulgada)
        out_diameter = {
            "0.125" : 10.3, "0.25" : 13.7, "0.375": 17.2, "0.5": 21.3, "0.75": 26.7, "1.0": 33.4,
            "1.25": 42.2, "1.5": 48.3, "1.75": 54.3, "2.0": 60.3, "2.5": 73.0, "3.0": 88.9, "3.5": 101.6,
            "4.0": 114.3, "5.0": 141.3, "6.0": 168.3, "8.0": 219.1, "10.0": 273.1, "12.0": 323.85,
            "14.0": 365.125, "16.0": 406.4, "18.0": pulgada*25.4
        }
        if pulgada <= 18 and pulgada > 0.125:
            str_od = out_diameter[str_pulgada]
            od = str_od
            return od
        elif pulgada >= 20:
            od = pulgada*25.4
        else: return od

    def wall_thickness_inox(self, cedula, pulgada) -> float:
        """
        Retorna el espesor de pared dependiendo la cedula
        """
        wall_tick: float = 0.0
        # wall tick en cedula 5S
        if cedula == "S-5S":
            if pulgada in (0.125, 0.25, 0.375, 0.5, 0.75, 1, 1.25, 1.5, 2): wall_tick = 1.65
            elif pulgada in (2.5, 3, 3.5, 4): wall_tick = 2.11
            elif pulgada in (5, 6, 8): wall_tick = 2.77
            elif pulgada == 10: wall_tick = 3.4
            elif pulgada in (12, 14): wall_tick = 3.96
            elif pulgada in (16, 18): wall_tick = 4.19
            elif pulgada in (20, 22): wall_tick = 4.78
            elif pulgada == 24: wall_tick = 5.54
            elif pulgada == 30: wall_tick = 6.35

        # wall tick en cedula 10S
        elif cedula == "S-10S":
            if pulgada == 0.125: wall_tick = 1.24
            elif pulgada in (0.25, 0.375): wall_tick = 1.65
            elif pulgada in (0.5, 0.75): wall_tick = 2.11
            elif pulgada in (1, 1.25, 1.5, 2): wall_tick = 2.77
            elif pulgada in (2.5, 3, 3.5, 4): wall_tick = 3.05
            elif pulgada in (5, 6): wall_tick = 3.4
            elif pulgada == 8: wall_tick = 3.76
            elif pulgada == 10: wall_tick = 4.19
            elif pulgada == 12: wall_tick = 4.57
            elif pulgada in (14, 16, 18): wall_tick = 4.78
            elif pulgada in (20, 22): wall_tick = 5.54
            elif pulgada == 24: wall_tick = 6.35
            elif pulgada == 8: wall_tick = 7.92

        # wall tick en cedula 40S    
        elif cedula == "S-40S":
            if pulgada == 0.125: wall_tick = 1.73
            elif pulgada == 0.25: wall_tick = 2.24
            elif pulgada == 0.375: wall_tick = 2.31
            elif pulgada == 0.5: wall_tick = 2.77
            elif pulgada == 0.75: wall_tick = 2.87
            elif pulgada == 1: wall_tick = 3.38
            elif pulgada == 1.25: wall_tick = 3.56
            elif pulgada == 1.5: wall_tick = 3.68
            elif pulgada == 2: wall_tick = 3.91
            elif pulgada == 2.5: wall_tick = 5.16
            elif pulgada == 3: wall_tick = 5.49
            elif pulgada == 3.5: wall_tick = 5.74
            elif pulgada == 4: wall_tick = 6.02
            elif pulgada == 5: wall_tick = 6.55
            elif pulgada == 6: wall_tick = 7.11
            elif pulgada == 8: wall_tick = 8.18
            elif pulgada == 10: wall_tick = 9.27
            elif pulgada in (12, 14, 16, 18, 20, 22, 24, 30): wall_tick = 9.53
        
        # wall tick en cedula 80S
        elif cedula == "S-80S":
            if pulgada == 0.125: wall_tick = 2.41
            elif pulgada == 0.25: wall_tick = 3.02
            elif pulgada == 0.375: wall_tick = 3.2
            elif pulgada == 0.5: wall_tick = 3.73
            elif pulgada == 0.75: wall_tick = 3.91
            elif pulgada == 1: wall_tick = 4.55
            elif pulgada == 1.25: wall_tick = 4.85
            elif pulgada == 1.5: wall_tick = 5.08
            elif pulgada == 2: wall_tick = 5.54
            elif pulgada == 2.5: wall_tick = 7.01
            elif pulgada == 3: wall_tick = 7.62
            elif pulgada == 3.5: wall_tick = 8.08
            elif pulgada == 4: wall_tick = 8.56
            elif pulgada == 5: wall_tick = 9.53
            elif pulgada == 6: wall_tick = 10.97
            elif pulgada in (8, 10, 12, 14, 16, 18, 20, 22, 24, 30): wall_tick = 12.7
        else: wall_tick = 0.0
        # Retorno
        return wall_tick

    def wall_tickness_ac(self, cedula, pulgada) -> float:
        wall_tick: float = 0.0
        str_pulgada = str(pulgada)
        sch_5 = { # 1/8 - 30
            "0.5": 1.65, "0.75": 1.65, "1.0": 1.65, "1.25": 1.65, "1.5": 1.65, "2.0": 1.65, "2.5": 2.11,
            "3.0": 2.11, "3.5": 2.11, "4.0": 2.11, "5.0": 2.77, "6.0": 2.77, "8.0": 2.77, "10.0": 3.4,
            "12.0": 3.96, "14.0": 3.96, "16.0": 4.19, "18.0": 4.19, "20.0": 4.78, "22.0": 4.78, "24.0": 5.54,
            "26.0": 5.54, "28.0": 6.35, "30.0": 6.35
        }
        sch_10 = { # 1/8 - 36
            "0.125": 1.24, "0.25": 1.65, "0.375": 1.65, "0.5": 2.11, "0.75": 2.11, "1.0": 2.77, "1.25": 2.77,
            "1.5": 2.77, "2.0": 2.77, "2.5": 3.05, "3.0": 3.05, "3.5": 3.05, "4.0": 3.05, "5.0": 3.4,
            "6.0": 3.4, "8.0": 3.76, "10.0": 4.19, "12.0": 4.57, "14.0": 6.35, "16.0": 6.35, "18.0": 6.35,
            "20.0": 6.35, "22.0": 6.35, "24.0": 6.35, "26.0": 7.92, "28.0": 7.92, "30.0": 7.92, "32.0": 7.92,
            "34.0": 7.92, "36.0": 7.92
        }
        sch_20 = { # 26 - 36
            "26.0": 12.7, "28.0": 12.7, "30.0": 12.7, "32.0": 12.7, "34.0": 12.7, "36.0": 12.7
        }
        sch_30 = { # 1/8 - 24
            "0.125": 1.45, "0.25": 1.85, "0.375": 1.85, "0.5": 2.41, "0.75": 2.41, "1.0": 2.9, "1.25": 2.97,
            "1.5": 3.18, "2.0": 3.18, "2.5": 4.78, "3.0": 4.78, "3.5": 4.78, "4.0": 4.78, "5.0": 4.78,
            "6.0": 4.78, "8.0": 7.04, "10.0": 7.08, "12.0": 8.38, "14.0": 9.53, "16.0": 9.53,
            "18.0": 11.13, "20.0": 12.7, "22.0": 12.7, "24.0": 14.27,
        }
        sch_40 = { # 1/8 - 24
            "0.125": 1.73, "0.25": 2.24, "0.375": 2.31, "0.5": 2.77, "0.75": 2.87, "1.0": 3.38,
            "1.25": 3.56, "1.5": 3.68, "2.0": 3.91, "2.5": 5.16, "3.0": 5.49, "3.5": 5.74,
            "4.0": 6.02, "5.0": 6.55, "6.0": 7.11, "8.0": 8.18, "10.0": 9.27, "12.0": 10.31,
            "14.0": 11.13, "16.0": 12.7, "18.0": 14.27, "20.0": 15.09, "22.0": 15.09, "24.0": 17.48,
        }
        std = { # 1/8 - 48
            "0.125": 1.73, "0.25": 2.24, "0.375": 2.31, "0.5": 2.77, "0.75": 2.87, "1.0": 3.38,
            "1.25": 3.56, "1.5": 3.68, "2.0": 3.91, "2.5": 5.16, "3.0": 5.49, "3.5": 5.74,
            "4.0": 6.02, "5.0": 6.55, "6.0": 7.11, "8.0": 8.18, "10.0": 9.27, "12.0": 9.53,
            "14.0": 9.53, "16.0": 9.53, "18.0": 9.53, "20.0": 9.53, "22.0": 9.53, "24.0": 9.53,
            "26.0": 9.53, "28.0": 9.53, "30.0": 9.53, "32.0": 9.53, "34.0": 9.53, "36.0": 9.53,
            "38.0": 9.53, "40.0": 9.53, "42.0": 9.53, "44.0": 9.53, "46.0": 9.53,
            "48.0": 9.53
        }
        sch_80 = { # 1/8 - 24
            "0.125": 2.41, "0.25": 3.02, "0.375": 3.2, "0.5": 3.73, "0.75": 3.91, "1.0": 4.55,
            "1.25": 4.85, "1.5": 5.08, "2.0": 5.54, "2.5": 7.01, "3.0": 7.62, "3.5": 8.08,
            "4.0": 8.56, "5.0": 9.53, "6.0": 10.97, "8.0": 12.7, "10.0": 15.09, "12.0": 17.48,
            "14.0": 19.05, "16.0": 21.44, "18.0": 23.83, "20.0": 26.19, "22.0": 28.58,
            "24.0": 30.96,
        }
        sch_60 = { # 8 - 24
            "8.0": 10.31, "10.0": 12.7, "12.0": 14.27, "14.0": 15.09,
            "16.0": 16.66, "18.0": 19.05, "20.0": 20.62, "22.0": 22.23,
            "24.0": 24.61,
        }
        xs = { # 1/8 - 48
            "0.125": 2.41, "0.25": 3.02, "0.375": 3.2, "0.5": 3.73, "0.75": 3.91, "1.0": 4.55,
            "1.25": 4.85, "1.5": 5.08, "2.0": 5.54, "2.5": 7.01, "3.0": 7.62, "3.5": 8.08,
            "4.0": 8.56, "5.0": 9.53, "6.0": 10.97, "8.0": 12.7, "10.0": 12.7, "12.0": 12.7,
            "14.0": 12.7, "16.0": 12.7, "18.0": 12.7, "20.0": 12.7, "22.0": 12.7, "24.0": 12.7,
            "26.0": 12.7, "28.0": 12.7, "30.0": 12.7, "32.0": 12.7, "34.0": 12.7, "36.0": 12.7,
            "38.0": 12.7, "40.0": 12.7, "42.0": 12.7, "44.0": 12.7, "46.0": 12.7, "48.0": 12.7
        }
        sch_120 = { # 4 - 24
            "4.0": 11.13, "5.0": 12.7, "6.0": 14.27, "8.0": 18.26, "10.0": 21.44, "12.0": 25.4,
            "14.0": 27.79, "16.0": 30.96, "18.0": 34.93, "20.0": 38.1, "22.0": 41.28, "24.0": 46.02,
        }
        sch_100 = { # 8 - 24
            "8.0": 15.09, "10.0": 18.26, "12.0": 21.44, "14.0": 23.83, "16.0": 26.19,
            "18.0": 29.36, "20.0": 32.54, "22.0": 34.93, "24.0": 38.89,
        }
        sch_160 = { # 1/2 - 24
            "0.5": 4.78, "0.75": 5.56, "1.0": 6.35, "1.25": 6.35, "1.5": 7.14, "2.0": 8.74,
            "2.5": 9.53, "3.0": 11.13, "3.5": 11.13, "4.0": 13.49, "5.0": 15.88, "6.0": 18.26,
            "8.0": 23.01, "10.0": 28.58, "12.0": 33.32, "14.0": 35.71, "16.0": 40.49,
            "18.0": 45.24, "20.0": 50.1, "22.0": 53.98, "24.0": 59.54,
        }
        xxs = { # 1/2 - 12
            "0.5": 7.47, "0.75": 7.82, "1.0": 9.09, "1.25": 9.7, "1.5": 10.16,
            "2.0": 11.07, "2.5": 14.02, "3.0": 15.24, "3.5": 15.24, "4.0": 17.12,
            "5.0": 19.05, "6.0": 21.95, "8.0": 22.23, "10.0": 25.4, "12.0": 25.4,
        }
        sch_140 = { # 8 - 24
            "8.0": 20.62, "10.0": 25.4, "12.0": 28.58, "14.0": 31.75, "16.0": 36.53,
            "18.0": 39.67, "20.0": 44.45, "22.0": 47.63, "24.0": 52.37, 
        }
        try: # solucion del error si las pulgadas no estan en el diccionario, pulgadas no validas
            if cedula == "S-5S":
                wall_tick = sch_5[str_pulgada]
                return wall_tick
            elif cedula == "S-10S":
                wall_tick = sch_10[str_pulgada]
                return wall_tick
            elif cedula == "S-20S":
                wall_tick = sch_20[str_pulgada]
                return wall_tick
            elif cedula == "S-30S":
                wall_tick = sch_30[str_pulgada]
                return wall_tick
            elif cedula == "S-40S":
                wall_tick = sch_40[str_pulgada]
                return wall_tick
            elif cedula == "S-60S":
                wall_tick = sch_60[str_pulgada]
                return wall_tick
            elif cedula == "S-80S":
                wall_tick = sch_80[str_pulgada]
                return wall_tick
            elif cedula == "S-100S":
                wall_tick = sch_100[str_pulgada]
                return wall_tick
            elif cedula == "S-120S":
                wall_tick = sch_120[str_pulgada]
                return wall_tick
            elif cedula == "S-140S":
                wall_tick = sch_140[str_pulgada]
                return wall_tick
            elif cedula == "S-160S":
                wall_tick = sch_160[str_pulgada]
                return wall_tick
            elif cedula == "STD":
                wall_tick = std[str_pulgada]
                return wall_tick
            elif cedula == "XS":
                wall_tick = xs[str_pulgada]
                return wall_tick
            elif cedula == "XXS":
                wall_tick = xxs[str_pulgada]
                return wall_tick
            else: return wall_tick
        except KeyError as e:
            print(f'Pulgadas no aceptables, error : {e}')
            return wall_tick

    def large_pipe(self, text) -> float:
        """
        Extrae y retorna el largo de la tubería
        """
        # Encontrar el largo de la tubería
        pattern = re.search(r"\d\d\.\d M", text, re.IGNORECASE) # 10.0 M
        if pattern:
            part = pattern.group()
            part = part.split()
            large = part[0]
            large = float(large)
        else:
            pattern = re.search(r"\d\.\d M", text, re.IGNORECASE) # 6.0 M
            if pattern:
                pt = pattern.group()
                pt = pt.split()
                large = pt[0]
                large = float(large)
            else: large = 0.0
        return large

    def capture_in(self, text) -> float:
        """
        regresa las pulgadas de la tubería
        """
        pipe_in: float = 0.0
        patt_int = re.search(r"\d{2} Pipes|\d{2} Pulgadas|\d{2}\.00 Pulgadas|\d{2}\.00 Pipes|\d\.00 Pulgadas|\d\.00 Pipes|\d Pulgadas|\d Pipes", text, re.IGNORECASE)
        if patt_int:
            ptt = patt_int.group()
            mitad = ptt.split()
            patt = mitad[0]
            pipe_in = float(patt) # Example 10 or 6
        patt_frac = re.search(r"(\d/\d) Pipes|(\d/\d) Pulgadas", text, re.IGNORECASE)
        if patt_frac:
            fraction = (patt_frac.group())
            new_fra = fraction.split()
            fra = Fraction(new_fra[0])
            pipe_in = float(fra) # Example 3/4
        patt_intfra = re.search(r"\d \d/\d Pipes|\d \d/\d Pulgadas", text, re.IGNORECASE)
        if patt_intfra:
            ptt = patt_intfra.group()
            # separamos el texto por espacios
            partes = ptt.split() # fracmentar la cadena de texto
            entero = float(partes[0]) # convertimos el primer numero a float
            fraccion = Fraction(partes[1]) # convertimos la fraccion
            fra = float(fraccion)
            pipe_in = entero+fra # Example 1 1/2
        else : return pipe_in
        return pipe_in

    def tan(self, grados) -> float:
        """
        Retorna la tangente de los grados colocados para el avance de grados especiales
        """
        new_grade: float = grados/2
        tangente: float = math.tan(math.radians(new_grade))
        return tangente

    def advanced_elbow90(self, inch) -> float:
        """
        Retorn del avance en mm de un codo de 90 R.L.
        """
        advanced_90 = inch*1.5
        ad_90 = advanced_90*25.4 # codo de 90 grade
        return ad_90

    def advanced_elbow45(self, inch) -> float:
        advanced_45 = inch*0.625
        ad_45 = advanced_45*25.4 # codo de 45 grade
        return ad_45

    def advanced_elbow42(self, tan_42, inch) -> float:
        """
        Retorno del avance en mm de un codo de 42 R.L.
        """
        ad_42: float = inch*38.1*tan_42 # codo degradado especial
        return ad_42

    def advanced_elbow52(self, tan_52, inch) -> float:
        """
        Retorno del avance en mm de un codo de 52 R.L.
        """
        ad_52: float = inch*38.1*tan_52 # codo degradado especial
        return ad_52

    def advanced_elbow60(self, tan_60, inch) -> float:
        """
        Retorno del avance en mm de un codo de 60 R.L.
        """
        ad_60: float = inch*38.1*tan_60 # codo degradado especial
        return ad_60

    def advanced_elbow65(self, tan_65, inch) -> float:
        """
        Retorno del avance en mm de un codo de 65 R.L.
        """
        ad_65: float = inch*38.1*tan_65 # codo degradado especial
        return ad_65

    def advanced_elbow70(self, tan_70, inch) -> float:
        """
        Retorno del avance en mm de un codo de 70 R.L.
        """
        ad_70: float = inch*38.1*tan_70 # codo degradado especial
        return ad_70

    def advanced_elbow80(self, tan_80, inch) -> float:
        """
        Retorno del avance en mm de un codo de 80 R.L.
        """
        ad_80: float = inch*38.1*tan_80 # codo degradado especial
        return ad_80

    def peso(self, od: float, t: float, c: float = 0.02491) -> float:
        """
        Retorna el peso de la tubería por kg/m
        """
        calculo: float = (od-t)*t*c
        return calculo

    def peso_total(self, peso_d, large) -> float:
        """
        Retorna el peso total de la tubería
        """
        result_full = peso_d*large
        return result_full

    def material_pipe(self, text) -> str:
        material = None
        acero_carbon = re.search(r"A.C.|106B|A106 GR.B|CARBON STEEL|ACERO AL CARBON", text, re.IGNORECASE)
        if acero_carbon:
            material = "A.C."
            return material
        inox = re.search(r"304/304|316/316|S.S.|ACERO INOXIDABLE|STAINLESS STEEL", text, re.IGNORECASE)
        if inox:
            material = "S.S."
            return material
        else: return material

    def cedula_ss(self, text) -> str:
        """
        Regresa la cedula de la tuberia de acero inoxidable
        """
        text.upper()
        cedula = None
        cedula_pattern_5 = re.search(r"S-5S|CEDULA 5S|SCHEDULE 5S", text, re.IGNORECASE)
        if cedula_pattern_5:
            cedula = "S-5S"
            return cedula
        cedula_pattern_10 = re.search(r"S-10S|CEDULA 5S|SCHEDULE 5S", text, re.IGNORECASE)
        if cedula_pattern_10:
            cedula = "S-10S"
            return cedula
        cedula_pattern_40 = re.search(r"S-40S|CEDULA 40S|SCHEDULE 40S", text, re.IGNORECASE)
        if cedula_pattern_40:
            cedula = "S-40S"
            return cedula
        cedula_pattern_80 = re.search(r"S-80S|CEDULA 80S|SCHEDULE 80S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-80S"
            return cedula
        else: return cedula

    def cedula_ac(self, text) -> str:
        """
        Regresa la cedula de la tuberia de acero al carbón
        """
        cedula = None
        cedula_pattern_5 = re.search(r"S-5S|CEDULA 5S|SCHEDULE 5S", text, re.IGNORECASE)
        if cedula_pattern_5:
            cedula = "S-5S"
            return cedula
        cedula_pattern_10 = re.search(r"S-10S|CEDULA 5S|SCHEDULE 5S", text, re.IGNORECASE)
        if cedula_pattern_10:
            cedula = "S-10S"
            return cedula
        cedula_pattern_40 = re.search(r"S-20S|CEDULA 20S|SCHEDULE 20S", text, re.IGNORECASE)
        if cedula_pattern_40:
            cedula = "S-20S"
            return cedula
        cedula_pattern_80 = re.search(r"S-30S|CEDULA 30S|SCHEDULE 30S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-30S"
            return cedula
        cedula_pattern_80 = re.search(r"S-40S|CEDULA 40S|SCHEDULE 40S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-40S"
            return cedula
        cedula_pattern_80 = re.search(r"S-60S|CEDULA 60S|SCHEDULE 60S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-60S"
            return cedula
        cedula_pattern_80 = re.search(r"S-80S|CEDULA 80S|SCHEDULE 80S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-80S"
            return cedula
        cedula_pattern_80 = re.search(r"S-100S|CEDULA 100S|SCHEDULE 100S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-100S"
            return cedula
        cedula_pattern_80 = re.search(r"S-120S|CEDULA 120S|SCHEDULE 120S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-120S"
            return cedula
        cedula_pattern_80 = re.search(r"S-140S|CEDULA 140S|SCHEDULE 140S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-140S"
            return cedula
        cedula_pattern_80 = re.search(r"S-160S|CEDULA 160S|SCHEDULE 160S", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "S-160S"
            return cedula
        cedula_pattern_80 = re.search(r"STD|CEDULA STANDARD|ESTANDAR", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "STD"
            return cedula
        cedula_pattern_80 = re.search(r"XS|CEDULA EXTRA FUERTE|SCHEDULE XS", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "XS"
            return cedula
        cedula_pattern_80 = re.search(r"XXS|CEDULA EXTRA EXTRA FUERTE|SCHEDULE XXS", text, re.IGNORECASE)
        if cedula_pattern_80:
            cedula = "XXS"
            return cedula
        else:
            return cedula