# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:13:03 2021

@author: vaishali.gunjal
"""

from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
         
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender_Male=1
                 
        else:
            Gender_Male=0
        
        Married=request.form['Married']
        if(Married=='Yes'):
            Married_Yes=1
                 
        else:
            Married_Yes=0
            
        Dependents = int(request.form['Dependents'])
        
         
            
        
        Education=request.form['Education']
        if(Education=='Graduate'):
            Education_Not =0
                 
        else:
            Education_Not =1
        
        Self_Employed=request.form['Self_Employed']
        if(Self_Employed=='Yes'):
            Self_Employed_Yes=1
                 
        else:
            Self_Employed_Yes=0
        
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        TotalIncome=ApplicantIncome + CoapplicantIncome
        TotalIncomeLog=np.log(TotalIncome)
        
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        EMI=LoanAmount/Loan_Amount_Term
        EMI=np.log(EMI)
        
        Credit_History = float(request.form['Credit_History'])
        
        Property_Area = (request.form['Property_Area'])
        if(Property_Area=='Semiurban'):
            Property_Area_Semiurban=1
            Property_Area_Urban=0
        elif((Property_Area=='Urban')):
            Property_Area_Semiurban=0
            Property_Area_Urban=1
        else:
            Property_Area_Semiurban=0
            Property_Area_Urban=0


        prediction=model.predict([[Dependents, Credit_History, TotalIncomeLog, EMI, Gender_Male,Married_Yes, Education_Not , Self_Employed_Yes, Property_Area_Semiurban, Property_Area_Urban]])
        output=int(prediction[0])
        print(output)
        if output==1:
            return render_template('index.html',prediction_text="Applicable for Loan:)")
        else:
            return render_template('index.html',prediction_text="Sorry Loan cannot be given!")


if __name__=="__main__":
    app.run(debug=True)