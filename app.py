from flask import Flask, jsonify

app = Flask(__name__)

def factoriall(n):
    if n < 0:
        return "No esta definido para numeros negativos"
    elif n == 0: 
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

@app.route('/factorial/<number>')
def factorial_page(number):
    number = int(number)
    factorial = factoriall(number)
    return jsonify({'number': number, 'factorial': factorial})

if __name__ == '__main__':
    app.run(debug=True)
