import json
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
    if !self.user: return None
    url = "https://www.wanikani.com/api/user/%s/%s" \
    % (self.user.apikey, resource)
    print(url)

  def user_information(self):
    """User information call"""
    pass

  def study_queue(self):
    pass

  def level_progression(self):
    pass

  def srs_distribution(self):
    pass

  def recent_unlocks(self, limit=10):
    pass

  def critical_items(self, thresh=75):
    pass

  def radicals(self, level=None):
    pass

  def kanji(self, level=None):
    pass

  def vocab(self, level=None):
    pass
