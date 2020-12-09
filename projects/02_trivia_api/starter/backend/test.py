from flaskr import create_app

app=create_app()
#app.run(host='127.0.0.1', port=5000, debug=True)
if __name__=="main":
    app.run(debug=True)
