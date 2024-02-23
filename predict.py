

def predict(X_flatten, model) -> tuple[list, list[list[float]]]:
    clf = model
    prediction = clf.predict(X_flatten)
    prediction_proba = clf.predict_proba(X_flatten)
    
    prediction_proba_dict = {str(i): proba for i, proba in enumerate(prediction_proba[0])}
    
    return prediction[0], prediction_proba_dict