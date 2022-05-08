from flask import Flask, jsonify, abort, send_file
import yaml

app = Flask(__name__)

versions = None

def load_versions():
    with open("data/versions.yaml", "r") as stream:
        try:
            global versions
            versions = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

@app.route('/versions/<string:app_name>', methods=['GET'])
def get_versions(app_name):
    return versions[app_name]

if __name__ == '__main__':
    load_versions()
    app.run(host='0.0.0.0', port=5000)

