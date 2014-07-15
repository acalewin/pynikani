import requests

class User:
  def __init__(self, apikey=None):
    self._apikey = apikey

  @property
  def apikey(self):
    """The user's apikey"""
    return self._apikey

  @apikey.setter
  def apikey(self, nval):
    self._apikey = nval

  @apikey.deleter
  def apikey(self):
    del self._apikey

class Wanikani:
  def __init__(self, apikey):
    self.user = User(apikey=apikey)

  @property
  def user(self):
    """User object to make apicalls against"""
    return self._user

  @user.setter
  def user(self, nval):
    self._user = nval

  @user.deleter
  def user(self):
    del self._user

  def _call(self, resource, arg=None):
    """Consolidating making resource calls to the WK api"""
    if not self.user: return None
    url = "https://www.wanikani.com/api/user/%s/%s" \
    % (self.user.apikey, resource)
    if arg:
      url += "/%s" % arg
    req = requests.get(url)
    req.raise_for_status()
    return req.json()

  def user_information(self):
    """User information call"""
    data = self._call(resource="user-information")
    return data['user_information']

  def study_queue(self):
    """Study queue call"""
    data = self._call(resource="study-queue")
    return data['requested_information']

  def level_progression(self):
    """Level progression call"""
    data = self._call(resource="level-progression")
    return data['requested_information']

  def srs_distribution(self):
    """SRS distribution call"""
    data = self._call(resource="srs-distribution")
    return data['requested_information']

  def recent_unlocks(self, limit=10):
    """Recent unlocks
      limit: max number of items to return"""
    data = self._call(resource='recent-unlocks', arg=limit)
    return data['requested_information']

  def critical_items(self, thresh=75):
    """Critical items
      thresh: threshold of percentage correct to use"""
    data = self._call(resource='critical-items', arg=thresh)
    return data['requested_information']

  def radicals(self, level=None):
    """radicals api call
      level: level to retrieve radicals from"""
    data = self._call(resource='radicals', arg=level)
    return data['requested_information']

  def kanji(self, level=None):
    """kanji api call
      level: level to retrieve kanji from"""
    data = self._call(resource='kanji', arg=level)
    return data['requested_information']

  def vocab(self, level=None):
    """vocabulary api call
      level: level to retrieve vocab from"""
    data = self._call(resource='vocabulary', arg=level)
    if level: #This needs to be unwrapped, because for some reason
      return data['requested_information']
    else:
      return data['requested_information']['general']
