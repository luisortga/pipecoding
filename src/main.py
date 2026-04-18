from pipe_funciones import Funciones
from diseño import Style
# orteg

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
        messe = "[green]El texto esta vacio"
        design.view_error(messe)
    else:
        ### Llamar a las funciones
        # Obtenemos las pulgadas de la tubería
        pulgada = pipe_fun.capture_in(text)

        # Obtenemos la tangente de los grados especiales
        tg_42 = pipe_fun.tan(42)
        tg_52 = pipe_fun.tan(52)
        tg_60 = pipe_fun.tan(60)
        tg_65 = pipe_fun.tan(65)
        tg_70 = pipe_fun.tan(70)
        tg_80 = pipe_fun.tan(80)

        # Obtenemos el avance de los codos de 90 y 45
        av_90 = pipe_fun.advanced_elbow90(pulgada)
        av_45 = pipe_fun.advanced_elbow45(pulgada)

        # Obtenemos el avance de los codos especiales
        av_42 = pipe_fun.advanced_elbow42(tg_42, pulgada)
        av_52 = pipe_fun.advanced_elbow52(tg_52, pulgada)
        av_60 = pipe_fun.advanced_elbow60(tg_60, pulgada)
        av_65 = pipe_fun.advanced_elbow65(tg_65, pulgada)
        av_70 = pipe_fun.advanced_elbow70(tg_70, pulgada)
        av_80 = pipe_fun.advanced_elbow80(tg_80, pulgada)

        # Obtenemos del metodo large_pipe el largo de la tuberia en una variable float
        large = pipe_fun.large_pipe(text)

        # Elejimos el material
        material = pipe_fun.material_pipe(text)

        # Obtener el od con la funcion
        od = pipe_fun.out_diameter(pulgada)

        # Obtener la cedula y
        # Espesor de pared wall thickness
        if material == "S.S.":
            cedula = pipe_fun.cedula_ss(text)
            t = pipe_fun.wall_thickness_inox(cedula, pulgada)
        elif material == "A.C.":
            cedula = pipe_fun.cedula_ac(text)
            t = pipe_fun.wall_tickness_ac(cedula, pulgada)
        else:
            t = 0.0
        
        # Solucion del error si el peso da None
        # try:
        peso_d = pipe_fun.peso(od, t)
        peso_t = pipe_fun.peso_total(peso_d, large)
        # except TypeError as e:
            # print(f'Error: {e}')

        # Datos de salida

        one_one = f"El avance de un codo de 90 grados de {pulgada}:"
        one_two = f"[green]{av_90} mm"

        two_one = f"El avance de un codo de 45 grados de {pulgada}:"
        two_two = f"[green]{av_45} mm"

        three_one = f"El avance de un codo de 52 grados de {pulgada}:"
        three_two = f"[green]{av_52} mm"

        four_one = f"El avance de un codo de 60 grados de {pulgada}:"
        four_two = f"[green]{av_60} mm"

        five_one = f"El avance de un codo de 65 grados de {pulgada}:"
        five_two = f"[green]{av_65} mm"

        six_one = f"El avance de un codo de 70 grados de {pulgada}:"
        six_two = f"[green]{av_70} mm"

        seven_one = f"El avance de un codo de 80 grados,de {pulgada}:"
        seven_two = f"[green]{av_80} mm"

        eight_one = f"El peso total:"
        eight_two = f"[green]{peso_t} kg x {large} M"

        # Creditos
        nine_one = f'~pipecoding'
        nine_two = f'@luisOrtga'

        if pulgada == 0 and av_90 == 0 and av_45 == 0 and peso_d == 0 and large == 0:
            ms = "[green]No se puede calcular por falta de datos. vuelva a intentarlo."
            design.view_error(ms)
        elif large == 0 and t == 0:
            # Creditos
            # @Override
            eight_one = f'~pipecoding'
            eight_two = f'@luisOrtga'

            # Mostrar los datos
            design.view_less(one_one,one_two,two_one,two_two,three_one,three_two,four_one,four_two,five_one,five_two,six_one,six_two,seven_one,seven_two,eight_one,eight_two)
        else:
            # Mostrar los datos
            design.__view__(one_one,one_two,two_one,two_two,three_one,three_two,four_one,four_two,five_one,five_two,six_one,six_two,seven_one,seven_two,eight_one,eight_two,nine_one,nine_two)
