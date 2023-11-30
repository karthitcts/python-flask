from flask import Flask, render_template, jsonify

app = Flask(__name__)

PlATFORM = [
  {
    'id': 1,
    'title': 'WEBQ Voice',
    'feature': 'Offering voice quality test automation',
    'link': 'https://192.168.2.143'
  },
  {
    'id': 2,
    'title': 'WEBQ Speed',
    'feature': 'Offering Speed test automation',
    'link': 'http://192.168.2.178/'
  },
  {
    'id': 3,
    'title': 'WEBQ Automation',
    'feature': 'Offering several automation like RFC2544, 5G core testing, Network protocol testing, etc .,',
    'link': 'http://192.168.2.141:8080'
  }
]

@app.route("/")
def webq_home():
    return render_template('home.html', 
                           platform=PlATFORM, 
                           company_name='TCTS WEBQ')

@app.route('/test', methods = ['GET', 'POST']) 
def test(): 
    if(request.method == 'GET'): 
  
        data = "Success::- WEBQ application is hosted"
        return jsonify({'data': data}) 

@app.route("/api/platforms")
def list_platform():
  return jsonify(PLATFORM)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=3000)
