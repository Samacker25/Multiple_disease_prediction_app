# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:00:22 2024

@author: SOUMEN
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('F:/projects/Multiple disease prediction system/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('F:/projects/Multiple disease prediction system/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('F:/projects/Multiple disease prediction system/parkinsons_model.sav','rb'))

breast_cancer_model = pickle.load(open('F:/projects/Multiple disease prediction system/breast_cancer_model.sav','rb'))

kidney_model = pickle.load(open('F:/projects/Multiple disease prediction system/kidney_model.sav','rb'))
                                    

# sidebar for navigation
    
with st.sidebar:
        
    selected = option_menu('Multiple Disease Prediction System',
                               ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Disease Prediction','Breast Cancer Prediction','Kidney Disease Prediction'],
                                icons =['capsule','heart-pulse','person standing','virus2','activity'],
                                menu_icon='hospital',
                               default_index=0)
        
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
        
   #page title
   st.title('Diabetes Prediction using ML')
        
   #getting the input data from the user
   col1, col2, col3 = st.columns(3)
        
   with col1:
    
       Pregnancies = st.text_input('Number of pregnancies')
            
   with col1:
        
       Glucose = st.text_input('Glucose level')
        
   with col1:
            
       BloodPressure = st.text_input('Blood Pressure Level')
            
   with col2:
        
        SkinThickness = st.text_input('SkinThickness level')
            
   with col2:
        
       Insulin = st.text_input('Insulin Level')
            
   with col2:
        
        BMI = st.text_input('BMI Rate')
        
   with col3:
            
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction level')
        
   with col3:
            
        Age = st.text_input('Age of the person')
        
   # code for prediction
   diab_diagnosis = ''
    
   # Button for prediction
        
   if st.button ('Diabetes test result'):
       
      diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
             
      if (diab_prediction[0]==1):
          diab_diagnosis = 'The person is diabetic'
      else:
          diab_diagnosis = 'The person is not diabetic'
        
   st.success(diab_diagnosis)
    
    
# Heart Disease Prediction Page    
if (selected == 'Heart Disease Prediction'):
        
  #page title
  st.title('Heart Disease Prediction using ML')
        
  #getting the input data from the user
  col1, col2  = st.columns(2)
        
  with col1:
            
     age = st.text_input('Age of the person')
            
  with col1:
    
    sex=0
    
    display = ("Male", "Female")
    
    options = list(range(len(display)))
    
    value = st.selectbox("Gender", options, format_func=lambda x: display[x])
    
    if value == "Male":
        
        sex = 1
        
    elif value == "Female":
        
        sex = 0        
            
        
  with col1:
        
        cp=0
        
        display = ("Typical angina","Atypical angina","Non — anginal pain","Asymptotic")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Chest_Pain Type", options, format_func=lambda x: display[x])
        
        if value == "Typical angina":
            
            cp = 0
            
        elif value == "Atypical angina":
            
            cp = 1
            
        elif value == "Non — anginal pain":
            
            cp = 2
            
        elif value == "Asymptotic":
            
            cp = 3
        
  with col1:
    
        trestbps = st.text_input(' Resting blood pressure')
        
  with col1:
    
        chol = st.text_input('Serum cholestoral in mg/dl')
        
  with col1:
        
        fbs=0
        
        display = ("> 120 mg/dl", "< 120 mg/dl")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Fasting blood sugar", options, format_func=lambda x: display[x])
        
        if value == "> 120 mg/dl":
            
            fbs = 1
            
        elif value == "< 120 mg/dl":
            
            fbs = 0
        
  with col1:
        
        restecg = 0
        
        display = ("Normal", "Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)","Showing probable or definite left ventricular hypertrophy by Estes criteria)")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Resting ECG results", options, format_func=lambda x: display[x])
        
        if value == "Normal":
            
            restecg = 0
            
        elif value == "Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)":
            
            restecg = 1
            
        elif value == "Showing probable or definite left ventricular hypertrophy by Estes criteria)":
            
            restecg = 2
            
        
  with col2:
    
        thalach = st.text_input('Maximum heart rate achieved')
    
  with col2:
        
        exang=0
        
        display = ("Yes", "No")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Exercise induced angina", options, format_func=lambda x: display[x])
        
        if value == "Yes":
            
            exang = 1
            
        elif value == "No":
            
            exang = 0
        
    
  with col2:
        
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    
  with col2:
      
        slope=0
        
        display = ("Upsloping", "Flat", "Downsloping")
        
        options = list(range(len(display)))
        
        value = st.selectbox("The slope of the peak exercise ST segment", options, format_func=lambda x: display[x])
        
        if value == "Upsloping":
            
            slope = 0
            
        elif value == "Flat":
            
            slope = 1
            
        elif value == "Downsloping":
            
            slope = 2
    
  with col2:
        
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    
  with col2:
      
        thal=1
        
        display = ("Fixed defect", "Normal", "Reversable")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Thal", options, format_func=lambda x: display[x])
        
        if value == "Fixed defect":
            
            thal = 1
            
        elif value == "Normal":
            
            thal = 2
                
        elif value == "Reversable":
            
            thal = 3

  #code for prediction
  heart_diagnosis = ''
    
  #create button for the result
    
  if st.button ('Heart disease prediction result'):
        
     user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

     user_input = [float(x) for x in user_input]

     heart_prediction = heart_disease_model.predict([user_input])
        

     if (heart_prediction==1):
                
        heart_diagnosis = 'The person has Heart Disease'
                
     else:
                
        heart_diagnosis = ' The person does not have Heart Disease'

  st.success(heart_diagnosis)
    
