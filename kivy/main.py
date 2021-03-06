from random import choice
import cPickle
import kivy
import sys

datafile=open("element.dat")
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
class findout(object):
    def __init__(self):
        self.data={}
        self.data=cPickle.load(datafile)   
        self.listdata=list(self.data)
        self.header="the %s of %s is %s"
        self.title="\t%s"
        self.head="%s\t %s"
        self.result= "%s \t %s"
        self.label="item"
        self.slabel="value"
        self.full_names="atomic number:","boiling point:", "melting point:","relative atomic mass:","state:","symbol:"
        self.numbers=[118,110,108,100,92,86,78,76,68,60,54,46,44,36,28,26,18,10,2,]
        self.transitionalmetals=range(21,31)+range(39,49)+range(57,81)+range(89,119)
        
    def choosennumber(self,number):
        self.number=number
        for i in self.numbers:
            if int(self.number)-int(i)>0<=8:
                return i
        
            
            
                
    def grouppp(self,atomicno):
        self.atomicno=atomicno
        if  self.atomicno in list(self.transitionalmetals):
            self.group="transitionalmetal"
        else:
            self.group=int(self.atomicno)-int(findout.choosennumber(self,self.atomicno))
        return str(self.group)    
           
        
        
        
        
        
        
        
        
        
    def lookup(self,element):
        self.answer=[]
        
        try:
            self.x=element.lower().strip()
            self.required=sorted(self.data[self.x].items())
            for i in self.required:
                self.answer.append(i[1]) 
            return self.answer           
        except TypeError:
            self.x="carbon"
            self.required=sorted(self.data[self.x].items())
            for i in self.required:
                self.answer.append(i[1]) 
            return self.answer 
        except KeyError:
            self.x="carbon"
            self.required=sorted(self.data[self.x].items())
            for i in self.required:
                self.answer.append(i[1]) 
            return self.answer            
            
            
        
    def read(self):
        self.choosen=choice(self.listdata)
        self.item={}        
        self.item=self.choosen
        self.found=self.data[self.item].items()
        self.new_got=[]
        self.got=sorted(self.found)
        for i in self.got:
            self.tuple2=i[1]
            self.new_got.append(self.tuple2)
        self.new_got.append(self.choosen)
        return  self.new_got   
        
    def quit(self):
        return sys.exit()
        
    def AskQuestion(self):
        self.choosen=choice(self.listdata)
        return self.choosen
        
            
        
        
    def Giveanswer(self,atomicnumber,boilingpoint,meltingpoint,relativeatomicmass,state,symbol):
        
        self.ful=(atomicnumber,boilingpoint,meltingpoint,relativeatomicmass,state,symbol)
        self.new_fullnames=list(self.ful)
        
        return self.new_fullnames
    def MarkAnswer(self,choosen,newfullnames):
        self.item={}        
        self.item=choosen
        self.found=self.data[self.item].items()
        self.new_got=[]
        self.got=sorted(self.found)
        self.answ=[]
        for i in self.got:
            self.tuple2=i[1]
            self.new_got.append(self.tuple2)
       
            
        self.tuplelist=zip(self.full_names,self.new_got,newfullnames) 
        for i in self.tuplelist:
            if i[1]!=i[2]:
                self.answer="wrong!! %s is not %s  its %s"%(i[0],i[2],i[1])
                self.answ.append(self.answer)
                
            else:
                self.answer="You got the %s"% i[0].strip(":")
                self.answ.append(self.answer)
            
                   
        return self.answ
                
                
                
                
                        
    def store(self,element,atomicno,bp,mp,state,ram,symbol):
        
        self.new=element
        self.store_parameters=[atomicno,bp,mp,state,ram,symbol]
        self.values=["atomicno","bp","mp","state","ram","symbol"]
        self.data[self.new]={}
        for i,bo in zip(self.values,self.store_parameters):
            self.data[self.new].setdefault(i, bo)       
            datafile["elements"]=self.data
    def periodd(self,atomicno):
            if atomicno <=2>=1:
                self.period=1
            elif atomicno <=10>=3:
                self.period=2
            elif atomicno <=18>=11:
                self.period=3
            elif atomicno<=36>=19:
                self.period=4
            elif atomicno <=54>=37:
                self.period=5
            elif atomicno <=86>=55: 
                self.period=6
            elif atomicno <=120>=87:
                self.period=7           
           
            return str(self.period)     
