def e_find_sublista_suma_mayor(lista):
    largest_sum = float('-inf')  # Inicializa la suma más grande con infinito negativo.
    start_sub_list = 0  # Índice del inicio de la sublista con mayor suma.
    end_sublist = 0  #Índice del final de la sublista con la suma mayor.
    current_sum = 0  # Suma actual de la sublista considerada.
    best_sublist_start = 0  # Índice del inicio de la mejor sublista encontrada hasta el momento.

    for i, number in enumerate(lista):  # Itera a través de la lista de números.
        current_sum += number  # Agrega el número actual a la suma actual.

        if current_sum > largest_sum:  #        if current_sum > largest_sum:  

            largest_sum = current_sum
            start_sub_list = best_sublist_start  # Actualiza el inicio de la sublista.
            end_sublist = i

        if current_sum < 0:  # Restablece la suma actual si se vuelve negativa.
            current_sum = 0
            best_sublist_start = i + 1

    return lista[start_sub_list:end_sublist + 1]  # Devuelve la sublista con la suma más grande.