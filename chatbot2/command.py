#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

The stateless command allows to encapsulate processing logic for specic
intent's command. Allows to easy build response processing pipelines with
multiple stages of intent data processing. The stateless commands may be shared
among various intents.


"""

import random
import requests
import re
import pickle
import os
import json
import joblib
import pandas as pd
import numpy as np


class Command(object):
    def __init__(self):
        self.x=0
    def do(self, bot, entity):
        """
        Execute command's action for specified intent.
        Arguments:
            bot the chatbot
            entity the parsed NLU entity
        """
        pass



class DiseasePredictCommand(Command):
    """
    The command to add item to the list
    """
    def do(self, bot, entity):
        #count = 0
        #if entity in bot.shopping_list:
        #    print (entity)
        #    print(bot.shopping_list)
         #   count = bot.shopping_list[entity]
        #print (bot)
        #print (entity)
        # t = "P"
        print("entity pogo rai")
        print(entity)
        filename = 'C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\chatbot2\\disease_predict.sav'
        feel = str(entity)
        data = [feel]
        cv = pickle.load(open("C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\chatbot2\\vectorizer.pickle", 'rb'))
        loaded_model = pickle.load(open(filename, 'rb'))
        vect=cv.transform(data).toarray()
        p=loaded_model.predict(vect)
        return 'You might be suffering from'+ (p[0]) +'.Please Visit A Doctor. We are here to Help You!'
        # return t

class AskSymptomBackCommand(Command):
    """
    The command to greet user
    """

    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "At your service.Don't worry, you will be fine.Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "I can help you consult a doctor. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "I can help you finding the right doctor to help you feel better. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "Don't worry. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "Help me understand better. Don't worry. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough"]

    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        return s


class DiseasePredictFromSymptomCommand(Command):
    """
    The command to add item to the list
    """
    def do(self, bot, entity):
        #count = 0
        #if entity in bot.shopping_list:
        #    print (entity)
        #    print(bot.shopping_list)
         #   count = bot.shopping_list[entity]
        #print (bot)
        #print (entity)
        # t = "P"
        print("entity pogo rai")
        print(entity)
        cls = joblib.load('C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\chatbot2\\decision_tree.joblib') # classification model
        cls1 = joblib.load('C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\chatbot2\\gradient_boost.joblib')

        cls3 = joblib.load('C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\chatbot2\\random_forest.joblib')
        symp_list = pd.read_csv('C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\chatbot2\\test_data.csv').columns[:-1]
        d = np.zeros((len(symp_list)))
        test_case = pd.DataFrame(d).transpose()
        test_case.columns= symp_list

        symptoms = entity   # need to input exact coulmn names with comma separated value
        symptoms = symptoms.split(',')
        for symp in symptoms:
            symp.replace(" ", "_")
            if symp in symp_list: test_case.loc[0, [symp]]=1
        disease = cls.predict(test_case)   #predicted disease
        disease1 = cls1.predict(test_case)
        disease3 = cls3.predict(test_case)
        # print(disease[0])
        # print("disease")
        dis_doc =  {'Fungal infection':'Dermatologist',
                    'Allergy':'Allergist/Immunologists',
                    'GERD':'Gastroenterologist',
                    'Acne':'Dermatologist',
                    'hepatitis A':'Hepatologist',
                    'hepatitis B':'Hepatologist',
                    'hepatitis C':'Hepatologist',
                    'hepatitis D':'Hepatologist',
                    'hepatitis E':'Hepatologist',
                    'Chronic cholestasis':'Gastroenterologist',
                    'Drug Reaction':'Pharmacologist',
                    'Peptic ulcer disease':'Gastroenterologist',
                    'AIDS':'HIV Specialist',
                    'Diabetes':'Endocrinologist',
                    'Gastroenteritis':'Gastroenterologist',
                    'Bronchial Asthma':'Asthma Specialist',
                    'Hypertension':'Cardiologist',
                    'Migraine':'Neurologist',
                    'Cervical spondylosis':'Otolaryngologist',
                    'Paralysis (brain hemorrhage)':'Paralysis Doctor',
                    'Jaundice':'Gastroenterologist',
                    'Malaria':'General Physician',
                    'Chicken pox':'General Physician',
                    'Dengue':'Microbiologist',
                    'Typhoid':'General Physician',
                    'Alcoholic_hepatitis':'Gastroenterologist',
                    'Tuberculosis':'Pulmonologists',
                    'Common_Cold':'Otolaryngologist',
                    'Pneumonia':'Pediatric',
                    'Dimorphic_hemmorhoids(piles)':'Proctologist',
                    'Heart_attack':'Cardiologist',
                    'Varicose_veins':'Endocrinologist',
                    'Hypothyroidism':'Endocrinologist',
                    'Hyperthyroidism':'Endocrinologist',
                    'Hypoglycemia':'Endocrinologist',
                    'Osteoarthristis':'Orthopedist',
                    'Arthritis':'Orthopedist',
                    '(vertigo)_Paroymsal_Positional_Vertigo':'ENT Specialist',
                    'Urinary_tract_infection':'Urologist',
                    'Psoriasis':'Physician',
                    'Impetigo':'Expert Physician'}
        print(bot.flag)
        if(bot.flag==1):
            doctor_predicted = ""
            bot.flag = 0
            for k, v in dis_doc.items():
                if(k == disease[0]):
                    doctor_predicted=doctor_predicted+" "+v
                elif(k == disease1[0]):
                    doctor_predicted=doctor_predicted+" "+v
                elif(k == disease3[0]):
                    doctor_predicted=doctor_predicted+" "+v

            return 'You might have the following diseases '+ str(disease[0])+" "+ str(disease1[0])+" "+ str(disease3[0])+'. Please Visit A Doctor. We are here to Help You! You can consult the following doctor:'+ doctor_predicted
        elif(bot.flag==2):
            bot.flag = 0
            return "Drug Predicting Successfully"
        # print(disease1[0])
        # print("disease1")

        # print(disease3[0])
        # print("disease3")
        return 'You might have the following diseases '+ str(disease[0])+ str(disease1[0])+ str(disease3[0])+'.Please Visit A Doctor. We are here to Help You!'


class DoctorPredictIntentCommand(Command):
    """
    The command to greet user
    """

    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """

        self.greetings = ["Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "At your service.Don't worry, you will be fine.Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "I can help you consult a doctor. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "I can help you finding the right doctor to help you feel better. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "Don't worry. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "Help me understand better. Don't worry. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough"]


    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        bot.flag=1
        return s



