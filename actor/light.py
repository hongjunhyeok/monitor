from tkinter import *



class Light(Label):
    def __init__(self,parent,on_file = 'light_on.png',off_file='light_off.png'):
        self.on_img = PhotoImage(file =on_file)
        self.off_img = PhotoImage(file=off_file)

        super().__init__(parent,image =self.off_img,bg='black')
        #Label.__init__(self,parent)###
        self.place(x=0, y=0)
        #OFF는 False와 같은 의미를 갖는 tkinter 내부 상수
        self.status = OFF

    def get_status(self):
        return self.status


    def turn_on(self):
        self.config(image=self.on_img,bg='white')
        self.status = ON
    def turn_off(self):
        self.config(image = self.off_img,bg='black')
        self.status = OFF

def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('500x400+10+10')
    light = Light(root)
    light.turn_on()
    root.mainloop()

if __name__ == '__main__':
    main()
