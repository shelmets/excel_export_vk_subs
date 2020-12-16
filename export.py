from abc import ABC, abstractclassmethod
from source import Source
import time

class Export(ABC):
    @abstractclassmethod
    def __init__(self, source:Source, chunk:int):
        self.source = source
        self.chunk = chunk

    @abstractclassmethod
    def to_write(self, subs):
        pass

    def export(self, group_id, token):
        count_subs = self.source.get_count_subs_of_group(group_id, token)
        offset = 0
        while(count_subs > 0):
            time.sleep(1)
            self.to_write(self.source.get_subs_of_group(group_id, self.chunk, offset, token))
            offset += self.chunk
            count_subs-=self.chunk


class ConsoleExport(Export):

    def to_write(self, subs):
        print(subs)


class CSVExport(Export):
    def __init__(self, source:Source, chunk:int):
        super().__init__(source, chunk)
        self.file_name = "members.csv"
        self.stream = open(self.file_name, 'w')
        self.stream.write("ID ВК, Имя, Фамилия\n")

    def dispose(self):
        self.stream.close()

    def to_write(self, subs):
        subs = map(lambda i: "{0},{1},{2}".format(i["id"], i["first_name"], i["last_name"]), subs)
        for line in subs:
            self.stream.write(line + "\n")



            