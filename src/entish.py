#!/usr/local/bin/python

import random
import string
import math
import cgi
import re

class EntishGenerator(object):

    def __init__(self,seed=None,name=None):
        self.__name = name
        if name:
            self.__name = name.lower()
        self.__ra = random.Random()
        if seed:
            self.__ra.seed(seed)
        elif name:
            self.__ra.seed(hash(name))

    def get_ra(self):
        return self.__ra
    def set_ra(self,ra):
        self._ra = ra
    ra=property(get_ra,set_ra)

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self._name = name
    name=property(get_name,set_name)


    def random_syllable_pattern(self):
        n = self.ra.random()
        if n <= .05:
            return ['V']
        elif n <= .75:
            return ['C','V']
        else:
            return ['C','V','L']
        
    def random_syllable(self):
        str = ""
        syl = self.random_syllable_pattern()
        for letter in syl:
            if letter is 'V':
                str = str + self.random_vowel()
            elif letter is 'C':
                str = str + self.random_consonant()
            elif letter is 'L':
                str = str + self.random_non_stop()
            else:
                error("Bad syllable specification: " + letter)
        return str

    def random_vowel(self):
        return self.ra.choice(['a','a','a','a','a','e','e','e','i','i','o','o','u'])

    def random_consonant(self):
        return self.ra.choice(['b','d','g','p','t','k','l','r','m','n','hr'])

    def random_non_stop(self):
        return self.ra.choice(['l','r','m','n','ng'])

    def prob_of_reduplication(self):
        return .20

    def prob_of_reaccent(self):
        return .20

    def accent(self,ch):
        if ch is "a":
            return "á"
        elif ch is "e":
            return "é"
        elif ch is "i":
            return "í"
        elif ch is "o":
            return "ó"
        elif ch is "u":
            return "ú"
        else:
            return ch
        

    def umlaut(self,ch):
        if ch is "a":
            return "ä"
        elif ch is "e":
            return "ë"
        elif ch is "i":
            return "ï"
        elif ch is "o":
            return "ö"
        elif ch is "u":
            return "ü"
        else:
            return ch
    
    def repair_lexeme(self,lex):
        nlex = lex[0:]
        # maybe put an accent
        syl_count = nlex.count(":")
        if (syl_count>=2) and (self.ra.random() <= self.prob_of_reaccent()):
            which_syl = self.ra.randint(1,syl_count-1)
            scnt = 0
            for i in range(1,len(nlex)):
                j = len(nlex)-i
                ch = nlex[j]
                if ch is ':':
                    scnt = scnt + 1
                elif ("aeiou".count(ch)>0): # ie we have the vowel!
                    nlex = nlex[0:j-1] + self.accent(ch) + nlex[j+1:]
                    break
        # final 'e' needing umlaut
        if re.search("[aeiou]:\w?e:$",nlex):
            nlex = nlex[0:-3] + "ë" + ":"

        # umlauts on double vowels
        p = re.compile("[aeiou]:[aeiou]")
        it = p.finditer(nlex)
        matches = []
        for match in it:
            matches.append(match.end())
        str = ""
        i = 0
        for m in matches:
            str = str + nlex[i:m-1]
            um = self.umlaut(nlex[m-1])
            str = str + um
            i = m + 1
        str = str + nlex[i:]
        nlex = str
        
        # remove syllable marks
        str = ""
        for ch in nlex:
            if ch is not ":":
                str = str + ch
        # return it
        
        return str
            

        
    def random_lexeme(self,last=None):
        if last and (self.ra.random() <= self.prob_of_reduplication()):
            return last
        else:
            str = ""
            for i in range(0,self.syllable_count()):
                str = str + self.random_syllable() + ":"
            return self.repair_lexeme(str)

    def syllable_count(self):
        n = self.ra.random()
        if n <= .05:
            return 1
        elif n <= .52:
            return 2
        elif n <= .75:
            return 3
        else:
            return self.ra.randint(4,7)

    def lexeme_count(self):
        return self.ra.randint(300,500)
    
    def generate_entish(self):
        n = self.lexeme_count()
        str = ""
        old_lexeme = None
        for i in range(0,(n-1)):
            new_lexeme = self.random_lexeme(last=old_lexeme)
            str = str + new_lexeme + " "
            old_lexeme = new_lexeme
        str = str + self.random_lexeme(last=old_lexeme)
        if self.name == "hill":
            str = "a lalla lalla rumba kamanda lindor burámë " + str 
        elif self.name in ['fangorn','finglas','fimbrethil','fladrif','bregalad', 'peregrin','meriadoc', 'hobbits', 'hroom']:
            str = self.name.capitalize() + ' ' + str
        # str = str.replace(" ","-")
        return str
                
    
def display_html():
    form = cgi.FieldStorage()
    print("Content-Type: text/html")     # HTML is following
    print()                               # blank line, end of headers 

    print("<HTML><HEAD>")
    print("<TITLE>What is your Entish name?</TITLE>")
    print('<link rel="stylesheet" type="text/css" href="/entishname/entish.css" title="default">')
    print("</HEAD><BODY>")
    print('<IMG SRC="http://www.entish.org/images/entwash.jpg" WIDTH=320 HEIGHT=240 ALT="The Entwash" ALIGN="RIGHT">')
    print("<H1>What is your Entish name?</H2>")
    print('<form action="http://www.entish.org/cgi/entish.pl"><p>What is your name? <input type="text" name="name" ')
    if ("name" in form):
        vstring = 'value="' + form["name"].value + '"'
        print(vstring)
    print('/></p></form>')
    if ("name" in form):
        nn = string.strip(form["name"].value)
        print("<H2>Here's your Entish name!</H2>")
        print("<P>")
        print(EntishGenerator(name=nn).generate_entish())
        print("</P>")
    print("<H2>About Entish</H2>")
    print("""
    <p>Entish is the language of the Ents. It's said to be long-winded and musical. The only
    authentic Entish we know is part of the name for 'hill,' which is
    <i>a lalla lalla rumba kamanda lindor bur&uacute;m&euml;</i>. Given this small
    corpus, I think that Entish words are normally accented on the first syllable (and so
    accent is marked only when it's not on the first syallable), and the syllables have
    follow a V, CV, or CVL structure (where V is vowel, C is consonant, and L are the liquids
    and nasals). I think the consonants are probably 'b','d','g','p','t','k','l','r','m' and 'n';
    with 'l' and 'r' the only liquids and 'm' and 'n' the only nasals.
    I'm sure the vowels take their 'European' values, and an 'umlaut' just emphasizes that
    the vowel be pronounced. Reduplication is also prevalent.
    See also: 
     <a href="http://www.uib.no/People/hnohf/entish.htm">Entish: Say nothing that isn't worth saying</a>.
    """)
    print("</BODY></HTML>")


        
# display_html()
