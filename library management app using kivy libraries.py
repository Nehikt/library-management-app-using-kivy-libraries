# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:50:13 2023

@author: 91954
"""

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class lib_grid(GridLayout):
    def __init__(self,**kwargs):
        super(lib_grid, self).__init__()
        self.cols=4
        
        self.add_widget(Label(text="Student's Name: "))
        self.name_one=TextInput()
        self.add_widget(self.name_one)
        
        self.add_widget(Label(text="Name of the Book: "))
        self.book_one=TextInput()
        self.add_widget(self.book_one)
        
        self.add_widget(Label(text="Issue Date of book: "))
        self.issue_one=TextInput()
        self.add_widget(self.issue_one)
        
        self.add_widget(Label(text="Return Date of book: "))
        self.return_one=TextInput()
        self.add_widget(self.return_one)
        
        self.add_widget(Label(text="fine(if any) : "))
        self.fine_one=TextInput()
        self.add_widget(self.fine_one)
        
        self.print_info=Button(text="click here to print the info")
        self.print_info.bind(on_press=self.click_button)        
        self.add_widget(self.print_info)
        
    def click_button(self,instance):
        print("Name of the student: "+ self.name_one.text)
        print("Name of the book: "+ self.book_one.text)
        print("Issue date of the book: "+ self.issue_one.text)
        print("Return date of the book: "+ self.return_one.text)
        print("Any fine: "+ self.fine_one.text)
         
        
class AppLibrary(App):
    def build(self):
        return lib_grid()
    
if __name__ == '__main__':
   AppLibrary().run()    
        