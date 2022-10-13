
Tourism Classification
=======================

## Business Case
<a name="Business_Case"></a>
The `Tourism.xlsx` file contains the last year of customer data at a travel package company. These customers have been pitched 1 of 5 different travel packages - Basic, Standard, Deluxe, Super Deluxe, King. Looking at the data of the last year, we observed that only 18% of the customers purchased the package they were pitched. Dig into the data and develop a recommendation model that will tell the company's sales team which package they should pitch based on the customer's attributes.

## Table of Contents
<details open>
  <summary>Show/Hide</summary>
  <br>
 
1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Structure ](#Structure)
4. [ Conclusion ](#Evaluation)
5. [ Future Improvements ](#Future_Improvements)

</details>


## Project Organization

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
 <br>


    ├── LICENSE
    ├── .gitignore
    ├── README.md          <- The top-level README for developers using this project.
    ├──
    ├── data
    │   ├── intermediate   <- Intermediate data that has been transformed.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── venv                <- Virtual Environment for the project
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
    
--------
  </details>   

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>

    ├──Python
        ├──Numpy
        ├──Pandas
        ├──Missingno
        ├──Matplotlib
        ├──Seaborn
        └──Scikit-learn
 ------------
 </details>

## Structure of Notebooks:
<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>

 1. Data Cleaning
      * 1.1 Load xlmx file into Pandas
      * 1.2 Check basic statistics of data
      * 1.3 Clean data of value errors
      * 1.4 Dealing with Null values
      * 1.5 Save dataset
 2. Exploratory Data Analysis
      * 2.1 Load Data
      * 2.2 Univariate Analysis
      * 2.3 Correlation of Variables
      * 2.4 Analysis of Product Taken Variable
      * 2.5 Analysis of Products Pitched Variable
      * 2.6 Analysis of City Tier Variable
 3. Modeling
      * 3.1 Load Data
      * 3.2 Feature Engineering
      * 3.3 Train/Test Split
      * 3.4 Create Custom Transformers
      * 3.5 Baseline Model 
      * 3.6 Feature Selection
      * 3.7 Hyperparameter tuning and model update
      * 3.8 Save Model

 </details>

## Conclusion:
<a name="Evaluation"></a>
<details>
<summary>Show/Hide</summary>
<br>
  
### Data Cleaning
* No duplicates were found
* Outliers were found in: DurationOfPitch, NumberOfTrips, and MonthlyIncome
* Both Gender and MaritalSatus had categorical errors that were cleaned
* Eight columns were noted to have missing data: Age, TypeOfContact, DurationOfPitch, NumberOfFollowups, PreferredPropertyStar, NumberOfTrips, NumberOfChildrenVisiting, and MonthlyIncome
    *   From these eight, I chose to ignore: DurationOfPitch, NumberOfFollowups, and TypeOfContact as they were not specific to the Customer, but rather the sales associate
    *  For the remaining five, I created functions of the imputation methods for each feature, specific to the data presented. 
    *  **Notable:** Age and MonthlyIncome were able to use each other to fill in missing information for more accurate representation of the data. Other features used median or mean of the entire feature for imputation.

### Exploritory Data Analysis

#### Univariate Analaysis
##### Occupation
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/Occupation.png">
<br>
  - The Occupation feature isn’t very explanatory, the categories within are confusing and imbalance. It will be removed during feature selection.

##### Designations
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/Designation.png">

##### Products Pitched
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/ProductPitched.png">


##### Designation and Product Pitched
  - When grouping designations against the product pitched category, I see that it is a 1 to 1 match. 
  - This means every time, for example, an Executive was pitched a product it was Basic.
  - This category is not suited for modeling as it will give us 100% accuracy but no insights.

#### Bivariate Analaysis
##### Correlations
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/Correlation.png">
<br>
  - NumberOfChildrenVisiting and NumberOfPersonVisiting have a correlation. This may indication children are included in the person visiting feature and may be removed in our model.
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/AgeVIncome.png">
<br>
  
  - There is a decent correlation with the mean average of MonthlyIncome and Age. This may need to be addressed during feature selection.

##### Product Accepted vs. Rejected
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/AgevPTaken.png">
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/IncomeVPTaken.png">
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/IncomeVPTaken_Line.png">
<br>
  
  - There wasn't any big insights with how products were accepted vs. rejected when looking at the customer profile.

##### Product Recommendations
<br>
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/AgeVProductPitched.png">
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/IncomeVPP.png">
<br>
  
  - Age and Income clearly play a role in which package was recommended, as seen in the significance testing. It didn't, however, have an impact on whether the recommendation was accepted or not.

### Model Performance

#### Model
Our model will be multi-class Classification. XGBoost was choosen for its robust nature and high quality average performance. There are 4 main reasons for this:
    1. Ensemble models generally outperform individual models
    2. Boosting generally outperforms bagging (RandomForest)
    3. The default model provides for regularization to protect against overfitting
    4. The hyperparameters have shown, when tweaked, to provide impressive model performance

#### Metric
The metric best suited for this project is a  F1_macro score. 
    1. Since we have a high class imbalance, F1 scores are the right choice for our metric as it considers both precision and recall.
    2. The choice between weighted, micro, and macro is also important. While weighted would give us more consideration to the basic package, since it had more occurances, macro would give us equal consideration to all packages. Micro would be a better choice if we had a balanced dataset.

#### Baseline
Using my custom Transformers, I created a sklearn pipeline to preprocess the data before feeding into our model. This helps protect against data leakage. Our F1_macro score was **78%**. This was cross-validated. Not a bad score for a base model with a small dataset. 
<br>
This confusion matrix helps to visualize how our model predicted vs. what the actual results were. 
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/base_CM.png">

#### Improvements
After the baseline model was trained, we went into feature selection. A lot of times there are features that don't provide any input to the model, these can be removed as they just bulk the model for no reason. Other times, there are features that are highly correlated to other features. For example, Gender_Male and Gender_Female. This project considers them binary features. If you are male, you are not female, and vice versa. That means the model only needs one of the two features to inform it of gender. This is known as multicollinearity. After feature selection, I trained and tested the model to ensure no drop in performance. The F1_macro was stil **78%**.
<br>
Finally, I used GridSearchCV to help quickly and systematically test a series of hyperparameters for XGBoost in order to improve performance.

#### Comparison
With this new model trained and cross-validated, I show a F1_macro score of **79%**. There is definitely more improvement to be made on this model, but for a system that had a 18% record of success, a model that 79% of the time provides a good insight into the correct product, is a huge improvement
<br>
You can see the improvement in the confusion matrix.
<img src="https://github.com/chabazite/Tourism_recommendations/blob/main/reports/figures/best_fit_CM.png">


</details>
  
## Future Improvements
 <a name="Future_Improvements"></a>
 <details>
<summary>Show/Hide</summary>
<br>

 1. Go back to the source of the information and uncover issues with unclear features to improve the data gathered and future model.
 2. Dive deeper into feature selection. 
 3. Try different models for classification (KNeighbor, RandomForest, etc.)
 4. Train with more hyperparameters 
 5. Use Deep Learning models if warranted by budget and improvement
 6. Create API for easier access and interpretability of model
 

</details>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
<p>README outline tailored from [awesomeahi95][]<p>
