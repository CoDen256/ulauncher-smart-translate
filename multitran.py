import requests

host="http://192.168.0.55:8080"
apiPrefix= "/api/multitran"

class Mutltitran:

    def __init__(self, hostname=host, apiPrefix=apiPrefix):
        self.hostname = hostname
        self.apiPrefix = apiPrefix

    def get_translations(self, source, target, phrase):
        data = {
            "sourceLanguage" : source,
            "targetLanguage": target,
            "phrase" : phrase
        }
        return requests.post(self.resolve("translation"), json=data).json()

    def resolve(self, endpoint):
        return self.hostname + apiPrefix + "/" + endpoint
if __name__ == '__main__':
    multitran = Mutltitran()
    print(multitran.get_translations("EN", "RU", "dick"))

