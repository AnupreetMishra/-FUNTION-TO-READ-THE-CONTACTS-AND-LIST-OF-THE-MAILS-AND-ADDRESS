#FUNTION TO READ THE CONTACTS FROM THE GIVEN CONTACT FILE AND RETURN a
#list of the mails and address
def get_contacts(filename):
     names = []
     emails = []
     with open(filename,mode='r', encoding='utf-8') as contact_file:
        for a_contact in contact_file:
             name.append(a_contact.split()[0])
             emails.append(a_contact.split()[1])
     return names, emails            