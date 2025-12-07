import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("testdata_MIE.csv") 

def run_llm_output(df):
    #############################
        required = {'Finding', 'Value'}
        missing = required.difference(df.columns)
        if missing:
            raise ValueError(f'Missing required columns: {missing}')

        mask = df['Finding'] == 'Diagnose'
        subset = df.loc[mask]

        counts = subset['Value'].value_counts().head(5)

        counts.plot(kind='bar')
        plt.xlabel('Diagnosis code')
        plt.ylabel('Count')
        plt.title('Top 5 secondary diagnoses')
        plt.tight_layout()
        plt.show()
    #############################

run_llm_output(df)

 