from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    progress = """Starting Flight Price Prediction Machine Learning Project
                    Day-1: 16072022"""
    return progress


if __name__=="__main__":
    app.run(debug=True)