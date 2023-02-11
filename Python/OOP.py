Autor = 'MAX WÖLFEL'
###########################################    OOP     #######################################################
#   Wichtig !!! Die __init__ funktion dient zum Instanzieren von mitgegeben Werten / direkte ausführungen der Klasse ohne Methoden
#   Die __init__ muss nicht wie eine MEthode spezifisch aufgerufen werden
#Methoden innerhalb müssen entweder extra aufgerufen werden oder vererbt werden
class Versuch1():
    print 'Vor der __init__'
    def __init__(self):
        print 'In der Init'             #wird direkt ausgeführt

    def Methode1 (self):
        print 'In der Methode 1'        #wird nicht angezeigt
Versuch1()




###########################################     Vererbung       #######################################################


class Vererbungs_klasse():                      #diese Klasse dient als überklasse von der die Beispielklasse Erben soll
    def huhu (self):                            #Dabei werden nur Funktionen weitergegeben
        Wert1=16
        return Wert1                                #der Return Befehl muss in jeder Methode enthalten sein


class Erbende_Klasse (Vererbungs_klasse):       #Erbende Klasse
    def __init__(self):                         #initialisierung der Variablen
        print 'klassische Vererbung: '+ str (self.huhu())
                                                #anstelle von Vererbung_klasse.huhu() ist es nur nochnötig self.huhu zu schreiben,
                                                #das die Parameter der Überklasse mitgeliefert wurden

Erbende_Klasse()                                #Klassenaufruf


############################     Mitgabe von Werten in eine Klasse       ###############################################

class Werte_bekommen ():                        #Übertragene Werte kommen nicht in den Vererbungsabschnitt
    def __init__(self, Wert_1,Wert_2):          #übertragene Werte werden über die instanzierung ausgewertet
        Wert1 = Wert_1
        Wert2 = Wert_2
        Beispiel = Wert1 + Wert2
        print 'Mitgabe von Werten: ' + str (Beispiel)

Wert_1 = 16
Wert_2 = 18
Werte_bekommen(Wert_1,Wert_2)                   #Müssen bei dem Klassenaufruf mitgegeben werden.




############################     Mitgabe von Werten innerhalb der Vererbung      #######################################

class Oberklasse ():
    def O_K (self,Wert_UK1):
        WERT_UK = Wert_UK1
        Wert_OK=13
        Summe = Wert_OK + WERT_UK
        return Summe

class Unterklasse (Oberklasse):                                         #Klasse wird aufgerufen und erbt von der Oberklasse
    def __init__(self):
        Wert_UK=13

        Rueckgabe=self.O_K(Wert_UK)                                     #Aufruf der Methode in der Ober Klasse Wert_UK wird mitgegeben
                                                                        #Die Summe wird als Rückgabe Wert an die Unterklasse zurück gegeben
        print ('Vererbte Werte Übertragung:     '+str (Rueckgabe))
Referenz= Unterklasse()


############################     Methodenaufruf einer Klasse von außen       #######################################

class Aufruf_von_aussen ():
    def Aufruf (self):
        print ('Aufruf von aussen: ich wurde Aufgerufen')

    def Methode2 (self):
        print ('Ich darf nicht aufgerufen werden ')
Instanz = Aufruf_von_aussen()                       #Um Klassen von aussen aufzurufen muss zu erst eine Instanz geschaffen werden
Instanz.Aufruf()                                   #Mit der instanz ist es nun möglich die einzelnen Methoden aufzurufen



##########################################     Mehrfach Vererbung     ##################################################



class OB_1 ():                                      #Oberklasse 1 deklariert den Wert 1
    def Wert_1(self):
        Wert_1 = 1
        return Wert_1

class OB_2 (OB_1):                                  #Oberklasse 2 deklariert den Wert 2
    def Wert_2 (self):
        Wert_2 = 2
        return Wert_2

class Summe (OB_2):                                 #Die Summen Klasse erbt von der Oberklasse 2 bekommt aber dennoch die Werte von der Oberklasse 1 mit
    def __init__(self):
        Summe = self.Wert_1() + self.Wert_2()
        print  'Mehrfach Vererbung: '+str(Summe)
Summe()


###################################### Parallele Vererung (Kein Fachbergriff )########################################

class ob_1 ():
    def Wert_1(self):
        Wert_1 = 1
        return Wert_1

class ob_2 ():
    def Wert_2(self):
        Wert_2 = 2
        return Wert_2

class summe2 (ob_1,ob_2):                               #anstelle von einer doppelvererbung kann man auch "Parallel" vererben

    def __init__(self):
        Summe = self.Wert_1() + self.Wert_2()
        print  'Parallele Vererbung: '+str(Summe)

summe2()