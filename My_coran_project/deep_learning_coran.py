#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys

#### This project is the meaning of my life 
#### All my life I dream about the conception of this project 
#### I start it the 04 jully 2019 

#### In this project I would like to create an application that show the power mathematics in the coran

### Let's start by reading and showing the coran with a function

### Import tkinter for graphic window
try:
    # Pour Python 2
    from Tkinter import * 
except ImportError:
    # Pour Python 3
    from tkinter import *

import matplotlib 
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np 


class Coran_application(tk.Tk):

    def createWidgets(self,coran_file,coran_cleaned,T):

        ### Label rechercher mot
        self.label = tk.Label(self, text="Rechercher un mot dans le coran")
        self.label.config(bg="PaleGreen4", font=("Arial",18), pady=5, width=30)

        
        ## Create button quitter
        self.QUIT = tk.Button(self,text="QUITTER",fg="red",command=self.quit)
        # self.QUIT["text"] = "QUITTER"
        # self.QUIT["fg"]   = "red"
        # self.QUIT["command"] =  self.quit

        ## Create button rechercher mots dans le coran
        self.RECHERCHER = tk.Button(self)
        self.RECHERCHER["text"] = "RECHERCHER"
        self.RECHERCHER["fg"]   = "green"
        self.RECHERCHER["command"] = lambda: self.get_number_of(coran_cleaned,str(eval(self.entree.get())),T)

        ## Label recherche sourate en configuration 
        self.label_rech_sour = tk.Label(self,text="Rechercher une sourate dans le coran ")
        self.label_rech_sour.config(bg="PaleGreen4", font=("Arial",18), pady=5, width=30)

        ## Crete button rechercher sourate dans le coran
        self.Rech_Sourate = tk.Button(self)
        self.Rech_Sourate["text"] = "RECHERCHER SOURATE"
        self.Rech_Sourate["fg"]   = "black"
        self.Rech_Sourate["command"] = lambda: self.get_sourate(num_sourate=str(eval(self.listsourate.get(tk.ACTIVE))),Text_windows=T)

        ## Label statistique en configuration
        self.label_stat = tk.Label(self,text="Afficher les statistiques")
        self.label_stat.config(bg="PaleGreen4", font=("Arial",18), pady=5, width=30)

        ## Boutton statistiques of the great names of God
        self.STATISTIQUES = tk.Button(self)
        self.STATISTIQUES["text"] = "Statistics names of God"
        self.STATISTIQUES["fg"]   = "blue"
        self.STATISTIQUES["command"] = lambda: self.stats_names_of_god(names=Names_God_inCoran,coran=coran_cleaned,T=T)

        ## Labels and button for compting words in the coran 
        self.label_compte_words_in_coran = tk.Label(self,text="Afficher les nombres des mots du coran")
        self.label_compte_words_in_coran.config(bg="PaleGreen4", font=("Arial",18), pady=5, width=30)
        self.COMPTE_WORD = tk.Button(self)
        self.COMPTE_WORD["text"] = "Compte words in coran"
        self.COMPTE_WORD["fg"]   = "DodgerBlue4"
        self.COMPTE_WORD["command"] = lambda: self.compte_words_in_coran(coran=coran_cleaned,T=T)



        ## entree texte en arabe à rechercher dans le coran
        self.entree = tk.Entry(self)

        ## entree numuro sourate to find in the coran most be between 1 to 114
        self.entree_num_sourate = tk.Entry(self)

        self.scrol_num_coran = tk.Scrollbar(self)
        #self.scrol_num_coran.grid(row=1,column=2,sticky='NS')

        ## Liste deroulante pour le choix du numero des sourates dans le coran
        self.listsourate = tk.Listbox(self,selectmode=tk.SINGLE, height=1,yscrollcommand=self.scrol_num_coran.set)

        ## Insert element in the list
        for i in range(0,114):
            self.listsourate.insert(i,str(i+1))


        ## LABEL END TEXT FOR RESEARCH WORD IN THE CORAN
        ## line 1
        self.label.grid(row=0,column=0)
        self.entree.grid(row=0,column=1)
        self.RECHERCHER.grid(row=0,column=2)

        ## Labels of recherche sourate en boutton  line 2
        self.label_rech_sour.grid(row=1,column=0)
        #self.entree_num_sourate.grid(row=1,column=1)
        self.listsourate.grid(row=1,column=1)
        self.Rech_Sourate.grid(row=1,column=2)
        
        ## Labels of statistiques and button line3
        self.label_stat.grid(row=2,column=0)
        self.STATISTIQUES.grid(row=2,column=2)

        ## Labels compte words in the coran
        self.label_compte_words_in_coran.grid(row=3,column=0)
        self.COMPTE_WORD.grid(row=3,column=2)

        
        ### QUIT BUTTON
        self.QUIT.grid(row=4,column=2,pady=5)

        
    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        ## Set title
        self.wm_title("Coran Browser") ### Control the window title
        ## Set fenetre background to white color
        self['bg']='PaleGreen4'

        ## Set size of window
        self.minsize(width=450, height=150)

        
        # ## Read and clean the coran from file
        coran3 = self.read_coran('quran-uthmani-min.txt')
        coran_cleaned = self.get_coran(coran3)

        
        # Vertical (y) Scroll Bar
        self.S = tk.Scrollbar(self)
        self.S.grid(column=5, row=5, sticky='NS',padx=1,pady=10)

        # Text Widget
        self.T = tk.Text(self, yscrollcommand=self.S.set, width = 80, wrap = tk.WORD, fg='black',bg='navajo white')
        self.T.config(font=(34))
        self.T.grid(row=5, columnspan=3,padx=1,pady=10)



        # Configure the scrollbars
        self.S.config(command=self.T.yview)

        # Get new coran file
        coran_file = self.read_coran('quran-uthmani-min.txt')

        ## Create widgets
        self.createWidgets(coran_file=coran_file,coran_cleaned=coran_cleaned,T=self.T)

        
        

    ### This function read and return the coran from file 
    def read_coran(self,file_path):
        f = open(file_path,"r")
        return f 


    ### Get sourate from the coran by given the number of sourate between 1 to 114
    def get_sourate(self,num_sourate,Text_windows):

        # init the result
        result = []
        num_line = 1

        coran_file = self.read_coran(file_path='quran-uthmani-min.txt')

        ## Get first line
        line = coran_file.readline()

        # Split line 
        array_line = line.split("|")

        while line:
            #print(" line ",num_line, "firs_element --> ",array_line[0])
            if(array_line[0].isdigit() and (int(array_line[0])==int(num_sourate))):

                line_tuned = "\" "+array_line[2]+" \"" +"v: "+array_line[1]+"  s: "+array_line[0] +"\n"              

                ### append the ayat to result
                result.append(line_tuned)

                #result.append(array_line[1])
                #result.append(array_line[2])

                ### Get next line and split it 
                line = coran_file.readline()
                array_line = line.split("|")
                num_line = num_line + 1
            else :
                line = coran_file.readline()
                array_line = line.split("|")
                num_line = num_line + 1


        print("sourate ",num_sourate,"-----> \n", result)

        ### Add result to the windows text area
        label_final="\nSourate n° "+num_sourate+"\n\n"
        for line in result:
            label_final = label_final + line + "\n"

        ## Put editable
        Text_windows.config(state=tk.NORMAL)

        ## Delete contains before
        #Text_windows.delete(1.0,tk.END)

        Text_windows.insert(1.0,label_final)

        ## Put no editable text
        #Text_windows.config(state=tk.DISABLED)

        return result

    ## Print all the coran
    def get_coran(self,coran):

        result = []

        ## Get first line
        line = coran.readline()

        array_line = line.split("|")

        while line:
            #print(" line ",num_line, "firs_element --> ",array_line[0])
            if(array_line[0].isdigit()):
                #print("sourate ayat found --> ",array_line[1]," ",array_line[2])
                result.append(array_line[0])
                result.append(array_line[1])
                result.append(array_line[2])
            
            line = coran.readline()
            array_line = line.split("|")


        return result

    
        
    ## Print some part of the coran
    ## argument sourate number and 
    # ayat interval start ... end ....
    #  
    def get_hizb(self,coran,num_sourate,start,end,T):

        result = []

        sourate = get_sourate(num_sourate,Text_windows=T) 

        for i in range(start*2,end*2):
            result.append(sourate[i])
            #print(sourate[i])  

        return result  

    ### Get number of some word in the coran
    def get_number_of(self,coran,word,T):

        ### number found
        number = 0
        ## resultat of ayyat found that contains the word
        result = []
        ## compter
        compter = 0
        
        for line in coran:
            #print(line)
            if word in line :
                #print(" Found ",word," in ayyat --->  ",line)
                number = number + line.count(word)
                ## Append the ayyat and the reference number sourate end number ayyat 
                result.append(line+"verset. n°: "+str(coran[compter-1])+" Sourate n°: "+str(coran[compter-2]))

            compter = compter + 1
   

        for i in range(len(result)):
            print("word ",word," is in --> ", result[i])

        print("\nTotal found ----> ",word," in the coran : ", number,"\n\n")

        label_final="\n\nle mot : \" "+word+" \" se trouve dans les verset suivants : \n\n"
        for line in result:
            label_final = label_final + "\n"+line + "\n"

        label_final = "\n######################################################################################\n ######################  Total du mot \""+word+"\" dans le coran : "+str(number)+"   ###################### \n######################################################################################\n" + label_final 
        

        T.config(state=tk.NORMAL) ## put editable text area
        ## Add result to the window text area
        #T.delete(1.0,tk.END)  ### clean text area
        T.insert(1.0,label_final)
        ## Put no editable text
        #T.config(state=tk.DISABLED) ## Put uneditable 


        return number


    ### Make some statistique with the great names of God in the coran
    def stats_names_of_god(self,names,coran,T):

        statResult = []

        for name in names:
            statResult.append(self.get_number_of(coran,name,T))

        #result = np.array(statResult)
        print(statResult)

        plt.plot(statResult)
        plt.hist(names,bins=30,density=True)
        #plt.plot(statResult)
        plt.ylabel('Nombre d\'apparition')
        plt.xlabel('Names')
        plt.show()


        return statResult
        
    ### Compte all words in the coran 
    def compte_words_in_coran(self,coran,T):
        ## Array of tuple result
        result = []

        ## Content the list of words in the coran
        list_words_in_coran = []

        for line in coran:
            if(not line.isdigit()):

                ## Split line to get words
                words = line.split()

                ## Get all word in the line
                for word in words:
                    #print("word -->",word)
                    list_words_in_coran.append(word)

                    
        print("Processing ...")

        ## sum of each words in the array 
        for word in list_words_in_coran:

            if(not word in [y[0] for y in result]):
                result.append((word,list_words_in_coran.count(word)))
        

        ### print list of words with count in the coran
        #print("List of words and count ---> ",result)

        ## Contains the numbers of each words in the coran
        numbers_of_words = []

        ## Contains words 
        list_words = []

        ## Contains words and numbers tuple 
        list_words_number = []

        ## Create final String to print
        string_result = "\n ################# Résultats des comptes des mots du coran ################# \n"
        for word in result:
            string_result = string_result + "\n >>> " +str(word[0])+" <<<  ----> "+str(word[1])+"  ***\n"
            numbers_of_words.append(word[1])
            list_words.append(word[0])
            list_words_number.append((word[1],word[0]))

        
        print("End processing !!!")

        print("\nNon sorted list ",list_words_number)

        ## sorte list of words 
        list_words_number = sorted(list_words_number)

        print("\nSorted list ",list_words_number)

        ## Add the result to the scree
        T.config(state=tk.NORMAL)
        T.delete(1.0,tk.END)
        T.insert(1.0,string_result)
        #T.config(state=tk.DISABLED)

        ## Plot result
        plt.plot(numbers_of_words)
        plt.hist(list_words,bins=30,density=True,histtype='bar')

        # counts, bins = np.histogram(result)
        # plt.hist(bins[:-1], bins, weights=counts)

        plt.ylabel('Nombre')
        plt.xlabel('Mot')
        plt.show()


        return result






### Main function 
if __name__ == "__main__":

    ### Array contains the 99 names of God in the Coran
    Names_God_inCoran = ["اللَّه","الرَّحمٰن","الرَّحيم","مٰلِك","رَبّ","هُوَ الَّذى"," عَليم","شاكِر","عَزيز","حَكيم","خَبير","بَصير",
                         "سَميعٌ","قَدير","وٰسِع","غَنِىّ","حَليم","حَميد","غَفورٌ","رَحيمٌ","الوَكيل","تَوّابًا","عَفُوًّا",]

    ## Run the application
    app = Coran_application()
    app.mainloop()

    