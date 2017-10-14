#Tkinter adding buttons
#Tkinter menu bar

from Tkinter import *
from PIL import Image,ImageTk
class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill = BOTH, expand = 1)
        # quitButton = Button(self,text="Quit",command = self.cilent_exit)
        # quitButton.place(x=0,y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        menu.add_cascade(label='File',menu=file)
        file.add_command(label="Exit",command =self.cilent_exit)
        file.add_command(label="Save",command =self.cilent_exit)
        file.add_command(label="NEW",command =self.cilent_exit)

        edit = Menu(menu)
        menu.add_cascade(label ='Edit',menu=edit)
        edit.add_command(label = "show image",command = self.show_image)
        edit.add_command(label = "show text",command = self.show_text)

    def show_image(self):
        load = Image.open('pic.jpg')
        render = ImageTk.PhotoImage(load)

        img=Label(self,image=render)
        img.image = render
        img.place(x=0,y=0)

    def show_text(self):
        text = Label(self,text= "HeY YOU !! dogdog")
        text.pack()

    def cilent_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
