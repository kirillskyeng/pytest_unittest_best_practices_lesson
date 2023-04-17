import requests


def get_user_repos(username: str) -> list:
    """Получает список репозиториев пользователя на GitHub."""
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return [repo["name"] for repo in response.json()]
