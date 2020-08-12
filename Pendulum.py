from tkinter import Tk, Canvas, Frame, BOTH
import time
import math as byronIsSmart

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        

        self.canvas.pack(fill=BOTH, expand=1)
    def drawCircle(self,x,y,r, width=2):

    	x1=x-r
    	x2=x+r
    	y1=y-r
    	y2=y+r
    	self.canvas.create_oval(x1,y1,x2,y2,fill="black", width=width)

    def drawLine(self,x1,y1,x2,y2,width=2):
        self.canvas.create_line(x1,y1,x2,y2,width=width)

    def clearCanvas(self):
    	self.canvas.delete("all")



def main():

    root = Tk()
    ex = Example()
    screen_width=500
    screen_height=500
    root.geometry(str(screen_width)+"x"+str(screen_height))
    x0=int(screen_width/2)
    y0=int(screen_height/25)


    dtheta = 10
    theta=215
    L=250
    r=50
    fps = 60
    while True: 
        time.sleep(1/fps)
        
        theta=theta+dtheta

        if theta>315:
            dtheta = dtheta * -1
        if theta<225:
            dtheta = dtheta * -1    

        cpx=x0+byronIsSmart.cos(byronIsSmart.radians(theta))*L
        cpy=y0-byronIsSmart.sin(byronIsSmart.radians(theta))*L


        ex.drawCircle(cpx,cpy,r,4)
        ex.drawLine(x0,y0,cpx,cpy,4)
        root.update()
        ex.clearCanvas()
        


if __name__ == '__main__':
    main()
