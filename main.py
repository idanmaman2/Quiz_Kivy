import tkinter as x
import kivy  # Required to run Kivy such as the next line of code
kivy.require('1.9.1')  # used to alert user if this code is run on an earlier version of Kivy.
from kivy.app import App 
from kivy.animation import Animation# Imports the base App class required for Kivy Apps
from kivy.lang import Builder  # Imports the KV language builder that provides the layout of kivy screens
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout  import FloatLayout
from kivy.uix.stacklayout  import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen  # Imports the Kivy Screen manager and Kivys Screen class
from kivy.core.text import LabelBase
import os

full_path = os.path.realpath(__file__)
path = os.path.split(full_path)
path2=path[0]
LabelBase.register(name="Arial", fn_regular=path2 +"//arial.ttf")
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.properties import StringProperty
import time

import math
import random
from kivy.network.urlrequest import UrlRequest
from kivy.graphics import Rectangle, Color 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Line
from functools import partial
from kivy.core.window import Window
import csv
from kivy.core.audio import SoundLoader
from collections import deque
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
lastpoint=(0,0)
from kivy.base import runTouchApp
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory



from kivy.uix.label import Label
Factory.unregister('ActionPrevious')
name=""
hello=True
arrlen=[]
check=True

Builder.load_file(path2+'//kivi.kv')






    

class Touch(FloatLayout ):
    image_source = StringProperty(path2+"//source1.jpg")
     
    def __init__(self, **kwargs):
        
        self.true= -1 
        Window.size=(480*0.8 , 883*0.8)
        self.stimer=8
        self.name=""
        self.timer=30
        self.sc=False 
        self.should=""
        self.all=""
        self.already=False 
        self.q=0
        self.a=0
        self.elf=True
        self.options= [] 
        self.indexofright=0 
        with open(r'D:\aramheb.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.list= list(csv_reader)
 
        
        super().__init__(**kwargs)
      

        
    def Next(self):
       
        self.timer=30
        self.sc=False 
        self.q+=1
        self.ids.points.text=str(self.a)+'/'+str(self.q)
        
        self.already=False
     
        
   
        func = [self.ids.slv1,self.ids.slv2,self.ids.slv3,self.ids.slv4] 
        randomn= random.randint(0,len(self.list))
        a=self.list[randomn]
        a2=self.list[randomn][2]
        options= [random.choice( self.list)[2]  for i in range(3) ]  
        options .append(a2)
        mixed= [] 
        for i in range(4): 
            mixed.append(random.choice(options))
            options.pop( options.index(mixed[i])) 
        for i in range(4): 
            func[i].text=mixed[i]
        print(mixed)
        print(a)
        alpabeta= [chr ( ord(u'א')+ i ) for i in range(22) ] 
        alpabeta+= ' '
        alpabeta += ',' 
        alpabeta += ';'
        a=''.join([ch if ch in alpabeta else '' for ch in a])   
        #r=x.Tk()
        #x.Label(r,text=a, font="arial 45 ").pack() 
        #r.mainloop() 
                
        result= a.split(" ")
            
        for i in range(len(result)):
            result[i]=result[i][::-1]
               
        result=" ".join(result)
         
                       
        result2= a2.split(" ")
            
        for i in range(len(result2)):
            result2[i]=result2[i][::-1]
               
        result2=" ".join(result)

        self.ids.sen.text=(result) 

     
        for i in range(4): 
                    result2= a2.split(" ")
            
        for i in range(len(result2)):
            result2[i]=result2[i][::-1]
               
        result2=" ".join(result)

        self.ids.sen.text=(result) 
        
     
  
    def Solve(self, num ):
        print(num)
        self.Next( )
        self.timer=30 
        self.stimer=8 
        self.sc=True 
  
      
       
     
        self.ids.points.text=str(self.a)+'/'+str(self.q)
     
            
      
    def clear_anddo(self,*args): 
        

        sound = SoundLoader.load(path2+"//sound2.mid")
        if(sound):
            sound.play() 
        self.image_source = path2+"//idhm.png" 
        self.ids.sen.text= " "
        self.ids.timer.text=" " 
        self.ids.slv1.background_color= [0,0,0,0]
        self.ids.slv2.background_color= [0,0,0,0]
        self.ids.slv3.background_color= [0,0,0,0]
        self.ids.slv4.background_color= [0,0,0,0]
        self.ids.sen.background_color= [0,0,0,0]
        self.ids.spacy.background_color=[0,0,0,0]
        self.ids.points.background_color= [0,0,0,0]
        self.ids.timer.background_color= [0,0,0,0]
        
        
    def ddo(self,*args):
        self.image_source=path2+"//source1.jpg" 
        self.ids.sen.text="© idan's quiz ©"
 
        self.ids.points.text=str(self.a)+'/'+str(self.q)
        self.ids.sen.font_size=  (self.size)[1] * self.size[0]*0.04
        self.ids.slv1.background_color= [0,0,0,0.60]
        self.ids.slv2.background_color= [0,0,0,0.60]
        self.ids.slv3.background_color= [0,0,0,0.60]
        self.ids.slv4.background_color=[0,0,0,0.60]
        self.ids.sen.background_color= [0,0,0,0.60]
        self.ids.points.background_color= [0,0,0,0.60]
        self.ids.timer.background_color= [0,0,0,0.60]
        self.ids.spacy.background_color=[1,0,0,0.8]
            

    def update(self,*args): 
        if(self.elf==True):
            anim = Animation(pos=(80, 10))
            anim &= Animation(size=(800, 800), duration=20.)
            anim.start(self.ids.spacy)
            Animation.stop_all(self.ids.spacy, 'x')
            with self.canvas:
                
                self.ids.slv1.text=u"האבה הלאש"
    
                self.ids.points.text=u"תודוקנ"
                self.ids.sen.text=u'ןממ ןדיע - יינב לכ לע ןודיח' 
                Color(0,0,0,0.5)
                Rectangle(pos=self.ids.points.pos , size=self.ids.points.size)
                Rectangle(pos=self.ids.timer.pos ,size=self.ids.timer.size )
            with self.canvas:
                Color(1,0,0,0.8)
                Rectangle(pos=self.ids.spacy.pos ,size=self.ids.spacy.size )
                Rectangle(pos=self.ids.spacy2.pos ,size=self.ids.spacy2.size )
                
                self.elf=False 
        if (not(self.sc)):
          self.timer-=1
          self.ids.timer.text=(str(self.timer)+" sec")
          if(self.timer==0 and not(self.sc)):
        
              self.timer=30
              self.sc=False  
              self.Next()
              return 
              
          self.ids.sen.font_size=Window.size [1]*0.04
    

        else:
            self.stimer-=1
            self.ids.timer.text=(str(self.stimer)+" sec")
            if(self.stimer==0 ):
            
              self.timer=30
              self.stimer=8
              self.sc=False  
              self.Next()
              return 


    
class Quiz(App):

    def build(self):
        a=Touch()
       
        
        a2= lambda *args : ( Clock.schedule_interval(a.update,1))
        Clock.schedule_once(a.clear_anddo)
        Clock.schedule_once(a.ddo,2.4)
        Clock.schedule_once(a2, 2.2)
    
    
        return a;




class MainWindow(FloatLayout):
    pass


if __name__ == "__main__":
    
 
    Quiz().run()
    
    #Mainscreen().run()
