import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("testdata_MIE.csv") 
counts = df['secondary_diagnosis'].value_counts().head(5) 

def run_llm_output(df):
    #############################
    # Get the five most common secondary diagnoses
    secondary_diagnoses = df['Finding'].value_counts().head(5)

    # Plot the five most common secondary diagnoses
    secondary_diagnoses.plot(kind='bar', stacked=True)
    plt.xlabel('Secondary Diagnoses')
    plt.ylabel('Number of Patients')
    plt.title('Five Most Common Secondary Diagnoses')
    plt.show()
    #############################
 



run_llm_output(df)
