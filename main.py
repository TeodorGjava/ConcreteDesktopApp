
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.properties import OptionProperty
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

class myscreen(TabbedPanel):
    #    fp = open("Zames.py", 'r', encoding='utf-8')

    kvfile = Builder.load_string("""<myscreen>

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    vlaga1:vlaga1
    vlaga2:vlaga2
    vlaga3:vlaga3

    dobavka:dobavka

    voda:voda
    voda1:voda1

    vlojeno:vlojeno

    kub1:kub1
    kub2:kub2

    procent:procent

    m1:m1
    m2:m2
    m3:m3
    m4:m4
    m5:m5
    m6:m6
    m7:m7
    m8:m8

    l:l

    l1:l1
    l2:l2
    l3:l3
    l4:l4
    l5:l5
    l6:l6
    l7:l7
    l8:l8
    pred:pred
    h20:h20
    h2o:h2o
    razlika:razlika
    razlikat:razlikat
    
#    w_c:w_c
    wc:wc
    do_default_tab: False
    TabbedPanelItem:
        
        text:"Prepare"
        direction:"top"
        
        size: root.width, root.height

        StackLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: "lr-tb"
            Label:
                size_hint: .125,.06
                text: "Дата: "
                color: 0,0,0,1
            TextInput:
                size_hint: .125,.06
                multiline: False
                write_tab: False
            Label:
                size_hint: .15,.06
                text: "Клиент : "
                color: 0,0,0,1
            TextInput:
                size_hint: .3,.06
                write_tab: False
            Label:
                size_hint: .15,.06
                text: "Клас :"
                color: 0,0,0,1
            TextInput:
                size_hint: .15,.06
                write_tab: False

            Label:
                size_hint: .5,.05
                text: "Пепел: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Цимент : "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Пясък 1: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Пясък 2: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Пясък 3: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Камък 1: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Камък 2: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False
            Label:
                size_hint: .5,.05
                text: "Камък 3: "
                color: 0,0,0,1
            TextInput:
                size_hint: .5,.05
                write_tab: False

            Label:
                size_hint: .250,.06
                text: "Кубчета 15x15:"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.256,.333,1
                    Rectangle:
                        pos: self.pos
                        size: self.size

            TextInput:
                id:kub1
                size_hint:.125,.06
                text: ""
                multiline: False
                input_type: "number"
                write_tab: False
            Label:
                size_hint: .250,.06
                text: "Кубчета 10x10:"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            TextInput:
                id:kub2
                size_hint:.125,.06
                text: ""
                multiline: False
                input_type: "number"
                write_tab: False
            Button:
                text: "Литри="
                size_hint: .250,.06
                on_press: root.press2()
            Label:
                size_hint: .250,.05
                text: "Влажности %:"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 0,.25,1,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            TextInput:
                id:vlaga1
                size_hint:.125,.05
                hint_text:"Влажност %:"
                text: "0"
                multiline: False
                input_type: "number"
                write_tab: False
            TextInput:
                id:vlaga2
                size_hint:.125,.05
                hint_text:"Влажност %:"
                text: "0"
                multiline: False
                input_type: "number"
                write_tab: False
            TextInput:
                id:vlaga3
                size_hint:.125,.05
                hint_text:"Влажност %:"
                text: "0"
                multiline: False
                input_type: "number"
                write_tab: False
            Label:
                size_hint: .2,.05
                text: "Вода(влажности):"
                color: 0,0,0,1
            Label:
                id:voda
                size_hint:.16,.05
                color: 0,0,0,1

            Label:
                size_hint: .125,.05
                text: "Пепел"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .666,.666,.666,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .125,.05
                text: "Цимент"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .666,.666,.555,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .125,.05
                text: "Пясък1"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .895,.66,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .125,.05
                text: "Пясък2"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .895,.66,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .125,.05
                text: "Пясък3"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .895,.66,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .125,.05
                text: "Камък1"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .125,.05
                text: "Камък2"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:

                size_hint: .125,.05
                text: "Камък3"
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            TextInput:
                id:m1
                hint_text: "Пепел:"
                size_hint: .125,.05
                text: "0"
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m2
                hint_text: "Цимент:"
                text:"0"
                size_hint: .125,.05
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m3
                hint_text: "пясък1:"
                size_hint: .125,.05
                text: "0"
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m4
                hint_text: "пясък2:"
                size_hint: .125,.05
                text: "0"
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m5
                hint_text: "пясък3:"
                size_hint: .125,.05
                text:"0"
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m6
                hint_text: "камък1:"
                size_hint: .125,.05
                text:"0"
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m7
                hint_text: "камък2:"
                size_hint: .125,.05
                text: "0"
                input_type: "number"
                multiline: False
                write_tab: False

            TextInput:
                id:m8
                hint_text: "камък3:"
                size_hint: .125,.05
                text: "0"
                input_type: "number"
                multiline: False
                write_tab: False


            Label:
                id:l1
                size_hint: .125,.05
                text:""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .666,.666,.666,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l2
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .666,.666,.555,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l3
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .895,.66,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l4
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .895,.66,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l5
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .895,.66,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l6
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l7
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                id:l8
                size_hint: .125,.05
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1,.78,.4,1
                    Rectangle:
                        pos: self.pos
                        size: self.size

            Label:
                size_hint: .25,.06
                text: "Предполагаема вода m3:"
                color: 0,0,0,1
            TextInput:
                id:voda1
                size_hint:.25,.06
                text_hint: "Вода"
                text: "0"
                multiline: False
                input_type: "number"
                write_tab: False
            Label:

                size_hint: .25,.06
                text: "Вложено: "
                color: 0,0,0,1

            Label:
                id:vlojeno
                size_hint: .25,.06
                color: 0,0,0,1
            Label:
                size_hint: .2,.06
                text:"Литри:"
                color: 0,0,0,1
            TextInput:
                id:l
                hint_text: "Литра: "
                size_hint: .2,.06
                text: "0"
                multiline: False
                input_type: "number"
                write_tab: False

            Label:
                text: "Добавка %:"
                size_hint: .2,.06
                color: 0,0,0,1
            TextInput:
                id:procent
                size_hint:.2,.06
                text: "0"
                multiline: False
                input_type: "number"
                write_tab: False
            Label:
                id:dobavka
                size_hint: .2,.06
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .666,.666,.666,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                size_hint: .5,.08
                text: "Предполагаема вода:"
                color: 0,0,0,1
            Label:
                id:pred
                size_hint: .5,.08
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: .666,.666,.666,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Button:
                text: "="
                size_hint: 1,.08
                on_press: root.press()   
    TabbedPanelItem:
        text: "Results"
        StackLayout:
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text:"Вода:"
                size_hint: .25,.2
                color: 0,0,0,1
            TextInput:
                id:h2o
                input_type: "number"
                hint_text: "Вода: "
                color: 0,0,0,1
                text:"0"
                size_hint: .25,.2
                multiline: False
            Label:
                id:h20
                color: 0,0,0,1
                text: ""
                size_hint: .25,.2

            Button:
                text: "="
                on_press: root.press3()
                size_hint: .25,.2
            Label:
                size_hint: .5,.2
                color: 0,0,0,1
                text:"В/Ц:"
            Label:
                id:wc
                color: 0,0,0,1
                size_hint: .5,.2
                text:""
#            TextInput:
#                id:w_c
#                text: "0"
#                size_hint: .5,.2
#                input_type: "number"
#                hint_text: "Вода: "
#                multiline: False
            
            Label:
                text: "Тегло 5л: "
                color: 0,0,0,1
                size_hint: .25,.2    
                
                
            TextInput:
                id:razlika
                input_type: "number"
                hint_text: "Тегло: "
                text:"0"
                size_hint: .25,.2
                multiline: False
            Label:
                text: "Разлика 5л/вложено: "
                color: 0,0,0,1
                size_hint: .25,.2    
            Label:
                color: 0,0,0,1
                id:razlikat
                text:"" 
                size_hint: .25,.2
    """)

    def press(self):
        material1 = self.ids.m1.text
        material2 = self.ids.m2.text
        material3 = self.ids.m1.text
        material4 = self.ids.m2.text
        answer1 = self.ids.l1.text
        answer2 = self.ids.l2.text
        answer3 = self.ids.l3.text
        answer4 = self.ids.l4.text
        answer5 = self.ids.l5.text
        answer6 = self.ids.l6.text
        answer7 = self.ids.l7.text
        answer8 = self.ids.l8.text
        voda = self.ids.voda.text
        voda1 = self.ids.voda1.text
        vlojeno = self.ids.vlojeno.text
        dobavka = self.ids.dobavka.text
        procent = self.ids.procent.text
        pred = self.ids.pred.text
        answer = 0
        for number in self.voda1.text:
            pred = float(self.voda1.text) * float(self.l.text) / 1000
        for number in self.m1.text:
            answer1 = float(self.m1.text) * float(self.l.text) / 1000
        for number in self.m2.text:
            answer2 = float(self.m2.text) * float(self.l.text) / 1000
        for number in self.m3.text:
            answer3 = float(self.m3.text) * float(self.l.text) \
                      / 1000 + ((float(self.m3.text) / 100 * (float(self.vlaga1.text)))) * float(self.l.text) / 1000
            voda = float(self.vlaga1.text) / 100 * float(self.m3.text) \
                   + float(self.vlaga2.text) / 100 * float(self.m4.text) \
                   + float(self.vlaga3.text) / 100 * float(self.m5.text)

        for number in self.m4.text:
            answer4 = float(self.m4.text) * float(self.l.text) / 1000 \
                      + ((float(self.m4.text) / 100 * (float(self.vlaga2.text)))) * float(self.l.text) / 1000

        for number in self.m5.text:
            answer5 = float(self.m5.text) * float(self.l.text) / 1000 \
                      + ((float(self.m5.text) / 100 * (float(self.vlaga3.text)))) * float(self.l.text) / 1000
        for number in self.m6.text:
            answer6 = float(self.m6.text) * float(self.l.text) / 1000
        for number in self.m7.text:
            answer7 = float(self.m7.text) * float(self.l.text) / 1000
        for number in self.m8.text:
            answer8 = float(self.m8.text) * float(self.l.text) / 1000
        for number in self.m1.text, self.m2.text, self.m3.text, self.m4.text, self.m5.text, \
                      self.m6.text, self.m7.text, self.m8.text, self.voda1.text:
            vlojeno = float(self.m1.text) + float(self.m2.text) + float(self.m3.text) \
                      + float(self.m4.text) + float(self.m5.text) \
                      + float(self.m6.text) + float(self.m7.text) + float(self.m8.text) \
                      + float(self.voda1.text)
        for number in self.m1.text, self.m2.text:
            dobavka = ((float(self.m1.text) * float(self.l.text) / 1000) + (float(self.m2.text) * float(self.l.text))
                       / 1000) * (float(self.procent.text) * 10)

        self.ids.l1.text = str(answer1)
        self.ids.l2.text = str(answer2)
        self.ids.l3.text = str(answer3)
        self.ids.l4.text = str(answer4)
        self.ids.l5.text = str(answer5)
        self.ids.l6.text = str(answer6)
        self.ids.l7.text = str(answer7)
        self.ids.l8.text = str(answer8)
        self.ids.voda.text = str(voda)
        self.ids.vlojeno.text = str(vlojeno)
        self.ids.dobavka.text = str(dobavka)
        self.ids.voda1.text = str(voda1)
        self.ids.pred.text = str(pred)

    def press2(self):
        kubche1 = self.ids.kub1.text
        bubche2 = self.ids.kub2.text
        litri = self.ids.l.text
        for num in self.kub1.text:
            litri = float(self.kub1.text) * 3.375 + float(self.kub2.text) + 2

        self.ids.l.text = str(litri)

    def press3(self):
        h2o = self.ids.h2o.text
        wc = self.ids.wc.text
        for number in self.h2o.text:
            h2o = (float(self.h2o.text) / float(self.l.text)) * 1000 + (
                    float(self.vlaga1.text) / 100 * float(self.m3.text) \
                    + float(self.vlaga2.text) / 100 * float(self.m4.text) \
                    + float(self.vlaga3.text) / 100 * float(self.m5.text))

        for number in self.h2o.text:
            wc = (float(self.h2o.text) / float(self.l.text) * 1000 + (
                        float(self.vlaga1.text) / 100 * float(self.m3.text) \
                        + float(self.vlaga2.text) / 100 * float(self.m4.text) \
                        + float(self.vlaga3.text) / 100 * float(self.m5.text))) / (
                             float(self.m1.text) + float(self.m2.text))

        self.ids.h20.text = str(h2o)
        self.ids.wc.text = str(wc)
        for number in self.razlika.text:
            razlika= float(self.razlika.text) - (float(self.m1.text) + float(self.m2.text) + float(self.m3.text) \
                      + float(self.m4.text) + float(self.m5.text) \
                      + float(self.m6.text) + float(self.m7.text) + float(self.m8.text)+ (float(self.h2o.text) / float(self.l.text)) * 1000 + (
                    float(self.vlaga1.text) / 100 * float(self.m3.text) \
                    + float(self.vlaga2.text) / 100 * float(self.m4.text) \
                    + float(self.vlaga3.text) / 100 * float(self.m5.text)))
        self.ids.razlikat.text =str(razlika)
class Smetki(App):

    def build(self):
        return myscreen()


if __name__ == "__main__":
    Smetki().run()