import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("testdata_MIE.csv")  

def run_llm_output(df):
    #############################
    if 'Gender' not in df.columns and 'Geschlecht' not in df.columns:
        print("The dataset does not contain a dedicated gender column ('Gender' or 'Geschlecht'). I cannot reliably create the requested plot.")
    else:
        col = 'Gender' if 'Gender' in df.columns else 'Geschlecht'
        counts = df[col].value_counts()
        plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
        plt.title('Gender distribution')
        plt.show()
    #############################
 



run_llm_output(df)
