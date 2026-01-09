import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("testdata_MIE.csv") 

def run_llm_output(df):
    #############################
        if 'Gender' not in df.columns and 'Geschlecht' not in df.columns:
            raise ValueError("The dataset does not contain a dedicated gender column ('Gender' or 'Geschlecht').")

        col = 'Gender' if 'Gender' in df.columns else 'Geschlecht'
        counts = df[col].value_counts()

        plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
        plt.title('Gender distribution')
        plt.tight_layout()
        plt.show()
    #############################

run_llm_output(df)

 