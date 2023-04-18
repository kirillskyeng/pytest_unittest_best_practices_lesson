from unittest.mock import patch
from src.github_api import get_user_repos


def test_get_user_repos():
    with patch("src.github_api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        assert get_user_repos('test_user') == ["repo1", "repo2"]
        mock_get.assert_called_with("https://api.github.com/users/test_user/repos")
