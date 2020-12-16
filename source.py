from abc import ABC, abstractclassmethod

class Source(ABC):

    @abstractclassmethod
    def get_subs_of_group(self, group_id, token):
        pass

    @abstractclassmethod
    def get_count_subs_of_group(self, group_id, count, offset, token):
        pass

import vk

class VkSource(Source):
    def __init__(self, v):
        session = vk.Session()
        self.api = vk.API(session, v=v)
    
    def get_count_subs_of_group(self, group_id, token):
        res = self.api.groups.getById(access_token=token, group_ids = group_id, fields = "members_count")
        return int(res[0]["members_count"])

    def get_subs_of_group(self, group_id, count, offset, token):
        res = self.api.groups.getMembers(access_token = token, group_id = group_id, count = count, offset = offset)
        res = self.api.users.get(user_ids=res["items"], access_token=token)
        return res

