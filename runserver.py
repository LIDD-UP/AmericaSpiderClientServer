from AmericaSpiderClientServer import app


if __name__ == '__main__':
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port='5001', debug=True)
    # app.run(host='0.0.0.0', port='5000', debug=True)




