import pickle
#MMM   MMM MMMMMMMM MMMMMMMM MMMMMMMM MMMMMMMM
#MMM   MMM MMM  MMM MMMMMMMM MMMMMMMM MMM  MMM
#MMMMMMMMM MMMMMMMM MMM  MMM MMM  MMM MMMMMMMM
#MMMMMMMMM MMMMMMMM MMM  MMM MMM  MMM MMMMMMMM
#MMM   MMM MMM  MMM MMM  MMM MMM  MMM MMM  MMM
#MMM   MMM MMM  MMM MMM  MMM MMM  MMM MMM  MMM
#See siin on Hannale
#Hanna, sulle vajalikud käsud:
# - Saadavat sõnastikku saad järgmiselt kasutada:
# -- sõnastik[kuupäev(str)][sündmuse nimi(str)][andme index]
# - timeplan.set(date, event, startTime, endTime, desc)
# -- selle käsuga talletab sündmusi ja muid sellised
# - timeplan.get()
# -- selle käsuga võtad andmebaasist sündmusi
# -- Tagastatud nimekirja saab kasutada järgmiselt (kuupäeva formaat on MM/DD/YY):
# --- eventsList = timeplan.get()
# --- events = events[date]
# --- event = events[date][eventName]
# --- eventStart = event[0]
# --- eventEnd = event[1]
# --- eventDescription = event[2]
class timeplan:
    def set(date, event, startTime, endTime, desc=''):
        finalDump = {}
        try:
            f = open('timeplan.pickle', 'rb')
            f.close()
        except:
            f = open('timeplan.pickle', 'x')
            f.close()
        with open('timeplan.pickle', 'rb') as timeplanData:
            #Check if datafile existed before
            try:
                data = pickle.load(timeplanData)
            except:
                data = {}

            #Check if any events on that date already
            try:
                dateEvents = data[date]
            except:
                dateEvents = {}

            #Create/edit the event on that date
            dateEvents[event] = [startTime, endTime, desc]

            #Add the event to that date
            data[date] = dateEvents

            #Saves the event to the file
            finalDump = data
        with open('timeplan.pickle', 'wb') as timeplanData:
            pickle.dump(finalDump, timeplanData)
    def get():
        with open ('timeplan.pickle', 'rb') as timeplanData:
            loadedData = pickle.load(timeplanData)
            return loadedData
#See osa Kaalebile
# käsud:
# - notes.set(notes)
# -- Salvestab parajasti kirjutatud asjad ära
# - notes.get()
# -- saad salvestatud märkmed
class notes:
    def set(notes):
        with open('notes.pickle', 'wb') as notesData:
            pickle.dump(notes, notesData)
    def get():
        with open('notes.pickle', 'rb') as notesData:
            loadedData = pickle.load(notesData)
            return loadedData
