# Purpose: frame for graphing with matplotlib using tkinter
from tkinter import *
from Math_Functions import *
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


# use np sin and cos in graphing, math.sin and math.cos will not work


class Graph:
    def __init__(self):
        # Tkinter window
        self.__window = Tk()
        self.__window.title('Graphing plot')
        self.__window.geometry("500x500")

    def getWindow(self):
        return self.__window

    # tkinter window plot func
    def plot(self, exq, isY):
        # figure
        fig = Figure(figsize=(5, 5), dpi=100)

        """
        To do:
            match case for exp searching for "^" and all np math funcs to return

            create y and x axis on the graph itself
            show me which variables changes to MIN AND MAX of X and Y
            create a grid
            search function (allow user to find Min and Max and intersections)
        """

        # assumes other variable is unchanged; user has no way to add = in an expression
        if not isY:
            x = np.linspace(-2, 2, 100)
            y = eval(exq)
        else:
            y = np.linspace(-2, 2, 100)
            x = eval(exq)

        # add graphing plot
        plot1 = fig.add_subplot()
        # plot
        plot1.plot(x, y)
        plot1.grid(True, which="both")
        plot1.axhline(y=0, color="k")
        plot1.axvline(x=0, color="k")
        # draw to tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.getWindow())
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self.getWindow())
        toolbar.update()
        canvas.get_tk_widget().pack()
        # run gui loop
        self.getWindow().mainloop()


if __name__ == "__main__":
    GRAPH = Graph()
    GRAPH.plot("x ** 2", False)  # example
