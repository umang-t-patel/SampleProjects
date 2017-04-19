from tkinter import *
import tkinter.messagebox as msg
import math

class CoefficientsDialog:
    def __init__(self, master):
        '''
        Create the window widgets
        ############################################################################
        #  Def Name     : __init__(master)
        #  Input        : parent
        #  Output       : None
        #  Purpose      : Create popup for Coefficients
        #  Author       : Umang Patel
        #  Last Modified: 04/12/2017 by Umang Patel
        ############################################################################
        '''
        self._root = master
        #This is the master window
        self.popupWindow = Toplevel(bg = 'white')
        self.popupWindow.title('Credits')
        self.popupWindow.geometry('250x200')

        self.aslabel = Label(self.popupWindow, text = 'a  ',fg='red', height=2)
        self.aslabel.grid(row = 0, column = 0,padx=5, pady=5)
        self.atext = Text(self.popupWindow, width=20, height=2)
        self.atext.grid(row = 0, column = 1,padx=5, pady=5)
        self.alabel = Label(self.popupWindow, text = 'X2     +',fg='red', height=2)
        self.alabel.grid(row = 0, column = 2,padx=5, pady=5)


        self.bslabel = Label(self.popupWindow, text = 'b  ',fg='red', height=2)
        self.bslabel.grid(row = 1, column = 0,padx=5, pady=5)
        self.btext = Text(self.popupWindow, width=20, height=2)
        self.btext.grid(row = 1, column = 1,padx=5, pady=5)
        self.blabel = Label(self.popupWindow, text = 'X     +',fg='red', height=2)
        self.blabel.grid(row = 1, column = 2,padx=5, pady=5)

        self.cslabel = Label(self.popupWindow, text = 'c  ',fg='red', height=2)
        self.cslabel.grid(row = 2, column = 0,padx=5, pady=5)
        self.ctext = Text(self.popupWindow, width=20, height=2)
        self.ctext.grid(row = 2, column = 1,padx=5, pady=5)
        self.clabel = Label(self.popupWindow, text = '', height=2)
        self.clabel.grid(row = 2, column = 2,padx=5, pady=5)

        #This is the button widget
        self.okButton = Button(self.popupWindow, text = 'Submit', command = self.submit, width = 20)
        #grid function arranges the widgets in the parent widget in a two-dimensional fashion
        self.okButton.grid(row = 3, column = 0,columnspan=2)
        self.popupWindow.grab_set()

    def submit(self, event = None):
        '''
        Handle submit button action
        ############################################################################
        #  Def Name     : submit(master)
        #  Input        : event
        #  Output       : a,b,c
        #  Purpose      : Provide output to parent for ploting
        #  Author       : Umang Patel
        #  Last Modified: 04/12/2017 by Umang Patel
        ############################################################################
        '''
        a = (self.atext.get("1.0",END)).strip()
        b = (self.btext.get("1.0",END)).strip()
        c = (self.ctext.get("1.0",END)).strip()

        if len(a) == 0:
            msg.showerror("Coefficient Empty","Coefficient 'a' cannot be  empty")
        elif len(b) == 0:
            msg.showerror("Coefficient Empty","Coefficient 'b' cannot be  empty")
        elif len(c) == 0:
            msg.showerror("Coefficient Empty","Coefficient 'c' cannot be  empty")
        elif a.lstrip('-').replace('.','',1).isdigit() and b.lstrip('-').replace('.','',1).isdigit() and c.lstrip('-').replace('.','',1).isdigit():
            if '0' == a.lstrip('-').replace('.','',1) :
                msg.showerror("Coefficient Non-zero","Coefficient 'a' cannot be 0")
            else:
                self.popupWindow.destroy()
                self.popupWindow.grab_release()
                self._root.plot_equation(int(a),int(b),int(c))
        else:
            msg.showerror("Coefficient Non-Integer","Coefficients values has to be integer")

