
class User:
    
    def __init__(self,name,followers):
       self.name = name
       self.followers = followers
       self.list_Of_Userfollowers = []
      

    def person (self, name, followers):
       person = {"name":name, "followers":followers}
       new_person = self.list_Of_Userfollowers.append(person)
       print(new_person)
    

harry = User(name= "Harry",followers=["munyao","mugaka","nyambura"])
print(harry.name)
print(harry.followers)
# print(harry.person(name= "Harry",followers=["munyao","mugaka","nyambura"]))







    