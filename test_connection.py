import config
import pycurl
from urllib import urlencode
import json
from io import BytesIO

data = BytesIO()

c = pycurl.Curl()
c.setopt(pycurl.URL, config.API_URL)
c.setopt(pycurl.CAINFO, config.PEM_FILE)
c.setopt(c.WRITEFUNCTION, data.write)

payload = {'key':config.API_KEY,
            'Operation':'GetEntities',
            'Entity':'cobalt_meetingregistration',
            'Attributes':'createdby',
            'Filter':'CreatedOn<ge>2013-03-01'}

postfields = urlencode(payload)

c.setopt(c.POSTFIELDS, postfields)
c.perform()

dictionary = json.loads(data.getvalue())
print(len(dictionary['Data']))