class QuadEQPlot:
    global root
    def __init__(self):
        '''
        initialize any required data
        call init_widgets to create the UI
        ###########################################################################
        #  Def Name     : __init__()
        #  Input        : parent(instance of TK() - root Window)
        #  Output       : None
        #  Purpose      : Constructor for the Quadratic Equation Plotter GUI class
        #  Author       : Umang Patel
        #  Last Modified: 04/10/2017 by Umang Patel
        ############################################################################
        '''
        self.root = Tk()
        self.mainFrame = None
        self.canvas = None
        self.header = None
        self.dynamicyaxis = False
        self.dynamicyval = []
        self.plotlines = None
        self.plotpoints = None
        self.plotxy = []
        self.typePlot = StringVar()
        self.init_widgets()
        self.root.mainloop();

    def init_widgets(self):
        '''
        Create the window widgets and start the mainloop here
        You can call plot_axis to draw the inital x and y
        ###########################################################################
        #  Def Name     : init_widgets()
        #  Purpose      : Creates the GUI widgets in the Quadratic Equation Plotter Application
        #  Author       : Umang Patel
        #  Last Modified: 04/10/2017 by Umang Patel
        ############################################################################
        '''
        self.root.title("Quadratic Equation Plotter - Umang Patel")
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        fileMenu = Menu(menubar, tearoff = 0)
        helpMenu = Menu(menubar, tearoff = 0)

        menubar.add_cascade(label = "File", underline = 0, menu = fileMenu)
        menubar.add_cascade(label = "Help", underline = 0, menu = helpMenu)
        fileMenu.add_command(label="New Equation", command=lambda : self.new_equation())
        fileMenu.add_command(label="Save plot as .ps", command=lambda : self.save_canvas())
        fileMenu.add_command(label="Clear", command=lambda : self.clear_canvas())
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", underline = 0, command =lambda: self.exit())
        helpMenu.add_command(label = "About", underline = 0, command=lambda : self.show_help_about())

        self.headerFrame = Frame(self.root, {'width' : 900,'height' : 40,'relief' : RAISED, 'borderwidth' : 5}, bg='#d9d9d9')
        self.headerFrame.grid({'row' : 0, 'column' : 0})
        self.headerFrame.pack_propagate(False)

        self.lblheader = Label(self.headerFrame, text = 'No Equation', bg='#d9d9d9')
        self.lblheader.grid({'row' : 0, 'column' : 0})
        self.lblheader.pack(side=LEFT)

        self.rdpoints = Radiobutton(self.headerFrame, text = 'Points', bg='#d9d9d9',value="point",variable = self.typePlot,command=lambda : self.plot_points(self.plotxy))
        self.rdpoints.grid({'row' : 0, 'column' : 1})
        self.rdpoints.pack(side=RIGHT)

        self.rdline = Radiobutton(self.headerFrame, text = 'Line', bg='#d9d9d9',value="line",variable = self.typePlot,command=lambda : self.plot_line(self.plotxy))
        self.rdline.grid({'row' : 0, 'column' : 2})
        self.rdline.pack(side=RIGHT)
        self.typePlot.set("line")


        self.mainFrame = Frame(self.root, {'width' : 900, 'height' : 600,'relief' : RAISED, 'borderwidth' : 5})
        self.mainFrame.grid({'row' : 1, 'column' : 0})
        self.mainFrame.pack_propagate(False)
        self.canvas = Canvas(self.mainFrame, {'width' : 900, 'height' : 600})
        self.canvas.pack(fill=BOTH, expand=1, anchor=CENTER)
        self.plot_axis()

    def plot_axis(self):
        '''
        Draw x and y axis in the middle of the canvas
        ###########################################################################
        #  Def Name     : plot_axis()
        #  Output       : None
        #  Purpose      : Creates the x and y axis in the Quadratic Equation Plotter Application
        #  Author       : Umang Patel
        #  Last Modified: 04/10/2017 by Umang Patel
        ############################################################################
        '''
        if self.dynamicyval:
            self.canvas.create_line(450,300,700,300, width=2, fill="blue")
            self.canvas.create_line(450,300,200,300, width=2, fill="blue")
            self.canvas.create_text(439.5,301.5, text='0', anchor=N)
            for i in range(1,6):
                x = 450 + (i * 45)
                #print("x",x)
                self.canvas.create_line(x,297.5,x,302.5, width=2, fill="blue")
                self.canvas.create_text(x,301.5, text='%d'% (i), anchor=N)
                x = 450 - (i * 45)
                #print("x",x)
                self.canvas.create_line(x,297.5,x,302.5, width=2, fill="blue")
                self.canvas.create_text(x,301.5, text='-%d'% (i), anchor=N)
            starty = int(math.ceil((max(self.dynamicyval)-300) / 45.0)) * 45
            self.canvas.create_line(450,300,450,550, width=2, fill="blue")
            self.canvas.create_line(450,300,450,50, width=2, fill="blue")
            print(starty)
            print(starty/45)
            for i in range(1,int(starty/45)):
                y = 300 - (i * 45)
                self.canvas.create_line(447.5,y,452.5,y, width=2, fill="blue")
                self.canvas.create_text(439.5,y, text='%d'% (i), anchor=N)
                #print("y",y)
                y = 300 + (i * 45)
                self.canvas.create_line(447.5,y,452.5,y, width=2, fill="blue")
                self.canvas.create_text(439.5,y, text='-%d'% (i), anchor=N)
        else:
            self.canvas.create_line(450,300,700,300, width=2, fill="blue")
            self.canvas.create_line(450,300,200,300, width=2, fill="blue")
            self.canvas.create_line(450,300,450,550, width=2, fill="blue")
            self.canvas.create_line(450,300,450,50, width=2, fill="blue")
            self.canvas.create_text(439.5,301.5, text='0', anchor=N)
            for i in range(1,6):
                x = 450 + (i * 45)
                #print("x",x)
                self.canvas.create_line(x,297.5,x,302.5, width=2, fill="blue")
                self.canvas.create_text(x,301.5, text='%d'% (i), anchor=N)
                x = 450 - (i * 45)
                #print("x",x)
                self.canvas.create_line(x,297.5,x,302.5, width=2, fill="blue")
                self.canvas.create_text(x,301.5, text='-%d'% (i), anchor=N)
                y = 300 - (i * 45)
                self.canvas.create_line(447.5,y,452.5,y, width=2, fill="blue")
                self.canvas.create_text(439.5,y, text='%d'% (i), anchor=N)
                #print("y",y)
                y = 300 + (i * 45)
                self.canvas.create_line(447.5,y,452.5,y, width=2, fill="blue")
                self.canvas.create_text(439.5,y, text='-%d'% (i), anchor=N)
            #print("y",y)
    def plot_equation(self,*args):
        '''
        plot the equation on canvas
        first clean the canvas, call plot_axis, calculate y values, and call either plot_points or plot_line
        ############################################################################
        #  Def Name     : plot_equation(*args)
        #  Input        : *args
        #  Output       : plot_line,plot_points
        #  Purpose      : Create the X and Y values and then call plot_line and plot_points based on the radio button selection
        #  Author       : Umang Patel
        #  Last Modified: 04/12/2017 by Umang Patel
        ############################################################################
        '''
        self.clear_canvas()
        a = args[0]
        b = args[1]
        c = args[2]
        self.lblheader.config(text="{0}X\u00b2 + {1}X + {2}".format(a,b,c))
        x=-5.0
        xy = []
        while (x<=5):
            xy.append(x*45 + 450)
            xy.append(300 - (a*(x**2) +b*x +c)*45/5)
            x+=0.1
        self.plotxy = xy
        if abs(xy[-1]) > 576 or abs(xy[1]) > 576 or abs(xy[-1]) < 75 or abs(xy[1]) < 75:
            self.dynamicyaxis = True
            self.dynamicyval = []
            self.dynamicyval.append(abs(xy[-1]))
            self.dynamicyval.append(abs(xy[1]))
            self.plot_axis()
        if self.typePlot.get() == "line":
            self.plot_line(self.plotxy)
        elif self.typePlot.get() == "points":
            self.plot_points(self.plotxy)
    def plot_points(self,scaled_points):
        '''
        for each x and y points, plot a 2x2 oval shape with a red border and yellow fill
        ############################################################################
        #  Def Name     : plot_points(scaled_points)
        #  Input        : scaled_points
        #  Output       : None
        #  Purpose      : Create points using create_oval function from canvas
        #  Author       : Umang Patel
        #  Last Modified: 04/12/2017 by Umang Patel
        ############################################################################
        '''
        print(scaled_points)
        print(len(scaled_points))
        if len(scaled_points) > 1:
            self.canvas.delete(self.plotlines)
            self.canvas.delete(self.plotpoints)
            for i in range(0,len(scaled_points),20):
                self.plotlines = self.canvas.create_oval(scaled_points[i],scaled_points[i+1],scaled_points[i]-3,scaled_points[i+1]-3,outline='red', fill='yellow')

    def plot_line(self,*scaled_points):
        '''
        using the (x, y) points, plot a smooth red line
        ############################################################################
        #  Def Name     : plot_line(scaled_points)
        #  Input        : scaled_points
        #  Output       : None
        #  Purpose      : Create points using create_line function from canvas
        #  Author       : Umang Patel
        #  Last Modified: 04/12/2017 by Umang Patel
        ############################################################################
        '''
        print(scaled_points[0])
        print(len(scaled_points[0]))
        if len(scaled_points[0]) > 1:
            self.canvas.delete(self.plotlines)
            self.canvas.delete(self.plotpoints)
            self.plotlines = self.canvas.create_line(scaled_points[0], fill='red')
    def clear_canvas(self):
        '''
        triggered when the menu command 'Clear' is clicked
        delete everything from the canvas and set the coefficients to 0's
        ############################################################################
        #  Def Name     : clear_canvas()
        #  Input        : None
        #  Output       : None
        #  Purpose      : Reset the GUI and create fresh GUI
        #  Author       : Umang Patel
        #  Last Modified: 04/12/2017 by Umang Patel
        ############################################################################
        '''
        self.typePlot.set("line")
        self.lblheader.config(text="No Equation")
        self.canvas.delete('all')
        self.plot_axis()

    def new_equation(self):
        '''
        triggered when the menu command 'New Equation' is clicked
        call the child window to get the equation coefficients and then call plot_equation
        ############################################################################
        #  Def Name     : new_equation()
        #  Input        : None
        #  Output       : New popupWindow
        #  Purpose      : Pop up new window for putting Coefficients
        #  Author       : Umang Patel
        #  Last Modified: 04/11/2017 by Umang Patel
        ############################################################################
        '''
        CoefficientsDialog(self)

    def save_canvas(self):
        '''
        triggered when the menu command 'Save plot as .PS' is clicked
        save the graph as '{your_student_id_number}.ps'
        ############################################################################
        #  Def Name     : onExit()
        #  Input        : None
        #  Output       : None
        #  Purpose      : Exit from the GUI
        #  Author       : Umang Patel
        #  Last Modified: 04/10/2017 by Umang Patel
        ############################################################################
        '''
        if self.plotxy:
            pass
        self.canvas.postscript(file="1002534.ps", colormode='color')

    def exit(self):
        '''
        triggered when the menu command 'Exit' is clicked
        Ask if the user is sure about exiting the application and if the answer is yes then quit the main window
        ############################################################################
        #  Def Name     : exit()
        #  Input        : None
        #  Output       : None
        #  Purpose      : Exit from the application
        #  Author       : Umang Patel
        #  Last Modified: 04/10/2017 by Umang Patel
        ############################################################################
        '''
        result = msg.askquestion("Exit", "Are you sure you want to exit?", icon='question')
        if result == 'yes':
            self.root.destroy()

    def show_help_about(self):
        '''
        triggered when the menu command 'About' is clicked
        Show an information dialog displaying your name on one line and id number on the second
        ############################################################################
        #  Def Name     : show_help_about()
        #  Input        : None
        #  Output       : None
        #  Purpose      : Show message popup for who create application
        #  Author       : Umang Patel
        #  Last Modified: 04/10/2017 by Umang Patel
        ############################################################################
        '''
        msg.showinfo('About QuadEQPlot', 'Created By: Umang Patel \nID: 1002534')
parent = QuadEQPlot()
