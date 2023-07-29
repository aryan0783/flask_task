import logging
logging.basicConfig(filename='calculator.log',level=logging.INFO,format='%(asctime)s %(name)s %(levelname)s %(message)s')
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def calculate():

    try:

        if request.method == 'GET':
            return render_template('calculator.html')
        else:
            if request.form['button'] == "add" :
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result = num1 + num2

            elif request.form['button'] == "subtract" :
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result = num1 - num2

            elif request.form['button'] == "multiply" :
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result = num1 * num2

            elif request.form['button'] == "divide" :
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result = num1 / num2

            if request.form['button']== 'Reset':
                result = ''

            logging.info(f'{num1} {request.form["button"]} {num2} : {result}')
                
            return render_template('calculator.html',results = result)

    except Exception as e:
        logging.error(f'Error occurred in the calculator operation : {e}')

if __name__ == '__main__':
    app.run(debug = True)