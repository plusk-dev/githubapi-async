from githubapi.events_base import Event


class CommitCommentEvent:
    def __init__(self) -> None:
        raise DeprecationWarning("THE LIBRARY STILL DOESNT SUPPORT THIS TYPE OF EVENT")

    # i didnt even find any user who has performed this event, so i am totally not familiar with what type of response body this event has. so im leaving it empty here, if you find anything then be sure to contribute :)


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
        ...