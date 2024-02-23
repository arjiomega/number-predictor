# Number Predictor

A streamlit app for predicting the number drawn by the user.

![image](https://i.imgur.com/eCf06GH.png)

## Usage

Install Dependencies
```bash
pip install -r requirements.txt
```

Train the model our streamlit app is going to  use
```bash
python model/train.py
```

Run the streamlit app
```bash
export PYTHONPATH=$(pwd)
streamlit run streamlit/app.py
```

We need to export `PYTHONPATH` to easily handle the dependencies.