# Entmoot of T.A. 3019 # 

This is my entry for [NaNoGenMo 2014](https://github.com/dariusk/NaNoGenMo-2014). It generates a transcript of the Entmoot (meeting of the Ents) as described in The Lord of The Rings ([Treebeard](http://tolkiengateway.net/wiki/Treebeard_(chapter))). 

The basic method is to create a skeleton of the Entmoot, which can be found in the file "entmoot.json". There, chapters are defined, as well as sentences in each chapter. Each sentence has a side note which is published at the beginning of the sentence. And each sentence has an English form; the words of which are used to “translate” into Entish, using my interpretation of the phonotactics of Entish.

Entish, of course, is the language of the Ents. It's said to be long-winded and musical. The only
authentic Entish we know is part of the name for 'hill,' which is
<i>a lalla lalla rumba kamanda lindor bur&uacute;m&euml;</i>. Given this small
corpus, I think that Entish words are normally accented on the first syllable (and so
accent is marked only when it's not on the first syallable), and the syllables have
follow a V, CV, or CVL structure (where V is vowel, C is consonant, and L are the liquids
and nasals). I think the consonants are probably 'b','d','g','p','t','k','l','r','m' and 'n';
with 'l' and 'r' the only liquids and 'm', 'n' and 'ng' the only nasals. I'm sure the vowels take their 'European' values, and an 'umlaut' just emphasizes that the vowel be pronounced. Reduplication is also prevalent. I've also pretended there is a heavy-breath 'r' indicated by 'hr'. This shows up in
some of Treebeard's dialog in the book.
    
See also [Entish: Say nothing that isn't worth saying](http://www.uib.no/People/hnohf/entish.htm).

I used the wonderful online LaTex publisher [WriteLaTex](https://www.writelatex.com) to generate a PDF file from the LaTex file created by this program.

To generate your own version (which should be identical to what is found in results/entmoot.latex), run:

    > cd src
    > python3 entmoot.py 
    
Data will go to the standard output, so to save the file, do:

    > python3 entmoot.py > some_file.latex
    
