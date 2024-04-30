from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# apply LDA on the dataset
def lda(X_train, X_test, y_train, y_test):
    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train, y_train)
    y_pred = lda.predict(X_test)
    print("LDA Accuracy: ", accuracy_score(y_test, y_pred))
    print("LDA Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
    print("LDA Classification Report: \n", classification_report(y_test, y_pred))
    return lda

if __name__ == "__main__":
    # Split the dataset
    X_train, X_test, y_train, y_test = split_dataset()