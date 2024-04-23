import pandas as pd

df_breast_cancer = pd.read_csv('Breast_Cancer.csv', sep=",", header=0)

# Check for missing values
missing_values = df_breast_cancer.isnull().sum()
print("Missing Values:\n", missing_values)

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

wd_stage_mapping = {
    'Well differentiated': 0,
    'Moderately differentiated': 1,
    'Poorly differentiated': 2,
    'Undifferentiated': 3
}
df_breast_cancer['WD Stage'] = df_breast_cancer['WD Stage'].map(wd_stage_mapping)
