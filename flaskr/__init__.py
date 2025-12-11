import os
from dotenv import load_dotenv
from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from . import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/upload', methods=['POST'])
    def hello():
        ALLOWED_EXTENSIONS = {'pdf', 'docx'}
        def check_file(filename: str):
            return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
        
        uploaded_file = request.files['resume']
        if uploaded_file.filename == '':
            #TODO  throw something  to frontend that file is empty
            print('Empty file')    
        if check_file(uploaded_file.filename):
            uploaded_file = secure_filename(uploaded_file.filename)
            print('ok')
            return 'success'
        #db.init_db()

    return app
