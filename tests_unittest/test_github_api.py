import unittest
from unittest.mock import patch
from src.github_api import get_user_repos


class TestGetUserRepos(unittest.TestCase):
    @patch("src.github_api.requests.get")
    def test_get_user_repos(self, mock_get):
        mock_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        self.assertEqual(get_user_repos('test_user'), ["repo1", "repo2"])
        mock_get.assert_called_with("https://api.github.com/users/test_user/repos")
