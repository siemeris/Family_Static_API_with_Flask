
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        #member["id"] = self._generateId()
        self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if person["id"]==id:
                self._members.remove(person)
                return True
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        for person in _members:
            if person["id"]==id:
                self._members.remove(person)
                self._members.append(member)
        pass

    def get_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if person["id"]==id:
                return person
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
