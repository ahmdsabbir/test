# from flask import Blueprint
# from .utils import sleepy
# site = Blueprint('site', __name__)


# @site.route('/sleep', methods=['POST'])
# def sleep():
#     x = sleepy()
#     return x


from flask import Blueprint, jsonify
from .utils import site_report_task

site = Blueprint('site', __name__)

@site.route('/sleep', methods=['POST'])
def sleep():
    # Call Celery task
    site_report_task.delay()

    # Return response
    return jsonify({'message': 'Task scheduled successfully'})