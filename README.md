# loanstatus-prdiction

<To predict loan status>
  This ML project aims to create a randondomforest gridsearch model that will classify how much loan the user can obtain based on various factors such as the user’s marital status, income, education, employment prospects, number of dependents, etc.
  
  
  
  project1 file: Contains below model preprocessing and model building part.
      >model training i.e. removing outliers , filling null values (both for categorical as well as numerical values) , removing skewness
      >feature engineering 
      >Balancing data
      >randondomforest gridsearch model
      >Kfold validation
 
   app file : Contains python code of flask deployment.
   
   model.pkl: pickle file where the model is dumped.
   
   templates/index.html : Contains html page code.
