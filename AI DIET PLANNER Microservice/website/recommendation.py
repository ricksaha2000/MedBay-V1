from .models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors
import json
import os
import requests

df = pd.read_csv(
    r'C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\AI DIET PLANNER Microservice\\website\\dataset.csv')


def Recommend(request):

    if request.user.is_authenticated:
        class Recommender:

            def __init__(self):
                self.df = pd.read_csv(
                    r'C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\AI DIET PLANNER Microservice\\website\\dataset.csv')

            def get_features(self):
                # getting dummies of dataset
                nutrient_dummies = self.df.Nutrient.str.get_dummies()
                disease_dummies = self.df.Disease.str.get_dummies(sep=' ')
                diet_dummies = self.df.Diet.str.get_dummies(sep=' ')
                feature_df = pd.concat(
                    [nutrient_dummies, disease_dummies, diet_dummies], axis=1)

                return feature_df

            def k_neighbor(self, inputs):

                feature_df = self.get_features()

                # initializing model with k=20 neighbors
                model = NearestNeighbors(n_neighbors=40, algorithm='ball_tree')

                # fitting model with dataset features
                model.fit(feature_df)

                df_results = pd.DataFrame(columns=list(self.df.columns))

                # getting distance and indices for k nearest neighbor
                distnaces, indices = model.kneighbors(inputs)

                for i in list(indices):
                    df_results = df_results.append(self.df.loc[i])

                df_results = df_results.filter(
                    ['Meal_Id', 'Name', 'catagory', 'Nutrient', 'Veg_Non', 'Price', 'Review', 'Diet', 'Disease', 'description'])
                df_results = df_results.drop_duplicates(subset=['Name'])
                df_results = df_results.reset_index(drop=True)
                return df_results

        ob = Recommender()
        data = ob.get_features()

        total_features = data.columns
        d = dict()
        for i in total_features:
            d[i] = 0

        # extract values from database where Table name is Profie
        p = Profile.objects.get(number=request.user.username)
        diet = list(p.diet.split('++'))
        disease = list(p.disease.split('++'))
        nutrient = list(p.nutrient.split('++'))

        Recommend_input = diet+disease+nutrient

        image = p.image.url

        for i in Recommend_input:
            d[i] = 1
        final_input = list(d.values())

        results = ob.k_neighbor([final_input])  # pass 2d array []

        data = dict(results)

        ids = list(data['Meal_Id'])
        n = list(data['Name'])
        c = list(data['catagory'])
        vn = list(data['Veg_Non'])
        r = list(data['Review'])
        nt = list(data['Nutrient'])
        p = list(data['Price'])
        i = range(len(n))
        sc = c
        headers = {"Content-Type": "application/json;","Authorization":"617bf2eb245383001100f8a6"}
        tab = '\t'

        if request.method == "POST":
            lengthDrugs = len(n)
           
            sendData = {
    "phone": "+917044659720",
    "media": {
      "type": "media_template",
      "lang_code": "en",
      "template_name": "welcome",
    "body":[

        {
            "text":f"DIETUP! Our Top 5 Recommendations for you! MEAL 1:  Name: {n[0]}  Category: {c[0]} Calories: {p[0]}  MEAL 2:  Name: {n[1]}  Category: {c[1]} Calories: {p[1]} MEAL 3:  Name: {n[2]}  Category: {c[2]} Calories: {p[2]}  MEAL 4:  Name: {n[3]}  Category: {c[3]} Calories: {p[3]} MEAL 5:  Name: {n[4]}  Category: {c[4]} Calories: {p[4]}"
        }
       
    ]
      
    }
  }
            jsonObject = json.dumps(sendData)
            req = requests.post(url = "https://rapidapi.rmlconnect.net/wbm/v1/message",headers=headers, data = jsonObject)
            

        data1 = zip(n, ids, n, c, sc, vn, r, nt, p, p)

        return render(request, "website/recommend.html", {'data1': data1, 'image': image})

    else:
        messages.error(
            request, 'You must be logged in for meal recommendations..')
        return redirect('Home')
