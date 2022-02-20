from flask import Flask, request, render_template
from ProductForm import ProductForm
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	form = ProductForm(request.form)
	if request.method == 'POST' and form.validate():
		mock_data = [[form.color.data,form.weight.data,form.rating.data]]
		#result is a list of predictions, each prediction is wrapped in a list
		result = model.predict(mock_data)[0][0]
		return f"<p>Our best guess is ${round(result,2)}!</p>"
	return render_template('index.html', form=form)
	
if __name__ == '__main__':
	model = pickle.load(open('./mock_model.sav', 'rb'))
	app.run()
	