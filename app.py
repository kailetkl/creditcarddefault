#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan_amount = request.form.get("loan_amount")
        print(income, age, loan_amount)
        model=load_model("creditcarddefault")        
        pred=model.predict([[float(income),float(age),float(loan_amount)]])
        print(pred)
        pred = pred[0]
        s = "The predicted credit card default is: " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="Credit Card Default Prediction"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("80"))


# In[ ]:




