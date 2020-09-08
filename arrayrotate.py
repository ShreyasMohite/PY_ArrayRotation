from tkinter import *
import tkinter.messagebox

class array_rotate():
    def __init__(self,root):
        self.root=root
        self.root.title("ArrayRotation")
        self.root.geometry("500x400")
        self.root.resizable(0,0)

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()


        Array1=IntVar()
        Array2=IntVar()
        Array3=IntVar()
        Array4=IntVar()
        Array5=IntVar()
        Array6=IntVar()
        Array7=IntVar()
        sizeofarray=IntVar()
        rotatebyarray=IntVar()

        Array11=IntVar()
        Array22=IntVar()
        Array33=IntVar()
        Array44=IntVar()
        Array55=IntVar()
        Array66=IntVar()
        Array77=IntVar()
        




        def openA():
            if(var1.get()==1):
                Ent_A.config(state="normal")
                Array1.set("")
            else:
                Ent_A.config(state="disable")

        def openB():
            if(var2.get()==1):
                Ent_B.config(state="normal")
                Array2.set("")
            else:
                Ent_B.config(state="disable")

        def openC():
            if(var3.get()==1):
                Ent_C.config(state="normal")
                Array3.set("")
            else:
                Ent_C.config(state="disable")

        def openD():
            if(var4.get()==1):
                Ent_D.config(state="normal")
                Array4.set("")
            else:
                Ent_D.config(state="disable")


        def openE():
            if(var5.get()==1):
                Ent_E.config(state="normal")
                #Array5.set("")
            else:
                Ent_E.config(state="disable")

        def openF():
            if(var6.get()==1):
                Ent_F.config(state="normal")
                #Array6.set("")
            else:
                Ent_F.config(state="disable")

        
        def openG():
            if(var7.get()==1):
                Ent_G.config(state="normal")
                #,Array7.set("")
            else:
                Ent_G.config(state="disable")

        def on_enter(e):
            But_rotatearray['background']="black"
            But_rotatearray['foreground']="cyan"
               
               

        def on_leave(e):
            But_rotatearray['background']="SystemButtonFace"
            But_rotatearray['foreground']="SystemButtonText"
        
        def on_enter1(e):
            But_reset['background']="black"
            But_reset['foreground']="cyan"
               
               

        def on_leave2(e):
            But_reset['background']="SystemButtonFace"
            But_reset['foreground']="SystemButtonText"

            #But_reset

        
        def rotatebynumber():
            try:
                arr=[Array1.get(),Array2.get(),Array3.get(),Array4.get(),Array5.get(),Array6.get(),Array7.get()]
                mod=rotatebyarray.get()%sizeofarray.get()
                Array11.set(arr[(mod+0)%sizeofarray.get()])
                Array22.set(arr[(mod+1)%sizeofarray.get()])
                Array33.set(arr[(mod+2)%sizeofarray.get()])
                Array44.set(arr[(mod+3)%sizeofarray.get()])
                Array55.set(arr[(mod+4)%sizeofarray.get()])
                Array66.set(arr[(mod+5)%sizeofarray.get()])
                Array77.set(arr[(mod+6)%sizeofarray.get()])
            except:
                tkinter.messagebox.askretrycancel("Information","Please Insert Some Inputs",icon="info")

        def reset():
            Array11.set(0)
            Array22.set(0)
            Array33.set(0)
            Array44.set(0)
            Array55.set(0)
            Array66.set(0)
            Array77.set(0)
            Array1.set(0)
            Array2.set(0)
            Array3.set(0)
            Array4.set(0)
            Array5.set(0)
            Array6.set(0)
            Array7.set(0)
            Ent_A.config(state="disable")
            Ent_B.config(state="disable")
            Ent_C.config(state="disable")
            Ent_D.config(state="disable")
            Ent_E.config(state="disable")
            Ent_F.config(state="disable")
            Ent_G.config(state="disable")
            sizeofarray.set("")
            rotatebyarray.set("")
            

            


        




        #Frm==========================
        Main_Frame=Frame(self.root,width=500,height=400,bg="#17354d",relief=RIDGE,bd=3)
        Main_Frame.place(x=0,y=0)

        Top_Frame=Frame(Main_Frame,width=495,height=250,bd=3,relief=RIDGE)
        Top_Frame.place(x=0,y=0)
        
        Bottom_Frame=Frame(Main_Frame,width=495,height=143,bg="#074b45",bd=3,relief=RIDGE)
        Bottom_Frame.place(x=0,y=250)

        #============================LabelFrame==============================
        lab_frame_top=LabelFrame(Top_Frame,width=490,height=245,text="Insert Array Elements",bg="#17354d",fg="white")
        lab_frame_top.place(x=0,y=0)

        lab_frame_bottom=LabelFrame(Bottom_Frame,width=490,height=137,text="Array Rotaions",bg="#074b45",fg="white")
        lab_frame_bottom.place(x=0,y=0)

        #=====================lab_frame_top==================================
        lab_sizeofarray=Label(lab_frame_top,text="Size of Array :",font=('times new roman',14,'bold'),fg="white",bg="#17354d")
        lab_sizeofarray.place(x=10,y=20)

        lab_arrayrotation=Label(lab_frame_top,text="Array Rotation By :",font=('times new roman',14,'bold'),fg="white",bg="#17354d")
        lab_arrayrotation.place(x=240,y=20)

        ent_sizeofarray=Entry(lab_frame_top,width=5,font=('times new roman',12,'bold'),relief=RIDGE,bd=3,textvariable=sizeofarray)
        ent_sizeofarray.place(x=140,y=25)

        ent_arrayrotation=Entry(lab_frame_top,width=5,font=('times new roman',12,'bold'),relief=RIDGE,bd=3,textvariable=rotatebyarray)
        ent_arrayrotation.place(x=420,y=25)
        
        chk_A=Checkbutton(lab_frame_top,text="A",fg="white",variable=var1,bg="#17354d",onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openA)
        chk_A.place(x=20,y=130)

        Ent_A=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array1,state="disable")
        Ent_A.place(x=20,y=90)

        chk_B=Checkbutton(lab_frame_top,text="B",fg="white",bg="#17354d",variable=var2,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openB)
        chk_B.place(x=90,y=130)

        Ent_B=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array2,state="disable")
        Ent_B.place(x=90,y=90)

        chk_C=Checkbutton(lab_frame_top,text="C",fg="white",bg="#17354d",variable=var3,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openC)
        chk_C.place(x=160,y=130)

        Ent_C=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array3,state="disable")
        Ent_C.place(x=160,y=90)

        chk_D=Checkbutton(lab_frame_top,text="D",fg="white",bg="#17354d",variable=var4,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openD)
        chk_D.place(x=230,y=130)

        Ent_D=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array4,state="disable")
        Ent_D.place(x=230,y=90)

        chk_E=Checkbutton(lab_frame_top,text="E",fg="white",bg="#17354d",variable=var5,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openE)
        chk_E.place(x=300,y=130)

        Ent_E=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array5,state="disable")
        Ent_E.place(x=300,y=90)

        chk_F=Checkbutton(lab_frame_top,text="F",fg="white",bg="#17354d",variable=var6,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openF)
        chk_F.place(x=370,y=130)

        Ent_F=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array6,state="disable")
        Ent_F.place(x=370,y=90)

        chk_G=Checkbutton(lab_frame_top,text="G",fg="white",bg="#17354d",variable=var7,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openG)
        chk_G.place(x=440,y=130)

        Ent_G=Entry(lab_frame_top,width=3,font=('times new roman',12,'bold'),textvariable=Array7,state="disable")
        Ent_G.place(x=440,y=90)

        But_rotatearray=Button(lab_frame_top,width=20,font=('times new roman',12,'bold'),text="Rotate Array",command=rotatebynumber,cursor="hand2")
        But_rotatearray.place(x=40,y=180)
        But_rotatearray.bind("<Enter>",on_enter)
        But_rotatearray.bind("<Leave>",on_leave)

        But_reset=Button(lab_frame_top,width=20,font=('times new roman',12,'bold'),text="Reset",command=reset,cursor="hand2")
        But_reset.place(x=260,y=180)
        But_reset.bind("<Enter>",on_enter1)
        But_reset.bind("<Leave>",on_leave2)



        #==================Label_frame_bottom========================================
        EntA=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array11,state="disable")
        EntA.place(x=20,y=30)

        labA=Label(lab_frame_bottom,text="A",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labA.place(x=25,y=70)

        EntB=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array22,state="disable")
        EntB.place(x=95,y=30)

        labB=Label(lab_frame_bottom,text="B",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labB.place(x=95,y=70)

        EntC=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array33,state="disable")
        EntC.place(x=165,y=30)

        labC=Label(lab_frame_bottom,text="C",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labC.place(x=165,y=70)

        EntD=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array44,state="disable")
        EntD.place(x=235,y=30)

        labD=Label(lab_frame_bottom,text="D",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labD.place(x=235,y=70)

        EntE=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array55,state="disable")
        EntE.place(x=305,y=30)

        labE=Label(lab_frame_bottom,text="E",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labE.place(x=305,y=70)

        EntF=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array66,state="disable")
        EntF.place(x=375,y=30)

        labF=Label(lab_frame_bottom,text="F",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labF.place(x=375,y=70)

        EntG=Entry(lab_frame_bottom,width=3,font=('times new roman',12,'bold'),textvariable=Array77,state="disable")
        EntG.place(x=445,y=30)

        labG=Label(lab_frame_bottom,text="G",font=('times new roman',12,'bold'),bg="#074b45",fg="white")
        labG.place(x=445,y=70)

        #============================================================================

        

       




if __name__ == "__main__":
    root=Tk()
    app=array_rotate(root)
    root.mainloop()
