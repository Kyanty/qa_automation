"""  ConfTests apiBREWERY"""
import json
import random
import pytest
import requests


class APIClient:
    """  Returns lists of names, cities, states, types, ids"""

    def __init__(self, address='http://api.openbrewerydb.org/breweries', name=list(), city=list(),
                 state=list(), b_type=list(), ids=list()):
        self.address = address
        self.name = name
        self.city = city
        self.state = state
        self.b_type = b_type
        self.ids = ids
        breweries = requests.get(address)
        all_item = json.loads(breweries.content)
        for item in all_item:
            ids.append(item['id'])
            name.append(item['name'])
            city.append(item['city'])
            state.append(item['state'])
            b_type.append(item['brewery_type'])

    def do_get_by_name(self):
        """  Returns lists of names, cities, states, types, ids"""
        name = random.choice(self.name)
        # print(name)
        first_word = name.partition(" ")[0]
        # print(first_word)
        url = "/?by_name=".join([self.address, first_word])
        # print(url)
        return requests.get(url)

    def do_get_by_city(self):
        """  Returns lists of names, cities, states, types, ids"""
        city = random.choice(self.city)
        url = "/?by_city=".join([self.address, city])
        # print(url)
        return requests.get(url)

    def do_get_by_state(self):
        """  Returns lists of names, cities, states, types, ids"""
        state = random.choice(self.state)
        url = "/?by_state=".join([self.address, state])
        # print(url)
        return requests.get(url)

    def do_get_by_type(self):
        """  Returns lists of names, cities, states, types, ids"""
        b_type = random.choice(self.b_type)
        url = "/?by_type=".join([self.address, b_type])
        # print(url)
        return requests.get(url)

    def do_get_by_ids(self):
        """  Returns lists of names, cities, states, types, ids"""
        ids = random.choice(self.ids)
        url = "/".join([self.address, str(ids)])
        # print(url)
        return requests.get(url)


class APIDog:
    """  Returns lists of breeds, subbreeds"""
    def __init__(self, address='https://dog.ceo/api/breeds/list/all',
                 breed=list(), subbreed=list()):
        self.address = address
        self.breed = breed
        self.subbreed = subbreed
        list_all = requests.get("https://dog.ceo/api/breeds/list/all")
        data = json.loads(list_all.content)
        breed.append(data["message"])

    def return_random_breed(self):
        """ DISPLAY an array of all breeds FROM ALL DOGS COLLECTION"""
        eds = self.breed[0]
        breeds = list(eds.keys())
        return random.choice(breeds)

    def return_random_subbreed(self):
        """ DISPLAY an array of all breeds FROM ALL DOGS COLLECTION"""
        eds = self.breed[0]
        subbreeds = list(eds.keys())
        return random.choice(subbreeds)


def pytest_addoption(parser):
    """  Add option --address"""
    parser.addoption("--url", action="store", dest="urls", choices=["b", "d", "c"],
                     default=["https://dog.ceo/api/breeds/list/all",
                              "https://api.cdnjs.com/libraries",
                              "http://api.openbrewerydb.org/breweries"])
    parser.addoption("--all", action="store",
                     default=["https://dog.ceo/api/breeds/list/all",
                              "https://api.cdnjs.com/libraries",
                              "http://api.openbrewerydb.org/breweries"])


@pytest.fixture(scope="module", autouse=True)
def api_dog_url(request):
    """  Returns APIClient's example"""
    if request.config.getoption("--url") == "d":
        dog = APIDog("https://dog.ceo/api/breeds/list/all")
    else:
        dog = APIDog("https://dog.ceo/api/breeds/list/all")
    return dog


@pytest.fixture(scope="module", autouse=True)
def api_cdnjs_url(request):
    """  Returns APIClient's example"""
    if request.config.getoption("--url") == "c":
        cdnjs = "https://api.cdnjs.com/libraries"
    else:
        cdnjs = "https://api.cdnjs.com/libraries"
    return cdnjs


@pytest.fixture(scope="module", autouse=True)
def api_brewery_url(request):
    """  Returns APIClient's example"""
    if request.config.getoption("--url") == "b":
        brewery = APIClient("http://api.openbrewerydb.org/breweries")
    else:
        brewery = APIClient("http://api.openbrewerydb.org/breweries")
    return brewery


FIELDS = ["version", "description", "homepage", "keywords", "license",
          "repository", "autoupdate", "author", "assets"]


@pytest.fixture(params=FIELDS)
def fields_fix(request):
    """  Tests api_cdnjs"""
    return request.param


@pytest.fixture(params=["https://api.cdnjs.com/libraries"])
def adrs(request):
    """  Tests api_cdnjs"""
    return request.param


@pytest.fixture(params=["", "output=human"])
def output_human(request):
    """  Tests api_cdnjs output=human"""
    return request.param


@pytest.fixture(params=[
    # DISPLAY an array of all breeds FROM ALL DOGS COLLECTION"""
    "https://dog.ceo/api/breeds/list/all",
    # Returns an array of all the sub-breeds from a breed"""
    "https://dog.ceo/api/breed/",
    # DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION"""
    "https://dog.ceo/api/breeds/image/random"])
def lst_from_all(request):
    """Docstring"""
    return request.param


@pytest.fixture(params=[
    # Returns an array of all the images from the sub-breed"""
    "https://dog.ceo/api/breed/"])
def img_random_subbreed(request):
    """Docstring"""
    return request.param


@pytest.fixture(params=[
    # DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION"""
    "https://dog.ceo/api/breeds/image/random/",
    # MULTIPLE IMAGES FROM A BREED COLLECTION"""
    "https://dog.ceo/api/breed/",
    # MULTIPLE IMAGES FROM A SUB-BREED COLLECTION"""
    "https://dog.ceo/api/breed/"
])
def img_random_breed(request):
    """Docstring"""
    return request.param
