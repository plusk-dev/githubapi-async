from githubapi.utils import make_request
from githubapi.objs import Repository, User


class Event:

    async def actor(self):
        response = await make_request(f"/users/{self.actor_login}")
        return await User.generate_user_object(response)

    async def repository(self):
        response = await make_request(f"/repos/{self.repository_name}")
        return await Repository.generate_repository_object(response)
