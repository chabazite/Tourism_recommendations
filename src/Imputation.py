def lowerSalaryNoAgeImpute(df):
    """
    This function will replace any NaN Age value that also has a Monthly income of less than 19000 with the mean age of the partitioned data that has an income less than 19000. 

    Args:
        df (Dataframe): Tourism dataframe

    Returns:
        dataframe: Dataframe with some Age NaN values replaced based on their monthly income being less than 19000
    """

    low_income_age = round(df[df['MonthlyIncome'] > 19000]['Age'].mean(), 0)

    mask =  (df['Age'].isna()) & (df['MonthlyIncome'] < 19000)    

    df.loc[mask,'Age'] = low_income_age
    
    return df


def designationAverageAgeCalulation(df):
    """
    This function will help prevent data leakage. It will calculate the mean ages of each degisnation from the given dataframe. This will only be the partitioned data during modeling, again to prevent leakage.

    Args:
        df (dataframe): partitioned dataframe for modelling (e.g. training data)

    Returns:
        int: an age for each designation stored as an interger variable.
    """

    executive_age = round(df[df['Designation'] == 'Executive']['Age'].mean(), 0)

    manager_age = round(df[df['Designation'] == 'Manager']['Age'].mean(),0)

    senior_manager_age = round(df[df['Designation'] == 'Senior Manager']['Age'].mean(), 0)

    VP_age = round(df[df['Designation'] == 'VP']['Age'].mean(), 0)

    AVP_age = round(df[df['Designation'] == 'AVP']['Age'].mean(), 0)


    return executive_age, manager_age, senior_manager_age, VP_age, AVP_age

def designationNoAgeImputation(df):
    """
    Based on the designation age calulation function, this function will replace  

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    executive_age, manager_age, senior_manager_age, VP_age, AVP_age =designationAverageAgeCalulation(df)
    
    mask_exec =  (df['Age'].isna()) & (df['Designation'] == "Executive")    
    df.loc[mask_exec,'Age'] = executive_age

    mask_manager =  (df['Age'].isna()) & (df['Designation'] == "Manager")    
    df.loc[mask_manager,'Age'] = manager_age

    mask_SM =  (df['Age'].isna()) & (df['Designation'] == "Senior Manager")    
    df.loc[mask_SM,'Age'] = senior_manager_age

    mask_AVP =  (df['Age'].isna()) & (df['Designation'] == "AVP")    
    df.loc[mask_AVP,'Age'] = AVP_age

    mask_VP =  (df['Age'].isna()) & (df['Designation'] == "VP")    
    df.loc[mask_VP,'Age'] = VP_age    


    return df
    
def AgeNoMonthlyIncomeImputation(df):
     """
     This function will impute any missing incomes by the median value of monthly income for that particular age.

     Args:
         df (dataframe): partitioned dataframe (e.g. training data)

     Returns:
         dataframe: dataframe without missing income values
     """

     income_by_age = df.groupby(['Age'])['MonthlyIncome'].agg(['median']).reset_index()

   
     for index, age in enumerate(income_by_age['Age']):
         mask = (df['MonthlyIncome'].isna()) & (df['Age'] == age)    

         df.loc[mask,'MonthlyIncome'] =income_by_age['median'].loc[index]
    
     return df