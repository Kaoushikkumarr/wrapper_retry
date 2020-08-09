
from retry import retry
from flask import Flask, request
from flask_restful import Resource, Api
from config.config import PLATFORM_URL, PATH_FINDER

from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)



class Wrap_api_url(Resource):

    def __init__(self):
        pass

    @retry(exceptions=Exception, tries=3, delay=0, max_delay=None)
    def get(self):
        static_url = PLATFORM_URL + '/' + PATH_FINDER  # import STATIC variables from config.config

        id = request.args.get('id')
        dynamic_url = request.args.get('controller')

        """result = requests.get('{}/pathfinder/certificate/{}'.format(PLATFORM_URL, id))"""

        url = '{}/{}/{}'.format(static_url, dynamic_url, id)
        print(url)

        if not url:  # OR try with if url != request.get(url):

            raise Exception

        return url


api.add_resource(Wrap_api_url, '/wrapper', methods=['GET'])
# api.add_resource(Wrap_api_url, '/wrapper/<string:controller>/<int:id>', methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
