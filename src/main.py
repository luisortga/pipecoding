from pipe_funciones import Funciones
from designe import Style
import re
"""
    Modulo principal del programa
"""


# Objetos
pipe_fun = Funciones()
design = Style()


# Main
if __name__ == "__main__":
    # Informacion de entrada
    # 10 Pipes, EFW + 100% RT, ASME C3ZCF0T2 6.6 M B36.19/B36.10, ASTM A358 Gr.304/304L Cl.1, BE, -, Imp Tested -196°C, Cryo Serv., S-10S
    text = input()
    # Primera informacion
    if not text:
        messe = "[red]El texto esta vacio"
        design.view_error(messe)
    else:
        ### Llamar a las funciones
        # Obtenemos las pulgadas de la tubería
        pattern = r"\s*\"\s*"
        result = re.search(pattern, text)
        if result:
            text_result = pipe_fun.comillas(text)
            text = text_result
         
        pulgadas = pipe_fun.capture_in(text)

        # Obtenemos la tangente de los grados especiales
        tg_42 = pipe_fun.tan(42)
        tg_52 = pipe_fun.tan(52)
        tg_60 = pipe_fun.tan(60)
        tg_65 = pipe_fun.tan(65)
        tg_70 = pipe_fun.tan(70)
        tg_80 = pipe_fun.tan(80)

        # Obtenemos el avance de los codos de 90 y 45
        av_90 = pipe_fun.advanced_elbow90(pulgadas)
        av_45 = pipe_fun.advanced_elbow45(pulgadas)

        # Obtenemos el avance de los codos especiales
        av_42 = pipe_fun.advanced_elbow42(tg_42, pulgadas)
        av_52 = pipe_fun.advanced_elbow52(tg_52, pulgadas)
        av_60 = pipe_fun.advanced_elbow60(tg_60, pulgadas)
        av_65 = pipe_fun.advanced_elbow65(tg_65, pulgadas)
        av_70 = pipe_fun.advanced_elbow70(tg_70, pulgadas)
        av_80 = pipe_fun.advanced_elbow80(tg_80, pulgadas)

        # Obtenemos del metodo large_pipe el largo de la tuberia en una variable float
        large = pipe_fun.large_pipe(text)

        # Elejimos el material
        material = pipe_fun.material_pipe(text)

        # Obtener el od con la funcion
        od = pipe_fun.out_diameter(pulgadas)

        # Obtener la cedula y
        # Espesor de pared wall thickness
        if material == "S.S.":
            cedula = pipe_fun.cedula_ss(text)
            t = pipe_fun.wall_thickness_inox(cedula, pulgadas)
        elif material == "A.C.":
            cedula = pipe_fun.cedula_ac(text)
            t = pipe_fun.wall_tickness_ac(cedula, pulgadas)
        else:
            t = 0.0
        
        peso_d = pipe_fun.peso(od, t)
        peso_t = pipe_fun.peso_total(peso_d, large)

        # Datos de salida

        one_one = f"El avance de un codo de 90 grados de {pulgadas}:"
        one_two = f"[green]{av_90} mm"

        two_one = f"El avance de un codo de 45 grados de {pulgadas}:"
        two_two = f"[green]{av_45} mm"

        three_one = f"El avance de un codo de 52 grados de {pulgadas}:"
        three_two = f"[green]{av_52} mm"

        four_one = f"El avance de un codo de 60 grados de {pulgadas}:"
        four_two = f"[green]{av_60} mm"

        five_one = f"El avance de un codo de 65 grados de {pulgadas}:"
        five_two = f"[green]{av_65} mm"

        six_one = f"El avance de un codo de 70 grados de {pulgadas}:"
        six_two = f"[green]{av_70} mm"

        seven_one = f"El avance de un codo de 80 grados,de {pulgadas}:"
        seven_two = f"[green]{av_80} mm"

        eight_one = f"El espesor de pared:"
        eight_two = f"[green]{t} mm"

        nine_one = f"El peso por metro lineal teorico:"
        nine_two = f"[green]{peso_d} kg"

        ten_one = f"El peso total teorico:"
        ten_two = f"[green]{peso_t} kg x {large} M"

        # Creditos
        eleven_one = f'~pipecoding'
        eleven_two = f'@luisOrtga'

        if pulgadas == 0 and av_90 == 0 and av_45 == 0 and peso_d == 0 and large == 0:
            ms = "[red]No se puede calcular por falta de datos. vuelva a intentarlo."
            design.view_error(ms)
        elif large == 0 and t == 0:
            # Creditos
            # @Override
            eight_one = f'falto la cedula y la longitud'
            eight_two = f'~pipecoding @luisOrtga'

            # Mostrar los datos
            design.incomplete_data(
                one_one,one_two,two_one,two_two,
                three_one,three_two,four_one,four_two,
                five_one,five_two,six_one,six_two,
                seven_one,seven_two,eight_one,eight_two
                )
        else:
            # Mostrar los datos
            design.complete_data(
                one_one,one_two,two_one,two_two,
                three_one,three_two,four_one,four_two,
                five_one,five_two,six_one,six_two,
                seven_one,seven_two,eight_one,eight_two,
                nine_one,nine_two,ten_one,ten_two,
                eleven_one,eleven_two
                )
