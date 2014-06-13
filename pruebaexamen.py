__author__ = 'Amine Banks'

print("hola")

class getWrite:
    contains = True
    app1='Free',
    app2 = 'pay'
    price = '10'
    download = ''
    punctuation = ''
    comment = ''
    objects = ['appli free','Google Play Store','16-05-2014','Price: 0','download: 100', 'number Punctuation: 100', 'Punctuation', 'Number comment: 10']
    objects2 =['appli pay', 'App Store','16-05-2014','Price = 10','download = 20', 'number Punctuation: 20', 'Punctuation', 'Number comment: 0']
    def __init__(self, contains):
        self.contains=contains
    def setContains(self, contains):
        self.contains = contains
    def getObjects(self):
        return self.objects
    def getObjects2(self):
        return self.objects2
    #write in the file if is application free
    def write(self):
        with open('file.txt', mode='w', encoding='utf-8') as archive:
            for i in self.getObjects():
                 for line in self.getObjects2():
                    archive.write(line +"\n")

            archive.write(i +"\n")

a = getWrite("test.txt")



ans=True
while(ans):
    print(""" 1.Add a Student
              2.Delete a Student
              3.Look Up Student Record
              4.Exit/Quit
              """)
    ans=input("What would you like to do?")
    if ans=="1":
      print(a.getObjects())
    elif ans=="2":
      print("\n Student Deleted")
    elif ans=="3":
      print("\n Student Record Found")
    elif ans=="4":
      print("\n Goodbye")
      break
    elif ans !="":
      print("\n Not Valid Choice Try again")