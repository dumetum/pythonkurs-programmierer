
class Knoten:

    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.naechster_knoten = None


class VerketteteListe:

    def __init__(self):
        self.__start_knoten = None

    def einfuegen(self, inhalt):
        neuer_knoten = Knoten(inhalt)
        if not self.__start_knoten:
            self.__start_knoten = neuer_knoten
            return
        knoten = self.__start_knoten
        while knoten.naechster_knoten:
            knoten = knoten.naechster_knoten
        # Knoten zeigt jetzt auf den letzten Knoten der Liste. Hier wird der neue Knoten eingefuegt
        knoten.naechster_knoten = neuer_knoten

    def __str__(self):
        knoten = self.__start_knoten
        ausgabe_string = ''
        while knoten:
            ausgabe_string += (str(knoten.inhalt) + " - ")
            knoten = knoten.naechster_knoten
        return ausgabe_string

    def loeschen(inhalt):
        pass

    def enthaelt(inhalt):
        pass

l = VerketteteListe()
l.einfuegen(1)
l.einfuegen(2)
print(str(l))

