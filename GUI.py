import tkinter as tk

class RobotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robot Wally")
        self.geometry("400x300")

        self.label_status = tk.Label(self, text="Estado actual: INICIO")
        self.label_status.pack()

        self.button_start = tk.Button(self, text="Iniciar", command=self.start)
        self.button_start.pack()

        self.button_stop = tk.Button(self, text="Detener", command=self.stop, state=tk.DISABLED)
        self.button_stop.pack()

        self.button_release = tk.Button(self, text="Soltar objeto", command=self.release_object)
        self.button_release.pack()

        self.button_object_moved = tk.Button(self, text="Objeto movido", command=self.object_moved)
        self.button_object_moved.pack()

        self.button_unreachable_position = tk.Button(self, text="Posición inalcanzable", command=self.unreachable_position)
        self.button_unreachable_position.pack()

        self.button_emergency_stop = tk.Button(self, text="Parada de emergencia", command=self.emergency_stop)
        self.button_emergency_stop.pack()

        self.button_continue = tk.Button(self, text="Continuar", command=self.continue_operation)
        self.button_continue.pack()

        self.button_change_category = tk.Button(self, text="Cambiar categoría", command=self.change_category)
        self.button_change_category.pack()

        self.button_reach_container = tk.Button(self, text="Llegar al contenedor", command=self.reach_container)
        self.button_reach_container.pack()

        self.button_no_objects = tk.Button(self, text="No hay más objetos", command=self.no_more_objects)
        self.button_no_objects.pack()

        self.button_camera_disconnected = tk.Button(self, text="Cámara desconectada", command=self.camera_disconnected)
        self.button_camera_disconnected.pack()

        self.button_grab_failed = tk.Button(self, text="Agarre fallido", command=self.grab_failed)
        self.button_grab_failed.pack()

        self.button_change_to_bottle = tk.Button(self, text="Cambiar a botella", command=self.change_to_bottle)
        self.button_change_to_bottle.pack()

    def start(self):
        self.label_status.config(text="Estado actual: EXPLORAR")
        self.button_start.config(state=tk.DISABLED)
        self.button_stop.config(state=tk.NORMAL)

    def stop(self):
        self.label_status.config(text="Estado actual: DETENIDO")
        self.button_start.config(state=tk.NORMAL)
        self.button_stop.config(state=tk.DISABLED)

    def release_object(self):
        self.label_status.config(text="Evento: Objeto soltado")

    def object_moved(self):
        self.label_status.config(text="Evento: Objeto movido")

    def unreachable_position(self):
        self.label_status.config(text="Evento: Posición inalcanzable")

    def emergency_stop(self):
        self.label_status.config(text="Evento: Parada de emergencia")

    def continue_operation(self):
        self.label_status.config(text="Evento: Continuar")

    def change_category(self):
        self.label_status.config(text="Evento: Cambiar categoría")

    def reach_container(self):
        self.label_status.config(text="Evento: Llegar al contenedor")

    def no_more_objects(self):
        self.label_status.config(text="Evento: No hay más objetos")

    def camera_disconnected(self):
        self.label_status.config(text="Evento: Cámara desconectada")

    def grab_failed(self):
        self.label_status.config(text="Evento: Agarre fallido")

    def change_to_bottle(self):
        self.label_status.config(text="Evento: Cambiar a botella")

if __name__ == "__main__":
    gui = RobotGUI()
    gui.mainloop()
