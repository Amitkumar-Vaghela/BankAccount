database=[]
class bank:
  # pass
  # print('hello bank')
  def register_data(self,name,phone):
    database.append([name,phone])
class user:
  def welcome(self):
     return "hello user"
     
  def register(self,name,phone):
    bank().register_data(name,phone)
    return 'created successfully'
  def login(self,name,phone):
    if[name,phone] in database:
      return 'logged in successfully'
      
    else:
      return 'login failed'
  def unregister(self,name,phone):
    if[name,phone] in database:
      bank().unregister_user(name,phone)
      return 'unregister successfully'
    else:
      return ' no user exits'
    

obj=user()
print(obj.welcome())
print(obj.register('Amit',809069))
print(obj.register('Om',8099069))
print(obj.login('Om',8099069))
print(database)
print(obj.unregister('sonu',89745454))
