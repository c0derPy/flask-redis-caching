from flask import Flask
from flask import request, jsonify
from config import BaseConfig
from flask_caching import Cache

import logging

logging.basicConfig(filename='debug.log', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
app.config.from_object(BaseConfig)
cache = Cache(app)

@app.route('/square/<int:number>')
@cache.cached(timeout=10)
def square(number):
    app.logger.info("Computing the square of {}".format(number))
    return jsonify({"Computed: ":number*number})

if __name__ == '__main__':
    app.run()
