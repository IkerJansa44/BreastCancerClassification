import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Generate some sample data (replace this with your own dataset)
data = pd.read_csv('data/Breast_Cancer_Preprocessed.csv')

# Separate features (X) from labels if applicable
X = data.drop(columns=['Race', 'Marital Status','Status'])

# Perform PCA
pca = PCA()
X_pca = pca.fit_transform(X)

# Get the explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_

# Calculate cumulative explained variance
'''cumulative_variance = explained_variance_ratio.cumsum()

# Plot histogram
plt.figure(figsize=(8, 6))
plt.bar(range(1, len(cumulative_variance) + 1), cumulative_variance, alpha=0.6)
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance Ratio')
plt.title('Cumulative Explained Variance Ratio by Number of Principal Components')
plt.grid(True)
plt.show()'''

# Get the principal components
components = pca.components_

# Plot original features as vectors in PCA space
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)  # Plot data points

features = ['Age','T Stage','N Stage','6th Stage','differentiate','A Stage','Tumor Size',
            'Estrogen Status','Progesterone Status','Regional Node Examined','Regional Node Positive',
            'Survival Months','Status']
# list of 13 colors
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'gray', 'orange', 'purple', 'brown', 'pink']
# Plot vectors representing original features
for i, (pc1, pc2) in enumerate(zip(components[0], components[1])):
    plt.arrow(0, 0, pc1*30, pc2*30, color=colors[i], alpha=1, width=0.05, head_width=0.5, label=features[i])
    
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA with Original Features as Vectors')
plt.legend()
plt.grid(True)
plt.show()
