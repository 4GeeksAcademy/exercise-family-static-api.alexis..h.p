"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, Date_member):
        new_member = {
            "id": self._generate_id(),
            "first_name": Date_member["first_name"],
            "last_name": Date_member["last_name"],
            "age": Date_member["age"],
            "lucky_numbers": Date_member["lucky_numbers"]
        }
        self._members.append(new_member)
        pass
   
    def get_member_for_id(self,id): 
        for member in self._members: 
            if member["id"] == id:
                return member
        return None

    def delete_member(self, id):
     member = self.get_member_for_id(id)
     if member is None:
        return {"message": "miembro no encontrado"}, 404
     self._members.remove(member)
     return "miembro eliminado"
  
        
            

    def get_member(self, id):
        for member in self._members: 
            if member["id"] == id:
                return member
            return "miembro no encontrado",400
        pass

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members