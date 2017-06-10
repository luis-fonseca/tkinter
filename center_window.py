def center_window(window_toplevel):
    # atualiza os valores relacionados ao tamanho da janela
    window_toplevel.update_idletasks()

    window_size   = window_toplevel.geometry().split("+")
    window_width  = int(window_size[0].split("x")[0])
    window_height = int(window_size[0].split("x")[1])

    screen_width  = window_toplevel.winfo_screenwidth()
    screen_height = window_toplevel.winfo_screenheight()

    x_position    = int((screen_width - window_width) / 2)
    y_position    = int((screen_height - window_height) / 2)
    
    window_toplevel.geometry("{0}x{1}+{2}+{3}".format(
        window_width, window_height, x_position, y_position))
