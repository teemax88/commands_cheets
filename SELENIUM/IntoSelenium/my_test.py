class TestSuit:
    def test_1(self, app):
        app.test_git()
        assert True

    def test_2(self, app):
        app.test_google()
        assert True
