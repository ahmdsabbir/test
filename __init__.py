# from flask import Flask
# from flask import jsonify

# from .routes import site
# from .utils import sleepy
# from celery import Celery

# def create_app(config_file='config.py'):
#     app = Flask(__name__)

#     app.config.from_pyfile(config_file)
#     # Configure Celery
#     app.config['CELERY_BROKER_URL'] = 'redis://redis'
#     app.config['CELERY_RESULT_BACKEND'] = 'redis://redis'
#     celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
    
#     app.register_blueprint(site, url_prefix='/api/site')

#     # Define task function
#     @celery.task(name='app.site_report_task')
#     def site_report_task():
#         report_data = sleepy()
#         # Do something with report_data, e.g. save to database
    
#     return app


from celery import Celery
from flask import Flask
from .routes import site
from .utils import sleepy, site_report_task


def create_app(config_file='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Configure Celery
    app.config['CELERY_BROKER_URL'] = 'redis://localhost'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost'
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    # Register blueprints
    app.register_blueprint(site, url_prefix='/api/site')

    return app