from robot.api.deco import keyword
from robot.api import logger
from RequestsLibrary.RequestsOnSessionKeywords import RequestsOnSessionKeywords


class CustomRequests(RequestsOnSessionKeywords):

    @keyword("Login On Session")
    def login_on_session(self, alias, url, params=None, expected_status=None, msg=None, **kwargs):
        session = self._cache.switch(alias)
        response = session.request("login", url, params=params, **kwargs)
        logger.info("Got response: {}".format(response.text))
        self._check_status(expected_status, response, msg)
        return response
