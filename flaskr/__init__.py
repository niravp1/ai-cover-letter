import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from . import db, groq_client



def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            ALLOWED_EXTENSIONS = {'pdf', 'docx'}

            def check_file(filename: str):
                return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
            
            uploaded_file = request.files['resume']
            if uploaded_file.filename == '':
                 return jsonify({"Error": "Not Found"}), 404

            if check_file(uploaded_file.filename):
                groq_client(uploaded_file)
                return jsonify({"Success" : "File Uploaded"}), 200

    return app
