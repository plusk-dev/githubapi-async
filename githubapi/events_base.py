from githubapi.utils import make_request
from githubapi.objs import Repository, User


class Event:

    """Base class for events

    Properties:
        actor: The user who took the action which led to the event.
        repository: The repository associated with the event.
    """

    @property
    async def actor(self):
        response = await make_request(f"/users/{self.actor_login}")
        return await User.generate_user_object(response)

    @property
    async def repository(self):
        response = await make_request(f"/repos/{self.repository_name}")
        return await Repository.generate_repository_object(response)
