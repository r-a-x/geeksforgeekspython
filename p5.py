# https://www.geeksforgeeks.org/google-interview-experience-off-campus/
# Q1: Implement the version control map system which takes the snapshot of the versions of data. Implement the following functions:
#
# put(key, value) -> puts the value again the key in the latest version of the map
#
# get(key) -> get the value of the key for the latest version of the data
#
# snapshot() -> take a snapshot and increment the version
#
# getValVersion(version id, key) -> return value of the key of the particular version
#
# A: I made use of maps of vectors like this map<int, vector<pair<int, int>> versionMap;

from collections import defaultdict

class VersionControl:

    def __init__(self):
        self.version = 0
        self.versionMap = defaultdict(lambda:dict)
        pass

#I will pass the value to
    def put(self, key, value):
        self.versionMap[self.version][key] = value
        pass

    def get(self, key):
        return self.getValVersion(self.version, key)

    def snapshot(self):
        self.version = self.version + 1

    def getValVersion(self, version, key):
        if key not in self.versionMap[version]:
            return 0
        return self.versionMap[version][key]
