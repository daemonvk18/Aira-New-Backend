from flask import Flask, request, jsonify
import time
import logging
from database.models import init_db

app = Flask(__name__)

# Initialize MongoDB and collections - store the result
db_initialized = init_db(app)

# Only import blueprints after DB is initialized
if db_initialized:
    from routes.auth import auth_bp
    from routes.assessment import assessment_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(assessment_bp)

@app.route('/api/hello', methods=['GET'])
def hello():    
    name = request.args.get('name', 'World')
    return jsonify(message=f'Hello, {name}!')

if __name__ == "__main__":
    app.start_time = time.time()
    logging.info("Starting AIRA Therapist application")
    app.run(debug=True)