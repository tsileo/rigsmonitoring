from datetime import datetime
import requests

from pycgminer import CgminerAPI

from flask import Flask, jsonify
from flask.ext.cache import Cache

from flask_yeoman import flask_yeoman

cgminer = CgminerAPI()

app = Flask(__name__, static_folder='app')
cache = Cache(app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp/'})

app.config.update(DEBUG=False)
app.config.from_pyfile('settings.cfg')
app.register_blueprint(flask_yeoman)


def _get_profile():
    """ Retrieve profile data from Slush's Pool API. """
    r = requests.get('https://mining.bitcoin.cz/accounts/profile/json/{0}'.format(app.config['SLUSH_TOKEN']),
                     verify=False)
    r.raise_for_status()
    profile = r.json()
    profile['total_reward'] = str(float(profile['confirmed_reward']) + float(profile['unconfirmed_reward']))
    workers = []
    for worker_name, worker in profile['workers'].iteritems():
        w = dict(worker)
        w['name'] = worker_name
        w['last_share_ts'] = float(w['last_share'])
        w['last_share'] = datetime.utcfromtimestamp(float(w['last_share'])).isoformat()
        workers.append(w)
    profile['workers'] = workers
    return profile


@app.route('/api/slush/')
@cache.cached(timeout=70)
def api_rounds_model():
    r = requests.get('https://mining.bitcoin.cz/stats/json/{0}'.format(app.config['SLUSH_TOKEN']),
                     verify=False)
    r.raise_for_status()
    blocks = []
    for block_id, block in r.json().get('blocks').iteritems():
        b = dict(block)
        b['id'] = int(block_id)
        blocks.append(b)

    return jsonify(rounds=sorted(blocks, key=lambda x: x['id'], reverse=True)[:20],
                   profile=_get_profile())


@app.route('/api/btc_guild/')
def api_btc_guild():
    r = requests.get('https://www.btcguild.com/api.php', params={'api_key': app.config['BTC_GUILD_API_KEY']})
    r.raise_for_status()
    return jsonify(data=r.json())


@app.route('/api/cgminer/devs')
def cgminer_devs():
    return jsonify(devs=cgminer.devs()['DEVS'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=app.config['PORT'])
