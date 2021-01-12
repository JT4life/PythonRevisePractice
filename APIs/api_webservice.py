import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        if self._data == "" or self.query == "":
            raise StopIteration

        items = self._data["items"]

        for dic in items:

            for key, value in dic.items():
                if key == "tags":
                    if self.query in dic[key]:
                        self.result.append(dic)

                        yield dic

        if self.result == []:
            raise StopIteration


    def first(self):
        # search generator and return the first found item
        pass

s = SearchByTag("data_file.json","crime")
print(s.search())