from flask import Flask,request
import pymongo

def get_db():
    client = pymongo.MongoClient(host='demo_mongodb',
                         port=27017, 
                         username='cars', 
                         password='carpass',
                        authSource="admin")
    db = client["cars_db"]
    return db

app=Flask(__name__)

@app.route('/addcar',methods=['post'])
def add_car():
    try:
        print("ÏN")
        db = get_db()
        val=request.get_json()
        print(val)
        db['cars'].insert_one(val)

        return "Added successfully"

    except Exception as e:
        print("error accures :" +str(e))
        return "failed to add"


@app.route('/view',methods=['get'])
def find_collcetion():
    try:
        db = get_db()
        result=list(db['cars'].find({},{"_id":0}))
        print(result)
        return {"data":result}

    except Exception as e:
        print("error accures :" +str(e))
        return "failed to view"

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)