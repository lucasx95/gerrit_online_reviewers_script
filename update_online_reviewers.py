from pygerrit2.rest import GerritRestAPI
from requests.auth import HTTPDigestAuth
import time

while True:
    auth = HTTPDigestAuth('', '')
    rest = GerritRestAPI(url='http://gerrit.url', auth=auth)
    online_group = rest.get('/groups/')['online-reviewers']
    members = list(map(lambda x: x['_account_id'], rest.get('/groups/' + online_group['id'] + '/members/')))
    online_fake = [25, 35]
    remove = list(filter(lambda x: x not in online_fake, members))
    add = list(filter(lambda x: x not in members, online_fake))
    for remove_id in remove:
        rest.delete('/groups/' + online_group['id'] + '/members/' + str(remove_id))
    for add_id in add:
        rest.put('/groups/' + online_group['id'] + '/members/' + str(add_id))
    time.sleep(900)
