import pandas as pd


def transform_balance_data():
    df_breast_cancer = pd.read_csv('data/Breast_Cancer.csv', sep=",", header=0)
    # Check for missing values
    missing_values = df_breast_cancer.isnull().sum()

    # Transformations
    stage_mapping = {
        'IIA': 0,
        'IIB': 1,
        'IIIA': 2,
        'IIIB': 3,
        'IIIC': 4
    }
    df_breast_cancer['6th Stage'] = df_breast_cancer['6th Stage'].map(stage_mapping)

    t_stage_mapping = {
        'T0': 0,
        'T1': 1,
        'T2': 2,
        'T3': 3,
        'T4': 4
    }
    df_breast_cancer['T Stage'] = df_breast_cancer['T Stage'].map(t_stage_mapping)

    n_stage_mapping = {
        'N0': 0,
        'N1': 1,
        'N2': 2,
        'N3': 3,
        'N4': 4
    }
    df_breast_cancer['N Stage'] = df_breast_cancer['N Stage'].map(n_stage_mapping)

    a_stage_mapping = {
        'Regional': 0,
        'Distant': 1,
    }
    df_breast_cancer['A Stage'] = df_breast_cancer['A Stage'].map(a_stage_mapping)

    diff_mapping = {
        'Well differentiated': 0,
        'Moderately differentiated': 1,
        'Poorly differentiated': 2,
        'Undifferentiated': 3
    }
    df_breast_cancer['differentiate'] = df_breast_cancer['differentiate'].map(diff_mapping)

    es_status_mapping = {
        'Negative': 0,
        'Positive': 1
    }
    df_breast_cancer['Estrogen Status'] = df_breast_cancer['Estrogen Status'].map(es_status_mapping)
    df_breast_cancer['Progesterone Status'] = df_breast_cancer['Progesterone Status'].map(es_status_mapping)

    status_status_mapping = {
        'Alive': 1,
        'Dead': 0
    }
    df_breast_cancer['Status'] = df_breast_cancer['Status'].map(status_status_mapping)

    # Eliminate grade column
    df_breast_cancer = df_breast_cancer.drop(columns=['Grade'])
    # keep 1500 rows having all the Status=0 and the rest of the rows having Status=1
    df_breast_cancer = df_breast_cancer.sort_values(by='Status', ascending=True)
    df_breast_cancer = df_breast_cancer.iloc[:1500, :]
    # Randomize the order of the dataframe
    df_breast_cancer = df_breast_cancer.sample(frac=1).reset_index(drop=True)
    df_breast_cancer.to_csv('data/Breast_Cancer_Preprocessed.csv', index=False)

