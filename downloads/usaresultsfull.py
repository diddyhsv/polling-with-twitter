import sys
sys.path.append("..")
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import pickle
from sortlocation import sortloc

#this uses sets to count the number of users that tweeted pro trump/biden, without any weighting regarding sex or ethnicity
#calculates based on districts, and for full state



trumpmo, bidenmo = set(), set() #trumpmo1, bidenmo1, trumpmo2, bidenmo2, trumpmo3, bidenmo3, trumpmo4, bidenmo4, trumpmo5, bidenmo5, trumpmo6, bidenmo6, trumpmo7, bidenmo7, trumpmo8, bidenmo8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpco, bidenco = set(), set() #trumpco1, bidenco1, trumpco2, bidenco2, trumpco3, bidenco3, trumpco4, bidenco4, trumpco5, bidenco5, trumpco6, bidenco6, trumpco7, bidenco7 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpsc, bidensc = set(), set() #trumpsc1, bidensc1, trumpsc2, bidensc2, trumpsc3, bidensc3, trumpsc4, bidensc4, trumpsc5, bidensc5, trumpsc6, bidensc6, trumpsc7, bidensc7 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpmn, bidenmn = set(), set() #trumpmn1, bidenmn1, trumpmn2, bidenmn2, trumpmn3, bidenmn3, trumpmn4, bidenmn4, trumpmn5, bidenmn5, trumpmn6, bidenmn6, trumpmn7, bidenmn7, trumpmn8, bidenmn8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpin, bidenin = set(), set() #trumpin1, bidenin1, trumpin2, bidenin2, trumpin3, bidenin3, trumpin4, bidenin4, trumpin5, bidenin5, trumpin6, bidenin6, trumpin7, bidenin7, trumpin8, bidenin8, trumpin9, bidenin9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpmd, bidenmd = set(), set() #trumpmd1, bidenmd1, trumpmd2, bidenmd2, trumpmd3, bidenmd3, trumpmd4, bidenmd4, trumpmd5, bidenmd5, trumpmd6, bidenmd6, trumpmd7, bidenmd7, trumpmd8, bidenmd8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpsd, bidensd = set(), set() #trumpsd1, bidensd1 = set(), set(), set(), set()
trumpvt, bidenvt = set(), set() #trumpvt1, bidenvt1 = set(), set(), set(), set()
trumpnd, bidennd = set(), set() #trumpnd1, bidennd1 = set(), set(), set(), set()
trumpde, bidende = set(), set() #trumpde1, bidende1 = set(), set(), set(), set()
trumpmt, bidenmt = set(), set() #trumpmt1, bidenmt1 = set(), set(), set(), set()
trumpne, bidenne = set(), set() #trumpne1, bidenne1, trumpne2, bidenne2, trumpne3, bidenne3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpmi, bidenmi = set(), set() #trumpmi1, bidenmi1, trumpmi2, bidenmi2, trumpmi3, bidenmi3, trumpmi4, bidenmi4, trumpmi5, bidenmi5, trumpmi6, bidenmi6, trumpmi7, bidenmi7, trumpmi8, bidenmi8, trumpmi9, bidenmi9, trumpmi10, bidenmi10, trumpmi11, bidenmi11, trumpmi12, bidenmi12, trumpmi13, bidenmi13, trumpmi14, bidenmi14 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpma, bidenma = set(), set() #trumpma1, bidenma1, trumpma2, bidenma2, trumpma3, bidenma3, trumpma4, bidenma4, trumpma5, bidenma5, trumpma6, bidenma6, trumpma7, bidenma7, trumpma8, bidenma8, trumpma9, bidenma9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpva, bidenva = set(), set() #trumpva1, bidenva1, trumpva2, bidenva2, trumpva3, bidenva3, trumpva4, bidenva4, trumpva5, bidenva5, trumpva6, bidenva6, trumpva7, bidenva7, trumpva8, bidenva8, trumpva9, bidenva9, trumpva10, bidenva10, trumpva11, bidenva11 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpme, bidenme = set(), set() #trumpme1, bidenme1, trumpme2, bidenme2 = set(), set(), set(), set(), set(), set()
trumpid, bidenid = set(), set() #trumpid1, bidenid1, trumpid2, bidenid2 = set(), set(), set(), set(), set(), set()
trumpwi, bidenwi = set(), set() #trumpwi1, bidenwi1, trumpwi2, bidenwi2, trumpwi3, bidenwi3, trumpwi4, bidenwi4, trumpwi5, bidenwi5, trumpwi6, bidenwi6, trumpwi7, bidenwi7, trumpwi8, bidenwi8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpwv, bidenwv = set(), set() #trumpwv1, bidenwv1, trumpwv2, bidenwv2, trumpwv3, bidenwv3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpia, bidenia = set(), set() #trumpia1, bidenia1, trumpia2, bidenia2, trumpia3, bidenia3, trumpia4, bidenia4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpms, bidenms = set(), set() #trumpms1, bidenms1, trumpms2, bidenms2, trumpms3, bidenms3, trumpms4, bidenms4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumphi, bidenhi = set(), set() #trumphi1, bidenhi1, trumphi2, bidenhi2 = set(), set(), set(), set(), set(), set()
trumpri, bidenri = set(), set() #trumpri1, bidenri1, trumpri2, bidenri2 = set(), set(), set(), set(), set(), set()
trumpwa, bidenwa = set(), set() #trumpwa1, bidenwa1, trumpwa2, bidenwa2, trumpwa3, bidenwa3, trumpwa4, bidenwa4, trumpwa5, bidenwa5, trumpwa6, bidenwa6, trumpwa7, bidenwa7, trumpwa8, bidenwa8, trumpwa9, bidenwa9, trumpwa10, bidenwa10 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpfl, bidenfl = set(), set() #trumpfl1, bidenfl1, trumpfl2, bidenfl2, trumpfl3, bidenfl3, trumpfl4, bidenfl4, trumpfl5, bidenfl5, trumpfl6, bidenfl6, trumpfl7, bidenfl7, trumpfl8, bidenfl8, trumpfl9, bidenfl9, trumpfl10, bidenfl10, trumpfl11, bidenfl11, trumpfl12, bidenfl12, trumpfl13, bidenfl13, trumpfl14, bidenfl14, trumpfl15, bidenfl15, trumpfl16, bidenfl16, trumpfl17, bidenfl17, trumpfl18, bidenfl18, trumpfl19, bidenfl19, trumpfl20, bidenfl20, trumpfl21, bidenfl21, trumpfl22, bidenfl22, trumpfl23, bidenfl23, trumpfl24, bidenfl24, trumpfl25, bidenfl25, trumpfl26, bidenfl26, trumpfl27, bidenfl27 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpal, bidenal = set(), set() #trumpal1, bidenal1, trumpal2, bidenal2, trumpal3, bidenal3, trumpal4, bidenal4, trumpal5, bidenal5, trumpal6, bidenal6, trumpal7, bidenal7 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpil, bidenil = set(), set() #trumpil1, bidenil1, trumpil2, bidenil2, trumpil3, bidenil3, trumpil4, bidenil4, trumpil5, bidenil5, trumpil6, bidenil6, trumpil7, bidenil7, trumpil8, bidenil8, trumpil9, bidenil9, trumpil10, bidenil10, trumpil11, bidenil11, trumpil12, bidenil12, trumpil13, bidenil13, trumpil14, bidenil14, trumpil15, bidenil15, trumpil16, bidenil16, trumpil17, bidenil17, trumpil18, bidenil18 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpca, bidenca = set(), set() #trumpca1, bidenca1, trumpca2, bidenca2, trumpca3, bidenca3, trumpca4, bidenca4, trumpca5, bidenca5, trumpca6, bidenca6, trumpca7, bidenca7, trumpca8, bidenca8, trumpca9, bidenca9, trumpca10, bidenca10, trumpca11, bidenca11, trumpca12, bidenca12, trumpca13, bidenca13, trumpca14, bidenca14, trumpca15, bidenca15, trumpca16, bidenca16, trumpca17, bidenca17, trumpca18, bidenca18, trumpca19, bidenca19, trumpca20, bidenca20, trumpca21, bidenca21, trumpca22, bidenca22, trumpca23, bidenca23, trumpca24, bidenca24, trumpca25, bidenca25, trumpca26, bidenca26, trumpca27, bidenca27, trumpca28, bidenca28, trumpca29, bidenca29, trumpca30, bidenca30, trumpca31, bidenca31, trumpca32, bidenca32, trumpca33, bidenca33, trumpca34, bidenca34, trumpca35, bidenca35, trumpca36, bidenca36, trumpca37, bidenca37, trumpca38, bidenca38, trumpca39, bidenca39, trumpca40, bidenca40, trumpca41, bidenca41, trumpca42, bidenca42, trumpca43, bidenca43, trumpca44, bidenca44, trumpca45, bidenca45, trumpca46, bidenca46, trumpca47, bidenca47, trumpca48, bidenca48, trumpca49, bidenca49, trumpca50, bidenca50, trumpca51, bidenca51, trumpca52, bidenca52, trumpca53, bidenca53 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpks, bidenks = set(), set() #trumpks1, bidenks1, trumpks2, bidenks2, trumpks3, bidenks3, trumpks4, bidenks4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpga, bidenga = set(), set() #trumpga1, bidenga1, trumpga2, bidenga2, trumpga3, bidenga3, trumpga4, bidenga4, trumpga5, bidenga5, trumpga6, bidenga6, trumpga7, bidenga7, trumpga8, bidenga8, trumpga9, bidenga9, trumpga10, bidenga10, trumpga11, bidenga11, trumpga12, bidenga12, trumpga13, bidenga13, trumpga14, bidenga14 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpaz, bidenaz = set(), set() #trumpaz1, bidenaz1, trumpaz2, bidenaz2, trumpaz3, bidenaz3, trumpaz4, bidenaz4, trumpaz5, bidenaz5, trumpaz6, bidenaz6, trumpaz7, bidenaz7, trumpaz8, bidenaz8, trumpaz9, bidenaz9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpak, bidenak = set(), set() #trumpak1, bidenak1 = set(), set(), set(), set()
trumpar, bidenar = set(), set() #trumpar1, bidenar1, trumpar2, bidenar2, trumpar3, bidenar3, trumpar4, bidenar4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnj, bidennj = set(), set() #trumpnj1, bidennj1, trumpnj2, bidennj2, trumpnj3, bidennj3, trumpnj4, bidennj4, trumpnj5, bidennj5, trumpnj6, bidennj6, trumpnj7, bidennj7, trumpnj8, bidennj8, trumpnj9, bidennj9, trumpnj10, bidennj10, trumpnj11, bidennj11, trumpnj12, bidennj12 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnv, bidennv = set(), set() #trumpnv1, bidennv1, trumpnv2, bidennv2, trumpnv3, bidennv3, trumpnv4, bidennv4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnh, bidennh = set(), set() #trumpnh1, bidennh1, trumpnh2, bidennh2 = set(), set(), set(), set(), set(), set()
trumpnc, bidennc = set(), set() #trumpnc1, bidennc1, trumpnc2, bidennc2, trumpnc3, bidennc3, trumpnc4, bidennc4, trumpnc5, bidennc5, trumpnc6, bidennc6, trumpnc7, bidennc7, trumpnc8, bidennc8, trumpnc9, bidennc9, trumpnc10, bidennc10, trumpnc11, bidennc11, trumpnc12, bidennc12, trumpnc13, bidennc13 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumptx, bidentx = set(), set() #trumptx1, bidentx1, trumptx2, bidentx2, trumptx3, bidentx3, trumptx4, bidentx4, trumptx5, bidentx5, trumptx6, bidentx6, trumptx7, bidentx7, trumptx8, bidentx8, trumptx9, bidentx9, trumptx10, bidentx10, trumptx11, bidentx11, trumptx12, bidentx12, trumptx13, bidentx13, trumptx14, bidentx14, trumptx15, bidentx15, trumptx16, bidentx16, trumptx17, bidentx17, trumptx18, bidentx18, trumptx19, bidentx19, trumptx20, bidentx20, trumptx21, bidentx21, trumptx22, bidentx22, trumptx23, bidentx23, trumptx24, bidentx24, trumptx25, bidentx25, trumptx26, bidentx26, trumptx27, bidentx27, trumptx28, bidentx28, trumptx29, bidentx29, trumptx30, bidentx30, trumptx31, bidentx31, trumptx32, bidentx32, trumptx33, bidentx33, trumptx34, bidentx34, trumptx35, bidentx35, trumptx36, bidentx36 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumptn, bidentn = set(), set() #trumptn1, bidentn1, trumptn2, bidentn2, trumptn3, bidentn3, trumptn4, bidentn4, trumptn5, bidentn5, trumptn6, bidentn6, trumptn7, bidentn7, trumptn8, bidentn8, trumptn9, bidentn9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnm, bidennm = set(), set() #trumpnm1, bidennm1, trumpnm2, bidennm2, trumpnm3, bidennm3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpny, bidenny = set(), set() #trumpny1, bidenny1, trumpny2, bidenny2, trumpny3, bidenny3, trumpny4, bidenny4, trumpny5, bidenny5, trumpny6, bidenny6, trumpny7, bidenny7, trumpny8, bidenny8, trumpny9, bidenny9, trumpny10, bidenny10, trumpny11, bidenny11, trumpny12, bidenny12, trumpny13, bidenny13, trumpny14, bidenny14, trumpny15, bidenny15, trumpny16, bidenny16, trumpny17, bidenny17, trumpny18, bidenny18, trumpny19, bidenny19, trumpny20, bidenny20, trumpny21, bidenny21, trumpny22, bidenny22, trumpny23, bidenny23, trumpny24, bidenny24, trumpny25, bidenny25, trumpny26, bidenny26, trumpny27, bidenny27 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpwy, bidenwy = set(), set() #trumpwy1, bidenwy1 = set(), set(), set(), set()
trumppa, bidenpa = set(), set() #trumppa1, bidenpa1, trumppa2, bidenpa2, trumppa3, bidenpa3, trumppa4, bidenpa4, trumppa5, bidenpa5, trumppa6, bidenpa6, trumppa7, bidenpa7, trumppa8, bidenpa8, trumppa9, bidenpa9, trumppa10, bidenpa10, trumppa11, bidenpa11, trumppa12, bidenpa12, trumppa13, bidenpa13, trumppa14, bidenpa14, trumppa15, bidenpa15, trumppa16, bidenpa16, trumppa17, bidenpa17, trumppa18, bidenpa18 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpct, bidenct = set(), set() #trumpct1, bidenct1, trumpct2, bidenct2, trumpct3, bidenct3, trumpct4, bidenct4, trumpct5, bidenct5 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpky, bidenky = set(), set() #trumpky1, bidenky1, trumpky2, bidenky2, trumpky3, bidenky3, trumpky4, bidenky4, trumpky5, bidenky5, trumpky6, bidenky6 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpla, bidenla = set(), set() #trumpla1, bidenla1, trumpla2, bidenla2, trumpla3, bidenla3, trumpla4, bidenla4, trumpla5, bidenla5, trumpla6, bidenla6 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpok, bidenok = set(), set() #trumpok1, bidenok1, trumpok2, bidenok2, trumpok3, bidenok3, trumpok4, bidenok4, trumpok5, bidenok5 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumput, bidenut = set(), set() #trumput1, bidenut1, trumput2, bidenut2, trumput3, bidenut3, trumput4, bidenut4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpoh, bidenoh = set(), set() #trumpoh1, bidenoh1, trumpoh2, bidenoh2, trumpoh3, bidenoh3, trumpoh4, bidenoh4, trumpoh5, bidenoh5, trumpoh6, bidenoh6, trumpoh7, bidenoh7, trumpoh8, bidenoh8, trumpoh9, bidenoh9, trumpoh10, bidenoh10, trumpoh11, bidenoh11, trumpoh12, bidenoh12, trumpoh13, bidenoh13, trumpoh14, bidenoh14, trumpoh15, bidenoh15, trumpoh16, bidenoh16 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpor, bidenor = set(), set() #trumpor1, bidenor1, trumpor2, bidenor2, trumpor3, bidenor3, trumpor4, bidenor4, trumpor5, bidenor5 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()

trumpmo, bidenmo, trumpmo1, bidenmo1, trumpmo2, bidenmo2, trumpmo3, bidenmo3, trumpmo4, bidenmo4, trumpmo5, bidenmo5, trumpmo6, bidenmo6, trumpmo7, bidenmo7, trumpmo8, bidenmo8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpco, bidenco, trumpco1, bidenco1, trumpco2, bidenco2, trumpco3, bidenco3, trumpco4, bidenco4, trumpco5, bidenco5, trumpco6, bidenco6, trumpco7, bidenco7 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpsc, bidensc, trumpsc1, bidensc1, trumpsc2, bidensc2, trumpsc3, bidensc3, trumpsc4, bidensc4, trumpsc5, bidensc5, trumpsc6, bidensc6, trumpsc7, bidensc7 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpmn, bidenmn, trumpmn1, bidenmn1, trumpmn2, bidenmn2, trumpmn3, bidenmn3, trumpmn4, bidenmn4, trumpmn5, bidenmn5, trumpmn6, bidenmn6, trumpmn7, bidenmn7, trumpmn8, bidenmn8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpin, bidenin, trumpin1, bidenin1, trumpin2, bidenin2, trumpin3, bidenin3, trumpin4, bidenin4, trumpin5, bidenin5, trumpin6, bidenin6, trumpin7, bidenin7, trumpin8, bidenin8, trumpin9, bidenin9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpmd, bidenmd, trumpmd1, bidenmd1, trumpmd2, bidenmd2, trumpmd3, bidenmd3, trumpmd4, bidenmd4, trumpmd5, bidenmd5, trumpmd6, bidenmd6, trumpmd7, bidenmd7, trumpmd8, bidenmd8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpsd, bidensd, trumpsd1, bidensd1 = set(), set(), set(), set()
trumpvt, bidenvt, trumpvt1, bidenvt1 = set(), set(), set(), set()
trumpnd, bidennd, trumpnd1, bidennd1 = set(), set(), set(), set()
trumpde, bidende, trumpde1, bidende1 = set(), set(), set(), set()
trumpmt, bidenmt, trumpmt1, bidenmt1 = set(), set(), set(), set()
trumpne, bidenne, trumpne1, bidenne1, trumpne2, bidenne2, trumpne3, bidenne3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpmi, bidenmi, trumpmi1, bidenmi1, trumpmi2, bidenmi2, trumpmi3, bidenmi3, trumpmi4, bidenmi4, trumpmi5, bidenmi5, trumpmi6, bidenmi6, trumpmi7, bidenmi7, trumpmi8, bidenmi8, trumpmi9, bidenmi9, trumpmi10, bidenmi10, trumpmi11, bidenmi11, trumpmi12, bidenmi12, trumpmi13, bidenmi13, trumpmi14, bidenmi14 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpma, bidenma, trumpma1, bidenma1, trumpma2, bidenma2, trumpma3, bidenma3, trumpma4, bidenma4, trumpma5, bidenma5, trumpma6, bidenma6, trumpma7, bidenma7, trumpma8, bidenma8, trumpma9, bidenma9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpva, bidenva, trumpva1, bidenva1, trumpva2, bidenva2, trumpva3, bidenva3, trumpva4, bidenva4, trumpva5, bidenva5, trumpva6, bidenva6, trumpva7, bidenva7, trumpva8, bidenva8, trumpva9, bidenva9, trumpva10, bidenva10, trumpva11, bidenva11 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpme, bidenme, trumpme1, bidenme1, trumpme2, bidenme2 = set(), set(), set(), set(), set(), set()
trumpid, bidenid, trumpid1, bidenid1, trumpid2, bidenid2 = set(), set(), set(), set(), set(), set()
trumpwi, bidenwi, trumpwi1, bidenwi1, trumpwi2, bidenwi2, trumpwi3, bidenwi3, trumpwi4, bidenwi4, trumpwi5, bidenwi5, trumpwi6, bidenwi6, trumpwi7, bidenwi7, trumpwi8, bidenwi8 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpwv, bidenwv, trumpwv1, bidenwv1, trumpwv2, bidenwv2, trumpwv3, bidenwv3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpia, bidenia, trumpia1, bidenia1, trumpia2, bidenia2, trumpia3, bidenia3, trumpia4, bidenia4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpms, bidenms, trumpms1, bidenms1, trumpms2, bidenms2, trumpms3, bidenms3, trumpms4, bidenms4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumphi, bidenhi, trumphi1, bidenhi1, trumphi2, bidenhi2 = set(), set(), set(), set(), set(), set()
trumpri, bidenri, trumpri1, bidenri1, trumpri2, bidenri2 = set(), set(), set(), set(), set(), set()
trumpwa, bidenwa, trumpwa1, bidenwa1, trumpwa2, bidenwa2, trumpwa3, bidenwa3, trumpwa4, bidenwa4, trumpwa5, bidenwa5, trumpwa6, bidenwa6, trumpwa7, bidenwa7, trumpwa8, bidenwa8, trumpwa9, bidenwa9, trumpwa10, bidenwa10 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpfl, bidenfl, trumpfl1, bidenfl1, trumpfl2, bidenfl2, trumpfl3, bidenfl3, trumpfl4, bidenfl4, trumpfl5, bidenfl5, trumpfl6, bidenfl6, trumpfl7, bidenfl7, trumpfl8, bidenfl8, trumpfl9, bidenfl9, trumpfl10, bidenfl10, trumpfl11, bidenfl11, trumpfl12, bidenfl12, trumpfl13, bidenfl13, trumpfl14, bidenfl14, trumpfl15, bidenfl15, trumpfl16, bidenfl16, trumpfl17, bidenfl17, trumpfl18, bidenfl18, trumpfl19, bidenfl19, trumpfl20, bidenfl20, trumpfl21, bidenfl21, trumpfl22, bidenfl22, trumpfl23, bidenfl23, trumpfl24, bidenfl24, trumpfl25, bidenfl25, trumpfl26, bidenfl26, trumpfl27, bidenfl27 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpal, bidenal, trumpal1, bidenal1, trumpal2, bidenal2, trumpal3, bidenal3, trumpal4, bidenal4, trumpal5, bidenal5, trumpal6, bidenal6, trumpal7, bidenal7 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpil, bidenil, trumpil1, bidenil1, trumpil2, bidenil2, trumpil3, bidenil3, trumpil4, bidenil4, trumpil5, bidenil5, trumpil6, bidenil6, trumpil7, bidenil7, trumpil8, bidenil8, trumpil9, bidenil9, trumpil10, bidenil10, trumpil11, bidenil11, trumpil12, bidenil12, trumpil13, bidenil13, trumpil14, bidenil14, trumpil15, bidenil15, trumpil16, bidenil16, trumpil17, bidenil17, trumpil18, bidenil18 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpca, bidenca, trumpca1, bidenca1, trumpca2, bidenca2, trumpca3, bidenca3, trumpca4, bidenca4, trumpca5, bidenca5, trumpca6, bidenca6, trumpca7, bidenca7, trumpca8, bidenca8, trumpca9, bidenca9, trumpca10, bidenca10, trumpca11, bidenca11, trumpca12, bidenca12, trumpca13, bidenca13, trumpca14, bidenca14, trumpca15, bidenca15, trumpca16, bidenca16, trumpca17, bidenca17, trumpca18, bidenca18, trumpca19, bidenca19, trumpca20, bidenca20, trumpca21, bidenca21, trumpca22, bidenca22, trumpca23, bidenca23, trumpca24, bidenca24, trumpca25, bidenca25, trumpca26, bidenca26, trumpca27, bidenca27, trumpca28, bidenca28, trumpca29, bidenca29, trumpca30, bidenca30, trumpca31, bidenca31, trumpca32, bidenca32, trumpca33, bidenca33, trumpca34, bidenca34, trumpca35, bidenca35, trumpca36, bidenca36, trumpca37, bidenca37, trumpca38, bidenca38, trumpca39, bidenca39, trumpca40, bidenca40, trumpca41, bidenca41, trumpca42, bidenca42, trumpca43, bidenca43, trumpca44, bidenca44, trumpca45, bidenca45, trumpca46, bidenca46, trumpca47, bidenca47, trumpca48, bidenca48, trumpca49, bidenca49, trumpca50, bidenca50, trumpca51, bidenca51, trumpca52, bidenca52, trumpca53, bidenca53 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpks, bidenks, trumpks1, bidenks1, trumpks2, bidenks2, trumpks3, bidenks3, trumpks4, bidenks4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpga, bidenga, trumpga1, bidenga1, trumpga2, bidenga2, trumpga3, bidenga3, trumpga4, bidenga4, trumpga5, bidenga5, trumpga6, bidenga6, trumpga7, bidenga7, trumpga8, bidenga8, trumpga9, bidenga9, trumpga10, bidenga10, trumpga11, bidenga11, trumpga12, bidenga12, trumpga13, bidenga13, trumpga14, bidenga14 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpaz, bidenaz, trumpaz1, bidenaz1, trumpaz2, bidenaz2, trumpaz3, bidenaz3, trumpaz4, bidenaz4, trumpaz5, bidenaz5, trumpaz6, bidenaz6, trumpaz7, bidenaz7, trumpaz8, bidenaz8, trumpaz9, bidenaz9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpak, bidenak, trumpak1, bidenak1 = set(), set(), set(), set()
trumpar, bidenar, trumpar1, bidenar1, trumpar2, bidenar2, trumpar3, bidenar3, trumpar4, bidenar4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnj, bidennj, trumpnj1, bidennj1, trumpnj2, bidennj2, trumpnj3, bidennj3, trumpnj4, bidennj4, trumpnj5, bidennj5, trumpnj6, bidennj6, trumpnj7, bidennj7, trumpnj8, bidennj8, trumpnj9, bidennj9, trumpnj10, bidennj10, trumpnj11, bidennj11, trumpnj12, bidennj12 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnv, bidennv, trumpnv1, bidennv1, trumpnv2, bidennv2, trumpnv3, bidennv3, trumpnv4, bidennv4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnh, bidennh, trumpnh1, bidennh1, trumpnh2, bidennh2 = set(), set(), set(), set(), set(), set()
trumpnc, bidennc, trumpnc1, bidennc1, trumpnc2, bidennc2, trumpnc3, bidennc3, trumpnc4, bidennc4, trumpnc5, bidennc5, trumpnc6, bidennc6, trumpnc7, bidennc7, trumpnc8, bidennc8, trumpnc9, bidennc9, trumpnc10, bidennc10, trumpnc11, bidennc11, trumpnc12, bidennc12, trumpnc13, bidennc13 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumptx, bidentx, trumptx1, bidentx1, trumptx2, bidentx2, trumptx3, bidentx3, trumptx4, bidentx4, trumptx5, bidentx5, trumptx6, bidentx6, trumptx7, bidentx7, trumptx8, bidentx8, trumptx9, bidentx9, trumptx10, bidentx10, trumptx11, bidentx11, trumptx12, bidentx12, trumptx13, bidentx13, trumptx14, bidentx14, trumptx15, bidentx15, trumptx16, bidentx16, trumptx17, bidentx17, trumptx18, bidentx18, trumptx19, bidentx19, trumptx20, bidentx20, trumptx21, bidentx21, trumptx22, bidentx22, trumptx23, bidentx23, trumptx24, bidentx24, trumptx25, bidentx25, trumptx26, bidentx26, trumptx27, bidentx27, trumptx28, bidentx28, trumptx29, bidentx29, trumptx30, bidentx30, trumptx31, bidentx31, trumptx32, bidentx32, trumptx33, bidentx33, trumptx34, bidentx34, trumptx35, bidentx35, trumptx36, bidentx36 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumptn, bidentn, trumptn1, bidentn1, trumptn2, bidentn2, trumptn3, bidentn3, trumptn4, bidentn4, trumptn5, bidentn5, trumptn6, bidentn6, trumptn7, bidentn7, trumptn8, bidentn8, trumptn9, bidentn9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpnm, bidennm, trumpnm1, bidennm1, trumpnm2, bidennm2, trumpnm3, bidennm3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpny, bidenny, trumpny1, bidenny1, trumpny2, bidenny2, trumpny3, bidenny3, trumpny4, bidenny4, trumpny5, bidenny5, trumpny6, bidenny6, trumpny7, bidenny7, trumpny8, bidenny8, trumpny9, bidenny9, trumpny10, bidenny10, trumpny11, bidenny11, trumpny12, bidenny12, trumpny13, bidenny13, trumpny14, bidenny14, trumpny15, bidenny15, trumpny16, bidenny16, trumpny17, bidenny17, trumpny18, bidenny18, trumpny19, bidenny19, trumpny20, bidenny20, trumpny21, bidenny21, trumpny22, bidenny22, trumpny23, bidenny23, trumpny24, bidenny24, trumpny25, bidenny25, trumpny26, bidenny26, trumpny27, bidenny27 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpwy, bidenwy, trumpwy1, bidenwy1 = set(), set(), set(), set()
trumppa, bidenpa, trumppa1, bidenpa1, trumppa2, bidenpa2, trumppa3, bidenpa3, trumppa4, bidenpa4, trumppa5, bidenpa5, trumppa6, bidenpa6, trumppa7, bidenpa7, trumppa8, bidenpa8, trumppa9, bidenpa9, trumppa10, bidenpa10, trumppa11, bidenpa11, trumppa12, bidenpa12, trumppa13, bidenpa13, trumppa14, bidenpa14, trumppa15, bidenpa15, trumppa16, bidenpa16, trumppa17, bidenpa17, trumppa18, bidenpa18 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpct, bidenct, trumpct1, bidenct1, trumpct2, bidenct2, trumpct3, bidenct3, trumpct4, bidenct4, trumpct5, bidenct5 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpky, bidenky, trumpky1, bidenky1, trumpky2, bidenky2, trumpky3, bidenky3, trumpky4, bidenky4, trumpky5, bidenky5, trumpky6, bidenky6 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpla, bidenla, trumpla1, bidenla1, trumpla2, bidenla2, trumpla3, bidenla3, trumpla4, bidenla4, trumpla5, bidenla5, trumpla6, bidenla6 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpok, bidenok, trumpok1, bidenok1, trumpok2, bidenok2, trumpok3, bidenok3, trumpok4, bidenok4, trumpok5, bidenok5 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumput, bidenut, trumput1, bidenut1, trumput2, bidenut2, trumput3, bidenut3, trumput4, bidenut4 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpoh, bidenoh, trumpoh1, bidenoh1, trumpoh2, bidenoh2, trumpoh3, bidenoh3, trumpoh4, bidenoh4, trumpoh5, bidenoh5, trumpoh6, bidenoh6, trumpoh7, bidenoh7, trumpoh8, bidenoh8, trumpoh9, bidenoh9, trumpoh10, bidenoh10, trumpoh11, bidenoh11, trumpoh12, bidenoh12, trumpoh13, bidenoh13, trumpoh14, bidenoh14, trumpoh15, bidenoh15, trumpoh16, bidenoh16 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
trumpor, bidenor, trumpor1, bidenor1, trumpor2, bidenor2, trumpor3, bidenor3, trumpor4, bidenor4, trumpor5, bidenor5 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()


# with open('/Volumes/WINDOWS/test.txt', 'rb') as f:
#     trumpal1, trumpal2, trumpal3, trumpal4, trumpal5, trumpal6, trumpal7, bidenal1, bidenal2, bidenal3, bidenal4, bidenal5, bidenal6, bidenal7, trumpak1, bidenak1, trumpaz1, trumpaz2, trumpaz3, trumpaz4, trumpaz5, trumpaz6, trumpaz7, trumpaz8, trumpaz9, bidenaz1, bidenaz2, bidenaz3, bidenaz4, bidenaz5, bidenaz6, bidenaz7, bidenaz8, bidenaz9, bidenar1, bidenar2, bidenar3, bidenar4, trumpar1, trumpar2, trumpar3, trumpar4, bidenak1, trumpca1, trumpca2, trumpca3, trumpca4, trumpca5, trumpca6, trumpca7, trumpca8, trumpca9, trumpca10, trumpca11, trumpca12, trumpca13, trumpca14, trumpca15, trumpca16, trumpca17, trumpca18, trumpca19, trumpca20, trumpca21, trumpca22, trumpca23, trumpca24, trumpca25, trumpca26, trumpca27, trumpca28, trumpca29, trumpca30, trumpca31, trumpca32, trumpca33, trumpca34, trumpca35, trumpca36, trumpca37, trumpca38, trumpca39, trumpca40, trumpca41, trumpca42, trumpca43, trumpca44, trumpca45, trumpca46, trumpca47, trumpca48, trumpca49, trumpca50, trumpca51, trumpca52, trumpca53, bidenca1, bidenca2, bidenca3, bidenca4, bidenca5, bidenca6, bidenca7, bidenca8, bidenca9, bidenca10, bidenca11, bidenca12, bidenca13, bidenca14, bidenca15, bidenca16, bidenca17, bidenca18, bidenca19, bidenca20, bidenca21, bidenca22, bidenca23, bidenca24, bidenca25, bidenca26, bidenca27, bidenca28, bidenca29, bidenca30, bidenca31, bidenca32, bidenca33, bidenca34, bidenca35, bidenca36, bidenca37, bidenca38, bidenca39, bidenca40, bidenca41, bidenca42, bidenca43, bidenca44, bidenca45, bidenca46, bidenca47, bidenca48, bidenca49, bidenca50, bidenca51, bidenca52, bidenca53, trumpco1, trumpco2, trumpco3, trumpco4, trumpco5, trumpco6, trumpco7, bidenco1, bidenco2, bidenco3, bidenco4, bidenco5, bidenco6, bidenco7, bidenct1, bidenct2, bidenct3, bidenct4, bidenct5, trumpct1, trumpct2, trumpct3, trumpct4, trumpct5, trumpde1, bidende1, bidenfl1, bidenfl2, bidenfl3, bidenfl4, bidenfl5, bidenfl6, bidenfl7, bidenfl8, bidenfl9, bidenfl10, bidenfl11, bidenfl12, bidenfl13, bidenfl14, bidenfl15, bidenfl16, bidenfl17, bidenfl18, bidenfl19, bidenfl20, bidenfl21, bidenfl22, bidenfl23, bidenfl24, bidenfl25, bidenfl26, bidenfl27, trumpfl1, trumpfl2, trumpfl3, trumpfl4, trumpfl5, trumpfl6, trumpfl7, trumpfl8, trumpfl9, trumpfl10, trumpfl11, trumpfl12, trumpfl13, trumpfl14, trumpfl15, trumpfl16, trumpfl17, trumpfl18, trumpfl19, trumpfl20, trumpfl21, trumpfl22, trumpfl23, trumpfl24, trumpfl25, trumpfl26, trumpfl27, trumpga1, trumpga2, trumpga3, trumpga4, trumpga5, trumpga6, trumpga7, trumpga8, trumpga9, trumpga10, trumpga11, trumpga12, trumpga13, trumpga14, bidenga1, bidenga2, bidenga3, bidenga4, bidenga5, bidenga6, bidenga7, bidenga8, bidenga9, bidenga10, bidenga11, bidenga12, bidenga13, bidenga14, trumphi1, trumphi2, bidenhi1, bidenhi2, trumpid1, trumpid2, bidenid1, bidenid2, bidenil1, bidenil2, bidenil3, bidenil4, bidenil5, bidenil6, bidenil7, bidenil8, bidenil9, bidenil10, bidenil11, bidenil12, bidenil13, bidenil14, bidenil15, bidenil16, bidenil17, bidenil18, trumpil1, trumpil2, trumpil3, trumpil4, trumpil5, trumpil6, trumpil7, trumpil8, trumpil9, trumpil10, trumpil11, trumpil12, trumpil13, trumpil14, trumpil15, trumpil16, trumpil17, trumpil18, trumpin1, trumpin2, trumpin3, trumpin4, trumpin5, trumpin6, trumpin7, trumpin8, trumpin9, bidenin1, bidenin2, bidenin3, bidenin4, bidenin5, bidenin6, bidenin7, bidenin8, bidenin9, trumpia1, trumpia2, trumpia3, trumpia4, bidenia1, bidenia2, bidenia3, bidenia4, trumpks1, trumpks2, trumpks3, trumpks4, bidenks1, bidenks2, bidenks3, bidenks4, trumpky1, trumpky2, trumpky3, trumpky4, trumpky5, trumpky6, bidenky1, bidenky2, bidenky3, bidenky4, bidenky5, bidenky6, trumpla1, trumpla2, trumpla3, trumpla4, trumpla5, trumpla6, bidenla1, bidenla2, bidenla3, bidenla4, bidenla5, bidenla6, trumpme1, trumpme2, bidenme1, bidenme2, trumpmd1, trumpmd2, trumpmd3, trumpmd4, trumpmd5, trumpmd6, trumpmd7, trumpmd8, bidenmd1, bidenmd2, bidenmd3, bidenmd4, bidenmd5, bidenmd6, bidenmd7, bidenmd8, trumpma1, trumpma2, trumpma3, trumpma4, trumpma5, trumpma6, trumpma7, trumpma8, trumpma9, bidenma1, bidenma2, bidenma3, bidenma4, bidenma5, bidenma6, bidenma7, bidenma8, bidenma9, bidenmi1, bidenmi2, bidenmi3, bidenmi4, bidenmi5, bidenmi6, bidenmi7, bidenmi8, bidenmi9, bidenmi10, bidenmi11, bidenmi12, bidenmi13, bidenmi14, trumpmi1, trumpmi2, trumpmi3, trumpmi4, trumpmi5, trumpmi6, trumpmi7, trumpmi8, trumpmi9, trumpmi10, trumpmi11, trumpmi12, trumpmi13, trumpmi14, trumpmn1, trumpmn2, trumpmn3, trumpmn4, trumpmn5, trumpmn6, trumpmn7, trumpmn8, bidenmn1, bidenmn2, bidenmn3, bidenmn4, bidenmn5, bidenmn6, bidenmn7, bidenmn8, trumpms1, trumpms2, trumpms3, trumpms4, bidenms1, bidenms2, bidenms3, bidenms4, trumpmo1, trumpmo2, trumpmo3, trumpmo4, trumpmo5, trumpmo6, trumpmo7, trumpmo8, bidenmo1, bidenmo2, bidenmo3, bidenmo4, bidenmo5, bidenmo6, bidenmo7, bidenmo8, trumpmt1, bidenmt1, trumpne1, trumpne2, trumpne3, bidenne1, bidenne2, bidenne3, trumpnv1, trumpnv2, trumpnv3, trumpnv4, bidennv1, bidennv2, bidennv3, bidennv4, trumpnh1, trumpnh2, bidennh1, bidennh2, bidennj1, bidennj2, bidennj3, bidennj4, bidennj5, bidennj6, bidennj7, bidennj8, bidennj9, bidennj10, bidennj11, bidennj12, trumpnj1, trumpnj2, trumpnj3, trumpnj4, trumpnj5, trumpnj6, trumpnj7, trumpnj8, trumpnj9, trumpnj10, trumpnj11, trumpnj12, trumpnm1, trumpnm2, trumpnm3, bidennm1, bidennm2, bidennm3, trumpny1, trumpny2, trumpny3, trumpny4, trumpny5, trumpny6, trumpny7, trumpny8, trumpny9, trumpny10, trumpny11, trumpny12, trumpny13, trumpny14, trumpny15, trumpny16, trumpny17, trumpny18, trumpny19, trumpny20, trumpny21, trumpny22, trumpny23, trumpny24, trumpny25, trumpny26, trumpny27, bidenny1, bidenny2, bidenny3, bidenny4, bidenny5, bidenny6, bidenny7, bidenny8, bidenny9, bidenny10, bidenny11, bidenny12, bidenny13, bidenny14, bidenny15, bidenny16, bidenny17, bidenny18, bidenny19, bidenny20, bidenny21, bidenny22, bidenny23, bidenny24, bidenny25, bidenny26, bidenny27, bidennc1, bidennc2, bidennc3, bidennc4, bidennc5, bidennc6, bidennc7, bidennc8, bidennc9, bidennc10, bidennc11, bidennc12, bidennc13, trumpnc1, trumpnc2, trumpnc3, trumpnc4, trumpnc5, trumpnc6, trumpnc7, trumpnc8, trumpnc9, trumpnc10, trumpnc11, trumpnc12, trumpnc13, trumpnd1, bidennd1, bidenoh1, bidenoh2, bidenoh3, bidenoh4, bidenoh5, bidenoh6, bidenoh7, bidenoh8, bidenoh9, bidenoh10, bidenoh11, bidenoh12, bidenoh13, bidenoh14, bidenoh15, bidenoh16, trumpoh1, trumpoh2, trumpoh3, trumpoh4, trumpoh5, trumpoh6, trumpoh7, trumpoh8, trumpoh9, trumpoh10, trumpoh11, trumpoh12, trumpoh13, trumpoh14, trumpoh15, trumpoh16, trumpok1, trumpok2, trumpok3, trumpok4, trumpok5, bidenok1, bidenok2, bidenok3, bidenok4, bidenok5, trumpor1, trumpor2, trumpor3, trumpor4, trumpor5, bidenor1, bidenor2, bidenor3, bidenor4, bidenor5, bidenpa1, bidenpa2, bidenpa3, bidenpa4, bidenpa5, bidenpa6, bidenpa7, bidenpa8, bidenpa9, bidenpa10, bidenpa11, bidenpa12, bidenpa13, bidenpa14, bidenpa15, bidenpa16, bidenpa17, bidenpa18, trumppa1, trumppa2, trumppa3, trumppa4, trumppa5, trumppa6, trumppa7, trumppa8, trumppa9, trumppa10, trumppa11, trumppa12, trumppa13, trumppa14, trumppa15, trumppa16, trumppa17, trumppa18, trumpri1, trumpri2, bidenri1, bidenri2, trumpsc1, trumpsc2, trumpsc3, trumpsc4, trumpsc5, trumpsc6, trumpsc7, bidensc1, bidensc2, bidensc3, bidensc4, bidensc5, bidensc6, bidensc7, trumpsd1, bidensd1, trumptn1, trumptn2, trumptn3, trumptn4, trumptn5, trumptn6, trumptn7, trumptn8, trumptn9, bidentn1, bidentn2, bidentn3, bidentn4, bidentn5, bidentn6, bidentn7, bidentn8, bidentn9, trumptx1, trumptx2, trumptx3, trumptx4, trumptx5, trumptx6, trumptx7, trumptx8, trumptx9, trumptx10, trumptx11, trumptx12, trumptx13, trumptx14, trumptx15, trumptx16, trumptx17, trumptx18, trumptx19, trumptx20, trumptx21, trumptx22, trumptx23, trumptx24, trumptx25, trumptx26, trumptx27, trumptx28, trumptx29, trumptx30, trumptx31, trumptx32, trumptx33, trumptx34, trumptx35, trumptx36, bidentx1, bidentx2, bidentx3, bidentx4, bidentx5, bidentx6, bidentx7, bidentx8, bidentx9, bidentx10, bidentx11, bidentx12, bidentx13, bidentx14, bidentx15, bidentx16, bidentx17, bidentx18, bidentx19, bidentx20, bidentx21, bidentx22, bidentx23, bidentx24, bidentx25, bidentx26, bidentx27, bidentx28, bidentx29, bidentx30, bidentx31, bidentx32, bidentx33, bidentx34, bidentx35, bidentx36, trumput1, trumput2, trumput3, trumput4, bidenut1, bidenut2, bidenut3, bidenut4, trumpvt1, bidenvt1, bidenva1, bidenva2, bidenva3, bidenva4, bidenva5, bidenva6, bidenva7, bidenva8, bidenva9, bidenva10, bidenva11, trumpva1, trumpva2, trumpva3, trumpva4, trumpva5, trumpva6, trumpva7, trumpva8, trumpva9, trumpva10, trumpva11, bidenwa1, bidenwa2, bidenwa3, bidenwa4, bidenwa5, bidenwa6, bidenwa7, bidenwa8, bidenwa9, bidenwa10, trumpwa1, trumpwa2, trumpwa3, trumpwa4, trumpwa5, trumpwa6, trumpwa7, trumpwa8, trumpwa9, trumpwa10, trumpwv1, trumpwv2, trumpwv3, bidenwv1, bidenwv2, bidenwv3, trumpwi1, trumpwi2, trumpwi3, trumpwi4, trumpwi5, trumpwi6, trumpwi7, trumpwi8, bidenwi1, bidenwi2, bidenwi3, bidenwi4, bidenwi5, bidenwi6, bidenwi7, bidenwi8, trumpwy1, bidenwy1 = pickle.load(f)



#			trumpmo1.add(tw["user"]["id"])
#trumpmo.add(tw["user"]["id"])

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
	district = sortloc("#trump2020", tw["user"]["location"], tw["retweeted_status"]["full_text"].lower())
	if(district != "null"):
		if(district == "mo1"):
			trumpmo1.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo2"):
			trumpmo2.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo3"):
			trumpmo3.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo4"):
			trumpmo4.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo5"):
			trumpmo5.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo6"):
			trumpmo6.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo7"):
			trumpmo7.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo8"):
			trumpmo8.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "sc1"):
			trumpsc1.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc2"):
			trumpsc2.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc3"):
			trumpsc3.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc4"):
			trumpsc4.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc5"):
			trumpsc5.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc6"):
			trumpsc6.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc7"):
			trumpsc7.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "ky1"):
			trumpky1.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky2"):
			trumpky2.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky3"):
			trumpky3.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky4"):
			trumpky4.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky5"):
			trumpky5.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky6"):
			trumpky6.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ok1"):
			trumpok1.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok2"):
			trumpok2.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok3"):
			trumpok3.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok4"):
			trumpok4.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok5"):
			trumpok5.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ia1"):
			trumpia1.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ia2"):
			trumpia2.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ia3"):
			trumpia3.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ia4"):
			trumpia4.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ks1"):
			trumpks1.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ks2"):
			trumpks2.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ks3"):
			trumpks3.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ks4"):
			trumpks4.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ca1"):
			trumpca1.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca2"):
			trumpca2.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca3"):
			trumpca3.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca4"):
			trumpca4.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca5"):
			trumpca5.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca6"):
			trumpca6.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca7"):
			trumpca7.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca8"):
			trumpca8.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca9"):
			trumpca9.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca10"):
			trumpca10.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca11"):
			trumpca11.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca12"):
			trumpca12.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca13"):
			trumpca13.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca14"):
			trumpca14.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca15"):
			trumpca15.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca16"):
			trumpca16.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca17"):
			trumpca17.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca18"):
			trumpca18.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca19"):
			trumpca19.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca20"):
			trumpca20.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca21"):
			trumpca21.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca22"):
			trumpca22.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca23"):
			trumpca23.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca24"):
			trumpca24.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca25"):
			trumpca25.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca26"):
			trumpca26.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca27"):
			trumpca27.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca28"):
			trumpca28.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca29"):
			trumpca29.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca30"):
			trumpca30.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca31"):
			trumpca31.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca32"):
			trumpca32.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca33"):
			trumpca33.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca34"):
			trumpca34.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca35"):
			trumpca35.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca36"):
			trumpca36.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca37"):
			trumpca37.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca38"):
			trumpca38.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca39"):
			trumpca39.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca40"):
			trumpca40.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca41"):
			trumpca41.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca42"):
			trumpca42.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca43"):
			trumpca43.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca44"):
			trumpca44.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca45"):
			trumpca45.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca46"):
			trumpca46.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca47"):
			trumpca47.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca48"):
			trumpca48.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca49"):
			trumpca49.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca50"):
			trumpca50.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca51"):
			trumpca51.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca52"):
			trumpca52.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca53"):
			trumpca53.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "la1"):
			trumpla1.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la2"):
			trumpla2.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la3"):
			trumpla3.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la4"):
			trumpla4.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la5"):
			trumpla5.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la6"):
			trumpla6.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "ct1"):
			trumpct1.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct2"):
			trumpct2.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct3"):
			trumpct3.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct4"):
			trumpct4.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct5"):
			trumpct5.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "mt1"):
			trumpmt1.add(tw["user"]["id"])
			trumpmt.add(tw["user"]["id"])
		elif(district == "ms1"):
			trumpms1.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "ms2"):
			trumpms2.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "ms3"):
			trumpms3.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "ms4"):
			trumpms4.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "pa1"):
			trumppa1.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa2"):
			trumppa2.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa3"):
			trumppa3.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa4"):
			trumppa4.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa5"):
			trumppa5.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa6"):
			trumppa6.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa7"):
			trumppa7.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa8"):
			trumppa8.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa9"):
			trumppa9.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa10"):
			trumppa10.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa11"):
			trumppa11.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa12"):
			trumppa12.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa13"):
			trumppa13.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa14"):
			trumppa14.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa15"):
			trumppa15.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa16"):
			trumppa16.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa17"):
			trumppa17.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa18"):
			trumppa18.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "oh1"):
			trumpoh1.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh2"):
			trumpoh2.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh3"):
			trumpoh3.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh4"):
			trumpoh4.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh5"):
			trumpoh5.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		if(district == "oh6"):
			trumpoh6.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh7"):
			trumpoh7.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh8"):
			trumpoh8.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh9"):
			trumpoh9.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh10"):
			trumpoh10.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh11"):
			trumpoh11.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh12"):
			trumpoh12.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh13"):
			trumpoh13.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh14"):
			trumpoh14.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh15"):
			trumpoh15.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh16"):
			trumpoh16.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "fl1"):
			trumpfl1.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl2"):
			trumpfl2.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl3"):
			trumpfl3.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl4"):
			trumpfl4.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl5"):
			trumpfl5.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl6"):
			trumpfl6.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl7"):
			trumpfl7.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl8"):
			trumpfl8.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl9"):
			trumpfl9.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl10"):
			trumpfl10.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl11"):
			trumpfl11.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl12"):
			trumpfl12.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl13"):
			trumpfl13.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl14"):
			trumpfl14.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl15"):
			trumpfl15.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl16"):
			trumpfl16.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl17"):
			trumpfl17.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl18"):
			trumpfl18.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl19"):
			trumpfl19.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl20"):
			trumpfl20.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl21"):
			trumpfl21.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl22"):
			trumpfl22.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl23"):
			trumpfl23.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl24"):
			trumpfl24.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl25"):
			trumpfl25.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl26"):
			trumpfl26.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl27"):
			trumpfl27.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "wa1"):
			trumpwa1.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa2"):
			trumpwa2.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa3"):
			trumpwa3.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa4"):
			trumpwa4.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa5"):
			trumpwa5.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa6"):
			trumpwa6.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa7"):
			trumpwa7.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa8"):
			trumpwa8.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa9"):
			trumpwa9.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa10"):
			trumpwa10.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "hi1"):
			trumphi1.add(tw["user"]["id"])
			trumphi.add(tw["user"]["id"])
		elif(district == "hi2"):
			trumphi2.add(tw["user"]["id"])
			trumphi.add(tw["user"]["id"])
		elif(district == "nj1"):
			trumpnj1.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj2"):
			trumpnj2.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj3"):
			trumpnj3.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj4"):
			trumpnj4.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj5"):
			trumpnj5.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj6"):
			trumpnj6.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj7"):
			trumpnj7.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj8"):
			trumpnj8.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj9"):
			trumpnj9.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj10"):
			trumpnj10.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj11"):
			trumpnj11.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj12"):
			trumpnj12.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "ny1"):
			trumpny1.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny2"):
			trumpny2.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny3"):
			trumpny3.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny4"):
			trumpny4.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny5"):
			trumpny5.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny6" or district == "ny7" or district == "ny8" or district == "ny9" or district == "ny10" or district == "ny11" or district == "ny12" or district == "ny13" or district == "ny14" or district == "ny15"):
			trumpny6.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny7.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny8.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny9.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny10.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny11.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny12.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny13.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny14.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny15.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny16"):
			trumpny16.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny17"):
			trumpny17.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny18"):
			trumpny18.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny19"):
			trumpny19.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny20"):
			trumpny20.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny21"):
			trumpny21.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny22"):
			trumpny22.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny23"):
			trumpny23.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny24"):
			trumpny24.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny25"):
			trumpny25.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny26"):
			trumpny26.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny27"):
			trumpny27.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ri1"):
			trumpri1.add(tw["user"]["id"])
			trumpri.add(tw["user"]["id"])
		elif(district == "ri2"):
			trumpri2.add(tw["user"]["id"])
			trumpri.add(tw["user"]["id"])
		elif(district == "mn1"):
			trumpmn1.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn2"):
			trumpmn2.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn3"):
			trumpmn3.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn4"):
			trumpmn4.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn5"):
			trumpmn5.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn6"):
			trumpmn6.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn7"):
			trumpmn7.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn8"):
			trumpmn8.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mi1"):
			trumpmi1.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi2"):
			trumpmi2.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi3"):
			trumpmi3.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi4"):
			trumpmi4.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi5"):
			trumpmi5.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi6"):
			trumpmi6.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi7"):
			trumpmi7.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi8"):
			trumpmi8.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi9"):
			trumpmi9.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi10"):
			trumpmi10.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi11"):
			trumpmi11.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi12"):
			trumpmi12.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi13"):
			trumpmi13.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi14"):
			trumpmi14.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "wi1"):
			trumpwi1.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi2"):
			trumpwi2.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi3"):
			trumpwi3.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi4"):
			trumpwi4.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi5"):
			trumpwi5.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi6"):
			trumpwi6.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi7"):
			trumpwi7.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi8"):
			trumpwi8.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "or1"):
			trumpor1.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or2"):
			trumpor2.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or3"):
			trumpor3.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or4"):
			trumpor4.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or5"):
			trumpor5.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "md1"):
			trumpmd1.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md2"):
			trumpmd2.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md3"):
			trumpmd3.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md4"):
			trumpmd4.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md5"):
			trumpmd5.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md6"):
			trumpmd6.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md7"):
			trumpmd7.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md8"):
			trumpmd8.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "ma1"):
			trumpma1.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma2"):
			trumpma2.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma3"):
			trumpma3.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma4"):
			trumpma4.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma5"):
			trumpma5.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma6"):
			trumpma6.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma7"):
			trumpma7.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma8"):
			trumpma8.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma9"):
			trumpma9.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "me1"):
			trumpme1.add(tw["user"]["id"])
			trumpme.add(tw["user"]["id"])
		elif(district == "me2"):
			trumpme2.add(tw["user"]["id"])
			trumpme.add(tw["user"]["id"])
		elif(district == "id1"):
			trumpid1.add(tw["user"]["id"])
			trumpid.add(tw["user"]["id"])
		elif(district == "id2"):
			trumpid2.add(tw["user"]["id"])
			trumpid.add(tw["user"]["id"])
		elif(district == "nc1"):
			trumpnc1.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc2"):
			trumpnc2.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc3"):
			trumpnc3.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc4"):
			trumpnc4.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc5"):
			trumpnc5.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc6"):
			trumpnc6.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc7"):
			trumpnc7.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc8"):
			trumpnc8.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc9"):
			trumpnc9.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc10"):
			trumpnc10.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc11"):
			trumpnc11.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc12"):
			trumpnc12.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc13"):
			trumpnc13.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nh1"):
			trumpnh1.add(tw["user"]["id"])
			trumpnh.add(tw["user"]["id"])
		elif(district == "nh2"):
			trumpnh2.add(tw["user"]["id"])
			trumpnh.add(tw["user"]["id"])
		elif(district == "nv1"):
			trumpnv1.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "nv2"):
			trumpnv2.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "nv3"):
			trumpnv3.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "nv4"):
			trumpnv4.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "co1"):
			trumpco1.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co2"):
			trumpco2.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co3"):
			trumpco3.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co4"):
			trumpco4.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co5"):
			trumpco5.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co6"):
			trumpco6.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co7"):
			trumpco7.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "nm1"):
			trumpnm1.add(tw["user"]["id"])
			trumpnm.add(tw["user"]["id"])
		elif(district == "nm2"):
			trumpnm2.add(tw["user"]["id"])
			trumpnm.add(tw["user"]["id"])
		elif(district == "nm3"):
			trumpnm3.add(tw["user"]["id"])
			trumpnm.add(tw["user"]["id"])
		elif(district == "az1"):
			trumpaz1.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az2"):
			trumpaz2.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az3"):
			trumpaz3.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az4"):
			trumpaz4.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az5"):
			trumpaz5.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az6"):
			trumpaz6.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az7"):
			trumpaz7.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az8"):
			trumpaz8.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az9"):
			trumpaz9.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "ga1"):
			trumpga1.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga2"):
			trumpga2.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga3"):
			trumpga3.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga4"):
			trumpga4.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga5"):
			trumpga5.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga6"):
			trumpga6.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga7"):
			trumpga7.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga8"):
			trumpga8.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga9"):
			trumpga9.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga10"):
			trumpga10.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga11"):
			trumpga11.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga12"):
			trumpga12.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga13"):
			trumpga13.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga14"):
			trumpga14.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "tx1"):
			trumptx1.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx2"):
			trumptx2.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx3"):
			trumptx3.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx4"):
			trumptx4.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx5"):
			trumptx5.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx6"):
			trumptx6.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx7"):
			trumptx7.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx8"):
			trumptx8.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx9"):
			trumptx9.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx10"):
			trumptx10.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx11"):
			trumptx11.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx12"):
			trumptx12.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx13"):
			trumptx13.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx14"):
			trumptx14.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx15"):
			trumptx15.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx16"):
			trumptx16.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx17"):
			trumptx17.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx18"):
			trumptx18.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx19"):
			trumptx19.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx20"):
			trumptx20.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx21"):
			trumptx21.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx22"):
			trumptx22.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx23"):
			trumptx23.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx24"):
			trumptx24.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx25"):
			trumptx25.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx26"):
			trumptx26.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx27"):
			trumptx27.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx28"):
			trumptx28.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx29"):
			trumptx29.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx30"):
			trumptx30.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx31"):
			trumptx31.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx32"):
			trumptx32.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx33"):
			trumptx33.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx34"):
			trumptx34.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx35"):
			trumptx35.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx36"):
			trumptx36.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "in1"):
			trumpin1.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in2"):
			trumpin2.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in3"):
			trumpin3.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in4"):
			trumpin4.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in5"):
			trumpin5.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in6"):
			trumpin6.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in7"):
			trumpin7.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in8"):
			trumpin8.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in9"):
			trumpin9.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "va1"):
			trumpva1.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va2"):
			trumpva2.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va3"):
			trumpva3.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va4"):
			trumpva4.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va5"):
			trumpva5.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va6"):
			trumpva6.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va7"):
			trumpva7.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va8"):
			trumpva8.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va9"):
			trumpva9.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va10"):
			trumpva10.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va11"):
			trumpva11.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "il1"):
			trumpil1.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il2"):
			trumpil2.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il3"):
			trumpil3.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il4"):
			trumpil4.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il5"):
			trumpil5.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il6"):
			trumpil6.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il7"):
			trumpil7.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il8"):
			trumpil8.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il9"):
			trumpil9.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il10"):
			trumpil10.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il11"):
			trumpil11.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il12"):
			trumpil12.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il13"):
			trumpil13.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il14"):
			trumpil14.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il15"):
			trumpil15.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il16"):
			trumpil16.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il17"):
			trumpil17.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il18"):
			trumpil18.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "de1"):
			trumpde1.add(tw["user"]["id"])
			trumpde.add(tw["user"]["id"])
		elif(district == "vt1"):
			trumpvt1.add(tw["user"]["id"])
			trumpvt.add(tw["user"]["id"])
		elif(district == "ut1"):
			trumput1.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ut2"):
			trumput2.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ut3"):
			trumput3.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ut4"):
			trumput4.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ne1"):
			trumpne1.add(tw["user"]["id"])
			trumpne.add(tw["user"]["id"])
		elif(district == "ne2"):
			trumpne2.add(tw["user"]["id"])
			trumpne.add(tw["user"]["id"])
		elif(district == "ne3"):
			trumpne3.add(tw["user"]["id"])
			trumpne.add(tw["user"]["id"])
		elif(district == "ak1"):
			trumpak1.add(tw["user"]["id"])
			trumpak.add(tw["user"]["id"])
		elif(district == "wy1"):
			trumpwy1.add(tw["user"]["id"])
			trumpwy.add(tw["user"]["id"])
		elif(district == "al1"):
			trumpal1.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al2"):
			trumpal2.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al3"):
			trumpal3.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al4"):
			trumpal4.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al5"):
			trumpal5.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al6"):
			trumpal6.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al7"):
			trumpal7.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "tn1"):
			trumptn1.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn2"):
			trumptn2.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn3"):
			trumptn3.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn4"):
			trumptn4.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn5"):
			trumptn5.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn6"):
			trumptn6.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn7"):
			trumptn7.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn8"):
			trumptn8.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn9"):
			trumptn9.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "nd1"):
			trumpnd1.add(tw["user"]["id"])
			trumpnd.add(tw["user"]["id"])
		elif(district == "sd1"):
			trumpsd1.add(tw["user"]["id"])
			trumpsd.add(tw["user"]["id"])
		elif(district == "wv1"):
			trumpwv1.add(tw["user"]["id"])
			trumpwv.add(tw["user"]["id"])
		elif(district == "wv2"):
			trumpwv2.add(tw["user"]["id"])
			trumpwv.add(tw["user"]["id"])
		elif(district == "wv3"):
			trumpwv3.add(tw["user"]["id"])
			trumpwv.add(tw["user"]["id"])
		elif(district == "ar1"):
			trumpar1.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
		elif(district == "ar2"):
			trumpar2.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
		elif(district == "ar3"):
			trumpar3.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
		elif(district == "ar4"):
			trumpar4.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
	district = sortloc("#biden2020", tw["user"]["location"], tw["retweeted_status"]["full_text"].lower())
	if(district != "null"):
		if(district == "mo1"):
			bidenmo1.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo2"):
			bidenmo2.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo3"):
			bidenmo3.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo4"):
			bidenmo4.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo5"):
			bidenmo5.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo6"):
			bidenmo6.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo7"):
			bidenmo7.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo8"):
			bidenmo8.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "sc1"):
			bidensc1.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc2"):
			bidensc2.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc3"):
			bidensc3.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc4"):
			bidensc4.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc5"):
			bidensc5.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc6"):
			bidensc6.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc7"):
			bidensc7.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "ky1"):
			bidenky1.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky2"):
			bidenky2.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky3"):
			bidenky3.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky4"):
			bidenky4.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky5"):
			bidenky5.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky6"):
			bidenky6.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ok1"):
			bidenok1.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok2"):
			bidenok2.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok3"):
			bidenok3.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok4"):
			bidenok4.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok5"):
			bidenok5.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ia1"):
			bidenia1.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ia2"):
			bidenia2.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ia3"):
			bidenia3.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ia4"):
			bidenia4.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ks1"):
			bidenks1.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ks2"):
			bidenks2.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ks3"):
			bidenks3.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ks4"):
			bidenks4.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ca1"):
			bidenca1.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca2"):
			bidenca2.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca3"):
			bidenca3.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca4"):
			bidenca4.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca5"):
			bidenca5.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca6"):
			bidenca6.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca7"):
			bidenca7.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca8"):
			bidenca8.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca9"):
			bidenca9.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca10"):
			bidenca10.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca11"):
			bidenca11.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca12"):
			bidenca12.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca13"):
			bidenca13.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca14"):
			bidenca14.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca15"):
			bidenca15.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca16"):
			bidenca16.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca17"):
			bidenca17.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca18"):
			bidenca18.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca19"):
			bidenca19.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca20"):
			bidenca20.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca21"):
			bidenca21.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca22"):
			bidenca22.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca23"):
			bidenca23.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca24"):
			bidenca24.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca25"):
			bidenca25.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca26"):
			bidenca26.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca27"):
			bidenca27.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca28"):
			bidenca28.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca29"):
			bidenca29.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca30"):
			bidenca30.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca31"):
			bidenca31.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca32"):
			bidenca32.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca33"):
			bidenca33.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca34"):
			bidenca34.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca35"):
			bidenca35.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca36"):
			bidenca36.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca37"):
			bidenca37.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca38"):
			bidenca38.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca39"):
			bidenca39.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca40"):
			bidenca40.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca41"):
			bidenca41.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca42"):
			bidenca42.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca43"):
			bidenca43.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca44"):
			bidenca44.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca45"):
			bidenca45.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca46"):
			bidenca46.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca47"):
			bidenca47.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca48"):
			bidenca48.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca49"):
			bidenca49.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca50"):
			bidenca50.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca51"):
			bidenca51.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca52"):
			bidenca52.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca53"):
			bidenca53.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "la1"):
			bidenla1.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la2"):
			bidenla2.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la3"):
			bidenla3.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la4"):
			bidenla4.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la5"):
			bidenla5.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la6"):
			bidenla6.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "ct1"):
			bidenct1.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct2"):
			bidenct2.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct3"):
			bidenct3.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct4"):
			bidenct4.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct5"):
			bidenct5.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "mt1"):
			bidenmt1.add(tw["user"]["id"])
			bidenmt.add(tw["user"]["id"])
		elif(district == "ms1"):
			bidenms1.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "ms2"):
			bidenms2.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "ms3"):
			bidenms3.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "ms4"):
			bidenms4.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "pa1"):
			bidenpa1.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa2"):
			bidenpa2.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa3"):
			bidenpa3.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa4"):
			bidenpa4.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa5"):
			bidenpa5.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa6"):
			bidenpa6.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa7"):
			bidenpa7.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa8"):
			bidenpa8.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa9"):
			bidenpa9.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa10"):
			bidenpa10.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa11"):
			bidenpa11.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa12"):
			bidenpa12.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa13"):
			bidenpa13.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa14"):
			bidenpa14.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa15"):
			bidenpa15.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa16"):
			bidenpa16.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa17"):
			bidenpa17.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa18"):
			bidenpa18.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "oh1"):
			bidenoh1.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh2"):
			bidenoh2.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh3"):
			bidenoh3.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh4"):
			bidenoh4.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh5"):
			bidenoh5.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		if(district == "oh6"):
			bidenoh6.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh7"):
			bidenoh7.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh8"):
			bidenoh8.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh9"):
			bidenoh9.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh10"):
			bidenoh10.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh11"):
			bidenoh11.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh12"):
			bidenoh12.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh13"):
			bidenoh13.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh14"):
			bidenoh14.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh15"):
			bidenoh15.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh16"):
			bidenoh16.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "fl1"):
			bidenfl1.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl2"):
			bidenfl2.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl3"):
			bidenfl3.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl4"):
			bidenfl4.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl5"):
			bidenfl5.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl6"):
			bidenfl6.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl7"):
			bidenfl7.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl8"):
			bidenfl8.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl9"):
			bidenfl9.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl10"):
			bidenfl10.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl11"):
			bidenfl11.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl12"):
			bidenfl12.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl13"):
			bidenfl13.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl14"):
			bidenfl14.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl15"):
			bidenfl15.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl16"):
			bidenfl16.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl17"):
			bidenfl17.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl18"):
			bidenfl18.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl19"):
			bidenfl19.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl20"):
			bidenfl20.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl21"):
			bidenfl21.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl22"):
			bidenfl22.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl23"):
			bidenfl23.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl24"):
			bidenfl24.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl25"):
			bidenfl25.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl26"):
			bidenfl26.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl27"):
			bidenfl27.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "wa1"):
			bidenwa1.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa2"):
			bidenwa2.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa3"):
			bidenwa3.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa4"):
			bidenwa4.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa5"):
			bidenwa5.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa6"):
			bidenwa6.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa7"):
			bidenwa7.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa8"):
			bidenwa8.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa9"):
			bidenwa9.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa10"):
			bidenwa10.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "hi1"):
			bidenhi1.add(tw["user"]["id"])
			bidenhi.add(tw["user"]["id"])
		elif(district == "hi2"):
			bidenhi2.add(tw["user"]["id"])
			bidenhi.add(tw["user"]["id"])
		elif(district == "nj1"):
			bidennj1.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj2"):
			bidennj2.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj3"):
			bidennj3.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj4"):
			bidennj4.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj5"):
			bidennj5.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj6"):
			bidennj6.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj7"):
			bidennj7.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj8"):
			bidennj8.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj9"):
			bidennj9.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj10"):
			bidennj10.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj11"):
			bidennj11.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj12"):
			bidennj12.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "ny1"):
			bidenny1.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny2"):
			bidenny2.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny3"):
			bidenny3.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny4"):
			bidenny4.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny5"):
			bidenny5.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny6" or district == "ny7" or district == "ny8" or district == "ny9" or district == "ny10" or district == "ny11" or district == "ny12" or district == "ny13" or district == "ny14" or district == "ny15"):
			bidenny6.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny7.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny8.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny9.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny10.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny11.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny12.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny13.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny14.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny15.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny16"):
			bidenny16.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny17"):
			bidenny17.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny18"):
			bidenny18.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny19"):
			bidenny19.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny20"):
			bidenny20.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny21"):
			bidenny21.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny22"):
			bidenny22.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny23"):
			bidenny23.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny24"):
			bidenny24.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny25"):
			bidenny25.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny26"):
			bidenny26.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny27"):
			bidenny27.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ri1"):
			bidenri1.add(tw["user"]["id"])
			bidenri.add(tw["user"]["id"])
		elif(district == "ri2"):
			bidenri2.add(tw["user"]["id"])
			bidenri.add(tw["user"]["id"])
		elif(district == "mn1"):
			bidenmn1.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn2"):
			bidenmn2.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn3"):
			bidenmn3.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn4"):
			bidenmn4.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn5"):
			bidenmn5.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn6"):
			bidenmn6.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn7"):
			bidenmn7.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn8"):
			bidenmn8.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mi1"):
			bidenmi1.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi2"):
			bidenmi2.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi3"):
			bidenmi3.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi4"):
			bidenmi4.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi5"):
			bidenmi5.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi6"):
			bidenmi6.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi7"):
			bidenmi7.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi8"):
			bidenmi8.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi9"):
			bidenmi9.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi10"):
			bidenmi10.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi11"):
			bidenmi11.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi12"):
			bidenmi12.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi13"):
			bidenmi13.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi14"):
			bidenmi14.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "wi1"):
			bidenwi1.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi2"):
			bidenwi2.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi3"):
			bidenwi3.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi4"):
			bidenwi4.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi5"):
			bidenwi5.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi6"):
			bidenwi6.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi7"):
			bidenwi7.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi8"):
			bidenwi8.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "or1"):
			bidenor1.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or2"):
			bidenor2.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or3"):
			bidenor3.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or4"):
			bidenor4.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or5"):
			bidenor5.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "md1"):
			bidenmd1.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md2"):
			bidenmd2.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md3"):
			bidenmd3.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md4"):
			bidenmd4.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md5"):
			bidenmd5.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md6"):
			bidenmd6.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md7"):
			bidenmd7.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md8"):
			bidenmd8.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "ma1"):
			bidenma1.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma2"):
			bidenma2.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma3"):
			bidenma3.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma4"):
			bidenma4.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma5"):
			bidenma5.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma6"):
			bidenma6.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma7"):
			bidenma7.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma8"):
			bidenma8.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma9"):
			bidenma9.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "me1"):
			bidenme1.add(tw["user"]["id"])
			bidenme.add(tw["user"]["id"])
		elif(district == "me2"):
			bidenme2.add(tw["user"]["id"])
			bidenme.add(tw["user"]["id"])
		elif(district == "id1"):
			bidenid1.add(tw["user"]["id"])
			bidenid.add(tw["user"]["id"])
		elif(district == "id2"):
			bidenid2.add(tw["user"]["id"])
			bidenid.add(tw["user"]["id"])
		elif(district == "nc1"):
			bidennc1.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc2"):
			bidennc2.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc3"):
			bidennc3.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc4"):
			bidennc4.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc5"):
			bidennc5.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc6"):
			bidennc6.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc7"):
			bidennc7.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc8"):
			bidennc8.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc9"):
			bidennc9.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc10"):
			bidennc10.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc11"):
			bidennc11.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc12"):
			bidennc12.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc13"):
			bidennc13.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nh1"):
			bidennh1.add(tw["user"]["id"])
			bidennh.add(tw["user"]["id"])
		elif(district == "nh2"):
			bidennh2.add(tw["user"]["id"])
			bidennh.add(tw["user"]["id"])
		elif(district == "nv1"):
			bidennv1.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "nv2"):
			bidennv2.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "nv3"):
			bidennv3.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "nv4"):
			bidennv4.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "co1"):
			bidenco1.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co2"):
			bidenco2.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co3"):
			bidenco3.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co4"):
			bidenco4.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co5"):
			bidenco5.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co6"):
			bidenco6.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co7"):
			bidenco7.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "nm1"):
			bidennm1.add(tw["user"]["id"])
			bidennm.add(tw["user"]["id"])
		elif(district == "nm2"):
			bidennm2.add(tw["user"]["id"])
			bidennm.add(tw["user"]["id"])
		elif(district == "nm3"):
			bidennm3.add(tw["user"]["id"])
			bidennm.add(tw["user"]["id"])
		elif(district == "az1"):
			bidenaz1.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az2"):
			bidenaz2.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az3"):
			bidenaz3.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az4"):
			bidenaz4.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az5"):
			bidenaz5.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az6"):
			bidenaz6.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az7"):
			bidenaz7.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az8"):
			bidenaz8.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az9"):
			bidenaz9.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "ga1"):
			bidenga1.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga2"):
			bidenga2.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga3"):
			bidenga3.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga4"):
			bidenga4.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga5"):
			bidenga5.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga6"):
			bidenga6.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga7"):
			bidenga7.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga8"):
			bidenga8.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga9"):
			bidenga9.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga10"):
			bidenga10.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga11"):
			bidenga11.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga12"):
			bidenga12.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga13"):
			bidenga13.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga14"):
			bidenga14.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "tx1"):
			bidentx1.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx2"):
			bidentx2.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx3"):
			bidentx3.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx4"):
			bidentx4.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx5"):
			bidentx5.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx6"):
			bidentx6.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx7"):
			bidentx7.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx8"):
			bidentx8.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx9"):
			bidentx9.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx10"):
			bidentx10.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx11"):
			bidentx11.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx12"):
			bidentx12.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx13"):
			bidentx13.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx14"):
			bidentx14.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx15"):
			bidentx15.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx16"):
			bidentx16.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx17"):
			bidentx17.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx18"):
			bidentx18.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx19"):
			bidentx19.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx20"):
			bidentx20.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx21"):
			bidentx21.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx22"):
			bidentx22.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx23"):
			bidentx23.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx24"):
			bidentx24.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx25"):
			bidentx25.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx26"):
			bidentx26.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx27"):
			bidentx27.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx28"):
			bidentx28.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx29"):
			bidentx29.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx30"):
			bidentx30.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx31"):
			bidentx31.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx32"):
			bidentx32.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx33"):
			bidentx33.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx34"):
			bidentx34.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx35"):
			bidentx35.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx36"):
			bidentx36.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "in1"):
			bidenin1.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in2"):
			bidenin2.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in3"):
			bidenin3.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in4"):
			bidenin4.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in5"):
			bidenin5.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in6"):
			bidenin6.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in7"):
			bidenin7.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in8"):
			bidenin8.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in9"):
			bidenin9.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "va1"):
			bidenva1.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va2"):
			bidenva2.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va3"):
			bidenva3.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va4"):
			bidenva4.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va5"):
			bidenva5.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va6"):
			bidenva6.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va7"):
			bidenva7.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va8"):
			bidenva8.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va9"):
			bidenva9.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va10"):
			bidenva10.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va11"):
			bidenva11.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "il1"):
			bidenil1.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il2"):
			bidenil2.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il3"):
			bidenil3.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il4"):
			bidenil4.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il5"):
			bidenil5.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il6"):
			bidenil6.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il7"):
			bidenil7.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il8"):
			bidenil8.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il9"):
			bidenil9.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il10"):
			bidenil10.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il11"):
			bidenil11.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il12"):
			bidenil12.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il13"):
			bidenil13.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il14"):
			bidenil14.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il15"):
			bidenil15.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il16"):
			bidenil16.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il17"):
			bidenil17.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il18"):
			bidenil18.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "de1"):
			bidende1.add(tw["user"]["id"])
			bidende.add(tw["user"]["id"])
		elif(district == "vt1"):
			bidenvt1.add(tw["user"]["id"])
			bidenvt.add(tw["user"]["id"])
		elif(district == "ut1"):
			bidenut1.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ut2"):
			bidenut2.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ut3"):
			bidenut3.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ut4"):
			bidenut4.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ne1"):
			bidenne1.add(tw["user"]["id"])
			bidenne.add(tw["user"]["id"])
		elif(district == "ne2"):
			bidenne2.add(tw["user"]["id"])
			bidenne.add(tw["user"]["id"])
		elif(district == "ne3"):
			bidenne3.add(tw["user"]["id"])
			bidenne.add(tw["user"]["id"])
		elif(district == "ak1"):
			bidenak1.add(tw["user"]["id"])
			bidenak.add(tw["user"]["id"])
		elif(district == "wy1"):
			bidenwy1.add(tw["user"]["id"])
			bidenwy.add(tw["user"]["id"])
		elif(district == "al1"):
			bidenal1.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al2"):
			bidenal2.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al3"):
			bidenal3.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al4"):
			bidenal4.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al5"):
			bidenal5.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al6"):
			bidenal6.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al7"):
			bidenal7.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "tn1"):
			bidentn1.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn2"):
			bidentn2.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn3"):
			bidentn3.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn4"):
			bidentn4.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn5"):
			bidentn5.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn6"):
			bidentn6.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn7"):
			bidentn7.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn8"):
			bidentn8.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn9"):
			bidentn9.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "nd1"):
			bidennd1.add(tw["user"]["id"])
			bidennd.add(tw["user"]["id"])
		elif(district == "sd1"):
			bidensd1.add(tw["user"]["id"])
			bidensd.add(tw["user"]["id"])
		elif(district == "wv1"):
			bidenwv1.add(tw["user"]["id"])
			bidenwv.add(tw["user"]["id"])
		elif(district == "wv2"):
			bidenwv2.add(tw["user"]["id"])
			bidenwv.add(tw["user"]["id"])
		elif(district == "wv3"):
			bidenwv3.add(tw["user"]["id"])
			bidenwv.add(tw["user"]["id"])
		elif(district == "ar1"):
			bidenar1.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])
		elif(district == "ar2"):
			bidenar2.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])
		elif(district == "ar3"):
			bidenar3.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])
		elif(district == "ar4"):
			bidenar4.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])

cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
	district = sortloc("#trump2020", tw["user"]["location"], tw["full_text"].lower())
	if(district != "null"):
		if(district == "mo1"):
			trumpmo1.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo2"):
			trumpmo2.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo3"):
			trumpmo3.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo4"):
			trumpmo4.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo5"):
			trumpmo5.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo6"):
			trumpmo6.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo7"):
			trumpmo7.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "mo8"):
			trumpmo8.add(tw["user"]["id"])
			trumpmo.add(tw["user"]["id"])
		elif(district == "sc1"):
			trumpsc1.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc2"):
			trumpsc2.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc3"):
			trumpsc3.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc4"):
			trumpsc4.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc5"):
			trumpsc5.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc6"):
			trumpsc6.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "sc7"):
			trumpsc7.add(tw["user"]["id"])
			trumpsc.add(tw["user"]["id"])
		elif(district == "ky1"):
			trumpky1.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky2"):
			trumpky2.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky3"):
			trumpky3.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky4"):
			trumpky4.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky5"):
			trumpky5.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ky6"):
			trumpky6.add(tw["user"]["id"])
			trumpky.add(tw["user"]["id"])
		elif(district == "ok1"):
			trumpok1.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok2"):
			trumpok2.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok3"):
			trumpok3.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok4"):
			trumpok4.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ok5"):
			trumpok5.add(tw["user"]["id"])
			trumpok.add(tw["user"]["id"])
		elif(district == "ia1"):
			trumpia1.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ia2"):
			trumpia2.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ia3"):
			trumpia3.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ia4"):
			trumpia4.add(tw["user"]["id"])
			trumpia.add(tw["user"]["id"])
		elif(district == "ks1"):
			trumpks1.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ks2"):
			trumpks2.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ks3"):
			trumpks3.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ks4"):
			trumpks4.add(tw["user"]["id"])
			trumpks.add(tw["user"]["id"])
		elif(district == "ca1"):
			trumpca1.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca2"):
			trumpca2.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca3"):
			trumpca3.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca4"):
			trumpca4.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca5"):
			trumpca5.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca6"):
			trumpca6.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca7"):
			trumpca7.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca8"):
			trumpca8.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca9"):
			trumpca9.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca10"):
			trumpca10.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca11"):
			trumpca11.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca12"):
			trumpca12.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca13"):
			trumpca13.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca14"):
			trumpca14.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca15"):
			trumpca15.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca16"):
			trumpca16.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca17"):
			trumpca17.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca18"):
			trumpca18.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca19"):
			trumpca19.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca20"):
			trumpca20.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca21"):
			trumpca21.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca22"):
			trumpca22.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca23"):
			trumpca23.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca24"):
			trumpca24.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca25"):
			trumpca25.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca26"):
			trumpca26.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca27"):
			trumpca27.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca28"):
			trumpca28.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca29"):
			trumpca29.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca30"):
			trumpca30.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca31"):
			trumpca31.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca32"):
			trumpca32.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca33"):
			trumpca33.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca34"):
			trumpca34.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca35"):
			trumpca35.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca36"):
			trumpca36.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca37"):
			trumpca37.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca38"):
			trumpca38.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca39"):
			trumpca39.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca40"):
			trumpca40.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca41"):
			trumpca41.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca42"):
			trumpca42.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca43"):
			trumpca43.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca44"):
			trumpca44.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca45"):
			trumpca45.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca46"):
			trumpca46.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca47"):
			trumpca47.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca48"):
			trumpca48.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca49"):
			trumpca49.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca50"):
			trumpca50.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca51"):
			trumpca51.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca52"):
			trumpca52.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "ca53"):
			trumpca53.add(tw["user"]["id"])
			trumpca.add(tw["user"]["id"])
		elif(district == "la1"):
			trumpla1.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la2"):
			trumpla2.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la3"):
			trumpla3.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la4"):
			trumpla4.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la5"):
			trumpla5.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "la6"):
			trumpla6.add(tw["user"]["id"])
			trumpla.add(tw["user"]["id"])
		elif(district == "ct1"):
			trumpct1.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct2"):
			trumpct2.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct3"):
			trumpct3.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct4"):
			trumpct4.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "ct5"):
			trumpct5.add(tw["user"]["id"])
			trumpct.add(tw["user"]["id"])
		elif(district == "mt1"):
			trumpmt1.add(tw["user"]["id"])
			trumpmt.add(tw["user"]["id"])
		elif(district == "ms1"):
			trumpms1.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "ms2"):
			trumpms2.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "ms3"):
			trumpms3.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "ms4"):
			trumpms4.add(tw["user"]["id"])
			trumpms.add(tw["user"]["id"])
		elif(district == "pa1"):
			trumppa1.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa2"):
			trumppa2.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa3"):
			trumppa3.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa4"):
			trumppa4.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa5"):
			trumppa5.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa6"):
			trumppa6.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa7"):
			trumppa7.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa8"):
			trumppa8.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa9"):
			trumppa9.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa10"):
			trumppa10.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa11"):
			trumppa11.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa12"):
			trumppa12.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa13"):
			trumppa13.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa14"):
			trumppa14.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa15"):
			trumppa15.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa16"):
			trumppa16.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa17"):
			trumppa17.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "pa18"):
			trumppa18.add(tw["user"]["id"])
			trumppa.add(tw["user"]["id"])
		elif(district == "oh1"):
			trumpoh1.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh2"):
			trumpoh2.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh3"):
			trumpoh3.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh4"):
			trumpoh4.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh5"):
			trumpoh5.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		if(district == "oh6"):
			trumpoh6.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh7"):
			trumpoh7.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh8"):
			trumpoh8.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh9"):
			trumpoh9.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh10"):
			trumpoh10.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh11"):
			trumpoh11.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh12"):
			trumpoh12.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh13"):
			trumpoh13.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh14"):
			trumpoh14.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh15"):
			trumpoh15.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "oh16"):
			trumpoh16.add(tw["user"]["id"])
			trumpoh.add(tw["user"]["id"])
		elif(district == "fl1"):
			trumpfl1.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl2"):
			trumpfl2.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl3"):
			trumpfl3.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl4"):
			trumpfl4.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl5"):
			trumpfl5.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl6"):
			trumpfl6.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl7"):
			trumpfl7.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl8"):
			trumpfl8.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl9"):
			trumpfl9.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl10"):
			trumpfl10.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl11"):
			trumpfl11.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl12"):
			trumpfl12.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl13"):
			trumpfl13.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl14"):
			trumpfl14.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl15"):
			trumpfl15.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl16"):
			trumpfl16.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl17"):
			trumpfl17.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl18"):
			trumpfl18.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl19"):
			trumpfl19.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl20"):
			trumpfl20.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl21"):
			trumpfl21.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl22"):
			trumpfl22.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl23"):
			trumpfl23.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl24"):
			trumpfl24.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl25"):
			trumpfl25.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl26"):
			trumpfl26.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "fl27"):
			trumpfl27.add(tw["user"]["id"])
			trumpfl.add(tw["user"]["id"])
		elif(district == "wa1"):
			trumpwa1.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa2"):
			trumpwa2.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa3"):
			trumpwa3.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa4"):
			trumpwa4.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa5"):
			trumpwa5.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa6"):
			trumpwa6.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa7"):
			trumpwa7.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa8"):
			trumpwa8.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa9"):
			trumpwa9.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "wa10"):
			trumpwa10.add(tw["user"]["id"])
			trumpwa.add(tw["user"]["id"])
		elif(district == "hi1"):
			trumphi1.add(tw["user"]["id"])
			trumphi.add(tw["user"]["id"])
		elif(district == "hi2"):
			trumphi2.add(tw["user"]["id"])
			trumphi.add(tw["user"]["id"])
		elif(district == "nj1"):
			trumpnj1.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj2"):
			trumpnj2.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj3"):
			trumpnj3.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj4"):
			trumpnj4.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj5"):
			trumpnj5.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj6"):
			trumpnj6.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj7"):
			trumpnj7.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj8"):
			trumpnj8.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj9"):
			trumpnj9.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj10"):
			trumpnj10.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj11"):
			trumpnj11.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "nj12"):
			trumpnj12.add(tw["user"]["id"])
			trumpnj.add(tw["user"]["id"])
		elif(district == "ny1"):
			trumpny1.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny2"):
			trumpny2.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny3"):
			trumpny3.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny4"):
			trumpny4.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny5"):
			trumpny5.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny6" or district == "ny7" or district == "ny8" or district == "ny9" or district == "ny10" or district == "ny11" or district == "ny12" or district == "ny13" or district == "ny14" or district == "ny15"):
			trumpny6.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny7.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny8.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny9.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny10.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny11.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny12.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny13.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny14.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
			trumpny15.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny16"):
			trumpny16.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny17"):
			trumpny17.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny18"):
			trumpny18.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny19"):
			trumpny19.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny20"):
			trumpny20.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny21"):
			trumpny21.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny22"):
			trumpny22.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny23"):
			trumpny23.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny24"):
			trumpny24.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny25"):
			trumpny25.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny26"):
			trumpny26.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ny27"):
			trumpny27.add(tw["user"]["id"])
			trumpny.add(tw["user"]["id"])
		elif(district == "ri1"):
			trumpri1.add(tw["user"]["id"])
			trumpri.add(tw["user"]["id"])
		elif(district == "ri2"):
			trumpri2.add(tw["user"]["id"])
			trumpri.add(tw["user"]["id"])
		elif(district == "mn1"):
			trumpmn1.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn2"):
			trumpmn2.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn3"):
			trumpmn3.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn4"):
			trumpmn4.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn5"):
			trumpmn5.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn6"):
			trumpmn6.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn7"):
			trumpmn7.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mn8"):
			trumpmn8.add(tw["user"]["id"])
			trumpmn.add(tw["user"]["id"])
		elif(district == "mi1"):
			trumpmi1.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi2"):
			trumpmi2.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi3"):
			trumpmi3.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi4"):
			trumpmi4.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi5"):
			trumpmi5.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi6"):
			trumpmi6.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi7"):
			trumpmi7.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi8"):
			trumpmi8.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi9"):
			trumpmi9.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi10"):
			trumpmi10.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi11"):
			trumpmi11.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi12"):
			trumpmi12.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi13"):
			trumpmi13.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "mi14"):
			trumpmi14.add(tw["user"]["id"])
			trumpmi.add(tw["user"]["id"])
		elif(district == "wi1"):
			trumpwi1.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi2"):
			trumpwi2.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi3"):
			trumpwi3.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi4"):
			trumpwi4.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi5"):
			trumpwi5.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi6"):
			trumpwi6.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi7"):
			trumpwi7.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "wi8"):
			trumpwi8.add(tw["user"]["id"])
			trumpwi.add(tw["user"]["id"])
		elif(district == "or1"):
			trumpor1.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or2"):
			trumpor2.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or3"):
			trumpor3.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or4"):
			trumpor4.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "or5"):
			trumpor5.add(tw["user"]["id"])
			trumpor.add(tw["user"]["id"])
		elif(district == "md1"):
			trumpmd1.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md2"):
			trumpmd2.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md3"):
			trumpmd3.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md4"):
			trumpmd4.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md5"):
			trumpmd5.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md6"):
			trumpmd6.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md7"):
			trumpmd7.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "md8"):
			trumpmd8.add(tw["user"]["id"])
			trumpmd.add(tw["user"]["id"])
		elif(district == "ma1"):
			trumpma1.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma2"):
			trumpma2.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma3"):
			trumpma3.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma4"):
			trumpma4.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma5"):
			trumpma5.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma6"):
			trumpma6.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma7"):
			trumpma7.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma8"):
			trumpma8.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "ma9"):
			trumpma9.add(tw["user"]["id"])
			trumpma.add(tw["user"]["id"])
		elif(district == "me1"):
			trumpme1.add(tw["user"]["id"])
			trumpme.add(tw["user"]["id"])
		elif(district == "me2"):
			trumpme2.add(tw["user"]["id"])
			trumpme.add(tw["user"]["id"])
		elif(district == "id1"):
			trumpid1.add(tw["user"]["id"])
			trumpid.add(tw["user"]["id"])
		elif(district == "id2"):
			trumpid2.add(tw["user"]["id"])
			trumpid.add(tw["user"]["id"])
		elif(district == "nc1"):
			trumpnc1.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc2"):
			trumpnc2.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc3"):
			trumpnc3.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc4"):
			trumpnc4.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc5"):
			trumpnc5.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc6"):
			trumpnc6.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc7"):
			trumpnc7.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc8"):
			trumpnc8.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc9"):
			trumpnc9.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc10"):
			trumpnc10.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc11"):
			trumpnc11.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc12"):
			trumpnc12.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nc13"):
			trumpnc13.add(tw["user"]["id"])
			trumpnc.add(tw["user"]["id"])
		elif(district == "nh1"):
			trumpnh1.add(tw["user"]["id"])
			trumpnh.add(tw["user"]["id"])
		elif(district == "nh2"):
			trumpnh2.add(tw["user"]["id"])
			trumpnh.add(tw["user"]["id"])
		elif(district == "nv1"):
			trumpnv1.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "nv2"):
			trumpnv2.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "nv3"):
			trumpnv3.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "nv4"):
			trumpnv4.add(tw["user"]["id"])
			trumpnv.add(tw["user"]["id"])
		elif(district == "co1"):
			trumpco1.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co2"):
			trumpco2.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co3"):
			trumpco3.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co4"):
			trumpco4.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co5"):
			trumpco5.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co6"):
			trumpco6.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "co7"):
			trumpco7.add(tw["user"]["id"])
			trumpco.add(tw["user"]["id"])
		elif(district == "nm1"):
			trumpnm1.add(tw["user"]["id"])
			trumpnm.add(tw["user"]["id"])
		elif(district == "nm2"):
			trumpnm2.add(tw["user"]["id"])
			trumpnm.add(tw["user"]["id"])
		elif(district == "nm3"):
			trumpnm3.add(tw["user"]["id"])
			trumpnm.add(tw["user"]["id"])
		elif(district == "az1"):
			trumpaz1.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az2"):
			trumpaz2.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az3"):
			trumpaz3.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az4"):
			trumpaz4.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az5"):
			trumpaz5.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az6"):
			trumpaz6.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az7"):
			trumpaz7.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az8"):
			trumpaz8.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "az9"):
			trumpaz9.add(tw["user"]["id"])
			trumpaz.add(tw["user"]["id"])
		elif(district == "ga1"):
			trumpga1.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga2"):
			trumpga2.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga3"):
			trumpga3.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga4"):
			trumpga4.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga5"):
			trumpga5.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga6"):
			trumpga6.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga7"):
			trumpga7.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga8"):
			trumpga8.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga9"):
			trumpga9.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga10"):
			trumpga10.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga11"):
			trumpga11.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga12"):
			trumpga12.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga13"):
			trumpga13.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "ga14"):
			trumpga14.add(tw["user"]["id"])
			trumpga.add(tw["user"]["id"])
		elif(district == "tx1"):
			trumptx1.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx2"):
			trumptx2.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx3"):
			trumptx3.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx4"):
			trumptx4.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx5"):
			trumptx5.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx6"):
			trumptx6.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx7"):
			trumptx7.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx8"):
			trumptx8.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx9"):
			trumptx9.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx10"):
			trumptx10.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx11"):
			trumptx11.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx12"):
			trumptx12.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx13"):
			trumptx13.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx14"):
			trumptx14.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx15"):
			trumptx15.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx16"):
			trumptx16.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx17"):
			trumptx17.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx18"):
			trumptx18.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx19"):
			trumptx19.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx20"):
			trumptx20.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx21"):
			trumptx21.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx22"):
			trumptx22.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx23"):
			trumptx23.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx24"):
			trumptx24.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx25"):
			trumptx25.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx26"):
			trumptx26.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx27"):
			trumptx27.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx28"):
			trumptx28.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx29"):
			trumptx29.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx30"):
			trumptx30.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx31"):
			trumptx31.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx32"):
			trumptx32.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx33"):
			trumptx33.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx34"):
			trumptx34.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx35"):
			trumptx35.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "tx36"):
			trumptx36.add(tw["user"]["id"])
			trumptx.add(tw["user"]["id"])
		elif(district == "in1"):
			trumpin1.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in2"):
			trumpin2.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in3"):
			trumpin3.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in4"):
			trumpin4.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in5"):
			trumpin5.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in6"):
			trumpin6.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in7"):
			trumpin7.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in8"):
			trumpin8.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "in9"):
			trumpin9.add(tw["user"]["id"])
			trumpin.add(tw["user"]["id"])
		elif(district == "va1"):
			trumpva1.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va2"):
			trumpva2.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va3"):
			trumpva3.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va4"):
			trumpva4.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va5"):
			trumpva5.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va6"):
			trumpva6.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va7"):
			trumpva7.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va8"):
			trumpva8.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va9"):
			trumpva9.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va10"):
			trumpva10.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "va11"):
			trumpva11.add(tw["user"]["id"])
			trumpva.add(tw["user"]["id"])
		elif(district == "il1"):
			trumpil1.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il2"):
			trumpil2.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il3"):
			trumpil3.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il4"):
			trumpil4.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il5"):
			trumpil5.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il6"):
			trumpil6.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il7"):
			trumpil7.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il8"):
			trumpil8.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il9"):
			trumpil9.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il10"):
			trumpil10.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il11"):
			trumpil11.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il12"):
			trumpil12.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il13"):
			trumpil13.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il14"):
			trumpil14.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il15"):
			trumpil15.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il16"):
			trumpil16.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il17"):
			trumpil17.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "il18"):
			trumpil18.add(tw["user"]["id"])
			trumpil.add(tw["user"]["id"])
		elif(district == "de1"):
			trumpde1.add(tw["user"]["id"])
			trumpde.add(tw["user"]["id"])
		elif(district == "vt1"):
			trumpvt1.add(tw["user"]["id"])
			trumpvt.add(tw["user"]["id"])
		elif(district == "ut1"):
			trumput1.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ut2"):
			trumput2.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ut3"):
			trumput3.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ut4"):
			trumput4.add(tw["user"]["id"])
			trumput.add(tw["user"]["id"])
		elif(district == "ne1"):
			trumpne1.add(tw["user"]["id"])
			trumpne.add(tw["user"]["id"])
		elif(district == "ne2"):
			trumpne2.add(tw["user"]["id"])
			trumpne.add(tw["user"]["id"])
		elif(district == "ne3"):
			trumpne3.add(tw["user"]["id"])
			trumpne.add(tw["user"]["id"])
		elif(district == "ak1"):
			trumpak1.add(tw["user"]["id"])
			trumpak.add(tw["user"]["id"])
		elif(district == "wy1"):
			trumpwy1.add(tw["user"]["id"])
			trumpwy.add(tw["user"]["id"])
		elif(district == "al1"):
			trumpal1.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al2"):
			trumpal2.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al3"):
			trumpal3.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al4"):
			trumpal4.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al5"):
			trumpal5.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al6"):
			trumpal6.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "al7"):
			trumpal7.add(tw["user"]["id"])
			trumpal.add(tw["user"]["id"])
		elif(district == "tn1"):
			trumptn1.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn2"):
			trumptn2.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn3"):
			trumptn3.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn4"):
			trumptn4.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn5"):
			trumptn5.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn6"):
			trumptn6.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn7"):
			trumptn7.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn8"):
			trumptn8.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "tn9"):
			trumptn9.add(tw["user"]["id"])
			trumptn.add(tw["user"]["id"])
		elif(district == "nd1"):
			trumpnd1.add(tw["user"]["id"])
			trumpnd.add(tw["user"]["id"])
		elif(district == "sd1"):
			trumpsd1.add(tw["user"]["id"])
			trumpsd.add(tw["user"]["id"])
		elif(district == "wv1"):
			trumpwv1.add(tw["user"]["id"])
			trumpwv.add(tw["user"]["id"])
		elif(district == "wv2"):
			trumpwv2.add(tw["user"]["id"])
			trumpwv.add(tw["user"]["id"])
		elif(district == "wv3"):
			trumpwv3.add(tw["user"]["id"])
			trumpwv.add(tw["user"]["id"])
		elif(district == "ar1"):
			trumpar1.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
		elif(district == "ar2"):
			trumpar2.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
		elif(district == "ar3"):
			trumpar3.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
		elif(district == "ar4"):
			trumpar4.add(tw["user"]["id"])
			trumpar.add(tw["user"]["id"])
	district = sortloc("#biden2020", tw["user"]["location"], tw["full_text"].lower())
	if(district != "null"):
		if(district == "mo1"):
			bidenmo1.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo2"):
			bidenmo2.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo3"):
			bidenmo3.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo4"):
			bidenmo4.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo5"):
			bidenmo5.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo6"):
			bidenmo6.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo7"):
			bidenmo7.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "mo8"):
			bidenmo8.add(tw["user"]["id"])
			bidenmo.add(tw["user"]["id"])
		elif(district == "sc1"):
			bidensc1.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc2"):
			bidensc2.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc3"):
			bidensc3.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc4"):
			bidensc4.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc5"):
			bidensc5.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc6"):
			bidensc6.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "sc7"):
			bidensc7.add(tw["user"]["id"])
			bidensc.add(tw["user"]["id"])
		elif(district == "ky1"):
			bidenky1.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky2"):
			bidenky2.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky3"):
			bidenky3.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky4"):
			bidenky4.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky5"):
			bidenky5.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ky6"):
			bidenky6.add(tw["user"]["id"])
			bidenky.add(tw["user"]["id"])
		elif(district == "ok1"):
			bidenok1.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok2"):
			bidenok2.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok3"):
			bidenok3.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok4"):
			bidenok4.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ok5"):
			bidenok5.add(tw["user"]["id"])
			bidenok.add(tw["user"]["id"])
		elif(district == "ia1"):
			bidenia1.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ia2"):
			bidenia2.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ia3"):
			bidenia3.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ia4"):
			bidenia4.add(tw["user"]["id"])
			bidenia.add(tw["user"]["id"])
		elif(district == "ks1"):
			bidenks1.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ks2"):
			bidenks2.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ks3"):
			bidenks3.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ks4"):
			bidenks4.add(tw["user"]["id"])
			bidenks.add(tw["user"]["id"])
		elif(district == "ca1"):
			bidenca1.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca2"):
			bidenca2.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca3"):
			bidenca3.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca4"):
			bidenca4.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca5"):
			bidenca5.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca6"):
			bidenca6.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca7"):
			bidenca7.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca8"):
			bidenca8.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca9"):
			bidenca9.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca10"):
			bidenca10.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca11"):
			bidenca11.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca12"):
			bidenca12.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca13"):
			bidenca13.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca14"):
			bidenca14.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca15"):
			bidenca15.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca16"):
			bidenca16.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca17"):
			bidenca17.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca18"):
			bidenca18.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca19"):
			bidenca19.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca20"):
			bidenca20.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca21"):
			bidenca21.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca22"):
			bidenca22.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca23"):
			bidenca23.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca24"):
			bidenca24.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca25"):
			bidenca25.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca26"):
			bidenca26.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca27"):
			bidenca27.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca28"):
			bidenca28.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca29"):
			bidenca29.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca30"):
			bidenca30.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca31"):
			bidenca31.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca32"):
			bidenca32.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca33"):
			bidenca33.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca34"):
			bidenca34.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca35"):
			bidenca35.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca36"):
			bidenca36.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca37"):
			bidenca37.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca38"):
			bidenca38.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca39"):
			bidenca39.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca40"):
			bidenca40.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca41"):
			bidenca41.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca42"):
			bidenca42.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca43"):
			bidenca43.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca44"):
			bidenca44.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca45"):
			bidenca45.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca46"):
			bidenca46.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca47"):
			bidenca47.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca48"):
			bidenca48.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca49"):
			bidenca49.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca50"):
			bidenca50.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca51"):
			bidenca51.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca52"):
			bidenca52.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "ca53"):
			bidenca53.add(tw["user"]["id"])
			bidenca.add(tw["user"]["id"])
		elif(district == "la1"):
			bidenla1.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la2"):
			bidenla2.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la3"):
			bidenla3.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la4"):
			bidenla4.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la5"):
			bidenla5.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "la6"):
			bidenla6.add(tw["user"]["id"])
			bidenla.add(tw["user"]["id"])
		elif(district == "ct1"):
			bidenct1.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct2"):
			bidenct2.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct3"):
			bidenct3.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct4"):
			bidenct4.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "ct5"):
			bidenct5.add(tw["user"]["id"])
			bidenct.add(tw["user"]["id"])
		elif(district == "mt1"):
			bidenmt1.add(tw["user"]["id"])
			bidenmt.add(tw["user"]["id"])
		elif(district == "ms1"):
			bidenms1.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "ms2"):
			bidenms2.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "ms3"):
			bidenms3.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "ms4"):
			bidenms4.add(tw["user"]["id"])
			bidenms.add(tw["user"]["id"])
		elif(district == "pa1"):
			bidenpa1.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa2"):
			bidenpa2.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa3"):
			bidenpa3.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa4"):
			bidenpa4.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa5"):
			bidenpa5.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa6"):
			bidenpa6.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa7"):
			bidenpa7.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa8"):
			bidenpa8.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa9"):
			bidenpa9.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa10"):
			bidenpa10.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa11"):
			bidenpa11.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa12"):
			bidenpa12.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa13"):
			bidenpa13.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa14"):
			bidenpa14.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa15"):
			bidenpa15.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa16"):
			bidenpa16.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa17"):
			bidenpa17.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "pa18"):
			bidenpa18.add(tw["user"]["id"])
			bidenpa.add(tw["user"]["id"])
		elif(district == "oh1"):
			bidenoh1.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh2"):
			bidenoh2.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh3"):
			bidenoh3.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh4"):
			bidenoh4.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh5"):
			bidenoh5.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		if(district == "oh6"):
			bidenoh6.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh7"):
			bidenoh7.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh8"):
			bidenoh8.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh9"):
			bidenoh9.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh10"):
			bidenoh10.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh11"):
			bidenoh11.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh12"):
			bidenoh12.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh13"):
			bidenoh13.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh14"):
			bidenoh14.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh15"):
			bidenoh15.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "oh16"):
			bidenoh16.add(tw["user"]["id"])
			bidenoh.add(tw["user"]["id"])
		elif(district == "fl1"):
			bidenfl1.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl2"):
			bidenfl2.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl3"):
			bidenfl3.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl4"):
			bidenfl4.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl5"):
			bidenfl5.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl6"):
			bidenfl6.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl7"):
			bidenfl7.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl8"):
			bidenfl8.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl9"):
			bidenfl9.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl10"):
			bidenfl10.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl11"):
			bidenfl11.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl12"):
			bidenfl12.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl13"):
			bidenfl13.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl14"):
			bidenfl14.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl15"):
			bidenfl15.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl16"):
			bidenfl16.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl17"):
			bidenfl17.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl18"):
			bidenfl18.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl19"):
			bidenfl19.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl20"):
			bidenfl20.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl21"):
			bidenfl21.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl22"):
			bidenfl22.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl23"):
			bidenfl23.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl24"):
			bidenfl24.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl25"):
			bidenfl25.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl26"):
			bidenfl26.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "fl27"):
			bidenfl27.add(tw["user"]["id"])
			bidenfl.add(tw["user"]["id"])
		elif(district == "wa1"):
			bidenwa1.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa2"):
			bidenwa2.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa3"):
			bidenwa3.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa4"):
			bidenwa4.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa5"):
			bidenwa5.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa6"):
			bidenwa6.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa7"):
			bidenwa7.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa8"):
			bidenwa8.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa9"):
			bidenwa9.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "wa10"):
			bidenwa10.add(tw["user"]["id"])
			bidenwa.add(tw["user"]["id"])
		elif(district == "hi1"):
			bidenhi1.add(tw["user"]["id"])
			bidenhi.add(tw["user"]["id"])
		elif(district == "hi2"):
			bidenhi2.add(tw["user"]["id"])
			bidenhi.add(tw["user"]["id"])
		elif(district == "nj1"):
			bidennj1.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj2"):
			bidennj2.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj3"):
			bidennj3.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj4"):
			bidennj4.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj5"):
			bidennj5.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj6"):
			bidennj6.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj7"):
			bidennj7.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj8"):
			bidennj8.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj9"):
			bidennj9.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj10"):
			bidennj10.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj11"):
			bidennj11.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "nj12"):
			bidennj12.add(tw["user"]["id"])
			bidennj.add(tw["user"]["id"])
		elif(district == "ny1"):
			bidenny1.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny2"):
			bidenny2.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny3"):
			bidenny3.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny4"):
			bidenny4.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny5"):
			bidenny5.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny6" or district == "ny7" or district == "ny8" or district == "ny9" or district == "ny10" or district == "ny11" or district == "ny12" or district == "ny13" or district == "ny14" or district == "ny15"):
			bidenny6.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny7.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny8.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny9.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny10.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny11.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny12.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny13.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny14.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
			bidenny15.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny16"):
			bidenny16.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny17"):
			bidenny17.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny18"):
			bidenny18.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny19"):
			bidenny19.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny20"):
			bidenny20.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny21"):
			bidenny21.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny22"):
			bidenny22.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny23"):
			bidenny23.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny24"):
			bidenny24.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny25"):
			bidenny25.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny26"):
			bidenny26.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ny27"):
			bidenny27.add(tw["user"]["id"])
			bidenny.add(tw["user"]["id"])
		elif(district == "ri1"):
			bidenri1.add(tw["user"]["id"])
			bidenri.add(tw["user"]["id"])
		elif(district == "ri2"):
			bidenri2.add(tw["user"]["id"])
			bidenri.add(tw["user"]["id"])
		elif(district == "mn1"):
			bidenmn1.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn2"):
			bidenmn2.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn3"):
			bidenmn3.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn4"):
			bidenmn4.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn5"):
			bidenmn5.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn6"):
			bidenmn6.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn7"):
			bidenmn7.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mn8"):
			bidenmn8.add(tw["user"]["id"])
			bidenmn.add(tw["user"]["id"])
		elif(district == "mi1"):
			bidenmi1.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi2"):
			bidenmi2.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi3"):
			bidenmi3.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi4"):
			bidenmi4.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi5"):
			bidenmi5.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi6"):
			bidenmi6.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi7"):
			bidenmi7.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi8"):
			bidenmi8.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi9"):
			bidenmi9.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi10"):
			bidenmi10.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi11"):
			bidenmi11.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi12"):
			bidenmi12.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi13"):
			bidenmi13.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "mi14"):
			bidenmi14.add(tw["user"]["id"])
			bidenmi.add(tw["user"]["id"])
		elif(district == "wi1"):
			bidenwi1.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi2"):
			bidenwi2.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi3"):
			bidenwi3.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi4"):
			bidenwi4.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi5"):
			bidenwi5.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi6"):
			bidenwi6.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi7"):
			bidenwi7.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "wi8"):
			bidenwi8.add(tw["user"]["id"])
			bidenwi.add(tw["user"]["id"])
		elif(district == "or1"):
			bidenor1.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or2"):
			bidenor2.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or3"):
			bidenor3.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or4"):
			bidenor4.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "or5"):
			bidenor5.add(tw["user"]["id"])
			bidenor.add(tw["user"]["id"])
		elif(district == "md1"):
			bidenmd1.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md2"):
			bidenmd2.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md3"):
			bidenmd3.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md4"):
			bidenmd4.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md5"):
			bidenmd5.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md6"):
			bidenmd6.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md7"):
			bidenmd7.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "md8"):
			bidenmd8.add(tw["user"]["id"])
			bidenmd.add(tw["user"]["id"])
		elif(district == "ma1"):
			bidenma1.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma2"):
			bidenma2.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma3"):
			bidenma3.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma4"):
			bidenma4.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma5"):
			bidenma5.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma6"):
			bidenma6.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma7"):
			bidenma7.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma8"):
			bidenma8.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "ma9"):
			bidenma9.add(tw["user"]["id"])
			bidenma.add(tw["user"]["id"])
		elif(district == "me1"):
			bidenme1.add(tw["user"]["id"])
			bidenme.add(tw["user"]["id"])
		elif(district == "me2"):
			bidenme2.add(tw["user"]["id"])
			bidenme.add(tw["user"]["id"])
		elif(district == "id1"):
			bidenid1.add(tw["user"]["id"])
			bidenid.add(tw["user"]["id"])
		elif(district == "id2"):
			bidenid2.add(tw["user"]["id"])
			bidenid.add(tw["user"]["id"])
		elif(district == "nc1"):
			bidennc1.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc2"):
			bidennc2.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc3"):
			bidennc3.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc4"):
			bidennc4.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc5"):
			bidennc5.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc6"):
			bidennc6.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc7"):
			bidennc7.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc8"):
			bidennc8.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc9"):
			bidennc9.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc10"):
			bidennc10.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc11"):
			bidennc11.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc12"):
			bidennc12.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nc13"):
			bidennc13.add(tw["user"]["id"])
			bidennc.add(tw["user"]["id"])
		elif(district == "nh1"):
			bidennh1.add(tw["user"]["id"])
			bidennh.add(tw["user"]["id"])
		elif(district == "nh2"):
			bidennh2.add(tw["user"]["id"])
			bidennh.add(tw["user"]["id"])
		elif(district == "nv1"):
			bidennv1.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "nv2"):
			bidennv2.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "nv3"):
			bidennv3.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "nv4"):
			bidennv4.add(tw["user"]["id"])
			bidennv.add(tw["user"]["id"])
		elif(district == "co1"):
			bidenco1.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co2"):
			bidenco2.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co3"):
			bidenco3.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co4"):
			bidenco4.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co5"):
			bidenco5.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co6"):
			bidenco6.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "co7"):
			bidenco7.add(tw["user"]["id"])
			bidenco.add(tw["user"]["id"])
		elif(district == "nm1"):
			bidennm1.add(tw["user"]["id"])
			bidennm.add(tw["user"]["id"])
		elif(district == "nm2"):
			bidennm2.add(tw["user"]["id"])
			bidennm.add(tw["user"]["id"])
		elif(district == "nm3"):
			bidennm3.add(tw["user"]["id"])
			bidennm.add(tw["user"]["id"])
		elif(district == "az1"):
			bidenaz1.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az2"):
			bidenaz2.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az3"):
			bidenaz3.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az4"):
			bidenaz4.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az5"):
			bidenaz5.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az6"):
			bidenaz6.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az7"):
			bidenaz7.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az8"):
			bidenaz8.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "az9"):
			bidenaz9.add(tw["user"]["id"])
			bidenaz.add(tw["user"]["id"])
		elif(district == "ga1"):
			bidenga1.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga2"):
			bidenga2.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga3"):
			bidenga3.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga4"):
			bidenga4.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga5"):
			bidenga5.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga6"):
			bidenga6.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga7"):
			bidenga7.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga8"):
			bidenga8.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga9"):
			bidenga9.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga10"):
			bidenga10.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga11"):
			bidenga11.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga12"):
			bidenga12.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga13"):
			bidenga13.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "ga14"):
			bidenga14.add(tw["user"]["id"])
			bidenga.add(tw["user"]["id"])
		elif(district == "tx1"):
			bidentx1.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx2"):
			bidentx2.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx3"):
			bidentx3.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx4"):
			bidentx4.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx5"):
			bidentx5.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx6"):
			bidentx6.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx7"):
			bidentx7.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx8"):
			bidentx8.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx9"):
			bidentx9.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx10"):
			bidentx10.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx11"):
			bidentx11.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx12"):
			bidentx12.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx13"):
			bidentx13.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx14"):
			bidentx14.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx15"):
			bidentx15.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx16"):
			bidentx16.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx17"):
			bidentx17.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx18"):
			bidentx18.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx19"):
			bidentx19.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx20"):
			bidentx20.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx21"):
			bidentx21.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx22"):
			bidentx22.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx23"):
			bidentx23.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx24"):
			bidentx24.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx25"):
			bidentx25.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx26"):
			bidentx26.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx27"):
			bidentx27.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx28"):
			bidentx28.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx29"):
			bidentx29.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx30"):
			bidentx30.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx31"):
			bidentx31.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx32"):
			bidentx32.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx33"):
			bidentx33.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx34"):
			bidentx34.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx35"):
			bidentx35.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "tx36"):
			bidentx36.add(tw["user"]["id"])
			bidentx.add(tw["user"]["id"])
		elif(district == "in1"):
			bidenin1.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in2"):
			bidenin2.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in3"):
			bidenin3.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in4"):
			bidenin4.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in5"):
			bidenin5.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in6"):
			bidenin6.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in7"):
			bidenin7.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in8"):
			bidenin8.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "in9"):
			bidenin9.add(tw["user"]["id"])
			bidenin.add(tw["user"]["id"])
		elif(district == "va1"):
			bidenva1.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va2"):
			bidenva2.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va3"):
			bidenva3.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va4"):
			bidenva4.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va5"):
			bidenva5.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va6"):
			bidenva6.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va7"):
			bidenva7.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va8"):
			bidenva8.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va9"):
			bidenva9.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va10"):
			bidenva10.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "va11"):
			bidenva11.add(tw["user"]["id"])
			bidenva.add(tw["user"]["id"])
		elif(district == "il1"):
			bidenil1.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il2"):
			bidenil2.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il3"):
			bidenil3.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il4"):
			bidenil4.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il5"):
			bidenil5.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il6"):
			bidenil6.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il7"):
			bidenil7.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il8"):
			bidenil8.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il9"):
			bidenil9.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il10"):
			bidenil10.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il11"):
			bidenil11.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il12"):
			bidenil12.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il13"):
			bidenil13.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il14"):
			bidenil14.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il15"):
			bidenil15.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il16"):
			bidenil16.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il17"):
			bidenil17.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "il18"):
			bidenil18.add(tw["user"]["id"])
			bidenil.add(tw["user"]["id"])
		elif(district == "de1"):
			bidende1.add(tw["user"]["id"])
			bidende.add(tw["user"]["id"])
		elif(district == "vt1"):
			bidenvt1.add(tw["user"]["id"])
			bidenvt.add(tw["user"]["id"])
		elif(district == "ut1"):
			bidenut1.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ut2"):
			bidenut2.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ut3"):
			bidenut3.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ut4"):
			bidenut4.add(tw["user"]["id"])
			bidenut.add(tw["user"]["id"])
		elif(district == "ne1"):
			bidenne1.add(tw["user"]["id"])
			bidenne.add(tw["user"]["id"])
		elif(district == "ne2"):
			bidenne2.add(tw["user"]["id"])
			bidenne.add(tw["user"]["id"])
		elif(district == "ne3"):
			bidenne3.add(tw["user"]["id"])
			bidenne.add(tw["user"]["id"])
		elif(district == "ak1"):
			bidenak1.add(tw["user"]["id"])
			bidenak.add(tw["user"]["id"])
		elif(district == "wy1"):
			bidenwy1.add(tw["user"]["id"])
			bidenwy.add(tw["user"]["id"])
		elif(district == "al1"):
			bidenal1.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al2"):
			bidenal2.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al3"):
			bidenal3.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al4"):
			bidenal4.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al5"):
			bidenal5.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al6"):
			bidenal6.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "al7"):
			bidenal7.add(tw["user"]["id"])
			bidenal.add(tw["user"]["id"])
		elif(district == "tn1"):
			bidentn1.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn2"):
			bidentn2.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn3"):
			bidentn3.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn4"):
			bidentn4.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn5"):
			bidentn5.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn6"):
			bidentn6.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn7"):
			bidentn7.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn8"):
			bidentn8.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "tn9"):
			bidentn9.add(tw["user"]["id"])
			bidentn.add(tw["user"]["id"])
		elif(district == "nd1"):
			bidennd1.add(tw["user"]["id"])
			bidennd.add(tw["user"]["id"])
		elif(district == "sd1"):
			bidensd1.add(tw["user"]["id"])
			bidensd.add(tw["user"]["id"])
		elif(district == "wv1"):
			bidenwv1.add(tw["user"]["id"])
			bidenwv.add(tw["user"]["id"])
		elif(district == "wv2"):
			bidenwv2.add(tw["user"]["id"])
			bidenwv.add(tw["user"]["id"])
		elif(district == "wv3"):
			bidenwv3.add(tw["user"]["id"])
			bidenwv.add(tw["user"]["id"])
		elif(district == "ar1"):
			bidenar1.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])
		elif(district == "ar2"):
			bidenar2.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])
		elif(district == "ar3"):
			bidenar3.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])
		elif(district == "ar4"):
			bidenar4.add(tw["user"]["id"])
			bidenar.add(tw["user"]["id"])




print("Missouri")
print("Trump: ", (len(trumpmo)/(len(trumpmo)+len(bidenmo))))
print("Biden: ",(len(bidenmo)/(len(trumpmo)+len(bidenmo))))
print("Missouri 1")
trumpmo1votes = (len(trumpmo1)/(len(trumpmo1)+len(bidenmo1)))*292856
bidenmo1votes = (len(bidenmo1)/(len(trumpmo1)+len(bidenmo1)))*292856
print("Trump: ", (len(trumpmo1)/(len(trumpmo1)+len(bidenmo1))))
print("votes ", trumpmo1votes)
print("Biden: ",(len(bidenmo1)/(len(trumpmo1)+len(bidenmo1))))
print("votes ", bidenmo1votes)
print("Missouri 2")
trumpmo2votes = (len(trumpmo2)/(len(trumpmo2)+len(bidenmo2)))*392157
bidenmo2votes = (len(bidenmo2)/(len(trumpmo2)+len(bidenmo2)))*392157
print("Trump: ", (len(trumpmo2)/(len(trumpmo2)+len(bidenmo2))))
print("votes ", trumpmo2votes)
print("Biden: ",(len(bidenmo2)/(len(trumpmo2)+len(bidenmo2))))
print("votes ", bidenmo2votes)
print("Missouri 3")
trumpmo3votes = (len(trumpmo3)/(len(trumpmo3)+len(bidenmo3)))*351364
bidenmo3votes = (len(bidenmo3)/(len(trumpmo3)+len(bidenmo3)))*351364
print("Trump: ", (len(trumpmo3)/(len(trumpmo3)+len(bidenmo3))))
print("votes ", trumpmo3votes)
print("Biden: ",(len(bidenmo3)/(len(trumpmo3)+len(bidenmo3))))
print("votes ", bidenmo3votes)
print("Missouri 4")
trumpmo4votes = (len(trumpmo4)/(len(trumpmo4)+len(bidenmo4)))*317419
bidenmo4votes = (len(bidenmo4)/(len(trumpmo4)+len(bidenmo4)))*317419
print("Trump: ", (len(trumpmo4)/(len(trumpmo4)+len(bidenmo4))))
print("votes ", trumpmo4votes)
print("Biden: ",(len(bidenmo4)/(len(trumpmo4)+len(bidenmo4))))
print("votes ", bidenmo4votes)
print("Missouri 5")
trumpmo5votes = (len(trumpmo5)/(len(trumpmo5)+len(bidenmo5)))*307861
bidenmo5votes = (len(bidenmo5)/(len(trumpmo5)+len(bidenmo5)))*307861
print("Trump: ", (len(trumpmo5)/(len(trumpmo5)+len(bidenmo5))))
print("votes ", trumpmo5votes)
print("Biden: ",(len(bidenmo5)/(len(trumpmo5)+len(bidenmo5))))
print("votes ", bidenmo5votes)
print("Missouri 6")
trumpmo6votes = (len(trumpmo6)/(len(trumpmo6)+len(bidenmo6)))*335526
bidenmo6votes = (len(bidenmo6)/(len(trumpmo6)+len(bidenmo6)))*335526
print("Trump: ", (len(trumpmo6)/(len(trumpmo6)+len(bidenmo6))))
print("votes ", trumpmo6votes)
print("Biden: ",(len(bidenmo6)/(len(trumpmo6)+len(bidenmo6))))
print("votes ", bidenmo6votes)
print("Missouri 7")
trumpmo7votes = (len(trumpmo7)/(len(trumpmo7)+len(bidenmo7)))*320391
bidenmo7votes = (len(bidenmo7)/(len(trumpmo7)+len(bidenmo7)))*320391
print("Trump: ", (len(trumpmo7)/(len(trumpmo7)+len(bidenmo7))))
print("votes ", trumpmo7votes)
print("Biden: ",(len(bidenmo7)/(len(trumpmo7)+len(bidenmo7))))
print("votes ", bidenmo7votes)
print("Missouri 8")
trumpmo8votes = (len(trumpmo8)/(len(trumpmo8)+len(bidenmo8)))*299597
bidenmo8votes = (len(bidenmo8)/(len(trumpmo8)+len(bidenmo8)))*299597
print("Trump: ", (len(trumpmo8)/(len(trumpmo8)+len(bidenmo8))))
print("votes ", trumpmo8votes)
print("Biden: ",(len(bidenmo8)/(len(trumpmo8)+len(bidenmo8))))
print("votes ", bidenmo8votes)
totalmovotestrump = trumpmo1votes+trumpmo2votes+trumpmo3votes+trumpmo4votes+trumpmo5votes+trumpmo6votes+trumpmo7votes+trumpmo8votes
totalmovotesbiden = bidenmo1votes+bidenmo2votes+bidenmo3votes+bidenmo4votes+bidenmo5votes+bidenmo6votes+bidenmo7votes+bidenmo8votes
print("TOTAL TRUMP VOTES: ", totalmovotestrump/(totalmovotestrump+totalmovotesbiden))
print("TOTAL BIDEN VOTES: ", totalmovotesbiden/(totalmovotestrump+totalmovotesbiden))
print("")
print("Colorado")
print("Trump: ", (len(trumpco)/(len(trumpco)+len(bidenco))))
print("Biden: ",(len(bidenco)/(len(trumpco)+len(bidenco))))
print("Colorado 1")
trumpco1votes = (len(trumpco1)/(len(trumpco1)+len(bidenco1)))*274515
bidenco1votes = (len(bidenco1)/(len(trumpco1)+len(bidenco1)))*274515
print("Trump: ", (len(trumpco1)/(len(trumpco1)+len(bidenco1))))
print("votes ", trumpco1votes)
print("Biden: ",(len(bidenco1)/(len(trumpco1)+len(bidenco1))))
print("votes ", bidenco1votes)
print("Colorado 2")
trumpco2votes = (len(trumpco2)/(len(trumpco2)+len(bidenco2)))*418008
bidenco2votes = (len(bidenco2)/(len(trumpco2)+len(bidenco2)))*418008
print("Trump: ", (len(trumpco2)/(len(trumpco2)+len(bidenco2))))
print("votes ", trumpco2votes)
print("Biden: ",(len(bidenco2)/(len(trumpco2)+len(bidenco2))))
print("votes ", bidenco2votes)
print("Colorado 3")
trumpco3votes = (len(trumpco3)/(len(trumpco3)+len(bidenco3)))*334711
bidenco3votes = (len(bidenco3)/(len(trumpco3)+len(bidenco3)))*334711
print("Trump: ", (len(trumpco3)/(len(trumpco3)+len(bidenco3))))
print("votes ", trumpco3votes)
print("Biden: ",(len(bidenco3)/(len(trumpco3)+len(bidenco3))))
print("votes ", bidenco3votes)
print("Colorado 4")
trumpco4votes = (len(trumpco4)/(len(trumpco4)+len(bidenco4)))*360673
bidenco4votes = (len(bidenco4)/(len(trumpco4)+len(bidenco4)))*360673
print("Trump: ", (len(trumpco4)/(len(trumpco4)+len(bidenco4))))
print("votes ", trumpco4votes)
print("Biden: ",(len(bidenco4)/(len(trumpco4)+len(bidenco4))))
print("votes ", bidenco4votes)
print("Colorado 5")
trumpco5votes = (len(trumpco5)/(len(trumpco5)+len(bidenco5)))*331742
bidenco5votes = (len(bidenco5)/(len(trumpco5)+len(bidenco5)))*331742
print("Trump: ", (len(trumpco5)/(len(trumpco5)+len(bidenco5))))
print("votes ", trumpco5votes)
print("Biden: ",(len(bidenco5)/(len(trumpco5)+len(bidenco5))))
print("votes ", bidenco5votes)
print("Colorado 6")
trumpco6votes = (len(trumpco6)/(len(trumpco6)+len(bidenco6)))*330144
bidenco6votes = (len(bidenco6)/(len(trumpco6)+len(bidenco6)))*330144
print("Trump: ", (len(trumpco6)/(len(trumpco6)+len(bidenco6))))
print("votes ", trumpco6votes)
print("Biden: ",(len(bidenco6)/(len(trumpco6)+len(bidenco6))))
print("votes ", bidenco6votes)
print("Colorado 7")
trumpco7votes = (len(trumpco7)/(len(trumpco7)+len(bidenco7)))*319452
bidenco7votes = (len(bidenco7)/(len(trumpco7)+len(bidenco7)))*319452
print("Trump: ", (len(trumpco7)/(len(trumpco7)+len(bidenco7))))
print("votes ", trumpco7votes)
print("Biden: ",(len(bidenco7)/(len(trumpco7)+len(bidenco7))))
print("votes ", bidenco7votes)
totalcovotestrump = trumpco1votes+trumpco2votes+trumpco3votes+trumpco4votes+trumpco5votes+trumpco6votes+trumpco7votes
totalcovotesbiden = bidenco1votes+bidenco2votes+bidenco3votes+bidenco4votes+bidenco5votes+bidenco6votes+bidenco7votes
print("TOTAL TRUMP VOTES: ", totalcovotestrump/(totalcovotestrump+totalcovotesbiden))
print("TOTAL BIDEN VOTES: ", totalcovotesbiden/(totalcovotestrump+totalcovotesbiden))
print("")
print("Minnesota")
print("Trump: ", (len(trumpmn)/(len(trumpmn)+len(bidenmn))))
print("Biden: ",(len(bidenmn)/(len(trumpmn)+len(bidenmn))))
print("Minnesota 1")
trumpmn1votes = (len(trumpmn1)/(len(trumpmn1)+len(bidenmn1)))*335603
bidenmn1votes = (len(bidenmn1)/(len(trumpmn1)+len(bidenmn1)))*335603
print("Trump: ", (len(trumpmn1)/(len(trumpmn1)+len(bidenmn1))))
print("votes ", trumpmn1votes)
print("Biden: ",(len(bidenmn1)/(len(trumpmn1)+len(bidenmn1))))
print("votes ", bidenmn1votes)
print("Minnesota 2")
trumpmn2votes = (len(trumpmn2)/(len(trumpmn2)+len(bidenmn2)))*341101
bidenmn2votes = (len(bidenmn2)/(len(trumpmn2)+len(bidenmn2)))*341101
print("Trump: ", (len(trumpmn2)/(len(trumpmn2)+len(bidenmn2))))
print("votes ", trumpmn2votes)
print("Biden: ",(len(bidenmn2)/(len(trumpmn2)+len(bidenmn2))))
print("votes ", bidenmn2votes)
print("Minnesota 3")
trumpmn3votes = (len(trumpmn3)/(len(trumpmn3)+len(bidenmn3)))*392313
bidenmn3votes = (len(bidenmn3)/(len(trumpmn3)+len(bidenmn3)))*392313
print("Trump: ", (len(trumpmn3)/(len(trumpmn3)+len(bidenmn3))))
print("votes ", trumpmn3votes)
print("Biden: ",(len(bidenmn3)/(len(trumpmn3)+len(bidenmn3))))
print("votes ", bidenmn3votes)
print("Minnesota 4")
trumpmn4votes = (len(trumpmn4)/(len(trumpmn4)+len(bidenmn4)))*323429
bidenmn4votes = (len(bidenmn4)/(len(trumpmn4)+len(bidenmn4)))*323429
print("Trump: ", (len(trumpmn4)/(len(trumpmn4)+len(bidenmn4))))
print("votes ", trumpmn4votes)
print("Biden: ",(len(bidenmn4)/(len(trumpmn4)+len(bidenmn4))))
print("votes ", bidenmn4votes)
print("Minnesota 5")
trumpmn5votes = (len(trumpmn5)/(len(trumpmn5)+len(bidenmn5)))*330617
bidenmn5votes = (len(bidenmn5)/(len(trumpmn5)+len(bidenmn5)))*330617
print("Trump: ", (len(trumpmn5)/(len(trumpmn5)+len(bidenmn5))))
print("votes ", trumpmn5votes)
print("Biden: ",(len(bidenmn5)/(len(trumpmn5)+len(bidenmn5))))
print("votes ", bidenmn5votes)
print("Minnesota 6")
trumpmn6votes = (len(trumpmn6)/(len(trumpmn6)+len(bidenmn6)))*358396
bidenmn6votes = (len(bidenmn6)/(len(trumpmn6)+len(bidenmn6)))*358396
print("Trump: ", (len(trumpmn6)/(len(trumpmn6)+len(bidenmn6))))
print("votes ", trumpmn6votes)
print("Biden: ",(len(bidenmn6)/(len(trumpmn6)+len(bidenmn6))))
print("votes ", bidenmn6votes)
print("Minnesota 7")
trumpmn7votes = (len(trumpmn7)/(len(trumpmn7)+len(bidenmn7)))*330521
bidenmn7votes = (len(bidenmn7)/(len(trumpmn7)+len(bidenmn7)))*330521
print("Trump: ", (len(trumpmn7)/(len(trumpmn7)+len(bidenmn7))))
print("votes ", trumpmn7votes)
print("Biden: ",(len(bidenmn7)/(len(trumpmn7)+len(bidenmn7))))
print("votes ", bidenmn7votes)
print("Minnesota 8")
trumpmn8votes = (len(trumpmn8)/(len(trumpmn8)+len(bidenmn8)))*356201
bidenmn8votes = (len(bidenmn8)/(len(trumpmn8)+len(bidenmn8)))*356201
print("Trump: ", (len(trumpmn8)/(len(trumpmn8)+len(bidenmn8))))
print("votes ", trumpmn8votes)
print("Biden: ",(len(bidenmn8)/(len(trumpmn8)+len(bidenmn8))))
print("votes ", bidenmn8votes)
totalmnvotestrump = trumpmn1votes+trumpmn2votes+trumpmn3votes+trumpmn4votes+trumpmn5votes+trumpmn6votes+trumpmn7votes+trumpmn8votes
totalmnvotesbiden = bidenmn1votes+bidenmn2votes+bidenmn3votes+bidenmn4votes+bidenmn5votes+bidenmn6votes+bidenmn7votes+bidenmn8votes
print("TOTAL TRUMP VOTES: ", totalmnvotestrump/(totalmnvotestrump+totalmnvotesbiden))
print("TOTAL BIDEN VOTES: ", totalmnvotesbiden/(totalmnvotestrump+totalmnvotesbiden))
print("")
print("Alaska")
print("Trump: ", (len(trumpak)/(len(trumpak)+len(bidenak))))
print("Biden: ",(len(bidenak)/(len(trumpak)+len(bidenak))))
print("Alaska 1")
bothak1 = trumpak1.intersection(bidenak1)
bothak1votes = (len(bothak1)/(len(trumpak1)+len(bidenak1)))
print("Trump: ", (len(trumpak1)/(len(trumpak1)+len(bidenak1)))-((len(bothak1)/(len(trumpak1)+len(bidenak1)))/2))
print("votes ", len(trumpak1))
print("Biden: ",(len(bidenak1)/(len(trumpak1)+len(bidenak1)))-((len(bothak1)/(len(trumpak1)+len(bidenak1)))/2))
print("votes ", len(bidenak1))
print("Both: ", (len(bothak1)/(len(trumpak1)+len(bidenak1))))
print("")
print("South Carolina")
print("Trump: ", (len(trumpsc)/(len(trumpsc)+len(bidensc))))
print("Biden: ",(len(bidensc)/(len(trumpsc)+len(bidensc))))
print("South Carolina 1")
trumpsc1votes = (len(trumpsc1)/(len(trumpsc1)+len(bidensc1)))*304222
bidensc1votes = (len(bidensc1)/(len(trumpsc1)+len(bidensc1)))*304222
print("Trump: ", (len(trumpsc1)/(len(trumpsc1)+len(bidensc1))))
print("votes ", trumpsc1votes)
print("Biden: ",(len(bidensc1)/(len(trumpsc1)+len(bidensc1))))
print("votes ", bidensc1votes)
print("South Carolina 2")
trumpsc2votes = (len(trumpsc2)/(len(trumpsc2)+len(bidensc2)))*293254
bidensc2votes = (len(bidensc2)/(len(trumpsc2)+len(bidensc2)))*293254
print("Trump: ", (len(trumpsc2)/(len(trumpsc2)+len(bidensc2))))
print("votes ", trumpsc2votes)
print("Biden: ",(len(bidensc2)/(len(trumpsc2)+len(bidensc2))))
print("votes ", bidensc2votes)
print("South Carolina 3")
trumpsc3votes = (len(trumpsc3)/(len(trumpsc3)+len(bidensc3)))*269786
bidensc3votes = (len(bidensc3)/(len(trumpsc3)+len(bidensc3)))*269786
print("Trump: ", (len(trumpsc3)/(len(trumpsc3)+len(bidensc3))))
print("votes ", trumpsc3votes)
print("Biden: ",(len(bidensc3)/(len(trumpsc3)+len(bidensc3))))
print("votes ", bidensc3votes)
print("South Carolina 4")
trumpsc4votes = (len(trumpsc4)/(len(trumpsc4)+len(bidensc4)))*288341
bidensc4votes = (len(bidensc4)/(len(trumpsc4)+len(bidensc4)))*288341
print("Trump: ", (len(trumpsc4)/(len(trumpsc4)+len(bidensc4))))
print("votes ", trumpsc4votes)
print("Biden: ",(len(bidensc4)/(len(trumpsc4)+len(bidensc4))))
print("votes ", bidensc4votes)
print("South Carolina 5")
trumpsc5votes = (len(trumpsc5)/(len(trumpsc5)+len(bidensc5)))*290075
bidensc5votes = (len(bidensc5)/(len(trumpsc5)+len(bidensc5)))*290075
print("Trump: ", (len(trumpsc5)/(len(trumpsc5)+len(bidensc5))))
print("votes ", trumpsc5votes)
print("Biden: ",(len(bidensc5)/(len(trumpsc5)+len(bidensc5))))
print("votes ", bidensc5votes)
print("South Carolina 6")
trumpsc6votes = (len(trumpsc6)/(len(trumpsc6)+len(bidensc6)))*249987
bidensc6votes = (len(bidensc6)/(len(trumpsc6)+len(bidensc6)))*249987
print("Trump: ", (len(trumpsc6)/(len(trumpsc6)+len(bidensc6))))
print("votes ", trumpsc6votes)
print("Biden: ",(len(bidensc6)/(len(trumpsc6)+len(bidensc6))))
print("votes ", bidensc6votes)
print("South Carolina 7")
trumpsc7votes = (len(trumpsc7)/(len(trumpsc7)+len(bidensc7)))*281204
bidensc7votes = (len(bidensc7)/(len(trumpsc7)+len(bidensc7)))*281204
print("Trump: ", (len(trumpsc7)/(len(trumpsc7)+len(bidensc7))))
print("votes ", trumpsc7votes)
print("Biden: ",(len(bidensc7)/(len(trumpsc7)+len(bidensc7))))
print("votes ", bidensc7votes)
totalscvotestrump = trumpsc1votes+trumpsc2votes+trumpsc3votes+trumpsc4votes+trumpsc5votes+trumpsc6votes+trumpsc7votes
totalscvotesbiden = bidensc1votes+bidensc2votes+bidensc3votes+bidensc4votes+bidensc5votes+bidensc6votes+bidensc7votes
print("TOTAL TRUMP VOTES: ", totalscvotestrump/(totalscvotestrump+totalscvotesbiden))
print("TOTAL BIDEN VOTES: ", totalscvotesbiden/(totalscvotestrump+totalscvotesbiden))
print("")
print("Indiana")
print("Trump: ", (len(trumpin)/(len(trumpin)+len(bidenin))))
print("Biden: ",(len(bidenin)/(len(trumpin)+len(bidenin))))
print("Indiana 1")
trumpin1votes = (len(trumpin1)/(len(trumpin1)+len(bidenin1)))*254308
bidenin1votes = (len(bidenin1)/(len(trumpin1)+len(bidenin1)))*254308
print("Trump: ", (len(trumpin1)/(len(trumpin1)+len(bidenin1))))
print("votes ", trumpin1votes)
print("Biden: ",(len(bidenin1)/(len(trumpin1)+len(bidenin1))))
print("votes ", bidenin1votes)
print("Indiana 2")
trumpin2votes = (len(trumpin2)/(len(trumpin2)+len(bidenin2)))*266608
bidenin2votes = (len(bidenin2)/(len(trumpin2)+len(bidenin2)))*266608
print("Trump: ", (len(trumpin2)/(len(trumpin2)+len(bidenin2))))
print("votes ", trumpin2votes)
print("Biden: ",(len(bidenin2)/(len(trumpin2)+len(bidenin2))))
print("votes ", bidenin2votes)
print("Indiana 3")
trumpin3votes = (len(trumpin3)/(len(trumpin3)+len(bidenin3)))*267124
bidenin3votes = (len(bidenin3)/(len(trumpin3)+len(bidenin3)))*267124
print("Trump: ", (len(trumpin3)/(len(trumpin3)+len(bidenin3))))
print("votes ", trumpin3votes)
print("Biden: ",(len(bidenin3)/(len(trumpin3)+len(bidenin3))))
print("votes ", bidenin3votes)
print("Indiana 4")
trumpin4votes = (len(trumpin4)/(len(trumpin4)+len(bidenin4)))*284425
bidenin4votes = (len(bidenin4)/(len(trumpin4)+len(bidenin4)))*284425
print("Trump: ", (len(trumpin4)/(len(trumpin4)+len(bidenin4))))
print("votes ", trumpin4votes)
print("Biden: ",(len(bidenin4)/(len(trumpin4)+len(bidenin4))))
print("votes ", bidenin4votes)
print("Indiana 5")
trumpin5votes = (len(trumpin5)/(len(trumpin5)+len(bidenin5)))*345576
bidenin5votes = (len(bidenin5)/(len(trumpin5)+len(bidenin5)))*345576
print("Trump: ", (len(trumpin5)/(len(trumpin5)+len(bidenin5))))
print("votes ", trumpin5votes)
print("Biden: ",(len(bidenin5)/(len(trumpin5)+len(bidenin5))))
print("votes ", bidenin5votes)
print("Indiana 6")
trumpin6votes = (len(trumpin6)/(len(trumpin6)+len(bidenin6)))*283919
bidenin6votes = (len(bidenin6)/(len(trumpin6)+len(bidenin6)))*283919
print("Trump: ", (len(trumpin6)/(len(trumpin6)+len(bidenin6))))
print("votes ", trumpin6votes)
print("Biden: ",(len(bidenin6)/(len(trumpin6)+len(bidenin6))))
print("votes ", bidenin6votes)
print("Indiana 7")
trumpin7votes = (len(trumpin7)/(len(trumpin7)+len(bidenin7)))*253002
bidenin7votes = (len(bidenin7)/(len(trumpin7)+len(bidenin7)))*253002
print("Trump: ", (len(trumpin7)/(len(trumpin7)+len(bidenin7))))
print("votes ", trumpin7votes)
print("Biden: ",(len(bidenin7)/(len(trumpin7)+len(bidenin7))))
print("votes ", bidenin7votes)
print("Indiana 8")
trumpin8votes = (len(trumpin8)/(len(trumpin8)+len(bidenin8)))*280699
bidenin8votes = (len(bidenin8)/(len(trumpin8)+len(bidenin8)))*280699
print("Trump: ", (len(trumpin8)/(len(trumpin8)+len(bidenin8))))
print("votes ", trumpin8votes)
print("Biden: ",(len(bidenin8)/(len(trumpin8)+len(bidenin8))))
print("votes ", bidenin8votes)
print("Indiana 9")
trumpin9votes = (len(trumpin9)/(len(trumpin9)+len(bidenin9)))*305237
bidenin9votes = (len(bidenin9)/(len(trumpin9)+len(bidenin9)))*305237
print("Trump: ", (len(trumpin9)/(len(trumpin9)+len(bidenin9))))
print("votes ", trumpin9votes)
print("Biden: ",(len(bidenin9)/(len(trumpin9)+len(bidenin9))))
print("votes ", bidenin9votes)
totalinvotestrump = trumpin1votes+trumpin2votes+trumpin3votes+trumpin4votes+trumpin5votes+trumpin6votes+trumpin7votes+trumpin8votes+trumpin9votes
totalinvotesbiden = bidenin1votes+bidenin2votes+bidenin3votes+bidenin4votes+bidenin5votes+bidenin6votes+bidenin7votes+bidenin8votes+bidenin9votes
print("TOTAL TRUMP VOTES: ", totalinvotestrump/(totalinvotestrump+totalinvotesbiden))
print("TOTAL BIDEN VOTES: ", totalinvotesbiden/(totalinvotestrump+totalinvotesbiden))
print("")
print("Maine")
print("Trump: ", (len(trumpme)/(len(trumpme)+len(bidenme))))
print("Biden: ",(len(bidenme)/(len(trumpme)+len(bidenme))))
print("Maine 1")
trumpme1votes = (len(trumpme1)/(len(trumpme1)+len(bidenme1)))*389476
bidenme1votes = (len(bidenme1)/(len(trumpme1)+len(bidenme1)))*389476
print("Trump: ", (len(trumpme1)/(len(trumpme1)+len(bidenme1))))
print("votes ", len(trumpme1))
print("Biden: ",(len(bidenme1)/(len(trumpme1)+len(bidenme1))))
print("votes ", len(bidenme1))
print("Maine 2")
trumpme2votes = (len(trumpme2)/(len(trumpme2)+len(bidenme2)))*350147
bidenme2votes = (len(bidenme2)/(len(trumpme2)+len(bidenme2)))*350147
print("Trump: ", (len(trumpme2)/(len(trumpme2)+len(bidenme2))))
print("votes ", len(trumpme2))
print("Biden: ",(len(bidenme2)/(len(trumpme2)+len(bidenme2))))
print("votes ", len(bidenme2))
totalmevotestrump = trumpme1votes+trumpme2votes
totalmevotesbiden = bidenme1votes+bidenme2votes
print("TOTAL TRUMP VOTES: ", totalmevotestrump/(totalmevotestrump+totalmevotesbiden))
print("TOTAL BIDEN VOTES: ", totalmevotesbiden/(totalmevotestrump+totalmevotesbiden))
print("")
print("Delaware")
print("Trump: ", (len(trumpde)/(len(trumpde)+len(bidende))))
print("Biden: ",(len(bidende)/(len(trumpde)+len(bidende))))
print("Delaware 1")
bothde1 = trumpde1.intersection(bidende1)
bothde1votes = (len(bothde1)/(len(trumpde1)+len(bidende1)))
print("Trump: ", (len(trumpde1)/(len(trumpde1)+len(bidende1)))-((len(bothde1)/(len(trumpde1)+len(bidende1)))/2))
print("votes ", len(trumpde1))
print("Biden: ",(len(bidende1)/(len(trumpde1)+len(bidende1)))-((len(bothde1)/(len(trumpde1)+len(bidende1)))/2))
print("votes ", len(bidende1))
print("Both: ", (len(bothde1)/(len(trumpde1)+len(bidende1))))
print("")
print("Maryland")
print("Trump: ", (len(trumpmd)/(len(trumpmd)+len(bidenmd))))
print("Biden: ",(len(bidenmd)/(len(trumpmd)+len(bidenmd))))
print("Maryland 1")
trumpmd1votes = (len(trumpmd1)/(len(trumpmd1)+len(bidenmd1)))*323911
bidenmd1votes = (len(bidenmd1)/(len(trumpmd1)+len(bidenmd1)))*323911
print("Trump: ", (len(trumpmd1)/(len(trumpmd1)+len(bidenmd1))))
print("votes ", trumpmd1votes)
print("Biden: ",(len(bidenmd1)/(len(trumpmd1)+len(bidenmd1))))
print("votes ", bidenmd1votes)
print("Maryland 2")
trumpmd2votes = (len(trumpmd2)/(len(trumpmd2)+len(bidenmd2)))*264423
bidenmd2votes = (len(bidenmd2)/(len(trumpmd2)+len(bidenmd2)))*264423
print("Trump: ", (len(trumpmd2)/(len(trumpmd2)+len(bidenmd2))))
print("votes ", trumpmd2votes)
print("Biden: ",(len(bidenmd2)/(len(trumpmd2)+len(bidenmd2))))
print("votes ", bidenmd2votes)
print("Maryland 3")
trumpmd3votes = (len(trumpmd3)/(len(trumpmd3)+len(bidenmd3)))*300989
bidenmd3votes = (len(bidenmd3)/(len(trumpmd3)+len(bidenmd3)))*300989
print("Trump: ", (len(trumpmd3)/(len(trumpmd3)+len(bidenmd3))))
print("votes ", trumpmd3votes)
print("Biden: ",(len(bidenmd3)/(len(trumpmd3)+len(bidenmd3))))
print("votes ", bidenmd3votes)
print("Maryland 4")
trumpmd4votes = (len(trumpmd4)/(len(trumpmd4)+len(bidenmd4)))*281889
bidenmd4votes = (len(bidenmd4)/(len(trumpmd4)+len(bidenmd4)))*281899
print("Trump: ", (len(trumpmd4)/(len(trumpmd4)+len(bidenmd4))))
print("votes ", trumpmd4votes)
print("Biden: ",(len(bidenmd4)/(len(trumpmd4)+len(bidenmd4))))
print("votes ", bidenmd4votes)
print("Maryland 5")
trumpmd5votes = (len(trumpmd5)/(len(trumpmd5)+len(bidenmd5)))*322350
bidenmd5votes = (len(bidenmd5)/(len(trumpmd5)+len(bidenmd5)))*322350
print("Trump: ", (len(trumpmd5)/(len(trumpmd5)+len(bidenmd5))))
print("votes ", trumpmd5votes)
print("Biden: ",(len(bidenmd5)/(len(trumpmd5)+len(bidenmd5))))
print("votes ", bidenmd5votes)
print("Maryland 6")
trumpmd6votes = (len(trumpmd6)/(len(trumpmd6)+len(bidenmd6)))*290840
bidenmd6votes = (len(bidenmd6)/(len(trumpmd6)+len(bidenmd6)))*290840
print("Trump: ", (len(trumpmd6)/(len(trumpmd6)+len(bidenmd6))))
print("votes ", trumpmd6votes)
print("Biden: ",(len(bidenmd6)/(len(trumpmd6)+len(bidenmd6))))
print("votes ", bidenmd6votes)
print("Maryland 7")
trumpmd7votes = (len(trumpmd7)/(len(trumpmd7)+len(bidenmd7)))*273816
bidenmd7votes = (len(bidenmd7)/(len(trumpmd7)+len(bidenmd7)))*273816
print("Trump: ", (len(trumpmd7)/(len(trumpmd7)+len(bidenmd7))))
print("votes ", trumpmd7votes)
print("Biden: ",(len(bidenmd7)/(len(trumpmd7)+len(bidenmd7))))
print("votes ", bidenmd7votes)
print("Maryland 8")
trumpmd8votes = (len(trumpmd8)/(len(trumpmd8)+len(bidenmd8)))*306871
bidenmd8votes = (len(bidenmd8)/(len(trumpmd8)+len(bidenmd8)))*306871
print("Trump: ", (len(trumpmd8)/(len(trumpmd8)+len(bidenmd8))))
print("votes ", trumpmd8votes)
print("Biden: ",(len(bidenmd8)/(len(trumpmd8)+len(bidenmd8))))
print("votes ", bidenmd8votes)
totalmdvotestrump = trumpmd1votes+trumpmd2votes+trumpmd3votes+trumpmd4votes+trumpmd5votes+trumpmd6votes+trumpmd7votes+trumpmd8votes
totalmdvotesbiden = bidenmd1votes+bidenmd2votes+bidenmd3votes+bidenmd4votes+bidenmd5votes+bidenmd6votes+bidenmd7votes+bidenmd8votes
print("TOTAL TRUMP VOTES: ", totalmdvotestrump/(totalmdvotestrump+totalmdvotesbiden))
print("TOTAL BIDEN VOTES: ", totalmdvotesbiden/(totalmdvotestrump+totalmdvotesbiden))
print("")
print("South Dakota")
print("Trump: ", (len(trumpsd)/(len(trumpsd)+len(bidensd))))
print("Biden: ",(len(bidensd)/(len(trumpsd)+len(bidensd))))
print("South Dakota 1")
bothsd1 = trumpsd1.intersection(bidensd1)
bothsd1votes = (len(bothsd1)/(len(trumpsd1)+len(bidensd1)))
print("Trump: ", (len(trumpsd1)/(len(trumpsd1)+len(bidensd1)))-((len(bothsd1)/(len(trumpsd1)+len(bidensd1)))/2))
print("votes ", len(trumpsd1))
print("biden: ",(len(bidensd1)/(len(trumpsd1)+len(bidensd1)))-((len(bothsd1)/(len(trumpsd1)+len(bidensd1)))/2))
print("votes ", len(bidensd1))
print("Both: ", (len(bothsd1)/(len(trumpsd1)+len(bidensd1))))
print("")
print("Massachusetts")
print("Trump: ", (len(trumpma)/(len(trumpma)+len(bidenma))))
print("Biden: ",(len(bidenma)/(len(trumpma)+len(bidenma))))
print("Massachusetts 1")
trumpma1votes = (len(trumpma1)/(len(trumpma1)+len(bidenma1)))*1
bidenma1votes = (len(bidenma1)/(len(trumpma1)+len(bidenma1)))*1
print("Trump: ", (len(trumpma1)/(len(trumpma1)+len(bidenma1))))
print("votes ", trumpma1votes)
print("Biden: ",(len(bidenma1)/(len(trumpma1)+len(bidenma1))))
print("votes ", bidenma1votes)
print("Massachusetts 2")
trumpma2votes = (len(trumpma2)/(len(trumpma2)+len(bidenma2)))*1
bidenma2votes = (len(bidenma2)/(len(trumpma2)+len(bidenma2)))*1
print("Trump: ", (len(trumpma2)/(len(trumpma2)+len(bidenma2))))
print("votes ", trumpma2votes)
print("Biden: ",(len(bidenma2)/(len(trumpma2)+len(bidenma2))))
print("votes ", bidenma2votes)
print("Massachusetts 3")
trumpma3votes = (len(trumpma3)/(len(trumpma3)+len(bidenma3)))*1
bidenma3votes = (len(bidenma3)/(len(trumpma3)+len(bidenma3)))*1
print("Trump: ", (len(trumpma3)/(len(trumpma3)+len(bidenma3))))
print("votes ", trumpma3votes)
print("Biden: ",(len(bidenma3)/(len(trumpma3)+len(bidenma3))))
print("votes ", bidenma3votes)
print("Massachusetts 4")
trumpma4votes = (len(trumpma4)/(len(trumpma4)+len(bidenma4)))*1
bidenma4votes = (len(bidenma4)/(len(trumpma4)+len(bidenma4)))*1
print("Trump: ", (len(trumpma4)/(len(trumpma4)+len(bidenma4))))
print("votes ", trumpma4votes)
print("Biden: ",(len(bidenma4)/(len(trumpma4)+len(bidenma4))))
print("votes ", bidenma4votes)
print("Massachusetts 5")
trumpma5votes = (len(trumpma5)/(len(trumpma5)+len(bidenma5)))*1
bidenma5votes = (len(bidenma5)/(len(trumpma5)+len(bidenma5)))*1
print("Trump: ", (len(trumpma5)/(len(trumpma5)+len(bidenma5))))
print("votes ", trumpma5votes)
print("Biden: ",(len(bidenma5)/(len(trumpma5)+len(bidenma5))))
print("votes ", bidenma5votes)
print("Massachusetts 6")
trumpma6votes = (len(trumpma6)/(len(trumpma6)+len(bidenma6)))*1
bidenma6votes = (len(bidenma6)/(len(trumpma6)+len(bidenma6)))*1
print("Trump: ", (len(trumpma6)/(len(trumpma6)+len(bidenma6))))
print("votes ", trumpma6votes)
print("Biden: ",(len(bidenma6)/(len(trumpma6)+len(bidenma6))))
print("votes ", bidenma6votes)
print("Massachusetts 7")
trumpma7votes = (len(trumpma7)/(len(trumpma7)+len(bidenma7)))*1
bidenma7votes = (len(bidenma7)/(len(trumpma7)+len(bidenma7)))*1
print("Trump: ", (len(trumpma7)/(len(trumpma7)+len(bidenma7))))
print("votes ", trumpma7votes)
print("Biden: ",(len(bidenma7)/(len(trumpma7)+len(bidenma7))))
print("votes ", bidenma7votes)
print("Massachusetts 8")
trumpma8votes = (len(trumpma8)/(len(trumpma8)+len(bidenma8)))*1
bidenma8votes = (len(bidenma8)/(len(trumpma8)+len(bidenma8)))*1
print("Trump: ", (len(trumpma8)/(len(trumpma8)+len(bidenma8))))
print("votes ", trumpma8votes)
print("Biden: ",(len(bidenma8)/(len(trumpma8)+len(bidenma8))))
print("votes ", bidenma8votes)
print("Massachusetts 9")
trumpma9votes = (len(trumpma9)/(len(trumpma9)+len(bidenma9)))*1
bidenma9votes = (len(bidenma9)/(len(trumpma9)+len(bidenma9)))*1
print("Trump: ", (len(trumpma9)/(len(trumpma9)+len(bidenma9))))
print("votes ", trumpma9votes)
print("Biden: ",(len(bidenma9)/(len(trumpma9)+len(bidenma9))))
print("votes ", bidenma9votes)
totalmavotestrump = trumpma1votes+trumpma2votes+trumpma3votes+trumpma4votes+trumpma5votes+trumpma6votes+trumpma7votes+trumpma8votes+trumpma9votes
totalmavotesbiden = bidenma1votes+bidenma2votes+bidenma3votes+bidenma4votes+bidenma5votes+bidenma6votes+bidenma7votes+bidenma8votes+bidenma9votes
print("TOTAL TRUMP VOTES: ", totalmavotestrump/(totalmavotestrump+totalmavotesbiden))
print("TOTAL BIDEN VOTES: ", totalmavotesbiden/(totalmavotestrump+totalmavotesbiden))
print("")
print("Michigan")
print("Trump: ", (len(trumpmi)/(len(trumpmi)+len(bidenmi))))
print("Biden: ",(len(bidenmi)/(len(trumpmi)+len(bidenmi))))
print("Michigan 1")
trumpmi1votes = (len(trumpmi1)/(len(trumpmi1)+len(bidenmi1)))*345472
bidenmi1votes = (len(bidenmi1)/(len(trumpmi1)+len(bidenmi1)))*345472
print("Trump: ", (len(trumpmi1)/(len(trumpmi1)+len(bidenmi1))))
print("votes ", trumpmi1votes)
print("Biden: ",(len(bidenmi1)/(len(trumpmi1)+len(bidenmi1))))
print("votes ", bidenmi1votes)
print("Michigan 2")
trumpmi2votes = (len(trumpmi2)/(len(trumpmi2)+len(bidenmi2)))*323172
bidenmi2votes = (len(bidenmi2)/(len(trumpmi2)+len(bidenmi2)))*323172
print("Trump: ", (len(trumpmi2)/(len(trumpmi2)+len(bidenmi2))))
print("votes ", trumpmi2votes)
print("Biden: ",(len(bidenmi2)/(len(trumpmi2)+len(bidenmi2))))
print("votes ", bidenmi2votes)
print("Michigan 3")
trumpmi3votes = (len(trumpmi3)/(len(trumpmi3)+len(bidenmi3)))*331228
bidenmi3votes = (len(bidenmi3)/(len(trumpmi3)+len(bidenmi3)))*331228
print("Trump: ", (len(trumpmi3)/(len(trumpmi3)+len(bidenmi3))))
print("votes ", trumpmi3votes)
print("Biden: ",(len(bidenmi3)/(len(trumpmi3)+len(bidenmi3))))
print("votes ", bidenmi3votes)
print("Michigan 4")
trumpmi4votes = (len(trumpmi4)/(len(trumpmi4)+len(bidenmi4)))*295844
bidenmi4votes = (len(bidenmi4)/(len(trumpmi4)+len(bidenmi4)))*295844
print("Trump: ", (len(trumpmi4)/(len(trumpmi4)+len(bidenmi4))))
print("votes ", trumpmi4votes)
print("Biden: ",(len(bidenmi4)/(len(trumpmi4)+len(bidenmi4))))
print("votes ", bidenmi4votes)
print("Michigan 5")
trumpmi5votes = (len(trumpmi5)/(len(trumpmi5)+len(bidenmi5)))*306984
bidenmi5votes = (len(bidenmi5)/(len(trumpmi5)+len(bidenmi5)))*306984
print("Trump: ", (len(trumpmi5)/(len(trumpmi5)+len(bidenmi5))))
print("votes ", trumpmi5votes)
print("Biden: ",(len(bidenmi5)/(len(trumpmi5)+len(bidenmi5))))
print("votes ", bidenmi5votes)
print("Michigan 6")
trumpmi6votes = (len(trumpmi6)/(len(trumpmi6)+len(bidenmi6)))*312733
bidenmi6votes = (len(bidenmi6)/(len(trumpmi6)+len(bidenmi6)))*312733
print("Trump: ", (len(trumpmi6)/(len(trumpmi6)+len(bidenmi6))))
print("votes ", trumpmi6votes)
print("Biden: ",(len(bidenmi6)/(len(trumpmi6)+len(bidenmi6))))
print("votes ", bidenmi6votes)
print("Michigan 7")
trumpmi7votes = (len(trumpmi7)/(len(trumpmi7)+len(bidenmi7)))*317246
bidenmi7votes = (len(bidenmi7)/(len(trumpmi7)+len(bidenmi7)))*317246
print("Trump: ", (len(trumpmi7)/(len(trumpmi7)+len(bidenmi7))))
print("votes ", trumpmi7votes)
print("Biden: ",(len(bidenmi7)/(len(trumpmi7)+len(bidenmi7))))
print("votes ", bidenmi7votes)
print("Michigan 8")
trumpmi8votes = (len(trumpmi8)/(len(trumpmi8)+len(bidenmi8)))*349775
bidenmi8votes = (len(bidenmi8)/(len(trumpmi8)+len(bidenmi8)))*349775
print("Trump: ", (len(trumpmi8)/(len(trumpmi8)+len(bidenmi8))))
print("votes ", trumpmi8votes)
print("Biden: ",(len(bidenmi8)/(len(trumpmi8)+len(bidenmi8))))
print("votes ", bidenmi8votes)
print("Michigan 9")
trumpmi9votes = (len(trumpmi9)/(len(trumpmi9)+len(bidenmi9)))*328527
bidenmi9votes = (len(bidenmi9)/(len(trumpmi9)+len(bidenmi9)))*328527
print("Trump: ", (len(trumpmi9)/(len(trumpmi9)+len(bidenmi9))))
print("votes ", trumpmi9votes)
print("Biden: ",(len(bidenmi9)/(len(trumpmi9)+len(bidenmi9))))
print("votes ", bidenmi9votes)
print("Michigan 10")
trumpmi10votes = (len(trumpmi10)/(len(trumpmi10)+len(bidenmi10)))*324039
bidenmi10votes = (len(bidenmi10)/(len(trumpmi10)+len(bidenmi10)))*324039
print("Trump: ", (len(trumpmi10)/(len(trumpmi10)+len(bidenmi10))))
print("votes ", trumpmi10votes)
print("Biden: ",(len(bidenmi10)/(len(trumpmi10)+len(bidenmi10))))
print("votes ", bidenmi10votes)
print("Michigan 11")
trumpmi11votes = (len(trumpmi11)/(len(trumpmi11)+len(bidenmi11)))*353146
bidenmi11votes = (len(bidenmi11)/(len(trumpmi11)+len(bidenmi11)))*353146
print("Trump: ", (len(trumpmi11)/(len(trumpmi11)+len(bidenmi11))))
print("votes ", trumpmi11votes)
print("Biden: ",(len(bidenmi11)/(len(trumpmi11)+len(bidenmi11))))
print("votes ", bidenmi11votes)
print("Michigan 12")
trumpmi12votes = (len(trumpmi12)/(len(trumpmi12)+len(bidenmi12)))*306745
bidenmi12votes = (len(bidenmi12)/(len(trumpmi12)+len(bidenmi12)))*306745
print("Trump: ", (len(trumpmi12)/(len(trumpmi12)+len(bidenmi12))))
print("votes ", trumpmi12votes)
print("Biden: ",(len(bidenmi12)/(len(trumpmi12)+len(bidenmi12))))
print("votes ", bidenmi12votes)
print("Michigan 13")
trumpmi13votes = (len(trumpmi13)/(len(trumpmi13)+len(bidenmi13)))*237656
bidenmi13votes = (len(bidenmi13)/(len(trumpmi13)+len(bidenmi13)))*237656
print("Trump: ", (len(trumpmi13)/(len(trumpmi13)+len(bidenmi13))))
print("votes ", trumpmi13votes)
print("Biden: ",(len(bidenmi13)/(len(trumpmi13)+len(bidenmi13))))
print("votes ", bidenmi13votes)
print("Michigan 14")
trumpmi14votes = (len(trumpmi14)/(len(trumpmi14)+len(bidenmi14)))*302331
bidenmi14votes = (len(bidenmi14)/(len(trumpmi14)+len(bidenmi14)))*302331
print("Trump: ", (len(trumpmi14)/(len(trumpmi14)+len(bidenmi14))))
print("votes ", trumpmi14votes)
print("Biden: ",(len(bidenmi14)/(len(trumpmi14)+len(bidenmi14))))
print("votes ", bidenmi14votes)
totalmivotestrump = trumpmi1votes+trumpmi2votes+trumpmi3votes+trumpmi4votes+trumpmi5votes+trumpmi6votes+trumpmi7votes+trumpmi8votes+trumpmi9votes+trumpmi10votes+trumpmi11votes+trumpmi12votes+trumpmi13votes+trumpmi14votes
totalmivotesbiden = bidenmi1votes+bidenmi2votes+bidenmi3votes+bidenmi4votes+bidenmi5votes+bidenmi6votes+bidenmi7votes+bidenmi8votes+bidenmi9votes+bidenmi10votes+bidenmi11votes+bidenmi12votes+bidenmi13votes+bidenmi14votes
print("TOTAL TRUMP VOTES: ", totalmivotestrump/(totalmivotestrump+totalmivotesbiden))
print("TOTAL BIDEN VOTES: ", totalmivotesbiden/(totalmivotestrump+totalmivotesbiden))
print("")
print("California")
print("Trump: ", (len(trumpca)/(len(trumpca)+len(bidenca))))
print("Biden: ",(len(bidenca)/(len(trumpca)+len(bidenca))))
print("California 1")
trumpca1votes = (len(trumpca1)/(len(trumpca1)+len(bidenca1)))*314036
bidenca1votes = (len(bidenca1)/(len(trumpca1)+len(bidenca1)))*314036
print("Trump: ", (len(trumpca1)/(len(trumpca1)+len(bidenca1))))
print("votes ", trumpca1votes)
print("Biden: ",(len(bidenca1)/(len(trumpca1)+len(bidenca1))))
print("votes ", bidenca1votes)
print("California 2")
trumpca2votes = (len(trumpca2)/(len(trumpca2)+len(bidenca2)))*330766
bidenca2votes = (len(bidenca2)/(len(trumpca2)+len(bidenca2)))*330766
print("Trump: ", (len(trumpca2)/(len(trumpca2)+len(bidenca2))))
print("votes ", trumpca2votes)
print("Biden: ",(len(bidenca2)/(len(trumpca2)+len(bidenca2))))
print("votes ", bidenca2votes)
print("California 3")
trumpca3votes = (len(trumpca3)/(len(trumpca3)+len(bidenca3)))*256966
bidenca3votes = (len(bidenca3)/(len(trumpca3)+len(bidenca3)))*256966
print("Trump: ", (len(trumpca3)/(len(trumpca3)+len(bidenca3))))
print("votes ", trumpca3votes)
print("Biden: ",(len(bidenca3)/(len(trumpca3)+len(bidenca3))))
print("votes ", bidenca3votes)
print("California 4")
trumpca4votes = (len(trumpca4)/(len(trumpca4)+len(bidenca4)))*350978
bidenca4votes = (len(bidenca4)/(len(trumpca4)+len(bidenca4)))*350978
print("Trump: ", (len(trumpca4)/(len(trumpca4)+len(bidenca4))))
print("votes ", trumpca4votes)
print("Biden: ",(len(bidenca4)/(len(trumpca4)+len(bidenca4))))
print("votes ", bidenca4votes)
print("California 5")
trumpca5votes = (len(trumpca5)/(len(trumpca5)+len(bidenca5)))*292091
bidenca5votes = (len(bidenca5)/(len(trumpca5)+len(bidenca5)))*292091
print("Trump: ", (len(trumpca5)/(len(trumpca5)+len(bidenca5))))
print("votes ", trumpca5votes)
print("Biden: ",(len(bidenca5)/(len(trumpca5)+len(bidenca5))))
print("votes ", bidenca5votes)
print("California 6")
trumpca6votes = (len(trumpca6)/(len(trumpca6)+len(bidenca6)))*235413
bidenca6votes = (len(bidenca6)/(len(trumpca6)+len(bidenca6)))*235413
print("Trump: ", (len(trumpca6)/(len(trumpca6)+len(bidenca6))))
print("votes ", trumpca6votes)
print("Biden: ",(len(bidenca6)/(len(trumpca6)+len(bidenca6))))
print("votes ", bidenca6votes)
print("California 7")
trumpca7votes = (len(trumpca7)/(len(trumpca7)+len(bidenca7)))*297301
bidenca7votes = (len(bidenca7)/(len(trumpca7)+len(bidenca7)))*297301
print("Trump: ", (len(trumpca7)/(len(trumpca7)+len(bidenca7))))
print("votes ", trumpca7votes)
print("Biden: ",(len(bidenca7)/(len(trumpca7)+len(bidenca7))))
print("votes ", bidenca7votes)
print("California 8")
trumpca8votes = (len(trumpca8)/(len(trumpca8)+len(bidenca8)))*220007
bidenca8votes = (len(bidenca8)/(len(trumpca8)+len(bidenca8)))*220007
print("Trump: ", (len(trumpca8)/(len(trumpca8)+len(bidenca8))))
print("votes ", trumpca8votes)
print("Biden: ",(len(bidenca8)/(len(trumpca8)+len(bidenca8))))
print("votes ", bidenca8votes)
print("California 9")
trumpca9votes = (len(trumpca9)/(len(trumpca9)+len(bidenca9)))*232155
bidenca9votes = (len(bidenca9)/(len(trumpca9)+len(bidenca9)))*232155
print("Trump: ", (len(trumpca9)/(len(trumpca9)+len(bidenca9))))
print("votes ", trumpca9votes)
print("Biden: ",(len(bidenca9)/(len(trumpca9)+len(bidenca9))))
print("votes ", bidenca9votes)
print("California 10")
trumpca10votes = (len(trumpca10)/(len(trumpca10)+len(bidenca10)))*241141
bidenca10votes = (len(bidenca10)/(len(trumpca10)+len(bidenca10)))*241141
print("Trump: ", (len(trumpca10)/(len(trumpca10)+len(bidenca10))))
print("votes ", trumpca10votes)
print("Biden: ",(len(bidenca10)/(len(trumpca10)+len(bidenca10))))
print("votes ", bidenca10votes)
print("California 11")
trumpca11votes = (len(trumpca11)/(len(trumpca11)+len(bidenca11)))*298209
bidenca11votes = (len(bidenca11)/(len(trumpca11)+len(bidenca11)))*298209
print("Trump: ", (len(trumpca11)/(len(trumpca11)+len(bidenca11))))
print("votes ", trumpca11votes)
print("Biden: ",(len(bidenca11)/(len(trumpca11)+len(bidenca11))))
print("votes ", bidenca11votes)
print("California 12")
trumpca12votes = (len(trumpca12)/(len(trumpca12)+len(bidenca12)))*338845
bidenca12votes = (len(bidenca12)/(len(trumpca12)+len(bidenca12)))*338845
print("Trump: ", (len(trumpca12)/(len(trumpca12)+len(bidenca12))))
print("votes ", trumpca12votes)
print("Biden: ",(len(bidenca12)/(len(trumpca12)+len(bidenca12))))
print("votes ", bidenca12votes)
print("California 13")
trumpca13votes = (len(trumpca13)/(len(trumpca13)+len(bidenca13)))*322871
bidenca13votes = (len(bidenca13)/(len(trumpca13)+len(bidenca13)))*322871
print("Trump: ", (len(trumpca13)/(len(trumpca13)+len(bidenca13))))
print("votes ", trumpca13votes)
print("Biden: ",(len(bidenca13)/(len(trumpca13)+len(bidenca13))))
print("votes ", bidenca13votes)
print("California 14")
trumpca14votes = (len(trumpca14)/(len(trumpca14)+len(bidenca14)))*286447
bidenca14votes = (len(bidenca14)/(len(trumpca14)+len(bidenca14)))*286447
print("Trump: ", (len(trumpca14)/(len(trumpca14)+len(bidenca14))))
print("votes ", trumpca14votes)
print("Biden: ",(len(bidenca14)/(len(trumpca14)+len(bidenca14))))
print("votes ", bidenca14votes)
print("California 15")
trumpca15votes = (len(trumpca15)/(len(trumpca15)+len(bidenca15)))*269197
bidenca15votes = (len(bidenca15)/(len(trumpca15)+len(bidenca15)))*269197
print("Trump: ", (len(trumpca15)/(len(trumpca15)+len(bidenca15))))
print("votes ", trumpca15votes)
print("Biden: ",(len(bidenca15)/(len(trumpca15)+len(bidenca15))))
print("votes ", bidenca15votes)
print("California 16")
trumpca16votes = (len(trumpca16)/(len(trumpca16)+len(bidenca16)))*167956
bidenca16votes = (len(bidenca16)/(len(trumpca16)+len(bidenca16)))*167956
print("Trump: ", (len(trumpca16)/(len(trumpca16)+len(bidenca16))))
print("votes ", trumpca16votes)
print("Biden: ",(len(bidenca16)/(len(trumpca16)+len(bidenca16))))
print("votes ", bidenca16votes)
print("California 17")
trumpca17votes = (len(trumpca17)/(len(trumpca17)+len(bidenca17)))*233192
bidenca17votes = (len(bidenca17)/(len(trumpca17)+len(bidenca17)))*233192
print("Trump: ", (len(trumpca17)/(len(trumpca17)+len(bidenca17))))
print("votes ", trumpca17votes)
print("Biden: ",(len(bidenca17)/(len(trumpca17)+len(bidenca17))))
print("votes ", bidenca17votes)
print("California 18")
trumpca18votes = (len(trumpca18)/(len(trumpca18)+len(bidenca18)))*323930
bidenca18votes = (len(bidenca18)/(len(trumpca18)+len(bidenca18)))*323930
print("Trump: ", (len(trumpca18)/(len(trumpca18)+len(bidenca18))))
print("votes ", trumpca18votes)
print("Biden: ",(len(bidenca18)/(len(trumpca18)+len(bidenca18))))
print("votes ", bidenca18votes)
print("California 19")
trumpca19votes = (len(trumpca19)/(len(trumpca19)+len(bidenca19)))*245863
bidenca19votes = (len(bidenca19)/(len(trumpca19)+len(bidenca19)))*245863
print("Trump: ", (len(trumpca19)/(len(trumpca19)+len(bidenca19))))
print("votes ", trumpca19votes)
print("Biden: ",(len(bidenca19)/(len(trumpca19)+len(bidenca19))))
print("votes ", bidenca19votes)
print("California 20")
trumpca20votes = (len(trumpca20)/(len(trumpca20)+len(bidenca20)))*255791
bidenca20votes = (len(bidenca20)/(len(trumpca20)+len(bidenca20)))*255791
print("Trump: ", (len(trumpca20)/(len(trumpca20)+len(bidenca20))))
print("votes ", trumpca20votes)
print("Biden: ",(len(bidenca20)/(len(trumpca20)+len(bidenca20))))
print("votes ", bidenca20votes)
print("California 21")
trumpca21votes = (len(trumpca21)/(len(trumpca21)+len(bidenca21)))*132408
bidenca21votes = (len(bidenca21)/(len(trumpca21)+len(bidenca21)))*132408
print("Trump: ", (len(trumpca21)/(len(trumpca21)+len(bidenca21))))
print("votes ", trumpca21votes)
print("Biden: ",(len(bidenca21)/(len(trumpca21)+len(bidenca21))))
print("votes ", bidenca21votes)
print("California 22")
trumpca22votes = (len(trumpca22)/(len(trumpca22)+len(bidenca22)))*234966
bidenca22votes = (len(bidenca22)/(len(trumpca22)+len(bidenca22)))*234966
print("Trump: ", (len(trumpca22)/(len(trumpca22)+len(bidenca22))))
print("votes ", trumpca22votes)
print("Biden: ",(len(bidenca22)/(len(trumpca22)+len(bidenca22))))
print("votes ", bidenca22votes)
print("California 23")
trumpca23votes = (len(trumpca23)/(len(trumpca23)+len(bidenca23)))*241584
bidenca23votes = (len(bidenca23)/(len(trumpca23)+len(bidenca23)))*241584
print("Trump: ", (len(trumpca23)/(len(trumpca23)+len(bidenca23))))
print("votes ", trumpca23votes)
print("Biden: ",(len(bidenca23)/(len(trumpca23)+len(bidenca23))))
print("votes ", bidenca23votes)
print("California 24")
trumpca24votes = (len(trumpca24)/(len(trumpca24)+len(bidenca24)))*310814
bidenca24votes = (len(bidenca24)/(len(trumpca24)+len(bidenca24)))*310814
print("Trump: ", (len(trumpca24)/(len(trumpca24)+len(bidenca24))))
print("votes ", trumpca24votes)
print("Biden: ",(len(bidenca24)/(len(trumpca24)+len(bidenca24))))
print("votes ", bidenca24votes)
print("California 25")
trumpca25votes = (len(trumpca25)/(len(trumpca25)+len(bidenca25)))*261161
bidenca25votes = (len(bidenca25)/(len(trumpca25)+len(bidenca25)))*261161
print("Trump: ", (len(trumpca25)/(len(trumpca25)+len(bidenca25))))
print("votes ", trumpca25votes)
print("Biden: ",(len(bidenca25)/(len(trumpca25)+len(bidenca25))))
print("votes ", bidenca25votes)
print("California 26")
trumpca26votes = (len(trumpca26)/(len(trumpca26)+len(bidenca26)))*280307
bidenca26votes = (len(bidenca26)/(len(trumpca26)+len(bidenca26)))*280307
print("Trump: ", (len(trumpca26)/(len(trumpca26)+len(bidenca26))))
print("votes ", trumpca26votes)
print("Biden: ",(len(bidenca26)/(len(trumpca26)+len(bidenca26))))
print("votes ", bidenca26votes)
print("California 27")
trumpca27votes = (len(trumpca27)/(len(trumpca27)+len(bidenca27)))*250632
bidenca27votes = (len(bidenca27)/(len(trumpca27)+len(bidenca27)))*250632
print("Trump: ", (len(trumpca27)/(len(trumpca27)+len(bidenca27))))
print("votes ", trumpca27votes)
print("Biden: ",(len(bidenca27)/(len(trumpca27)+len(bidenca27))))
print("votes ", bidenca27votes)
print("California 28")
trumpca28votes = (len(trumpca28)/(len(trumpca28)+len(bidenca28)))*270409
bidenca28votes = (len(bidenca28)/(len(trumpca28)+len(bidenca28)))*270409
print("Trump: ", (len(trumpca28)/(len(trumpca28)+len(bidenca28))))
print("votes ", trumpca28votes)
print("Biden: ",(len(bidenca28)/(len(trumpca28)+len(bidenca28))))
print("votes ", bidenca28votes)
print("California 29")
trumpca29votes = (len(trumpca29)/(len(trumpca29)+len(bidenca29)))*171824
bidenca29votes = (len(bidenca29)/(len(trumpca29)+len(bidenca29)))*171824
print("Trump: ", (len(trumpca29)/(len(trumpca29)+len(bidenca29))))
print("votes ", trumpca29votes)
print("Biden: ",(len(bidenca29)/(len(trumpca29)+len(bidenca29))))
print("votes ", bidenca29votes)
print("California 30")
trumpca30votes = (len(trumpca30)/(len(trumpca30)+len(bidenca30)))*282604
bidenca30votes = (len(bidenca30)/(len(trumpca30)+len(bidenca30)))*282604
print("Trump: ", (len(trumpca30)/(len(trumpca30)+len(bidenca30))))
print("votes ", trumpca30votes)
print("Biden: ",(len(bidenca30)/(len(trumpca30)+len(bidenca30))))
print("votes ", bidenca30votes)
print("California 31")
trumpca31votes = (len(trumpca31)/(len(trumpca31)+len(bidenca31)))*215936
bidenca31votes = (len(bidenca31)/(len(trumpca31)+len(bidenca31)))*215936
print("Trump: ", (len(trumpca31)/(len(trumpca31)+len(bidenca31))))
print("votes ", trumpca31votes)
print("Biden: ",(len(bidenca31)/(len(trumpca31)+len(bidenca31))))
print("votes ", bidenca31votes)
print("California 32")
trumpca32votes = (len(trumpca32)/(len(trumpca32)+len(bidenca32)))*186646
bidenca32votes = (len(bidenca32)/(len(trumpca32)+len(bidenca32)))*186646
print("Trump: ", (len(trumpca32)/(len(trumpca32)+len(bidenca32))))
print("votes ", trumpca32votes)
print("Biden: ",(len(bidenca32)/(len(trumpca32)+len(bidenca32))))
print("votes ", bidenca32votes)
print("California 33")
trumpca33votes = (len(trumpca33)/(len(trumpca33)+len(bidenca33)))*330219
bidenca33votes = (len(bidenca33)/(len(trumpca33)+len(bidenca33)))*330219
print("Trump: ", (len(trumpca33)/(len(trumpca33)+len(bidenca33))))
print("votes ", trumpca33votes)
print("Biden: ",(len(bidenca33)/(len(trumpca33)+len(bidenca33))))
print("votes ", bidenca33votes)
print("California 34")
trumpca34votes = (len(trumpca34)/(len(trumpca34)+len(bidenca34)))*159156
bidenca34votes = (len(bidenca34)/(len(trumpca34)+len(bidenca34)))*159156
print("Trump: ", (len(trumpca34)/(len(trumpca34)+len(bidenca34))))
print("votes ", trumpca34votes)
print("Biden: ",(len(bidenca34)/(len(trumpca34)+len(bidenca34))))
print("votes ", bidenca34votes)
print("California 35")
trumpca35votes = (len(trumpca35)/(len(trumpca35)+len(bidenca35)))*171353
bidenca35votes = (len(bidenca35)/(len(trumpca35)+len(bidenca35)))*171353
print("Trump: ", (len(trumpca35)/(len(trumpca35)+len(bidenca35))))
print("votes ", trumpca35votes)
print("Biden: ",(len(bidenca35)/(len(trumpca35)+len(bidenca35))))
print("votes ", bidenca35votes)
print("California 36")
trumpca36votes = (len(trumpca36)/(len(trumpca36)+len(bidenca36)))*232617
bidenca36votes = (len(bidenca36)/(len(trumpca36)+len(bidenca36)))*232617
print("Trump: ", (len(trumpca36)/(len(trumpca36)+len(bidenca36))))
print("votes ", trumpca36votes)
print("Biden: ",(len(bidenca36)/(len(trumpca36)+len(bidenca36))))
print("votes ", bidenca36votes)
print("California 37")
trumpca37votes = (len(trumpca37)/(len(trumpca37)+len(bidenca37)))*237272
bidenca37votes = (len(bidenca37)/(len(trumpca37)+len(bidenca37)))*237272
print("Trump: ", (len(trumpca37)/(len(trumpca37)+len(bidenca37))))
print("votes ", trumpca37votes)
print("Biden: ",(len(bidenca37)/(len(trumpca37)+len(bidenca37))))
print("votes ", bidenca37votes)
print("California 38")
trumpca38votes = (len(trumpca38)/(len(trumpca38)+len(bidenca38)))*232114
bidenca38votes = (len(bidenca38)/(len(trumpca38)+len(bidenca38)))*232114
print("Trump: ", (len(trumpca38)/(len(trumpca38)+len(bidenca38))))
print("votes ", trumpca38votes)
print("Biden: ",(len(bidenca38)/(len(trumpca38)+len(bidenca38))))
print("votes ", bidenca38votes)
print("California 39")
trumpca39votes = (len(trumpca39)/(len(trumpca39)+len(bidenca39)))*263456
bidenca39votes = (len(bidenca39)/(len(trumpca39)+len(bidenca39)))*263456
print("Trump: ", (len(trumpca39)/(len(trumpca39)+len(bidenca39))))
print("votes ", trumpca39votes)
print("Biden: ",(len(bidenca39)/(len(trumpca39)+len(bidenca39))))
print("votes ", bidenca39votes)
print("California 40")
trumpca40votes = (len(trumpca40)/(len(trumpca40)+len(bidenca40)))*149297
bidenca40votes = (len(bidenca40)/(len(trumpca40)+len(bidenca40)))*149297
print("Trump: ", (len(trumpca40)/(len(trumpca40)+len(bidenca40))))
print("votes ", trumpca40votes)
print("Biden: ",(len(bidenca40)/(len(trumpca40)+len(bidenca40))))
print("votes ", bidenca40votes)
print("California 41")
trumpca41votes = (len(trumpca41)/(len(trumpca41)+len(bidenca41)))*197323
bidenca41votes = (len(bidenca41)/(len(trumpca41)+len(bidenca41)))*197323
print("Trump: ", (len(trumpca41)/(len(trumpca41)+len(bidenca41))))
print("votes ", trumpca41votes)
print("Biden: ",(len(bidenca41)/(len(trumpca41)+len(bidenca41))))
print("votes ", bidenca41votes)
print("California 42")
trumpca42votes = (len(trumpca42)/(len(trumpca42)+len(bidenca42)))*254236
bidenca42votes = (len(bidenca42)/(len(trumpca42)+len(bidenca42)))*254236
print("Trump: ", (len(trumpca42)/(len(trumpca42)+len(bidenca42))))
print("votes ", trumpca42votes)
print("Biden: ",(len(bidenca42)/(len(trumpca42)+len(bidenca42))))
print("votes ", bidenca42votes)
print("California 43")
trumpca43votes = (len(trumpca43)/(len(trumpca43)+len(bidenca43)))*219516
bidenca43votes = (len(bidenca43)/(len(trumpca43)+len(bidenca43)))*219516
print("Trump: ", (len(trumpca43)/(len(trumpca43)+len(bidenca43))))
print("votes ", trumpca43votes)
print("Biden: ",(len(bidenca43)/(len(trumpca43)+len(bidenca43))))
print("votes ", bidenca43votes)
print("California 44")
trumpca44votes = (len(trumpca44)/(len(trumpca44)+len(bidenca44)))*178413
bidenca44votes = (len(bidenca44)/(len(trumpca44)+len(bidenca44)))*178413
print("Trump: ", (len(trumpca44)/(len(trumpca44)+len(bidenca44))))
print("votes ", trumpca44votes)
print("Biden: ",(len(bidenca44)/(len(trumpca44)+len(bidenca44))))
print("votes ", bidenca44votes)
print("California 45")
trumpca45votes = (len(trumpca45)/(len(trumpca45)+len(bidenca45)))*311849
bidenca45votes = (len(bidenca45)/(len(trumpca45)+len(bidenca45)))*311849
print("Trump: ", (len(trumpca45)/(len(trumpca45)+len(bidenca45))))
print("votes ", trumpca45votes)
print("Biden: ",(len(bidenca45)/(len(trumpca45)+len(bidenca45))))
print("votes ", bidenca45votes)
print("California 46")
trumpca46votes = (len(trumpca46)/(len(trumpca46)+len(bidenca46)))*164593
bidenca46votes = (len(bidenca46)/(len(trumpca46)+len(bidenca46)))*164593
print("Trump: ", (len(trumpca46)/(len(trumpca46)+len(bidenca46))))
print("votes ", trumpca46votes)
print("Biden: ",(len(bidenca46)/(len(trumpca46)+len(bidenca46))))
print("votes ", bidenca46votes)
print("California 47")
trumpca47votes = (len(trumpca47)/(len(trumpca47)+len(bidenca47)))*242868
bidenca47votes = (len(bidenca47)/(len(trumpca47)+len(bidenca47)))*242868
print("Trump: ", (len(trumpca47)/(len(trumpca47)+len(bidenca47))))
print("votes ", trumpca47votes)
print("Biden: ",(len(bidenca47)/(len(trumpca47)+len(bidenca47))))
print("votes ", bidenca47votes)
print("California 48")
trumpca48votes = (len(trumpca48)/(len(trumpca48)+len(bidenca48)))*306416
bidenca48votes = (len(bidenca48)/(len(trumpca48)+len(bidenca48)))*306416
print("Trump: ", (len(trumpca48)/(len(trumpca48)+len(bidenca48))))
print("votes ", trumpca48votes)
print("Biden: ",(len(bidenca48)/(len(trumpca48)+len(bidenca48))))
print("votes ", bidenca48votes)
print("California 49")
trumpca49votes = (len(trumpca49)/(len(trumpca49)+len(bidenca49)))*310155
bidenca49votes = (len(bidenca49)/(len(trumpca49)+len(bidenca49)))*310155
print("Trump: ", (len(trumpca49)/(len(trumpca49)+len(bidenca49))))
print("votes ", trumpca49votes)
print("Biden: ",(len(bidenca49)/(len(trumpca49)+len(bidenca49))))
print("votes ", bidenca49votes)
print("California 50")
trumpca50votes = (len(trumpca50)/(len(trumpca50)+len(bidenca50)))*283583
bidenca50votes = (len(bidenca50)/(len(trumpca50)+len(bidenca50)))*283583
print("Trump: ", (len(trumpca50)/(len(trumpca50)+len(bidenca50))))
print("votes ", trumpca50votes)
print("Biden: ",(len(bidenca50)/(len(trumpca50)+len(bidenca50))))
print("votes ", bidenca50votes)
print("California 51")
trumpca51votes = (len(trumpca51)/(len(trumpca51)+len(bidenca51)))*199524
bidenca51votes = (len(bidenca51)/(len(trumpca51)+len(bidenca51)))*199524
print("Trump: ", (len(trumpca51)/(len(trumpca51)+len(bidenca51))))
print("votes ", trumpca51votes)
print("Biden: ",(len(bidenca51)/(len(trumpca51)+len(bidenca51))))
print("votes ", bidenca51votes)
print("California 52")
trumpca52votes = (len(trumpca52)/(len(trumpca52)+len(bidenca52)))*320656
bidenca52votes = (len(bidenca52)/(len(trumpca52)+len(bidenca52)))*320656
print("Trump: ", (len(trumpca52)/(len(trumpca52)+len(bidenca52))))
print("votes ", trumpca52votes)
print("Biden: ",(len(bidenca52)/(len(trumpca52)+len(bidenca52))))
print("votes ", bidenca52votes)
print("California 53")
trumpca53votes = (len(trumpca53)/(len(trumpca53)+len(bidenca53)))*296956
bidenca53votes = (len(bidenca53)/(len(trumpca53)+len(bidenca53)))*296956
print("Trump: ", (len(trumpca53)/(len(trumpca53)+len(bidenca53))))
print("votes ", trumpca53votes)
print("Biden: ",(len(bidenca53)/(len(trumpca53)+len(bidenca53))))
print("votes ", bidenca53votes)
totalcavotestrump = trumpca1votes+trumpca2votes+trumpca3votes+trumpca4votes+trumpca5votes+trumpca6votes+trumpca7votes+trumpca8votes+trumpca9votes+trumpca10votes+trumpca11votes+trumpca12votes+trumpca13votes+trumpca14votes+trumpca15votes+trumpca16votes+trumpca17votes+trumpca18votes+trumpca19votes+trumpca20votes+trumpca21votes+trumpca22votes+trumpca23votes+trumpca24votes+trumpca25votes+trumpca26votes+trumpca27votes+trumpca28votes+trumpca29votes+trumpca30votes+trumpca31votes+trumpca32votes+trumpca33votes+trumpca34votes+trumpca35votes+trumpca36votes+trumpca37votes+trumpca38votes+trumpca39votes+trumpca40votes+trumpca41votes+trumpca42votes+trumpca43votes+trumpca44votes+trumpca45votes+trumpca46votes+trumpca47votes+trumpca48votes+trumpca49votes+trumpca50votes+trumpca51votes+trumpca52votes+trumpca53votes
totalcavotesbiden = bidenca1votes+bidenca2votes+bidenca3votes+bidenca4votes+bidenca5votes+bidenca6votes+bidenca7votes+bidenca8votes+bidenca9votes+bidenca10votes+bidenca11votes+bidenca12votes+bidenca13votes+bidenca14votes+bidenca15votes+bidenca16votes+bidenca17votes+bidenca18votes+bidenca19votes+bidenca20votes+bidenca21votes+bidenca22votes+bidenca23votes+bidenca24votes+bidenca25votes+bidenca26votes+bidenca27votes+bidenca28votes+bidenca29votes+bidenca30votes+bidenca31votes+bidenca32votes+bidenca33votes+bidenca34votes+bidenca35votes+bidenca36votes+bidenca37votes+bidenca38votes+bidenca39votes+bidenca40votes+bidenca41votes+bidenca42votes+bidenca43votes+bidenca44votes+bidenca45votes+bidenca46votes+bidenca47votes+bidenca48votes+bidenca49votes+bidenca50votes+bidenca51votes+bidenca52votes+bidenca53votes
print("TOTAL TRUMP VOTES: ", totalcavotestrump/(totalcavotestrump+totalcavotesbiden))
print("TOTAL BIDEN VOTES: ", totalcavotesbiden/(totalcavotestrump+totalcavotesbiden))
print("")
print("Virginia")
print("Trump: ", (len(trumpva)/(len(trumpva)+len(bidenva))))
print("Biden: ",(len(bidenva)/(len(trumpva)+len(bidenva))))
print("Virginia 1")
trumpva1votes = (len(trumpva1)/(len(trumpva1)+len(bidenva1)))*1
bidenva1votes = (len(bidenva1)/(len(trumpva1)+len(bidenva1)))*1
print("Trump: ", (len(trumpva1)/(len(trumpva1)+len(bidenva1))))
print("votes ", trumpva1votes)
print("Biden: ",(len(bidenva1)/(len(trumpva1)+len(bidenva1))))
print("votes ", bidenva1votes)
print("Virginia 2")
trumpva2votes = (len(trumpva2)/(len(trumpva2)+len(bidenva2)))*1
bidenva2votes = (len(bidenva2)/(len(trumpva2)+len(bidenva2)))*1
print("Trump: ", (len(trumpva2)/(len(trumpva2)+len(bidenva2))))
print("votes ", trumpva2votes)
print("Biden: ",(len(bidenva2)/(len(trumpva2)+len(bidenva2))))
print("votes ", bidenva2votes)
print("Virginia 3")
trumpva3votes = (len(trumpva3)/(len(trumpva3)+len(bidenva3)))*1
bidenva3votes = (len(bidenva3)/(len(trumpva3)+len(bidenva3)))*1
print("Trump: ", (len(trumpva3)/(len(trumpva3)+len(bidenva3))))
print("votes ", trumpva3votes)
print("Biden: ",(len(bidenva3)/(len(trumpva3)+len(bidenva3))))
print("votes ", bidenva3votes)
print("Virginia 4")
trumpva4votes = (len(trumpva4)/(len(trumpva4)+len(bidenva4)))*1
bidenva4votes = (len(bidenva4)/(len(trumpva4)+len(bidenva4)))*1
print("Trump: ", (len(trumpva4)/(len(trumpva4)+len(bidenva4))))
print("votes ", trumpva4votes)
print("Biden: ",(len(bidenva4)/(len(trumpva4)+len(bidenva4))))
print("votes ", bidenva4votes)
print("Virginia 5")
trumpva5votes = (len(trumpva5)/(len(trumpva5)+len(bidenva5)))*1
bidenva5votes = (len(bidenva5)/(len(trumpva5)+len(bidenva5)))*1
print("Trump: ", (len(trumpva5)/(len(trumpva5)+len(bidenva5))))
print("votes ", trumpva5votes)
print("Biden: ",(len(bidenva5)/(len(trumpva5)+len(bidenva5))))
print("votes ", bidenva5votes)
print("Virginia 6")
trumpva6votes = (len(trumpva6)/(len(trumpva6)+len(bidenva6)))*1
bidenva6votes = (len(bidenva6)/(len(trumpva6)+len(bidenva6)))*1
print("Trump: ", (len(trumpva6)/(len(trumpva6)+len(bidenva6))))
print("votes ", trumpva6votes)
print("Biden: ",(len(bidenva6)/(len(trumpva6)+len(bidenva6))))
print("votes ", bidenva6votes)
print("Virginia 7")
trumpva7votes = (len(trumpva7)/(len(trumpva7)+len(bidenva7)))*1
bidenva7votes = (len(bidenva7)/(len(trumpva7)+len(bidenva7)))*1
print("Trump: ", (len(trumpva7)/(len(trumpva7)+len(bidenva7))))
print("votes ", trumpva7votes)
print("Biden: ",(len(bidenva7)/(len(trumpva7)+len(bidenva7))))
print("votes ", bidenva7votes)
print("Virginia 8")
trumpva8votes = (len(trumpva8)/(len(trumpva8)+len(bidenva8)))*1
bidenva8votes = (len(bidenva8)/(len(trumpva8)+len(bidenva8)))*1
print("Trump: ", (len(trumpva8)/(len(trumpva8)+len(bidenva8))))
print("votes ", trumpva8votes)
print("Biden: ",(len(bidenva8)/(len(trumpva8)+len(bidenva8))))
print("votes ", bidenva8votes)
print("Virginia 9")
trumpva9votes = (len(trumpva9)/(len(trumpva9)+len(bidenva9)))*1
bidenva9votes = (len(bidenva9)/(len(trumpva9)+len(bidenva9)))*1
print("Trump: ", (len(trumpva9)/(len(trumpva9)+len(bidenva9))))
print("votes ", trumpva9votes)
print("Biden: ",(len(bidenva9)/(len(trumpva9)+len(bidenva9))))
print("votes ", bidenva9votes)
print("Virginia 10")
trumpva10votes = (len(trumpva10)/(len(trumpva10)+len(bidenva10)))*1
bidenva10votes = (len(bidenva10)/(len(trumpva10)+len(bidenva10)))*1
print("Trump: ", (len(trumpva10)/(len(trumpva10)+len(bidenva10))))
print("votes ", trumpva10votes)
print("Biden: ",(len(bidenva10)/(len(trumpva10)+len(bidenva10))))
print("votes ", bidenva10votes)
print("Virginia 11")
trumpva11votes = (len(trumpva11)/(len(trumpva11)+len(bidenva11)))*1
bidenva11votes = (len(bidenva11)/(len(trumpva11)+len(bidenva11)))*1
print("Trump: ", (len(trumpva11)/(len(trumpva11)+len(bidenva11))))
print("votes ", trumpva11votes)
print("Biden: ",(len(bidenva11)/(len(trumpva11)+len(bidenva11))))
print("votes ", bidenva11votes)
totalvavotestrump = trumpva1votes+trumpva2votes+trumpva3votes+trumpva4votes+trumpva5votes+trumpva6votes+trumpva7votes+trumpva8votes+trumpva9votes+trumpva10votes+trumpva11votes
totalvavotesbiden = bidenva1votes+bidenva2votes+bidenva3votes+bidenva4votes+bidenva5votes+bidenva6votes+bidenva7votes+bidenva8votes+bidenva9votes+bidenva10votes+bidenva11votes
print("TOTAL TRUMP VOTES: ", totalvavotestrump/(totalvavotestrump+totalvavotesbiden))
print("TOTAL BIDEN VOTES: ", totalvavotesbiden/(totalvavotestrump+totalvavotesbiden))
print("")
print("Georgia")
print("Trump: ", (len(trumpga)/(len(trumpga)+len(bidenga))))
print("Biden: ",(len(bidenga)/(len(trumpga)+len(bidenga))))
print("Georgia 1")
trumpga1votes = (len(trumpga1)/(len(trumpga1)+len(bidenga1)))*1
bidenga1votes = (len(bidenga1)/(len(trumpga1)+len(bidenga1)))*1
print("Trump: ", (len(trumpga1)/(len(trumpga1)+len(bidenga1))))
print("votes ", trumpga1votes)
print("Biden: ",(len(bidenga1)/(len(trumpga1)+len(bidenga1))))
print("votes ", bidenga1votes)
print("Georgia 2")
trumpga2votes = (len(trumpga2)/(len(trumpga2)+len(bidenga2)))*1
bidenga2votes = (len(bidenga2)/(len(trumpga2)+len(bidenga2)))*1
print("Trump: ", (len(trumpga2)/(len(trumpga2)+len(bidenga2))))
print("votes ", trumpga2votes)
print("Biden: ",(len(bidenga2)/(len(trumpga2)+len(bidenga2))))
print("votes ", bidenga2votes)
print("Georgia 3")
trumpga3votes = (len(trumpga3)/(len(trumpga3)+len(bidenga3)))*1
bidenga3votes = (len(bidenga3)/(len(trumpga3)+len(bidenga3)))*1
print("Trump: ", (len(trumpga3)/(len(trumpga3)+len(bidenga3))))
print("votes ", trumpga3votes)
print("Biden: ",(len(bidenga3)/(len(trumpga3)+len(bidenga3))))
print("votes ", bidenga3votes)
print("Georgia 4")
trumpga4votes = (len(trumpga4)/(len(trumpga4)+len(bidenga4)))*1
bidenga4votes = (len(bidenga4)/(len(trumpga4)+len(bidenga4)))*1
print("Trump: ", (len(trumpga4)/(len(trumpga4)+len(bidenga4))))
print("votes ", trumpga4votes)
print("Biden: ",(len(bidenga4)/(len(trumpga4)+len(bidenga4))))
print("votes ", bidenga4votes)
print("Georgia 5")
trumpga5votes = (len(trumpga5)/(len(trumpga5)+len(bidenga5)))*1
bidenga5votes = (len(bidenga5)/(len(trumpga5)+len(bidenga5)))*1
print("Trump: ", (len(trumpga5)/(len(trumpga5)+len(bidenga5))))
print("votes ", trumpga5votes)
print("Biden: ",(len(bidenga5)/(len(trumpga5)+len(bidenga5))))
print("votes ", bidenga5votes)
print("Georgia 6")
trumpga6votes = (len(trumpga6)/(len(trumpga6)+len(bidenga6)))*1
bidenga6votes = (len(bidenga6)/(len(trumpga6)+len(bidenga6)))*1
print("Trump: ", (len(trumpga6)/(len(trumpga6)+len(bidenga6))))
print("votes ", trumpga6votes)
print("Biden: ",(len(bidenga6)/(len(trumpga6)+len(bidenga6))))
print("votes ", bidenga6votes)
print("Georgia 7")
trumpga7votes = (len(trumpga7)/(len(trumpga7)+len(bidenga7)))*1
bidenga7votes = (len(bidenga7)/(len(trumpga7)+len(bidenga7)))*1
print("Trump: ", (len(trumpga7)/(len(trumpga7)+len(bidenga7))))
print("votes ", trumpga7votes)
print("Biden: ",(len(bidenga7)/(len(trumpga7)+len(bidenga7))))
print("votes ", bidenga7votes)
print("Georgia 8")
trumpga8votes = (len(trumpga8)/(len(trumpga8)+len(bidenga8)))*1
bidenga8votes = (len(bidenga8)/(len(trumpga8)+len(bidenga8)))*1
print("Trump: ", (len(trumpga8)/(len(trumpga8)+len(bidenga8))))
print("votes ", trumpga8votes)
print("Biden: ",(len(bidenga8)/(len(trumpga8)+len(bidenga8))))
print("votes ", bidenga8votes)
print("Georgia 9")
trumpga9votes = (len(trumpga9)/(len(trumpga9)+len(bidenga9)))*1
bidenga9votes = (len(bidenga9)/(len(trumpga9)+len(bidenga9)))*1
print("Trump: ", (len(trumpga9)/(len(trumpga9)+len(bidenga9))))
print("votes ", trumpga9votes)
print("Biden: ",(len(bidenga9)/(len(trumpga9)+len(bidenga9))))
print("votes ", bidenga9votes)
print("Georgia 10")
trumpga10votes = (len(trumpga10)/(len(trumpga10)+len(bidenga10)))*1
bidenga10votes = (len(bidenga10)/(len(trumpga10)+len(bidenga10)))*1
print("Trump: ", (len(trumpga10)/(len(trumpga10)+len(bidenga10))))
print("votes ", trumpga10votes)
print("Biden: ",(len(bidenga10)/(len(trumpga10)+len(bidenga10))))
print("votes ", bidenga10votes)
print("Georgia 11")
trumpga11votes = (len(trumpga11)/(len(trumpga11)+len(bidenga11)))*1
bidenga11votes = (len(bidenga11)/(len(trumpga11)+len(bidenga11)))*1
print("Trump: ", (len(trumpga11)/(len(trumpga11)+len(bidenga11))))
print("votes ", trumpga11votes)
print("Biden: ",(len(bidenga11)/(len(trumpga11)+len(bidenga11))))
print("votes ", bidenga11votes)
print("Georgia 12")
trumpga12votes = (len(trumpga12)/(len(trumpga12)+len(bidenga12)))*1
bidenga12votes = (len(bidenga12)/(len(trumpga12)+len(bidenga12)))*1
print("Trump: ", (len(trumpga12)/(len(trumpga12)+len(bidenga12))))
print("votes ", trumpga12votes)
print("Biden: ",(len(bidenga12)/(len(trumpga12)+len(bidenga12))))
print("votes ", bidenga12votes)
print("Georgia 13")
trumpga13votes = (len(trumpga13)/(len(trumpga13)+len(bidenga13)))*1
bidenga13votes = (len(bidenga13)/(len(trumpga13)+len(bidenga13)))*1
print("Trump: ", (len(trumpga13)/(len(trumpga13)+len(bidenga13))))
print("votes ", trumpga13votes)
print("Biden: ",(len(bidenga13)/(len(trumpga13)+len(bidenga13))))
print("votes ", bidenga13votes)
print("Georgia 14")
trumpga14votes = (len(trumpga14)/(len(trumpga14)+len(bidenga14)))*1
bidenga14votes = (len(bidenga14)/(len(trumpga14)+len(bidenga14)))*1
print("Trump: ", (len(trumpga14)/(len(trumpga14)+len(bidenga14))))
print("votes ", trumpga14votes)
print("Biden: ",(len(bidenga14)/(len(trumpga14)+len(bidenga14))))
print("votes ", bidenga14votes)
totalgavotestrump = trumpga1votes+trumpga2votes+trumpga3votes+trumpga4votes+trumpga5votes+trumpga6votes+trumpga7votes+trumpga8votes+trumpga9votes+trumpga10votes+trumpga11votes+trumpga12votes+trumpga13votes+trumpga14votes
totalgavotesbiden = bidenga1votes+bidenga2votes+bidenga3votes+bidenga4votes+bidenga5votes+bidenga6votes+bidenga7votes+bidenga8votes+bidenga9votes+bidenga10votes+bidenga11votes+bidenga12votes+bidenga13votes+bidenga14votes
print("TOTAL TRUMP VOTES: ", totalgavotestrump/(totalgavotestrump+totalgavotesbiden))
print("TOTAL BIDEN VOTES: ", totalgavotesbiden/(totalgavotestrump+totalgavotesbiden))
print("")
print("Florida")
print("Trump: ", (len(trumpfl)/(len(trumpfl)+len(bidenfl))))
print("Biden: ",(len(bidenfl)/(len(trumpfl)+len(bidenfl))))
print("Florida 1")
trumpfl1votes = (len(trumpfl1)/(len(trumpfl1)+len(bidenfl1)))*1
bidenfl1votes = (len(bidenfl1)/(len(trumpfl1)+len(bidenfl1)))*1
print("Trump: ", (len(trumpfl1)/(len(trumpfl1)+len(bidenfl1))))
print("votes ", trumpfl1votes)
print("Biden: ",(len(bidenfl1)/(len(trumpfl1)+len(bidenfl1))))
print("votes ", bidenfl1votes)
print("Florida 2")
trumpfl2votes = (len(trumpfl2)/(len(trumpfl2)+len(bidenfl2)))*1
bidenfl2votes = (len(bidenfl2)/(len(trumpfl2)+len(bidenfl2)))*1
print("Trump: ", (len(trumpfl2)/(len(trumpfl2)+len(bidenfl2))))
print("votes ", trumpfl2votes)
print("Biden: ",(len(bidenfl2)/(len(trumpfl2)+len(bidenfl2))))
print("votes ", bidenfl2votes)
print("Florida 3")
trumpfl3votes = (len(trumpfl3)/(len(trumpfl3)+len(bidenfl3)))*1
bidenfl3votes = (len(bidenfl3)/(len(trumpfl3)+len(bidenfl3)))*1
print("Trump: ", (len(trumpfl3)/(len(trumpfl3)+len(bidenfl3))))
print("votes ", trumpfl3votes)
print("Biden: ",(len(bidenfl3)/(len(trumpfl3)+len(bidenfl3))))
print("votes ", bidenfl3votes)
print("Florida 4")
trumpfl4votes = (len(trumpfl4)/(len(trumpfl4)+len(bidenfl4)))*1
bidenfl4votes = (len(bidenfl4)/(len(trumpfl4)+len(bidenfl4)))*1
print("Trump: ", (len(trumpfl4)/(len(trumpfl4)+len(bidenfl4))))
print("votes ", trumpfl4votes)
print("Biden: ",(len(bidenfl4)/(len(trumpfl4)+len(bidenfl4))))
print("votes ", bidenfl4votes)
print("Florida 5")
trumpfl5votes = (len(trumpfl5)/(len(trumpfl5)+len(bidenfl5)))*1
bidenfl5votes = (len(bidenfl5)/(len(trumpfl5)+len(bidenfl5)))*1
print("Trump: ", (len(trumpfl5)/(len(trumpfl5)+len(bidenfl5))))
print("votes ", trumpfl5votes)
print("Biden: ",(len(bidenfl5)/(len(trumpfl5)+len(bidenfl5))))
print("votes ", bidenfl5votes)
print("Florida 6")
trumpfl6votes = (len(trumpfl6)/(len(trumpfl6)+len(bidenfl6)))*1
bidenfl6votes = (len(bidenfl6)/(len(trumpfl6)+len(bidenfl6)))*1
print("Trump: ", (len(trumpfl6)/(len(trumpfl6)+len(bidenfl6))))
print("votes ", trumpfl6votes)
print("Biden: ",(len(bidenfl6)/(len(trumpfl6)+len(bidenfl6))))
print("votes ", bidenfl6votes)
print("Florida 7")
trumpfl7votes = (len(trumpfl7)/(len(trumpfl7)+len(bidenfl7)))*1
bidenfl7votes = (len(bidenfl7)/(len(trumpfl7)+len(bidenfl7)))*1
print("Trump: ", (len(trumpfl7)/(len(trumpfl7)+len(bidenfl7))))
print("votes ", trumpfl7votes)
print("Biden: ",(len(bidenfl7)/(len(trumpfl7)+len(bidenfl7))))
print("votes ", bidenfl7votes)
print("Florida 8")
trumpfl8votes = (len(trumpfl8)/(len(trumpfl8)+len(bidenfl8)))*1
bidenfl8votes = (len(bidenfl8)/(len(trumpfl8)+len(bidenfl8)))*1
print("Trump: ", (len(trumpfl8)/(len(trumpfl8)+len(bidenfl8))))
print("votes ", trumpfl8votes)
print("Biden: ",(len(bidenfl8)/(len(trumpfl8)+len(bidenfl8))))
print("votes ", bidenfl8votes)
print("Florida 9")
trumpfl9votes = (len(trumpfl9)/(len(trumpfl9)+len(bidenfl9)))*1
bidenfl9votes = (len(bidenfl9)/(len(trumpfl9)+len(bidenfl9)))*1
print("Trump: ", (len(trumpfl9)/(len(trumpfl9)+len(bidenfl9))))
print("votes ", trumpfl9votes)
print("Biden: ",(len(bidenfl9)/(len(trumpfl9)+len(bidenfl9))))
print("votes ", bidenfl9votes)
print("Florida 10")
trumpfl10votes = (len(trumpfl10)/(len(trumpfl10)+len(bidenfl10)))*1
bidenfl10votes = (len(bidenfl10)/(len(trumpfl10)+len(bidenfl10)))*1
print("Trump: ", (len(trumpfl10)/(len(trumpfl10)+len(bidenfl10))))
print("votes ", trumpfl10votes)
print("Biden: ",(len(bidenfl10)/(len(trumpfl10)+len(bidenfl10))))
print("votes ", bidenfl10votes)
print("Florida 11")
trumpfl11votes = (len(trumpfl11)/(len(trumpfl11)+len(bidenfl11)))*1
bidenfl11votes = (len(bidenfl11)/(len(trumpfl11)+len(bidenfl11)))*1
print("Trump: ", (len(trumpfl11)/(len(trumpfl11)+len(bidenfl11))))
print("votes ", trumpfl11votes)
print("Biden: ",(len(bidenfl11)/(len(trumpfl11)+len(bidenfl11))))
print("votes ", bidenfl11votes)
print("Florida 12")
trumpfl12votes = (len(trumpfl12)/(len(trumpfl12)+len(bidenfl12)))*1
bidenfl12votes = (len(bidenfl12)/(len(trumpfl12)+len(bidenfl12)))*1
print("Trump: ", (len(trumpfl12)/(len(trumpfl12)+len(bidenfl12))))
print("votes ", trumpfl12votes)
print("Biden: ",(len(bidenfl12)/(len(trumpfl12)+len(bidenfl12))))
print("votes ", bidenfl12votes)
print("Florida 13")
trumpfl13votes = (len(trumpfl13)/(len(trumpfl13)+len(bidenfl13)))*1
bidenfl13votes = (len(bidenfl13)/(len(trumpfl13)+len(bidenfl13)))*1
print("Trump: ", (len(trumpfl13)/(len(trumpfl13)+len(bidenfl13))))
print("votes ", trumpfl13votes)
print("Biden: ",(len(bidenfl13)/(len(trumpfl13)+len(bidenfl13))))
print("votes ", bidenfl13votes)
print("Florida 14")
trumpfl14votes = (len(trumpfl14)/(len(trumpfl14)+len(bidenfl14)))*1
bidenfl14votes = (len(bidenfl14)/(len(trumpfl14)+len(bidenfl14)))*1
print("Trump: ", (len(trumpfl14)/(len(trumpfl14)+len(bidenfl14))))
print("votes ", trumpfl14votes)
print("Biden: ",(len(bidenfl14)/(len(trumpfl14)+len(bidenfl14))))
print("votes ", bidenfl14votes)
print("Florida 15")
trumpfl15votes = (len(trumpfl15)/(len(trumpfl15)+len(bidenfl15)))*1
bidenfl15votes = (len(bidenfl15)/(len(trumpfl15)+len(bidenfl15)))*1
print("Trump: ", (len(trumpfl15)/(len(trumpfl15)+len(bidenfl15))))
print("votes ", trumpfl15votes)
print("Biden: ",(len(bidenfl15)/(len(trumpfl15)+len(bidenfl15))))
print("votes ", bidenfl15votes)
print("Florida 16")
trumpfl16votes = (len(trumpfl16)/(len(trumpfl16)+len(bidenfl16)))*1
bidenfl16votes = (len(bidenfl16)/(len(trumpfl16)+len(bidenfl16)))*1
print("Trump: ", (len(trumpfl16)/(len(trumpfl16)+len(bidenfl16))))
print("votes ", trumpfl16votes)
print("Biden: ",(len(bidenfl16)/(len(trumpfl16)+len(bidenfl16))))
print("votes ", bidenfl16votes)
print("Florida 17")
trumpfl17votes = (len(trumpfl17)/(len(trumpfl17)+len(bidenfl17)))*1
bidenfl17votes = (len(bidenfl17)/(len(trumpfl17)+len(bidenfl17)))*1
print("Trump: ", (len(trumpfl17)/(len(trumpfl17)+len(bidenfl17))))
print("votes ", trumpfl17votes)
print("Biden: ",(len(bidenfl17)/(len(trumpfl17)+len(bidenfl17))))
print("votes ", bidenfl17votes)
print("Florida 18")
trumpfl18votes = (len(trumpfl18)/(len(trumpfl18)+len(bidenfl18)))*1
bidenfl18votes = (len(bidenfl18)/(len(trumpfl18)+len(bidenfl18)))*1
print("Trump: ", (len(trumpfl18)/(len(trumpfl18)+len(bidenfl18))))
print("votes ", trumpfl18votes)
print("Biden: ",(len(bidenfl18)/(len(trumpfl18)+len(bidenfl18))))
print("votes ", bidenfl18votes)
print("Florida 19")
trumpfl19votes = (len(trumpfl19)/(len(trumpfl19)+len(bidenfl19)))*1
bidenfl19votes = (len(bidenfl19)/(len(trumpfl19)+len(bidenfl19)))*1
print("Trump: ", (len(trumpfl19)/(len(trumpfl19)+len(bidenfl19))))
print("votes ", trumpfl19votes)
print("Biden: ",(len(bidenfl19)/(len(trumpfl19)+len(bidenfl19))))
print("votes ", bidenfl19votes)
print("Florida 20")
trumpfl20votes = (len(trumpfl20)/(len(trumpfl20)+len(bidenfl20)))*1
bidenfl20votes = (len(bidenfl20)/(len(trumpfl20)+len(bidenfl20)))*1
print("Trump: ", (len(trumpfl20)/(len(trumpfl20)+len(bidenfl20))))
print("votes ", trumpfl20votes)
print("Biden: ",(len(bidenfl20)/(len(trumpfl20)+len(bidenfl20))))
print("votes ", bidenfl20votes)
print("Florida 21")
trumpfl21votes = (len(trumpfl21)/(len(trumpfl21)+len(bidenfl21)))*1
bidenfl21votes = (len(bidenfl21)/(len(trumpfl21)+len(bidenfl21)))*1
print("Trump: ", (len(trumpfl21)/(len(trumpfl21)+len(bidenfl21))))
print("votes ", trumpfl21votes)
print("Biden: ",(len(bidenfl21)/(len(trumpfl21)+len(bidenfl21))))
print("votes ", bidenfl21votes)
print("Florida 22")
trumpfl22votes = (len(trumpfl22)/(len(trumpfl22)+len(bidenfl22)))*1
bidenfl22votes = (len(bidenfl22)/(len(trumpfl22)+len(bidenfl22)))*1
print("Trump: ", (len(trumpfl22)/(len(trumpfl22)+len(bidenfl22))))
print("votes ", trumpfl22votes)
print("Biden: ",(len(bidenfl22)/(len(trumpfl22)+len(bidenfl22))))
print("votes ", bidenfl22votes)
print("Florida 23")
trumpfl23votes = (len(trumpfl23)/(len(trumpfl23)+len(bidenfl23)))*1
bidenfl23votes = (len(bidenfl23)/(len(trumpfl23)+len(bidenfl23)))*1
print("Trump: ", (len(trumpfl23)/(len(trumpfl23)+len(bidenfl23))))
print("votes ", trumpfl23votes)
print("Biden: ",(len(bidenfl23)/(len(trumpfl23)+len(bidenfl23))))
print("votes ", bidenfl23votes)
print("Florida 24")
trumpfl24votes = (len(trumpfl24)/(len(trumpfl24)+len(bidenfl24)))*1
bidenfl24votes = (len(bidenfl24)/(len(trumpfl24)+len(bidenfl24)))*1
print("Trump: ", (len(trumpfl24)/(len(trumpfl24)+len(bidenfl24))))
print("votes ", trumpfl24votes)
print("Biden: ",(len(bidenfl24)/(len(trumpfl24)+len(bidenfl24))))
print("votes ", bidenfl24votes)
print("Florida 25")
trumpfl25votes = (len(trumpfl25)/(len(trumpfl25)+len(bidenfl25)))*1
bidenfl25votes = (len(bidenfl25)/(len(trumpfl25)+len(bidenfl25)))*1
print("Trump: ", (len(trumpfl25)/(len(trumpfl25)+len(bidenfl25))))
print("votes ", trumpfl25votes)
print("Biden: ",(len(bidenfl25)/(len(trumpfl25)+len(bidenfl25))))
print("votes ", bidenfl25votes)
print("Florida 26")
trumpfl26votes = (len(trumpfl26)/(len(trumpfl26)+len(bidenfl26)))*1
bidenfl26votes = (len(bidenfl26)/(len(trumpfl26)+len(bidenfl26)))*1
print("Trump: ", (len(trumpfl26)/(len(trumpfl26)+len(bidenfl26))))
print("votes ", trumpfl26votes)
print("Biden: ",(len(bidenfl26)/(len(trumpfl26)+len(bidenfl26))))
print("votes ", bidenfl26votes)
print("Florida 27")
trumpfl27votes = (len(trumpfl27)/(len(trumpfl27)+len(bidenfl27)))*1
bidenfl27votes = (len(bidenfl27)/(len(trumpfl27)+len(bidenfl27)))*1
print("Trump: ", (len(trumpfl27)/(len(trumpfl27)+len(bidenfl27))))
print("votes ", trumpfl27votes)
print("Biden: ",(len(bidenfl27)/(len(trumpfl27)+len(bidenfl27))))
print("votes ", bidenfl27votes)
totalflvotestrump = trumpfl1votes+trumpfl2votes+trumpfl3votes+trumpfl4votes+trumpfl5votes+trumpfl6votes+trumpfl7votes+trumpfl8votes+trumpfl9votes+trumpfl10votes+trumpfl11votes+trumpfl12votes+trumpfl13votes+trumpfl14votes+trumpfl15votes+trumpfl16votes+trumpfl17votes+trumpfl18votes+trumpfl19votes+trumpfl20votes+trumpfl21votes+trumpfl22votes+trumpfl23votes+trumpfl24votes+trumpfl25votes+trumpfl26votes+trumpfl27votes
totalflvotesbiden = bidenfl1votes+bidenfl2votes+bidenfl3votes+bidenfl4votes+bidenfl5votes+bidenfl6votes+bidenfl7votes+bidenfl8votes+bidenfl9votes+bidenfl10votes+bidenfl11votes+bidenfl12votes+bidenfl13votes+bidenfl14votes+bidenfl15votes+bidenfl16votes+bidenfl17votes+bidenfl18votes+bidenfl19votes+bidenfl20votes+bidenfl21votes+bidenfl22votes+bidenfl23votes+bidenfl24votes+bidenfl25votes+bidenfl26votes+bidenfl27votes
print("TOTAL TRUMP VOTES: ", totalflvotestrump/(totalflvotestrump+totalflvotesbiden))
print("TOTAL BIDEN VOTES: ", totalflvotesbiden/(totalflvotestrump+totalflvotesbiden))
print("")
print("Mississippi")
print("Trump: ", (len(trumpms)/(len(trumpms)+len(bidenms))))
print("Biden: ",(len(bidenms)/(len(trumpms)+len(bidenms))))
print("Mississippi 1")
trumpms1votes = (len(trumpms1)/(len(trumpms1)+len(bidenms1)))*285275
bidenms1votes = (len(bidenms1)/(len(trumpms1)+len(bidenms1)))*285275
print("Trump: ", (len(trumpms1)/(len(trumpms1)+len(bidenms1))))
print("votes ", trumpms1votes)
print("Biden: ",(len(bidenms1)/(len(trumpms1)+len(bidenms1))))
print("votes ", bidenms1votes)
print("Mississippi 2")
trumpms2votes = (len(trumpms2)/(len(trumpms2)+len(bidenms2)))*260881
bidenms2votes = (len(bidenms2)/(len(trumpms2)+len(bidenms2)))*260881
print("Trump: ", (len(trumpms2)/(len(trumpms2)+len(bidenms2))))
print("votes ", trumpms2votes)
print("Biden: ",(len(bidenms2)/(len(trumpms2)+len(bidenms2))))
print("votes ", bidenms2votes)
print("Mississippi 3")
trumpms3votes = (len(trumpms3)/(len(trumpms3)+len(bidenms3)))*293272
bidenms3votes = (len(bidenms3)/(len(trumpms3)+len(bidenms3)))*293272
print("Trump: ", (len(trumpms3)/(len(trumpms3)+len(bidenms3))))
print("votes ", trumpms3votes)
print("Biden: ",(len(bidenms3)/(len(trumpms3)+len(bidenms3))))
print("votes ", bidenms3votes)
print("Mississippi 4")
trumpms4votes = (len(trumpms4)/(len(trumpms4)+len(bidenms4)))*248959
bidenms4votes = (len(bidenms4)/(len(trumpms4)+len(bidenms4)))*248959
print("Trump: ", (len(trumpms4)/(len(trumpms4)+len(bidenms4))))
print("votes ", trumpms4votes)
print("Biden: ",(len(bidenms4)/(len(trumpms4)+len(bidenms4))))
print("votes ", bidenms4votes)
totalmsvotestrump = trumpms1votes+trumpms2votes+trumpms3votes+trumpms4votes
totalmsvotesbiden = bidenms1votes+bidenms2votes+bidenms3votes+bidenms4votes
print("TOTAL TRUMP VOTES: ", totalmsvotestrump/(totalmsvotestrump+totalmsvotesbiden))
print("TOTAL BIDEN VOTES: ", totalmsvotesbiden/(totalmsvotestrump+totalmsvotesbiden))
print("")
print("Pennsylvania")
print("Trump: ", (len(trumppa)/(len(trumppa)+len(bidenpa))))
print("Biden: ",(len(bidenpa)/(len(trumppa)+len(bidenpa))))
print("Pennsylvania 1")
trumppa1votes = (len(trumppa1)/(len(trumppa1)+len(bidenpa1)))*1
bidenpa1votes = (len(bidenpa1)/(len(trumppa1)+len(bidenpa1)))*1
print("Trump: ", (len(trumppa1)/(len(trumppa1)+len(bidenpa1))))
print("votes ", trumppa1votes)
print("Biden: ",(len(bidenpa1)/(len(trumppa1)+len(bidenpa1))))
print("votes ", bidenpa1votes)
print("Pennsylvania 2")
trumppa2votes = (len(trumppa2)/(len(trumppa2)+len(bidenpa2)))*1
bidenpa2votes = (len(bidenpa2)/(len(trumppa2)+len(bidenpa2)))*1
print("Trump: ", (len(trumppa2)/(len(trumppa2)+len(bidenpa2))))
print("votes ", trumppa2votes)
print("Biden: ",(len(bidenpa2)/(len(trumppa2)+len(bidenpa2))))
print("votes ", bidenpa2votes)
print("Pennsylvania 3")
trumppa3votes = (len(trumppa3)/(len(trumppa3)+len(bidenpa3)))*1
bidenpa3votes = (len(bidenpa3)/(len(trumppa3)+len(bidenpa3)))*1
print("Trump: ", (len(trumppa3)/(len(trumppa3)+len(bidenpa3))))
print("votes ", trumppa3votes)
print("Biden: ",(len(bidenpa3)/(len(trumppa3)+len(bidenpa3))))
print("votes ", bidenpa3votes)
print("Pennsylvania 4")
trumppa4votes = (len(trumppa4)/(len(trumppa4)+len(bidenpa4)))*1
bidenpa4votes = (len(bidenpa4)/(len(trumppa4)+len(bidenpa4)))*1
print("Trump: ", (len(trumppa4)/(len(trumppa4)+len(bidenpa4))))
print("votes ", trumppa4votes)
print("Biden: ",(len(bidenpa4)/(len(trumppa4)+len(bidenpa4))))
print("votes ", bidenpa4votes)
print("Pennsylvania 5")
trumppa5votes = (len(trumppa5)/(len(trumppa5)+len(bidenpa5)))*1
bidenpa5votes = (len(bidenpa5)/(len(trumppa5)+len(bidenpa5)))*1
print("Trump: ", (len(trumppa5)/(len(trumppa5)+len(bidenpa5))))
print("votes ", trumppa5votes)
print("Biden: ",(len(bidenpa5)/(len(trumppa5)+len(bidenpa5))))
print("votes ", bidenpa5votes)
print("Pennsylvania 6")
trumppa6votes = (len(trumppa6)/(len(trumppa6)+len(bidenpa6)))*1
bidenpa6votes = (len(bidenpa6)/(len(trumppa6)+len(bidenpa6)))*1
print("Trump: ", (len(trumppa6)/(len(trumppa6)+len(bidenpa6))))
print("votes ", trumppa6votes)
print("Biden: ",(len(bidenpa6)/(len(trumppa6)+len(bidenpa6))))
print("votes ", bidenpa6votes)
print("Pennsylvania 7")
trumppa7votes = (len(trumppa7)/(len(trumppa7)+len(bidenpa7)))*1
bidenpa7votes = (len(bidenpa7)/(len(trumppa7)+len(bidenpa7)))*1
print("Trump: ", (len(trumppa7)/(len(trumppa7)+len(bidenpa7))))
print("votes ", trumppa7votes)
print("Biden: ",(len(bidenpa7)/(len(trumppa7)+len(bidenpa7))))
print("votes ", bidenpa7votes)
print("Pennsylvania 8")
trumppa8votes = (len(trumppa8)/(len(trumppa8)+len(bidenpa8)))*1
bidenpa8votes = (len(bidenpa8)/(len(trumppa8)+len(bidenpa8)))*1
print("Trump: ", (len(trumppa8)/(len(trumppa8)+len(bidenpa8))))
print("votes ", trumppa8votes)
print("Biden: ",(len(bidenpa8)/(len(trumppa8)+len(bidenpa8))))
print("votes ", bidenpa8votes)
print("Pennsylvania 9")
trumppa9votes = (len(trumppa9)/(len(trumppa9)+len(bidenpa9)))*1
bidenpa9votes = (len(bidenpa9)/(len(trumppa9)+len(bidenpa9)))*1
print("Trump: ", (len(trumppa9)/(len(trumppa9)+len(bidenpa9))))
print("votes ", trumppa9votes)
print("Biden: ",(len(bidenpa9)/(len(trumppa9)+len(bidenpa9))))
print("votes ", bidenpa9votes)
print("Pennsylvania 10")
trumppa10votes = (len(trumppa10)/(len(trumppa10)+len(bidenpa10)))*1
bidenpa10votes = (len(bidenpa10)/(len(trumppa10)+len(bidenpa10)))*1
print("Trump: ", (len(trumppa10)/(len(trumppa10)+len(bidenpa10))))
print("votes ", trumppa10votes)
print("Biden: ",(len(bidenpa10)/(len(trumppa10)+len(bidenpa10))))
print("votes ", bidenpa10votes)
print("Pennsylvania 11")
trumppa11votes = (len(trumppa11)/(len(trumppa11)+len(bidenpa11)))*1
bidenpa11votes = (len(bidenpa11)/(len(trumppa11)+len(bidenpa11)))*1
print("Trump: ", (len(trumppa11)/(len(trumppa11)+len(bidenpa11))))
print("votes ", trumppa11votes)
print("Biden: ",(len(bidenpa11)/(len(trumppa11)+len(bidenpa11))))
print("votes ", bidenpa11votes)
print("Pennsylvania 12")
trumppa12votes = (len(trumppa12)/(len(trumppa12)+len(bidenpa12)))*1
bidenpa12votes = (len(bidenpa12)/(len(trumppa12)+len(bidenpa12)))*1
print("Trump: ", (len(trumppa12)/(len(trumppa12)+len(bidenpa12))))
print("votes ", trumppa12votes)
print("Biden: ",(len(bidenpa12)/(len(trumppa12)+len(bidenpa12))))
print("votes ", bidenpa12votes)
print("Pennsylvania 13")
trumppa13votes = (len(trumppa13)/(len(trumppa13)+len(bidenpa13)))*1
bidenpa13votes = (len(bidenpa13)/(len(trumppa13)+len(bidenpa13)))*1
print("Trump: ", (len(trumppa13)/(len(trumppa13)+len(bidenpa13))))
print("votes ", trumppa13votes)
print("Biden: ",(len(bidenpa13)/(len(trumppa13)+len(bidenpa13))))
print("votes ", bidenpa13votes)
print("Pennsylvania 14")
trumppa14votes = (len(trumppa14)/(len(trumppa14)+len(bidenpa14)))*1
bidenpa14votes = (len(bidenpa14)/(len(trumppa14)+len(bidenpa14)))*1
print("Trump: ", (len(trumppa14)/(len(trumppa14)+len(bidenpa14))))
print("votes ", trumppa14votes)
print("Biden: ",(len(bidenpa14)/(len(trumppa14)+len(bidenpa14))))
print("votes ", bidenpa14votes)
print("Pennsylvania 15")
trumppa15votes = (len(trumppa15)/(len(trumppa15)+len(bidenpa15)))*1
bidenpa15votes = (len(bidenpa15)/(len(trumppa15)+len(bidenpa15)))*1
print("Trump: ", (len(trumppa15)/(len(trumppa15)+len(bidenpa15))))
print("votes ", trumppa15votes)
print("Biden: ",(len(bidenpa15)/(len(trumppa15)+len(bidenpa15))))
print("votes ", bidenpa15votes)
print("Pennsylvania 16")
trumppa16votes = (len(trumppa16)/(len(trumppa16)+len(bidenpa16)))*1
bidenpa16votes = (len(bidenpa16)/(len(trumppa16)+len(bidenpa16)))*1
print("Trump: ", (len(trumppa16)/(len(trumppa16)+len(bidenpa16))))
print("votes ", trumppa16votes)
print("Biden: ",(len(bidenpa16)/(len(trumppa16)+len(bidenpa16))))
print("votes ", bidenpa16votes)
print("Pennsylvania 17")
trumppa17votes = (len(trumppa17)/(len(trumppa17)+len(bidenpa17)))*1
bidenpa17votes = (len(bidenpa17)/(len(trumppa17)+len(bidenpa17)))*1
print("Trump: ", (len(trumppa17)/(len(trumppa17)+len(bidenpa17))))
print("votes ", trumppa17votes)
print("Biden: ",(len(bidenpa17)/(len(trumppa17)+len(bidenpa17))))
print("votes ", bidenpa17votes)
print("Pennsylvania 18")
trumppa18votes = (len(trumppa18)/(len(trumppa18)+len(bidenpa18)))*1
bidenpa18votes = (len(bidenpa18)/(len(trumppa18)+len(bidenpa18)))*1
print("Trump: ", (len(trumppa18)/(len(trumppa18)+len(bidenpa18))))
print("votes ", trumppa18votes)
print("Biden: ",(len(bidenpa18)/(len(trumppa18)+len(bidenpa18))))
print("votes ", bidenpa18votes)
totalpavotestrump = trumppa1votes+trumppa2votes+trumppa3votes+trumppa4votes+trumppa5votes+trumppa6votes+trumppa7votes+trumppa8votes+trumppa9votes+trumppa10votes+trumppa11votes+trumppa12votes+trumppa13votes+trumppa14votes+trumppa15votes+trumppa16votes+trumppa17votes+trumppa18votes
totalpavotesbiden = bidenpa1votes+bidenpa2votes+bidenpa3votes+bidenpa4votes+bidenpa5votes+bidenpa6votes+bidenpa7votes+bidenpa8votes+bidenpa9votes+bidenpa10votes+bidenpa11votes+bidenpa12votes+bidenpa13votes+bidenpa14votes+bidenpa15votes+bidenpa16votes+bidenpa17votes+bidenpa18votes
print("TOTAL TRUMP VOTES: ", totalpavotestrump/(totalpavotestrump+totalpavotesbiden))
print("TOTAL BIDEN VOTES: ", totalpavotesbiden/(totalpavotestrump+totalpavotesbiden))
print("")
print("Arizona")
print("Trump: ", (len(trumpaz)/(len(trumpaz)+len(bidenaz))))
print("Biden: ",(len(bidenaz)/(len(trumpaz)+len(bidenaz))))
print("Arizona 1")
trumpaz1votes = (len(trumpaz1)/(len(trumpaz1)+len(bidenaz1)))*1
bidenaz1votes = (len(bidenaz1)/(len(trumpaz1)+len(bidenaz1)))*1
print("Trump: ", (len(trumpaz1)/(len(trumpaz1)+len(bidenaz1))))
print("votes ", trumpaz1votes)
print("Biden: ",(len(bidenaz1)/(len(trumpaz1)+len(bidenaz1))))
print("votes ", bidenaz1votes)
print("Arizona 2")
trumpaz2votes = (len(trumpaz2)/(len(trumpaz2)+len(bidenaz2)))*1
bidenaz2votes = (len(bidenaz2)/(len(trumpaz2)+len(bidenaz2)))*1
print("Trump: ", (len(trumpaz2)/(len(trumpaz2)+len(bidenaz2))))
print("votes ", trumpaz2votes)
print("Biden: ",(len(bidenaz2)/(len(trumpaz2)+len(bidenaz2))))
print("votes ", bidenaz2votes)
print("Arizona 3")
trumpaz3votes = (len(trumpaz3)/(len(trumpaz3)+len(bidenaz3)))*1
bidenaz3votes = (len(bidenaz3)/(len(trumpaz3)+len(bidenaz3)))*1
print("Trump: ", (len(trumpaz3)/(len(trumpaz3)+len(bidenaz3))))
print("votes ", trumpaz3votes)
print("Biden: ",(len(bidenaz3)/(len(trumpaz3)+len(bidenaz3))))
print("votes ", bidenaz3votes)
print("Arizona 4")
trumpaz4votes = (len(trumpaz4)/(len(trumpaz4)+len(bidenaz4)))*1
bidenaz4votes = (len(bidenaz4)/(len(trumpaz4)+len(bidenaz4)))*1
print("Trump: ", (len(trumpaz4)/(len(trumpaz4)+len(bidenaz4))))
print("votes ", trumpaz4votes)
print("Biden: ",(len(bidenaz4)/(len(trumpaz4)+len(bidenaz4))))
print("votes ", bidenaz4votes)
print("Arizona 5")
trumpaz5votes = (len(trumpaz5)/(len(trumpaz5)+len(bidenaz5)))*1
bidenaz5votes = (len(bidenaz5)/(len(trumpaz5)+len(bidenaz5)))*1
print("Trump: ", (len(trumpaz5)/(len(trumpaz5)+len(bidenaz5))))
print("votes ", trumpaz5votes)
print("Biden: ",(len(bidenaz5)/(len(trumpaz5)+len(bidenaz5))))
print("votes ", bidenaz5votes)
print("Arizona 6")
trumpaz6votes = (len(trumpaz6)/(len(trumpaz6)+len(bidenaz6)))*1
bidenaz6votes = (len(bidenaz6)/(len(trumpaz6)+len(bidenaz6)))*1
print("Trump: ", (len(trumpaz6)/(len(trumpaz6)+len(bidenaz6))))
print("votes ", trumpaz6votes)
print("Biden: ",(len(bidenaz6)/(len(trumpaz6)+len(bidenaz6))))
print("votes ", bidenaz6votes)
print("Arizona 7")
trumpaz7votes = (len(trumpaz7)/(len(trumpaz7)+len(bidenaz7)))*1
bidenaz7votes = (len(bidenaz7)/(len(trumpaz7)+len(bidenaz7)))*1
print("Trump: ", (len(trumpaz7)/(len(trumpaz7)+len(bidenaz7))))
print("votes ", trumpaz7votes)
print("Biden: ",(len(bidenaz7)/(len(trumpaz7)+len(bidenaz7))))
print("votes ", bidenaz7votes)
print("Arizona 8")
trumpaz8votes = (len(trumpaz8)/(len(trumpaz8)+len(bidenaz8)))*1
bidenaz8votes = (len(bidenaz8)/(len(trumpaz8)+len(bidenaz8)))*1
print("Trump: ", (len(trumpaz8)/(len(trumpaz8)+len(bidenaz8))))
print("votes ", trumpaz8votes)
print("Biden: ",(len(bidenaz8)/(len(trumpaz8)+len(bidenaz8))))
print("votes ", bidenaz8votes)
print("Arizona 8")
trumpaz9votes = (len(trumpaz9)/(len(trumpaz9)+len(bidenaz9)))*1
bidenaz9votes = (len(bidenaz9)/(len(trumpaz9)+len(bidenaz9)))*1
print("Trump: ", (len(trumpaz9)/(len(trumpaz9)+len(bidenaz9))))
print("votes ", trumpaz9votes)
print("Biden: ",(len(bidenaz9)/(len(trumpaz9)+len(bidenaz9))))
print("votes ", bidenaz9votes)
totalazvotestrump = trumpaz1votes+trumpaz2votes+trumpaz3votes+trumpaz4votes+trumpaz5votes+trumpaz6votes+trumpaz7votes+trumpaz8votes+trumpaz9votes
totalazvotesbiden = bidenaz1votes+bidenaz2votes+bidenaz3votes+bidenaz4votes+bidenaz5votes+bidenaz6votes+bidenaz7votes+bidenaz8votes+bidenaz9votes
print("TOTAL TRUMP VOTES: ", totalazvotestrump/(totalazvotestrump+totalazvotesbiden))
print("TOTAL BIDEN VOTES: ", totalazvotesbiden/(totalazvotestrump+totalazvotesbiden))
print("")
print("Arkansas")
print("Trump: ", (len(trumpar)/(len(trumpar)+len(bidenar))))
print("Biden: ",(len(bidenar)/(len(trumpar)+len(bidenar))))
print("Arkansas 1")
trumpar1votes = (len(trumpar1)/(len(trumpar1)+len(bidenar1)))*239268
bidenar1votes = (len(bidenar1)/(len(trumpar1)+len(bidenar1)))*239268
print("Trump: ", (len(trumpar1)/(len(trumpar1)+len(bidenar1))))
print("votes ", trumpar1votes)
print("Biden: ",(len(bidenar1)/(len(trumpar1)+len(bidenar1))))
print("votes ", bidenar1votes)
print("Arkansas 2")
trumpar2votes = (len(trumpar2)/(len(trumpar2)+len(bidenar2)))*287149
bidenar2votes = (len(bidenar2)/(len(trumpar2)+len(bidenar2)))*287149
print("Trump: ", (len(trumpar2)/(len(trumpar2)+len(bidenar2))))
print("votes ", trumpar2votes)
print("Biden: ",(len(bidenar2)/(len(trumpar2)+len(bidenar2))))
print("votes ", bidenar2votes)
print("Arkansas 3")
trumpar3votes = (len(trumpar3)/(len(trumpar3)+len(bidenar3)))*277061
bidenar3votes = (len(bidenar3)/(len(trumpar3)+len(bidenar3)))*277061
print("Trump: ", (len(trumpar3)/(len(trumpar3)+len(bidenar3))))
print("votes ", trumpar3votes)
print("Biden: ",(len(bidenar3)/(len(trumpar3)+len(bidenar3))))
print("votes ", bidenar3votes)
print("Arkansas 4")
trumpar4votes = (len(trumpar4)/(len(trumpar4)+len(bidenar4)))*242890
bidenar4votes = (len(bidenar4)/(len(trumpar4)+len(bidenar4)))*242890
print("Trump: ", (len(trumpar4)/(len(trumpar4)+len(bidenar4))))
print("votes ", trumpar4votes)
print("Biden: ",(len(bidenar4)/(len(trumpar4)+len(bidenar4))))
print("votes ", bidenar4votes)
totalarvotestrump = trumpar1votes+trumpar2votes+trumpar3votes+trumpar4votes
totalarvotesbiden = bidenar1votes+bidenar2votes+bidenar3votes+bidenar4votes
print("TOTAL TRUMP VOTES: ", totalarvotestrump/(totalarvotestrump+totalarvotesbiden))
print("TOTAL BIDEN VOTES: ", totalarvotesbiden/(totalarvotestrump+totalarvotesbiden))
print("")
print("Alabama")
print("Trump: ", (len(trumpal)/(len(trumpal)+len(bidenal))))
print("Biden: ",(len(bidenal)/(len(trumpal)+len(bidenal))))
print("Alabama 1")
trumpal1votes = (len(trumpal1)/(len(trumpal1)+len(bidenal1)))*1
bidenal1votes = (len(bidenal1)/(len(trumpal1)+len(bidenal1)))*1
print("Trump: ", (len(trumpal1)/(len(trumpal1)+len(bidenal1))))
print("votes ", trumpal1votes)
print("Biden: ",(len(bidenal1)/(len(trumpal1)+len(bidenal1))))
print("votes ", bidenal1votes)
print("Alabama 2")
trumpal2votes = (len(trumpal2)/(len(trumpal2)+len(bidenal2)))*1
bidenal2votes = (len(bidenal2)/(len(trumpal2)+len(bidenal2)))*1
print("Trump: ", (len(trumpal2)/(len(trumpal2)+len(bidenal2))))
print("votes ", trumpal2votes)
print("Biden: ",(len(bidenal2)/(len(trumpal2)+len(bidenal2))))
print("votes ", bidenal2votes)
print("Alabama 3")
trumpal3votes = (len(trumpal3)/(len(trumpal3)+len(bidenal3)))*1
bidenal3votes = (len(bidenal3)/(len(trumpal3)+len(bidenal3)))*1
print("Trump: ", (len(trumpal3)/(len(trumpal3)+len(bidenal3))))
print("votes ", trumpal3votes)
print("Biden: ",(len(bidenal3)/(len(trumpal3)+len(bidenal3))))
print("votes ", bidenal3votes)
print("Alabama 4")
trumpal4votes = (len(trumpal4)/(len(trumpal4)+len(bidenal4)))*1
bidenal4votes = (len(bidenal4)/(len(trumpal4)+len(bidenal4)))*1
print("Trump: ", (len(trumpal4)/(len(trumpal4)+len(bidenal4))))
print("votes ", trumpal4votes)
print("Biden: ",(len(bidenal4)/(len(trumpal4)+len(bidenal4))))
print("votes ", bidenal4votes)
print("Alabama 5")
trumpal5votes = (len(trumpal5)/(len(trumpal5)+len(bidenal5)))*1
bidenal5votes = (len(bidenal5)/(len(trumpal5)+len(bidenal5)))*1
print("Trump: ", (len(trumpal5)/(len(trumpal5)+len(bidenal5))))
print("votes ", trumpal5votes)
print("Biden: ",(len(bidenal5)/(len(trumpal5)+len(bidenal5))))
print("votes ", bidenal5votes)
print("Alabama 6")
trumpal6votes = (len(trumpal6)/(len(trumpal6)+len(bidenal6)))*1
bidenal6votes = (len(bidenal6)/(len(trumpal6)+len(bidenal6)))*1
print("Trump: ", (len(trumpal6)/(len(trumpal6)+len(bidenal6))))
print("votes ", trumpal6votes)
print("Biden: ",(len(bidenal6)/(len(trumpal6)+len(bidenal6))))
print("votes ", bidenal6votes)
print("Alabama 7")
trumpal7votes = (len(trumpal7)/(len(trumpal7)+len(bidenal7)))*1
bidenal7votes = (len(bidenal7)/(len(trumpal7)+len(bidenal7)))*1
print("Trump: ", (len(trumpal7)/(len(trumpal7)+len(bidenal7))))
print("votes ", trumpal7votes)
print("Biden: ",(len(bidenal7)/(len(trumpal7)+len(bidenal7))))
print("votes ", bidenal7votes)
totalalvotestrump = trumpal1votes+trumpal2votes+trumpal3votes+trumpal4votes+trumpal5votes+trumpal6votes+trumpal7votes
totalalvotesbiden = bidenal1votes+bidenal2votes+bidenal3votes+bidenal4votes+bidenal5votes+bidenal6votes+bidenal7votes
print("TOTAL TRUMP VOTES: ", totalalvotestrump/(totalalvotestrump+totalalvotesbiden))
print("TOTAL BIDEN VOTES: ", totalalvotesbiden/(totalalvotestrump+totalalvotesbiden))
print("")
print("Louisiana")
print("Trump: ", (len(trumpla)/(len(trumpla)+len(bidenla))))
print("Biden: ",(len(bidenla)/(len(trumpla)+len(bidenla))))
print("Louisiana 1")
trumpla1votes = (len(trumpla1)/(len(trumpla1)+len(bidenla1)))*285391
bidenla1votes = (len(bidenla1)/(len(trumpla1)+len(bidenla1)))*285391
print("Trump: ", (len(trumpla1)/(len(trumpla1)+len(bidenla1))))
print("votes ", trumpla1votes)
print("Biden: ",(len(bidenla1)/(len(trumpla1)+len(bidenla1))))
print("votes ", bidenla1votes)
print("Louisiana 2")
trumpla2votes = (len(trumpla2)/(len(trumpla2)+len(bidenla2)))*275078
bidenla2votes = (len(bidenla2)/(len(trumpla2)+len(bidenla2)))*275078
print("Trump: ", (len(trumpla2)/(len(trumpla2)+len(bidenla2))))
print("votes ", trumpla2votes)
print("Biden: ",(len(bidenla2)/(len(trumpla2)+len(bidenla2))))
print("votes ", bidenla2votes)
print("Louisiana 3")
trumpla3votes = (len(trumpla3)/(len(trumpla3)+len(bidenla3)))*138430
bidenla3votes = (len(bidenla3)/(len(trumpla3)+len(bidenla3)))*138430
print("Trump: ", (len(trumpla3)/(len(trumpla3)+len(bidenla3))))
print("votes ", trumpla3votes)
print("Biden: ",(len(bidenla3)/(len(trumpla3)+len(bidenla3))))
print("votes ", bidenla3votes)
print("Louisiana 4")
trumpla4votes = (len(trumpla4)/(len(trumpla4)+len(bidenla4)))*133947
bidenla4votes = (len(bidenla4)/(len(trumpla4)+len(bidenla4)))*133947
print("Trump: ", (len(trumpla4)/(len(trumpla4)+len(bidenla4))))
print("votes ", trumpla4votes)
print("Biden: ",(len(bidenla4)/(len(trumpla4)+len(bidenla4))))
print("votes ", bidenla4votes)
print("Louisiana 5")
trumpla5votes = (len(trumpla5)/(len(trumpla5)+len(bidenla5)))*255610
bidenla5votes = (len(bidenla5)/(len(trumpla5)+len(bidenla5)))*255610
print("Trump: ", (len(trumpla5)/(len(trumpla5)+len(bidenla5))))
print("votes ", trumpla5votes)
print("Biden: ",(len(bidenla5)/(len(trumpla5)+len(bidenla5))))
print("votes ", bidenla5votes)
print("Louisiana 6")
trumpla6votes = (len(trumpla6)/(len(trumpla6)+len(bidenla6)))*256805
bidenla6votes = (len(bidenla6)/(len(trumpla6)+len(bidenla6)))*256805
print("Trump: ", (len(trumpla6)/(len(trumpla6)+len(bidenla6))))
print("votes ", trumpla6votes)
print("Biden: ",(len(bidenla6)/(len(trumpla6)+len(bidenla6))))
print("votes ", bidenla6votes)
totallavotestrump = trumpla1votes+trumpla2votes+trumpla3votes+trumpla4votes+trumpla5votes+trumpla6votes
totallavotesbiden = bidenla1votes+bidenla2votes+bidenla3votes+bidenla4votes+bidenla5votes+bidenla6votes
print("TOTAL TRUMP VOTES: ", totallavotestrump/(totallavotestrump+totallavotesbiden))
print("TOTAL BIDEN VOTES: ", totallavotesbiden/(totallavotestrump+totallavotesbiden))
print("")
print("Washington")
print("Trump: ", (len(trumpwa)/(len(trumpwa)+len(bidenwa))))
print("Biden: ",(len(bidenwa)/(len(trumpwa)+len(bidenwa))))
print("Washington 1")
trumpwa1votes = (len(trumpwa1)/(len(trumpwa1)+len(bidenwa1)))*323733
bidenwa1votes = (len(bidenwa1)/(len(trumpwa1)+len(bidenwa1)))*323733
print("Trump: ", (len(trumpwa1)/(len(trumpwa1)+len(bidenwa1))))
print("votes ", trumpwa1votes)
print("Biden: ",(len(bidenwa1)/(len(trumpwa1)+len(bidenwa1))))
print("votes ", bidenwa1votes)
print("Washington 2")
trumpwa2votes = (len(trumpwa2)/(len(trumpwa2)+len(bidenwa2)))*305499
bidenwa2votes = (len(bidenwa2)/(len(trumpwa2)+len(bidenwa2)))*305499
print("Trump: ", (len(trumpwa2)/(len(trumpwa2)+len(bidenwa2))))
print("votes ", trumpwa2votes)
print("Biden: ",(len(bidenwa2)/(len(trumpwa2)+len(bidenwa2))))
print("votes ", bidenwa2votes)
print("Washington 3")
trumpwa3votes = (len(trumpwa3)/(len(trumpwa3)+len(bidenwa3)))*298652
bidenwa3votes = (len(bidenwa3)/(len(trumpwa3)+len(bidenwa3)))*298652
print("Trump: ", (len(trumpwa3)/(len(trumpwa3)+len(bidenwa3))))
print("votes ", trumpwa3votes)
print("Biden: ",(len(bidenwa3)/(len(trumpwa3)+len(bidenwa3))))
print("votes ", bidenwa3votes)
print("Washington 4")
trumpwa4votes = (len(trumpwa4)/(len(trumpwa4)+len(bidenwa4)))*211347
bidenwa4votes = (len(bidenwa4)/(len(trumpwa4)+len(bidenwa4)))*211347
print("Trump: ", (len(trumpwa4)/(len(trumpwa4)+len(bidenwa4))))
print("votes ", trumpwa4votes)
print("Biden: ",(len(bidenwa4)/(len(trumpwa4)+len(bidenwa4))))
print("votes ", bidenwa4votes)
print("Washington 5")
trumpwa5votes = (len(trumpwa5)/(len(trumpwa5)+len(bidenwa5)))*286821
bidenwa5votes = (len(bidenwa5)/(len(trumpwa5)+len(bidenwa5)))*286821
print("Trump: ", (len(trumpwa5)/(len(trumpwa5)+len(bidenwa5))))
print("votes ", trumpwa5votes)
print("Biden: ",(len(bidenwa5)/(len(trumpwa5)+len(bidenwa5))))
print("votes ", bidenwa5votes)
print("Washington 6")
trumpwa6votes = (len(trumpwa6)/(len(trumpwa6)+len(bidenwa6)))*306556
bidenwa6votes = (len(bidenwa6)/(len(trumpwa6)+len(bidenwa6)))*306556
print("Trump: ", (len(trumpwa6)/(len(trumpwa6)+len(bidenwa6))))
print("votes ", trumpwa6votes)
print("Biden: ",(len(bidenwa6)/(len(trumpwa6)+len(bidenwa6))))
print("votes ", bidenwa6votes)
print("Washington 7")
trumpwa7votes = (len(trumpwa7)/(len(trumpwa7)+len(bidenwa7)))*343369
bidenwa7votes = (len(bidenwa7)/(len(trumpwa7)+len(bidenwa7)))*343369
print("Trump: ", (len(trumpwa7)/(len(trumpwa7)+len(bidenwa7))))
print("votes ", trumpwa7votes)
print("Biden: ",(len(bidenwa7)/(len(trumpwa7)+len(bidenwa7))))
print("votes ", bidenwa7votes)
print("Washington 8")
trumpwa8votes = (len(trumpwa8)/(len(trumpwa8)+len(bidenwa8)))*290997
bidenwa8votes = (len(bidenwa8)/(len(trumpwa8)+len(bidenwa8)))*290997
print("Trump: ", (len(trumpwa8)/(len(trumpwa8)+len(bidenwa8))))
print("votes ", trumpwa8votes)
print("Biden: ",(len(bidenwa8)/(len(trumpwa8)+len(bidenwa8))))
print("votes ", bidenwa8votes)
print("Washington 9")
trumpwa9votes = (len(trumpwa9)/(len(trumpwa9)+len(bidenwa9)))*255785
bidenwa9votes = (len(bidenwa9)/(len(trumpwa9)+len(bidenwa9)))*255785
print("Trump: ", (len(trumpwa9)/(len(trumpwa9)+len(bidenwa9))))
print("votes ", trumpwa9votes)
print("Biden: ",(len(bidenwa9)/(len(trumpwa9)+len(bidenwa9))))
print("votes ", bidenwa9votes)
print("Washington 10")
trumpwa10votes = (len(trumpwa10)/(len(trumpwa10)+len(bidenwa10)))*271372
bidenwa10votes = (len(bidenwa10)/(len(trumpwa10)+len(bidenwa10)))*271372
print("Trump: ", (len(trumpwa10)/(len(trumpwa10)+len(bidenwa10))))
print("votes ", trumpwa10votes)
print("Biden: ",(len(bidenwa10)/(len(trumpwa10)+len(bidenwa10))))
print("votes ", bidenwa10votes)
totalwavotestrump = trumpwa1votes+trumpwa2votes+trumpwa3votes+trumpwa4votes+trumpwa5votes+trumpwa6votes+trumpwa7votes+trumpwa8votes+trumpwa9votes+trumpwa10votes
totalwavotesbiden = bidenwa1votes+bidenwa2votes+bidenwa3votes+bidenwa4votes+bidenwa5votes+bidenwa6votes+bidenwa7votes+bidenwa8votes+bidenwa9votes+bidenwa10votes
print("TOTAL TRUMP VOTES: ", totalwavotestrump/(totalwavotestrump+totalwavotesbiden))
print("TOTAL BIDEN VOTES: ", totalwavotesbiden/(totalwavotestrump+totalwavotesbiden))
print("")
print("West Virginia")
print("Trump: ", (len(trumpwv)/(len(trumpwv)+len(bidenwv))))
print("Biden: ",(len(bidenwv)/(len(trumpwv)+len(bidenwv))))
print("West Virginia 1")
trumpwv1votes = (len(trumpwv1)/(len(trumpwv1)+len(bidenwv1)))*235364
bidenwv1votes = (len(bidenwv1)/(len(trumpwv1)+len(bidenwv1)))*235364
print("Trump: ", (len(trumpwv1)/(len(trumpwv1)+len(bidenwv1))))
print("votes ", len(trumpwv1))
print("Biden: ",(len(bidenwv1)/(len(trumpwv1)+len(bidenwv1))))
print("votes ", len(bidenwv1))
print("West Virginia 2")
trumpwv2votes = (len(trumpwv2)/(len(trumpwv2)+len(bidenwv2)))*240704
bidenwv2votes = (len(bidenwv2)/(len(trumpwv2)+len(bidenwv2)))*240704
print("Trump: ", (len(trumpwv2)/(len(trumpwv2)+len(bidenwv2))))
print("votes ", len(trumpwv2))
print("Biden: ",(len(bidenwv2)/(len(trumpwv2)+len(bidenwv2))))
print("votes ", len(bidenwv2))
print("West Virginia 3")
trumpwv3votes = (len(trumpwv3)/(len(trumpwv3)+len(bidenwv3)))*189009
bidenwv3votes = (len(bidenwv3)/(len(trumpwv3)+len(bidenwv3)))*189009
print("Trump: ", (len(trumpwv3)/(len(trumpwv3)+len(bidenwv3))))
print("votes ", len(trumpwv3))
print("Biden: ",(len(bidenwv3)/(len(trumpwv3)+len(bidenwv3))))
print("votes ", len(bidenwv3))
totalwvvotestrump = trumpwv1votes+trumpwv2votes+trumpwv3votes
totalwvvotesbiden = bidenwv1votes+bidenwv2votes+bidenwv3votes
print("TOTAL TRUMP VOTES: ", totalwvvotestrump/(totalwvvotestrump+totalwvvotesbiden))
print("TOTAL BIDEN VOTES: ", totalwvvotesbiden/(totalwvvotestrump+totalwvvotesbiden))
print("")
print("New Jersey")
print("Trump: ", (len(trumpnj)/(len(trumpnj)+len(bidennj))))
print("Biden: ",(len(bidennj)/(len(trumpnj)+len(bidennj))))
print("New Jersey 1")
trumpnj1votes = (len(trumpnj1)/(len(trumpnj1)+len(bidennj1)))*288890
bidennj1votes = (len(bidennj1)/(len(trumpnj1)+len(bidennj1)))*288890
bothnj1 = trumpnj1.intersection(bidennj1)
bothnj1votes = (len(bothnj1)/(len(trumpnj1)+len(bidennj1)))*288890
print("Trump: ", (len(trumpnj1)/(len(trumpnj1)+len(bidennj1)))-((len(bothnj1)/(len(trumpnj1)+len(bidennj1)))/2))
print("votes ", len(trumpnj1))
print("Biden: ",(len(bidennj1)/(len(trumpnj1)+len(bidennj1)))-((len(bothnj1)/(len(trumpnj1)+len(bidennj1)))/2))
print("votes ", len(bidennj1))
print("Both: ", (len(bothnj1)/(len(trumpnj1)+len(bidennj1))))
print("New Jersey 2")
trumpnj2votes = (len(trumpnj2)/(len(trumpnj2)+len(bidennj2)))*272542
bidennj2votes = (len(bidennj2)/(len(trumpnj2)+len(bidennj2)))*272542
bothnj2 = trumpnj2.intersection(bidennj2)
bothnj2votes = (len(bothnj2)/(len(trumpnj2)+len(bidennj2)))*272542
print("Trump: ", (len(trumpnj2)/(len(trumpnj2)+len(bidennj2)))-((len(bothnj2)/(len(trumpnj2)+len(bidennj2)))/2))
print("votes ", len(trumpnj2))
print("Biden: ",(len(bidennj2)/(len(trumpnj2)+len(bidennj2)))-((len(bothnj2)/(len(trumpnj2)+len(bidennj2)))/2))
print("votes ", len(bidennj2))
print("Both: ", (len(bothnj2)/(len(trumpnj2)+len(bidennj2))))
print("New Jersey 3")
trumpnj3votes = (len(trumpnj3)/(len(trumpnj3)+len(bidennj3)))*292734
bidennj3votes = (len(bidennj3)/(len(trumpnj3)+len(bidennj3)))*292734
bothnj3 = trumpnj3.intersection(bidennj3)
bothnj3votes = (len(bothnj3)/(len(trumpnj3)+len(bidennj3)))*292734
print("Trump: ", (len(trumpnj3)/(len(trumpnj3)+len(bidennj3)))-((len(bothnj3)/(len(trumpnj3)+len(bidennj3)))/2))
print("votes ", len(trumpnj3))
print("Biden: ",(len(bidennj3)/(len(trumpnj3)+len(bidennj3)))-((len(bothnj3)/(len(trumpnj3)+len(bidennj3)))/2))
print("votes ", len(bidennj3))
print("Both: ", (len(bothnj3)/(len(trumpnj3)+len(bidennj3))))
print("New Jersey 4")
trumpnj4votes = (len(trumpnj4)/(len(trumpnj4)+len(bidennj4)))*314510
bidennj4votes = (len(bidennj4)/(len(trumpnj4)+len(bidennj4)))*314510
bothnj4 = trumpnj4.intersection(bidennj4)
bothnj4votes = (len(bothnj4)/(len(trumpnj4)+len(bidennj4)))*314510
print("Trump: ", (len(trumpnj4)/(len(trumpnj4)+len(bidennj4)))-((len(bothnj4)/(len(trumpnj4)+len(bidennj4)))/2))
print("votes ", len(trumpnj4))
print("Biden: ",(len(bidennj4)/(len(trumpnj4)+len(bidennj4)))-((len(bothnj4)/(len(trumpnj4)+len(bidennj4)))/2))
print("votes ", len(bidennj4))
print("Both: ", (len(bothnj4)/(len(trumpnj4)+len(bidennj4))))
print("New Jersey 5")
trumpnj5votes = (len(trumpnj5)/(len(trumpnj5)+len(bidennj5)))*303506
bidennj5votes = (len(bidennj5)/(len(trumpnj5)+len(bidennj5)))*303506
bothnj5 = trumpnj5.intersection(bidennj5)
bothnj5votes = (len(bothnj5)/(len(trumpnj5)+len(bidennj5)))*303506
print("Trump: ", (len(trumpnj5)/(len(trumpnj5)+len(bidennj5)))-((len(bothnj5)/(len(trumpnj5)+len(bidennj5)))/2))
print("votes ", len(trumpnj5))
print("Biden: ",(len(bidennj5)/(len(trumpnj5)+len(bidennj5)))-((len(bothnj5)/(len(trumpnj5)+len(bidennj5)))/2))
print("votes ", len(bidennj5))
print("Both: ", (len(bothnj5)/(len(trumpnj5)+len(bidennj5))))
print("New Jersey 6")
trumpnj6votes = (len(trumpnj6)/(len(trumpnj6)+len(bidennj6)))*236584
bidennj6votes = (len(bidennj6)/(len(trumpnj6)+len(bidennj6)))*236584
bothnj6 = trumpnj6.intersection(bidennj6)
bothnj6votes = (len(bothnj6)/(len(trumpnj6)+len(bidennj6)))*236584
print("Trump: ", (len(trumpnj6)/(len(trumpnj6)+len(bidennj6)))-((len(bothnj6)/(len(trumpnj6)+len(bidennj6)))/2))
print("votes ", len(trumpnj6))
print("Biden: ",(len(bidennj6)/(len(trumpnj6)+len(bidennj6)))-((len(bothnj6)/(len(trumpnj6)+len(bidennj6)))/2))
print("votes ", len(bidennj6))
print("Both: ", (len(bothnj6)/(len(trumpnj6)+len(bidennj6))))
print("New Jersey 7")
trumpnj7votes = (len(trumpnj7)/(len(trumpnj7)+len(bidennj7)))*330659
bidennj7votes = (len(bidennj7)/(len(trumpnj7)+len(bidennj7)))*330659
bothnj7 = trumpnj7.intersection(bidennj7)
bothnj7votes = (len(bothnj7)/(len(trumpnj7)+len(bidennj7)))*330659
print("Trump: ", (len(trumpnj7)/(len(trumpnj7)+len(bidennj7)))-((len(bothnj7)/(len(trumpnj7)+len(bidennj7)))/2))
print("votes ", len(trumpnj7))
print("Biden: ",(len(bidennj7)/(len(trumpnj7)+len(bidennj7)))-((len(bothnj7)/(len(trumpnj7)+len(bidennj7)))/2))
print("votes ", len(bidennj7))
print("Both: ", (len(bothnj7)/(len(trumpnj7)+len(bidennj7))))
print("New Jersey 8")
trumpnj8votes = (len(trumpnj8)/(len(trumpnj8)+len(bidennj8)))*154466
bidennj8votes = (len(bidennj8)/(len(trumpnj8)+len(bidennj8)))*154466
bothnj8 = trumpnj8.intersection(bidennj8)
bothnj8votes = (len(bothnj8)/(len(trumpnj8)+len(bidennj8)))*154466
print("Trump: ", (len(trumpnj8)/(len(trumpnj8)+len(bidennj8)))-((len(bothnj8)/(len(trumpnj8)+len(bidennj8)))/2))
print("votes ", len(trumpnj8))
print("Biden: ",(len(bidennj8)/(len(trumpnj8)+len(bidennj8)))-((len(bothnj8)/(len(trumpnj8)+len(bidennj8)))/2))
print("votes ", len(bidennj8))
print("Both: ", (len(bothnj8)/(len(trumpnj8)+len(bidennj8))))
print("New Jersey 9")
trumpnj9votes = (len(trumpnj9)/(len(trumpnj9)+len(bidennj9)))*213207
bidennj9votes = (len(bidennj9)/(len(trumpnj9)+len(bidennj9)))*213207
bothnj9 = trumpnj9.intersection(bidennj9)
bothnj9votes = (len(bothnj9)/(len(trumpnj9)+len(bidennj9)))*213207
print("Trump: ", (len(trumpnj9)/(len(trumpnj9)+len(bidennj9)))-((len(bothnj9)/(len(trumpnj9)+len(bidennj9)))/2))
print("votes ", len(trumpnj9))
print("Biden: ",(len(bidennj9)/(len(trumpnj9)+len(bidennj9)))-((len(bothnj9)/(len(trumpnj9)+len(bidennj9)))/2))
print("votes ", len(bidennj9))
print("Both: ", (len(bothnj9)/(len(trumpnj9)+len(bidennj9))))
print("New Jersey 10")
trumpnj10votes = (len(trumpnj10)/(len(trumpnj10)+len(bidennj10)))*207043
bidennj10votes = (len(bidennj10)/(len(trumpnj10)+len(bidennj10)))*207043
bothnj10 = trumpnj10.intersection(bidennj10)
bothnj10votes = (len(bothnj10)/(len(trumpnj10)+len(bidennj10)))*207043
print("Trump: ", (len(trumpnj10)/(len(trumpnj10)+len(bidennj10)))-((len(bothnj10)/(len(trumpnj10)+len(bidennj10)))/2))
print("votes ", len(trumpnj10))
print("Biden: ",(len(bidennj10)/(len(trumpnj10)+len(bidennj10)))-((len(bothnj10)/(len(trumpnj10)+len(bidennj10)))/2))
print("votes ", len(bidennj10))
print("Both: ", (len(bothnj10)/(len(trumpnj10)+len(bidennj10))))
print("New Jersey 11")
trumpnj11votes = (len(trumpnj11)/(len(trumpnj11)+len(bidennj11)))*320770
bidennj11votes = (len(bidennj11)/(len(trumpnj11)+len(bidennj11)))*320770
bothnj11 = trumpnj11.intersection(bidennj11)
bothnj11votes = (len(bothnj11)/(len(trumpnj11)+len(bidennj11)))*320770
print("Trump: ", (len(trumpnj11)/(len(trumpnj11)+len(bidennj11)))-((len(bothnj11)/(len(trumpnj11)+len(bidennj11)))/2))
print("votes ", len(trumpnj11))
print("Biden: ",(len(bidennj11)/(len(trumpnj11)+len(bidennj11)))-((len(bothnj11)/(len(trumpnj11)+len(bidennj11)))/2))
print("votes ", len(bidennj11))
print("Both: ", (len(bothnj11)/(len(trumpnj11)+len(bidennj11))))
print("New Jersey 12")
trumpnj12votes = (len(trumpnj12)/(len(trumpnj12)+len(bidennj12)))*246016
bidennj12votes = (len(bidennj12)/(len(trumpnj12)+len(bidennj12)))*246016
bothnj12 = trumpnj12.intersection(bidennj12)
bothnj12votes = (len(bothnj12)/(len(trumpnj12)+len(bidennj12)))*246016
print("Trump: ", (len(trumpnj12)/(len(trumpnj12)+len(bidennj12)))-((len(bothnj12)/(len(trumpnj12)+len(bidennj12)))/2))
print("votes ", len(trumpnj12))
print("Biden: ",(len(bidennj12)/(len(trumpnj12)+len(bidennj12)))-((len(bothnj12)/(len(trumpnj12)+len(bidennj12)))/2))
print("votes ", len(bidennj12))
print("Both: ", (len(bothnj12)/(len(trumpnj12)+len(bidennj12))))
totalnjvotestrump = trumpnj1votes+trumpnj2votes+trumpnj3votes+trumpnj4votes+trumpnj5votes+trumpnj6votes+trumpnj7votes+trumpnj8votes+trumpnj9votes+trumpnj10votes+trumpnj11votes+trumpnj12votes
totalnjvotesbiden = bidennj1votes+bidennj2votes+bidennj3votes+bidennj4votes+bidennj5votes+bidennj6votes+bidennj7votes+bidennj8votes+bidennj9votes+bidennj10votes+bidennj11votes+bidennj12votes
totalnjvotesboth = bothnj1votes+bothnj2votes+bothnj3votes+bothnj4votes+bothnj5votes+bothnj6votes+bothnj7votes+bothnj8votes+bothnj9votes+bothnj10votes+bothnj11votes+bothnj12votes
print("TOTAL TRUMP VOTES: ", (totalnjvotestrump/(totalnjvotestrump+totalnjvotesbiden))-(totalnjvotesboth/(totalnjvotestrump+totalnjvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalnjvotesbiden/(totalnjvotestrump+totalnjvotesbiden))-(totalnjvotesboth/(totalnjvotestrump+totalnjvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalnjvotesboth/(totalnjvotestrump+totalnjvotesbiden)))
print("")
print("New Mexico")
print("Trump: ", (len(trumpnm)/(len(trumpnm)+len(bidennm))))
print("Biden: ",(len(bidennm)/(len(trumpnm)+len(bidennm))))
print("New Mexico 1")
bothnm1 = trumpnm1.intersection(bidennm1)
bothnm1votes = (len(bothnm1)/(len(trumpnm1)+len(bidennm1)))*275441
print("Trump: ", (len(trumpnm1)/(len(trumpnm1)+len(bidennm1)))-((len(bothnm1)/(len(trumpnm1)+len(bidennm1)))/2))
print("votes ", len(trumpnm1))
print("Biden: ",(len(bidennm1)/(len(trumpnm1)+len(bidennm1)))-((len(bothnm1)/(len(trumpnm1)+len(bidennm1)))/2))
print("votes ", len(bidennm1))
print("Both: ", (len(bothnm1)/(len(trumpnm1)+len(bidennm1))))
trumpnm1votes = (len(trumpnm1)/(len(trumpnm1)+len(bidennm1)))*275441
bidennm1votes = (len(bidennm1)/(len(trumpnm1)+len(bidennm1)))*275441
print("New Mexico 2")
bothnm2 = trumpnm2.intersection(bidennm2)
bothnm2votes = (len(bothnm2)/(len(trumpnm2)+len(bidennm2)))*227013
print("Trump: ", (len(trumpnm2)/(len(trumpnm2)+len(bidennm2)))-((len(bothnm2)/(len(trumpnm2)+len(bidennm2)))/2))
print("votes ", len(trumpnm2))
print("Biden: ",(len(bidennm2)/(len(trumpnm2)+len(bidennm2)))-((len(bothnm2)/(len(trumpnm2)+len(bidennm2)))/2))
print("votes ", len(bidennm2))
print("Both: ", (len(bothnm2)/(len(trumpnm2)+len(bidennm2))))
trumpnm2votes = (len(trumpnm2)/(len(trumpnm2)+len(bidennm2)))*227013
bidennm2votes = (len(bidennm2)/(len(trumpnm2)+len(bidennm2)))*227013
print("New Mexico 3")
bothnm3 = trumpnm3.intersection(bidennm3)
bothnm3votes = (len(bothnm3)/(len(trumpnm3)+len(bidennm3)))*268377
print("Trump: ", (len(trumpnm3)/(len(trumpnm3)+len(bidennm3)))-((len(bothnm3)/(len(trumpnm3)+len(bidennm3)))/2))
print("votes ", len(trumpnm3))
print("Biden: ",(len(bidennm3)/(len(trumpnm3)+len(bidennm3)))-((len(bothnm3)/(len(trumpnm3)+len(bidennm3)))/2))
print("votes ", len(bidennm3))
print("Both: ", (len(bothnm3)/(len(trumpnm3)+len(bidennm3))))
trumpnm3votes = (len(trumpnm3)/(len(trumpnm3)+len(bidennm3)))*268377
bidennm3votes = (len(bidennm3)/(len(trumpnm3)+len(bidennm3)))*268377
totalnmvotestrump = trumpnm1votes+trumpnm2votes+trumpnm3votes
totalnmvotesbiden = bidennm1votes+bidennm2votes+bidennm3votes
totalnmvotesboth = bothnm1votes+bothnm2votes+bothnm3votes
print("TOTAL TRUMP VOTES: ", (totalnmvotestrump/(totalnmvotestrump+totalnmvotesbiden))-(totalnmvotesboth/(totalnmvotestrump+totalnmvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalnmvotesbiden/(totalnmvotestrump+totalnmvotesbiden))-(totalnmvotesboth/(totalnmvotestrump+totalnmvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalnmvotesboth/(totalnmvotestrump+totalnmvotesbiden)))
print("")
print("Nebraska")
print("Trump: ", (len(trumpne)/(len(trumpne)+len(bidenne))))
print("Biden: ",(len(bidenne)/(len(trumpne)+len(bidenne))))
print("Nebraska 1")
trumpne1votes = (len(trumpne1)/(len(trumpne1)+len(bidenne1)))*1
bidenne1votes = (len(bidenne1)/(len(trumpne1)+len(bidenne1)))*1
bothne1 = trumpne1.intersection(bidenne1)
bothne1votes = (len(bothne1)/(len(trumpne1)+len(bidenne1)))*1
print("Trump: ", (len(trumpne1)/(len(trumpne1)+len(bidenne1)))-((len(bothne1)/(len(trumpne1)+len(bidenne1)))/2))
print("votes ", len(trumpne1))
print("Biden: ",(len(bidenne1)/(len(trumpne1)+len(bidenne1)))-((len(bothne1)/(len(trumpne1)+len(bidenne1)))/2))
print("votes ", len(bidenne1))
print("Both: ", (len(bothne1)/(len(trumpne1)+len(bidenne1))))
print("Nebraska 2")
trumpne2votes = (len(trumpne2)/(len(trumpne2)+len(bidenne2)))*1
bidenne2votes = (len(bidenne2)/(len(trumpne2)+len(bidenne2)))*1
bothne2 = trumpne2.intersection(bidenne2)
bothne2votes = (len(bothne2)/(len(trumpne2)+len(bidenne2)))*1
print("Trump: ", (len(trumpne2)/(len(trumpne2)+len(bidenne2)))-((len(bothne2)/(len(trumpne2)+len(bidenne2)))/2))
print("votes ", len(trumpne2))
print("Biden: ",(len(bidenne2)/(len(trumpne2)+len(bidenne2)))-((len(bothne2)/(len(trumpne2)+len(bidenne2)))/2))
print("votes ", len(bidenne2))
print("Both: ", (len(bothne2)/(len(trumpne2)+len(bidenne2))))
print("Nebraska 3")
trumpne3votes = (len(trumpne3)/(len(trumpne3)+len(bidenne3)))*1
bidenne3votes = (len(bidenne3)/(len(trumpne3)+len(bidenne3)))*1
bothne3 = trumpne3.intersection(bidenne3)
bothne3votes = (len(bothne3)/(len(trumpne3)+len(bidenne3)))*1
print("Trump: ", (len(trumpne3)/(len(trumpne3)+len(bidenne3)))-((len(bothne3)/(len(trumpne3)+len(bidenne3)))/2))
print("votes ", len(trumpne3))
print("Biden: ",(len(bidenne3)/(len(trumpne3)+len(bidenne3)))-((len(bothne3)/(len(trumpne3)+len(bidenne3)))/2))
print("votes ", len(bidenne3))
print("Both: ", (len(bothne3)/(len(trumpne3)+len(bidenne3))))
totalnevotestrump = trumpne1votes+trumpne2votes+trumpne3votes
totalnevotesbiden = bidenne1votes+bidenne2votes+bidenne3votes
totalnevotesboth = bothne1votes+bothne2votes+bothne3votes
print("TOTAL TRUMP VOTES: ", (totalnevotestrump/(totalnevotestrump+totalnevotesbiden))-(totalnevotesboth/(totalnevotestrump+totalnevotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalnevotesbiden/(totalnevotestrump+totalnevotesbiden))-(totalnevotesboth/(totalnevotestrump+totalnevotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalnevotesboth/(totalnevotestrump+totalnevotesbiden)))
print("")
print("New Hampshire")
print("Trump: ", (len(trumpnh)/(len(trumpnh)+len(bidennh))))
print("Biden: ",(len(bidennh)/(len(trumpnh)+len(bidennh))))
print("New Hampshire 1")
trumpnh1votes = (len(trumpnh1)/(len(trumpnh1)+len(bidennh1)))*318839
bidennh1votes = (len(bidennh1)/(len(trumpnh1)+len(bidennh1)))*318839
bothnh1 = trumpnh1.intersection(bidennh1)
bothnh1votes = (len(bothnh1)/(len(trumpnh1)+len(bidennh1)))*318839
print("Trump: ", (len(trumpnh1)/(len(trumpnh1)+len(bidennh1)))-((len(bothnh1)/(len(trumpnh1)+len(bidennh1)))/2))
print("votes ", len(trumpnh1))
print("Biden: ",(len(bidennh1)/(len(trumpnh1)+len(bidennh1)))-((len(bothnh1)/(len(trumpnh1)+len(bidennh1)))/2))
print("votes ", len(bidennh1))
print("Both: ", (len(bothnh1)/(len(trumpnh1)+len(bidennh1))))
print("New Hampshire 2")
trumpnh2votes = (len(trumpnh2)/(len(trumpnh2)+len(bidennh2)))*333346
bidennh2votes = (len(bidennh2)/(len(trumpnh2)+len(bidennh2)))*333346
bothnh2 = trumpnh2.intersection(bidennh2)
bothnh2votes = (len(bothnh2)/(len(trumpnh2)+len(bidennh2)))*333346
print("Trump: ", (len(trumpnh2)/(len(trumpnh2)+len(bidennh2)))-((len(bothnh2)/(len(trumpnh2)+len(bidennh2)))/2))
print("votes ", len(trumpnh2))
print("Biden: ",(len(bidennh2)/(len(trumpnh2)+len(bidennh2)))-((len(bothnh2)/(len(trumpnh2)+len(bidennh2)))/2))
print("votes ", len(bidennh2))
print("Both: ", (len(bothnh2)/(len(trumpnh2)+len(bidennh2))))
totalnhvotestrump = trumpnh1votes+trumpnh2votes
totalnhvotesbiden = bidennh1votes+bidennh2votes
totalnhvotesboth = bothnh1votes+bothnh2votes
print("TOTAL TRUMP VOTES: ", (totalnhvotestrump/(totalnhvotestrump+totalnhvotesbiden))-(totalnhvotesboth/(totalnhvotestrump+totalnhvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalnhvotesbiden/(totalnhvotestrump+totalnhvotesbiden))-(totalnhvotesboth/(totalnhvotestrump+totalnhvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalnhvotesboth/(totalnhvotestrump+totalnhvotesbiden)))
print("")
print("Nevada")
print("Trump: ", (len(trumpnv)/(len(trumpnv)+len(bidennv))))
print("Biden: ",(len(bidennv)/(len(trumpnv)+len(bidennv))))
print("Nevada 1")
trumpnv1votes = (len(trumpnv1)/(len(trumpnv1)+len(bidennv1)))*170098
bidennv1votes = (len(bidennv1)/(len(trumpnv1)+len(bidennv1)))*170098
bothnv1 = trumpnv1.intersection(bidennv1)
bothnv1votes = (len(bothnv1)/(len(trumpnv1)+len(bidennv1)))*170098
print("Trump: ", (len(trumpnv1)/(len(trumpnv1)+len(bidennv1)))-((len(bothnv1)/(len(trumpnv1)+len(bidennv1)))/2))
print("votes ", len(trumpnv1))
print("Biden: ",(len(bidennv1)/(len(trumpnv1)+len(bidennv1)))-((len(bothnv1)/(len(trumpnv1)+len(bidennv1)))/2))
print("votes ", len(bidennv1))
print("Both: ", (len(bothnv1)/(len(trumpnv1)+len(bidennv1))))
print("Nevada 2")
trumpnv2votes = (len(trumpnv2)/(len(trumpnv2)+len(bidennv2)))*297847
bidennv2votes = (len(bidennv2)/(len(trumpnv2)+len(bidennv2)))*297847
bothnv2 = trumpnv2.intersection(bidennv2)
bothnv2votes = (len(bothnv2)/(len(trumpnv2)+len(bidennv2)))*297847
print("Trump: ", (len(trumpnv2)/(len(trumpnv2)+len(bidennv2)))-((len(bothnv2)/(len(trumpnv2)+len(bidennv2)))/2))
print("votes ", len(trumpnv2))
print("Biden: ",(len(bidennv2)/(len(trumpnv2)+len(bidennv2)))-((len(bothnv2)/(len(trumpnv2)+len(bidennv2)))/2))
print("votes ", len(bidennv2))
print("Both: ", (len(bothnv2)/(len(trumpnv2)+len(bidennv2))))
print("Nevada 3")
trumpnv3votes = (len(trumpnv3)/(len(trumpnv3)+len(bidennv3)))*289379
bidennv3votes = (len(bidennv3)/(len(trumpnv3)+len(bidennv3)))*289379
bothnv3 = trumpnv3.intersection(bidennv3)
bothnv3votes = (len(bothnv3)/(len(trumpnv3)+len(bidennv3)))*289379
print("Trump: ", (len(trumpnv3)/(len(trumpnv3)+len(bidennv3)))-((len(bothnv3)/(len(trumpnv3)+len(bidennv3)))/2))
print("votes ", len(trumpnv3))
print("Biden: ",(len(bidennv3)/(len(trumpnv3)+len(bidennv3)))-((len(bothnv3)/(len(trumpnv3)+len(bidennv3)))/2))
print("votes ", len(bidennv3))
print("Both: ", (len(bothnv3)/(len(trumpnv3)+len(bidennv3))))
print("Nevada 4")
trumpnv4votes = (len(trumpnv4)/(len(trumpnv4)+len(bidennv4)))*246900
bidennv4votes = (len(bidennv4)/(len(trumpnv4)+len(bidennv4)))*246900
bothnv4 = trumpnv4.intersection(bidennv4)
bothnv4votes = (len(bothnv4)/(len(trumpnv4)+len(bidennv4)))*246900
print("Trump: ", (len(trumpnv4)/(len(trumpnv4)+len(bidennv4)))-((len(bothnv4)/(len(trumpnv4)+len(bidennv4)))/2))
print("votes ", len(trumpnv4))
print("Biden: ",(len(bidennv4)/(len(trumpnv4)+len(bidennv4)))-((len(bothnv4)/(len(trumpnv4)+len(bidennv4)))/2))
print("votes ", len(bidennv4))
print("Both: ", (len(bothnv4)/(len(trumpnv4)+len(bidennv4))))
totalnvvotestrump = trumpnv1votes+trumpnv2votes+trumpnv3votes+trumpnv4votes
totalnvvotesbiden = bidennv1votes+bidennv2votes+bidennv3votes+bidennv4votes
totalnvvotesboth = bothnv1votes+bothnv2votes+bothnv3votes+bothnv4votes
print("TOTAL TRUMP VOTES: ", (totalnvvotestrump/(totalnvvotestrump+totalnvvotesbiden))-(totalnvvotesboth/(totalnvvotestrump+totalnvvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalnvvotesbiden/(totalnvvotestrump+totalnvvotesbiden))-(totalnvvotesboth/(totalnvvotestrump+totalnvvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalnvvotesboth/(totalnvvotestrump+totalnvvotesbiden)))
print("")
print("North Carolina")
print("Trump: ", (len(trumpnc)/(len(trumpnc)+len(bidennc))))
print("Biden: ",(len(bidennc)/(len(trumpnc)+len(bidennc))))
print("North Carolina 1")
trumpnc1votes = (len(trumpnc1)/(len(trumpnc1)+len(bidennc1)))*338571
bidennc1votes = (len(bidennc1)/(len(trumpnc1)+len(bidennc1)))*338571
bothnc1 = trumpnc1.intersection(bidennc1)
bothnc1votes = (len(bothnc1)/(len(trumpnc1)+len(bidennc1)))*338571
print("Trump: ", (len(trumpnc1)/(len(trumpnc1)+len(bidennc1)))-((len(bothnc1)/(len(trumpnc1)+len(bidennc1)))/2))
print("votes ", len(trumpnc1))
print("Biden: ",(len(bidennc1)/(len(trumpnc1)+len(bidennc1)))-((len(bothnc1)/(len(trumpnc1)+len(bidennc1)))/2))
print("votes ", len(bidennc1))
print("Both: ", (len(bothnc1)/(len(trumpnc1)+len(bidennc1))))
print("North Carolina 2")
trumpnc2votes = (len(trumpnc2)/(len(trumpnc2)+len(bidennc2)))*386641
bidennc2votes = (len(bidennc2)/(len(trumpnc2)+len(bidennc2)))*386641
bothnc2 = trumpnc2.intersection(bidennc2)
bothnc2votes = (len(bothnc2)/(len(trumpnc2)+len(bidennc2)))*386641
print("Trump: ", (len(trumpnc2)/(len(trumpnc2)+len(bidennc2)))-((len(bothnc2)/(len(trumpnc2)+len(bidennc2)))/2))
print("votes ", len(trumpnc2))
print("Biden: ",(len(bidennc2)/(len(trumpnc2)+len(bidennc2)))-((len(bothnc2)/(len(trumpnc2)+len(bidennc2)))/2))
print("votes ", len(bidennc2))
print("Both: ", (len(bothnc2)/(len(trumpnc2)+len(bidennc2))))
print("North Carolina 3")
trumpnc3votes = (len(trumpnc3)/(len(trumpnc3)+len(bidennc3)))*318857
bidennc3votes = (len(bidennc3)/(len(trumpnc3)+len(bidennc3)))*318857
bothnc3 = trumpnc3.intersection(bidennc3)
bothnc3votes = (len(bothnc3)/(len(trumpnc3)+len(bidennc3)))*318857
print("Trump: ", (len(trumpnc3)/(len(trumpnc3)+len(bidennc3)))-((len(bothnc3)/(len(trumpnc3)+len(bidennc3)))/2))
print("votes ", len(trumpnc3))
print("Biden: ",(len(bidennc3)/(len(trumpnc3)+len(bidennc3)))-((len(bothnc3)/(len(trumpnc3)+len(bidennc3)))/2))
print("votes ", len(bidennc3))
print("Both: ", (len(bothnc3)/(len(trumpnc3)+len(bidennc3))))
print("North Carolina 4")
trumpnc4votes = (len(trumpnc4)/(len(trumpnc4)+len(bidennc4)))*403832
bidennc4votes = (len(bidennc4)/(len(trumpnc4)+len(bidennc4)))*403832
bothnc4 = trumpnc4.intersection(bidennc4)
bothnc4votes = (len(bothnc4)/(len(trumpnc4)+len(bidennc4)))*403832
print("Trump: ", (len(trumpnc4)/(len(trumpnc4)+len(bidennc4)))-((len(bothnc4)/(len(trumpnc4)+len(bidennc4)))/2))
print("votes ", len(trumpnc4))
print("Biden: ",(len(bidennc4)/(len(trumpnc4)+len(bidennc4)))-((len(bothnc4)/(len(trumpnc4)+len(bidennc4)))/2))
print("votes ", len(bidennc4))
print("Both: ", (len(bothnc4)/(len(trumpnc4)+len(bidennc4))))
print("North Carolina 5")
trumpnc5votes = (len(trumpnc5)/(len(trumpnc5)+len(bidennc5)))*350540
bidennc5votes = (len(bidennc5)/(len(trumpnc5)+len(bidennc5)))*350540
bothnc5 = trumpnc5.intersection(bidennc5)
bothnc5votes = (len(bothnc5)/(len(trumpnc5)+len(bidennc5)))*350540
print("Trump: ", (len(trumpnc5)/(len(trumpnc5)+len(bidennc5)))-((len(bothnc5)/(len(trumpnc5)+len(bidennc5)))/2))
print("votes ", len(trumpnc5))
print("Biden: ",(len(bidennc5)/(len(trumpnc5)+len(bidennc5)))-((len(bothnc5)/(len(trumpnc5)+len(bidennc5)))/2))
print("votes ", len(bidennc5))
print("Both: ", (len(bothnc5)/(len(trumpnc5)+len(bidennc5))))
print("North Carolina 6")
trumpnc6votes = (len(trumpnc6)/(len(trumpnc6)+len(bidennc6)))*347453
bidennc6votes = (len(bidennc6)/(len(trumpnc6)+len(bidennc6)))*347453
bothnc6 = trumpnc6.intersection(bidennc6)
bothnc6votes = (len(bothnc6)/(len(trumpnc6)+len(bidennc6)))*347453
print("Trump: ", (len(trumpnc6)/(len(trumpnc6)+len(bidennc6)))-((len(bothnc6)/(len(trumpnc6)+len(bidennc6)))/2))
print("votes ", len(trumpnc6))
print("Biden: ",(len(bidennc6)/(len(trumpnc6)+len(bidennc6)))-((len(bothnc6)/(len(trumpnc6)+len(bidennc6)))/2))
print("votes ", len(bidennc6))
print("Both: ", (len(bothnc6)/(len(trumpnc6)+len(bidennc6))))
print("North Carolina 7")
trumpnc7votes = (len(trumpnc7)/(len(trumpnc7)+len(bidennc7)))*344277
bidennc7votes = (len(bidennc7)/(len(trumpnc7)+len(bidennc7)))*344277
bothnc7 = trumpnc7.intersection(bidennc7)
bothnc7votes = (len(bothnc7)/(len(trumpnc7)+len(bidennc7)))*344277
print("Trump: ", (len(trumpnc7)/(len(trumpnc7)+len(bidennc7)))-((len(bothnc7)/(len(trumpnc7)+len(bidennc7)))/2))
print("votes ", len(trumpnc7))
print("Biden: ",(len(bidennc7)/(len(trumpnc7)+len(bidennc7)))-((len(bothnc7)/(len(trumpnc7)+len(bidennc7)))/2))
print("votes ", len(bidennc7))
print("Both: ", (len(bothnc7)/(len(trumpnc7)+len(bidennc7))))
print("North Carolina 8")
trumpnc8votes = (len(trumpnc8)/(len(trumpnc8)+len(bidennc8)))*319337
bidennc8votes = (len(bidennc8)/(len(trumpnc8)+len(bidennc8)))*319337
bothnc8 = trumpnc8.intersection(bidennc8)
bothnc8votes = (len(bothnc8)/(len(trumpnc8)+len(bidennc8)))*319337
print("Trump: ", (len(trumpnc8)/(len(trumpnc8)+len(bidennc8)))-((len(bothnc8)/(len(trumpnc8)+len(bidennc8)))/2))
print("votes ", len(trumpnc8))
print("Biden: ",(len(bidennc8)/(len(trumpnc8)+len(bidennc8)))-((len(bothnc8)/(len(trumpnc8)+len(bidennc8)))/2))
print("votes ", len(bidennc8))
print("Both: ", (len(bothnc8)/(len(trumpnc8)+len(bidennc8))))
print("North Carolina 9")
trumpnc9votes = (len(trumpnc9)/(len(trumpnc9)+len(bidennc9)))*328995
bidennc9votes = (len(bidennc9)/(len(trumpnc9)+len(bidennc9)))*328995
bothnc9 = trumpnc9.intersection(bidennc9)
bothnc9votes = (len(bothnc9)/(len(trumpnc9)+len(bidennc9)))*328995
print("Trump: ", (len(trumpnc9)/(len(trumpnc9)+len(bidennc9)))-((len(bothnc9)/(len(trumpnc9)+len(bidennc9)))/2))
print("votes ", len(trumpnc9))
print("Biden: ",(len(bidennc9)/(len(trumpnc9)+len(bidennc9)))-((len(bothnc9)/(len(trumpnc9)+len(bidennc9)))/2))
print("votes ", len(bidennc9))
print("Both: ", (len(bothnc9)/(len(trumpnc9)+len(bidennc9))))
print("North Carolina 10")
trumpnc10votes = (len(trumpnc10)/(len(trumpnc10)+len(bidennc10)))*347703
bidennc10votes = (len(bidennc10)/(len(trumpnc10)+len(bidennc10)))*347703
bothnc10 = trumpnc10.intersection(bidennc10)
bothnc10votes = (len(bothnc10)/(len(trumpnc10)+len(bidennc10)))*347703
print("Trump: ", (len(trumpnc10)/(len(trumpnc10)+len(bidennc10)))-((len(bothnc10)/(len(trumpnc10)+len(bidennc10)))/2))
print("votes ", len(trumpnc10))
print("Biden: ",(len(bidennc10)/(len(trumpnc10)+len(bidennc10)))-((len(bothnc10)/(len(trumpnc10)+len(bidennc10)))/2))
print("votes ", len(bidennc10))
print("Both: ", (len(bothnc10)/(len(trumpnc10)+len(bidennc10))))
print("North Carolina 11")
trumpnc11votes = (len(trumpnc11)/(len(trumpnc11)+len(bidennc11)))*357102
bidennc11votes = (len(bidennc11)/(len(trumpnc11)+len(bidennc11)))*357102
bothnc11 = trumpnc11.intersection(bidennc11)
bothnc11votes = (len(bothnc11)/(len(trumpnc11)+len(bidennc11)))*357102
print("Trump: ", (len(trumpnc11)/(len(trumpnc11)+len(bidennc11)))-((len(bothnc11)/(len(trumpnc11)+len(bidennc11)))/2))
print("votes ", len(trumpnc11))
print("Biden: ",(len(bidennc11)/(len(trumpnc11)+len(bidennc11)))-((len(bothnc11)/(len(trumpnc11)+len(bidennc11)))/2))
print("votes ", len(bidennc11))
print("Both: ", (len(bothnc11)/(len(trumpnc11)+len(bidennc11))))
print("North Carolina 12")
trumpnc12votes = (len(trumpnc12)/(len(trumpnc12)+len(bidennc12)))*346693
bidennc12votes = (len(bidennc12)/(len(trumpnc12)+len(bidennc12)))*346693
bothnc12 = trumpnc12.intersection(bidennc12)
bothnc12votes = (len(bothnc12)/(len(trumpnc12)+len(bidennc12)))*346693
print("Trump: ", (len(trumpnc12)/(len(trumpnc12)+len(bidennc12)))-((len(bothnc12)/(len(trumpnc12)+len(bidennc12)))/2))
print("votes ", len(trumpnc12))
print("Biden: ",(len(bidennc12)/(len(trumpnc12)+len(bidennc12)))-((len(bothnc12)/(len(trumpnc12)+len(bidennc12)))/2))
print("votes ", len(bidennc12))
print("Both: ", (len(bothnc12)/(len(trumpnc12)+len(bidennc12))))
print("North Carolina 13")
trumpnc13votes = (len(trumpnc13)/(len(trumpnc13)+len(bidennc13)))*350427
bidennc13votes = (len(bidennc13)/(len(trumpnc13)+len(bidennc13)))*350427
bothnc13 = trumpnc13.intersection(bidennc13)
bothnc13votes = (len(bothnc13)/(len(trumpnc13)+len(bidennc13)))*350427
print("Trump: ", (len(trumpnc13)/(len(trumpnc13)+len(bidennc13)))-((len(bothnc13)/(len(trumpnc13)+len(bidennc13)))/2))
print("votes ", len(trumpnc13))
print("Biden: ",(len(bidennc13)/(len(trumpnc13)+len(bidennc13)))-((len(bothnc13)/(len(trumpnc13)+len(bidennc13)))/2))
print("votes ", len(bidennc13))
print("Both: ", (len(bothnc13)/(len(trumpnc13)+len(bidennc13))))
totalncvotestrump = trumpnc1votes+trumpnc2votes+trumpnc3votes+trumpnc4votes+trumpnc5votes+trumpnc6votes+trumpnc7votes+trumpnc8votes+trumpnc9votes+trumpnc10votes+trumpnc11votes+trumpnc12votes+trumpnc13votes
totalncvotesbiden = bidennc1votes+bidennc2votes+bidennc3votes+bidennc4votes+bidennc5votes+bidennc6votes+bidennc7votes+bidennc8votes+bidennc9votes+bidennc10votes+bidennc11votes+bidennc12votes+bidennc13votes
totalncvotesboth = bothnc1votes+bothnc2votes+bothnc3votes+bothnc4votes+bothnc5votes+bothnc6votes+bothnc7votes+bothnc8votes+bothnc9votes+bothnc10votes+bothnc11votes+bothnc12votes+bothnc13votes
print("TOTAL TRUMP VOTES: ", (totalncvotestrump/(totalncvotestrump+totalncvotesbiden))-(totalncvotesboth/(totalncvotestrump+totalncvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalncvotesbiden/(totalncvotestrump+totalncvotesbiden))-(totalncvotesboth/(totalncvotestrump+totalncvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalncvotesboth/(totalncvotestrump+totalncvotesbiden)))
print("")
print("Oklahoma")
print("Trump: ", (len(trumpok)/(len(trumpok)+len(bidenok))))
print("Biden: ",(len(bidenok)/(len(trumpok)+len(bidenok))))
print("Oklahoma 1")
trumpok1votes = (len(trumpok1)/(len(trumpok1)+len(bidenok1)))*1
bidenok1votes = (len(bidenok1)/(len(trumpok1)+len(bidenok1)))*1
bothok1 = trumpok1.intersection(bidenok1)
bothok1votes = (len(bothok1)/(len(trumpok1)+len(bidenok1)))*1
print("Trump: ", (len(trumpok1)/(len(trumpok1)+len(bidenok1)))-((len(bothok1)/(len(trumpok1)+len(bidenok1)))/2))
print("votes ", len(trumpok1))
print("Biden: ",(len(bidenok1)/(len(trumpok1)+len(bidenok1)))-((len(bothok1)/(len(trumpok1)+len(bidenok1)))/2))
print("votes ", len(bidenok1))
print("Both: ", (len(bothok1)/(len(trumpok1)+len(bidenok1))))
print("Oklahoma 2")
trumpok2votes = (len(trumpok2)/(len(trumpok2)+len(bidenok2)))*1
bidenok2votes = (len(bidenok2)/(len(trumpok2)+len(bidenok2)))*1
bothok2 = trumpok2.intersection(bidenok2)
bothok2votes = (len(bothok2)/(len(trumpok2)+len(bidenok2)))*1
print("Trump: ", (len(trumpok2)/(len(trumpok2)+len(bidenok2)))-((len(bothok2)/(len(trumpok2)+len(bidenok2)))/2))
print("votes ", len(trumpok2))
print("Biden: ",(len(bidenok2)/(len(trumpok2)+len(bidenok2)))-((len(bothok2)/(len(trumpok2)+len(bidenok2)))/2))
print("votes ", len(bidenok2))
print("Both: ", (len(bothok2)/(len(trumpok2)+len(bidenok2))))
print("Oklahoma 3")
trumpok3votes = (len(trumpok3)/(len(trumpok3)+len(bidenok3)))*1
bidenok3votes = (len(bidenok3)/(len(trumpok3)+len(bidenok3)))*1
bothok3 = trumpok3.intersection(bidenok3)
bothok3votes = (len(bothok3)/(len(trumpok3)+len(bidenok3)))*1
print("Trump: ", (len(trumpok3)/(len(trumpok3)+len(bidenok3)))-((len(bothok3)/(len(trumpok3)+len(bidenok3)))/2))
print("votes ", len(trumpok3))
print("Biden: ",(len(bidenok3)/(len(trumpok3)+len(bidenok3)))-((len(bothok3)/(len(trumpok3)+len(bidenok3)))/2))
print("votes ", len(bidenok3))
print("Both: ", (len(bothok3)/(len(trumpok3)+len(bidenok3))))
print("Oklahoma 4")
trumpok4votes = (len(trumpok4)/(len(trumpok4)+len(bidenok4)))*1
bidenok4votes = (len(bidenok4)/(len(trumpok4)+len(bidenok4)))*1
bothok4 = trumpok4.intersection(bidenok4)
bothok4votes = (len(bothok4)/(len(trumpok4)+len(bidenok4)))*1
print("Trump: ", (len(trumpok4)/(len(trumpok4)+len(bidenok4)))-((len(bothok4)/(len(trumpok4)+len(bidenok4)))/2))
print("votes ", len(trumpok4))
print("Biden: ",(len(bidenok4)/(len(trumpok4)+len(bidenok4)))-((len(bothok4)/(len(trumpok4)+len(bidenok4)))/2))
print("votes ", len(bidenok4))
print("Both: ", (len(bothok4)/(len(trumpok4)+len(bidenok4))))
print("Oklahoma 5")
trumpok5votes = (len(trumpok5)/(len(trumpok5)+len(bidenok5)))*1
bidenok5votes = (len(bidenok5)/(len(trumpok5)+len(bidenok5)))*1
bothok5 = trumpok5.intersection(bidenok5)
bothok5votes = (len(bothok5)/(len(trumpok5)+len(bidenok5)))*1
print("Trump: ", (len(trumpok5)/(len(trumpok5)+len(bidenok5)))-((len(bothok5)/(len(trumpok5)+len(bidenok5)))/2))
print("votes ", len(trumpok5))
print("Biden: ",(len(bidenok5)/(len(trumpok5)+len(bidenok5)))-((len(bothok5)/(len(trumpok5)+len(bidenok5)))/2))
print("votes ", len(bidenok5))
print("Both: ", (len(bothok5)/(len(trumpok5)+len(bidenok5))))
totalokvotestrump = trumpok1votes+trumpok2votes+trumpok3votes+trumpok4votes+trumpok5votes
totalokvotesbiden = bidenok1votes+bidenok2votes+bidenok3votes+bidenok4votes+bidenok5votes
totalokvotesboth = bothok1votes+bothok2votes+bothok3votes+bothok4votes+bothok5votes
print("TOTAL TRUMP VOTES: ", (totalokvotestrump/(totalokvotestrump+totalokvotesbiden))-(totalokvotesboth/(totalokvotestrump+totalokvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalokvotesbiden/(totalokvotestrump+totalokvotesbiden))-(totalokvotesboth/(totalokvotestrump+totalokvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalokvotesboth/(totalokvotestrump+totalokvotesbiden)))
print("")
print("New York")
print("Trump: ", (len(trumpny)/(len(trumpny)+len(bidenny))))
print("Biden: ",(len(bidenny)/(len(trumpny)+len(bidenny))))
print("New York 1")
trumpny1votes = (len(trumpny1)/(len(trumpny1)+len(bidenny1)))*1
bidenny1votes = (len(bidenny1)/(len(trumpny1)+len(bidenny1)))*1
bothny1 = trumpny1.intersection(bidenny1)
bothny1votes = (len(bothny1)/(len(trumpny1)+len(bidenny1)))*1
print("Trump: ", (len(trumpny1)/(len(trumpny1)+len(bidenny1)))-((len(bothny1)/(len(trumpny1)+len(bidenny1)))/2))
print("votes ", len(trumpny1))
print("Biden: ",(len(bidenny1)/(len(trumpny1)+len(bidenny1)))-((len(bothny1)/(len(trumpny1)+len(bidenny1)))/2))
print("votes ", len(bidenny1))
print("Both: ", (len(bothny1)/(len(trumpny1)+len(bidenny1))))
print("New York 2")
trumpny2votes = (len(trumpny2)/(len(trumpny2)+len(bidenny2)))*1
bidenny2votes = (len(bidenny2)/(len(trumpny2)+len(bidenny2)))*1
bothny2 = trumpny2.intersection(bidenny2)
bothny2votes = (len(bothny2)/(len(trumpny2)+len(bidenny2)))*1
print("Trump: ", (len(trumpny2)/(len(trumpny2)+len(bidenny2)))-((len(bothny2)/(len(trumpny2)+len(bidenny2)))/2))
print("votes ", len(trumpny2))
print("Biden: ",(len(bidenny2)/(len(trumpny2)+len(bidenny2)))-((len(bothny2)/(len(trumpny2)+len(bidenny2)))/2))
print("votes ", len(bidenny2))
print("Both: ", (len(bothny2)/(len(trumpny2)+len(bidenny2))))
print("New York 3")
trumpny3votes = (len(trumpny3)/(len(trumpny3)+len(bidenny3)))*1
bidenny3votes = (len(bidenny3)/(len(trumpny3)+len(bidenny3)))*1
bothny3 = trumpny3.intersection(bidenny3)
bothny3votes = (len(bothny3)/(len(trumpny3)+len(bidenny3)))*1
print("Trump: ", (len(trumpny3)/(len(trumpny3)+len(bidenny3)))-((len(bothny3)/(len(trumpny3)+len(bidenny3)))/2))
print("votes ", len(trumpny3))
print("Biden: ",(len(bidenny3)/(len(trumpny3)+len(bidenny3)))-((len(bothny3)/(len(trumpny3)+len(bidenny3)))/2))
print("votes ", len(bidenny3))
print("Both: ", (len(bothny3)/(len(trumpny3)+len(bidenny3))))
print("New York 4")
trumpny4votes = (len(trumpny4)/(len(trumpny4)+len(bidenny4)))*1
bidenny4votes = (len(bidenny4)/(len(trumpny4)+len(bidenny4)))*1
bothny4 = trumpny4.intersection(bidenny4)
bothny4votes = (len(bothny4)/(len(trumpny4)+len(bidenny4)))*1
print("Trump: ", (len(trumpny4)/(len(trumpny4)+len(bidenny4)))-((len(bothny4)/(len(trumpny4)+len(bidenny4)))/2))
print("votes ", len(trumpny4))
print("Biden: ",(len(bidenny4)/(len(trumpny4)+len(bidenny4)))-((len(bothny4)/(len(trumpny4)+len(bidenny4)))/2))
print("votes ", len(bidenny4))
print("Both: ", (len(bothny4)/(len(trumpny4)+len(bidenny4))))
print("New York 5")
trumpny5votes = (len(trumpny5)/(len(trumpny5)+len(bidenny5)))*1
bidenny5votes = (len(bidenny5)/(len(trumpny5)+len(bidenny5)))*1
bothny5 = trumpny5.intersection(bidenny5)
bothny5votes = (len(bothny5)/(len(trumpny5)+len(bidenny5)))*1
print("Trump: ", (len(trumpny5)/(len(trumpny5)+len(bidenny5)))-((len(bothny5)/(len(trumpny5)+len(bidenny5)))/2))
print("votes ", len(trumpny5))
print("Biden: ",(len(bidenny5)/(len(trumpny5)+len(bidenny5)))-((len(bothny5)/(len(trumpny5)+len(bidenny5)))/2))
print("votes ", len(bidenny5))
print("Both: ", (len(bothny5)/(len(trumpny5)+len(bidenny5))))
print("New York 6")
trumpny6votes = (len(trumpny6)/(len(trumpny6)+len(bidenny6)))*1
bidenny6votes = (len(bidenny6)/(len(trumpny6)+len(bidenny6)))*1
bothny6 = trumpny6.intersection(bidenny6)
bothny6votes = (len(bothny6)/(len(trumpny6)+len(bidenny6)))*1
print("Trump: ", (len(trumpny6)/(len(trumpny6)+len(bidenny6)))-((len(bothny6)/(len(trumpny6)+len(bidenny6)))/2))
print("votes ", len(trumpny6))
print("Biden: ",(len(bidenny6)/(len(trumpny6)+len(bidenny6)))-((len(bothny6)/(len(trumpny6)+len(bidenny6)))/2))
print("votes ", len(bidenny6))
print("Both: ", (len(bothny6)/(len(trumpny6)+len(bidenny6))))
print("New York 7")
trumpny7votes = (len(trumpny7)/(len(trumpny7)+len(bidenny7)))*1
bidenny7votes = (len(bidenny7)/(len(trumpny7)+len(bidenny7)))*1
bothny7 = trumpny7.intersection(bidenny7)
bothny7votes = (len(bothny7)/(len(trumpny7)+len(bidenny7)))*1
print("Trump: ", (len(trumpny7)/(len(trumpny7)+len(bidenny7)))-((len(bothny7)/(len(trumpny7)+len(bidenny7)))/2))
print("votes ", len(trumpny7))
print("Biden: ",(len(bidenny7)/(len(trumpny7)+len(bidenny7)))-((len(bothny7)/(len(trumpny7)+len(bidenny7)))/2))
print("votes ", len(bidenny7))
print("Both: ", (len(bothny7)/(len(trumpny7)+len(bidenny7))))
print("New York 8")
trumpny8votes = (len(trumpny8)/(len(trumpny8)+len(bidenny8)))*1
bidenny8votes = (len(bidenny8)/(len(trumpny8)+len(bidenny8)))*1
bothny8 = trumpny8.intersection(bidenny8)
bothny8votes = (len(bothny8)/(len(trumpny8)+len(bidenny8)))*1
print("Trump: ", (len(trumpny8)/(len(trumpny8)+len(bidenny8)))-((len(bothny8)/(len(trumpny8)+len(bidenny8)))/2))
print("votes ", len(trumpny8))
print("Biden: ",(len(bidenny8)/(len(trumpny8)+len(bidenny8)))-((len(bothny8)/(len(trumpny8)+len(bidenny8)))/2))
print("votes ", len(bidenny8))
print("Both: ", (len(bothny8)/(len(trumpny8)+len(bidenny8))))
print("New York 9")
trumpny9votes = (len(trumpny9)/(len(trumpny9)+len(bidenny9)))*1
bidenny9votes = (len(bidenny9)/(len(trumpny9)+len(bidenny9)))*1
bothny9 = trumpny9.intersection(bidenny9)
bothny9votes = (len(bothny9)/(len(trumpny9)+len(bidenny9)))*1
print("Trump: ", (len(trumpny9)/(len(trumpny9)+len(bidenny9)))-((len(bothny9)/(len(trumpny9)+len(bidenny9)))/2))
print("votes ", len(trumpny9))
print("Biden: ",(len(bidenny9)/(len(trumpny9)+len(bidenny9)))-((len(bothny9)/(len(trumpny9)+len(bidenny9)))/2))
print("votes ", len(bidenny9))
print("Both: ", (len(bothny9)/(len(trumpny9)+len(bidenny9))))
print("New York 10")
trumpny10votes = (len(trumpny10)/(len(trumpny10)+len(bidenny10)))*1
bidenny10votes = (len(bidenny10)/(len(trumpny10)+len(bidenny10)))*1
bothny10 = trumpny10.intersection(bidenny10)
bothny10votes = (len(bothny10)/(len(trumpny10)+len(bidenny10)))*1
print("Trump: ", (len(trumpny10)/(len(trumpny10)+len(bidenny10)))-((len(bothny10)/(len(trumpny10)+len(bidenny10)))/2))
print("votes ", len(trumpny10))
print("Biden: ",(len(bidenny10)/(len(trumpny10)+len(bidenny10)))-((len(bothny10)/(len(trumpny10)+len(bidenny10)))/2))
print("votes ", len(bidenny10))
print("Both: ", (len(bothny10)/(len(trumpny10)+len(bidenny10))))
print("New York 11")
trumpny11votes = (len(trumpny11)/(len(trumpny11)+len(bidenny11)))*1
bidenny11votes = (len(bidenny11)/(len(trumpny11)+len(bidenny11)))*1
bothny11 = trumpny11.intersection(bidenny11)
bothny11votes = (len(bothny11)/(len(trumpny11)+len(bidenny11)))*1
print("Trump: ", (len(trumpny11)/(len(trumpny11)+len(bidenny11)))-((len(bothny11)/(len(trumpny11)+len(bidenny11)))/2))
print("votes ", len(trumpny11))
print("Biden: ",(len(bidenny11)/(len(trumpny11)+len(bidenny11)))-((len(bothny11)/(len(trumpny11)+len(bidenny11)))/2))
print("votes ", len(bidenny11))
print("Both: ", (len(bothny11)/(len(trumpny11)+len(bidenny11))))
print("New York 12")
trumpny12votes = (len(trumpny12)/(len(trumpny12)+len(bidenny12)))*1
bidenny12votes = (len(bidenny12)/(len(trumpny12)+len(bidenny12)))*1
bothny12 = trumpny12.intersection(bidenny12)
bothny12votes = (len(bothny12)/(len(trumpny12)+len(bidenny12)))*1
print("Trump: ", (len(trumpny12)/(len(trumpny12)+len(bidenny12)))-((len(bothny12)/(len(trumpny12)+len(bidenny12)))/2))
print("votes ", len(trumpny12))
print("Biden: ",(len(bidenny12)/(len(trumpny12)+len(bidenny12)))-((len(bothny12)/(len(trumpny12)+len(bidenny12)))/2))
print("votes ", len(bidenny12))
print("Both: ", (len(bothny12)/(len(trumpny12)+len(bidenny12))))
print("New York 13")
trumpny13votes = (len(trumpny13)/(len(trumpny13)+len(bidenny13)))*1
bidenny13votes = (len(bidenny13)/(len(trumpny13)+len(bidenny13)))*1
bothny13 = trumpny13.intersection(bidenny13)
bothny13votes = (len(bothny13)/(len(trumpny13)+len(bidenny13)))*1
print("Trump: ", (len(trumpny13)/(len(trumpny13)+len(bidenny13)))-((len(bothny13)/(len(trumpny13)+len(bidenny13)))/2))
print("votes ", len(trumpny13))
print("Biden: ",(len(bidenny13)/(len(trumpny13)+len(bidenny13)))-((len(bothny13)/(len(trumpny13)+len(bidenny13)))/2))
print("votes ", len(bidenny13))
print("Both: ", (len(bothny13)/(len(trumpny13)+len(bidenny13))))
print("New York 14")
trumpny14votes = (len(trumpny14)/(len(trumpny14)+len(bidenny14)))*1
bidenny14votes = (len(bidenny14)/(len(trumpny14)+len(bidenny14)))*1
bothny14 = trumpny14.intersection(bidenny14)
bothny14votes = (len(bothny14)/(len(trumpny14)+len(bidenny14)))*1
print("Trump: ", (len(trumpny14)/(len(trumpny14)+len(bidenny14)))-((len(bothny14)/(len(trumpny14)+len(bidenny14)))/2))
print("votes ", len(trumpny14))
print("Biden: ",(len(bidenny14)/(len(trumpny14)+len(bidenny14)))-((len(bothny14)/(len(trumpny14)+len(bidenny14)))/2))
print("votes ", len(bidenny14))
print("Both: ", (len(bothny14)/(len(trumpny14)+len(bidenny14))))
print("New York 15")
trumpny15votes = (len(trumpny15)/(len(trumpny15)+len(bidenny15)))*1
bidenny15votes = (len(bidenny15)/(len(trumpny15)+len(bidenny15)))*1
bothny15 = trumpny15.intersection(bidenny15)
bothny15votes = (len(bothny15)/(len(trumpny15)+len(bidenny15)))*1
print("Trump: ", (len(trumpny15)/(len(trumpny15)+len(bidenny15)))-((len(bothny15)/(len(trumpny15)+len(bidenny15)))/2))
print("votes ", len(trumpny15))
print("Biden: ",(len(bidenny15)/(len(trumpny15)+len(bidenny15)))-((len(bothny15)/(len(trumpny15)+len(bidenny15)))/2))
print("votes ", len(bidenny15))
print("Both: ", (len(bothny15)/(len(trumpny15)+len(bidenny15))))
print("New York 16")
trumpny16votes = (len(trumpny16)/(len(trumpny16)+len(bidenny16)))*1
bidenny16votes = (len(bidenny16)/(len(trumpny16)+len(bidenny16)))*1
bothny16 = trumpny16.intersection(bidenny16)
bothny16votes = (len(bothny16)/(len(trumpny16)+len(bidenny16)))*1
print("Trump: ", (len(trumpny16)/(len(trumpny16)+len(bidenny16)))-((len(bothny16)/(len(trumpny16)+len(bidenny16)))/2))
print("votes ", len(trumpny16))
print("Biden: ",(len(bidenny16)/(len(trumpny16)+len(bidenny16)))-((len(bothny16)/(len(trumpny16)+len(bidenny16)))/2))
print("votes ", len(bidenny16))
print("Both: ", (len(bothny16)/(len(trumpny16)+len(bidenny16))))
print("New York 17")
trumpny17votes = (len(trumpny17)/(len(trumpny17)+len(bidenny17)))*1
bidenny17votes = (len(bidenny17)/(len(trumpny17)+len(bidenny17)))*1
bothny17 = trumpny17.intersection(bidenny17)
bothny17votes = (len(bothny17)/(len(trumpny17)+len(bidenny17)))*1
print("Trump: ", (len(trumpny17)/(len(trumpny17)+len(bidenny17)))-((len(bothny17)/(len(trumpny17)+len(bidenny17)))/2))
print("votes ", len(trumpny17))
print("Biden: ",(len(bidenny17)/(len(trumpny17)+len(bidenny17)))-((len(bothny17)/(len(trumpny17)+len(bidenny17)))/2))
print("votes ", len(bidenny17))
print("Both: ", (len(bothny17)/(len(trumpny17)+len(bidenny17))))
print("New York 18")
trumpny18votes = (len(trumpny18)/(len(trumpny18)+len(bidenny18)))*1
bidenny18votes = (len(bidenny18)/(len(trumpny18)+len(bidenny18)))*1
bothny18 = trumpny18.intersection(bidenny18)
bothny18votes = (len(bothny18)/(len(trumpny18)+len(bidenny18)))*1
print("Trump: ", (len(trumpny18)/(len(trumpny18)+len(bidenny18)))-((len(bothny18)/(len(trumpny18)+len(bidenny18)))/2))
print("votes ", len(trumpny18))
print("Biden: ",(len(bidenny18)/(len(trumpny18)+len(bidenny18)))-((len(bothny18)/(len(trumpny18)+len(bidenny18)))/2))
print("votes ", len(bidenny18))
print("Both: ", (len(bothny18)/(len(trumpny18)+len(bidenny18))))
print("New York 19")
trumpny19votes = (len(trumpny19)/(len(trumpny19)+len(bidenny19)))*1
bidenny19votes = (len(bidenny19)/(len(trumpny19)+len(bidenny19)))*1
bothny19 = trumpny19.intersection(bidenny19)
bothny19votes = (len(bothny19)/(len(trumpny19)+len(bidenny19)))*1
print("Trump: ", (len(trumpny19)/(len(trumpny19)+len(bidenny19)))-((len(bothny19)/(len(trumpny19)+len(bidenny19)))/2))
print("votes ", len(trumpny19))
print("Biden: ",(len(bidenny19)/(len(trumpny19)+len(bidenny19)))-((len(bothny19)/(len(trumpny19)+len(bidenny19)))/2))
print("votes ", len(bidenny19))
print("Both: ", (len(bothny19)/(len(trumpny19)+len(bidenny19))))
print("New York 20")
trumpny20votes = (len(trumpny20)/(len(trumpny20)+len(bidenny20)))*1
bidenny20votes = (len(bidenny20)/(len(trumpny20)+len(bidenny20)))*1
bothny20 = trumpny20.intersection(bidenny20)
bothny20votes = (len(bothny20)/(len(trumpny20)+len(bidenny20)))*1
print("Trump: ", (len(trumpny20)/(len(trumpny20)+len(bidenny20)))-((len(bothny20)/(len(trumpny20)+len(bidenny20)))/2))
print("votes ", len(trumpny20))
print("Biden: ",(len(bidenny20)/(len(trumpny20)+len(bidenny20)))-((len(bothny20)/(len(trumpny20)+len(bidenny20)))/2))
print("votes ", len(bidenny20))
print("Both: ", (len(bothny20)/(len(trumpny20)+len(bidenny20))))
print("New York 21")
trumpny21votes = (len(trumpny21)/(len(trumpny21)+len(bidenny21)))*1
bidenny21votes = (len(bidenny21)/(len(trumpny21)+len(bidenny21)))*1
bothny21 = trumpny21.intersection(bidenny21)
bothny21votes = (len(bothny21)/(len(trumpny21)+len(bidenny21)))*1
print("Trump: ", (len(trumpny21)/(len(trumpny21)+len(bidenny21)))-((len(bothny21)/(len(trumpny21)+len(bidenny21)))/2))
print("votes ", len(trumpny21))
print("Biden: ",(len(bidenny21)/(len(trumpny21)+len(bidenny21)))-((len(bothny21)/(len(trumpny21)+len(bidenny21)))/2))
print("votes ", len(bidenny21))
print("Both: ", (len(bothny21)/(len(trumpny21)+len(bidenny21))))
print("New York 22")
trumpny22votes = (len(trumpny22)/(len(trumpny22)+len(bidenny22)))*1
bidenny22votes = (len(bidenny22)/(len(trumpny22)+len(bidenny22)))*1
bothny22 = trumpny22.intersection(bidenny22)
bothny22votes = (len(bothny22)/(len(trumpny22)+len(bidenny22)))*1
print("Trump: ", (len(trumpny22)/(len(trumpny22)+len(bidenny22)))-((len(bothny22)/(len(trumpny22)+len(bidenny22)))/2))
print("votes ", len(trumpny22))
print("Biden: ",(len(bidenny22)/(len(trumpny22)+len(bidenny22)))-((len(bothny22)/(len(trumpny22)+len(bidenny22)))/2))
print("votes ", len(bidenny22))
print("Both: ", (len(bothny22)/(len(trumpny22)+len(bidenny22))))
print("New York 23")
trumpny23votes = (len(trumpny23)/(len(trumpny23)+len(bidenny23)))*1
bidenny23votes = (len(bidenny23)/(len(trumpny23)+len(bidenny23)))*1
bothny23 = trumpny23.intersection(bidenny23)
bothny23votes = (len(bothny23)/(len(trumpny23)+len(bidenny23)))*1
print("Trump: ", (len(trumpny23)/(len(trumpny23)+len(bidenny23)))-((len(bothny23)/(len(trumpny23)+len(bidenny23)))/2))
print("votes ", len(trumpny23))
print("Biden: ",(len(bidenny23)/(len(trumpny23)+len(bidenny23)))-((len(bothny23)/(len(trumpny23)+len(bidenny23)))/2))
print("votes ", len(bidenny23))
print("Both: ", (len(bothny23)/(len(trumpny23)+len(bidenny23))))
print("New York 24")
trumpny24votes = (len(trumpny24)/(len(trumpny24)+len(bidenny24)))*1
bidenny24votes = (len(bidenny24)/(len(trumpny24)+len(bidenny24)))*1
bothny24 = trumpny24.intersection(bidenny24)
bothny24votes = (len(bothny24)/(len(trumpny24)+len(bidenny24)))*1
print("Trump: ", (len(trumpny24)/(len(trumpny24)+len(bidenny24)))-((len(bothny24)/(len(trumpny24)+len(bidenny24)))/2))
print("votes ", len(trumpny24))
print("Biden: ",(len(bidenny24)/(len(trumpny24)+len(bidenny24)))-((len(bothny24)/(len(trumpny24)+len(bidenny24)))/2))
print("votes ", len(bidenny24))
print("Both: ", (len(bothny24)/(len(trumpny24)+len(bidenny24))))
print("New York 25")
trumpny25votes = (len(trumpny25)/(len(trumpny25)+len(bidenny25)))*1
bidenny25votes = (len(bidenny25)/(len(trumpny25)+len(bidenny25)))*1
bothny25 = trumpny25.intersection(bidenny25)
bothny25votes = (len(bothny25)/(len(trumpny25)+len(bidenny25)))*1
print("Trump: ", (len(trumpny25)/(len(trumpny25)+len(bidenny25)))-((len(bothny25)/(len(trumpny25)+len(bidenny25)))/2))
print("votes ", len(trumpny25))
print("Biden: ",(len(bidenny25)/(len(trumpny25)+len(bidenny25)))-((len(bothny25)/(len(trumpny25)+len(bidenny25)))/2))
print("votes ", len(bidenny25))
print("Both: ", (len(bothny25)/(len(trumpny25)+len(bidenny25))))
print("New York 26")
trumpny26votes = (len(trumpny26)/(len(trumpny26)+len(bidenny26)))*1
bidenny26votes = (len(bidenny26)/(len(trumpny26)+len(bidenny26)))*1
bothny26 = trumpny26.intersection(bidenny26)
bothny26votes = (len(bothny26)/(len(trumpny26)+len(bidenny26)))*1
print("Trump: ", (len(trumpny26)/(len(trumpny26)+len(bidenny26)))-((len(bothny26)/(len(trumpny26)+len(bidenny26)))/2))
print("votes ", len(trumpny26))
print("Biden: ",(len(bidenny26)/(len(trumpny26)+len(bidenny26)))-((len(bothny26)/(len(trumpny26)+len(bidenny26)))/2))
print("votes ", len(bidenny26))
print("Both: ", (len(bothny26)/(len(trumpny26)+len(bidenny26))))
print("New York 27")
trumpny27votes = (len(trumpny27)/(len(trumpny27)+len(bidenny27)))*1
bidenny27votes = (len(bidenny27)/(len(trumpny27)+len(bidenny27)))*1
bothny27 = trumpny27.intersection(bidenny27)
bothny27votes = (len(bothny27)/(len(trumpny27)+len(bidenny27)))*1
print("Trump: ", (len(trumpny27)/(len(trumpny27)+len(bidenny27)))-((len(bothny27)/(len(trumpny27)+len(bidenny27)))/2))
print("votes ", len(trumpny27))
print("Biden: ",(len(bidenny27)/(len(trumpny27)+len(bidenny27)))-((len(bothny27)/(len(trumpny27)+len(bidenny27)))/2))
print("votes ", len(bidenny27))
print("Both: ", (len(bothny27)/(len(trumpny27)+len(bidenny27))))
totalnyvotestrump = trumpny1votes+trumpny2votes+trumpny3votes+trumpny4votes+trumpny5votes+trumpny6votes+trumpny7votes+trumpny8votes+trumpny9votes+trumpny10votes+trumpny11votes+trumpny12votes+trumpny13votes+trumpny14votes+trumpny15votes+trumpny16votes+trumpny17votes+trumpny18votes+trumpny19votes+trumpny20votes+trumpny21votes+trumpny22votes+trumpny23votes+trumpny24votes+trumpny25votes+trumpny26votes+trumpny27votes
totalnyvotesbiden = bidenny1votes+bidenny2votes+bidenny3votes+bidenny4votes+bidenny5votes+bidenny6votes+bidenny7votes+bidenny8votes+bidenny9votes+bidenny10votes+bidenny11votes+bidenny12votes+bidenny13votes+bidenny14votes+bidenny15votes+bidenny16votes+bidenny17votes+bidenny18votes+bidenny19votes+bidenny20votes+bidenny21votes+bidenny22votes+bidenny23votes+bidenny24votes+bidenny25votes+bidenny26votes+bidenny27votes
totalnyvotesboth = bothny1votes+bothny2votes+bothny3votes+bothny4votes+bothny5votes+bothny6votes+bothny7votes+bothny8votes+bothny9votes+bothny10votes+bothny11votes+bothny12votes+bothny13votes+bothny14votes+bothny15votes+bothny16votes+bothny17votes+bothny18votes+bothny19votes+bothny20votes+bothny21votes+bothny22votes+bothny23votes+bothny24votes+bothny25votes+bothny26votes+bothny27votes
print("TOTAL TRUMP VOTES: ", (totalnyvotestrump/(totalnyvotestrump+totalnyvotesbiden))-(totalnyvotesboth/(totalnyvotestrump+totalnyvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalnyvotesbiden/(totalnyvotestrump+totalnyvotesbiden))-(totalnyvotesboth/(totalnyvotestrump+totalnyvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalnyvotesboth/(totalnyvotestrump+totalnyvotesbiden)))
print("")
print("North Dakota")
print("Trump: ", (len(trumpnd)/(len(trumpnd)+len(bidennd))))
print("Biden: ",(len(bidennd)/(len(trumpnd)+len(bidennd))))
print("North Dakota 1")
bothnd1 = trumpnd1.intersection(bidennd1)
bothnd1votes = (len(bothnd1)/(len(trumpnd1)+len(bidennd1)))
print("Trump: ", (len(trumpnd1)/(len(trumpnd1)+len(bidennd1)))-((len(bothnd1)/(len(trumpnd1)+len(bidennd1)))/2))
print("votes ", len(trumpnd1))
print("Biden: ",(len(bidennd1)/(len(trumpnd1)+len(bidennd1)))-((len(bothnd1)/(len(trumpnd1)+len(bidennd1)))/2))
print("votes ", len(bidennd1))
print("Both: ", (len(bothnd1)/(len(trumpnd1)+len(bidennd1))))
print("")
print("Montana")
print("Trump: ", (len(trumpmt)/(len(trumpmt)+len(bidenmt))))
print("Biden: ",(len(bidenmt)/(len(trumpmt)+len(bidenmt))))
print("Montana 1")
bothmt1 = trumpmt1.intersection(bidenmt1)
bothmt1votes = (len(bothmt1)/(len(trumpmt1)+len(bidenmt1)))
print("Trump: ", (len(trumpmt1)/(len(trumpmt1)+len(bidenmt1)))-((len(bothmt1)/(len(trumpmt1)+len(bidenmt1)))/2))
print("votes ", len(trumpmt1))
print("Biden: ",(len(bidenmt1)/(len(trumpmt1)+len(bidenmt1)))-((len(bothmt1)/(len(trumpmt1)+len(bidenmt1)))/2))
print("votes ", len(bidenmt1))
print("Both: ", (len(bothmt1)/(len(trumpmt1)+len(bidenmt1))))
print("")
print("Wyoming")
print("Trump: ", (len(trumpwy)/(len(trumpwy)+len(bidenwy))))
print("Biden: ",(len(bidenwy)/(len(trumpwy)+len(bidenwy))))
print("Wyoming 1")
bothwy1 = trumpwy1.intersection(bidenwy1)
bothwy1votes = (len(bothwy1)/(len(trumpwy1)+len(bidenwy1)))
print("Trump: ", (len(trumpwy1)/(len(trumpwy1)+len(bidenwy1)))-((len(bothwy1)/(len(trumpwy1)+len(bidenwy1)))/2))
print("votes ", len(trumpwy1))
print("Biden: ",(len(bidenwy1)/(len(trumpwy1)+len(bidenwy1)))-((len(bothwy1)/(len(trumpwy1)+len(bidenwy1)))/2))
print("votes ", len(bidenwy1))
print("Both: ", (len(bothwy1)/(len(trumpwy1)+len(bidenwy1))))
print("")
print("Vermont")
print("Trump: ", (len(trumpvt)/(len(trumpvt)+len(bidenvt))))
print("Biden: ",(len(bidenvt)/(len(trumpvt)+len(bidenvt))))
print("Vermont 1")
bothvt1 = trumpvt1.intersection(bidenvt1)
bothvt1votes = (len(bothvt1)/(len(trumpvt1)+len(bidenvt1)))
print("Trump: ", (len(trumpvt1)/(len(trumpvt1)+len(bidenvt1)))-((len(bothvt1)/(len(trumpvt1)+len(bidenvt1)))/2))
print("votes ", len(trumpvt1))
print("Biden: ",(len(bidenvt1)/(len(trumpvt1)+len(bidenvt1)))-((len(bothvt1)/(len(trumpvt1)+len(bidenvt1)))/2))
print("votes ", len(bidenvt1))
print("Both: ", (len(bothvt1)/(len(trumpvt1)+len(bidenvt1))))
print("")
print("Ohio")
print("Trump: ", (len(trumpoh)/(len(trumpoh)+len(bidenoh))))
print("Biden: ",(len(bidenoh)/(len(trumpoh)+len(bidenoh))))
print("Ohio 1")
trumpoh1votes = (len(trumpoh1)/(len(trumpoh1)+len(bidenoh1)))*344562
bidenoh1votes = (len(bidenoh1)/(len(trumpoh1)+len(bidenoh1)))*344562
bothoh1 = trumpoh1.intersection(bidenoh1)
bothoh1votes = (len(bothoh1)/(len(trumpoh1)+len(bidenoh1)))*344562
print("Trump: ", (len(trumpoh1)/(len(trumpoh1)+len(bidenoh1)))-((len(bothoh1)/(len(trumpoh1)+len(bidenoh1)))/2))
print("votes ", len(trumpoh1))
print("Biden: ",(len(bidenoh1)/(len(trumpoh1)+len(bidenoh1)))-((len(bothoh1)/(len(trumpoh1)+len(bidenoh1)))/2))
print("votes ", len(bidenoh1))
print("Both: ", (len(bothoh1)/(len(trumpoh1)+len(bidenoh1))))
print("Ohio 2")
trumpoh2votes = (len(trumpoh2)/(len(trumpoh2)+len(bidenoh2)))*323124
bidenoh2votes = (len(bidenoh2)/(len(trumpoh2)+len(bidenoh2)))*323124
bothoh2 = trumpoh2.intersection(bidenoh2)
bothoh2votes = (len(bothoh2)/(len(trumpoh2)+len(bidenoh2)))*323124
print("Trump: ", (len(trumpoh2)/(len(trumpoh2)+len(bidenoh2)))-((len(bothoh2)/(len(trumpoh2)+len(bidenoh2)))/2))
print("votes ", len(trumpoh2))
print("Biden: ",(len(bidenoh2)/(len(trumpoh2)+len(bidenoh2)))-((len(bothoh2)/(len(trumpoh2)+len(bidenoh2)))/2))
print("votes ", len(bidenoh2))
print("Both: ", (len(bothoh2)/(len(trumpoh2)+len(bidenoh2))))
print("Ohio 3")
trumpoh3votes = (len(trumpoh3)/(len(trumpoh3)+len(bidenoh3)))*277576
bidenoh3votes = (len(bidenoh3)/(len(trumpoh3)+len(bidenoh3)))*277576
bothoh3 = trumpoh3.intersection(bidenoh3)
bothoh3votes = (len(bothoh3)/(len(trumpoh3)+len(bidenoh3)))*277576
print("Trump: ", (len(trumpoh3)/(len(trumpoh3)+len(bidenoh3)))-((len(bothoh3)/(len(trumpoh3)+len(bidenoh3)))/2))
print("votes ", len(trumpoh3))
print("Biden: ",(len(bidenoh3)/(len(trumpoh3)+len(bidenoh3)))-((len(bothoh3)/(len(trumpoh3)+len(bidenoh3)))/2))
print("votes ", len(bidenoh3))
print("Both: ", (len(bothoh3)/(len(trumpoh3)+len(bidenoh3))))
print("Ohio 4")
trumpoh4votes = (len(trumpoh4)/(len(trumpoh4)+len(bidenoh4)))*302003
bidenoh4votes = (len(bidenoh4)/(len(trumpoh4)+len(bidenoh4)))*302003
bothoh4 = trumpoh4.intersection(bidenoh4)
bothoh4votes = (len(bothoh4)/(len(trumpoh4)+len(bidenoh4)))*302003
print("Trump: ", (len(trumpoh4)/(len(trumpoh4)+len(bidenoh4)))-((len(bothoh4)/(len(trumpoh4)+len(bidenoh4)))/2))
print("votes ", len(trumpoh4))
print("Biden: ",(len(bidenoh4)/(len(trumpoh4)+len(bidenoh4)))-((len(bothoh4)/(len(trumpoh4)+len(bidenoh4)))/2))
print("votes ", len(bidenoh4))
print("Both: ", (len(bothoh4)/(len(trumpoh4)+len(bidenoh4))))
print("Ohio 5")
trumpoh5votes = (len(trumpoh5)/(len(trumpoh5)+len(bidenoh5)))*338081
bidenoh5votes = (len(bidenoh5)/(len(trumpoh5)+len(bidenoh5)))*338081
bothoh5 = trumpoh5.intersection(bidenoh5)
bothoh5votes = (len(bothoh5)/(len(trumpoh5)+len(bidenoh5)))*338081
print("Trump: ", (len(trumpoh5)/(len(trumpoh5)+len(bidenoh5)))-((len(bothoh5)/(len(trumpoh5)+len(bidenoh5)))/2))
print("votes ", len(trumpoh5))
print("Biden: ",(len(bidenoh5)/(len(trumpoh5)+len(bidenoh5)))-((len(bothoh5)/(len(trumpoh5)+len(bidenoh5)))/2))
print("votes ", len(bidenoh5))
print("Both: ", (len(bothoh5)/(len(trumpoh5)+len(bidenoh5))))
print("Ohio 6")
trumpoh6votes = (len(trumpoh6)/(len(trumpoh6)+len(bidenoh6)))*296115
bidenoh6votes = (len(bidenoh6)/(len(trumpoh6)+len(bidenoh6)))*296115
bothoh6 = trumpoh6.intersection(bidenoh6)
bothoh6votes = (len(bothoh6)/(len(trumpoh6)+len(bidenoh6)))*296115
print("Trump: ", (len(trumpoh6)/(len(trumpoh6)+len(bidenoh6)))-((len(bothoh6)/(len(trumpoh6)+len(bidenoh6)))/2))
print("votes ", len(trumpoh6))
print("Biden: ",(len(bidenoh6)/(len(trumpoh6)+len(bidenoh6)))-((len(bothoh6)/(len(trumpoh6)+len(bidenoh6)))/2))
print("votes ", len(bidenoh6))
print("Both: ", (len(bothoh6)/(len(trumpoh6)+len(bidenoh6))))
print("Ohio 7")
trumpoh7votes = (len(trumpoh7)/(len(trumpoh7)+len(bidenoh7)))*281748
bidenoh7votes = (len(bidenoh7)/(len(trumpoh7)+len(bidenoh7)))*281748
bothoh7 = trumpoh7.intersection(bidenoh7)
bothoh7votes = (len(bothoh7)/(len(trumpoh7)+len(bidenoh7)))*281748
print("Trump: ", (len(trumpoh7)/(len(trumpoh7)+len(bidenoh7)))-((len(bothoh7)/(len(trumpoh7)+len(bidenoh7)))/2))
print("votes ", len(trumpoh7))
print("Biden: ",(len(bidenoh7)/(len(trumpoh7)+len(bidenoh7)))-((len(bothoh7)/(len(trumpoh7)+len(bidenoh7)))/2))
print("votes ", len(bidenoh7))
print("Both: ", (len(bothoh7)/(len(trumpoh7)+len(bidenoh7))))
print("Ohio 8")
trumpoh8votes = (len(trumpoh8)/(len(trumpoh8)+len(bidenoh8)))*304766
bidenoh8votes = (len(bidenoh8)/(len(trumpoh8)+len(bidenoh8)))*304766
bothoh8 = trumpoh8.intersection(bidenoh8)
bothoh8votes = (len(bothoh8)/(len(trumpoh8)+len(bidenoh8)))*304766
print("Trump: ", (len(trumpoh8)/(len(trumpoh8)+len(bidenoh8)))-((len(bothoh8)/(len(trumpoh8)+len(bidenoh8)))/2))
print("votes ", len(trumpoh8))
print("Biden: ",(len(bidenoh8)/(len(trumpoh8)+len(bidenoh8)))-((len(bothoh8)/(len(trumpoh8)+len(bidenoh8)))/2))
print("votes ", len(bidenoh8))
print("Both: ", (len(bothoh8)/(len(trumpoh8)+len(bidenoh8))))
print("Ohio 9")
trumpoh9votes = (len(trumpoh9)/(len(trumpoh9)+len(bidenoh9)))*274237
bidenoh9votes = (len(bidenoh9)/(len(trumpoh9)+len(bidenoh9)))*274237
bothoh9 = trumpoh9.intersection(bidenoh9)
bothoh9votes = (len(bothoh9)/(len(trumpoh9)+len(bidenoh9)))*274237
print("Trump: ", (len(trumpoh9)/(len(trumpoh9)+len(bidenoh9)))-((len(bothoh9)/(len(trumpoh9)+len(bidenoh9)))/2))
print("votes ", len(trumpoh9))
print("Biden: ",(len(bidenoh9)/(len(trumpoh9)+len(bidenoh9)))-((len(bothoh9)/(len(trumpoh9)+len(bidenoh9)))/2))
print("votes ", len(bidenoh9))
print("Both: ", (len(bothoh9)/(len(trumpoh9)+len(bidenoh9))))
print("Ohio 10")
trumpoh10votes = (len(trumpoh10)/(len(trumpoh10)+len(bidenoh10)))*316203
bidenoh10votes = (len(bidenoh10)/(len(trumpoh10)+len(bidenoh10)))*316203
bothoh10 = trumpoh10.intersection(bidenoh10)
bothoh10votes = (len(bothoh10)/(len(trumpoh10)+len(bidenoh10)))*316203
print("Trump: ", (len(trumpoh10)/(len(trumpoh10)+len(bidenoh10)))-((len(bothoh10)/(len(trumpoh10)+len(bidenoh10)))/2))
print("votes ", len(trumpoh10))
print("Biden: ",(len(bidenoh10)/(len(trumpoh10)+len(bidenoh10)))-((len(bothoh10)/(len(trumpoh10)+len(bidenoh10)))/2))
print("votes ", len(bidenoh10))
print("Both: ", (len(bothoh10)/(len(trumpoh10)+len(bidenoh10))))
print("Ohio 11")
trumpoh11votes = (len(trumpoh11)/(len(trumpoh11)+len(bidenoh11)))*291351
bidenoh11votes = (len(bidenoh11)/(len(trumpoh11)+len(bidenoh11)))*291351
bothoh11 = trumpoh11.intersection(bidenoh11)
bothoh11votes = (len(bothoh11)/(len(trumpoh11)+len(bidenoh11)))*291351
print("Trump: ", (len(trumpoh11)/(len(trumpoh11)+len(bidenoh11)))-((len(bothoh11)/(len(trumpoh11)+len(bidenoh11)))/2))
print("votes ", len(trumpoh11))
print("Biden: ",(len(bidenoh11)/(len(trumpoh11)+len(bidenoh11)))-((len(bothoh11)/(len(trumpoh11)+len(bidenoh11)))/2))
print("votes ", len(bidenoh11))
print("Both: ", (len(bothoh11)/(len(trumpoh11)+len(bidenoh11))))
print("Ohio 12")
trumpoh12votes = (len(trumpoh12)/(len(trumpoh12)+len(bidenoh12)))*353425
bidenoh12votes = (len(bidenoh12)/(len(trumpoh12)+len(bidenoh12)))*353425
bothoh12 = trumpoh12.intersection(bidenoh12)
bothoh12votes = (len(bothoh12)/(len(trumpoh12)+len(bidenoh12)))*353425
print("Trump: ", (len(trumpoh12)/(len(trumpoh12)+len(bidenoh12)))-((len(bothoh12)/(len(trumpoh12)+len(bidenoh12)))/2))
print("votes ", len(trumpoh12))
print("Biden: ",(len(bidenoh12)/(len(trumpoh12)+len(bidenoh12)))-((len(bothoh12)/(len(trumpoh12)+len(bidenoh12)))/2))
print("votes ", len(bidenoh12))
print("Both: ", (len(bothoh12)/(len(trumpoh12)+len(bidenoh12))))
print("Ohio 13")
trumpoh13votes = (len(trumpoh13)/(len(trumpoh13)+len(bidenoh13)))*300742
bidenoh13votes = (len(bidenoh13)/(len(trumpoh13)+len(bidenoh13)))*300742
bothoh13 = trumpoh13.intersection(bidenoh13)
bothoh13votes = (len(bothoh13)/(len(trumpoh13)+len(bidenoh13)))*300742
print("Trump: ", (len(trumpoh13)/(len(trumpoh13)+len(bidenoh13)))-((len(bothoh13)/(len(trumpoh13)+len(bidenoh13)))/2))
print("votes ", len(trumpoh13))
print("Biden: ",(len(bidenoh13)/(len(trumpoh13)+len(bidenoh13)))-((len(bothoh13)/(len(trumpoh13)+len(bidenoh13)))/2))
print("votes ", len(bidenoh13))
print("Both: ", (len(bothoh13)/(len(trumpoh13)+len(bidenoh13))))
print("Ohio 14")
trumpoh14votes = (len(trumpoh14)/(len(trumpoh14)+len(bidenoh14)))*342165
bidenoh14votes = (len(bidenoh14)/(len(trumpoh14)+len(bidenoh14)))*342165
bothoh14 = trumpoh14.intersection(bidenoh14)
bothoh14votes = (len(bothoh14)/(len(trumpoh14)+len(bidenoh14)))*342165
print("Trump: ", (len(trumpoh14)/(len(trumpoh14)+len(bidenoh14)))-((len(bothoh14)/(len(trumpoh14)+len(bidenoh14)))/2))
print("votes ", len(trumpoh14))
print("Biden: ",(len(bidenoh14)/(len(trumpoh14)+len(bidenoh14)))-((len(bothoh14)/(len(trumpoh14)+len(bidenoh14)))/2))
print("votes ", len(bidenoh14))
print("Both: ", (len(bothoh14)/(len(trumpoh14)+len(bidenoh14))))
print("Ohio 15")
trumpoh15votes = (len(trumpoh15)/(len(trumpoh15)+len(bidenoh15)))*326458
bidenoh15votes = (len(bidenoh15)/(len(trumpoh15)+len(bidenoh15)))*326458
bothoh15 = trumpoh15.intersection(bidenoh15)
bothoh15votes = (len(bothoh15)/(len(trumpoh15)+len(bidenoh15)))*326458
print("Trump: ", (len(trumpoh15)/(len(trumpoh15)+len(bidenoh15)))-((len(bothoh15)/(len(trumpoh15)+len(bidenoh15)))/2))
print("votes ", len(trumpoh15))
print("Biden: ",(len(bidenoh15)/(len(trumpoh15)+len(bidenoh15)))-((len(bothoh15)/(len(trumpoh15)+len(bidenoh15)))/2))
print("votes ", len(bidenoh15))
print("Both: ", (len(bothoh15)/(len(trumpoh15)+len(bidenoh15))))
print("Ohio 16")
trumpoh16votes = (len(trumpoh16)/(len(trumpoh16)+len(bidenoh16)))*338791
bidenoh16votes = (len(bidenoh16)/(len(trumpoh16)+len(bidenoh16)))*338791
bothoh16 = trumpoh16.intersection(bidenoh16)
bothoh16votes = (len(bothoh16)/(len(trumpoh16)+len(bidenoh16)))*338791
print("Trump: ", (len(trumpoh16)/(len(trumpoh16)+len(bidenoh16)))-((len(bothoh16)/(len(trumpoh16)+len(bidenoh16)))/2))
print("votes ", len(trumpoh16))
print("Biden: ",(len(bidenoh16)/(len(trumpoh16)+len(bidenoh16)))-((len(bothoh16)/(len(trumpoh16)+len(bidenoh16)))/2))
print("votes ", len(bidenoh16))
print("Both: ", (len(bothoh16)/(len(trumpoh16)+len(bidenoh16))))
totalohvotestrump = trumpoh1votes+trumpoh2votes+trumpoh3votes+trumpoh4votes+trumpoh5votes+trumpoh6votes+trumpoh7votes+trumpoh8votes+trumpoh9votes+trumpoh10votes+trumpoh11votes+trumpoh12votes+trumpoh13votes+trumpoh14votes+trumpoh15votes+trumpoh16votes
totalohvotesbiden = bidenoh1votes+bidenoh2votes+bidenoh3votes+bidenoh4votes+bidenoh5votes+bidenoh6votes+bidenoh7votes+bidenoh8votes+bidenoh9votes+bidenoh10votes+bidenoh11votes+bidenoh12votes+bidenoh13votes+bidenoh14votes+bidenoh15votes+bidenoh16votes
totalohvotesboth = bothoh1votes+bothoh2votes+bothoh3votes+bothoh4votes+bothoh5votes+bothoh6votes+bothoh7votes+bothoh8votes+bothoh9votes+bothoh10votes+bothoh11votes+bothoh12votes+bothoh13votes+bothoh14votes+bothoh15votes+bothoh16votes
print("TOTAL TRUMP VOTES: ", (totalohvotestrump/(totalohvotestrump+totalohvotesbiden))-(totalohvotesboth/(totalohvotestrump+totalohvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalohvotesbiden/(totalohvotestrump+totalohvotesbiden))-(totalohvotesboth/(totalohvotestrump+totalohvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalohvotesboth/(totalohvotestrump+totalohvotesbiden)))
print("")
print("Oregon")
print("Trump: ", (len(trumpor)/(len(trumpor)+len(bidenor))))
print("Biden: ",(len(bidenor)/(len(trumpor)+len(bidenor))))
print("Oregon 1")
trumpor1votes = (len(trumpor1)/(len(trumpor1)+len(bidenor1)))*336685
bidenor1votes = (len(bidenor1)/(len(trumpor1)+len(bidenor1)))*336685
bothor1 = trumpor1.intersection(bidenor1)
bothor1votes = (len(bothor1)/(len(trumpor1)+len(bidenor1)))*336685
print("Trump: ", (len(trumpor1)/(len(trumpor1)+len(bidenor1)))-((len(bothor1)/(len(trumpor1)+len(bidenor1)))/2))
print("votes ", len(trumpor1))
print("Biden: ",(len(bidenor1)/(len(trumpor1)+len(bidenor1)))-((len(bothor1)/(len(trumpor1)+len(bidenor1)))/2))
print("votes ", len(bidenor1))
print("Both: ", (len(bothor1)/(len(trumpor1)+len(bidenor1))))
print("Oregon 2")
trumpor2votes = (len(trumpor2)/(len(trumpor2)+len(bidenor2)))*370562
bidenor2votes = (len(bidenor2)/(len(trumpor2)+len(bidenor2)))*370562
bothor2 = trumpor2.intersection(bidenor2)
bothor2votes = (len(bothor2)/(len(trumpor2)+len(bidenor2)))*370562
print("Trump: ", (len(trumpor2)/(len(trumpor2)+len(bidenor2)))-((len(bothor2)/(len(trumpor2)+len(bidenor2)))/2))
print("votes ", len(trumpor2))
print("Biden: ",(len(bidenor2)/(len(trumpor2)+len(bidenor2)))-((len(bothor2)/(len(trumpor2)+len(bidenor2)))/2))
print("votes ", len(bidenor2))
print("Both: ", (len(bothor2)/(len(trumpor2)+len(bidenor2))))
print("Oregon 3")
trumpor3votes = (len(trumpor3)/(len(trumpor3)+len(bidenor3)))*352976
bidenor3votes = (len(bidenor3)/(len(trumpor3)+len(bidenor3)))*352976
bothor3 = trumpor3.intersection(bidenor3)
bothor3votes = (len(bothor3)/(len(trumpor3)+len(bidenor3)))*352976
print("Trump: ", (len(trumpor3)/(len(trumpor3)+len(bidenor3)))-((len(bothor3)/(len(trumpor3)+len(bidenor3)))/2))
print("votes ", len(trumpor3))
print("Biden: ",(len(bidenor3)/(len(trumpor3)+len(bidenor3)))-((len(bothor3)/(len(trumpor3)+len(bidenor3)))/2))
print("votes ", len(bidenor3))
print("Both: ", (len(bothor3)/(len(trumpor3)+len(bidenor3))))
print("Oregon 4")
trumpor4votes = (len(trumpor4)/(len(trumpor4)+len(bidenor4)))*371713
bidenor4votes = (len(bidenor4)/(len(trumpor4)+len(bidenor4)))*371713
bothor4 = trumpor4.intersection(bidenor4)
bothor4votes = (len(bothor4)/(len(trumpor4)+len(bidenor4)))*371713
print("Trump: ", (len(trumpor4)/(len(trumpor4)+len(bidenor4)))-((len(bothor4)/(len(trumpor4)+len(bidenor4)))/2))
print("votes ", len(trumpor4))
print("Biden: ",(len(bidenor4)/(len(trumpor4)+len(bidenor4)))-((len(bothor4)/(len(trumpor4)+len(bidenor4)))/2))
print("votes ", len(bidenor4))
print("Both: ", (len(bothor4)/(len(trumpor4)+len(bidenor4))))
print("Oregon 5")
trumpor5votes = (len(trumpor5)/(len(trumpor5)+len(bidenor5)))*322244
bidenor5votes = (len(bidenor5)/(len(trumpor5)+len(bidenor5)))*322244
bothor5 = trumpor5.intersection(bidenor5)
bothor5votes = (len(bothor5)/(len(trumpor5)+len(bidenor5)))*322244
print("Trump: ", (len(trumpor5)/(len(trumpor5)+len(bidenor5)))-((len(bothor5)/(len(trumpor5)+len(bidenor5)))/2))
print("votes ", len(trumpor5))
print("Biden: ",(len(bidenor5)/(len(trumpor5)+len(bidenor5)))-((len(bothor5)/(len(trumpor5)+len(bidenor5)))/2))
print("votes ", len(bidenor5))
print("Both: ", (len(bothor5)/(len(trumpor5)+len(bidenor5))))
totalorvotestrump = trumpor1votes+trumpor2votes+trumpor3votes+trumpor4votes+trumpor5votes
totalorvotesbiden = bidenor1votes+bidenor2votes+bidenor3votes+bidenor4votes+bidenor5votes
totalorvotesboth = bothor1votes+bothor2votes+bothor3votes+bothor4votes+bothor5votes
print("TOTAL TRUMP VOTES: ", (totalorvotestrump/(totalorvotestrump+totalorvotesbiden))-(totalorvotesboth/(totalorvotestrump+totalorvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalorvotesbiden/(totalorvotestrump+totalorvotesbiden))-(totalorvotesboth/(totalorvotestrump+totalorvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalorvotesboth/(totalorvotestrump+totalorvotesbiden)))
print("")
print("Hawaii")
print("Trump: ", (len(trumphi)/(len(trumphi)+len(bidenhi))))
print("Biden: ",(len(bidenhi)/(len(trumphi)+len(bidenhi))))
print("Hawaii 1")
trumphi1votes = (len(trumphi1)/(len(trumphi1)+len(bidenhi1)))*173112
bidenhi1votes = (len(bidenhi1)/(len(trumphi1)+len(bidenhi1)))*173112
bothhi1 = trumphi1.intersection(bidenhi1)
bothhi1votes = (len(bothhi1)/(len(trumphi1)+len(bidenhi1)))*173112
print("Trump: ", (len(trumphi1)/(len(trumphi1)+len(bidenhi1)))-((len(bothhi1)/(len(trumphi1)+len(bidenhi1)))/2))
print("votes ", len(trumphi1))
print("Biden: ",(len(bidenhi1)/(len(trumphi1)+len(bidenhi1)))-((len(bothhi1)/(len(trumphi1)+len(bidenhi1)))/2))
print("votes ", len(bidenhi1))
print("Both: ", (len(bothhi1)/(len(trumphi1)+len(bidenhi1))))
print("Hawaii 2")
trumphi2votes = (len(trumphi2)/(len(trumphi2)+len(bidenhi2)))*210491
bidenhi2votes = (len(bidenhi2)/(len(trumphi2)+len(bidenhi2)))*210491
bothhi2 = trumphi2.intersection(bidenhi2)
bothhi2votes = (len(bothhi2)/(len(trumphi2)+len(bidenhi2)))*210491
print("Trump: ", (len(trumphi2)/(len(trumphi2)+len(bidenhi2)))-((len(bothhi2)/(len(trumphi2)+len(bidenhi2)))/2))
print("votes ", len(trumphi2))
print("Biden: ",(len(bidenhi2)/(len(trumphi2)+len(bidenhi2)))-((len(bothhi2)/(len(trumphi2)+len(bidenhi2)))/2))
print("votes ", len(bidenhi2))
print("Both: ", (len(bothhi2)/(len(trumphi2)+len(bidenhi2))))
totalhivotestrump = trumphi1votes+trumphi2votes
totalhivotesbiden = bidenhi1votes+bidenhi2votes
totalhivotesboth = bothhi1votes+bothhi2votes
print("TOTAL TRUMP VOTES: ", (totalhivotestrump/(totalhivotestrump+totalhivotesbiden))-(totalhivotesboth/(totalhivotestrump+totalhivotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalhivotesbiden/(totalhivotestrump+totalhivotesbiden))-(totalhivotesboth/(totalhivotestrump+totalhivotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalhivotesboth/(totalhivotestrump+totalhivotesbiden)))
print("")
print("Texas")
print("Trump: ", (len(trumptx)/(len(trumptx)+len(bidentx))))
print("Biden: ",(len(bidentx)/(len(trumptx)+len(bidentx))))
print("Texas 1")
trumptx1votes = (len(trumptx1)/(len(trumptx1)+len(bidentx1)))*1
bidentx1votes = (len(bidentx1)/(len(trumptx1)+len(bidentx1)))*1
bothtx1 = trumptx1.intersection(bidentx1)
bothtx1votes = (len(bothtx1)/(len(trumptx1)+len(bidentx1)))*1
print("Trump: ", (len(trumptx1)/(len(trumptx1)+len(bidentx1)))-((len(bothtx1)/(len(trumptx1)+len(bidentx1)))/2))
print("votes ", len(trumptx1))
print("Biden: ",(len(bidentx1)/(len(trumptx1)+len(bidentx1)))-((len(bothtx1)/(len(trumptx1)+len(bidentx1)))/2))
print("votes ", len(bidentx1))
print("Both: ", (len(bothtx1)/(len(trumptx1)+len(bidentx1))))
print("Texas 2")
trumptx2votes = (len(trumptx2)/(len(trumptx2)+len(bidentx2)))*1
bidentx2votes = (len(bidentx2)/(len(trumptx2)+len(bidentx2)))*1
bothtx2 = trumptx2.intersection(bidentx2)
bothtx2votes = (len(bothtx2)/(len(trumptx2)+len(bidentx2)))*1
print("Trump: ", (len(trumptx2)/(len(trumptx2)+len(bidentx2)))-((len(bothtx2)/(len(trumptx2)+len(bidentx2)))/2))
print("votes ", len(trumptx2))
print("Biden: ",(len(bidentx2)/(len(trumptx2)+len(bidentx2)))-((len(bothtx2)/(len(trumptx2)+len(bidentx2)))/2))
print("votes ", len(bidentx2))
print("Both: ", (len(bothtx2)/(len(trumptx2)+len(bidentx2))))
print("Texas 3")
trumptx3votes = (len(trumptx3)/(len(trumptx3)+len(bidentx3)))*1
bidentx3votes = (len(bidentx3)/(len(trumptx3)+len(bidentx3)))*1
bothtx3 = trumptx3.intersection(bidentx3)
bothtx3votes = (len(bothtx3)/(len(trumptx3)+len(bidentx3)))*1
print("Trump: ", (len(trumptx3)/(len(trumptx3)+len(bidentx3)))-((len(bothtx3)/(len(trumptx3)+len(bidentx3)))/2))
print("votes ", len(trumptx3))
print("Biden: ",(len(bidentx3)/(len(trumptx3)+len(bidentx3)))-((len(bothtx3)/(len(trumptx3)+len(bidentx3)))/2))
print("votes ", len(bidentx3))
print("Both: ", (len(bothtx3)/(len(trumptx3)+len(bidentx3))))
print("Texas 4")
trumptx4votes = (len(trumptx4)/(len(trumptx4)+len(bidentx4)))*1
bidentx4votes = (len(bidentx4)/(len(trumptx4)+len(bidentx4)))*1
bothtx4 = trumptx4.intersection(bidentx4)
bothtx4votes = (len(bothtx4)/(len(trumptx4)+len(bidentx4)))*1
print("Trump: ", (len(trumptx4)/(len(trumptx4)+len(bidentx4)))-((len(bothtx4)/(len(trumptx4)+len(bidentx4)))/2))
print("votes ", len(trumptx4))
print("Biden: ",(len(bidentx4)/(len(trumptx4)+len(bidentx4)))-((len(bothtx4)/(len(trumptx4)+len(bidentx4)))/2))
print("votes ", len(bidentx4))
print("Both: ", (len(bothtx4)/(len(trumptx4)+len(bidentx4))))
print("Texas 5")
trumptx5votes = (len(trumptx5)/(len(trumptx5)+len(bidentx5)))*1
bidentx5votes = (len(bidentx5)/(len(trumptx5)+len(bidentx5)))*1
bothtx5 = trumptx5.intersection(bidentx5)
bothtx5votes = (len(bothtx5)/(len(trumptx5)+len(bidentx5)))*1
print("Trump: ", (len(trumptx5)/(len(trumptx5)+len(bidentx5)))-((len(bothtx5)/(len(trumptx5)+len(bidentx5)))/2))
print("votes ", len(trumptx5))
print("Biden: ",(len(bidentx5)/(len(trumptx5)+len(bidentx5)))-((len(bothtx5)/(len(trumptx5)+len(bidentx5)))/2))
print("votes ", len(bidentx5))
print("Both: ", (len(bothtx5)/(len(trumptx5)+len(bidentx5))))
print("Texas 6")
trumptx6votes = (len(trumptx6)/(len(trumptx6)+len(bidentx6)))*1
bidentx6votes = (len(bidentx6)/(len(trumptx6)+len(bidentx6)))*1
bothtx6 = trumptx6.intersection(bidentx6)
bothtx6votes = (len(bothtx6)/(len(trumptx6)+len(bidentx6)))*1
print("Trump: ", (len(trumptx6)/(len(trumptx6)+len(bidentx6)))-((len(bothtx6)/(len(trumptx6)+len(bidentx6)))/2))
print("votes ", len(trumptx6))
print("Biden: ",(len(bidentx6)/(len(trumptx6)+len(bidentx6)))-((len(bothtx6)/(len(trumptx6)+len(bidentx6)))/2))
print("votes ", len(bidentx6))
print("Both: ", (len(bothtx6)/(len(trumptx6)+len(bidentx6))))
print("Texas 7")
trumptx7votes = (len(trumptx7)/(len(trumptx7)+len(bidentx7)))*1
bidentx7votes = (len(bidentx7)/(len(trumptx7)+len(bidentx7)))*1
bothtx7 = trumptx7.intersection(bidentx7)
bothtx7votes = (len(bothtx7)/(len(trumptx7)+len(bidentx7)))*1
print("Trump: ", (len(trumptx7)/(len(trumptx7)+len(bidentx7)))-((len(bothtx7)/(len(trumptx7)+len(bidentx7)))/2))
print("votes ", len(trumptx7))
print("Biden: ",(len(bidentx7)/(len(trumptx7)+len(bidentx7)))-((len(bothtx7)/(len(trumptx7)+len(bidentx7)))/2))
print("votes ", len(bidentx7))
print("Both: ", (len(bothtx7)/(len(trumptx7)+len(bidentx7))))
print("Texas 8")
trumptx8votes = (len(trumptx8)/(len(trumptx8)+len(bidentx8)))*1
bidentx8votes = (len(bidentx8)/(len(trumptx8)+len(bidentx8)))*1
bothtx8 = trumptx8.intersection(bidentx8)
bothtx8votes = (len(bothtx8)/(len(trumptx8)+len(bidentx8)))*1
print("Trump: ", (len(trumptx8)/(len(trumptx8)+len(bidentx8)))-((len(bothtx8)/(len(trumptx8)+len(bidentx8)))/2))
print("votes ", len(trumptx8))
print("Biden: ",(len(bidentx8)/(len(trumptx8)+len(bidentx8)))-((len(bothtx8)/(len(trumptx8)+len(bidentx8)))/2))
print("votes ", len(bidentx8))
print("Both: ", (len(bothtx8)/(len(trumptx8)+len(bidentx8))))
print("Texas 9")
trumptx9votes = (len(trumptx9)/(len(trumptx9)+len(bidentx9)))*1
bidentx9votes = (len(bidentx9)/(len(trumptx9)+len(bidentx9)))*1
bothtx9 = trumptx9.intersection(bidentx9)
bothtx9votes = (len(bothtx9)/(len(trumptx9)+len(bidentx9)))*1
print("Trump: ", (len(trumptx9)/(len(trumptx9)+len(bidentx9)))-((len(bothtx9)/(len(trumptx9)+len(bidentx9)))/2))
print("votes ", len(trumptx9))
print("Biden: ",(len(bidentx9)/(len(trumptx9)+len(bidentx9)))-((len(bothtx9)/(len(trumptx9)+len(bidentx9)))/2))
print("votes ", len(bidentx9))
print("Both: ", (len(bothtx9)/(len(trumptx9)+len(bidentx9))))
print("Texas 10")
trumptx10votes = (len(trumptx10)/(len(trumptx10)+len(bidentx10)))*1
bidentx10votes = (len(bidentx10)/(len(trumptx10)+len(bidentx10)))*1
bothtx10 = trumptx10.intersection(bidentx10)
bothtx10votes = (len(bothtx10)/(len(trumptx10)+len(bidentx10)))*1
print("Trump: ", (len(trumptx10)/(len(trumptx10)+len(bidentx10)))-((len(bothtx10)/(len(trumptx10)+len(bidentx10)))/2))
print("votes ", len(trumptx10))
print("Biden: ",(len(bidentx10)/(len(trumptx10)+len(bidentx10)))-((len(bothtx10)/(len(trumptx10)+len(bidentx10)))/2))
print("votes ", len(bidentx10))
print("Both: ", (len(bothtx10)/(len(trumptx10)+len(bidentx10))))
print("Texas 11")
trumptx11votes = (len(trumptx11)/(len(trumptx11)+len(bidentx11)))*1
bidentx11votes = (len(bidentx11)/(len(trumptx11)+len(bidentx11)))*1
bothtx11 = trumptx11.intersection(bidentx11)
bothtx11votes = (len(bothtx11)/(len(trumptx11)+len(bidentx11)))*1
print("Trump: ", (len(trumptx11)/(len(trumptx11)+len(bidentx11)))-((len(bothtx11)/(len(trumptx11)+len(bidentx11)))/2))
print("votes ", len(trumptx11))
print("Biden: ",(len(bidentx11)/(len(trumptx11)+len(bidentx11)))-((len(bothtx11)/(len(trumptx11)+len(bidentx11)))/2))
print("votes ", len(bidentx11))
print("Both: ", (len(bothtx11)/(len(trumptx11)+len(bidentx11))))
print("Texas 12")
trumptx12votes = (len(trumptx12)/(len(trumptx12)+len(bidentx12)))*1
bidentx12votes = (len(bidentx12)/(len(trumptx12)+len(bidentx12)))*1
bothtx12 = trumptx12.intersection(bidentx12)
bothtx12votes = (len(bothtx12)/(len(trumptx12)+len(bidentx12)))*1
print("Trump: ", (len(trumptx12)/(len(trumptx12)+len(bidentx12)))-((len(bothtx12)/(len(trumptx12)+len(bidentx12)))/2))
print("votes ", len(trumptx12))
print("Biden: ",(len(bidentx12)/(len(trumptx12)+len(bidentx12)))-((len(bothtx12)/(len(trumptx12)+len(bidentx12)))/2))
print("votes ", len(bidentx12))
print("Both: ", (len(bothtx12)/(len(trumptx12)+len(bidentx12))))
print("Texas 13")
trumptx13votes = (len(trumptx13)/(len(trumptx13)+len(bidentx13)))*1
bidentx13votes = (len(bidentx13)/(len(trumptx13)+len(bidentx13)))*1
bothtx13 = trumptx13.intersection(bidentx13)
bothtx13votes = (len(bothtx13)/(len(trumptx13)+len(bidentx13)))*1
print("Trump: ", (len(trumptx13)/(len(trumptx13)+len(bidentx13)))-((len(bothtx13)/(len(trumptx13)+len(bidentx13)))/2))
print("votes ", len(trumptx13))
print("Biden: ",(len(bidentx13)/(len(trumptx13)+len(bidentx13)))-((len(bothtx13)/(len(trumptx13)+len(bidentx13)))/2))
print("votes ", len(bidentx13))
print("Both: ", (len(bothtx13)/(len(trumptx13)+len(bidentx13))))
print("Texas 14")
trumptx14votes = (len(trumptx14)/(len(trumptx14)+len(bidentx14)))*1
bidentx14votes = (len(bidentx14)/(len(trumptx14)+len(bidentx14)))*1
bothtx14 = trumptx14.intersection(bidentx14)
bothtx14votes = (len(bothtx14)/(len(trumptx14)+len(bidentx14)))*1
print("Trump: ", (len(trumptx14)/(len(trumptx14)+len(bidentx14)))-((len(bothtx14)/(len(trumptx14)+len(bidentx14)))/2))
print("votes ", len(trumptx14))
print("Biden: ",(len(bidentx14)/(len(trumptx14)+len(bidentx14)))-((len(bothtx14)/(len(trumptx14)+len(bidentx14)))/2))
print("votes ", len(bidentx14))
print("Both: ", (len(bothtx14)/(len(trumptx14)+len(bidentx14))))
print("Texas 15")
trumptx15votes = (len(trumptx15)/(len(trumptx15)+len(bidentx15)))*1
bidentx15votes = (len(bidentx15)/(len(trumptx15)+len(bidentx15)))*1
bothtx15 = trumptx15.intersection(bidentx15)
bothtx15votes = (len(bothtx15)/(len(trumptx15)+len(bidentx15)))*1
print("Trump: ", (len(trumptx15)/(len(trumptx15)+len(bidentx15)))-((len(bothtx15)/(len(trumptx15)+len(bidentx15)))/2))
print("votes ", len(trumptx15))
print("Biden: ",(len(bidentx15)/(len(trumptx15)+len(bidentx15)))-((len(bothtx15)/(len(trumptx15)+len(bidentx15)))/2))
print("votes ", len(bidentx15))
print("Both: ", (len(bothtx15)/(len(trumptx15)+len(bidentx15))))
print("Texas 16")
trumptx16votes = (len(trumptx16)/(len(trumptx16)+len(bidentx16)))*1
bidentx16votes = (len(bidentx16)/(len(trumptx16)+len(bidentx16)))*1
bothtx16 = trumptx16.intersection(bidentx16)
bothtx16votes = (len(bothtx16)/(len(trumptx16)+len(bidentx16)))*1
print("Trump: ", (len(trumptx16)/(len(trumptx16)+len(bidentx16)))-((len(bothtx16)/(len(trumptx16)+len(bidentx16)))/2))
print("votes ", len(trumptx16))
print("Biden: ",(len(bidentx16)/(len(trumptx16)+len(bidentx16)))-((len(bothtx16)/(len(trumptx16)+len(bidentx16)))/2))
print("votes ", len(bidentx16))
print("Both: ", (len(bothtx16)/(len(trumptx16)+len(bidentx16))))
print("Texas 17")
trumptx17votes = (len(trumptx17)/(len(trumptx17)+len(bidentx17)))*1
bidentx17votes = (len(bidentx17)/(len(trumptx17)+len(bidentx17)))*1
bothtx17 = trumptx17.intersection(bidentx17)
bothtx17votes = (len(bothtx17)/(len(trumptx17)+len(bidentx17)))*1
print("Trump: ", (len(trumptx17)/(len(trumptx17)+len(bidentx17)))-((len(bothtx17)/(len(trumptx17)+len(bidentx17)))/2))
print("votes ", len(trumptx17))
print("Biden: ",(len(bidentx17)/(len(trumptx17)+len(bidentx17)))-((len(bothtx17)/(len(trumptx17)+len(bidentx17)))/2))
print("votes ", len(bidentx17))
print("Both: ", (len(bothtx17)/(len(trumptx17)+len(bidentx17))))
print("Texas 18")
trumptx18votes = (len(trumptx18)/(len(trumptx18)+len(bidentx18)))*1
bidentx18votes = (len(bidentx18)/(len(trumptx18)+len(bidentx18)))*1
bothtx18 = trumptx18.intersection(bidentx18)
bothtx18votes = (len(bothtx18)/(len(trumptx18)+len(bidentx18)))*1
print("Trump: ", (len(trumptx18)/(len(trumptx18)+len(bidentx18)))-((len(bothtx18)/(len(trumptx18)+len(bidentx18)))/2))
print("votes ", len(trumptx18))
print("Biden: ",(len(bidentx18)/(len(trumptx18)+len(bidentx18)))-((len(bothtx18)/(len(trumptx18)+len(bidentx18)))/2))
print("votes ", len(bidentx18))
print("Both: ", (len(bothtx18)/(len(trumptx18)+len(bidentx18))))
print("Texas 19")
trumptx19votes = (len(trumptx19)/(len(trumptx19)+len(bidentx19)))*1
bidentx19votes = (len(bidentx19)/(len(trumptx19)+len(bidentx19)))*1
bothtx19 = trumptx19.intersection(bidentx19)
bothtx19votes = (len(bothtx19)/(len(trumptx19)+len(bidentx19)))*1
print("Trump: ", (len(trumptx19)/(len(trumptx19)+len(bidentx19)))-((len(bothtx19)/(len(trumptx19)+len(bidentx19)))/2))
print("votes ", len(trumptx19))
print("Biden: ",(len(bidentx19)/(len(trumptx19)+len(bidentx19)))-((len(bothtx19)/(len(trumptx19)+len(bidentx19)))/2))
print("votes ", len(bidentx19))
print("Both: ", (len(bothtx19)/(len(trumptx19)+len(bidentx19))))
print("Texas 20")
trumptx20votes = (len(trumptx20)/(len(trumptx20)+len(bidentx20)))*1
bidentx20votes = (len(bidentx20)/(len(trumptx20)+len(bidentx20)))*1
bothtx20 = trumptx20.intersection(bidentx20)
bothtx20votes = (len(bothtx20)/(len(trumptx20)+len(bidentx20)))*1
print("Trump: ", (len(trumptx20)/(len(trumptx20)+len(bidentx20)))-((len(bothtx20)/(len(trumptx20)+len(bidentx20)))/2))
print("votes ", len(trumptx20))
print("Biden: ",(len(bidentx20)/(len(trumptx20)+len(bidentx20)))-((len(bothtx20)/(len(trumptx20)+len(bidentx20)))/2))
print("votes ", len(bidentx20))
print("Both: ", (len(bothtx20)/(len(trumptx20)+len(bidentx20))))
print("Texas 21")
trumptx21votes = (len(trumptx21)/(len(trumptx21)+len(bidentx21)))*1
bidentx21votes = (len(bidentx21)/(len(trumptx21)+len(bidentx21)))*1
bothtx21 = trumptx21.intersection(bidentx21)
bothtx21votes = (len(bothtx21)/(len(trumptx21)+len(bidentx21)))*1
print("Trump: ", (len(trumptx21)/(len(trumptx21)+len(bidentx21)))-((len(bothtx21)/(len(trumptx21)+len(bidentx21)))/2))
print("votes ", len(trumptx21))
print("Biden: ",(len(bidentx21)/(len(trumptx21)+len(bidentx21)))-((len(bothtx21)/(len(trumptx21)+len(bidentx21)))/2))
print("votes ", len(bidentx21))
print("Both: ", (len(bothtx21)/(len(trumptx21)+len(bidentx21))))
print("Texas 22")
trumptx22votes = (len(trumptx22)/(len(trumptx22)+len(bidentx22)))*1
bidentx22votes = (len(bidentx22)/(len(trumptx22)+len(bidentx22)))*1
bothtx22 = trumptx22.intersection(bidentx22)
bothtx22votes = (len(bothtx22)/(len(trumptx22)+len(bidentx22)))*1
print("Trump: ", (len(trumptx22)/(len(trumptx22)+len(bidentx22)))-((len(bothtx22)/(len(trumptx22)+len(bidentx22)))/2))
print("votes ", len(trumptx22))
print("Biden: ",(len(bidentx22)/(len(trumptx22)+len(bidentx22)))-((len(bothtx22)/(len(trumptx22)+len(bidentx22)))/2))
print("votes ", len(bidentx22))
print("Both: ", (len(bothtx22)/(len(trumptx22)+len(bidentx22))))
print("Texas 23")
trumptx23votes = (len(trumptx23)/(len(trumptx23)+len(bidentx23)))*1
bidentx23votes = (len(bidentx23)/(len(trumptx23)+len(bidentx23)))*1
bothtx23 = trumptx23.intersection(bidentx23)
bothtx23votes = (len(bothtx23)/(len(trumptx23)+len(bidentx23)))*1
print("Trump: ", (len(trumptx23)/(len(trumptx23)+len(bidentx23)))-((len(bothtx23)/(len(trumptx23)+len(bidentx23)))/2))
print("votes ", len(trumptx23))
print("Biden: ",(len(bidentx23)/(len(trumptx23)+len(bidentx23)))-((len(bothtx23)/(len(trumptx23)+len(bidentx23)))/2))
print("votes ", len(bidentx23))
print("Both: ", (len(bothtx23)/(len(trumptx23)+len(bidentx23))))
print("Texas 24")
trumptx24votes = (len(trumptx24)/(len(trumptx24)+len(bidentx24)))*1
bidentx24votes = (len(bidentx24)/(len(trumptx24)+len(bidentx24)))*1
bothtx24 = trumptx24.intersection(bidentx24)
bothtx24votes = (len(bothtx24)/(len(trumptx24)+len(bidentx24)))*1
print("Trump: ", (len(trumptx24)/(len(trumptx24)+len(bidentx24)))-((len(bothtx24)/(len(trumptx24)+len(bidentx24)))/2))
print("votes ", len(trumptx24))
print("Biden: ",(len(bidentx24)/(len(trumptx24)+len(bidentx24)))-((len(bothtx24)/(len(trumptx24)+len(bidentx24)))/2))
print("votes ", len(bidentx24))
print("Both: ", (len(bothtx24)/(len(trumptx24)+len(bidentx24))))
print("Texas 25")
trumptx25votes = (len(trumptx25)/(len(trumptx25)+len(bidentx25)))*1
bidentx25votes = (len(bidentx25)/(len(trumptx25)+len(bidentx25)))*1
bothtx25 = trumptx25.intersection(bidentx25)
bothtx25votes = (len(bothtx25)/(len(trumptx25)+len(bidentx25)))*1
print("Trump: ", (len(trumptx25)/(len(trumptx25)+len(bidentx25)))-((len(bothtx25)/(len(trumptx25)+len(bidentx25)))/2))
print("votes ", len(trumptx25))
print("Biden: ",(len(bidentx25)/(len(trumptx25)+len(bidentx25)))-((len(bothtx25)/(len(trumptx25)+len(bidentx25)))/2))
print("votes ", len(bidentx25))
print("Both: ", (len(bothtx25)/(len(trumptx25)+len(bidentx25))))
print("Texas 26")
trumptx26votes = (len(trumptx26)/(len(trumptx26)+len(bidentx26)))*1
bidentx26votes = (len(bidentx26)/(len(trumptx26)+len(bidentx26)))*1
bothtx26 = trumptx26.intersection(bidentx26)
bothtx26votes = (len(bothtx26)/(len(trumptx26)+len(bidentx26)))*1
print("Trump: ", (len(trumptx26)/(len(trumptx26)+len(bidentx26)))-((len(bothtx26)/(len(trumptx26)+len(bidentx26)))/2))
print("votes ", len(trumptx26))
print("Biden: ",(len(bidentx26)/(len(trumptx26)+len(bidentx26)))-((len(bothtx26)/(len(trumptx26)+len(bidentx26)))/2))
print("votes ", len(bidentx26))
print("Both: ", (len(bothtx26)/(len(trumptx26)+len(bidentx26))))
print("Texas 27")
trumptx27votes = (len(trumptx27)/(len(trumptx27)+len(bidentx27)))*1
bidentx27votes = (len(bidentx27)/(len(trumptx27)+len(bidentx27)))*1
bothtx27 = trumptx27.intersection(bidentx27)
bothtx27votes = (len(bothtx27)/(len(trumptx27)+len(bidentx27)))*1
print("Trump: ", (len(trumptx27)/(len(trumptx27)+len(bidentx27)))-((len(bothtx27)/(len(trumptx27)+len(bidentx27)))/2))
print("votes ", len(trumptx27))
print("Biden: ",(len(bidentx27)/(len(trumptx27)+len(bidentx27)))-((len(bothtx27)/(len(trumptx27)+len(bidentx27)))/2))
print("votes ", len(bidentx27))
print("Both: ", (len(bothtx27)/(len(trumptx27)+len(bidentx27))))
print("Texas 28")
trumptx28votes = (len(trumptx28)/(len(trumptx28)+len(bidentx28)))*1
bidentx28votes = (len(bidentx28)/(len(trumptx28)+len(bidentx28)))*1
bothtx28 = trumptx28.intersection(bidentx28)
bothtx28votes = (len(bothtx28)/(len(trumptx28)+len(bidentx28)))*1
print("Trump: ", (len(trumptx28)/(len(trumptx28)+len(bidentx28)))-((len(bothtx28)/(len(trumptx28)+len(bidentx28)))/2))
print("votes ", len(trumptx28))
print("Biden: ",(len(bidentx28)/(len(trumptx28)+len(bidentx28)))-((len(bothtx28)/(len(trumptx28)+len(bidentx28)))/2))
print("votes ", len(bidentx28))
print("Both: ", (len(bothtx28)/(len(trumptx28)+len(bidentx28))))
print("Texas 29")
trumptx29votes = (len(trumptx29)/(len(trumptx29)+len(bidentx29)))*1
bidentx29votes = (len(bidentx29)/(len(trumptx29)+len(bidentx29)))*1
bothtx29 = trumptx29.intersection(bidentx29)
bothtx29votes = (len(bothtx29)/(len(trumptx29)+len(bidentx29)))*1
print("Trump: ", (len(trumptx29)/(len(trumptx29)+len(bidentx29)))-((len(bothtx29)/(len(trumptx29)+len(bidentx29)))/2))
print("votes ", len(trumptx29))
print("Biden: ",(len(bidentx29)/(len(trumptx29)+len(bidentx29)))-((len(bothtx29)/(len(trumptx29)+len(bidentx29)))/2))
print("votes ", len(bidentx29))
print("Both: ", (len(bothtx29)/(len(trumptx29)+len(bidentx29))))
print("Texas 30")
trumptx30votes = (len(trumptx30)/(len(trumptx30)+len(bidentx30)))*1
bidentx30votes = (len(bidentx30)/(len(trumptx30)+len(bidentx30)))*1
bothtx30 = trumptx30.intersection(bidentx30)
bothtx30votes = (len(bothtx30)/(len(trumptx30)+len(bidentx30)))*1
print("Trump: ", (len(trumptx30)/(len(trumptx30)+len(bidentx30)))-((len(bothtx30)/(len(trumptx30)+len(bidentx30)))/2))
print("votes ", len(trumptx30))
print("Biden: ",(len(bidentx30)/(len(trumptx30)+len(bidentx30)))-((len(bothtx30)/(len(trumptx30)+len(bidentx30)))/2))
print("votes ", len(bidentx30))
print("Both: ", (len(bothtx30)/(len(trumptx30)+len(bidentx30))))
print("Texas 31")
trumptx31votes = (len(trumptx31)/(len(trumptx31)+len(bidentx31)))*1
bidentx31votes = (len(bidentx31)/(len(trumptx31)+len(bidentx31)))*1
bothtx31 = trumptx31.intersection(bidentx31)
bothtx31votes = (len(bothtx31)/(len(trumptx31)+len(bidentx31)))*1
print("Trump: ", (len(trumptx31)/(len(trumptx31)+len(bidentx31)))-((len(bothtx31)/(len(trumptx31)+len(bidentx31)))/2))
print("votes ", len(trumptx31))
print("Biden: ",(len(bidentx31)/(len(trumptx31)+len(bidentx31)))-((len(bothtx31)/(len(trumptx31)+len(bidentx31)))/2))
print("votes ", len(bidentx31))
print("Both: ", (len(bothtx31)/(len(trumptx31)+len(bidentx31))))
print("Texas 32")
trumptx32votes = (len(trumptx32)/(len(trumptx32)+len(bidentx32)))*1
bidentx32votes = (len(bidentx32)/(len(trumptx32)+len(bidentx32)))*1
bothtx32 = trumptx32.intersection(bidentx32)
bothtx32votes = (len(bothtx32)/(len(trumptx32)+len(bidentx32)))*1
print("Trump: ", (len(trumptx32)/(len(trumptx32)+len(bidentx32)))-((len(bothtx32)/(len(trumptx32)+len(bidentx32)))/2))
print("votes ", len(trumptx32))
print("Biden: ",(len(bidentx32)/(len(trumptx32)+len(bidentx32)))-((len(bothtx32)/(len(trumptx32)+len(bidentx32)))/2))
print("votes ", len(bidentx32))
print("Both: ", (len(bothtx32)/(len(trumptx32)+len(bidentx32))))
print("Texas 33")
trumptx33votes = (len(trumptx33)/(len(trumptx33)+len(bidentx33)))*1
bidentx33votes = (len(bidentx33)/(len(trumptx33)+len(bidentx33)))*1
bothtx33 = trumptx33.intersection(bidentx33)
bothtx33votes = (len(bothtx33)/(len(trumptx33)+len(bidentx33)))*1
print("Trump: ", (len(trumptx33)/(len(trumptx33)+len(bidentx33)))-((len(bothtx33)/(len(trumptx33)+len(bidentx33)))/2))
print("votes ", len(trumptx33))
print("Biden: ",(len(bidentx33)/(len(trumptx33)+len(bidentx33)))-((len(bothtx33)/(len(trumptx33)+len(bidentx33)))/2))
print("votes ", len(bidentx33))
print("Both: ", (len(bothtx33)/(len(trumptx33)+len(bidentx33))))
print("Texas 34")
trumptx34votes = (len(trumptx34)/(len(trumptx34)+len(bidentx34)))*1
bidentx34votes = (len(bidentx34)/(len(trumptx34)+len(bidentx34)))*1
bothtx34 = trumptx34.intersection(bidentx34)
bothtx34votes = (len(bothtx34)/(len(trumptx34)+len(bidentx34)))*1
print("Trump: ", (len(trumptx34)/(len(trumptx34)+len(bidentx34)))-((len(bothtx34)/(len(trumptx34)+len(bidentx34)))/2))
print("votes ", len(trumptx34))
print("Biden: ",(len(bidentx34)/(len(trumptx34)+len(bidentx34)))-((len(bothtx34)/(len(trumptx34)+len(bidentx34)))/2))
print("votes ", len(bidentx34))
print("Both: ", (len(bothtx34)/(len(trumptx34)+len(bidentx34))))
print("Texas 35")
trumptx35votes = (len(trumptx35)/(len(trumptx35)+len(bidentx35)))*1
bidentx35votes = (len(bidentx35)/(len(trumptx35)+len(bidentx35)))*1
bothtx35 = trumptx35.intersection(bidentx35)
bothtx35votes = (len(bothtx35)/(len(trumptx35)+len(bidentx35)))*1
print("Trump: ", (len(trumptx35)/(len(trumptx35)+len(bidentx35)))-((len(bothtx35)/(len(trumptx35)+len(bidentx35)))/2))
print("votes ", len(trumptx35))
print("Biden: ",(len(bidentx35)/(len(trumptx35)+len(bidentx35)))-((len(bothtx35)/(len(trumptx35)+len(bidentx35)))/2))
print("votes ", len(bidentx35))
print("Both: ", (len(bothtx35)/(len(trumptx35)+len(bidentx35))))
print("Texas 36")
trumptx36votes = (len(trumptx36)/(len(trumptx36)+len(bidentx36)))*1
bidentx36votes = (len(bidentx36)/(len(trumptx36)+len(bidentx36)))*1
bothtx36 = trumptx36.intersection(bidentx36)
bothtx36votes = (len(bothtx36)/(len(trumptx36)+len(bidentx36)))*1
print("Trump: ", (len(trumptx36)/(len(trumptx36)+len(bidentx36)))-((len(bothtx36)/(len(trumptx36)+len(bidentx36)))/2))
print("votes ", len(trumptx36))
print("Biden: ",(len(bidentx36)/(len(trumptx36)+len(bidentx36)))-((len(bothtx36)/(len(trumptx36)+len(bidentx36)))/2))
print("votes ", len(bidentx36))
print("Both: ", (len(bothtx36)/(len(trumptx36)+len(bidentx36))))
totaltxvotestrump = trumptx1votes+trumptx2votes+trumptx3votes+trumptx4votes+trumptx5votes+trumptx6votes+trumptx7votes+trumptx8votes+trumptx9votes+trumptx10votes+trumptx11votes+trumptx12votes+trumptx13votes+trumptx14votes+trumptx15votes+trumptx16votes+trumptx17votes+trumptx18votes+trumptx19votes+trumptx20votes+trumptx21votes+trumptx22votes+trumptx23votes+trumptx24votes+trumptx25votes+trumptx26votes+trumptx27votes+trumptx28votes+trumptx29votes+trumptx30votes+trumptx31votes+trumptx32votes+trumptx33votes+trumptx34votes+trumptx35votes+trumptx36votes
totaltxvotesbiden = bidentx1votes+bidentx2votes+bidentx3votes+bidentx4votes+bidentx5votes+bidentx6votes+bidentx7votes+bidentx8votes+bidentx9votes+bidentx10votes+bidentx11votes+bidentx12votes+bidentx13votes+bidentx14votes+bidentx15votes+bidentx16votes+bidentx17votes+bidentx18votes+bidentx19votes+bidentx20votes+bidentx21votes+bidentx22votes+bidentx23votes+bidentx24votes+bidentx25votes+bidentx26votes+bidentx27votes+bidentx28votes+bidentx29votes+bidentx30votes+bidentx31votes+bidentx32votes+bidentx33votes+bidentx34votes+bidentx35votes+bidentx36votes
totaltxvotesboth = bothtx1votes+bothtx2votes+bothtx3votes+bothtx4votes+bothtx5votes+bothtx6votes+bothtx7votes+bothtx8votes+bothtx9votes+bothtx10votes+bothtx11votes+bothtx12votes+bothtx13votes+bothtx14votes+bothtx15votes+bothtx16votes+bothtx17votes+bothtx18votes+bothtx19votes+bothtx20votes+bothtx21votes+bothtx22votes+bothtx23votes+bothtx24votes+bothtx25votes+bothtx26votes+bothtx27votes+bothtx28votes+bothtx29votes+bothtx30votes+bothtx31votes+bothtx32votes+bothtx33votes+bothtx34votes+bothtx35votes+bothtx36votes
print("TOTAL TRUMP VOTES: ", (totaltxvotestrump/(totaltxvotestrump+totaltxvotesbiden))-(totaltxvotesboth/(totaltxvotestrump+totaltxvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totaltxvotesbiden/(totaltxvotestrump+totaltxvotesbiden))-(totaltxvotesboth/(totaltxvotestrump+totaltxvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totaltxvotesboth/(totaltxvotestrump+totaltxvotesbiden)))
print("")
print("Kentucky")
print("Trump: ", (len(trumpky)/(len(trumpky)+len(bidenky))))
print("Biden: ",(len(bidenky)/(len(trumpky)+len(bidenky))))
print("Kentucky 1")
trumpky1votes = (len(trumpky1)/(len(trumpky1)+len(bidenky1)))*1
bidenky1votes = (len(bidenky1)/(len(trumpky1)+len(bidenky1)))*1
bothky1 = trumpky1.intersection(bidenky1)
bothky1votes = (len(bothky1)/(len(trumpky1)+len(bidenky1)))*1
print("Trump: ", (len(trumpky1)/(len(trumpky1)+len(bidenky1)))-((len(bothky1)/(len(trumpky1)+len(bidenky1)))/2))
print("votes ", len(trumpky1))
print("Biden: ",(len(bidenky1)/(len(trumpky1)+len(bidenky1)))-((len(bothky1)/(len(trumpky1)+len(bidenky1)))/2))
print("votes ", len(bidenky1))
print("Both: ", (len(bothky1)/(len(trumpky1)+len(bidenky1))))
print("Kentucky 2")
trumpky2votes = (len(trumpky2)/(len(trumpky2)+len(bidenky2)))*1
bidenky2votes = (len(bidenky2)/(len(trumpky2)+len(bidenky2)))*1
bothky2 = trumpky2.intersection(bidenky2)
bothky2votes = (len(bothky2)/(len(trumpky2)+len(bidenky2)))*1
print("Trump: ", (len(trumpky2)/(len(trumpky2)+len(bidenky2)))-((len(bothky2)/(len(trumpky2)+len(bidenky2)))/2))
print("votes ", len(trumpky2))
print("Biden: ",(len(bidenky2)/(len(trumpky2)+len(bidenky2)))-((len(bothky2)/(len(trumpky2)+len(bidenky2)))/2))
print("votes ", len(bidenky2))
print("Both: ", (len(bothky2)/(len(trumpky2)+len(bidenky2))))
print("Kentucky 3")
trumpky3votes = (len(trumpky3)/(len(trumpky3)+len(bidenky3)))*1
bidenky3votes = (len(bidenky3)/(len(trumpky3)+len(bidenky3)))*1
bothky3 = trumpky3.intersection(bidenky3)
bothky3votes = (len(bothky3)/(len(trumpky3)+len(bidenky3)))*1
print("Trump: ", (len(trumpky3)/(len(trumpky3)+len(bidenky3)))-((len(bothky3)/(len(trumpky3)+len(bidenky3)))/2))
print("votes ", len(trumpky3))
print("Biden: ",(len(bidenky3)/(len(trumpky3)+len(bidenky3)))-((len(bothky3)/(len(trumpky3)+len(bidenky3)))/2))
print("votes ", len(bidenky3))
print("Both: ", (len(bothky3)/(len(trumpky3)+len(bidenky3))))
print("Kentucky 4")
trumpky4votes = (len(trumpky4)/(len(trumpky4)+len(bidenky4)))*1
bidenky4votes = (len(bidenky4)/(len(trumpky4)+len(bidenky4)))*1
bothky4 = trumpky4.intersection(bidenky4)
bothky4votes = (len(bothky4)/(len(trumpky4)+len(bidenky4)))*1
print("Trump: ", (len(trumpky4)/(len(trumpky4)+len(bidenky4)))-((len(bothky4)/(len(trumpky4)+len(bidenky4)))/2))
print("votes ", len(trumpky4))
print("Biden: ",(len(bidenky4)/(len(trumpky4)+len(bidenky4)))-((len(bothky4)/(len(trumpky4)+len(bidenky4)))/2))
print("votes ", len(bidenky4))
print("Both: ", (len(bothky4)/(len(trumpky4)+len(bidenky4))))
print("Kentucky 5")
trumpky5votes = (len(trumpky5)/(len(trumpky5)+len(bidenky5)))*1
bidenky5votes = (len(bidenky5)/(len(trumpky5)+len(bidenky5)))*1
bothky5 = trumpky5.intersection(bidenky5)
bothky5votes = (len(bothky5)/(len(trumpky5)+len(bidenky5)))*1
print("Trump: ", (len(trumpky5)/(len(trumpky5)+len(bidenky5)))-((len(bothky5)/(len(trumpky5)+len(bidenky5)))/2))
print("votes ", len(trumpky5))
print("Biden: ",(len(bidenky5)/(len(trumpky5)+len(bidenky5)))-((len(bothky5)/(len(trumpky5)+len(bidenky5)))/2))
print("votes ", len(bidenky5))
print("Both: ", (len(bothky5)/(len(trumpky5)+len(bidenky5))))
print("Kentucky 6")
trumpky6votes = (len(trumpky6)/(len(trumpky6)+len(bidenky6)))*1
bidenky6votes = (len(bidenky6)/(len(trumpky6)+len(bidenky6)))*1
bothky6 = trumpky6.intersection(bidenky6)
bothky6votes = (len(bothky6)/(len(trumpky6)+len(bidenky6)))*1
print("Trump: ", (len(trumpky6)/(len(trumpky6)+len(bidenky6)))-((len(bothky6)/(len(trumpky6)+len(bidenky6)))/2))
print("votes ", len(trumpky6))
print("Biden: ",(len(bidenky6)/(len(trumpky6)+len(bidenky6)))-((len(bothky6)/(len(trumpky6)+len(bidenky6)))/2))
print("votes ", len(bidenky6))
print("Both: ", (len(bothky6)/(len(trumpky6)+len(bidenky6))))
totalkyvotestrump = trumpky1votes+trumpky2votes+trumpky3votes+trumpky4votes+trumpky5votes+trumpky6votes
totalkyvotesbiden = bidenky1votes+bidenky2votes+bidenky3votes+bidenky4votes+bidenky5votes+bidenky6votes
totalkyvotesboth = bothky1votes+bothky2votes+bothky3votes+bothky4votes+bothky5votes+bothky6votes
print("TOTAL TRUMP VOTES: ", (totalkyvotestrump/(totalkyvotestrump+totalkyvotesbiden))-(totalkyvotesboth/(totalkyvotestrump+totalkyvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalkyvotesbiden/(totalkyvotestrump+totalkyvotesbiden))-(totalkyvotesboth/(totalkyvotestrump+totalkyvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalkyvotesboth/(totalkyvotestrump+totalkyvotesbiden)))
print("")
print("Tennessee")
print("Trump: ", (len(trumptn)/(len(trumptn)+len(bidentn))))
print("Biden: ",(len(bidentn)/(len(trumptn)+len(bidentn))))
print("Tennessee 1")
trumptn1votes = (len(trumptn1)/(len(trumptn1)+len(bidentn1)))*235076
bidentn1votes = (len(bidentn1)/(len(trumptn1)+len(bidentn1)))*235076
bothtn1 = trumptn1.intersection(bidentn1)
bothtn1votes = (len(bothtn1)/(len(trumptn1)+len(bidentn1)))*235076
print("Trump: ", (len(trumptn1)/(len(trumptn1)+len(bidentn1)))-((len(bothtn1)/(len(trumptn1)+len(bidentn1)))/2))
print("votes ", len(trumptn1))
print("Biden: ",(len(bidentn1)/(len(trumptn1)+len(bidentn1)))-((len(bothtn1)/(len(trumptn1)+len(bidentn1)))/2))
print("votes ", len(bidentn1))
print("Both: ", (len(bothtn1)/(len(trumptn1)+len(bidentn1))))
print("Tennessee 2")
trumptn2votes = (len(trumptn2)/(len(trumptn2)+len(bidentn2)))*280686
bidentn2votes = (len(bidentn2)/(len(trumptn2)+len(bidentn2)))*280686
bothtn2 = trumptn2.intersection(bidentn2)
bothtn2votes = (len(bothtn2)/(len(trumptn2)+len(bidentn2)))*280686
print("Trump: ", (len(trumptn2)/(len(trumptn2)+len(bidentn2)))-((len(bothtn2)/(len(trumptn2)+len(bidentn2)))/2))
print("votes ", len(trumptn2))
print("Biden: ",(len(bidentn2)/(len(trumptn2)+len(bidentn2)))-((len(bothtn2)/(len(trumptn2)+len(bidentn2)))/2))
print("votes ", len(bidentn2))
print("Both: ", (len(bothtn2)/(len(trumptn2)+len(bidentn2))))
print("Tennessee 3")
trumptn3votes = (len(trumptn3)/(len(trumptn3)+len(bidentn3)))*253104
bidentn3votes = (len(bidentn3)/(len(trumptn3)+len(bidentn3)))*253104
bothtn3 = trumptn3.intersection(bidentn3)
bothtn3votes = (len(bothtn3)/(len(trumptn3)+len(bidentn3)))*253104
print("Trump: ", (len(trumptn3)/(len(trumptn3)+len(bidentn3)))-((len(bothtn3)/(len(trumptn3)+len(bidentn3)))/2))
print("votes ", len(trumptn3))
print("Biden: ",(len(bidentn3)/(len(trumptn3)+len(bidentn3)))-((len(bothtn3)/(len(trumptn3)+len(bidentn3)))/2))
print("votes ", len(bidentn3))
print("Both: ", (len(bothtn3)/(len(trumptn3)+len(bidentn3))))
print("Tennessee 4")
trumptn4votes = (len(trumptn4)/(len(trumptn4)+len(bidentn4)))*254612
bidentn4votes = (len(bidentn4)/(len(trumptn4)+len(bidentn4)))*254612
bothtn4 = trumptn4.intersection(bidentn4)
bothtn4votes = (len(bothtn4)/(len(trumptn4)+len(bidentn4)))*254612
print("Trump: ", (len(trumptn4)/(len(trumptn4)+len(bidentn4)))-((len(bothtn4)/(len(trumptn4)+len(bidentn4)))/2))
print("votes ", len(trumptn4))
print("Biden: ",(len(bidentn4)/(len(trumptn4)+len(bidentn4)))-((len(bothtn4)/(len(trumptn4)+len(bidentn4)))/2))
print("votes ", len(bidentn4))
print("Both: ", (len(bothtn4)/(len(trumptn4)+len(bidentn4))))
print("Tennessee 5")
trumptn5votes = (len(trumptn5)/(len(trumptn5)+len(bidentn5)))*272949
bidentn5votes = (len(bidentn5)/(len(trumptn5)+len(bidentn5)))*272949
bothtn5 = trumptn5.intersection(bidentn5)
bothtn5votes = (len(bothtn5)/(len(trumptn5)+len(bidentn5)))*272949
print("Trump: ", (len(trumptn5)/(len(trumptn5)+len(bidentn5)))-((len(bothtn5)/(len(trumptn5)+len(bidentn5)))/2))
print("votes ", len(trumptn5))
print("Biden: ",(len(bidentn5)/(len(trumptn5)+len(bidentn5)))-((len(bothtn5)/(len(trumptn5)+len(bidentn5)))/2))
print("votes ", len(bidentn5))
print("Both: ", (len(bothtn5)/(len(trumptn5)+len(bidentn5))))
print("Tennessee 6")
trumptn6votes = (len(trumptn6)/(len(trumptn6)+len(bidentn6)))*263978
bidentn6votes = (len(bidentn6)/(len(trumptn6)+len(bidentn6)))*263978
bothtn6 = trumptn6.intersection(bidentn6)
bothtn6votes = (len(bothtn6)/(len(trumptn6)+len(bidentn6)))*263978
print("Trump: ", (len(trumptn6)/(len(trumptn6)+len(bidentn6)))-((len(bothtn6)/(len(trumptn6)+len(bidentn6)))/2))
print("votes ", len(trumptn6))
print("Biden: ",(len(bidentn6)/(len(trumptn6)+len(bidentn6)))-((len(bothtn6)/(len(trumptn6)+len(bidentn6)))/2))
print("votes ", len(bidentn6))
print("Both: ", (len(bothtn6)/(len(trumptn6)+len(bidentn6))))
print("Tennessee 7")
trumptn7votes = (len(trumptn7)/(len(trumptn7)+len(bidentn7)))*263995
bidentn7votes = (len(bidentn7)/(len(trumptn7)+len(bidentn7)))*263995
bothtn7 = trumptn7.intersection(bidentn7)
bothtn7votes = (len(bothtn7)/(len(trumptn7)+len(bidentn7)))*263995
print("Trump: ", (len(trumptn7)/(len(trumptn7)+len(bidentn7)))-((len(bothtn7)/(len(trumptn7)+len(bidentn7)))/2))
print("votes ", len(trumptn7))
print("Biden: ",(len(bidentn7)/(len(trumptn7)+len(bidentn7)))-((len(bothtn7)/(len(trumptn7)+len(bidentn7)))/2))
print("votes ", len(bidentn7))
print("Both: ", (len(bothtn7)/(len(trumptn7)+len(bidentn7))))
print("Tennessee 8")
trumptn8votes = (len(trumptn8)/(len(trumptn8)+len(bidentn8)))*263779
bidentn8votes = (len(bidentn8)/(len(trumptn8)+len(bidentn8)))*263779
bothtn8 = trumptn8.intersection(bidentn8)
bothtn8votes = (len(bothtn8)/(len(trumptn8)+len(bidentn8)))*263779
print("Trump: ", (len(trumptn8)/(len(trumptn8)+len(bidentn8)))-((len(bothtn8)/(len(trumptn8)+len(bidentn8)))/2))
print("votes ", len(trumptn8))
print("Biden: ",(len(bidentn8)/(len(trumptn8)+len(bidentn8)))-((len(bothtn8)/(len(trumptn8)+len(bidentn8)))/2))
print("votes ", len(bidentn8))
print("Both: ", (len(bothtn8)/(len(trumptn8)+len(bidentn8))))
print("Tennessee 9")
trumptn9votes = (len(trumptn9)/(len(trumptn9)+len(bidentn9)))*210491
bidentn9votes = (len(bidentn9)/(len(trumptn9)+len(bidentn9)))*210491
bothtn9 = trumptn9.intersection(bidentn9)
bothtn9votes = (len(bothtn9)/(len(trumptn9)+len(bidentn9)))*210491
print("Trump: ", (len(trumptn9)/(len(trumptn9)+len(bidentn9)))-((len(bothtn9)/(len(trumptn9)+len(bidentn9)))/2))
print("votes ", len(trumptn9))
print("Biden: ",(len(bidentn9)/(len(trumptn9)+len(bidentn9)))-((len(bothtn9)/(len(trumptn9)+len(bidentn9)))/2))
print("votes ", len(bidentn9))
print("Both: ", (len(bothtn9)/(len(trumptn9)+len(bidentn9))))
totaltnvotestrump = trumptn1votes+trumptn2votes+trumptn3votes+trumptn4votes+trumptn5votes+trumptn6votes+trumptn7votes+trumptn8votes+trumptn9votes
totaltnvotesbiden = bidentn1votes+bidentn2votes+bidentn3votes+bidentn4votes+bidentn5votes+bidentn6votes+bidentn7votes+bidentn8votes+bidentn9votes
totaltnvotesboth = bothtn1votes+bothtn2votes+bothtn3votes+bothtn4votes+bothtn5votes+bothtn6votes+bothtn7votes+bothtn8votes+bothtn9votes
print("TOTAL TRUMP VOTES: ", (totaltnvotestrump/(totaltnvotestrump+totaltnvotesbiden))-(totaltnvotesboth/(totaltnvotestrump+totaltnvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totaltnvotesbiden/(totaltnvotestrump+totaltnvotesbiden))-(totaltnvotesboth/(totaltnvotestrump+totaltnvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totaltnvotesboth/(totaltnvotestrump+totaltnvotesbiden)))
print("")
print("Wisconsin")
print("Trump: ", (len(trumpwi)/(len(trumpwi)+len(bidenwi))))
print("Biden: ",(len(bidenwi)/(len(trumpwi)+len(bidenwi))))
print("Wisconsin 1")
trumpwi1votes = (len(trumpwi1)/(len(trumpwi1)+len(bidenwi1)))*1
bidenwi1votes = (len(bidenwi1)/(len(trumpwi1)+len(bidenwi1)))*1
bothwi1 = trumpwi1.intersection(bidenwi1)
bothwi1votes = (len(bothwi1)/(len(trumpwi1)+len(bidenwi1)))*1
print("Trump: ", (len(trumpwi1)/(len(trumpwi1)+len(bidenwi1)))-((len(bothwi1)/(len(trumpwi1)+len(bidenwi1)))/2))
print("votes ", len(trumpwi1))
print("Biden: ",(len(bidenwi1)/(len(trumpwi1)+len(bidenwi1)))-((len(bothwi1)/(len(trumpwi1)+len(bidenwi1)))/2))
print("votes ", len(bidenwi1))
print("Both: ", (len(bothwi1)/(len(trumpwi1)+len(bidenwi1))))
print("Wisconsin 2")
trumpwi2votes = (len(trumpwi2)/(len(trumpwi2)+len(bidenwi2)))*1
bidenwi2votes = (len(bidenwi2)/(len(trumpwi2)+len(bidenwi2)))*1
bothwi2 = trumpwi2.intersection(bidenwi2)
bothwi2votes = (len(bothwi2)/(len(trumpwi2)+len(bidenwi2)))*1
print("Trump: ", (len(trumpwi2)/(len(trumpwi2)+len(bidenwi2)))-((len(bothwi2)/(len(trumpwi2)+len(bidenwi2)))/2))
print("votes ", len(trumpwi2))
print("Biden: ",(len(bidenwi2)/(len(trumpwi2)+len(bidenwi2)))-((len(bothwi2)/(len(trumpwi2)+len(bidenwi2)))/2))
print("votes ", len(bidenwi2))
print("Both: ", (len(bothwi2)/(len(trumpwi2)+len(bidenwi2))))
print("Wisconsin 3")
trumpwi3votes = (len(trumpwi3)/(len(trumpwi3)+len(bidenwi3)))*1
bidenwi3votes = (len(bidenwi3)/(len(trumpwi3)+len(bidenwi3)))*1
bothwi3 = trumpwi3.intersection(bidenwi3)
bothwi3votes = (len(bothwi3)/(len(trumpwi3)+len(bidenwi3)))*1
print("Trump: ", (len(trumpwi3)/(len(trumpwi3)+len(bidenwi3)))-((len(bothwi3)/(len(trumpwi3)+len(bidenwi3)))/2))
print("votes ", len(trumpwi3))
print("Biden: ",(len(bidenwi3)/(len(trumpwi3)+len(bidenwi3)))-((len(bothwi3)/(len(trumpwi3)+len(bidenwi3)))/2))
print("votes ", len(bidenwi3))
print("Both: ", (len(bothwi3)/(len(trumpwi3)+len(bidenwi3))))
print("Wisconsin 4")
trumpwi4votes = (len(trumpwi4)/(len(trumpwi4)+len(bidenwi4)))*1
bidenwi4votes = (len(bidenwi4)/(len(trumpwi4)+len(bidenwi4)))*1
bothwi4 = trumpwi4.intersection(bidenwi4)
bothwi4votes = (len(bothwi4)/(len(trumpwi4)+len(bidenwi4)))*1
print("Trump: ", (len(trumpwi4)/(len(trumpwi4)+len(bidenwi4)))-((len(bothwi4)/(len(trumpwi4)+len(bidenwi4)))/2))
print("votes ", len(trumpwi4))
print("Biden: ",(len(bidenwi4)/(len(trumpwi4)+len(bidenwi4)))-((len(bothwi4)/(len(trumpwi4)+len(bidenwi4)))/2))
print("votes ", len(bidenwi4))
print("Both: ", (len(bothwi4)/(len(trumpwi4)+len(bidenwi4))))
print("Wisconsin 5")
trumpwi5votes = (len(trumpwi5)/(len(trumpwi5)+len(bidenwi5)))*1
bidenwi5votes = (len(bidenwi5)/(len(trumpwi5)+len(bidenwi5)))*1
bothwi5 = trumpwi5.intersection(bidenwi5)
bothwi5votes = (len(bothwi5)/(len(trumpwi5)+len(bidenwi5)))*1
print("Trump: ", (len(trumpwi5)/(len(trumpwi5)+len(bidenwi5)))-((len(bothwi5)/(len(trumpwi5)+len(bidenwi5)))/2))
print("votes ", len(trumpwi5))
print("Biden: ",(len(bidenwi5)/(len(trumpwi5)+len(bidenwi5)))-((len(bothwi5)/(len(trumpwi5)+len(bidenwi5)))/2))
print("votes ", len(bidenwi5))
print("Both: ", (len(bothwi5)/(len(trumpwi5)+len(bidenwi5))))
print("Wisconsin 6")
trumpwi6votes = (len(trumpwi6)/(len(trumpwi6)+len(bidenwi6)))*1
bidenwi6votes = (len(bidenwi6)/(len(trumpwi6)+len(bidenwi6)))*1
bothwi6 = trumpwi6.intersection(bidenwi6)
bothwi6votes = (len(bothwi6)/(len(trumpwi6)+len(bidenwi6)))*1
print("Trump: ", (len(trumpwi6)/(len(trumpwi6)+len(bidenwi6)))-((len(bothwi6)/(len(trumpwi6)+len(bidenwi6)))/2))
print("votes ", len(trumpwi6))
print("Biden: ",(len(bidenwi6)/(len(trumpwi6)+len(bidenwi6)))-((len(bothwi6)/(len(trumpwi6)+len(bidenwi6)))/2))
print("votes ", len(bidenwi6))
print("Both: ", (len(bothwi6)/(len(trumpwi6)+len(bidenwi6))))
print("Wisconsin 7")
trumpwi7votes = (len(trumpwi7)/(len(trumpwi7)+len(bidenwi7)))*1
bidenwi7votes = (len(bidenwi7)/(len(trumpwi7)+len(bidenwi7)))*1
bothwi7 = trumpwi7.intersection(bidenwi7)
bothwi7votes = (len(bothwi7)/(len(trumpwi7)+len(bidenwi7)))*1
print("Trump: ", (len(trumpwi7)/(len(trumpwi7)+len(bidenwi7)))-((len(bothwi7)/(len(trumpwi7)+len(bidenwi7)))/2))
print("votes ", len(trumpwi7))
print("Biden: ",(len(bidenwi7)/(len(trumpwi7)+len(bidenwi7)))-((len(bothwi7)/(len(trumpwi7)+len(bidenwi7)))/2))
print("votes ", len(bidenwi7))
print("Both: ", (len(bothwi7)/(len(trumpwi7)+len(bidenwi7))))
print("Wisconsin 8")
trumpwi8votes = (len(trumpwi8)/(len(trumpwi8)+len(bidenwi8)))*1
bidenwi8votes = (len(bidenwi8)/(len(trumpwi8)+len(bidenwi8)))*1
bothwi8 = trumpwi8.intersection(bidenwi8)
bothwi8votes = (len(bothwi8)/(len(trumpwi8)+len(bidenwi8)))*1
print("Trump: ", (len(trumpwi8)/(len(trumpwi8)+len(bidenwi8)))-((len(bothwi8)/(len(trumpwi8)+len(bidenwi8)))/2))
print("votes ", len(trumpwi8))
print("Biden: ",(len(bidenwi8)/(len(trumpwi8)+len(bidenwi8)))-((len(bothwi8)/(len(trumpwi8)+len(bidenwi8)))/2))
print("votes ", len(bidenwi8))
print("Both: ", (len(bothwi8)/(len(trumpwi8)+len(bidenwi8))))
totalwivotestrump = trumpwi1votes+trumpwi2votes+trumpwi3votes+trumpwi4votes+trumpwi5votes+trumpwi6votes+trumpwi7votes+trumpwi8votes
totalwivotesbiden = bidenwi1votes+bidenwi2votes+bidenwi3votes+bidenwi4votes+bidenwi5votes+bidenwi6votes+bidenwi7votes+bidenwi8votes
totalwivotesboth = bothwi1votes+bothwi2votes+bothwi3votes+bothwi4votes+bothwi5votes+bothwi6votes+bothwi7votes+bothwi8votes
print("TOTAL TRUMP VOTES: ", (totalwivotestrump/(totalwivotestrump+totalwivotesbiden))-(totalwivotesboth/(totalwivotestrump+totalwivotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalwivotesbiden/(totalwivotestrump+totalwivotesbiden))-(totalwivotesboth/(totalwivotestrump+totalwivotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalwivotesboth/(totalwivotestrump+totalwivotesbiden)))
print("")
print("Rhode Island")
bothri1 = trumpri1.intersection(bidenri1)
bothri1votes = (len(bothri1)/(len(trumpri1)+len(bidenri1)))*199880
bothri2 = trumpri2.intersection(bidenri2)
bothri2votes = (len(bothri2)/(len(trumpri2)+len(bidenri2)))*201886
print("Trump: ", (len(trumpri)/(len(trumpri)+len(bidenri))))
print("Biden: ",(len(bidenri)/(len(trumpri)+len(bidenri))))
print("Rhode Island 1")
bothri1 = trumpri1.intersection(bidenri1)
bothri1votes = (len(bothri1)/(len(trumpri1)+len(bidenri1)))*199880
print("Trump: ", (len(trumpri1)/(len(trumpri1)+len(bidenri1)))-((len(bothri1)/(len(trumpri1)+len(bidenri1)))/2))
print("votes ", len(trumpri1))
print("Biden: ",(len(bidenri1)/(len(trumpri1)+len(bidenri1)))-((len(bothri1)/(len(trumpri1)+len(bidenri1)))/2))
print("votes ", len(bidenri1))
print("Both: ", (len(bothri1)/(len(trumpri1)+len(bidenri1))))
trumpri1votes = (len(trumpri1)/(len(trumpri1)+len(bidenri1)))*199880
bidenri1votes = (len(bidenri1)/(len(trumpri1)+len(bidenri1)))*199880
print("Rhode Island 2")
bothri2 = trumpri2.intersection(bidenri2)
bothri2votes = (len(bothri2)/(len(trumpri2)+len(bidenri2)))*201886
print("Trump: ", (len(trumpri2)/(len(trumpri2)+len(bidenri2)))-((len(bothri2)/(len(trumpri2)+len(bidenri2)))/2))
print("votes ", len(trumpri2))
print("Biden: ",(len(bidenri2)/(len(trumpri2)+len(bidenri2)))-((len(bothri2)/(len(trumpri2)+len(bidenri2)))/2))
print("votes ", len(bidenri2))
print("Both: ", (len(bothri2)/(len(trumpri2)+len(bidenri2))))
trumpri2votes = (len(trumpri2)/(len(trumpri2)+len(bidenri2)))*201886
bidenri2votes = (len(bidenri2)/(len(trumpri2)+len(bidenri2)))*201886
totalrivotestrump = trumpri1votes+trumpri2votes
totalrivotesbiden = bidenri1votes+bidenri2votes
totalrivotesboth = bothri1votes + bothri2votes
print("TOTAL TRUMP VOTES: ", (totalrivotestrump/(totalrivotestrump+totalrivotesbiden))-(totalrivotesboth/(totalrivotestrump+totalrivotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalrivotesbiden/(totalrivotestrump+totalrivotesbiden))-(totalrivotesboth/(totalrivotestrump+totalrivotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalrivotesboth/(totalrivotestrump+totalrivotesbiden)))
print("")
print("Idaho")
print("Trump: ", (len(trumpid)/(len(trumpid)+len(bidenid))))
print("Biden: ",(len(bidenid)/(len(trumpid)+len(bidenid))))
print("Idaho 1")
trumpid1votes = (len(trumpid1)/(len(trumpid1)+len(bidenid1)))*347432
bidenid1votes = (len(bidenid1)/(len(trumpid1)+len(bidenid1)))*347432
bothid1 = trumpid1.intersection(bidenid1)
bothid1votes = (len(bothid1)/(len(trumpid1)+len(bidenid1)))*347432
print("Trump: ", (len(trumpid1)/(len(trumpid1)+len(bidenid1)))-((len(bothid1)/(len(trumpid1)+len(bidenid1)))/2))
print("votes ", len(trumpid1))
print("Biden: ",(len(bidenid1)/(len(trumpid1)+len(bidenid1)))-((len(bothid1)/(len(trumpid1)+len(bidenid1)))/2))
print("votes ", len(bidenid1))
print("Both: ", (len(bothid1)/(len(trumpid1)+len(bidenid1))))
print("Idaho 2")
trumpid2votes = (len(trumpid2)/(len(trumpid2)+len(bidenid2)))*306137
bidenid2votes = (len(bidenid2)/(len(trumpid2)+len(bidenid2)))*306137
bothid2 = trumpid2.intersection(bidenid2)
bothid2votes = (len(bothid2)/(len(trumpid2)+len(bidenid2)))*306137
print("Trump: ", (len(trumpid2)/(len(trumpid2)+len(bidenid2)))-((len(bothid2)/(len(trumpid2)+len(bidenid2)))/2))
print("votes ", len(trumpid2))
print("Biden: ",(len(bidenid2)/(len(trumpid2)+len(bidenid2)))-((len(bothid2)/(len(trumpid2)+len(bidenid2)))/2))
print("votes ", len(bidenid2))
print("Both: ", (len(bothid2)/(len(trumpid2)+len(bidenid2))))
totalidvotestrump = trumpid1votes+trumpid2votes
totalidvotesbiden = bidenid1votes+bidenid2votes
totalidvotesboth = bothid1votes+bothid2votes
print("TOTAL TRUMP VOTES: ", (totalidvotestrump/(totalidvotestrump+totalidvotesbiden))-(totalidvotesboth/(totalidvotestrump+totalidvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalidvotesbiden/(totalidvotestrump+totalidvotesbiden))-(totalidvotesboth/(totalidvotestrump+totalidvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalidvotesboth/(totalidvotestrump+totalidvotesbiden)))
print("")
print("Connecticut")
print("Trump: ", (len(trumpct)/(len(trumpct)+len(bidenct))))
print("Biden: ",(len(bidenct)/(len(trumpct)+len(bidenct))))
print("Connecticut 1")
trumpct1votes = (len(trumpct1)/(len(trumpct1)+len(bidenct1)))*297254
bidenct1votes = (len(bidenct1)/(len(trumpct1)+len(bidenct1)))*297254
bothct1 = trumpct1.intersection(bidenct1)
bothct1votes = (len(bothct1)/(len(trumpct1)+len(bidenct1)))*297254
print("Trump: ", (len(trumpct1)/(len(trumpct1)+len(bidenct1)))-((len(bothct1)/(len(trumpct1)+len(bidenct1)))/2))
print("votes ", len(trumpct1))
print("Biden: ",(len(bidenct1)/(len(trumpct1)+len(bidenct1)))-((len(bothct1)/(len(trumpct1)+len(bidenct1)))/2))
print("votes ", len(bidenct1))
print("Both: ", (len(bothct1)/(len(trumpct1)+len(bidenct1))))
print("Connecticut 2")
trumpct2votes = (len(trumpct2)/(len(trumpct2)+len(bidenct2)))*319171
bidenct2votes = (len(bidenct2)/(len(trumpct2)+len(bidenct2)))*319171
bothct2 = trumpct2.intersection(bidenct2)
bothct2votes = (len(bothct2)/(len(trumpct2)+len(bidenct2)))*319171
print("Trump: ", (len(trumpct2)/(len(trumpct2)+len(bidenct2)))-((len(bothct2)/(len(trumpct2)+len(bidenct2)))/2))
print("votes ", len(trumpct2))
print("Biden: ",(len(bidenct2)/(len(trumpct2)+len(bidenct2)))-((len(bothct2)/(len(trumpct2)+len(bidenct2)))/2))
print("votes ", len(bidenct2))
print("Both: ", (len(bothct2)/(len(trumpct2)+len(bidenct2))))
print("Connecticut 3")
trumpct3votes = (len(trumpct3)/(len(trumpct3)+len(bidenct3)))*304270
bidenct3votes = (len(bidenct3)/(len(trumpct3)+len(bidenct3)))*304270
bothct3 = trumpct3.intersection(bidenct3)
bothct3votes = (len(bothct3)/(len(trumpct3)+len(bidenct3)))*304270
print("Trump: ", (len(trumpct3)/(len(trumpct3)+len(bidenct3)))-((len(bothct3)/(len(trumpct3)+len(bidenct3)))/2))
print("votes ", len(trumpct3))
print("Biden: ",(len(bidenct3)/(len(trumpct3)+len(bidenct3)))-((len(bothct3)/(len(trumpct3)+len(bidenct3)))/2))
print("votes ", len(bidenct3))
print("Both: ", (len(bothct3)/(len(trumpct3)+len(bidenct3))))
print("Connecticut 4")
trumpct4votes = (len(trumpct4)/(len(trumpct4)+len(bidenct4)))*309558
bidenct4votes = (len(bidenct4)/(len(trumpct4)+len(bidenct4)))*309558
bothct4 = trumpct4.intersection(bidenct4)
bothct4votes = (len(bothct4)/(len(trumpct4)+len(bidenct4)))*309558
print("Trump: ", (len(trumpct4)/(len(trumpct4)+len(bidenct4)))-((len(bothct4)/(len(trumpct4)+len(bidenct4)))/2))
print("votes ", len(trumpct4))
print("Biden: ",(len(bidenct4)/(len(trumpct4)+len(bidenct4)))-((len(bothct4)/(len(trumpct4)+len(bidenct4)))/2))
print("votes ", len(bidenct4))
print("Both: ", (len(bothct4)/(len(trumpct4)+len(bidenct4))))
print("Connecticut 5")
trumpct5votes = (len(trumpct5)/(len(trumpct5)+len(bidenct5)))*301630
bidenct5votes = (len(bidenct5)/(len(trumpct5)+len(bidenct5)))*301630
bothct5 = trumpct5.intersection(bidenct5)
bothct5votes = (len(bothct5)/(len(trumpct5)+len(bidenct5)))*301630
print("Trump: ", (len(trumpct5)/(len(trumpct5)+len(bidenct5)))-((len(bothct5)/(len(trumpct5)+len(bidenct5)))/2))
print("votes ", len(trumpct5))
print("Biden: ",(len(bidenct5)/(len(trumpct5)+len(bidenct5)))-((len(bothct5)/(len(trumpct5)+len(bidenct5)))/2))
print("votes ", len(bidenct5))
print("Both: ", (len(bothct5)/(len(trumpct5)+len(bidenct5))))
totalctvotestrump = trumpct1votes+trumpct2votes+trumpct3votes+trumpct4votes+trumpct5votes
totalctvotesbiden = bidenct1votes+bidenct2votes+bidenct3votes+bidenct4votes+bidenct5votes
totalctvotesboth = bothct1votes+bothct2votes+bothct3votes+bothct4votes+bothct5votes
print("TOTAL TRUMP VOTES: ", (totalctvotestrump/(totalctvotestrump+totalctvotesbiden))-(totalctvotesboth/(totalctvotestrump+totalctvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalctvotesbiden/(totalctvotestrump+totalctvotesbiden))-(totalctvotesboth/(totalctvotestrump+totalctvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalctvotesboth/(totalctvotestrump+totalctvotesbiden)))
print("")
print("Kansas")
print("Trump: ", (len(trumpks)/(len(trumpks)+len(bidenks))))
print("Biden: ",(len(bidenks)/(len(trumpks)+len(bidenks))))
print("Kansas 1")
trumpks1votes = (len(trumpks1)/(len(trumpks1)+len(bidenks1)))*382720
bidenks1votes = (len(bidenks1)/(len(trumpks1)+len(bidenks1)))*382720
bothks1 = trumpks1.intersection(bidenks1)
bothks1votes = (len(bothks1)/(len(trumpks1)+len(bidenks1)))*382720
print("Trump: ", (len(trumpks1)/(len(trumpks1)+len(bidenks1)))-((len(bothks1)/(len(trumpks1)+len(bidenks1)))/2))
print("votes ", len(trumpks1))
print("Biden: ",(len(bidenks1)/(len(trumpks1)+len(bidenks1)))-((len(bothks1)/(len(trumpks1)+len(bidenks1)))/2))
print("votes ", len(bidenks1))
print("Both: ", (len(bothks1)/(len(trumpks1)+len(bidenks1))))
print("Kansas 2")
trumpks2votes = (len(trumpks2)/(len(trumpks2)+len(bidenks2)))*368331
bidenks2votes = (len(bidenks2)/(len(trumpks2)+len(bidenks2)))*368331
bothks2 = trumpks2.intersection(bidenks2)
bothks2votes = (len(bothks2)/(len(trumpks2)+len(bidenks2)))*368331
print("Trump: ", (len(trumpks2)/(len(trumpks2)+len(bidenks2)))-((len(bothks2)/(len(trumpks2)+len(bidenks2)))/2))
print("votes ", len(trumpks2))
print("Biden: ",(len(bidenks2)/(len(trumpks2)+len(bidenks2)))-((len(bothks2)/(len(trumpks2)+len(bidenks2)))/2))
print("votes ", len(bidenks2))
print("Both: ", (len(bothks2)/(len(trumpks2)+len(bidenks2))))
print("Kansas 3")
trumpks3votes = (len(trumpks3)/(len(trumpks3)+len(bidenks3)))*363044
bidenks3votes = (len(bidenks3)/(len(trumpks3)+len(bidenks3)))*363044
bothks3 = trumpks3.intersection(bidenks3)
bothks3votes = (len(bothks3)/(len(trumpks3)+len(bidenks3)))*363044
print("Trump: ", (len(trumpks3)/(len(trumpks3)+len(bidenks3)))-((len(bothks3)/(len(trumpks3)+len(bidenks3)))/2))
print("votes ", len(trumpks3))
print("Biden: ",(len(bidenks3)/(len(trumpks3)+len(bidenks3)))-((len(bothks3)/(len(trumpks3)+len(bidenks3)))/2))
print("votes ", len(bidenks3))
print("Both: ", (len(bothks3)/(len(trumpks3)+len(bidenks3))))
print("Kansas 4")
trumpks4votes = (len(trumpks4)/(len(trumpks4)+len(bidenks4)))*367860
bidenks4votes = (len(bidenks4)/(len(trumpks4)+len(bidenks4)))*367860
bothks4 = trumpks4.intersection(bidenks4)
bothks4votes = (len(bothks4)/(len(trumpks4)+len(bidenks4)))*367860
print("Trump: ", (len(trumpks4)/(len(trumpks4)+len(bidenks4)))-((len(bothks4)/(len(trumpks4)+len(bidenks4)))/2))
print("votes ", len(trumpks4))
print("Biden: ",(len(bidenks4)/(len(trumpks4)+len(bidenks4)))-((len(bothks4)/(len(trumpks4)+len(bidenks4)))/2))
print("votes ", len(bidenks4))
print("Both: ", (len(bothks4)/(len(trumpks4)+len(bidenks4))))
totalksvotestrump = trumpks1votes+trumpks2votes+trumpks3votes+trumpks4votes
totalksvotesbiden = bidenks1votes+bidenks2votes+bidenks3votes+bidenks4votes
totalksvotesboth = bothks1votes+bothks2votes+bothks3votes+bothks4votes
print("TOTAL TRUMP VOTES: ", (totalksvotestrump/(totalksvotestrump+totalksvotesbiden))-(totalksvotesboth/(totalksvotestrump+totalksvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalksvotesbiden/(totalksvotestrump+totalksvotesbiden))-(totalksvotesboth/(totalksvotestrump+totalksvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalksvotesboth/(totalksvotestrump+totalksvotesbiden)))

print("")
print("Utah")
print("Trump: ", (len(trumput)/(len(trumput)+len(bidenut))))
print("Biden: ",(len(bidenut)/(len(trumput)+len(bidenut))))
print("Utah 1")
trumput1votes = (len(trumput1)/(len(trumput1)+len(bidenut1)))*222509
bidenut1votes = (len(bidenut1)/(len(trumput1)+len(bidenut1)))*222509
bothut1 = trumput1.intersection(bidenut1)
bothut1votes = (len(bothut1)/(len(trumput1)+len(bidenut1)))*222509
print("Trump: ", (len(trumput1)/(len(trumput1)+len(bidenut1)))-((len(bothut1)/(len(trumput1)+len(bidenut1)))/2))
print("votes ", len(trumput1))
print("Biden: ",(len(bidenut1)/(len(trumput1)+len(bidenut1)))-((len(bothut1)/(len(trumput1)+len(bidenut1)))/2))
print("votes ", len(bidenut1))
print("Both: ", (len(bothut1)/(len(trumput1)+len(bidenut1))))
print("Utah 2")
trumput2votes = (len(trumput2)/(len(trumput2)+len(bidenut2)))*232969
bidenut2votes = (len(bidenut2)/(len(trumput2)+len(bidenut2)))*232969
bothut2 = trumput2.intersection(bidenut2)
bothut2votes = (len(bothut2)/(len(trumput2)+len(bidenut2)))*232969
print("Trump: ", (len(trumput2)/(len(trumput2)+len(bidenut2)))-((len(bothut2)/(len(trumput2)+len(bidenut2)))/2))
print("votes ", len(trumput2))
print("Biden: ",(len(bidenut2)/(len(trumput2)+len(bidenut2)))-((len(bothut2)/(len(trumput2)+len(bidenut2)))/2))
print("votes ", len(bidenut2))
print("Both: ", (len(bothut2)/(len(trumput2)+len(bidenut2))))
print("Utah 3")
trumput3votes = (len(trumput3)/(len(trumput3)+len(bidenut3)))*254847
bidenut3votes = (len(bidenut3)/(len(trumput3)+len(bidenut3)))*254847
bothut3 = trumput3.intersection(bidenut3)
bothut3votes = (len(bothut3)/(len(trumput3)+len(bidenut3)))*254847
print("Trump: ", (len(trumput3)/(len(trumput3)+len(bidenut3)))-((len(bothut3)/(len(trumput3)+len(bidenut3)))/2))
print("votes ", len(trumput3))
print("Biden: ",(len(bidenut3)/(len(trumput3)+len(bidenut3)))-((len(bothut3)/(len(trumput3)+len(bidenut3)))/2))
print("votes ", len(bidenut3))
print("Both: ", (len(bothut3)/(len(trumput3)+len(bidenut3))))
print("Utah 4")
trumput4votes = (len(trumput4)/(len(trumput4)+len(bidenut4)))*219743
bidenut4votes = (len(bidenut4)/(len(trumput4)+len(bidenut4)))*219743
bothut4 = trumput4.intersection(bidenut4)
bothut4votes = (len(bothut4)/(len(trumput4)+len(bidenut4)))*219743
print("Trump: ", (len(trumput4)/(len(trumput4)+len(bidenut4)))-((len(bothut4)/(len(trumput4)+len(bidenut4)))/2))
print("votes ", len(trumput4))
print("Biden: ",(len(bidenut4)/(len(trumput4)+len(bidenut4)))-((len(bothut4)/(len(trumput4)+len(bidenut4)))/2))
print("votes ", len(bidenut4))
print("Both: ", (len(bothut4)/(len(trumput4)+len(bidenut4))))
totalutvotestrump = trumput1votes+trumput2votes+trumput3votes+trumput4votes
totalutvotesbiden = bidenut1votes+bidenut2votes+bidenut3votes+bidenut4votes
totalutvotesboth = bothut1votes+bothut2votes+bothut3votes+bothut4votes
print("TOTAL TRUMP VOTES: ", (totalutvotestrump/(totalutvotestrump+totalutvotesbiden))-(totalutvotesboth/(totalutvotestrump+totalutvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalutvotesbiden/(totalutvotestrump+totalutvotesbiden))-(totalutvotesboth/(totalutvotestrump+totalutvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalutvotesboth/(totalutvotestrump+totalutvotesbiden)))

print("")
print("Iowa")
print("Trump: ", (len(trumpia)/(len(trumpia)+len(bidenia))))
print("Biden: ",(len(bidenia)/(len(trumpia)+len(bidenia))))
print("Iowa 1")
trumpia1votes = (len(trumpia1)/(len(trumpia1)+len(bidenia1)))*382720
bidenia1votes = (len(bidenia1)/(len(trumpia1)+len(bidenia1)))*382720
bothia1 = trumpia1.intersection(bidenia1)
bothia1votes = (len(bothia1)/(len(trumpia1)+len(bidenia1)))*382720
print("Trump: ", (len(trumpia1)/(len(trumpia1)+len(bidenia1)))-((len(bothia1)/(len(trumpia1)+len(bidenia1)))/2))
print("votes ", len(trumpia1))
print("Biden: ",(len(bidenia1)/(len(trumpia1)+len(bidenia1)))-((len(bothia1)/(len(trumpia1)+len(bidenia1)))/2))
print("votes ", len(bidenia1))
print("Both: ", (len(bothia1)/(len(trumpia1)+len(bidenia1))))
print("Iowa 2")
trumpia2votes = (len(trumpia2)/(len(trumpia2)+len(bidenia2)))*368331
bidenia2votes = (len(bidenia2)/(len(trumpia2)+len(bidenia2)))*368331
bothia2 = trumpia2.intersection(bidenia2)
bothia2votes = (len(bothia2)/(len(trumpia2)+len(bidenia2)))*368331
print("Trump: ", (len(trumpia2)/(len(trumpia2)+len(bidenia2)))-((len(bothia2)/(len(trumpia2)+len(bidenia2)))/2))
print("votes ", len(trumpia2))
print("Biden: ",(len(bidenia2)/(len(trumpia2)+len(bidenia2)))-((len(bothia2)/(len(trumpia2)+len(bidenia2)))/2))
print("votes ", len(bidenia2))
print("Both: ", (len(bothia2)/(len(trumpia2)+len(bidenia2))))
print("Iowa 3")
trumpia3votes = (len(trumpia3)/(len(trumpia3)+len(bidenia3)))*363044
bidenia3votes = (len(bidenia3)/(len(trumpia3)+len(bidenia3)))*363044
bothia3 = trumpia3.intersection(bidenia3)
bothia3votes = (len(bothia3)/(len(trumpia3)+len(bidenia3)))*363044
print("Trump: ", (len(trumpia3)/(len(trumpia3)+len(bidenia3)))-((len(bothia3)/(len(trumpia3)+len(bidenia3)))/2))
print("votes ", len(trumpia3))
print("Biden: ",(len(bidenia3)/(len(trumpia3)+len(bidenia3)))-((len(bothia3)/(len(trumpia3)+len(bidenia3)))/2))
print("votes ", len(bidenia3))
print("Both: ", (len(bothia3)/(len(trumpia3)+len(bidenia3))))
print("Iowa 4")
trumpia4votes = (len(trumpia4)/(len(trumpia4)+len(bidenia4)))*367860
bidenia4votes = (len(bidenia4)/(len(trumpia4)+len(bidenia4)))*367860
bothia4 = trumpia4.intersection(bidenia4)
bothia4votes = (len(bothia4)/(len(trumpia4)+len(bidenia4)))*367860
print("Trump: ", (len(trumpia4)/(len(trumpia4)+len(bidenia4)))-((len(bothia4)/(len(trumpia4)+len(bidenia4)))/2))
print("votes ", len(trumpia4))
print("Biden: ",(len(bidenia4)/(len(trumpia4)+len(bidenia4)))-((len(bothia4)/(len(trumpia4)+len(bidenia4)))/2))
print("votes ", len(bidenia4))
print("Both: ", (len(bothia4)/(len(trumpia4)+len(bidenia4))))
totaliavotestrump = trumpia1votes+trumpia2votes+trumpia3votes+trumpia4votes
totaliavotesbiden = bidenia1votes+bidenia2votes+bidenia3votes+bidenia4votes
totaliavotesboth = bothia1votes+bothia2votes+bothia3votes+bothia4votes
print("TOTAL TRUMP VOTES: ", (totaliavotestrump/(totaliavotestrump+totaliavotesbiden))-(totaliavotesboth/(totaliavotestrump+totaliavotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totaliavotesbiden/(totaliavotestrump+totaliavotesbiden))-(totaliavotesboth/(totaliavotestrump+totaliavotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totaliavotesboth/(totaliavotestrump+totaliavotesbiden)))
print("")
print("Illinois")
print("Trump: ", (len(trumpil)/(len(trumpil)+len(bidenil))))
print("Biden: ",(len(bidenil)/(len(trumpil)+len(bidenil))))
print("Illinois 1")
trumpil1votes = (len(trumpil1)/(len(trumpil1)+len(bidenil1)))*1
bidenil1votes = (len(bidenil1)/(len(trumpil1)+len(bidenil1)))*1
bothil1 = trumpil1.intersection(bidenil1)
bothil1votes = (len(bothil1)/(len(trumpil1)+len(bidenil1)))
print("Trump: ", (len(trumpil1)/(len(trumpil1)+len(bidenil1)))-((len(bothil1)/(len(trumpil1)+len(bidenil1)))/2))
print("votes ", len(trumpil1))
print("Biden: ",(len(bidenil1)/(len(trumpil1)+len(bidenil1)))-((len(bothil1)/(len(trumpil1)+len(bidenil1)))/2))
print("votes ", len(bidenil1))
print("Both: ", (len(bothil1)/(len(trumpil1)+len(bidenil1))))
print("Illinois 2")
trumpil2votes = (len(trumpil2)/(len(trumpil2)+len(bidenil2)))*1
bidenil2votes = (len(bidenil2)/(len(trumpil2)+len(bidenil2)))*1
bothil2 = trumpil2.intersection(bidenil2)
bothil2votes = (len(bothil2)/(len(trumpil2)+len(bidenil2)))
print("Trump: ", (len(trumpil2)/(len(trumpil2)+len(bidenil2)))-((len(bothil2)/(len(trumpil2)+len(bidenil2)))/2))
print("votes ", len(trumpil2))
print("Biden: ",(len(bidenil2)/(len(trumpil2)+len(bidenil2)))-((len(bothil2)/(len(trumpil2)+len(bidenil2)))/2))
print("votes ", len(bidenil2))
print("Both: ", (len(bothil2)/(len(trumpil2)+len(bidenil2))))
print("Illinois 3")
trumpil3votes = (len(trumpil3)/(len(trumpil3)+len(bidenil3)))*1
bidenil3votes = (len(bidenil3)/(len(trumpil3)+len(bidenil3)))*1
bothil3 = trumpil3.intersection(bidenil3)
bothil3votes = (len(bothil3)/(len(trumpil3)+len(bidenil3)))
print("Trump: ", (len(trumpil3)/(len(trumpil3)+len(bidenil3)))-((len(bothil3)/(len(trumpil3)+len(bidenil3)))/2))
print("votes ", len(trumpil3))
print("Biden: ",(len(bidenil3)/(len(trumpil3)+len(bidenil3)))-((len(bothil3)/(len(trumpil3)+len(bidenil3)))/2))
print("votes ", len(bidenil3))
print("Both: ", (len(bothil3)/(len(trumpil3)+len(bidenil3))))
print("Illinois 4")
trumpil4votes = (len(trumpil4)/(len(trumpil4)+len(bidenil4)))*1
bidenil4votes = (len(bidenil4)/(len(trumpil4)+len(bidenil4)))*1
bothil4 = trumpil4.intersection(bidenil4)
bothil4votes = (len(bothil4)/(len(trumpil4)+len(bidenil4)))
print("Trump: ", (len(trumpil4)/(len(trumpil4)+len(bidenil4)))-((len(bothil4)/(len(trumpil4)+len(bidenil4)))/2))
print("votes ", len(trumpil4))
print("Biden: ",(len(bidenil4)/(len(trumpil4)+len(bidenil4)))-((len(bothil4)/(len(trumpil4)+len(bidenil4)))/2))
print("votes ", len(bidenil4))
print("Both: ", (len(bothil4)/(len(trumpil4)+len(bidenil4))))
print("Illinois 5")
trumpil5votes = (len(trumpil5)/(len(trumpil5)+len(bidenil5)))*1
bidenil5votes = (len(bidenil5)/(len(trumpil5)+len(bidenil5)))*1
bothil5 = trumpil5.intersection(bidenil5)
bothil5votes = (len(bothil5)/(len(trumpil5)+len(bidenil5)))
print("Trump: ", (len(trumpil5)/(len(trumpil5)+len(bidenil5)))-((len(bothil5)/(len(trumpil5)+len(bidenil5)))/2))
print("votes ", len(trumpil5))
print("Biden: ",(len(bidenil5)/(len(trumpil5)+len(bidenil5)))-((len(bothil5)/(len(trumpil5)+len(bidenil5)))/2))
print("votes ", len(bidenil5))
print("Both: ", (len(bothil5)/(len(trumpil5)+len(bidenil5))))
print("Illinois 6")
trumpil6votes = (len(trumpil6)/(len(trumpil6)+len(bidenil6)))*1
bidenil6votes = (len(bidenil6)/(len(trumpil6)+len(bidenil6)))*1
bothil6 = trumpil6.intersection(bidenil6)
bothil6votes = (len(bothil6)/(len(trumpil6)+len(bidenil6)))
print("Trump: ", (len(trumpil6)/(len(trumpil6)+len(bidenil6)))-((len(bothil6)/(len(trumpil6)+len(bidenil6)))/2))
print("votes ", len(trumpil6))
print("Biden: ",(len(bidenil6)/(len(trumpil6)+len(bidenil6)))-((len(bothil6)/(len(trumpil6)+len(bidenil6)))/2))
print("votes ", len(bidenil6))
print("Both: ", (len(bothil6)/(len(trumpil6)+len(bidenil6))))
print("Illinois 7")
trumpil7votes = (len(trumpil7)/(len(trumpil7)+len(bidenil7)))*1
bidenil7votes = (len(bidenil7)/(len(trumpil7)+len(bidenil7)))*1
bothil7 = trumpil7.intersection(bidenil7)
bothil7votes = (len(bothil7)/(len(trumpil7)+len(bidenil7)))
print("Trump: ", (len(trumpil7)/(len(trumpil7)+len(bidenil7)))-((len(bothil7)/(len(trumpil7)+len(bidenil7)))/2))
print("votes ", len(trumpil7))
print("Biden: ",(len(bidenil7)/(len(trumpil7)+len(bidenil7)))-((len(bothil7)/(len(trumpil7)+len(bidenil7)))/2))
print("votes ", len(bidenil7))
print("Both: ", (len(bothil7)/(len(trumpil7)+len(bidenil7))))
print("Illinois 8")
trumpil8votes = (len(trumpil8)/(len(trumpil8)+len(bidenil8)))*1
bidenil8votes = (len(bidenil8)/(len(trumpil8)+len(bidenil8)))*1
bothil8 = trumpil8.intersection(bidenil8)
bothil8votes = (len(bothil8)/(len(trumpil8)+len(bidenil8)))
print("Trump: ", (len(trumpil8)/(len(trumpil8)+len(bidenil8)))-((len(bothil8)/(len(trumpil8)+len(bidenil8)))/2))
print("votes ", len(trumpil8))
print("Biden: ",(len(bidenil8)/(len(trumpil8)+len(bidenil8)))-((len(bothil8)/(len(trumpil8)+len(bidenil8)))/2))
print("votes ", len(bidenil8))
print("Both: ", (len(bothil8)/(len(trumpil8)+len(bidenil8))))
print("Illinois 9")
trumpil9votes = (len(trumpil9)/(len(trumpil9)+len(bidenil9)))*1
bidenil9votes = (len(bidenil9)/(len(trumpil9)+len(bidenil9)))*1
bothil9 = trumpil9.intersection(bidenil9)
bothil9votes = (len(bothil9)/(len(trumpil9)+len(bidenil9)))
print("Trump: ", (len(trumpil9)/(len(trumpil9)+len(bidenil9)))-((len(bothil9)/(len(trumpil9)+len(bidenil9)))/2))
print("votes ", len(trumpil9))
print("Biden: ",(len(bidenil9)/(len(trumpil9)+len(bidenil9)))-((len(bothil9)/(len(trumpil9)+len(bidenil9)))/2))
print("votes ", len(bidenil9))
print("Both: ", (len(bothil9)/(len(trumpil9)+len(bidenil9))))
print("Illinois 10")
trumpil10votes = (len(trumpil10)/(len(trumpil10)+len(bidenil10)))*1
bidenil10votes = (len(bidenil10)/(len(trumpil10)+len(bidenil10)))*1
bothil10 = trumpil10.intersection(bidenil10)
bothil10votes = (len(bothil10)/(len(trumpil10)+len(bidenil10)))
print("Trump: ", (len(trumpil10)/(len(trumpil10)+len(bidenil10)))-((len(bothil10)/(len(trumpil10)+len(bidenil10)))/2))
print("votes ", len(trumpil10))
print("Biden: ",(len(bidenil10)/(len(trumpil10)+len(bidenil10)))-((len(bothil10)/(len(trumpil10)+len(bidenil10)))/2))
print("votes ", len(bidenil10))
print("Both: ", (len(bothil10)/(len(trumpil10)+len(bidenil10))))
print("Illinois 11")
trumpil11votes = (len(trumpil11)/(len(trumpil11)+len(bidenil11)))*1
bidenil11votes = (len(bidenil11)/(len(trumpil11)+len(bidenil11)))*1
bothil11 = trumpil11.intersection(bidenil11)
bothil11votes = (len(bothil11)/(len(trumpil11)+len(bidenil11)))
print("Trump: ", (len(trumpil11)/(len(trumpil11)+len(bidenil11)))-((len(bothil11)/(len(trumpil11)+len(bidenil11)))/2))
print("votes ", len(trumpil11))
print("Biden: ",(len(bidenil11)/(len(trumpil11)+len(bidenil11)))-((len(bothil11)/(len(trumpil11)+len(bidenil11)))/2))
print("votes ", len(bidenil11))
print("Both: ", (len(bothil11)/(len(trumpil11)+len(bidenil11))))
print("Illinois 12")
trumpil12votes = (len(trumpil12)/(len(trumpil12)+len(bidenil12)))*1
bidenil12votes = (len(bidenil12)/(len(trumpil12)+len(bidenil12)))*1
bothil12 = trumpil12.intersection(bidenil12)
bothil12votes = (len(bothil12)/(len(trumpil12)+len(bidenil12)))
print("Trump: ", (len(trumpil12)/(len(trumpil12)+len(bidenil12)))-((len(bothil12)/(len(trumpil12)+len(bidenil12)))/2))
print("votes ", len(trumpil12))
print("Biden: ",(len(bidenil12)/(len(trumpil12)+len(bidenil12)))-((len(bothil12)/(len(trumpil12)+len(bidenil12)))/2))
print("votes ", len(bidenil12))
print("Both: ", (len(bothil12)/(len(trumpil12)+len(bidenil12))))
print("Illinois 13")
trumpil13votes = (len(trumpil13)/(len(trumpil13)+len(bidenil13)))*1
bidenil13votes = (len(bidenil13)/(len(trumpil13)+len(bidenil13)))*1
bothil13 = trumpil13.intersection(bidenil13)
bothil13votes = (len(bothil13)/(len(trumpil13)+len(bidenil13)))
print("Trump: ", (len(trumpil13)/(len(trumpil13)+len(bidenil13)))-((len(bothil13)/(len(trumpil13)+len(bidenil13)))/2))
print("votes ", len(trumpil13))
print("Biden: ",(len(bidenil13)/(len(trumpil13)+len(bidenil13)))-((len(bothil13)/(len(trumpil13)+len(bidenil13)))/2))
print("votes ", len(bidenil13))
print("Both: ", (len(bothil13)/(len(trumpil13)+len(bidenil13))))
print("Illinois 14")
trumpil14votes = (len(trumpil14)/(len(trumpil14)+len(bidenil14)))*1
bidenil14votes = (len(bidenil14)/(len(trumpil14)+len(bidenil14)))*1
bothil14 = trumpil14.intersection(bidenil14)
bothil14votes = (len(bothil14)/(len(trumpil14)+len(bidenil14)))
print("Trump: ", (len(trumpil14)/(len(trumpil14)+len(bidenil14)))-((len(bothil14)/(len(trumpil14)+len(bidenil14)))/2))
print("votes ", len(trumpil14))
print("Biden: ",(len(bidenil14)/(len(trumpil14)+len(bidenil14)))-((len(bothil14)/(len(trumpil14)+len(bidenil14)))/2))
print("votes ", len(bidenil14))
print("Both: ", (len(bothil14)/(len(trumpil14)+len(bidenil14))))
print("Illinois 15")
trumpil15votes = (len(trumpil15)/(len(trumpil15)+len(bidenil15)))*1
bidenil15votes = (len(bidenil15)/(len(trumpil15)+len(bidenil15)))*1
bothil15 = trumpil15.intersection(bidenil15)
bothil15votes = (len(bothil15)/(len(trumpil15)+len(bidenil15)))
print("Trump: ", (len(trumpil15)/(len(trumpil15)+len(bidenil15)))-((len(bothil15)/(len(trumpil15)+len(bidenil15)))/2))
print("votes ", len(trumpil15))
print("Biden: ",(len(bidenil15)/(len(trumpil15)+len(bidenil15)))-((len(bothil15)/(len(trumpil15)+len(bidenil15)))/2))
print("votes ", len(bidenil15))
print("Both: ", (len(bothil15)/(len(trumpil15)+len(bidenil15))))
print("Illinois 16")
trumpil16votes = (len(trumpil16)/(len(trumpil16)+len(bidenil16)))*1
bidenil16votes = (len(bidenil16)/(len(trumpil16)+len(bidenil16)))*1
bothil16 = trumpil16.intersection(bidenil16)
bothil16votes = (len(bothil16)/(len(trumpil16)+len(bidenil16)))
print("Trump: ", (len(trumpil16)/(len(trumpil16)+len(bidenil16)))-((len(bothil16)/(len(trumpil16)+len(bidenil16)))/2))
print("votes ", len(trumpil16))
print("Biden: ",(len(bidenil16)/(len(trumpil16)+len(bidenil16)))-((len(bothil16)/(len(trumpil16)+len(bidenil16)))/2))
print("votes ", len(bidenil16))
print("Both: ", (len(bothil16)/(len(trumpil16)+len(bidenil16))))
print("Illinois 17")
trumpil17votes = (len(trumpil17)/(len(trumpil17)+len(bidenil17)))*1
bidenil17votes = (len(bidenil17)/(len(trumpil17)+len(bidenil17)))*1
bothil17 = trumpil17.intersection(bidenil17)
bothil17votes = (len(bothil17)/(len(trumpil17)+len(bidenil17)))
print("Trump: ", (len(trumpil17)/(len(trumpil17)+len(bidenil17)))-((len(bothil17)/(len(trumpil17)+len(bidenil17)))/2))
print("votes ", len(trumpil17))
print("Biden: ",(len(bidenil17)/(len(trumpil17)+len(bidenil17)))-((len(bothil17)/(len(trumpil17)+len(bidenil17)))/2))
print("votes ", len(bidenil17))
print("Both: ", (len(bothil17)/(len(trumpil17)+len(bidenil17))))
print("Illinois 18")
trumpil18votes = (len(trumpil18)/(len(trumpil18)+len(bidenil18)))*1
bidenil18votes = (len(bidenil18)/(len(trumpil18)+len(bidenil18)))*1
bothil18 = trumpil18.intersection(bidenil18)
bothil18votes = (len(bothil18)/(len(trumpil18)+len(bidenil18)))
print("Trump: ", (len(trumpil18)/(len(trumpil18)+len(bidenil18)))-((len(bothil18)/(len(trumpil18)+len(bidenil18)))/2))
print("votes ", len(trumpil18))
print("Biden: ",(len(bidenil18)/(len(trumpil18)+len(bidenil18)))-((len(bothil18)/(len(trumpil18)+len(bidenil18)))/2))
print("votes ", len(bidenil18))
print("Both: ", (len(bothil18)/(len(trumpil18)+len(bidenil18))))
totalilvotestrump = trumpil1votes+trumpil2votes+trumpil3votes+trumpil4votes+trumpil5votes+trumpil6votes+trumpil7votes+trumpil8votes+trumpil9votes+trumpil10votes+trumpil11votes+trumpil12votes+trumpil13votes+trumpil14votes+trumpil15votes+trumpil16votes+trumpil17votes+trumpil18votes
totalilvotesbiden = bidenil1votes+bidenil2votes+bidenil3votes+bidenil4votes+bidenil5votes+bidenil6votes+bidenil7votes+bidenil8votes+bidenil9votes+bidenil10votes+bidenil11votes+bidenil12votes+bidenil13votes+bidenil14votes+bidenil15votes+bidenil16votes+bidenil17votes+bidenil18votes
totalilvotesboth = bothil1votes+bothil2votes+bothil3votes+bothil4votes+bothil5votes+bothil6votes+bothil7votes+bothil8votes+bothil9votes+bothil10votes+bothil11votes+bothil12votes+bothil13votes+bothil14votes+bothil15votes+bothil16votes+bothil17votes+bothil18votes
print("TOTAL TRUMP VOTES: ", (totalilvotestrump/(totalilvotestrump+totalilvotesbiden))-(totalilvotesboth/(totalilvotestrump+totalilvotesbiden))/2)
print("TOTAL BIDEN VOTES: ", (totalilvotesbiden/(totalilvotestrump+totalilvotesbiden))-(totalilvotesboth/(totalilvotestrump+totalilvotesbiden))/2)
print("TOTAL BOTH VOTES: ", (totalilvotesboth/(totalilvotestrump+totalilvotesbiden)))

with open("/Volumes/WINDOWS/test.txt", 'wb') as f:
	pickle.dump([trumpal1, trumpal2, trumpal3, trumpal4, trumpal5, trumpal6, trumpal7, bidenal1, bidenal2, bidenal3, bidenal4, bidenal5, bidenal6, bidenal7, trumpak1, bidenak1, trumpaz1, trumpaz2, trumpaz3, trumpaz4, trumpaz5, trumpaz6, trumpaz7, trumpaz8, trumpaz9, bidenaz1, bidenaz2, bidenaz3, bidenaz4, bidenaz5, bidenaz6, bidenaz7, bidenaz8, bidenaz9, bidenar1, bidenar2, bidenar3, bidenar4, trumpar1, trumpar2, trumpar3, trumpar4, bidenak1, trumpca1, trumpca2, trumpca3, trumpca4, trumpca5, trumpca6, trumpca7, trumpca8, trumpca9, trumpca10, trumpca11, trumpca12, trumpca13, trumpca14, trumpca15, trumpca16, trumpca17, trumpca18, trumpca19, trumpca20, trumpca21, trumpca22, trumpca23, trumpca24, trumpca25, trumpca26, trumpca27, trumpca28, trumpca29, trumpca30, trumpca31, trumpca32, trumpca33, trumpca34, trumpca35, trumpca36, trumpca37, trumpca38, trumpca39, trumpca40, trumpca41, trumpca42, trumpca43, trumpca44, trumpca45, trumpca46, trumpca47, trumpca48, trumpca49, trumpca50, trumpca51, trumpca52, trumpca53, bidenca1, bidenca2, bidenca3, bidenca4, bidenca5, bidenca6, bidenca7, bidenca8, bidenca9, bidenca10, bidenca11, bidenca12, bidenca13, bidenca14, bidenca15, bidenca16, bidenca17, bidenca18, bidenca19, bidenca20, bidenca21, bidenca22, bidenca23, bidenca24, bidenca25, bidenca26, bidenca27, bidenca28, bidenca29, bidenca30, bidenca31, bidenca32, bidenca33, bidenca34, bidenca35, bidenca36, bidenca37, bidenca38, bidenca39, bidenca40, bidenca41, bidenca42, bidenca43, bidenca44, bidenca45, bidenca46, bidenca47, bidenca48, bidenca49, bidenca50, bidenca51, bidenca52, bidenca53, trumpco1, trumpco2, trumpco3, trumpco4, trumpco5, trumpco6, trumpco7, bidenco1, bidenco2, bidenco3, bidenco4, bidenco5, bidenco6, bidenco7, bidenct1, bidenct2, bidenct3, bidenct4, bidenct5, trumpct1, trumpct2, trumpct3, trumpct4, trumpct5, trumpde1, bidende1, bidenfl1, bidenfl2, bidenfl3, bidenfl4, bidenfl5, bidenfl6, bidenfl7, bidenfl8, bidenfl9, bidenfl10, bidenfl11, bidenfl12, bidenfl13, bidenfl14, bidenfl15, bidenfl16, bidenfl17, bidenfl18, bidenfl19, bidenfl20, bidenfl21, bidenfl22, bidenfl23, bidenfl24, bidenfl25, bidenfl26, bidenfl27, trumpfl1, trumpfl2, trumpfl3, trumpfl4, trumpfl5, trumpfl6, trumpfl7, trumpfl8, trumpfl9, trumpfl10, trumpfl11, trumpfl12, trumpfl13, trumpfl14, trumpfl15, trumpfl16, trumpfl17, trumpfl18, trumpfl19, trumpfl20, trumpfl21, trumpfl22, trumpfl23, trumpfl24, trumpfl25, trumpfl26, trumpfl27, trumpga1, trumpga2, trumpga3, trumpga4, trumpga5, trumpga6, trumpga7, trumpga8, trumpga9, trumpga10, trumpga11, trumpga12, trumpga13, trumpga14, bidenga1, bidenga2, bidenga3, bidenga4, bidenga5, bidenga6, bidenga7, bidenga8, bidenga9, bidenga10, bidenga11, bidenga12, bidenga13, bidenga14, trumphi1, trumphi2, bidenhi1, bidenhi2, trumpid1, trumpid2, bidenid1, bidenid2, bidenil1, bidenil2, bidenil3, bidenil4, bidenil5, bidenil6, bidenil7, bidenil8, bidenil9, bidenil10, bidenil11, bidenil12, bidenil13, bidenil14, bidenil15, bidenil16, bidenil17, bidenil18, trumpil1, trumpil2, trumpil3, trumpil4, trumpil5, trumpil6, trumpil7, trumpil8, trumpil9, trumpil10, trumpil11, trumpil12, trumpil13, trumpil14, trumpil15, trumpil16, trumpil17, trumpil18, trumpin1, trumpin2, trumpin3, trumpin4, trumpin5, trumpin6, trumpin7, trumpin8, trumpin9, bidenin1, bidenin2, bidenin3, bidenin4, bidenin5, bidenin6, bidenin7, bidenin8, bidenin9, trumpia1, trumpia2, trumpia3, trumpia4, bidenia1, bidenia2, bidenia3, bidenia4, trumpks1, trumpks2, trumpks3, trumpks4, bidenks1, bidenks2, bidenks3, bidenks4, trumpky1, trumpky2, trumpky3, trumpky4, trumpky5, trumpky6, bidenky1, bidenky2, bidenky3, bidenky4, bidenky5, bidenky6, trumpla1, trumpla2, trumpla3, trumpla4, trumpla5, trumpla6, bidenla1, bidenla2, bidenla3, bidenla4, bidenla5, bidenla6, trumpme1, trumpme2, bidenme1, bidenme2, trumpmd1, trumpmd2, trumpmd3, trumpmd4, trumpmd5, trumpmd6, trumpmd7, trumpmd8, bidenmd1, bidenmd2, bidenmd3, bidenmd4, bidenmd5, bidenmd6, bidenmd7, bidenmd8, trumpma1, trumpma2, trumpma3, trumpma4, trumpma5, trumpma6, trumpma7, trumpma8, trumpma9, bidenma1, bidenma2, bidenma3, bidenma4, bidenma5, bidenma6, bidenma7, bidenma8, bidenma9, bidenmi1, bidenmi2, bidenmi3, bidenmi4, bidenmi5, bidenmi6, bidenmi7, bidenmi8, bidenmi9, bidenmi10, bidenmi11, bidenmi12, bidenmi13, bidenmi14, trumpmi1, trumpmi2, trumpmi3, trumpmi4, trumpmi5, trumpmi6, trumpmi7, trumpmi8, trumpmi9, trumpmi10, trumpmi11, trumpmi12, trumpmi13, trumpmi14, trumpmn1, trumpmn2, trumpmn3, trumpmn4, trumpmn5, trumpmn6, trumpmn7, trumpmn8, bidenmn1, bidenmn2, bidenmn3, bidenmn4, bidenmn5, bidenmn6, bidenmn7, bidenmn8, trumpms1, trumpms2, trumpms3, trumpms4, bidenms1, bidenms2, bidenms3, bidenms4, trumpmo1, trumpmo2, trumpmo3, trumpmo4, trumpmo5, trumpmo6, trumpmo7, trumpmo8, bidenmo1, bidenmo2, bidenmo3, bidenmo4, bidenmo5, bidenmo6, bidenmo7, bidenmo8, trumpmt1, bidenmt1, trumpne1, trumpne2, trumpne3, bidenne1, bidenne2, bidenne3, trumpnv1, trumpnv2, trumpnv3, trumpnv4, bidennv1, bidennv2, bidennv3, bidennv4, trumpnh1, trumpnh2, bidennh1, bidennh2, bidennj1, bidennj2, bidennj3, bidennj4, bidennj5, bidennj6, bidennj7, bidennj8, bidennj9, bidennj10, bidennj11, bidennj12, trumpnj1, trumpnj2, trumpnj3, trumpnj4, trumpnj5, trumpnj6, trumpnj7, trumpnj8, trumpnj9, trumpnj10, trumpnj11, trumpnj12, trumpnm1, trumpnm2, trumpnm3, bidennm1, bidennm2, bidennm3, trumpny1, trumpny2, trumpny3, trumpny4, trumpny5, trumpny6, trumpny7, trumpny8, trumpny9, trumpny10, trumpny11, trumpny12, trumpny13, trumpny14, trumpny15, trumpny16, trumpny17, trumpny18, trumpny19, trumpny20, trumpny21, trumpny22, trumpny23, trumpny24, trumpny25, trumpny26, trumpny27, bidenny1, bidenny2, bidenny3, bidenny4, bidenny5, bidenny6, bidenny7, bidenny8, bidenny9, bidenny10, bidenny11, bidenny12, bidenny13, bidenny14, bidenny15, bidenny16, bidenny17, bidenny18, bidenny19, bidenny20, bidenny21, bidenny22, bidenny23, bidenny24, bidenny25, bidenny26, bidenny27, bidennc1, bidennc2, bidennc3, bidennc4, bidennc5, bidennc6, bidennc7, bidennc8, bidennc9, bidennc10, bidennc11, bidennc12, bidennc13, trumpnc1, trumpnc2, trumpnc3, trumpnc4, trumpnc5, trumpnc6, trumpnc7, trumpnc8, trumpnc9, trumpnc10, trumpnc11, trumpnc12, trumpnc13, trumpnd1, bidennd1, bidenoh1, bidenoh2, bidenoh3, bidenoh4, bidenoh5, bidenoh6, bidenoh7, bidenoh8, bidenoh9, bidenoh10, bidenoh11, bidenoh12, bidenoh13, bidenoh14, bidenoh15, bidenoh16, trumpoh1, trumpoh2, trumpoh3, trumpoh4, trumpoh5, trumpoh6, trumpoh7, trumpoh8, trumpoh9, trumpoh10, trumpoh11, trumpoh12, trumpoh13, trumpoh14, trumpoh15, trumpoh16, trumpok1, trumpok2, trumpok3, trumpok4, trumpok5, bidenok1, bidenok2, bidenok3, bidenok4, bidenok5, trumpor1, trumpor2, trumpor3, trumpor4, trumpor5, bidenor1, bidenor2, bidenor3, bidenor4, bidenor5, bidenpa1, bidenpa2, bidenpa3, bidenpa4, bidenpa5, bidenpa6, bidenpa7, bidenpa8, bidenpa9, bidenpa10, bidenpa11, bidenpa12, bidenpa13, bidenpa14, bidenpa15, bidenpa16, bidenpa17, bidenpa18, trumppa1, trumppa2, trumppa3, trumppa4, trumppa5, trumppa6, trumppa7, trumppa8, trumppa9, trumppa10, trumppa11, trumppa12, trumppa13, trumppa14, trumppa15, trumppa16, trumppa17, trumppa18, trumpri1, trumpri2, bidenri1, bidenri2, trumpsc1, trumpsc2, trumpsc3, trumpsc4, trumpsc5, trumpsc6, trumpsc7, bidensc1, bidensc2, bidensc3, bidensc4, bidensc5, bidensc6, bidensc7, trumpsd1, bidensd1, trumptn1, trumptn2, trumptn3, trumptn4, trumptn5, trumptn6, trumptn7, trumptn8, trumptn9, bidentn1, bidentn2, bidentn3, bidentn4, bidentn5, bidentn6, bidentn7, bidentn8, bidentn9, trumptx1, trumptx2, trumptx3, trumptx4, trumptx5, trumptx6, trumptx7, trumptx8, trumptx9, trumptx10, trumptx11, trumptx12, trumptx13, trumptx14, trumptx15, trumptx16, trumptx17, trumptx18, trumptx19, trumptx20, trumptx21, trumptx22, trumptx23, trumptx24, trumptx25, trumptx26, trumptx27, trumptx28, trumptx29, trumptx30, trumptx31, trumptx32, trumptx33, trumptx34, trumptx35, trumptx36, bidentx1, bidentx2, bidentx3, bidentx4, bidentx5, bidentx6, bidentx7, bidentx8, bidentx9, bidentx10, bidentx11, bidentx12, bidentx13, bidentx14, bidentx15, bidentx16, bidentx17, bidentx18, bidentx19, bidentx20, bidentx21, bidentx22, bidentx23, bidentx24, bidentx25, bidentx26, bidentx27, bidentx28, bidentx29, bidentx30, bidentx31, bidentx32, bidentx33, bidentx34, bidentx35, bidentx36, trumput1, trumput2, trumput3, trumput4, bidenut1, bidenut2, bidenut3, bidenut4, trumpvt1, bidenvt1, bidenva1, bidenva2, bidenva3, bidenva4, bidenva5, bidenva6, bidenva7, bidenva8, bidenva9, bidenva10, bidenva11, trumpva1, trumpva2, trumpva3, trumpva4, trumpva5, trumpva6, trumpva7, trumpva8, trumpva9, trumpva10, trumpva11, bidenwa1, bidenwa2, bidenwa3, bidenwa4, bidenwa5, bidenwa6, bidenwa7, bidenwa8, bidenwa9, bidenwa10, trumpwa1, trumpwa2, trumpwa3, trumpwa4, trumpwa5, trumpwa6, trumpwa7, trumpwa8, trumpwa9, trumpwa10, trumpwv1, trumpwv2, trumpwv3, bidenwv1, bidenwv2, bidenwv3, trumpwi1, trumpwi2, trumpwi3, trumpwi4, trumpwi5, trumpwi6, trumpwi7, trumpwi8, bidenwi1, bidenwi2, bidenwi3, bidenwi4, bidenwi5, bidenwi6, bidenwi7, bidenwi8, trumpwy1, bidenwy1], f)