# Parkinsons Disease Prediction Page    
if (selected == 'Parkinsons Disease Prediction'):
    
    #page title
    st.title('Parkinsons Disease Prediction using ML')
    
    #getting the input data from the user
    col1, col2, col3, col4  = st.columns(4)
    
    with col1:                 
    
        Fo = st.text_input(' MDVP:Fo(Hz)')
        
    with col1:
    
        Fhi = st.text_input('MDVP:Fhi(Hz)')
    
    with col1:
        
        Flo = st.text_input(' MDVP:Flo(Hz)')
    
    with col1:
        
        Jitter = st.text_input('MDVP:Jitter(percentage)')
    
    with col1:
        
        JitterAbs = st.text_input('MDVP:Jitter(Abs)')
    
    with col1:
        
        RAP = st.text_input(' MDVP:RAP')
    
    with col2:
        
        PPQ = st.text_input('MDVP:PPQ')
    
    with col2:
        
        DDP = st.text_input('Jitter:DDP')
    
    with col2:
        
        Shimmer = st.text_input('MDVP:Shimmer')
    
    with col2:
        
        ShimmerdB = st.text_input('MDVP:Shimmer(dB)')
    
    with col2:
        
        APQ3 = st.text_input('Shimmer:APQ3')
    
    with col2:
        
        APQ5 = st.text_input('Shimmer:APQ5')
    
    with col3:
        
        APQ = st.text_input('MDVP:APQ')
    
    with col3:
        
        DDA = st.text_input('Shimmer:DDA')
    
    with col3:
        
        NHR = st.text_input('NHR')
    
    with col3:
        
        HNR = st.text_input('HNR')
    
    with col3:
        
        RPDE = st.text_input('RPDE')
    
    with col3:
        
        DFA = st.text_input(' DFA')
    
    with col4:
        
        spread1 = st.text_input('Spread1')
    
    with col4:
        
        spread2 = st.text_input('Spread2')
    
    with col4:
        
        D2 = st.text_input('D2')
    
    with col4:
        
        PPE = st.text_input('PPE')
        
    #code for prediction
    parkinsons_diagnosis = ''
    
    #create button for the result
    
    if st.button("Parkinson's disease prediction result"):
        user_input = [Fo,Fhi,Flo,Jitter,JitterAbs,RAP,PPQ,DDP,Shimmer,ShimmerdB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        
        user_input = [float(x) for x in user_input]
        
        parkinsons_prediction = parkinsons_model.predict([user_input])
        
        if (parkinsons_prediction[0]==1):
            
            parkinsons_diagnosis = "The person has parkinson's disease"
            
        else:
            
            parkinsons_diagnosis = "The person does not have parkinson's disease"
            
    st.success(parkinsons_diagnosis)
    
    
# Breast Cancer Prediction Page    
if (selected == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    #getting the input data from the user
    col1, col2, col3, col4,col5  = st.columns(5)
    
    with col1:                 
    
        meanradius = st.text_input(' Mean radius')
        
    with col1:
    
        meantexture = st.text_input('Mean texture')
    
    with col1:
        
        meanperimeter = st.text_input(' Mean perimeter')
    
    with col1:
        
        meanarea = st.text_input('Mean area')
    
    with col1:
        
        meansmoothness = st.text_input('Mean smoothness')
    
    with col1:
        
        meancompactness = st.text_input('Mean compactness')
    
    with col2:
        
        meanconcavity = st.text_input('Mean concavity')
    
    with col2:
        
        meanconcavepoints = st.text_input('Mean concave points')
    
    with col2:
        
        meansymmetry = st.text_input('Mean symmetry')
    
    with col2:
        
        meanfractaldimension = st.text_input('Mean fractal dimension')
    
    with col2:
        
        radiuserror = st.text_input('Radius error')

    with col2:
        
        textureerror = st.text_input('Texture error')
    
    with col3:
        
        perimetererror = st.text_input('Perimeter error')
    
    with col3:
        
        areaerror = st.text_input('Area error')
    
    with col3:
        
        smoothnesserror = st.text_input('Smoothness errorNHR')
    
    with col3:
        
        compactnesserror = st.text_input('Compactness error')
    
    with col3:
        
        concavityerror = st.text_input('Concavity error')
    
    with col3:
        
        concavepointserror = st.text_input(' Concave points error')
    
    with col4:
        
        symmetryerror = st.text_input('Symmetry error')
    
    with col4:
        
        fractaldimensionerror = st.text_input('Fractal dimension error')
    
    with col4:
        
        worstradius = st.text_input('Worst radius')
    
    with col4:
        
        worsttexture = st.text_input('Worst texture')
        
    with col4:
        
        worstperimeter = st.text_input('Worst perimeter')
    
    with col4:
        
        worstarea = st.text_input('Worst area')
        
    with col5:
        
        worstsmoothness = st.text_input('Worst smoothness')
        
    with col5:
        
        worstcompactness = st.text_input('Worst compactness')
    
    with col5:
        
        worstconcavity = st.text_input('Worst concavity')
        
    with col5:
        
        worstconcavepoints = st.text_input('Worst concave points')
    
    with col5:
        
        worstsymmetry = st.text_input('Worst symmetry')
        
    with col5:
        
        worstfractaldimension = st.text_input('Worst fractal dimension')
        
    #code for prediction
    breast_cancer_diagnosis = ''
    
    #create button for the result
    
    if st.button("Breast Cancer's predction result"):
        user_input = [meanradius,meantexture,meanperimeter,meanarea,meansmoothness,meancompactness,meanconcavity,meanconcavepoints,meansymmetry,meanfractaldimension,radiuserror,textureerror,perimetererror,areaerror,smoothnesserror,compactnesserror,concavityerror,concavepointserror,symmetryerror,fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstsmoothness,worstcompactness,worstconcavity,worstconcavepoints,worstsymmetry,worstfractaldimension]
        
        user_input = [float(x) for x in user_input]
        
        breast_cancer_prediction = breast_cancer_model.predict([user_input])
        
        if (breast_cancer_prediction[0]==0):
            
            breast_cancer_diagnosis = "The Breast cancer is Malignant"
            
        else:
            
            breast_cancer_diagnosis = "The Breast cancer is Benign"
            
    st.success(breast_cancer_diagnosis)
    
# Kidney Disease Prediction Page
if (selected == 'Kidney Disease Prediction'):
    
    #page title
    st.title('Kidney Disease Prediction using ML')
    
    #getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:

        age = st.text_input('Age')
        
    with col1:
    
        blood_pressure = st.text_input('Blood Pressure Level')
    
    with col1:
        
        specific_gravity = st.text_input('Specific_gravity')
        
    with col1:
    
        albumin = st.text_input('Albumin level')
        
    with col1:
    
        sugar = st.text_input('Sugar Level')
        
    with col1:
        
        red_blood_cells = 0
        
        display = ("Normal", "Abnormal")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Red blood cells", options, format_func=lambda x: display[x])
        
        if value == "Normal":
            
            red_blood_cells = 1
            
        elif value == "Abnormal":
            
            red_blood_cells = 0      
    
    with col2:
        
        pus_cell = 0
        
        display = ("Normal", "Abnormal")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Pus cell", options, format_func=lambda x: display[x])
        
        if value == "Normal":
            
            pus_cell = 1
            
        elif value == "Abnormal":
            
            pus_cell = 0
    
    with col2:
        
        pus_cell_clumps = 0
        
        display = ("Present", "Not present")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Pus cell clumps", options, format_func=lambda x: display[x])
        
        if value == "Present":
            
            pus_cell_clumps = 1
            
        elif value == "Not present":
            
            pus_cell_clumps = 0
        
    with col2:
        
        bacteria = 0
        
        display = ("Present", "Not present")
        
        options = list(range(len(display)))
        
        value = st.selectbox("Bacteria", options, format_func=lambda x: display[x])
        
        if value == "Present":
            
            bacteria = 1
            
        elif value == "Not present":
            
            bacteria = 0
            
    with col2:
    
        blood_glucose_random = st.text_input('Blood glucose random')
    
    with col2:
        
        blood_urea = st.text_input('Urea')
        
    with col2:
    
        serum_creatinine = st.text_input('Serum creatinine ')
        
    with col3:
    
        sodium = st.text_input('Sodium')
        
    with col3:
    
        potassium = st.text_input('Potassium')
    
    with col3:
        
        haemoglobin = st.text_input('Haemoglobin')
    
    with col3:
        
        packed_cell_volume = st.text_input('Packed cell volume')
        
    with col3:
 
         white_blood_cell_count = st.text_input('WBC count')
         
    with col3:
     
         red_blood_cell_count = st.text_input('RBC count')
     
    with col4:
        
         hypertension = 0
         
         display = ("Yes", "No")
         
         options = list(range(len(display)))
         
         value = st.selectbox("Hypertension", options, format_func=lambda x: display[x])
         
         if value == "Yes":
             
             hypertension = 1
             
         elif value == "No":
             
             hypertension = 0
         
    with col4:
        
         diabetes_mellitus = 0
         
         display = ("Yes", "No")
         
         options = list(range(len(display)))
         
         value = st.selectbox("Diabetes mellitus", options, format_func=lambda x: display[x])
         
         if value == "Yes":
             
             diabetes_mellitus = 1
             
         elif value == "No":
             
             diabetes_mellitus = 0   
         
    with col4:
        
         coronary_artery_disease = 0
         
         display = ("Yes", "No")
         
         options = list(range(len(display)))
         
         value = st.selectbox("Coronary artery disease", options, format_func=lambda x: display[x])
         
         if value == "Yes":
             
             coronary_artery_disease = 1
             
         elif value == "No":
             
             coronary_artery_disease = 0
         
    with col4:
        
         appetite = 0
         
         display = ("Good", "Poor")
         
         options = list(range(len(display)))
         
         value = st.selectbox("Appetite", options, format_func=lambda x: display[x])
         
         if value == "Poor":
             
             appetite = 1
             
         elif value == "Good":
             
             appetite = 0
     
    with col4:
        
         peda_edema = 0
         
         display = ("Yes", "No")
         
         options = list(range(len(display)))
         
         value = st.selectbox("Peda edema", options, format_func=lambda x: display[x])
         
         if value == "Yes":
             
             peda_edema = 1
             
         elif value == "No":
             
             peda_edema = 0
     
    with col4:
        
         aanemia = 0
         
         display = ("Yes", "No")
         
         options = list(range(len(display)))
         
         value = st.selectbox("Anemia", options, format_func=lambda x: display[x])
         
         if value == "Yes":
             
             aanemia = 1
             
         elif value == "No":
             
             aanemia = 0
    
    # code for prediction
    kidney_diagnosis = ''

    # Button for prediction
    
    if st.button ('Kidney disease prediction result'):
        
         user_input = [age,blood_pressure,specific_gravity,albumin,sugar,red_blood_cells,pus_cell,pus_cell_clumps,bacteria,blood_glucose_random,blood_urea,serum_creatinine,sodium,potassium,haemoglobin,packed_cell_volume,white_blood_cell_count,red_blood_cell_count,hypertension,diabetes_mellitus,coronary_artery_disease,appetite,peda_edema,aanemia]

         user_input = [float(x) for x in user_input]

         kidney_prediction = kidney_model.predict([user_input])
         
         if (kidney_prediction[0]==1):
             
             kidney_diagnosis= 'The person has Kidney disease'
             
         else:
             
             kidney_diagnosis = 'The person does not have Kidney disease'
    
    st.success(kidney_diagnosis)

print(pickle.format_version)
def set_bg_from_url(url, opacity=1):
    
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made by Soumen Kundu
                &nbsp;
                <a href="https://www.linkedin.com/in/Samacker25">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>          
                </a>
                &nbsp;
                <a href="https://github.com/Samacker25">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                </a>
            </p>
        </div>
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)
    
    
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://cdn.builtin.com/cdn-cgi/image/f=auto,fit=cover,w=1200,h=635,q=80/https://builtin.com/sites/www.builtin.com/files/2022-06/ai-healthcare-examples.png", opacity=0.9)