class ChooseForm(BoxLayout):
    search_input=ObjectProperty()
    
    pass
    
class ChemestryRoot(BoxLayout):

    search_input=ObjectProperty()
    written=ObjectProperty()
    search=ObjectProperty()
    atomicn=ObjectProperty()
    boilingn=ObjectProperty()
    staten=ObjectProperty()
    meltingn=ObjectProperty()
    relativen=ObjectProperty()
    symboln=ObjectProperty()
	
    cc=""   
    z=findout()
	
    ans=[]
    elemented=""
    readato=""
    readboi=""
    readboi=""
    readmel=""
    readrel=""
    readsta=""
    readsym=""
    readele=""
    atomic=""
    boiling=""
    melting=""
    relative=""
    state=""
    symbol=""
    element=""
    asked=""
    ear="carbon"
    b=[]
    look_form=None
    trans=""
    ansform=None
    groupp=None
    cv=None
    ask_form=None
    peri=0
    grouped=0
    per=""
    groupp=""
    def add_chose_form(self):
        self.clear_widgets()
        mainn=Factory.Back()
        self.add_widget(mainn)
        
       
    def add_ask_form(self,element):
        self.clear_widgets()
        self.asked=self.z.AskQuestion()
        
        self.ask_form=Factory.Ask()
        
        
        
        self.add_widget(self.ask_form)
    def read(self):
        self.clear_widgets()
        f=self.z.read()
        
        self.readato=f.pop(0)
        self.readboi=f.pop(0)
        self.readmel=f.pop(0)
        self.readrel=f.pop(0)
        self.readsta=f.pop(0)
        self.readsym=f.pop(0)
        self.readele=f.pop(0)
        self.peri=self.z.periodd(int(self.readato))
        self.grouped=self.z.grouppp(int(self.readato))
        rea=Factory.Read()
        self.add_widget(rea)
        
    def answered(self):
        self.b=self.z.Giveanswer(self.ask_form.atomicn.text,self.ask_form.boilingn.text,self.ask_form.meltingn.text,self.ask_form.relativen.text,self.ask_form.staten.text,self.ask_form.symboln.text)
        self.cv=self.z.MarkAnswer(self.asked,self.b)
        self.clear_widgets()
        gotans=Factory.answered()
        
        self.add_widget(gotans) 
        print self.cv
    def add_lookup_form(self):
        
        self.clear_widgets()
        
        
        
        self.look_form=Factory.Lookup()
        
        
        

        
        self.add_widget(self.look_form)
    def gen(self):
        self.clear_widgets()
        self.cc=self.look_form.search_input.text
        for i in self.z.lookup(self.look_form.search_input.text):
            self.ans.append(i)
        self.atomic=self.ans.pop(0)
        self.boiling=self.ans.pop(0)
        self.melting=self.ans.pop(0)
        self.relative=self.ans.pop(0)
        self.state=self.ans.pop(0)
        self.symbol=self.ans.pop(0)
        self.groupp=self.z.grouppp(int(self.atomic))
        
        self.per=self.z.periodd(int(self.atomic))
        ansform=Factory.Answer()
        
        

        
        
        self.add_widget(ansform)
        
    def credit(self):
        self.clear_widgets()
        creditform=Factory.Credit()
                        
        self.add_widget(creditform)
        
        
class ChemestryTutorApp(App):
    pass
if __name__=="__main__":
    from kivy.core.window import Window
    from  kivy.utils import get_color_from_hex
    Window.clearcolor=get_color_from_hex('#101216')
    ChemestryTutorApp().run()
