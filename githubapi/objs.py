from githubapi.exceptions import EventTypeNotFound, UserNotFoundError
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
    async def get_followers(self) -> list:
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
    async def get_following(self) -> list:
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
    async def get_repos(self) -> list:
        """Get a list of the user's repositories.

        Returns:
            `list`: A list of the user's repositories. Each repository is a `Repository` object.
        """
        results = await make_request(f"/users/{self.username}/repos")
        repos = []
        for repo in results:
            k = await Repository.generate_repository_object(repo)
            repos.append(k)
        return repos

    async def events(
            self,
            per_page: int = 30,
            page: int = 100,
            event_type=None,
    ):
        response = await make_request(f"/users/{self.username}/events/public?per_page={per_page}&page={page}")
        events = []
        for event in response:
            try:
                if event_type is None:
                    event_import = __import__(
                        "githubapi.events", fromlist=[event["type"]])
                    event_class = getattr(event_import, event["type"])
                    event_object = await event_class.create_object(event)
                    events.append(event_object)
                elif event_type is not None:
                    try:
                        event_import = __import__(
                            "githubapi.events", fromlist=[str(event_type.__name__)])
                        event_class = getattr(
                            event_import, str(event_type.__name__))
                        event_object = await event_class.create_object(event)
                        event_payload = type(
                            "Payload", (object,), event_object.payload)
                        event_object.payload = event_payload
                        if event["type"] == event_type.__name__:
                            events.append(event_object)
                    except Exception:
                        raise EventTypeNotFound(
                            f"Event of type {str(event_type.__name__)} does not exist.")
            except Exception as e:
                raise EventTypeNotFound(
                    f"Event of type {event['type']} does not exist.")
        return events


class Repository:

    async def make_request_for_repo(self, url: str) -> dict:
        return await make_request(f"/repos/{self.owner.username}/{self.name}{url}")

    @classmethod
    async def generate_repository_object(cls, data: dict):
        repo = cls()
        for i in data:
            if not i.endswith("url"):
                setattr(repo, i, data[i])
        repo.owner = await User.generate_user_object(data['owner'])
        return repo

    @property
    async def parent(self):
        if self.fork:
            response = await self.make_request_for_repo("")
            parent_repo = response["parent"]
            return await self.generate_repository_object(parent_repo)

    @property
    async def events(self):
        response = await self.make_request_for_repo("/events")
        return response

    @property
    async def issues(self):
        response = await self.make_request_for_repo("/issues")
        return response

    @property
    async def contributors(self):
        response = await self.make_request_for_repo("/contributors")
        return response

    @property
    async def languages(self):
        response = await self.make_request_for_repo("/languages")
        return response

    @property
    async def comments(self):
        response = await self.make_request_for_repo("/comments")
        return response

    @property
    async def commits(self):
        response = await self.make_request_for_repo("/commits")
        return response
        
class Issue:
    @classmethod
    async def generate_issue_object(cls, data: dict):
        pass
