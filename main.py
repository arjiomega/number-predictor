import pickle

from PIL import Image, ImageGrab
import tkinter as tk
from tkinter import ttk
import numpy as np

#loaded_model = pickle.load(open("number_predictor.sav", 'rb'))

class NumberPredictor:
    def __init__(self,container):
        self.container = container

    def get_image(self,container):
        x = container.winfo_rootx()
        y = container.winfo_rooty()

        img = ImageGrab.grab(bbox=(x+50,y+50,x+400-50,y+400-50))

        return img

    def preprocess(self,img):
        img = img.resize((28,28), resample=Image.NEAREST)
        img = np.array(img)

        #Convert to reversed binary image (blank space contains value)
        threshold = 150
        binarized = 255 * (img[:,:,0] < threshold)

        return binarized.reshape(1,-1)

    def predict(self,img_input,predict_val):
        pass
        #result = loaded_model.predict(img_input)
        #predict_val.config(text=result[0])

        #print(loaded_model.predict_proba(img_input))


class TestFrame(tk.Frame):
    def __init__(self,container):
        super().__init__(container)
        #self.number_predictor = NumberPredictor(container)

        self.frame1=tk.Frame(self,bg='#323232',width=400,height=400)
        self.frame2=tk.Frame(self,bg='#DDD0C8',width=400,height=100)
        self.frame3=tk.Frame(self,bg='white',width=75,height=75)

        self.frame1.pack(fill="both",expand=True)
        self.frame2.pack(fill="both",expand=True)

        # Display Predict
        self.frame3.place(x=300,y=415)

        self.predict_val = tk.Label(self,text="0",font=("Arial",30),bg="white")
        self.predict_val.place(x=323,y=425)

         # Buttons
        self.button1 = tk.Button(self,text="predict")#,command = lambda: self.number_predictor.predict(None, self.predict_val))
        predict_img1 = tk.PhotoImage(file=r"C:\Users\rjome\OneDrive\Desktop\GIT\tkinter_to_numpy\predict.png")
        self.button1.config(image=predict_img1)
        self.button1.place(x=55,y=425)

        self.button2 = tk.Button(self,text="clear",command=lambda:self.canvas.delete("all"))
        predict_img2 = tk.PhotoImage(file=r"C:\Users\rjome\OneDrive\Desktop\GIT\tkinter_to_numpy\clear.png")
        self.button2.config(image=predict_img2)
        self.button2.place(x=175,y=425)

        # Canvas
        self.canvas = tk.Canvas(self,width=300,height=300)
        self.canvas.place(in_=self.frame1, anchor="c",relx=0.5,rely=0.5)

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self,event):
        x = event.x
        y = event.y

        self.canvas.create_oval(x,y,x+20,y+20,fill="black")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Predictor")
        self.geometry("400x500")
        self.resizable(False,False)

if __name__ == "__main__":
    app = App()
    TestFrame(app)
    app.mainloop()