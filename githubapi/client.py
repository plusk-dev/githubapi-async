from githubapi.exceptions import QueryMissingError
from githubapi.objs import Repository, User
from githubapi import ENDPOINT
from githubapi.utils import make_request
import warnings
from typing import List


class GithubAPIClient:
    def __init__(self):
        self.endpoint = ENDPOINT

    async def get_user(self, username: str) -> User:
        """A method to get the data of a user by their username.

        Args:
            `username` (str): GitHub username of the user.

        Returns:
            `User` Object:
                `id` (str): The user's GitHub ID
                `username` (str): The user's GitHub username
                `avatar_url` (str): The user's GitHub avatar URL
                `gravatar_id` (str): The user's GitHub gravatar ID (if present)
                `name` (str): The user's full name
                `blog` (str): The URL to the user's blog page
                `bio` (str): The user's bio
                `company` (str): The company where the user works, if any
                `location` (str): The user's location
                `followers` (int): The number of user's followers
                `following` (int): The number of people the user follows
                `twitter_username` (str): The user's twitter username (if provided)
                `last_updated` (str): The last time user updated their profile
                `created_at` (str): The time of user's account creation.
        """
        data = await make_request(f"/users/{username}")
        return await User.generate_user_object(data)

    async def search_user(
        self,
        keyword: str,
        page: int = 1,
        per_page: int = 30,
        sort: str = "",
        order: str = ""
    ) -> List[User]:
        if per_page > 100:
            warnings.warn(
                "The GitHub API does not allow more than 100 search results per page.")
        response = await make_request(f"/search/users?q={keyword}&page={page}&order={order}&per_page={per_page}&sort={sort}")
        if len(keyword) == keyword.count(" "):
            raise QueryMissingError("A Query is required to run search.")
        users = []
        for user in response["items"]:
            m = await User.generate_user_object(user)
            users.append(m)

        return users


    async def search_repositories(
        self,
        keyword: str,
        page: int = 1,
        per_page: int = 30,
        sort: str = "",
        order: str = ""
    ) -> List[Repository]:
        if per_page > 100:
            warnings.warn(
                "The GitHub API does not allow more than 100 search results per page.")
        response = await make_request(f"/search/repositories?q={keyword}&page={page}&order={order}&per_page={per_page}&sort={sort}")
        if len(keyword) == keyword.count(" "):
            raise QueryMissingError("A Query is required to run search.")
        repos = []
        for repo in response["items"]:
            m = await Repository.generate_repository_object(repo)
            repos.append(m)

        return repos
