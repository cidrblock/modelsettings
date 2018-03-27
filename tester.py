from modelsettings import settings
from pprint import pprint
import logging




#
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger('twelvesettings')
# logger.setLevel(logging.DEBUG)

#
# with open("settings_dev.yml", 'r') as stream:
#     try:
#         filec = yaml.load(stream)
#     except yaml.YAMLError as exc:
#         print(exc)

# print(settings.RETRY)

# pprint(vars(settings))
#
# class Settings(dict):
#
#     # FOO = dict(value="aaa", help="bbb")
#     # VALUE = 5
#
#     # def __repr__(self):
#     #     return self['value']
#     def __getitem__(self, item):
#         print(self['FOO'])
#     # def __call__(self, *args, **kwargs):
#     #     print(args)
#     #     print(kwargs)
#     #     return self['value']
#
# class Settings(dict):
#     def __getattr__(self, *args, **kwargs):
#         print(args)
#         return self[args[0]] #['value']
#     def __setattr__(self, attr, value):
#         self[attr] = value
#     def help(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return self[attr]['help']


# class Settings(dict):
#     def __init__(self, *args, **kwargs):
#         super(Settings, self).__init__(*args, **kwargs)
#         self.__dict__ = self
#
#     def __getattr__(self, attr):
#         print(attr)
#         return self[attr]
#
#     def __getitem__(self, attr):
#         print(attr)
#         print('here')
#         return self[attr]
    #     print(key)
    #     return self.store[self.__keytransform__(key)]['value']

#
# class Settings(AttrDict):
#     """A dictionary that applies an arbitrary key-altering
#        function before accessing the keys"""
#     #
#     # def __init__(self, *args, **kwargs):
#     #     self.store = AttrDict()
#     #     self.update(dict(*args, **kwargs))  # use the free update to set keys
#
#     def __getitem__(self, key):
#         print(key)
#         return self.store[self.__keytransform__(key)]['value']
#     #
    # def __setitem__(self, key, value):
    #     self.store[self.__keytransform__(key)] = value
    #
    # def __delitem__(self, key):
    #     del self.store[self.__keytransform__(key)]
    #
    # def __iter__(self):
    #     return iter(self.store)
    #
    # def __len__(self):
    #     return len(self.store)
    #
    # def __keytransform__(self, key):
    #     return key
    #
    # def help(self, key):
    #     return self.store[self.__keytransform__(key)]['help']
#
#
# dikt = Settings(FOO=Settings(value="aaa", help="bbb"))
#
# print(dikt.FOO)
#
# print(dikt.FOO.help())
#
# dikt.FOO.help()
#
# print(dikt.help('FOO'))
#
# # print(dikt)
# dikt['value'] = "hi"

# print(dikt() + 5)
# print(f"{dikt}")
#
# def do(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# do(dikt)
