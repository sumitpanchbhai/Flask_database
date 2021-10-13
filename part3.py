from flask import Flask,request
import part2

app = Flask(__name__)

@app.route('/insert',methods=['POST'])
def insert():
    data=request.get_json()
    part2.api.insert_method(data)
    return "data inserted successfully"

@app.route('/delete',methods=['POST'])
def delete():
    data=request.get_json()
    part2.api.delete_method(data)
    return "record deleted succesfully"

@app.route('/update',methods=['POST'])
def update():
    data=request.get_json()
    part2.api.update_method(data)
    return "updated successfully"

@app.route('/fetch',methods=['GET'])
def fetch():
    data=request.args['name']
    return part2.api.fetch_method(data)

if __name__ == "__main__":
    app.run(debug=True,port=5019)