class DrugPredictIntentCommand(Command):
    """
    The command to greet user
    """

    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """

        self.greetings = ["Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "At your service.Don't worry, you will be fine.Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "I can help you consult a doctor. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "I can help you finding the right doctor to help you feel better. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "Don't worry. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough",
                          "Help me understand better. Don't worry. Please write your symptoms separated by commas. I have an example for you->Headache,fever,cough"]

    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        bot.flag=2
        return s








class GreetCommand(Command):
    """
    The command to greet user
    """

    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Hey!", "Hello!", "Hi there!", "How are you!"]

    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        return s
class WishBackCommand(Command):
    """
    The command to greet user
    """

    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Oh! Me Amazing.How may I help you?", "I am fine.How may I assist you?", "At your service.", "First time someone asked me.I am wonderful.How may I be of your assistance?"]

    def do(self, bot, entity):
        s = random.choice(self.greetings)
        print("Printing : "+s)
        return s

class AddItemCommand(Command):
    """
    The command to add item to the list
    """
    def do(self, bot, entity):
        #count = 0
        #if entity in bot.shopping_list:
        #    print (entity)
        #    print(bot.shopping_list)
         #   count = bot.shopping_list[entity]
        #print (bot)
        #print (entity)
        if (bool(re.search(r'\d', entity))==True):
            t=1
            L=entity.split()
            a=int(L[0])
            if L[1] in bot.shopping_list:
                bot.shopping_list[L[1]]+=a
            else:
                bot.shopping_list[L[1]]=a
        return t

class RemoveItemCommand(Command):
    """
    The command to add item to the list
    """
    def do(self, bot, entity):
        #count = 0
        #if entity in bot.shopping_list:
        #    print (entity)
        #    print(bot.shopping_list)
         #   count = bot.shopping_list[entity]
        #print (bot)
        #print (entity)
        t=1
        if (bool(re.search(r'\d', entity))==True):
            L=entity.split()
            a=int(L[0])
            if L[1] in bot.shopping_list:
                temp=bot.shopping_list[L[1]]-a
                if (temp<=0):
                    t=0
                    #print(t)
                else:
                    bot.shopping_list[L[1]]=temp
            else:
                t=0
                #print(z)
        return t




class ShowItemsCommand(Command):
    """
    The command to display shopping list
    """

    def do(self, bot, entity):
        if len(bot.shopping_list) == 0:
            s = "Your shopping list is empty!"
            # print(s)
            return s
        s = "Shopping list items:"
        l = bot.shopping_list.items()

        for k, v in bot.shopping_list.items():
            t = "%s - quantity: %d" % (k, v)
            print(t)
            s = s + "\n" + t
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # print(s)
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return (s,l)

class ClearListCommand(Command):
    """
    The command to clear shopping list
    """

    def do(self, bot, entity):
        bot.shopping_list.clear()
        s = "Items removed from your list!"
        print(s)
        return s

class ShowStatsCommand(Command):
    """
    The command to show shopping list statistics
    """

    def do(self, bot, entity):
        s = "shopping list is empty"
        unique = len(bot.shopping_list)
        if unique == 0:
            print(s)

        total = 0
        for v in bot.shopping_list.values():
            total += v
        t = "# of unique items: %d, total # of items: %d" % (unique, total)
        s = s + '\n' + t
        print(t)
        return s

class SuggestCorona(Command):
    def do(self, bot, entity):

        response = requests.get("https://disease.sh/v2/countries/"+entity+"?yesterday=false%22%20-H%20%22accept:%20application/json").json()
        # location = bot.shopping_list[entity]
        # print(entity)
        s = entity+"\n"+"Country:"+response['country']+"\n"+"Total Cases:"+str(response['cases'])+"\n"+"Total Cases Today:"+str(response['todayCases'])
        s = s + "Total Death Count:"+str(response['deaths']) +"\n"+ "Total Deaths Today:"+str(response['todayDeaths'])+"\n"+ "Total Recovered:"+str(response['recovered']) +"\n"
        s = s + "Total Active Cases:"+str(response['active']) +"\n"+ "STAY SAFE AND STAY INSIDE ~ FROM TEAM $__TROUBLESHOOTERS__$ \n"

        # print(s)

        return s


