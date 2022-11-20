import json

class ZendeskSearch():
    def __init__(self):
        self.searchTerm = ''
        self.searchValue = ''

    def displayIntro(self):
        print(' ')
        print("Welcome to Zendesk Search")
        print("Type \'quit\' to exit at any time, Press \'Enter\' to continue ")
        print(' ')

    def displayMenu(self):
        print(' '*5,"Select Search options: ")
        print(' '*5,"* Press 1 to search Zendesk ")
        print(' '*5,"* Press 2 to view a list of searchable fields ")
        print(' '*5,"* Type \'quit\' to exit")

    def selectMainMenu(self):
        selectOption = input()

        if selectOption == '1':
            self.searchMode()

        elif selectOption == '2':
            self.displaySearchMethod()

        elif selectOption == 'quit':
            self.terminateProgram()
    
    def searchMode(self):
        selectMode = input("Select 1)Users or 2)Tickets or 3)Organization \n")
        if selectMode == 'quit':
            self.terminateProgram()

        self.searchTerm = input("Enter search term \n")

        if self.searchTerm == 'quit':
            self.terminateProgram()

        self.searchValue = input("Enter search value \n")
        if self.searchValue == 'false' or self.searchValue == 'true':
            self.searchValue = self.searchValue.capitalize()

        if self.searchValue == 'quit':
            self.terminateProgram()
        
        if selectMode == '1':
            with open(r'json\users.json', encoding='utf-8') as users:
                usersData = json.load(users)
            searchFor = 'Users'
            self.searchFun(usersData,searchFor)

        elif selectMode == '2':
            with open(r'json\tickets.json', encoding='utf-8') as tickets:
                ticketsData = json.load(tickets)
            searchFor = 'Tickets'
            self.searchFun(ticketsData,searchFor)

        elif selectMode == '3':
            with open(r'json\organizations.json', encoding='utf-8') as organizations:
                organizationsData = json.load(organizations)
            searchFor = 'Organizations'
            self.searchFun(organizationsData,searchFor)

        else:
            self.terminateProgram()

    def searchFun(self,Data,searchFor):
        flag = False
        total = 0
        finalList = []
        for data in Data:
            flag = False
            for keys,values in data.items():
                if keys == self.searchTerm and str(values) == self.searchValue:
                    finalList.append(data)
                    flag = True
                    total += 1

                elif self.searchTerm == 'tags' or self.searchTerm == 'domain_names':
                    if keys == self.searchTerm and self.searchValue in values:
                        finalList.append(data)
                        flag = True
                        total += 1
                else:
                    flag = False
        
        for searchData in finalList:
            for key, val in searchData.items():
                print(key, ':', val)

        if flag == False and total == 0:
                print(' ')
                print("Searching ",searchFor, " for ",self.searchTerm," with a value of ", self.searchValue, "\nNo results found ")

    def displaySearchMethod(self):
        print("--------------------------------------------------")
        print("Search Users with")
        print("_id \n url \n external_id \n name \n alias \n created_at \n active \n verified \n shared \n locale \n timezone \n last_login_at \n email \n phone \n signature \n organization_id \n tags \n suspended \n role \n")
        
        print("--------------------------------------------------")
        print("Search Tickets with")
        print("_id \n url \n external_id \n created_at \n type \n subject \n description \n priority \n status \n submitter_id \n assignee_id \n organization_id \n tags \n has_incidents \n due_at \n via \n")
        
        print("--------------------------------------------------")
        print("Search Organizations with")
        print("_id \n url \n external_id \n name \n domain_names \n created_at \n details \n shared_tickets \n tags")

    def terminateProgram(self):
        exit()

    def callBySequence(self):
        self.displayIntro()
        self.displayMenu()
        self.selectMainMenu()


zendeskObj = ZendeskSearch()
while True:
    zendeskObj.callBySequence()
