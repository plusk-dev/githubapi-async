from githubapi.exceptions import UserNotFoundError
from githubapi.utils import make_request


class User:

    @classmethod
    async def generate_user_object(cls, data: dict):
        try:
            data['username'] = data['login']
            unwanted = ["login", "node_id", "followers_url", "following_url", "gists_url", "starred_url",
                        "subscriptions_url", "organizations_url", "repos_url", "events_url", "received_events_url"]
            for i in unwanted:
                del data[i]
            user = cls()
            for m in data:
                setattr(user, m, data[m])

            return user
        except KeyError:
            raise UserNotFoundError(
                "The user with the given username was not found.")

    @property
    async def get_followers(self):
        """Get an array of `User` objects that follow the user.

        Returns:
            `list`: An array of users that follow the user.
        """

        results = await make_request(f"/users/{self.username}/followers")
        followers = []
        try:
            for data in results:
                user = await self.generate_user_object(data)
                followers.append(user)
            return followers
        except KeyError:
            raise UserNotFoundError(
                "The user with the given username was not found.")

    @property
    async def get_following(self):
        """Get an array of `User` the user follows.

        Returns:
            `list`: An array of users that the user follows.
        """
        results = await make_request(f"/users/{self.username}/following")
        following = []
        try:
            for data in results:
                user = await self.generate_user_object(data)
                following.append(user)
            return following
        except KeyError:
            raise UserNotFoundError(
                "The user with the given username was not found.")

    @property
    async def get_repos(self):
        results = await make_request(f"/users/{self.username}/repos")
        repos = []
        for repo in results:
            k = await Repository.generate_repository_object(repo)
            k.owner = await self.generate_user_object(repo['owner'])
            repos.append(k)
        return repos


class Repository:
    @classmethod
    async def generate_repository_object(cls, data: dict):
        repo = cls()
        for i in data:
            if not i.endswith("url"):
                setattr(repo, i, data[i])

        repo.owner = "test"
        return repo

    @property
    async def parent(self):
        if self.fork:
            response = await make_request(f"/repos/{self.owner.username}/{self.name}")
            parent_repo = response["parent"]
            return await self.generate_repository_object(parent_repo)
