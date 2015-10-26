import tkinter.ttk


class View(object):
    root = None

    edit_var = None
    label_var = None
    doit_button = None

    def __init__(self):
        self.root = tkinter.Tk()

        self.root.title('Interactive Helloworld')

        x, y, w, h = 0, 0, 300, 75
        self.root.geometry('%sx%s+%s+%s' % (w, h, x, y))

        main_frame = tkinter.ttk.Frame(self.root)
        main_frame['padding'] = (5, 5)
        main_frame.pack(side='top', fill='both', expand=True)

        self.edit_var = tkinter.StringVar()
        edit = tkinter.ttk.Entry(main_frame, textvariable=self.edit_var)
        edit.pack(side='top', fill='x')

        self.label_var = tkinter.StringVar()
        label = tkinter.ttk.Label(main_frame, textvariable=self.label_var)
        label.pack(side='top', fill='x')

        self.doit_button = tkinter.ttk.Button(main_frame, text='DO IT')
        self.doit_button.pack(side='top', fill='x')

    def close(self):
        self.root.destroy()
        self.root.quit()


class Model(object):
    ui = None

    def __init__(self, view):
        self.ui = view

    def doit(self):
        text = self.ui.edit_var.get()
        self.ui.label_var.set(text)


class Ctrl(object):
    view = None
    model = None

    def __init__(self):
        self.view = View()
        self.model = Model(self.view)

        self.bind()

        self.view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
        self.view.root.mainloop()

    def bind(self):
        self.view.doit_button.bind("<Button-1>", self.doit_handler)

    def doit_handler(self, event):
        self.model.doit()

    def close_handler(self):
        self.view.close()


class App(object):
    ctrl = None

    def __init__(self):
        self.ctrl = Ctrl()


if __name__ == '__main__':
    app = App()
