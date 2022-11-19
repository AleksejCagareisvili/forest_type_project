import pandas as pd
import numpy as np
import pickle
#import os
from feature_function import return_df		#подключаем функцию генерации признаков


import flask
from flask import Flask, render_template, request


#creating instance of the class
app=Flask(__name__, template_folder='templates')

loaded_model = pickle.load(open('model_lgmb.pkl', 'rb'))

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#prediction function
def ValuePredictor(df):
	X = df.values
	result = loaded_model.predict(X)
	return result[0]


@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		to_predict_dict = request.form.to_dict()
		to_predict_values = list(map(int, to_predict_dict.values()))
		df_cut = pd.DataFrame(np.array(to_predict_values).reshape(1,10), columns=to_predict_dict.keys())
		df_cut_full = return_df(df_cut)

		result = ValuePredictor(df_cut_full)

		if int(result)==0:
			prediction='Класс №1 - ель/пихта. Лесная зона - Neota'
		elif int(result)==1:
			prediction='Класс №2 - сосна. Лесная зона - Rawah/Comanche Peak'
		elif int(result)==2:
			prediction='Класс №3 - сосна Ponderosa. Лесная зона - Cache la Poudre'
		elif int(result)==3:
			prediction='Класс №4 - тополь/ива'
		elif int(result)==4:
			prediction='Класс №5 - ель/пихта/осина'
		elif int(result)==5:
			prediction='Класс №6 - пихта Douglas'
		else:
			prediction='Класс №7 - прочее'

		return render_template('index.html', prediction=prediction)


if __name__=="__main__":
	app.run(debug=True)







