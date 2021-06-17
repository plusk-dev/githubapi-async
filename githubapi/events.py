from githubapi.events_base import Event
from githubapi.objs import Repository, User

class CommitCommentEvent:
    def __init__(self) -> None:
        raise DeprecationWarning("THE LIBRARY STILL DOESNT SUPPORT THIS TYPE OF EVENT")

    # i didn't even find any user who has performed this event, so i am totally not familiar with what type of
    # response body this event has. so im leaving it empty here, if you find anything then be sure to contribute :)


class CreateEvent(Event):
    @classmethod
    async def create_object(cls, data: dict):
        cls.actor_login = data["actor"]["login"]
        cls.repository_name = data["repo"]["name"]
        del data["actor"]
        del data["repo"]
        for i in data:
            setattr(cls, i, data[i])
        return cls


class DeleteEvent(Event):
    @classmethod
    async def create_object(cls, data: dict):
        await CreateEvent.create_object(data=data)


class ForkEvent(Event):
    @classmethod
    async def create_object(cls, data: dict):
        cls.actor_login = data["actor"]["login"]
        cls.repository = await Repository.generate_repository_object(data=data["payload"]["forkee"])
        del data["actor"]
        del data["repo"]
        for i in data:
            setattr(cls, i, data[i])
        return cls


class GollumEvent(Event):
    """
    ive got no idea what this event means, i mean, i do know its related to wikis but i couldn't find an example for it
    """

    def __init__(self):
        raise DeprecationWarning("THE LIBRARY STILL DOESNT SUPPORT THIS TYPE OF EVENT")


class IssueCommentEvent(Event):
    @classmethod
    async def create_object(cls, data:dict):
        cls.actor_login = data["actor"]["login"]
        cls.repository_name = data["repo"]["name"]
        # TODO: Create The Issue Object :)

class IssuesEvent(Event):
    @classmethod
    async def create_object(cls, data: dict):
        cls.actor_login = data["actor"]["login"]
        cls.repository_name = data["repo"]["name"]
        payload = data["payload"]
        cls.creator = await User.generate_user_object(payload["issue"]["user"])
        return cls