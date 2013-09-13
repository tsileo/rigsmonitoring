from flask import Flask, redirect, url_for, jsonify, request, make_response, request, current_app, abort, render_template
from flask.ext.cache import Cache

app = Flask(__name__, static_folder='app')
cache = Cache(app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp/'})
from datetime import timedelta, datetime
import requests
import time


app.config.update(DEBUG=False)
app.config.from_pyfile('settings.cfg')

from flask_yeoman import flask_yeoman

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


@app.route("/api/slush/")
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

    return jsonify(rounds=sorted(blocks, key=lambda x: x['id'], reverse=True)[:16],
                   profile=_get_profile())

from hashlib import sha1
import hmac
import json

from redis import Redis

r = Redis(db=5)

KEY = '\x88\xc0\xb3H\xe7d\x8a.\xf86\xdf\xf9h\x96\xee=7\x00\xcc\xd0|\x88\x98\xc5\x91\x8d\xa3\xa3\x807\xadu\xa9\x0e\xa8i\x99\x90\xf3p\x89^\xb2|eV\x88\x83\xdf\x16\x9cM0\xf7;\x02\xcc\x1c\x85\x0f\x9ceE\xe3N\xadQ.l0l\x1d\x97y\x1b\x18|K05\xf2v\x80m\xb0\xb1>\xa4\xf5\x1b\xf598\x8c*\x071\xc9\xdc\xaf;yha9b\xf2/o\x82k\x06 \xf9\x14\xe9\xeb\xc9\x8a/\xbd\x95\x95P\xdd\x1f\xae\xe9'


@app.route('/api/check_last_share')
def check_last_share():
    auth = request.headers.get('Authorization')
    if not auth:
        abort(500)
    user_id, hmac_hash = auth.split(':')
    if r.sismember('testapp:nonce:{0}'.format(user_id), json.loads(request.data)['nonce']):
        abort(401)
    if hmac.new(KEY, request.data, sha1).hexdigest() != hmac_hash:
        abort(401)
    r.sadd('testapp:nonce:{0}'.format(user_id), json.loads(request.data)['nonce'])
    profile = _get_profile()
    alerts = []
    for w in profile['workers']:
        elapsed = time.time() - w['last_share_ts']
        if elapsed > 500.0:
            alerts.append(dict(data={'elapsed': elapsed, 'worker_name': w['name']},
                               msg=u'Worker {0} last share: {1} ({2} seconds ago).'.format(w['name'], w['last_share'], int(elapsed))
                               ))
    # 70 / 130
    return jsonify(alerts=alerts, id='check_last_share')

@app.route('/website')
def website():
    return render_template('website.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
