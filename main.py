from flask import Flask, request, jsonify

app = Flask(__name__)
{
"data" : [
    {
        'Contact': "9987644456",
        'Name': "Raju",
        'done':False
        'id': 1,
    },
   {
        'Contact': "9987644456",
        'Name': "Raju",
        'done':False
        'id': 1,
    }
]
}
# App.route is a decortaor which tells the web app which Url endpoint is associated with the function
@app.route("/")
def hello_world():
    return ("Hello World")

#Post is used to send data to the server to create or update a resource
@app.route("/addtask", methods = ["POST"])


def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        }, 400)
    task = {
        'id':tasks[-1]['id']+1,
        'title': request.json['Name'],
        'Contact': request.json.get('Contact'),
        'done':False    
        }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"task added successfully"
    })

@app.route("/gettask")

def get_task():
    return jsonify({
        "data":tasks
    
    })




# To run the application
if __name__ == "__main__":
    app.run(debug = True)

