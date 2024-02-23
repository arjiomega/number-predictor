import pickle
from pathlib import Path

import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neighbors import KNeighborsClassifier

MODEL_SAVEPATH = Path(__file__).parent.resolve()
MODEL_NAME = "mnist_clf"

def split_data(X,y):
    X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]
    
    return X_train, X_test, y_train, y_test

def load_data():
    mnist = fetch_openml('mnist_784', as_frame=False)
    X_train, X_test, y_train, y_test = split_data(mnist.data, mnist.target)
    
    return X_train, X_test, y_train, y_test

def train():
    # Load data
    X_train, X_test, y_train, y_test = load_data()
    
    print(np.unique(X_train[0]))
    
    # Train model
    clf = KNeighborsClassifier()
    clf.fit(X_train,y_train)
        
    # Score model
    print(clf.score(X_test,y_test))
    print(clf.predict_proba(X_train[0].reshape(1,-1)))
    
    # Save model
    pickle.dump(clf, open(Path(MODEL_SAVEPATH,MODEL_NAME+'.pickle'), 'wb'))
    

if __name__ == "__main__":
    train()