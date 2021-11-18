#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st 
import pandas as pd 
import numpy as np
from PIL import Image

image = Image.open(r'C:\Users\balla\Pictures\Saved Pictures\Streamlit project\Nature.jpg')

# Configuration de la page
st.set_page_config(
    page_title ='World Happiness Report App'   
    )

# Création d'une barre laterale pour le menu
Menu = st.sidebar.radio("Menu",("Home","Exploration du jeu de données ","Etude du PIB et de l'espérance de vie","Aperçu de la Condition de la femme","Impact du COVID19","Machine Learning"))

# Enrichissement du menu Home
if Menu == "Home":
    # Affichage principal
    st.title("WORD HAPPINESS REPORT PROJECT")
    st.image(image)
    st.markdown("# *Introduction*")
    st.write(""" Cette étude s'inscrit dans le cadre du projet fil rouge de fin formation du parcours 'Data Analyst' de mai 2021 de **DATASCIENTEST**.  
             Le World Happiness Report est une mesure du bonheur publiée par le 'Réseau des solutions pour le développement durable des nations unies depuis 2012
             et est rédigé par John F.Helliwell.  
             Notre étude portera sur le rapport de 2019 et aura pour objectif de mettre en avant des visualisations et  de construire des Modèles simples de Machine Learning.  
             Afin d'y parvenir, nous allons tout d'abord faire une étude des données qui nous sont présentées. Ensuite, nous enrichirons notre jeu de données  
             en fonction de différentes thématiques telles que *la condition d'épanouissement de la femme* ou encore *l'impact de la COVID19*, le but étant de les mettre en
             relation avec le score de bonheur.Enfin, nous nous développerons un modèle de Machine Learning afin de faire quelques prévisions du score de bonheur.   
              """) 
             
#if Menu == 'Score du bonheur':
