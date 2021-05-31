from githubapi.objs import  User
from githubapi import ENDPOINT
from githubapi._session import make_request


class GithubAPIClient:
    def __init__(self):
        self.endpoint = ENDPOINT

    async def get_user(self, username: str):
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

    async def search_user(self, keyword):
        pass
