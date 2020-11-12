from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from sortlocation import sortloc


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

# with open("/Volumes/TOSHIBA_BACKUP/iterate2sortlocsave.txt", 'rb') as f:
# 	trumpmo, bidenmo, trumpmo1, bidenmo1, trumpmo2, bidenmo2, trumpmo3, bidenmo3, trumpmo4, bidenmo4, trumpmo5, bidenmo5, trumpmo6, bidenmo6, trumpmo7, bidenmo7, trumpmo8, bidenmo8, trumpco, bidenco, trumpco1, bidenco1, trumpco2, bidenco2, trumpco3, bidenco3, trumpco4, bidenco4, trumpco5, bidenco5, trumpco6, bidenco6, trumpco7, bidenco7, trumpsc, bidensc, trumpsc1, bidensc1, trumpsc2, bidensc2, trumpsc3, bidensc3, trumpsc4, bidensc4, trumpsc5, bidensc5, trumpsc6, bidensc6, trumpsc7, bidensc7, trumpmn, bidenmn, trumpmn1, bidenmn1, trumpmn2, bidenmn2, trumpmn3, bidenmn3, trumpmn4, bidenmn4, trumpmn5, bidenmn5, trumpmn6, bidenmn6, trumpmn7, bidenmn7, trumpmn8, bidenmn8, trumpin, bidenin, trumpin1, bidenin1, trumpin2, bidenin2, trumpin3, bidenin3, trumpin4, bidenin4, trumpin5, bidenin5, trumpin6, bidenin6, trumpin7, bidenin7, trumpin8, bidenin8, trumpin9, bidenin9, trumpmd, bidenmd, trumpmd1, bidenmd1, trumpmd2, bidenmd2, trumpmd3, bidenmd3, trumpmd4, bidenmd4, trumpmd5, bidenmd5, trumpmd6, bidenmd6, trumpmd7, bidenmd7, trumpmd8, bidenmd8, trumpsd, bidensd, trumpsd1, bidensd1, trumpvt, bidenvt, trumpvt1, bidenvt1, trumpnd, bidennd, trumpnd1, bidennd1, trumpde, bidende, trumpde1, bidende1, trumpmt, bidenmt, trumpmt1, bidenmt1, trumpne, bidenne, trumpne1, bidenne1, trumpne2, bidenne2, trumpne3, bidenne3, trumpmi, bidenmi, trumpmi1, bidenmi1, trumpmi2, bidenmi2, trumpmi3, bidenmi3, trumpmi4, bidenmi4, trumpmi5, bidenmi5, trumpmi6, bidenmi6, trumpmi7, bidenmi7, trumpmi8, bidenmi8, trumpmi9, bidenmi9, trumpmi10, bidenmi10, trumpmi11, bidenmi11, trumpmi12, bidenmi12, trumpmi13, bidenmi13, trumpmi14, bidenmi14, trumpma, bidenma, trumpma1, bidenma1, trumpma2, bidenma2, trumpma3, bidenma3, trumpma4, bidenma4, trumpma5, bidenma5, trumpma6, bidenma6, trumpma7, bidenma7, trumpma8, bidenma8, trumpma9, bidenma9, trumpva, bidenva, trumpva1, bidenva1, trumpva2, bidenva2, trumpva3, bidenva3, trumpva4, bidenva4, trumpva5, bidenva5, trumpva6, bidenva6, trumpva7, bidenva7, trumpva8, bidenva8, trumpva9, bidenva9, trumpva10, bidenva10, trumpva11, bidenva11, trumpme, bidenme, trumpme1, bidenme1, trumpme2, bidenme2, trumpid, bidenid, trumpid1, bidenid1, trumpid2, bidenid2, trumpwi, bidenwi, trumpwi1, bidenwi1, trumpwi2, bidenwi2, trumpwi3, bidenwi3, trumpwi4, bidenwi4, trumpwi5, bidenwi5, trumpwi6, bidenwi6, trumpwi7, bidenwi7, trumpwi8, bidenwi8, trumpwv, bidenwv, trumpwv1, bidenwv1, trumpwv2, bidenwv2, trumpwv3, bidenwv3, trumpia, bidenia, trumpia1, bidenia1, trumpia2, bidenia2, trumpia3, bidenia3, trumpia4, bidenia4, trumpms, bidenms, trumpms1, bidenms1, trumpms2, bidenms2, trumpms3, bidenms3, trumpms4, bidenms4, trumphi, bidenhi, trumphi1, bidenhi1, trumphi2, bidenhi2, trumpri, bidenri, trumpri1, bidenri1, trumpri2, bidenri2, trumpwa, bidenwa, trumpwa1, bidenwa1, trumpwa2, bidenwa2, trumpwa3, bidenwa3, trumpwa4, bidenwa4, trumpwa5, bidenwa5, trumpwa6, bidenwa6, trumpwa7, bidenwa7, trumpwa8, bidenwa8, trumpwa9, bidenwa9, trumpwa10, bidenwa10, trumpfl, bidenfl, trumpfl1, bidenfl1, trumpfl2, bidenfl2, trumpfl3, bidenfl3, trumpfl4, bidenfl4, trumpfl5, bidenfl5, trumpfl6, bidenfl6, trumpfl7, bidenfl7, trumpfl8, bidenfl8, trumpfl9, bidenfl9, trumpfl10, bidenfl10, trumpfl11, bidenfl11, trumpfl12, bidenfl12, trumpfl13, bidenfl13, trumpfl14, bidenfl14, trumpfl15, bidenfl15, trumpfl16, bidenfl16, trumpfl17, bidenfl17, trumpfl18, bidenfl18, trumpfl19, bidenfl19, trumpfl20, bidenfl20, trumpfl21, bidenfl21, trumpfl22, bidenfl22, trumpfl23, bidenfl23, trumpfl24, bidenfl24, trumpfl25, bidenfl25, trumpfl26, bidenfl26, trumpfl27, bidenfl27, trumpal, bidenal, trumpal1, bidenal1, trumpal2, bidenal2, trumpal3, bidenal3, trumpal4, bidenal4, trumpal5, bidenal5, trumpal6, bidenal6, trumpal7, bidenal7, trumpil, bidenil, trumpil1, bidenil1, trumpil2, bidenil2, trumpil3, bidenil3, trumpil4, bidenil4, trumpil5, bidenil5, trumpil6, bidenil6, trumpil7, bidenil7, trumpil8, bidenil8, trumpil9, bidenil9, trumpil10, bidenil10, trumpil11, bidenil11, trumpil12, bidenil12, trumpil13, bidenil13, trumpil14, bidenil14, trumpil15, bidenil15, trumpil16, bidenil16, trumpil17, bidenil17, trumpil18, bidenil18, trumpca, bidenca, trumpca1, bidenca1, trumpca2, bidenca2, trumpca3, bidenca3, trumpca4, bidenca4, trumpca5, bidenca5, trumpca6, bidenca6, trumpca7, bidenca7, trumpca8, bidenca8, trumpca9, bidenca9, trumpca10, bidenca10, trumpca11, bidenca11, trumpca12, bidenca12, trumpca13, bidenca13, trumpca14, bidenca14, trumpca15, bidenca15, trumpca16, bidenca16, trumpca17, bidenca17, trumpca18, bidenca18, trumpca19, bidenca19, trumpca20, bidenca20, trumpca21, bidenca21, trumpca22, bidenca22, trumpca23, bidenca23, trumpca24, bidenca24, trumpca25, bidenca25, trumpca26, bidenca26, trumpca27, bidenca27, trumpca28, bidenca28, trumpca29, bidenca29, trumpca30, bidenca30, trumpca31, bidenca31, trumpca32, bidenca32, trumpca33, bidenca33, trumpca34, bidenca34, trumpca35, bidenca35, trumpca36, bidenca36, trumpca37, bidenca37, trumpca38, bidenca38, trumpca39, bidenca39, trumpca40, bidenca40, trumpca41, bidenca41, trumpca42, bidenca42, trumpca43, bidenca43, trumpca44, bidenca44, trumpca45, bidenca45, trumpca46, bidenca46, trumpca47, bidenca47, trumpca48, bidenca48, trumpca49, bidenca49, trumpca50, bidenca50, trumpca51, bidenca51, trumpca52, bidenca52, trumpca53, bidenca53, trumpks, bidenks, trumpks1, bidenks1, trumpks2, bidenks2, trumpks3, bidenks3, trumpks4, bidenks4, trumpga, bidenga, trumpga1, bidenga1, trumpga2, bidenga2, trumpga3, bidenga3, trumpga4, bidenga4, trumpga5, bidenga5, trumpga6, bidenga6, trumpga7, bidenga7, trumpga8, bidenga8, trumpga9, bidenga9, trumpga10, bidenga10, trumpga11, bidenga11, trumpga12, bidenga12, trumpga13, bidenga13, trumpga14, bidenga14, trumpaz, bidenaz, trumpaz1, bidenaz1, trumpaz2, bidenaz2, trumpaz3, bidenaz3, trumpaz4, bidenaz4, trumpaz5, bidenaz5, trumpaz6, bidenaz6, trumpaz7, bidenaz7, trumpaz8, bidenaz8, trumpaz9, bidenaz9, trumpak, bidenak, trumpak1, bidenak1, trumpar, bidenar, trumpar1, bidenar1, trumpar2, bidenar2, trumpar3, bidenar3, trumpar4, bidenar4, trumpnj, bidennj, trumpnj1, bidennj1, trumpnj2, bidennj2, trumpnj3, bidennj3, trumpnj4, bidennj4, trumpnj5, bidennj5, trumpnj6, bidennj6, trumpnj7, bidennj7, trumpnj8, bidennj8, trumpnj9, bidennj9, trumpnj10, bidennj10, trumpnj11, bidennj11, trumpnj12, bidennj12, trumpnv, bidennv, trumpnv1, bidennv1, trumpnv2, bidennv2, trumpnv3, bidennv3, trumpnv4, bidennv4, trumpnh, bidennh, trumpnh1, bidennh1, trumpnh2, bidennh2, trumpnc, bidennc, trumpnc1, bidennc1, trumpnc2, bidennc2, trumpnc3, bidennc3, trumpnc4, bidennc4, trumpnc5, bidennc5, trumpnc6, bidennc6, trumpnc7, bidennc7, trumpnc8, bidennc8, trumpnc9, bidennc9, trumpnc10, bidennc10, trumpnc11, bidennc11, trumpnc12, bidennc12, trumpnc13, bidennc13, trumptx, bidentx, trumptx1, bidentx1, trumptx2, bidentx2, trumptx3, bidentx3, trumptx4, bidentx4, trumptx5, bidentx5, trumptx6, bidentx6, trumptx7, bidentx7, trumptx8, bidentx8, trumptx9, bidentx9, trumptx10, bidentx10, trumptx11, bidentx11, trumptx12, bidentx12, trumptx13, bidentx13, trumptx14, bidentx14, trumptx15, bidentx15, trumptx16, bidentx16, trumptx17, bidentx17, trumptx18, bidentx18, trumptx19, bidentx19, trumptx20, bidentx20, trumptx21, bidentx21, trumptx22, bidentx22, trumptx23, bidentx23, trumptx24, bidentx24, trumptx25, bidentx25, trumptx26, bidentx26, trumptx27, bidentx27, trumptx28, bidentx28, trumptx29, bidentx29, trumptx30, bidentx30, trumptx31, bidentx31, trumptx32, bidentx32, trumptx33, bidentx33, trumptx34, bidentx34, trumptx35, bidentx35, trumptx36, bidentx36, trumptn, bidentn, trumptn1, bidentn1, trumptn2, bidentn2, trumptn3, bidentn3, trumptn4, bidentn4, trumptn5, bidentn5, trumptn6, bidentn6, trumptn7, bidentn7, trumptn8, bidentn8, trumptn9, bidentn9, trumpnm, bidennm, trumpnm1, bidennm1, trumpnm2, bidennm2, trumpnm3, bidennm3, trumpny, bidenny, trumpny1, bidenny1, trumpny2, bidenny2, trumpny3, bidenny3, trumpny4, bidenny4, trumpny5, bidenny5, trumpny6, bidenny6, trumpny7, bidenny7, trumpny8, bidenny8, trumpny9, bidenny9, trumpny10, bidenny10, trumpny11, bidenny11, trumpny12, bidenny12, trumpny13, bidenny13, trumpny14, bidenny14, trumpny15, bidenny15, trumpny16, bidenny16, trumpny17, bidenny17, trumpny18, bidenny18, trumpny19, bidenny19, trumpny20, bidenny20, trumpny21, bidenny21, trumpny22, bidenny22, trumpny23, bidenny23, trumpny24, bidenny24, trumpny25, bidenny25, trumpny26, bidenny26, trumpny27, bidenny27, trumpwy, bidenwy, trumpwy1, bidenwy1, trumppa, bidenpa, trumppa1, bidenpa1, trumppa2, bidenpa2, trumppa3, bidenpa3, trumppa4, bidenpa4, trumppa5, bidenpa5, trumppa6, bidenpa6, trumppa7, bidenpa7, trumppa8, bidenpa8, trumppa9, bidenpa9, trumppa10, bidenpa10, trumppa11, bidenpa11, trumppa12, bidenpa12, trumppa13, bidenpa13, trumppa14, bidenpa14, trumppa15, bidenpa15, trumppa16, bidenpa16, trumppa17, bidenpa17, trumppa18, bidenpa18, trumpct, bidenct, trumpct1, bidenct1, trumpct2, bidenct2, trumpct3, bidenct3, trumpct4, bidenct4, trumpct5, bidenct5, trumpky, bidenky, trumpky1, bidenky1, trumpky2, bidenky2, trumpky3, bidenky3, trumpky4, bidenky4, trumpky5, bidenky5, trumpky6, bidenky6, trumpla, bidenla, trumpla1, bidenla1, trumpla2, bidenla2, trumpla3, bidenla3, trumpla4, bidenla4, trumpla5, bidenla5, trumpla6, bidenla6, trumpok, bidenok, trumpok1, bidenok1, trumpok2, bidenok2, trumpok3, bidenok3, trumpok4, bidenok4, trumpok5, bidenok5, trumput, bidenut, trumput1, bidenut1, trumput2, bidenut2, trumput3, bidenut3, trumput4, bidenut4, trumpoh, bidenoh, trumpoh1, bidenoh1, trumpoh2, bidenoh2, trumpoh3, bidenoh3, trumpoh4, bidenoh4, trumpoh5, bidenoh5, trumpoh6, bidenoh6, trumpoh7, bidenoh7, trumpoh8, bidenoh8, trumpoh9, bidenoh9, trumpoh10, bidenoh10, trumpoh11, bidenoh11, trumpoh12, bidenoh12, trumpoh13, bidenoh13, trumpoh14, bidenoh14, trumpoh15, bidenoh15, trumpoh16, bidenoh16, trumpor, bidenor, trumpor1, bidenor1, trumpor2, bidenor2, trumpor3, bidenor3, trumpor4, bidenor4, trumpor5, bidenor5 = pickle.load(f)


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
#trumpmo1.add(tw["user"]["id"])
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
    district = sortloc(["#trump2020", "#votered"], tw["user"]["location"], tw["retweeted_status"]["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            trumpmo1.add(tw["user"]["id"])
        if("mo2" in district):
            trumpmo2.add(tw["user"]["id"])
        if("mo3" in district):
            trumpmo3.add(tw["user"]["id"])
        if("mo4" in district):
            trumpmo4.add(tw["user"]["id"])
        if("mo5" in district):
            trumpmo5.add(tw["user"]["id"])
        if("mo6" in district):
            trumpmo6.add(tw["user"]["id"])
        if("mo7" in district):
            trumpmo7.add(tw["user"]["id"])
        if("mo8" in district):
            trumpmo8.add(tw["user"]["id"])
        if("sc1" in district):
            trumpsc1.add(tw["user"]["id"])
        if("sc2" in district):
            trumpsc2.add(tw["user"]["id"])
        if("sc3" in district):
            trumpsc3.add(tw["user"]["id"])
        if("sc4" in district):
            trumpsc4.add(tw["user"]["id"])
        if("sc5" in district):
            trumpsc5.add(tw["user"]["id"])
        if("sc6" in district):
            trumpsc6.add(tw["user"]["id"])
        if("sc7" in district):
            trumpsc7.add(tw["user"]["id"])
        if("ky1" in district):
            trumpky1.add(tw["user"]["id"])
        if("ky2" in district):
            trumpky2.add(tw["user"]["id"])
        if("ky3" in district):
            trumpky3.add(tw["user"]["id"])
        if("ky4" in district):
            trumpky4.add(tw["user"]["id"])
        if("ky5" in district):
            trumpky5.add(tw["user"]["id"])
        if("ky6" in district):
            trumpky6.add(tw["user"]["id"])
        if("ok1" in district):
            trumpok1.add(tw["user"]["id"])
        if("ok2" in district):
            trumpok2.add(tw["user"]["id"])
        if("ok3" in district):
            trumpok3.add(tw["user"]["id"])
        if("ok4" in district):
            trumpok4.add(tw["user"]["id"])
        if("ok5" in district):
            trumpok5.add(tw["user"]["id"])
        if("ia1" in district):
            trumpia1.add(tw["user"]["id"])
        if("ia2" in district):
            trumpia2.add(tw["user"]["id"])
        if("ia3" in district):
            trumpia3.add(tw["user"]["id"])
        if("ia4" in district):
            trumpia4.add(tw["user"]["id"])
        if("ks1" in district):
            trumpks1.add(tw["user"]["id"])
        if("ks2" in district):
            trumpks2.add(tw["user"]["id"])
        if("ks3" in district):
            trumpks3.add(tw["user"]["id"])
        if("ks4" in district):
            trumpks4.add(tw["user"]["id"])
        if("ca1" in district):
            trumpca1.add(tw["user"]["id"])
        if("ca2" in district):
            trumpca2.add(tw["user"]["id"])
        if("ca3" in district):
            trumpca3.add(tw["user"]["id"])
        if("ca4" in district):
            trumpca4.add(tw["user"]["id"])
        if("ca5" in district):
            trumpca5.add(tw["user"]["id"])
        if("ca6" in district):
            trumpca6.add(tw["user"]["id"])
        if("ca7" in district):
            trumpca7.add(tw["user"]["id"])
        if("ca8" in district):
            trumpca8.add(tw["user"]["id"])
        if("ca9" in district):
            trumpca9.add(tw["user"]["id"])
        if("ca10" in district):
            trumpca10.add(tw["user"]["id"])
        if("ca11" in district):
            trumpca11.add(tw["user"]["id"])
        if("ca12" in district):
            trumpca12.add(tw["user"]["id"])
        if("ca13" in district):
            trumpca13.add(tw["user"]["id"])
        if("ca14" in district):
            trumpca14.add(tw["user"]["id"])
        if("ca15" in district):
            trumpca15.add(tw["user"]["id"])
        if("ca16" in district):
            trumpca16.add(tw["user"]["id"])
        if("ca17" in district):
            trumpca17.add(tw["user"]["id"])
        if("ca18" in district):
            trumpca18.add(tw["user"]["id"])
        if("ca19" in district):
            trumpca19.add(tw["user"]["id"])
        if("ca20" in district):
            trumpca20.add(tw["user"]["id"])
        if("ca21" in district):
            trumpca21.add(tw["user"]["id"])
        if("ca22" in district):
            trumpca22.add(tw["user"]["id"])
        if("ca23" in district):
            trumpca23.add(tw["user"]["id"])
        if("ca24" in district):
            trumpca24.add(tw["user"]["id"])
        if("ca25" in district):
            trumpca25.add(tw["user"]["id"])
        if("ca26" in district):
            trumpca26.add(tw["user"]["id"])
        if("ca27" in district):
            trumpca27.add(tw["user"]["id"])
        if("ca28" in district):
            trumpca28.add(tw["user"]["id"])
        if("ca29" in district):
            trumpca29.add(tw["user"]["id"])
        if("ca30" in district):
            trumpca30.add(tw["user"]["id"])
        if("ca31" in district):
            trumpca31.add(tw["user"]["id"])
        if("ca32" in district):
            trumpca32.add(tw["user"]["id"])
        if("ca33" in district):
            trumpca33.add(tw["user"]["id"])
        if("ca34" in district):
            trumpca34.add(tw["user"]["id"])
        if("ca35" in district):
            trumpca35.add(tw["user"]["id"])
        if("ca36" in district):
            trumpca36.add(tw["user"]["id"])
        if("ca37" in district):
            trumpca37.add(tw["user"]["id"])
        if("ca38" in district):
            trumpca38.add(tw["user"]["id"])
        if("ca39" in district):
            trumpca39.add(tw["user"]["id"])
        if("ca40" in district):
            trumpca40.add(tw["user"]["id"])
        if("ca41" in district):
            trumpca41.add(tw["user"]["id"])
        if("ca42" in district):
            trumpca42.add(tw["user"]["id"])
        if("ca43" in district):
            trumpca43.add(tw["user"]["id"])
        if("ca44" in district):
            trumpca44.add(tw["user"]["id"])
        if("ca45" in district):
            trumpca45.add(tw["user"]["id"])
        if("ca46" in district):
            trumpca46.add(tw["user"]["id"])
        if("ca47" in district):
            trumpca47.add(tw["user"]["id"])
        if("ca48" in district):
            trumpca48.add(tw["user"]["id"])
        if("ca49" in district):
            trumpca49.add(tw["user"]["id"])
        if("ca50" in district):
            trumpca50.add(tw["user"]["id"])
        if("ca51" in district):
            trumpca51.add(tw["user"]["id"])
        if("ca52" in district):
            trumpca52.add(tw["user"]["id"])
        if("ca53" in district):
            trumpca53.add(tw["user"]["id"])
        if("la1" in district):
            trumpla1.add(tw["user"]["id"])
        if("la2" in district):
            trumpla2.add(tw["user"]["id"])
        if("la3" in district):
            trumpla3.add(tw["user"]["id"])
        if("la4" in district):
            trumpla4.add(tw["user"]["id"])
        if("la5" in district):
            trumpla5.add(tw["user"]["id"])
        if("la6" in district):
            trumpla6.add(tw["user"]["id"])
        if("ct1" in district):
            trumpct1.add(tw["user"]["id"])
        if("ct2" in district):
            trumpct2.add(tw["user"]["id"])
        if("ct3" in district):
            trumpct3.add(tw["user"]["id"])
        if("ct4" in district):
            trumpct4.add(tw["user"]["id"])
        if("ct5" in district):
            trumpct5.add(tw["user"]["id"])
        if("mt1" in district):
            trumpmt1.add(tw["user"]["id"])
        if("ms1" in district):
            trumpms1.add(tw["user"]["id"])
        if("ms2" in district):
            trumpms2.add(tw["user"]["id"])
        if("ms3" in district):
            trumpms3.add(tw["user"]["id"])
        if("ms4" in district):
            trumpms4.add(tw["user"]["id"])
        if("pa1" in district):
            trumppa1.add(tw["user"]["id"])
        if("pa2" in district):
            trumppa2.add(tw["user"]["id"])
        if("pa3" in district):
            trumppa3.add(tw["user"]["id"])
        if("pa4" in district):
            trumppa4.add(tw["user"]["id"])
        if("pa5" in district):
            trumppa5.add(tw["user"]["id"])
        if("pa6" in district):
            trumppa6.add(tw["user"]["id"])
        if("pa7" in district):
            trumppa7.add(tw["user"]["id"])
        if("pa8" in district):
            trumppa8.add(tw["user"]["id"])
        if("pa9" in district):
            trumppa9.add(tw["user"]["id"])
        if("pa10" in district):
            trumppa10.add(tw["user"]["id"])
        if("pa11" in district):
            trumppa11.add(tw["user"]["id"])
        if("pa12" in district):
            trumppa12.add(tw["user"]["id"])
        if("pa13" in district):
            trumppa13.add(tw["user"]["id"])
        if("pa14" in district):
            trumppa14.add(tw["user"]["id"])
        if("pa15" in district):
            trumppa15.add(tw["user"]["id"])
        if("pa16" in district):
            trumppa16.add(tw["user"]["id"])
        if("pa17" in district):
            trumppa17.add(tw["user"]["id"])
        if("pa18" in district):
            trumppa18.add(tw["user"]["id"])
        if("oh1" in district):
            trumpoh1.add(tw["user"]["id"])
        if("oh2" in district):
            trumpoh2.add(tw["user"]["id"])
        if("oh3" in district):
            trumpoh3.add(tw["user"]["id"])
        if("oh4" in district):
            trumpoh4.add(tw["user"]["id"])
        if("oh5" in district):
            trumpoh5.add(tw["user"]["id"])
        if("oh6" in district):
            trumpoh6.add(tw["user"]["id"])
        if("oh7" in district):
            trumpoh7.add(tw["user"]["id"])
        if("oh8" in district):
            trumpoh8.add(tw["user"]["id"])
        if("oh9" in district):
            trumpoh9.add(tw["user"]["id"])
        if("oh10" in district):
            trumpoh10.add(tw["user"]["id"])
        if("oh11" in district):
            trumpoh11.add(tw["user"]["id"])
        if("oh12" in district):
            trumpoh12.add(tw["user"]["id"])
        if("oh13" in district):
            trumpoh13.add(tw["user"]["id"])
        if("oh14" in district):
            trumpoh14.add(tw["user"]["id"])
        if("oh15" in district):
            trumpoh15.add(tw["user"]["id"])
        if("oh16" in district):
            trumpoh16.add(tw["user"]["id"])
        if("fl1" in district):
            trumpfl1.add(tw["user"]["id"])
        if("fl2" in district):
            trumpfl2.add(tw["user"]["id"])
        if("fl3" in district):
            trumpfl3.add(tw["user"]["id"])
        if("fl4" in district):
            trumpfl4.add(tw["user"]["id"])
        if("fl5" in district):
            trumpfl5.add(tw["user"]["id"])
        if("fl6" in district):
            trumpfl6.add(tw["user"]["id"])
        if("fl7" in district):
            trumpfl7.add(tw["user"]["id"])
        if("fl8" in district):
            trumpfl8.add(tw["user"]["id"])
        if("fl9" in district):
            trumpfl9.add(tw["user"]["id"])
        if("fl10" in district):
            trumpfl10.add(tw["user"]["id"])
        if("fl11" in district):
            trumpfl11.add(tw["user"]["id"])
        if("fl12" in district):
            trumpfl12.add(tw["user"]["id"])
        if("fl13" in district):
            trumpfl13.add(tw["user"]["id"])
        if("fl14" in district):
            trumpfl14.add(tw["user"]["id"])
        if("fl15" in district):
            trumpfl15.add(tw["user"]["id"])
        if("fl16" in district):
            trumpfl16.add(tw["user"]["id"])
        if("fl17" in district):
            trumpfl17.add(tw["user"]["id"])
        if("fl18" in district):
            trumpfl18.add(tw["user"]["id"])
        if("fl19" in district):
            trumpfl19.add(tw["user"]["id"])
        if("fl20" in district):
            trumpfl20.add(tw["user"]["id"])
        if("fl21" in district):
            trumpfl21.add(tw["user"]["id"])
        if("fl22" in district):
            trumpfl22.add(tw["user"]["id"])
        if("fl23" in district):
            trumpfl23.add(tw["user"]["id"])
        if("fl24" in district):
            trumpfl24.add(tw["user"]["id"])
        if("fl25" in district):
            trumpfl25.add(tw["user"]["id"])
        if("fl26" in district):
            trumpfl26.add(tw["user"]["id"])
        if("fl27" in district):
            trumpfl27.add(tw["user"]["id"])
        if("wa1" in district):
            trumpwa1.add(tw["user"]["id"])
        if("wa2" in district):
            trumpwa2.add(tw["user"]["id"])
        if("wa3" in district):
            trumpwa3.add(tw["user"]["id"])
        if("wa4" in district):
            trumpwa4.add(tw["user"]["id"])
        if("wa5" in district):
            trumpwa5.add(tw["user"]["id"])
        if("wa6" in district):
            trumpwa6.add(tw["user"]["id"])
        if("wa7" in district):
            trumpwa7.add(tw["user"]["id"])
        if("wa8" in district):
            trumpwa8.add(tw["user"]["id"])
        if("wa9" in district):
            trumpwa9.add(tw["user"]["id"])
        if("wa10" in district):
            trumpwa10.add(tw["user"]["id"])
        if("hi1" in district):
            trumphi1.add(tw["user"]["id"])
        if("hi2" in district):
            trumphi2.add(tw["user"]["id"])
        if("nj1" in district):
            trumpnj1.add(tw["user"]["id"])
        if("nj2" in district):
            trumpnj2.add(tw["user"]["id"])
        if("nj3" in district):
            trumpnj3.add(tw["user"]["id"])
        if("nj4" in district):
            trumpnj4.add(tw["user"]["id"])
        if("nj5" in district):
            trumpnj5.add(tw["user"]["id"])
        if("nj6" in district):
            trumpnj6.add(tw["user"]["id"])
        if("nj7" in district):
            trumpnj7.add(tw["user"]["id"])
        if("nj8" in district):
            trumpnj8.add(tw["user"]["id"])
        if("nj9" in district):
            trumpnj9.add(tw["user"]["id"])
        if("nj10" in district):
            trumpnj10.add(tw["user"]["id"])
        if("nj11" in district):
            trumpnj11.add(tw["user"]["id"])
        if("nj12" in district):
            trumpnj12.add(tw["user"]["id"])
        if("ny1" in district):
            trumpny1.add(tw["user"]["id"])
        if("ny2" in district):
            trumpny2.add(tw["user"]["id"])
        if("ny3" in district):
            trumpny3.add(tw["user"]["id"])
        if("ny4" in district):
            trumpny4.add(tw["user"]["id"])
        if("ny5" in district):
            trumpny5.add(tw["user"]["id"])
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            trumpny6.add(tw["user"]["id"])
            trumpny7.add(tw["user"]["id"])
            trumpny8.add(tw["user"]["id"])
            trumpny9.add(tw["user"]["id"])
            trumpny10.add(tw["user"]["id"])
            trumpny11.add(tw["user"]["id"])
            trumpny12.add(tw["user"]["id"])
            trumpny13.add(tw["user"]["id"])
            trumpny14.add(tw["user"]["id"])
            trumpny15.add(tw["user"]["id"])
        if("ny16" in district):
            trumpny16.add(tw["user"]["id"])
        if("ny17" in district):
            trumpny17.add(tw["user"]["id"])
        if("ny18" in district):
            trumpny18.add(tw["user"]["id"])
        if("ny19" in district):
            trumpny19.add(tw["user"]["id"])
        if("ny20" in district):
            trumpny20.add(tw["user"]["id"])
        if("ny21" in district):
            trumpny21.add(tw["user"]["id"])
        if("ny22" in district):
            trumpny22.add(tw["user"]["id"])
        if("ny23" in district):
            trumpny23.add(tw["user"]["id"])
        if("ny24" in district):
            trumpny24.add(tw["user"]["id"])
        if("ny25" in district):
            trumpny25.add(tw["user"]["id"])
        if("ny26" in district):
            trumpny26.add(tw["user"]["id"])
        if("ny27" in district):
            trumpny27.add(tw["user"]["id"])
        if("ri1" in district):
            trumpri1.add(tw["user"]["id"])
        if("ri2" in district):
            trumpri2.add(tw["user"]["id"])
        if("mn1" in district):
            trumpmn1.add(tw["user"]["id"])
        if("mn2" in district):
            trumpmn2.add(tw["user"]["id"])
        if("mn3" in district):
            trumpmn3.add(tw["user"]["id"])
        if("mn4" in district):
            trumpmn4.add(tw["user"]["id"])
        if("mn5" in district):
            trumpmn5.add(tw["user"]["id"])
        if("mn6" in district):
            trumpmn6.add(tw["user"]["id"])
        if("mn7" in district):
            trumpmn7.add(tw["user"]["id"])
        if("mn8" in district):
            trumpmn8.add(tw["user"]["id"])
        if("mi1" in district):
            trumpmi1.add(tw["user"]["id"])
        if("mi2" in district):
            trumpmi2.add(tw["user"]["id"])
        if("mi3" in district):
            trumpmi3.add(tw["user"]["id"])
        if("mi4" in district):
            trumpmi4.add(tw["user"]["id"])
        if("mi5" in district):
            trumpmi5.add(tw["user"]["id"])
        if("mi6" in district):
            trumpmi6.add(tw["user"]["id"])
        if("mi7" in district):
            trumpmi7.add(tw["user"]["id"])
        if("mi8" in district):
            trumpmi8.add(tw["user"]["id"])
        if("mi9" in district):
            trumpmi9.add(tw["user"]["id"])
        if("mi10" in district):
            trumpmi10.add(tw["user"]["id"])
        if("mi11" in district):
            trumpmi11.add(tw["user"]["id"])
        if("mi12" in district):
            trumpmi12.add(tw["user"]["id"])
        if("mi13" in district):
            trumpmi13.add(tw["user"]["id"])
        if("mi14" in district):
            trumpmi14.add(tw["user"]["id"])
        if("wi1" in district):
            trumpwi1.add(tw["user"]["id"])
        if("wi2" in district):
            trumpwi2.add(tw["user"]["id"])
        if("wi3" in district):
            trumpwi3.add(tw["user"]["id"])
        if("wi4" in district):
            trumpwi4.add(tw["user"]["id"])
        if("wi5" in district):
            trumpwi5.add(tw["user"]["id"])
        if("wi6" in district):
            trumpwi6.add(tw["user"]["id"])
        if("wi7" in district):
            trumpwi7.add(tw["user"]["id"])
        if("wi8" in district):
            trumpwi8.add(tw["user"]["id"])
        if("or1" in district):
            trumpor1.add(tw["user"]["id"])
        if("or2" in district):
            trumpor2.add(tw["user"]["id"])
        if("or3" in district):
            trumpor3.add(tw["user"]["id"])
        if("or4" in district):
            trumpor4.add(tw["user"]["id"])
        if("or5" in district):
            trumpor5.add(tw["user"]["id"])
        if("md1" in district):
            trumpmd1.add(tw["user"]["id"])
        if("md2" in district):
            trumpmd2.add(tw["user"]["id"])
        if("md3" in district):
            trumpmd3.add(tw["user"]["id"])
        if("md4" in district):
            trumpmd4.add(tw["user"]["id"])
        if("md5" in district):
            trumpmd5.add(tw["user"]["id"])
        if("md6" in district):
            trumpmd6.add(tw["user"]["id"])
        if("md7" in district):
            trumpmd7.add(tw["user"]["id"])
        if("md8" in district):
            trumpmd8.add(tw["user"]["id"])
        if("ma1" in district):
            trumpma1.add(tw["user"]["id"])
        if("ma2" in district):
            trumpma2.add(tw["user"]["id"])
        if("ma3" in district):
            trumpma3.add(tw["user"]["id"])
        if("ma4" in district):
            trumpma4.add(tw["user"]["id"])
        if("ma5" in district):
            trumpma5.add(tw["user"]["id"])
        if("ma6" in district):
            trumpma6.add(tw["user"]["id"])
        if("ma7" in district):
            trumpma7.add(tw["user"]["id"])
        if("ma8" in district):
            trumpma8.add(tw["user"]["id"])
        if("ma9" in district):
            trumpma9.add(tw["user"]["id"])
        if("me1" in district):
            trumpme1.add(tw["user"]["id"])
        if("me2" in district):
            trumpme2.add(tw["user"]["id"])
        if("id1" in district):
            trumpid1.add(tw["user"]["id"])
        if("id2" in district):
            trumpid2.add(tw["user"]["id"])
        if("nc1" in district):
            trumpnc1.add(tw["user"]["id"])
        if("nc2" in district):
            trumpnc2.add(tw["user"]["id"])
        if("nc3" in district):
            trumpnc3.add(tw["user"]["id"])
        if("nc4" in district):
            trumpnc4.add(tw["user"]["id"])
        if("nc5" in district):
            trumpnc5.add(tw["user"]["id"])
        if("nc6" in district):
            trumpnc6.add(tw["user"]["id"])
        if("nc7" in district):
            trumpnc7.add(tw["user"]["id"])
        if("nc8" in district):
            trumpnc8.add(tw["user"]["id"])
        if("nc9" in district):
            trumpnc9.add(tw["user"]["id"])
        if("nc10" in district):
            trumpnc10.add(tw["user"]["id"])
        if("nc11" in district):
            trumpnc11.add(tw["user"]["id"])
        if("nc12" in district):
            trumpnc12.add(tw["user"]["id"])
        if("nc13" in district):
            trumpnc13.add(tw["user"]["id"])
        if("nh1" in district):
            trumpnh1.add(tw["user"]["id"])
        if("nh2" in district):
            trumpnh2.add(tw["user"]["id"])
        if("nv1" in district):
            trumpnv1.add(tw["user"]["id"])
        if("nv2" in district):
            trumpnv2.add(tw["user"]["id"])
        if("nv3" in district):
            trumpnv3.add(tw["user"]["id"])
        if("nv4" in district):
            trumpnv4.add(tw["user"]["id"])
        if("co1" in district):
            trumpco1.add(tw["user"]["id"])
        if("co2" in district):
            trumpco2.add(tw["user"]["id"])
        if("co3" in district):
            trumpco3.add(tw["user"]["id"])
        if("co4" in district):
            trumpco4.add(tw["user"]["id"])
        if("co5" in district):
            trumpco5.add(tw["user"]["id"])
        if("co6" in district):
            trumpco6.add(tw["user"]["id"])
        if("co7" in district):
            trumpco7.add(tw["user"]["id"])
        if("nm1" in district):
            trumpnm1.add(tw["user"]["id"])
        if("nm2" in district):
            trumpnm2.add(tw["user"]["id"])
        if("nm3" in district):
            trumpnm3.add(tw["user"]["id"])
        if("az1" in district):
            trumpaz1.add(tw["user"]["id"])
        if("az2" in district):
            trumpaz2.add(tw["user"]["id"])
        if("az3" in district):
            trumpaz3.add(tw["user"]["id"])
        if("az4" in district):
            trumpaz4.add(tw["user"]["id"])
        if("az5" in district):
            trumpaz5.add(tw["user"]["id"])
        if("az6" in district):
            trumpaz6.add(tw["user"]["id"])
        if("az7" in district):
            trumpaz7.add(tw["user"]["id"])
        if("az8" in district):
            trumpaz8.add(tw["user"]["id"])
        if("az9" in district):
            trumpaz9.add(tw["user"]["id"])
        if("ga1" in district):
            trumpga1.add(tw["user"]["id"])
        if("ga2" in district):
            trumpga2.add(tw["user"]["id"])
        if("ga3" in district):
            trumpga3.add(tw["user"]["id"])
        if("ga4" in district):
            trumpga4.add(tw["user"]["id"])
        if("ga5" in district):
            trumpga5.add(tw["user"]["id"])
        if("ga6" in district):
            trumpga6.add(tw["user"]["id"])
        if("ga7" in district):
            trumpga7.add(tw["user"]["id"])
        if("ga8" in district):
            trumpga8.add(tw["user"]["id"])
        if("ga9" in district):
            trumpga9.add(tw["user"]["id"])
        if("ga10" in district):
            trumpga10.add(tw["user"]["id"])
        if("ga11" in district):
            trumpga11.add(tw["user"]["id"])
        if("ga12" in district):
            trumpga12.add(tw["user"]["id"])
        if("ga13" in district):
            trumpga13.add(tw["user"]["id"])
        if("ga14" in district):
            trumpga14.add(tw["user"]["id"])
        if("tx1" in district):
            trumptx1.add(tw["user"]["id"])
        if("tx2" in district):
            trumptx2.add(tw["user"]["id"])
        if("tx3" in district):
            trumptx3.add(tw["user"]["id"])
        if("tx4" in district):
            trumptx4.add(tw["user"]["id"])
        if("tx5" in district):
            trumptx5.add(tw["user"]["id"])
        if("tx6" in district):
            trumptx6.add(tw["user"]["id"])
        if("tx7" in district):
            trumptx7.add(tw["user"]["id"])
        if("tx8" in district):
            trumptx8.add(tw["user"]["id"])
        if("tx9" in district):
            trumptx9.add(tw["user"]["id"])
        if("tx10" in district):
            trumptx10.add(tw["user"]["id"])
        if("tx11" in district):
            trumptx11.add(tw["user"]["id"])
        if("tx12" in district):
            trumptx12.add(tw["user"]["id"])
        if("tx13" in district):
            trumptx13.add(tw["user"]["id"])
        if("tx14" in district):
            trumptx14.add(tw["user"]["id"])
        if("tx15" in district):
            trumptx15.add(tw["user"]["id"])
        if("tx16" in district):
            trumptx16.add(tw["user"]["id"])
        if("tx17" in district):
            trumptx17.add(tw["user"]["id"])
        if("tx18" in district):
            trumptx18.add(tw["user"]["id"])
        if("tx19" in district):
            trumptx19.add(tw["user"]["id"])
        if("tx20" in district):
            trumptx20.add(tw["user"]["id"])
        if("tx21" in district):
            trumptx21.add(tw["user"]["id"])
        if("tx22" in district):
            trumptx22.add(tw["user"]["id"])
        if("tx23" in district):
            trumptx23.add(tw["user"]["id"])
        if("tx24" in district):
            trumptx24.add(tw["user"]["id"])
        if("tx25" in district):
            trumptx25.add(tw["user"]["id"])
        if("tx26" in district):
            trumptx26.add(tw["user"]["id"])
        if("tx27" in district):
            trumptx27.add(tw["user"]["id"])
        if("tx28" in district):
            trumptx28.add(tw["user"]["id"])
        if("tx29" in district):
            trumptx29.add(tw["user"]["id"])
        if("tx30" in district):
            trumptx30.add(tw["user"]["id"])
        if("tx31" in district):
            trumptx31.add(tw["user"]["id"])
        if("tx32" in district):
            trumptx32.add(tw["user"]["id"])
        if("tx33" in district):
            trumptx33.add(tw["user"]["id"])
        if("tx34" in district):
            trumptx34.add(tw["user"]["id"])
        if("tx35" in district):
            trumptx35.add(tw["user"]["id"])
        if("tx36" in district):
            trumptx36.add(tw["user"]["id"])
        if("in1" in district):
            trumpin1.add(tw["user"]["id"])
        if("in2" in district):
            trumpin2.add(tw["user"]["id"])
        if("in3" in district):
            trumpin3.add(tw["user"]["id"])
        if("in4" in district):
            trumpin4.add(tw["user"]["id"])
        if("in5" in district):
            trumpin5.add(tw["user"]["id"])
        if("in6" in district):
            trumpin6.add(tw["user"]["id"])
        if("in7" in district):
            trumpin7.add(tw["user"]["id"])
        if("in8" in district):
            trumpin8.add(tw["user"]["id"])
        if("in9" in district):
            trumpin9.add(tw["user"]["id"])
        if("va1" in district):
            trumpva1.add(tw["user"]["id"])
        if("va2" in district):
            trumpva2.add(tw["user"]["id"])
        if("va3" in district):
            trumpva3.add(tw["user"]["id"])
        if("va4" in district):
            trumpva4.add(tw["user"]["id"])
        if("va5" in district):
            trumpva5.add(tw["user"]["id"])
        if("va6" in district):
            trumpva6.add(tw["user"]["id"])
        if("va7" in district):
            trumpva7.add(tw["user"]["id"])
        if("va8" in district):
            trumpva8.add(tw["user"]["id"])
        if("va9" in district):
            trumpva9.add(tw["user"]["id"])
        if("va10" in district):
            trumpva10.add(tw["user"]["id"])
        if("va11" in district):
            trumpva11.add(tw["user"]["id"])
        if("il1" in district):
            trumpil1.add(tw["user"]["id"])
        if("il2" in district):
            trumpil2.add(tw["user"]["id"])
        if("il3" in district):
            trumpil3.add(tw["user"]["id"])
        if("il4" in district):
            trumpil4.add(tw["user"]["id"])
        if("il5" in district):
            trumpil5.add(tw["user"]["id"])
        if("il6" in district):
            trumpil6.add(tw["user"]["id"])
        if("il7" in district):
            trumpil7.add(tw["user"]["id"])
        if("il8" in district):
            trumpil8.add(tw["user"]["id"])
        if("il9" in district):
            trumpil9.add(tw["user"]["id"])
        if("il10" in district):
            trumpil10.add(tw["user"]["id"])
        if("il11" in district):
            trumpil11.add(tw["user"]["id"])
        if("il12" in district):
            trumpil12.add(tw["user"]["id"])
        if("il13" in district):
            trumpil13.add(tw["user"]["id"])
        if("il14" in district):
            trumpil14.add(tw["user"]["id"])
        if("il15" in district):
            trumpil15.add(tw["user"]["id"])
        if("il16" in district):
            trumpil16.add(tw["user"]["id"])
        if("il17" in district):
            trumpil17.add(tw["user"]["id"])
        if("il18" in district):
            trumpil18.add(tw["user"]["id"])
        if("de1" in district):
            trumpde1.add(tw["user"]["id"])
        if("vt1" in district):
            trumpvt1.add(tw["user"]["id"])
        if("ut1" in district):
            trumput1.add(tw["user"]["id"])
        if("ut2" in district):
            trumput2.add(tw["user"]["id"])
        if("ut3" in district):
            trumput3.add(tw["user"]["id"])
        if("ut4" in district):
            trumput4.add(tw["user"]["id"])
        if("ne1" in district):
            trumpne1.add(tw["user"]["id"])
        if("ne2" in district):
            trumpne2.add(tw["user"]["id"])
        if("ne3" in district):
            trumpne3.add(tw["user"]["id"])
        if("ak1" in district):
            trumpak1.add(tw["user"]["id"])
        if("wy1" in district):
            trumpwy1.add(tw["user"]["id"])
        if("al1" in district):
            trumpal1.add(tw["user"]["id"])
        if("al2" in district):
            trumpal2.add(tw["user"]["id"])
        if("al3" in district):
            trumpal3.add(tw["user"]["id"])
        if("al4" in district):
            trumpal4.add(tw["user"]["id"])
        if("al5" in district):
            trumpal5.add(tw["user"]["id"])
        if("al6" in district):
            trumpal6.add(tw["user"]["id"])
        if("al7" in district):
            trumpal7.add(tw["user"]["id"])
        if("tn1" in district):
            trumptn1.add(tw["user"]["id"])
        if("tn2" in district):
            trumptn2.add(tw["user"]["id"])
        if("tn3" in district):
            trumptn3.add(tw["user"]["id"])
        if("tn4" in district):
            trumptn4.add(tw["user"]["id"])
        if("tn5" in district):
            trumptn5.add(tw["user"]["id"])
        if("tn6" in district):
            trumptn6.add(tw["user"]["id"])
        if("tn7" in district):
            trumptn7.add(tw["user"]["id"])
        if("tn8" in district):
            trumptn8.add(tw["user"]["id"])
        if("tn9" in district):
            trumptn9.add(tw["user"]["id"])
        if("nd1" in district):
            trumpnd1.add(tw["user"]["id"])
        if("sd1" in district):
            trumpsd1.add(tw["user"]["id"])
        if("wv1" in district):
            trumpwv1.add(tw["user"]["id"])
        if("wv2" in district):
            trumpwv2.add(tw["user"]["id"])
        if("wv3" in district):
            trumpwv3.add(tw["user"]["id"])
        if("ar1" in district):
            trumpar1.add(tw["user"]["id"])
        if("ar2" in district):
            trumpar2.add(tw["user"]["id"])
        if("ar3" in district):
            trumpar3.add(tw["user"]["id"])
        if("ar4" in district):
            trumpar4.add(tw["user"]["id"])
    district = sortloc(["#biden2020", "#voteblue"], tw["user"]["location"], tw["retweeted_status"]["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            bidenmo1.add(tw["user"]["id"])
        if("mo2" in district):
            bidenmo2.add(tw["user"]["id"])
        if("mo3" in district):
            bidenmo3.add(tw["user"]["id"])
        if("mo4" in district):
            bidenmo4.add(tw["user"]["id"])
        if("mo5" in district):
            bidenmo5.add(tw["user"]["id"])
        if("mo6" in district):
            bidenmo6.add(tw["user"]["id"])
        if("mo7" in district):
            bidenmo7.add(tw["user"]["id"])
        if("mo8" in district):
            bidenmo8.add(tw["user"]["id"])
        if("sc1" in district):
            bidensc1.add(tw["user"]["id"])
        if("sc2" in district):
            bidensc2.add(tw["user"]["id"])
        if("sc3" in district):
            bidensc3.add(tw["user"]["id"])
        if("sc4" in district):
            bidensc4.add(tw["user"]["id"])
        if("sc5" in district):
            bidensc5.add(tw["user"]["id"])
        if("sc6" in district):
            bidensc6.add(tw["user"]["id"])
        if("sc7" in district):
            bidensc7.add(tw["user"]["id"])
        if("ky1" in district):
            bidenky1.add(tw["user"]["id"])
        if("ky2" in district):
            bidenky2.add(tw["user"]["id"])
        if("ky3" in district):
            bidenky3.add(tw["user"]["id"])
        if("ky4" in district):
            bidenky4.add(tw["user"]["id"])
        if("ky5" in district):
            bidenky5.add(tw["user"]["id"])
        if("ky6" in district):
            bidenky6.add(tw["user"]["id"])
        if("ok1" in district):
            bidenok1.add(tw["user"]["id"])
        if("ok2" in district):
            bidenok2.add(tw["user"]["id"])
        if("ok3" in district):
            bidenok3.add(tw["user"]["id"])
        if("ok4" in district):
            bidenok4.add(tw["user"]["id"])
        if("ok5" in district):
            bidenok5.add(tw["user"]["id"])
        if("ia1" in district):
            bidenia1.add(tw["user"]["id"])
        if("ia2" in district):
            bidenia2.add(tw["user"]["id"])
        if("ia3" in district):
            bidenia3.add(tw["user"]["id"])
        if("ia4" in district):
            bidenia4.add(tw["user"]["id"])
        if("ks1" in district):
            bidenks1.add(tw["user"]["id"])
        if("ks2" in district):
            bidenks2.add(tw["user"]["id"])
        if("ks3" in district):
            bidenks3.add(tw["user"]["id"])
        if("ks4" in district):
            bidenks4.add(tw["user"]["id"])
        if("ca1" in district):
            bidenca1.add(tw["user"]["id"])
        if("ca2" in district):
            bidenca2.add(tw["user"]["id"])
        if("ca3" in district):
            bidenca3.add(tw["user"]["id"])
        if("ca4" in district):
            bidenca4.add(tw["user"]["id"])
        if("ca5" in district):
            bidenca5.add(tw["user"]["id"])
        if("ca6" in district):
            bidenca6.add(tw["user"]["id"])
        if("ca7" in district):
            bidenca7.add(tw["user"]["id"])
        if("ca8" in district):
            bidenca8.add(tw["user"]["id"])
        if("ca9" in district):
            bidenca9.add(tw["user"]["id"])
        if("ca10" in district):
            bidenca10.add(tw["user"]["id"])
        if("ca11" in district):
            bidenca11.add(tw["user"]["id"])
        if("ca12" in district):
            bidenca12.add(tw["user"]["id"])
        if("ca13" in district):
            bidenca13.add(tw["user"]["id"])
        if("ca14" in district):
            bidenca14.add(tw["user"]["id"])
        if("ca15" in district):
            bidenca15.add(tw["user"]["id"])
        if("ca16" in district):
            bidenca16.add(tw["user"]["id"])
        if("ca17" in district):
            bidenca17.add(tw["user"]["id"])
        if("ca18" in district):
            bidenca18.add(tw["user"]["id"])
        if("ca19" in district):
            bidenca19.add(tw["user"]["id"])
        if("ca20" in district):
            bidenca20.add(tw["user"]["id"])
        if("ca21" in district):
            bidenca21.add(tw["user"]["id"])
        if("ca22" in district):
            bidenca22.add(tw["user"]["id"])
        if("ca23" in district):
            bidenca23.add(tw["user"]["id"])
        if("ca24" in district):
            bidenca24.add(tw["user"]["id"])
        if("ca25" in district):
            bidenca25.add(tw["user"]["id"])
        if("ca26" in district):
            bidenca26.add(tw["user"]["id"])
        if("ca27" in district):
            bidenca27.add(tw["user"]["id"])
        if("ca28" in district):
            bidenca28.add(tw["user"]["id"])
        if("ca29" in district):
            bidenca29.add(tw["user"]["id"])
        if("ca30" in district):
            bidenca30.add(tw["user"]["id"])
        if("ca31" in district):
            bidenca31.add(tw["user"]["id"])
        if("ca32" in district):
            bidenca32.add(tw["user"]["id"])
        if("ca33" in district):
            bidenca33.add(tw["user"]["id"])
        if("ca34" in district):
            bidenca34.add(tw["user"]["id"])
        if("ca35" in district):
            bidenca35.add(tw["user"]["id"])
        if("ca36" in district):
            bidenca36.add(tw["user"]["id"])
        if("ca37" in district):
            bidenca37.add(tw["user"]["id"])
        if("ca38" in district):
            bidenca38.add(tw["user"]["id"])
        if("ca39" in district):
            bidenca39.add(tw["user"]["id"])
        if("ca40" in district):
            bidenca40.add(tw["user"]["id"])
        if("ca41" in district):
            bidenca41.add(tw["user"]["id"])
        if("ca42" in district):
            bidenca42.add(tw["user"]["id"])
        if("ca43" in district):
            bidenca43.add(tw["user"]["id"])
        if("ca44" in district):
            bidenca44.add(tw["user"]["id"])
        if("ca45" in district):
            bidenca45.add(tw["user"]["id"])
        if("ca46" in district):
            bidenca46.add(tw["user"]["id"])
        if("ca47" in district):
            bidenca47.add(tw["user"]["id"])
        if("ca48" in district):
            bidenca48.add(tw["user"]["id"])
        if("ca49" in district):
            bidenca49.add(tw["user"]["id"])
        if("ca50" in district):
            bidenca50.add(tw["user"]["id"])
        if("ca51" in district):
            bidenca51.add(tw["user"]["id"])
        if("ca52" in district):
            bidenca52.add(tw["user"]["id"])
        if("ca53" in district):
            bidenca53.add(tw["user"]["id"])
        if("la1" in district):
            bidenla1.add(tw["user"]["id"])
        if("la2" in district):
            bidenla2.add(tw["user"]["id"])
        if("la3" in district):
            bidenla3.add(tw["user"]["id"])
        if("la4" in district):
            bidenla4.add(tw["user"]["id"])
        if("la5" in district):
            bidenla5.add(tw["user"]["id"])
        if("la6" in district):
            bidenla6.add(tw["user"]["id"])
        if("ct1" in district):
            bidenct1.add(tw["user"]["id"])
        if("ct2" in district):
            bidenct2.add(tw["user"]["id"])
        if("ct3" in district):
            bidenct3.add(tw["user"]["id"])
        if("ct4" in district):
            bidenct4.add(tw["user"]["id"])
        if("ct5" in district):
            bidenct5.add(tw["user"]["id"])
        if("mt1" in district):
            bidenmt1.add(tw["user"]["id"])
        if("ms1" in district):
            bidenms1.add(tw["user"]["id"])
        if("ms2" in district):
            bidenms2.add(tw["user"]["id"])
        if("ms3" in district):
            bidenms3.add(tw["user"]["id"])
        if("ms4" in district):
            bidenms4.add(tw["user"]["id"])
        if("pa1" in district):
            bidenpa1.add(tw["user"]["id"])
        if("pa2" in district):
            bidenpa2.add(tw["user"]["id"])
        if("pa3" in district):
            bidenpa3.add(tw["user"]["id"])
        if("pa4" in district):
            bidenpa4.add(tw["user"]["id"])
        if("pa5" in district):
            bidenpa5.add(tw["user"]["id"])
        if("pa6" in district):
            bidenpa6.add(tw["user"]["id"])
        if("pa7" in district):
            bidenpa7.add(tw["user"]["id"])
        if("pa8" in district):
            bidenpa8.add(tw["user"]["id"])
        if("pa9" in district):
            bidenpa9.add(tw["user"]["id"])
        if("pa10" in district):
            bidenpa10.add(tw["user"]["id"])
        if("pa11" in district):
            bidenpa11.add(tw["user"]["id"])
        if("pa12" in district):
            bidenpa12.add(tw["user"]["id"])
        if("pa13" in district):
            bidenpa13.add(tw["user"]["id"])
        if("pa14" in district):
            bidenpa14.add(tw["user"]["id"])
        if("pa15" in district):
            bidenpa15.add(tw["user"]["id"])
        if("pa16" in district):
            bidenpa16.add(tw["user"]["id"])
        if("pa17" in district):
            bidenpa17.add(tw["user"]["id"])
        if("pa18" in district):
            bidenpa18.add(tw["user"]["id"])
        if("oh1" in district):
            bidenoh1.add(tw["user"]["id"])
        if("oh2" in district):
            bidenoh2.add(tw["user"]["id"])
        if("oh3" in district):
            bidenoh3.add(tw["user"]["id"])
        if("oh4" in district):
            bidenoh4.add(tw["user"]["id"])
        if("oh5" in district):
            bidenoh5.add(tw["user"]["id"])
        if("oh6" in district):
            bidenoh6.add(tw["user"]["id"])
        if("oh7" in district):
            bidenoh7.add(tw["user"]["id"])
        if("oh8" in district):
            bidenoh8.add(tw["user"]["id"])
        if("oh9" in district):
            bidenoh9.add(tw["user"]["id"])
        if("oh10" in district):
            bidenoh10.add(tw["user"]["id"])
        if("oh11" in district):
            bidenoh11.add(tw["user"]["id"])
        if("oh12" in district):
            bidenoh12.add(tw["user"]["id"])
        if("oh13" in district):
            bidenoh13.add(tw["user"]["id"])
        if("oh14" in district):
            bidenoh14.add(tw["user"]["id"])
        if("oh15" in district):
            bidenoh15.add(tw["user"]["id"])
        if("oh16" in district):
            bidenoh16.add(tw["user"]["id"])
        if("fl1" in district):
            bidenfl1.add(tw["user"]["id"])
        if("fl2" in district):
            bidenfl2.add(tw["user"]["id"])
        if("fl3" in district):
            bidenfl3.add(tw["user"]["id"])
        if("fl4" in district):
            bidenfl4.add(tw["user"]["id"])
        if("fl5" in district):
            bidenfl5.add(tw["user"]["id"])
        if("fl6" in district):
            bidenfl6.add(tw["user"]["id"])
        if("fl7" in district):
            bidenfl7.add(tw["user"]["id"])
        if("fl8" in district):
            bidenfl8.add(tw["user"]["id"])
        if("fl9" in district):
            bidenfl9.add(tw["user"]["id"])
        if("fl10" in district):
            bidenfl10.add(tw["user"]["id"])
        if("fl11" in district):
            bidenfl11.add(tw["user"]["id"])
        if("fl12" in district):
            bidenfl12.add(tw["user"]["id"])
        if("fl13" in district):
            bidenfl13.add(tw["user"]["id"])
        if("fl14" in district):
            bidenfl14.add(tw["user"]["id"])
        if("fl15" in district):
            bidenfl15.add(tw["user"]["id"])
        if("fl16" in district):
            bidenfl16.add(tw["user"]["id"])
        if("fl17" in district):
            bidenfl17.add(tw["user"]["id"])
        if("fl18" in district):
            bidenfl18.add(tw["user"]["id"])
        if("fl19" in district):
            bidenfl19.add(tw["user"]["id"])
        if("fl20" in district):
            bidenfl20.add(tw["user"]["id"])
        if("fl21" in district):
            bidenfl21.add(tw["user"]["id"])
        if("fl22" in district):
            bidenfl22.add(tw["user"]["id"])
        if("fl23" in district):
            bidenfl23.add(tw["user"]["id"])
        if("fl24" in district):
            bidenfl24.add(tw["user"]["id"])
        if("fl25" in district):
            bidenfl25.add(tw["user"]["id"])
        if("fl26" in district):
            bidenfl26.add(tw["user"]["id"])
        if("fl27" in district):
            bidenfl27.add(tw["user"]["id"])
        if("wa1" in district):
            bidenwa1.add(tw["user"]["id"])
        if("wa2" in district):
            bidenwa2.add(tw["user"]["id"])
        if("wa3" in district):
            bidenwa3.add(tw["user"]["id"])
        if("wa4" in district):
            bidenwa4.add(tw["user"]["id"])
        if("wa5" in district):
            bidenwa5.add(tw["user"]["id"])
        if("wa6" in district):
            bidenwa6.add(tw["user"]["id"])
        if("wa7" in district):
            bidenwa7.add(tw["user"]["id"])
        if("wa8" in district):
            bidenwa8.add(tw["user"]["id"])
        if("wa9" in district):
            bidenwa9.add(tw["user"]["id"])
        if("wa10" in district):
            bidenwa10.add(tw["user"]["id"])
        if("hi1" in district):
            bidenhi1.add(tw["user"]["id"])
        if("hi2" in district):
            bidenhi2.add(tw["user"]["id"])
        if("nj1" in district):
            bidennj1.add(tw["user"]["id"])
        if("nj2" in district):
            bidennj2.add(tw["user"]["id"])
        if("nj3" in district):
            bidennj3.add(tw["user"]["id"])
        if("nj4" in district):
            bidennj4.add(tw["user"]["id"])
        if("nj5" in district):
            bidennj5.add(tw["user"]["id"])
        if("nj6" in district):
            bidennj6.add(tw["user"]["id"])
        if("nj7" in district):
            bidennj7.add(tw["user"]["id"])
        if("nj8" in district):
            bidennj8.add(tw["user"]["id"])
        if("nj9" in district):
            bidennj9.add(tw["user"]["id"])
        if("nj10" in district):
            bidennj10.add(tw["user"]["id"])
        if("nj11" in district):
            bidennj11.add(tw["user"]["id"])
        if("nj12" in district):
            bidennj12.add(tw["user"]["id"])
        if("ny1" in district):
            bidenny1.add(tw["user"]["id"])
        if("ny2" in district):
            bidenny2.add(tw["user"]["id"])
        if("ny3" in district):
            bidenny3.add(tw["user"]["id"])
        if("ny4" in district):
            bidenny4.add(tw["user"]["id"])
        if("ny5" in district):
            bidenny5.add(tw["user"]["id"])
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            bidenny6.add(tw["user"]["id"])
            bidenny7.add(tw["user"]["id"])
            bidenny8.add(tw["user"]["id"])
            bidenny9.add(tw["user"]["id"])
            bidenny10.add(tw["user"]["id"])
            bidenny11.add(tw["user"]["id"])
            bidenny12.add(tw["user"]["id"])
            bidenny13.add(tw["user"]["id"])
            bidenny14.add(tw["user"]["id"])
            bidenny15.add(tw["user"]["id"])
        if("ny16" in district):
            bidenny16.add(tw["user"]["id"])
        if("ny17" in district):
            bidenny17.add(tw["user"]["id"])
        if("ny18" in district):
            bidenny18.add(tw["user"]["id"])
        if("ny19" in district):
            bidenny19.add(tw["user"]["id"])
        if("ny20" in district):
            bidenny20.add(tw["user"]["id"])
        if("ny21" in district):
            bidenny21.add(tw["user"]["id"])
        if("ny22" in district):
            bidenny22.add(tw["user"]["id"])
        if("ny23" in district):
            bidenny23.add(tw["user"]["id"])
        if("ny24" in district):
            bidenny24.add(tw["user"]["id"])
        if("ny25" in district):
            bidenny25.add(tw["user"]["id"])
        if("ny26" in district):
            bidenny26.add(tw["user"]["id"])
        if("ny27" in district):
            bidenny27.add(tw["user"]["id"])
        if("ri1" in district):
            bidenri1.add(tw["user"]["id"])
        if("ri2" in district):
            bidenri2.add(tw["user"]["id"])
        if("mn1" in district):
            bidenmn1.add(tw["user"]["id"])
        if("mn2" in district):
            bidenmn2.add(tw["user"]["id"])
        if("mn3" in district):
            bidenmn3.add(tw["user"]["id"])
        if("mn4" in district):
            bidenmn4.add(tw["user"]["id"])
        if("mn5" in district):
            bidenmn5.add(tw["user"]["id"])
        if("mn6" in district):
            bidenmn6.add(tw["user"]["id"])
        if("mn7" in district):
            bidenmn7.add(tw["user"]["id"])
        if("mn8" in district):
            bidenmn8.add(tw["user"]["id"])
        if("mi1" in district):
            bidenmi1.add(tw["user"]["id"])
        if("mi2" in district):
            bidenmi2.add(tw["user"]["id"])
        if("mi3" in district):
            bidenmi3.add(tw["user"]["id"])
        if("mi4" in district):
            bidenmi4.add(tw["user"]["id"])
        if("mi5" in district):
            bidenmi5.add(tw["user"]["id"])
        if("mi6" in district):
            bidenmi6.add(tw["user"]["id"])
        if("mi7" in district):
            bidenmi7.add(tw["user"]["id"])
        if("mi8" in district):
            bidenmi8.add(tw["user"]["id"])
        if("mi9" in district):
            bidenmi9.add(tw["user"]["id"])
        if("mi10" in district):
            bidenmi10.add(tw["user"]["id"])
        if("mi11" in district):
            bidenmi11.add(tw["user"]["id"])
        if("mi12" in district):
            bidenmi12.add(tw["user"]["id"])
        if("mi13" in district):
            bidenmi13.add(tw["user"]["id"])
        if("mi14" in district):
            bidenmi14.add(tw["user"]["id"])
        if("wi1" in district):
            bidenwi1.add(tw["user"]["id"])
        if("wi2" in district):
            bidenwi2.add(tw["user"]["id"])
        if("wi3" in district):
            bidenwi3.add(tw["user"]["id"])
        if("wi4" in district):
            bidenwi4.add(tw["user"]["id"])
        if("wi5" in district):
            bidenwi5.add(tw["user"]["id"])
        if("wi6" in district):
            bidenwi6.add(tw["user"]["id"])
        if("wi7" in district):
            bidenwi7.add(tw["user"]["id"])
        if("wi8" in district):
            bidenwi8.add(tw["user"]["id"])
        if("or1" in district):
            bidenor1.add(tw["user"]["id"])
        if("or2" in district):
            bidenor2.add(tw["user"]["id"])
        if("or3" in district):
            bidenor3.add(tw["user"]["id"])
        if("or4" in district):
            bidenor4.add(tw["user"]["id"])
        if("or5" in district):
            bidenor5.add(tw["user"]["id"])
        if("md1" in district):
            bidenmd1.add(tw["user"]["id"])
        if("md2" in district):
            bidenmd2.add(tw["user"]["id"])
        if("md3" in district):
            bidenmd3.add(tw["user"]["id"])
        if("md4" in district):
            bidenmd4.add(tw["user"]["id"])
        if("md5" in district):
            bidenmd5.add(tw["user"]["id"])
        if("md6" in district):
            bidenmd6.add(tw["user"]["id"])
        if("md7" in district):
            bidenmd7.add(tw["user"]["id"])
        if("md8" in district):
            bidenmd8.add(tw["user"]["id"])
        if("ma1" in district):
            bidenma1.add(tw["user"]["id"])
        if("ma2" in district):
            bidenma2.add(tw["user"]["id"])
        if("ma3" in district):
            bidenma3.add(tw["user"]["id"])
        if("ma4" in district):
            bidenma4.add(tw["user"]["id"])
        if("ma5" in district):
            bidenma5.add(tw["user"]["id"])
        if("ma6" in district):
            bidenma6.add(tw["user"]["id"])
        if("ma7" in district):
            bidenma7.add(tw["user"]["id"])
        if("ma8" in district):
            bidenma8.add(tw["user"]["id"])
        if("ma9" in district):
            bidenma9.add(tw["user"]["id"])
        if("me1" in district):
            bidenme1.add(tw["user"]["id"])
        if("me2" in district):
            bidenme2.add(tw["user"]["id"])
        if("id1" in district):
            bidenid1.add(tw["user"]["id"])
        if("id2" in district):
            bidenid2.add(tw["user"]["id"])
        if("nc1" in district):
            bidennc1.add(tw["user"]["id"])
        if("nc2" in district):
            bidennc2.add(tw["user"]["id"])
        if("nc3" in district):
            bidennc3.add(tw["user"]["id"])
        if("nc4" in district):
            bidennc4.add(tw["user"]["id"])
        if("nc5" in district):
            bidennc5.add(tw["user"]["id"])
        if("nc6" in district):
            bidennc6.add(tw["user"]["id"])
        if("nc7" in district):
            bidennc7.add(tw["user"]["id"])
        if("nc8" in district):
            bidennc8.add(tw["user"]["id"])
        if("nc9" in district):
            bidennc9.add(tw["user"]["id"])
        if("nc10" in district):
            bidennc10.add(tw["user"]["id"])
        if("nc11" in district):
            bidennc11.add(tw["user"]["id"])
        if("nc12" in district):
            bidennc12.add(tw["user"]["id"])
        if("nc13" in district):
            bidennc13.add(tw["user"]["id"])
        if("nh1" in district):
            bidennh1.add(tw["user"]["id"])
        if("nh2" in district):
            bidennh2.add(tw["user"]["id"])
        if("nv1" in district):
            bidennv1.add(tw["user"]["id"])
        if("nv2" in district):
            bidennv2.add(tw["user"]["id"])
        if("nv3" in district):
            bidennv3.add(tw["user"]["id"])
        if("nv4" in district):
            bidennv4.add(tw["user"]["id"])
        if("co1" in district):
            bidenco1.add(tw["user"]["id"])
        if("co2" in district):
            bidenco2.add(tw["user"]["id"])
        if("co3" in district):
            bidenco3.add(tw["user"]["id"])
        if("co4" in district):
            bidenco4.add(tw["user"]["id"])
        if("co5" in district):
            bidenco5.add(tw["user"]["id"])
        if("co6" in district):
            bidenco6.add(tw["user"]["id"])
        if("co7" in district):
            bidenco7.add(tw["user"]["id"])
        if("nm1" in district):
            bidennm1.add(tw["user"]["id"])
        if("nm2" in district):
            bidennm2.add(tw["user"]["id"])
        if("nm3" in district):
            bidennm3.add(tw["user"]["id"])
        if("az1" in district):
            bidenaz1.add(tw["user"]["id"])
        if("az2" in district):
            bidenaz2.add(tw["user"]["id"])
        if("az3" in district):
            bidenaz3.add(tw["user"]["id"])
        if("az4" in district):
            bidenaz4.add(tw["user"]["id"])
        if("az5" in district):
            bidenaz5.add(tw["user"]["id"])
        if("az6" in district):
            bidenaz6.add(tw["user"]["id"])
        if("az7" in district):
            bidenaz7.add(tw["user"]["id"])
        if("az8" in district):
            bidenaz8.add(tw["user"]["id"])
        if("az9" in district):
            bidenaz9.add(tw["user"]["id"])
        if("ga1" in district):
            bidenga1.add(tw["user"]["id"])
        if("ga2" in district):
            bidenga2.add(tw["user"]["id"])
        if("ga3" in district):
            bidenga3.add(tw["user"]["id"])
        if("ga4" in district):
            bidenga4.add(tw["user"]["id"])
        if("ga5" in district):
            bidenga5.add(tw["user"]["id"])
        if("ga6" in district):
            bidenga6.add(tw["user"]["id"])
        if("ga7" in district):
            bidenga7.add(tw["user"]["id"])
        if("ga8" in district):
            bidenga8.add(tw["user"]["id"])
        if("ga9" in district):
            bidenga9.add(tw["user"]["id"])
        if("ga10" in district):
            bidenga10.add(tw["user"]["id"])
        if("ga11" in district):
            bidenga11.add(tw["user"]["id"])
        if("ga12" in district):
            bidenga12.add(tw["user"]["id"])
        if("ga13" in district):
            bidenga13.add(tw["user"]["id"])
        if("ga14" in district):
            bidenga14.add(tw["user"]["id"])
        if("tx1" in district):
            bidentx1.add(tw["user"]["id"])
        if("tx2" in district):
            bidentx2.add(tw["user"]["id"])
        if("tx3" in district):
            bidentx3.add(tw["user"]["id"])
        if("tx4" in district):
            bidentx4.add(tw["user"]["id"])
        if("tx5" in district):
            bidentx5.add(tw["user"]["id"])
        if("tx6" in district):
            bidentx6.add(tw["user"]["id"])
        if("tx7" in district):
            bidentx7.add(tw["user"]["id"])
        if("tx8" in district):
            bidentx8.add(tw["user"]["id"])
        if("tx9" in district):
            bidentx9.add(tw["user"]["id"])
        if("tx10" in district):
            bidentx10.add(tw["user"]["id"])
        if("tx11" in district):
            bidentx11.add(tw["user"]["id"])
        if("tx12" in district):
            bidentx12.add(tw["user"]["id"])
        if("tx13" in district):
            bidentx13.add(tw["user"]["id"])
        if("tx14" in district):
            bidentx14.add(tw["user"]["id"])
        if("tx15" in district):
            bidentx15.add(tw["user"]["id"])
        if("tx16" in district):
            bidentx16.add(tw["user"]["id"])
        if("tx17" in district):
            bidentx17.add(tw["user"]["id"])
        if("tx18" in district):
            bidentx18.add(tw["user"]["id"])
        if("tx19" in district):
            bidentx19.add(tw["user"]["id"])
        if("tx20" in district):
            bidentx20.add(tw["user"]["id"])
        if("tx21" in district):
            bidentx21.add(tw["user"]["id"])
        if("tx22" in district):
            bidentx22.add(tw["user"]["id"])
        if("tx23" in district):
            bidentx23.add(tw["user"]["id"])
        if("tx24" in district):
            bidentx24.add(tw["user"]["id"])
        if("tx25" in district):
            bidentx25.add(tw["user"]["id"])
        if("tx26" in district):
            bidentx26.add(tw["user"]["id"])
        if("tx27" in district):
            bidentx27.add(tw["user"]["id"])
        if("tx28" in district):
            bidentx28.add(tw["user"]["id"])
        if("tx29" in district):
            bidentx29.add(tw["user"]["id"])
        if("tx30" in district):
            bidentx30.add(tw["user"]["id"])
        if("tx31" in district):
            bidentx31.add(tw["user"]["id"])
        if("tx32" in district):
            bidentx32.add(tw["user"]["id"])
        if("tx33" in district):
            bidentx33.add(tw["user"]["id"])
        if("tx34" in district):
            bidentx34.add(tw["user"]["id"])
        if("tx35" in district):
            bidentx35.add(tw["user"]["id"])
        if("tx36" in district):
            bidentx36.add(tw["user"]["id"])
        if("in1" in district):
            bidenin1.add(tw["user"]["id"])
        if("in2" in district):
            bidenin2.add(tw["user"]["id"])
        if("in3" in district):
            bidenin3.add(tw["user"]["id"])
        if("in4" in district):
            bidenin4.add(tw["user"]["id"])
        if("in5" in district):
            bidenin5.add(tw["user"]["id"])
        if("in6" in district):
            bidenin6.add(tw["user"]["id"])
        if("in7" in district):
            bidenin7.add(tw["user"]["id"])
        if("in8" in district):
            bidenin8.add(tw["user"]["id"])
        if("in9" in district):
            bidenin9.add(tw["user"]["id"])
        if("va1" in district):
            bidenva1.add(tw["user"]["id"])
        if("va2" in district):
            bidenva2.add(tw["user"]["id"])
        if("va3" in district):
            bidenva3.add(tw["user"]["id"])
        if("va4" in district):
            bidenva4.add(tw["user"]["id"])
        if("va5" in district):
            bidenva5.add(tw["user"]["id"])
        if("va6" in district):
            bidenva6.add(tw["user"]["id"])
        if("va7" in district):
            bidenva7.add(tw["user"]["id"])
        if("va8" in district):
            bidenva8.add(tw["user"]["id"])
        if("va9" in district):
            bidenva9.add(tw["user"]["id"])
        if("va10" in district):
            bidenva10.add(tw["user"]["id"])
        if("va11" in district):
            bidenva11.add(tw["user"]["id"])
        if("il1" in district):
            bidenil1.add(tw["user"]["id"])
        if("il2" in district):
            bidenil2.add(tw["user"]["id"])
        if("il3" in district):
            bidenil3.add(tw["user"]["id"])
        if("il4" in district):
            bidenil4.add(tw["user"]["id"])
        if("il5" in district):
            bidenil5.add(tw["user"]["id"])
        if("il6" in district):
            bidenil6.add(tw["user"]["id"])
        if("il7" in district):
            bidenil7.add(tw["user"]["id"])
        if("il8" in district):
            bidenil8.add(tw["user"]["id"])
        if("il9" in district):
            bidenil9.add(tw["user"]["id"])
        if("il10" in district):
            bidenil10.add(tw["user"]["id"])
        if("il11" in district):
            bidenil11.add(tw["user"]["id"])
        if("il12" in district):
            bidenil12.add(tw["user"]["id"])
        if("il13" in district):
            bidenil13.add(tw["user"]["id"])
        if("il14" in district):
            bidenil14.add(tw["user"]["id"])
        if("il15" in district):
            bidenil15.add(tw["user"]["id"])
        if("il16" in district):
            bidenil16.add(tw["user"]["id"])
        if("il17" in district):
            bidenil17.add(tw["user"]["id"])
        if("il18" in district):
            bidenil18.add(tw["user"]["id"])
        if("de1" in district):
            bidende1.add(tw["user"]["id"])
        if("vt1" in district):
            bidenvt1.add(tw["user"]["id"])
        if("ut1" in district):
            bidenut1.add(tw["user"]["id"])
        if("ut2" in district):
            bidenut2.add(tw["user"]["id"])
        if("ut3" in district):
            bidenut3.add(tw["user"]["id"])
        if("ut4" in district):
            bidenut4.add(tw["user"]["id"])
        if("ne1" in district):
            bidenne1.add(tw["user"]["id"])
        if("ne2" in district):
            bidenne2.add(tw["user"]["id"])
        if("ne3" in district):
            bidenne3.add(tw["user"]["id"])
        if("ak1" in district):
            bidenak1.add(tw["user"]["id"])
        if("wy1" in district):
            bidenwy1.add(tw["user"]["id"])
        if("al1" in district):
            bidenal1.add(tw["user"]["id"])
        if("al2" in district):
            bidenal2.add(tw["user"]["id"])
        if("al3" in district):
            bidenal3.add(tw["user"]["id"])
        if("al4" in district):
            bidenal4.add(tw["user"]["id"])
        if("al5" in district):
            bidenal5.add(tw["user"]["id"])
        if("al6" in district):
            bidenal6.add(tw["user"]["id"])
        if("al7" in district):
            bidenal7.add(tw["user"]["id"])
        if("tn1" in district):
            bidentn1.add(tw["user"]["id"])
        if("tn2" in district):
            bidentn2.add(tw["user"]["id"])
        if("tn3" in district):
            bidentn3.add(tw["user"]["id"])
        if("tn4" in district):
            bidentn4.add(tw["user"]["id"])
        if("tn5" in district):
            bidentn5.add(tw["user"]["id"])
        if("tn6" in district):
            bidentn6.add(tw["user"]["id"])
        if("tn7" in district):
            bidentn7.add(tw["user"]["id"])
        if("tn8" in district):
            bidentn8.add(tw["user"]["id"])
        if("tn9" in district):
            bidentn9.add(tw["user"]["id"])
        if("nd1" in district):
            bidennd1.add(tw["user"]["id"])
        if("sd1" in district):
            bidensd1.add(tw["user"]["id"])
        if("wv1" in district):
            bidenwv1.add(tw["user"]["id"])
        if("wv2" in district):
            bidenwv2.add(tw["user"]["id"])
        if("wv3" in district):
            bidenwv3.add(tw["user"]["id"])
        if("ar1" in district):
            bidenar1.add(tw["user"]["id"])
        if("ar2" in district):
            bidenar2.add(tw["user"]["id"])
        if("ar3" in district):
            bidenar3.add(tw["user"]["id"])
        if("ar4" in district):
            bidenar4.add(tw["user"]["id"])

cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
    district = sortloc(["#trump2020", "#votered"], tw["user"]["location"], tw["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            trumpmo1.add(tw["user"]["id"])
        if("mo2" in district):
            trumpmo2.add(tw["user"]["id"])
        if("mo3" in district):
            trumpmo3.add(tw["user"]["id"])
        if("mo4" in district):
            trumpmo4.add(tw["user"]["id"])
        if("mo5" in district):
            trumpmo5.add(tw["user"]["id"])
        if("mo6" in district):
            trumpmo6.add(tw["user"]["id"])
        if("mo7" in district):
            trumpmo7.add(tw["user"]["id"])
        if("mo8" in district):
            trumpmo8.add(tw["user"]["id"])
        if("sc1" in district):
            trumpsc1.add(tw["user"]["id"])
        if("sc2" in district):
            trumpsc2.add(tw["user"]["id"])
        if("sc3" in district):
            trumpsc3.add(tw["user"]["id"])
        if("sc4" in district):
            trumpsc4.add(tw["user"]["id"])
        if("sc5" in district):
            trumpsc5.add(tw["user"]["id"])
        if("sc6" in district):
            trumpsc6.add(tw["user"]["id"])
        if("sc7" in district):
            trumpsc7.add(tw["user"]["id"])
        if("ky1" in district):
            trumpky1.add(tw["user"]["id"])
        if("ky2" in district):
            trumpky2.add(tw["user"]["id"])
        if("ky3" in district):
            trumpky3.add(tw["user"]["id"])
        if("ky4" in district):
            trumpky4.add(tw["user"]["id"])
        if("ky5" in district):
            trumpky5.add(tw["user"]["id"])
        if("ky6" in district):
            trumpky6.add(tw["user"]["id"])
        if("ok1" in district):
            trumpok1.add(tw["user"]["id"])
        if("ok2" in district):
            trumpok2.add(tw["user"]["id"])
        if("ok3" in district):
            trumpok3.add(tw["user"]["id"])
        if("ok4" in district):
            trumpok4.add(tw["user"]["id"])
        if("ok5" in district):
            trumpok5.add(tw["user"]["id"])
        if("ia1" in district):
            trumpia1.add(tw["user"]["id"])
        if("ia2" in district):
            trumpia2.add(tw["user"]["id"])
        if("ia3" in district):
            trumpia3.add(tw["user"]["id"])
        if("ia4" in district):
            trumpia4.add(tw["user"]["id"])
        if("ks1" in district):
            trumpks1.add(tw["user"]["id"])
        if("ks2" in district):
            trumpks2.add(tw["user"]["id"])
        if("ks3" in district):
            trumpks3.add(tw["user"]["id"])
        if("ks4" in district):
            trumpks4.add(tw["user"]["id"])
        if("ca1" in district):
            trumpca1.add(tw["user"]["id"])
        if("ca2" in district):
            trumpca2.add(tw["user"]["id"])
        if("ca3" in district):
            trumpca3.add(tw["user"]["id"])
        if("ca4" in district):
            trumpca4.add(tw["user"]["id"])
        if("ca5" in district):
            trumpca5.add(tw["user"]["id"])
        if("ca6" in district):
            trumpca6.add(tw["user"]["id"])
        if("ca7" in district):
            trumpca7.add(tw["user"]["id"])
        if("ca8" in district):
            trumpca8.add(tw["user"]["id"])
        if("ca9" in district):
            trumpca9.add(tw["user"]["id"])
        if("ca10" in district):
            trumpca10.add(tw["user"]["id"])
        if("ca11" in district):
            trumpca11.add(tw["user"]["id"])
        if("ca12" in district):
            trumpca12.add(tw["user"]["id"])
        if("ca13" in district):
            trumpca13.add(tw["user"]["id"])
        if("ca14" in district):
            trumpca14.add(tw["user"]["id"])
        if("ca15" in district):
            trumpca15.add(tw["user"]["id"])
        if("ca16" in district):
            trumpca16.add(tw["user"]["id"])
        if("ca17" in district):
            trumpca17.add(tw["user"]["id"])
        if("ca18" in district):
            trumpca18.add(tw["user"]["id"])
        if("ca19" in district):
            trumpca19.add(tw["user"]["id"])
        if("ca20" in district):
            trumpca20.add(tw["user"]["id"])
        if("ca21" in district):
            trumpca21.add(tw["user"]["id"])
        if("ca22" in district):
            trumpca22.add(tw["user"]["id"])
        if("ca23" in district):
            trumpca23.add(tw["user"]["id"])
        if("ca24" in district):
            trumpca24.add(tw["user"]["id"])
        if("ca25" in district):
            trumpca25.add(tw["user"]["id"])
        if("ca26" in district):
            trumpca26.add(tw["user"]["id"])
        if("ca27" in district):
            trumpca27.add(tw["user"]["id"])
        if("ca28" in district):
            trumpca28.add(tw["user"]["id"])
        if("ca29" in district):
            trumpca29.add(tw["user"]["id"])
        if("ca30" in district):
            trumpca30.add(tw["user"]["id"])
        if("ca31" in district):
            trumpca31.add(tw["user"]["id"])
        if("ca32" in district):
            trumpca32.add(tw["user"]["id"])
        if("ca33" in district):
            trumpca33.add(tw["user"]["id"])
        if("ca34" in district):
            trumpca34.add(tw["user"]["id"])
        if("ca35" in district):
            trumpca35.add(tw["user"]["id"])
        if("ca36" in district):
            trumpca36.add(tw["user"]["id"])
        if("ca37" in district):
            trumpca37.add(tw["user"]["id"])
        if("ca38" in district):
            trumpca38.add(tw["user"]["id"])
        if("ca39" in district):
            trumpca39.add(tw["user"]["id"])
        if("ca40" in district):
            trumpca40.add(tw["user"]["id"])
        if("ca41" in district):
            trumpca41.add(tw["user"]["id"])
        if("ca42" in district):
            trumpca42.add(tw["user"]["id"])
        if("ca43" in district):
            trumpca43.add(tw["user"]["id"])
        if("ca44" in district):
            trumpca44.add(tw["user"]["id"])
        if("ca45" in district):
            trumpca45.add(tw["user"]["id"])
        if("ca46" in district):
            trumpca46.add(tw["user"]["id"])
        if("ca47" in district):
            trumpca47.add(tw["user"]["id"])
        if("ca48" in district):
            trumpca48.add(tw["user"]["id"])
        if("ca49" in district):
            trumpca49.add(tw["user"]["id"])
        if("ca50" in district):
            trumpca50.add(tw["user"]["id"])
        if("ca51" in district):
            trumpca51.add(tw["user"]["id"])
        if("ca52" in district):
            trumpca52.add(tw["user"]["id"])
        if("ca53" in district):
            trumpca53.add(tw["user"]["id"])
        if("la1" in district):
            trumpla1.add(tw["user"]["id"])
        if("la2" in district):
            trumpla2.add(tw["user"]["id"])
        if("la3" in district):
            trumpla3.add(tw["user"]["id"])
        if("la4" in district):
            trumpla4.add(tw["user"]["id"])
        if("la5" in district):
            trumpla5.add(tw["user"]["id"])
        if("la6" in district):
            trumpla6.add(tw["user"]["id"])
        if("ct1" in district):
            trumpct1.add(tw["user"]["id"])
        if("ct2" in district):
            trumpct2.add(tw["user"]["id"])
        if("ct3" in district):
            trumpct3.add(tw["user"]["id"])
        if("ct4" in district):
            trumpct4.add(tw["user"]["id"])
        if("ct5" in district):
            trumpct5.add(tw["user"]["id"])
        if("mt1" in district):
            trumpmt1.add(tw["user"]["id"])
        if("ms1" in district):
            trumpms1.add(tw["user"]["id"])
        if("ms2" in district):
            trumpms2.add(tw["user"]["id"])
        if("ms3" in district):
            trumpms3.add(tw["user"]["id"])
        if("ms4" in district):
            trumpms4.add(tw["user"]["id"])
        if("pa1" in district):
            trumppa1.add(tw["user"]["id"])
        if("pa2" in district):
            trumppa2.add(tw["user"]["id"])
        if("pa3" in district):
            trumppa3.add(tw["user"]["id"])
        if("pa4" in district):
            trumppa4.add(tw["user"]["id"])
        if("pa5" in district):
            trumppa5.add(tw["user"]["id"])
        if("pa6" in district):
            trumppa6.add(tw["user"]["id"])
        if("pa7" in district):
            trumppa7.add(tw["user"]["id"])
        if("pa8" in district):
            trumppa8.add(tw["user"]["id"])
        if("pa9" in district):
            trumppa9.add(tw["user"]["id"])
        if("pa10" in district):
            trumppa10.add(tw["user"]["id"])
        if("pa11" in district):
            trumppa11.add(tw["user"]["id"])
        if("pa12" in district):
            trumppa12.add(tw["user"]["id"])
        if("pa13" in district):
            trumppa13.add(tw["user"]["id"])
        if("pa14" in district):
            trumppa14.add(tw["user"]["id"])
        if("pa15" in district):
            trumppa15.add(tw["user"]["id"])
        if("pa16" in district):
            trumppa16.add(tw["user"]["id"])
        if("pa17" in district):
            trumppa17.add(tw["user"]["id"])
        if("pa18" in district):
            trumppa18.add(tw["user"]["id"])
        if("oh1" in district):
            trumpoh1.add(tw["user"]["id"])
        if("oh2" in district):
            trumpoh2.add(tw["user"]["id"])
        if("oh3" in district):
            trumpoh3.add(tw["user"]["id"])
        if("oh4" in district):
            trumpoh4.add(tw["user"]["id"])
        if("oh5" in district):
            trumpoh5.add(tw["user"]["id"])
        if("oh6" in district):
            trumpoh6.add(tw["user"]["id"])
        if("oh7" in district):
            trumpoh7.add(tw["user"]["id"])
        if("oh8" in district):
            trumpoh8.add(tw["user"]["id"])
        if("oh9" in district):
            trumpoh9.add(tw["user"]["id"])
        if("oh10" in district):
            trumpoh10.add(tw["user"]["id"])
        if("oh11" in district):
            trumpoh11.add(tw["user"]["id"])
        if("oh12" in district):
            trumpoh12.add(tw["user"]["id"])
        if("oh13" in district):
            trumpoh13.add(tw["user"]["id"])
        if("oh14" in district):
            trumpoh14.add(tw["user"]["id"])
        if("oh15" in district):
            trumpoh15.add(tw["user"]["id"])
        if("oh16" in district):
            trumpoh16.add(tw["user"]["id"])
        if("fl1" in district):
            trumpfl1.add(tw["user"]["id"])
        if("fl2" in district):
            trumpfl2.add(tw["user"]["id"])
        if("fl3" in district):
            trumpfl3.add(tw["user"]["id"])
        if("fl4" in district):
            trumpfl4.add(tw["user"]["id"])
        if("fl5" in district):
            trumpfl5.add(tw["user"]["id"])
        if("fl6" in district):
            trumpfl6.add(tw["user"]["id"])
        if("fl7" in district):
            trumpfl7.add(tw["user"]["id"])
        if("fl8" in district):
            trumpfl8.add(tw["user"]["id"])
        if("fl9" in district):
            trumpfl9.add(tw["user"]["id"])
        if("fl10" in district):
            trumpfl10.add(tw["user"]["id"])
        if("fl11" in district):
            trumpfl11.add(tw["user"]["id"])
        if("fl12" in district):
            trumpfl12.add(tw["user"]["id"])
        if("fl13" in district):
            trumpfl13.add(tw["user"]["id"])
        if("fl14" in district):
            trumpfl14.add(tw["user"]["id"])
        if("fl15" in district):
            trumpfl15.add(tw["user"]["id"])
        if("fl16" in district):
            trumpfl16.add(tw["user"]["id"])
        if("fl17" in district):
            trumpfl17.add(tw["user"]["id"])
        if("fl18" in district):
            trumpfl18.add(tw["user"]["id"])
        if("fl19" in district):
            trumpfl19.add(tw["user"]["id"])
        if("fl20" in district):
            trumpfl20.add(tw["user"]["id"])
        if("fl21" in district):
            trumpfl21.add(tw["user"]["id"])
        if("fl22" in district):
            trumpfl22.add(tw["user"]["id"])
        if("fl23" in district):
            trumpfl23.add(tw["user"]["id"])
        if("fl24" in district):
            trumpfl24.add(tw["user"]["id"])
        if("fl25" in district):
            trumpfl25.add(tw["user"]["id"])
        if("fl26" in district):
            trumpfl26.add(tw["user"]["id"])
        if("fl27" in district):
            trumpfl27.add(tw["user"]["id"])
        if("wa1" in district):
            trumpwa1.add(tw["user"]["id"])
        if("wa2" in district):
            trumpwa2.add(tw["user"]["id"])
        if("wa3" in district):
            trumpwa3.add(tw["user"]["id"])
        if("wa4" in district):
            trumpwa4.add(tw["user"]["id"])
        if("wa5" in district):
            trumpwa5.add(tw["user"]["id"])
        if("wa6" in district):
            trumpwa6.add(tw["user"]["id"])
        if("wa7" in district):
            trumpwa7.add(tw["user"]["id"])
        if("wa8" in district):
            trumpwa8.add(tw["user"]["id"])
        if("wa9" in district):
            trumpwa9.add(tw["user"]["id"])
        if("wa10" in district):
            trumpwa10.add(tw["user"]["id"])
        if("hi1" in district):
            trumphi1.add(tw["user"]["id"])
        if("hi2" in district):
            trumphi2.add(tw["user"]["id"])
        if("nj1" in district):
            trumpnj1.add(tw["user"]["id"])
        if("nj2" in district):
            trumpnj2.add(tw["user"]["id"])
        if("nj3" in district):
            trumpnj3.add(tw["user"]["id"])
        if("nj4" in district):
            trumpnj4.add(tw["user"]["id"])
        if("nj5" in district):
            trumpnj5.add(tw["user"]["id"])
        if("nj6" in district):
            trumpnj6.add(tw["user"]["id"])
        if("nj7" in district):
            trumpnj7.add(tw["user"]["id"])
        if("nj8" in district):
            trumpnj8.add(tw["user"]["id"])
        if("nj9" in district):
            trumpnj9.add(tw["user"]["id"])
        if("nj10" in district):
            trumpnj10.add(tw["user"]["id"])
        if("nj11" in district):
            trumpnj11.add(tw["user"]["id"])
        if("nj12" in district):
            trumpnj12.add(tw["user"]["id"])
        if("ny1" in district):
            trumpny1.add(tw["user"]["id"])
        if("ny2" in district):
            trumpny2.add(tw["user"]["id"])
        if("ny3" in district):
            trumpny3.add(tw["user"]["id"])
        if("ny4" in district):
            trumpny4.add(tw["user"]["id"])
        if("ny5" in district):
            trumpny5.add(tw["user"]["id"])
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            trumpny6.add(tw["user"]["id"])
            trumpny7.add(tw["user"]["id"])
            trumpny8.add(tw["user"]["id"])
            trumpny9.add(tw["user"]["id"])
            trumpny10.add(tw["user"]["id"])
            trumpny11.add(tw["user"]["id"])
            trumpny12.add(tw["user"]["id"])
            trumpny13.add(tw["user"]["id"])
            trumpny14.add(tw["user"]["id"])
            trumpny15.add(tw["user"]["id"])
        if("ny16" in district):
            trumpny16.add(tw["user"]["id"])
        if("ny17" in district):
            trumpny17.add(tw["user"]["id"])
        if("ny18" in district):
            trumpny18.add(tw["user"]["id"])
        if("ny19" in district):
            trumpny19.add(tw["user"]["id"])
        if("ny20" in district):
            trumpny20.add(tw["user"]["id"])
        if("ny21" in district):
            trumpny21.add(tw["user"]["id"])
        if("ny22" in district):
            trumpny22.add(tw["user"]["id"])
        if("ny23" in district):
            trumpny23.add(tw["user"]["id"])
        if("ny24" in district):
            trumpny24.add(tw["user"]["id"])
        if("ny25" in district):
            trumpny25.add(tw["user"]["id"])
        if("ny26" in district):
            trumpny26.add(tw["user"]["id"])
        if("ny27" in district):
            trumpny27.add(tw["user"]["id"])
        if("ri1" in district):
            trumpri1.add(tw["user"]["id"])
        if("ri2" in district):
            trumpri2.add(tw["user"]["id"])
        if("mn1" in district):
            trumpmn1.add(tw["user"]["id"])
        if("mn2" in district):
            trumpmn2.add(tw["user"]["id"])
        if("mn3" in district):
            trumpmn3.add(tw["user"]["id"])
        if("mn4" in district):
            trumpmn4.add(tw["user"]["id"])
        if("mn5" in district):
            trumpmn5.add(tw["user"]["id"])
        if("mn6" in district):
            trumpmn6.add(tw["user"]["id"])
        if("mn7" in district):
            trumpmn7.add(tw["user"]["id"])
        if("mn8" in district):
            trumpmn8.add(tw["user"]["id"])
        if("mi1" in district):
            trumpmi1.add(tw["user"]["id"])
        if("mi2" in district):
            trumpmi2.add(tw["user"]["id"])
        if("mi3" in district):
            trumpmi3.add(tw["user"]["id"])
        if("mi4" in district):
            trumpmi4.add(tw["user"]["id"])
        if("mi5" in district):
            trumpmi5.add(tw["user"]["id"])
        if("mi6" in district):
            trumpmi6.add(tw["user"]["id"])
        if("mi7" in district):
            trumpmi7.add(tw["user"]["id"])
        if("mi8" in district):
            trumpmi8.add(tw["user"]["id"])
        if("mi9" in district):
            trumpmi9.add(tw["user"]["id"])
        if("mi10" in district):
            trumpmi10.add(tw["user"]["id"])
        if("mi11" in district):
            trumpmi11.add(tw["user"]["id"])
        if("mi12" in district):
            trumpmi12.add(tw["user"]["id"])
        if("mi13" in district):
            trumpmi13.add(tw["user"]["id"])
        if("mi14" in district):
            trumpmi14.add(tw["user"]["id"])
        if("wi1" in district):
            trumpwi1.add(tw["user"]["id"])
        if("wi2" in district):
            trumpwi2.add(tw["user"]["id"])
        if("wi3" in district):
            trumpwi3.add(tw["user"]["id"])
        if("wi4" in district):
            trumpwi4.add(tw["user"]["id"])
        if("wi5" in district):
            trumpwi5.add(tw["user"]["id"])
        if("wi6" in district):
            trumpwi6.add(tw["user"]["id"])
        if("wi7" in district):
            trumpwi7.add(tw["user"]["id"])
        if("wi8" in district):
            trumpwi8.add(tw["user"]["id"])
        if("or1" in district):
            trumpor1.add(tw["user"]["id"])
        if("or2" in district):
            trumpor2.add(tw["user"]["id"])
        if("or3" in district):
            trumpor3.add(tw["user"]["id"])
        if("or4" in district):
            trumpor4.add(tw["user"]["id"])
        if("or5" in district):
            trumpor5.add(tw["user"]["id"])
        if("md1" in district):
            trumpmd1.add(tw["user"]["id"])
        if("md2" in district):
            trumpmd2.add(tw["user"]["id"])
        if("md3" in district):
            trumpmd3.add(tw["user"]["id"])
        if("md4" in district):
            trumpmd4.add(tw["user"]["id"])
        if("md5" in district):
            trumpmd5.add(tw["user"]["id"])
        if("md6" in district):
            trumpmd6.add(tw["user"]["id"])
        if("md7" in district):
            trumpmd7.add(tw["user"]["id"])
        if("md8" in district):
            trumpmd8.add(tw["user"]["id"])
        if("ma1" in district):
            trumpma1.add(tw["user"]["id"])
        if("ma2" in district):
            trumpma2.add(tw["user"]["id"])
        if("ma3" in district):
            trumpma3.add(tw["user"]["id"])
        if("ma4" in district):
            trumpma4.add(tw["user"]["id"])
        if("ma5" in district):
            trumpma5.add(tw["user"]["id"])
        if("ma6" in district):
            trumpma6.add(tw["user"]["id"])
        if("ma7" in district):
            trumpma7.add(tw["user"]["id"])
        if("ma8" in district):
            trumpma8.add(tw["user"]["id"])
        if("ma9" in district):
            trumpma9.add(tw["user"]["id"])
        if("me1" in district):
            trumpme1.add(tw["user"]["id"])
        if("me2" in district):
            trumpme2.add(tw["user"]["id"])
        if("id1" in district):
            trumpid1.add(tw["user"]["id"])
        if("id2" in district):
            trumpid2.add(tw["user"]["id"])
        if("nc1" in district):
            trumpnc1.add(tw["user"]["id"])
        if("nc2" in district):
            trumpnc2.add(tw["user"]["id"])
        if("nc3" in district):
            trumpnc3.add(tw["user"]["id"])
        if("nc4" in district):
            trumpnc4.add(tw["user"]["id"])
        if("nc5" in district):
            trumpnc5.add(tw["user"]["id"])
        if("nc6" in district):
            trumpnc6.add(tw["user"]["id"])
        if("nc7" in district):
            trumpnc7.add(tw["user"]["id"])
        if("nc8" in district):
            trumpnc8.add(tw["user"]["id"])
        if("nc9" in district):
            trumpnc9.add(tw["user"]["id"])
        if("nc10" in district):
            trumpnc10.add(tw["user"]["id"])
        if("nc11" in district):
            trumpnc11.add(tw["user"]["id"])
        if("nc12" in district):
            trumpnc12.add(tw["user"]["id"])
        if("nc13" in district):
            trumpnc13.add(tw["user"]["id"])
        if("nh1" in district):
            trumpnh1.add(tw["user"]["id"])
        if("nh2" in district):
            trumpnh2.add(tw["user"]["id"])
        if("nv1" in district):
            trumpnv1.add(tw["user"]["id"])
        if("nv2" in district):
            trumpnv2.add(tw["user"]["id"])
        if("nv3" in district):
            trumpnv3.add(tw["user"]["id"])
        if("nv4" in district):
            trumpnv4.add(tw["user"]["id"])
        if("co1" in district):
            trumpco1.add(tw["user"]["id"])
        if("co2" in district):
            trumpco2.add(tw["user"]["id"])
        if("co3" in district):
            trumpco3.add(tw["user"]["id"])
        if("co4" in district):
            trumpco4.add(tw["user"]["id"])
        if("co5" in district):
            trumpco5.add(tw["user"]["id"])
        if("co6" in district):
            trumpco6.add(tw["user"]["id"])
        if("co7" in district):
            trumpco7.add(tw["user"]["id"])
        if("nm1" in district):
            trumpnm1.add(tw["user"]["id"])
        if("nm2" in district):
            trumpnm2.add(tw["user"]["id"])
        if("nm3" in district):
            trumpnm3.add(tw["user"]["id"])
        if("az1" in district):
            trumpaz1.add(tw["user"]["id"])
        if("az2" in district):
            trumpaz2.add(tw["user"]["id"])
        if("az3" in district):
            trumpaz3.add(tw["user"]["id"])
        if("az4" in district):
            trumpaz4.add(tw["user"]["id"])
        if("az5" in district):
            trumpaz5.add(tw["user"]["id"])
        if("az6" in district):
            trumpaz6.add(tw["user"]["id"])
        if("az7" in district):
            trumpaz7.add(tw["user"]["id"])
        if("az8" in district):
            trumpaz8.add(tw["user"]["id"])
        if("az9" in district):
            trumpaz9.add(tw["user"]["id"])
        if("ga1" in district):
            trumpga1.add(tw["user"]["id"])
        if("ga2" in district):
            trumpga2.add(tw["user"]["id"])
        if("ga3" in district):
            trumpga3.add(tw["user"]["id"])
        if("ga4" in district):
            trumpga4.add(tw["user"]["id"])
        if("ga5" in district):
            trumpga5.add(tw["user"]["id"])
        if("ga6" in district):
            trumpga6.add(tw["user"]["id"])
        if("ga7" in district):
            trumpga7.add(tw["user"]["id"])
        if("ga8" in district):
            trumpga8.add(tw["user"]["id"])
        if("ga9" in district):
            trumpga9.add(tw["user"]["id"])
        if("ga10" in district):
            trumpga10.add(tw["user"]["id"])
        if("ga11" in district):
            trumpga11.add(tw["user"]["id"])
        if("ga12" in district):
            trumpga12.add(tw["user"]["id"])
        if("ga13" in district):
            trumpga13.add(tw["user"]["id"])
        if("ga14" in district):
            trumpga14.add(tw["user"]["id"])
        if("tx1" in district):
            trumptx1.add(tw["user"]["id"])
        if("tx2" in district):
            trumptx2.add(tw["user"]["id"])
        if("tx3" in district):
            trumptx3.add(tw["user"]["id"])
        if("tx4" in district):
            trumptx4.add(tw["user"]["id"])
        if("tx5" in district):
            trumptx5.add(tw["user"]["id"])
        if("tx6" in district):
            trumptx6.add(tw["user"]["id"])
        if("tx7" in district):
            trumptx7.add(tw["user"]["id"])
        if("tx8" in district):
            trumptx8.add(tw["user"]["id"])
        if("tx9" in district):
            trumptx9.add(tw["user"]["id"])
        if("tx10" in district):
            trumptx10.add(tw["user"]["id"])
        if("tx11" in district):
            trumptx11.add(tw["user"]["id"])
        if("tx12" in district):
            trumptx12.add(tw["user"]["id"])
        if("tx13" in district):
            trumptx13.add(tw["user"]["id"])
        if("tx14" in district):
            trumptx14.add(tw["user"]["id"])
        if("tx15" in district):
            trumptx15.add(tw["user"]["id"])
        if("tx16" in district):
            trumptx16.add(tw["user"]["id"])
        if("tx17" in district):
            trumptx17.add(tw["user"]["id"])
        if("tx18" in district):
            trumptx18.add(tw["user"]["id"])
        if("tx19" in district):
            trumptx19.add(tw["user"]["id"])
        if("tx20" in district):
            trumptx20.add(tw["user"]["id"])
        if("tx21" in district):
            trumptx21.add(tw["user"]["id"])
        if("tx22" in district):
            trumptx22.add(tw["user"]["id"])
        if("tx23" in district):
            trumptx23.add(tw["user"]["id"])
        if("tx24" in district):
            trumptx24.add(tw["user"]["id"])
        if("tx25" in district):
            trumptx25.add(tw["user"]["id"])
        if("tx26" in district):
            trumptx26.add(tw["user"]["id"])
        if("tx27" in district):
            trumptx27.add(tw["user"]["id"])
        if("tx28" in district):
            trumptx28.add(tw["user"]["id"])
        if("tx29" in district):
            trumptx29.add(tw["user"]["id"])
        if("tx30" in district):
            trumptx30.add(tw["user"]["id"])
        if("tx31" in district):
            trumptx31.add(tw["user"]["id"])
        if("tx32" in district):
            trumptx32.add(tw["user"]["id"])
        if("tx33" in district):
            trumptx33.add(tw["user"]["id"])
        if("tx34" in district):
            trumptx34.add(tw["user"]["id"])
        if("tx35" in district):
            trumptx35.add(tw["user"]["id"])
        if("tx36" in district):
            trumptx36.add(tw["user"]["id"])
        if("in1" in district):
            trumpin1.add(tw["user"]["id"])
        if("in2" in district):
            trumpin2.add(tw["user"]["id"])
        if("in3" in district):
            trumpin3.add(tw["user"]["id"])
        if("in4" in district):
            trumpin4.add(tw["user"]["id"])
        if("in5" in district):
            trumpin5.add(tw["user"]["id"])
        if("in6" in district):
            trumpin6.add(tw["user"]["id"])
        if("in7" in district):
            trumpin7.add(tw["user"]["id"])
        if("in8" in district):
            trumpin8.add(tw["user"]["id"])
        if("in9" in district):
            trumpin9.add(tw["user"]["id"])
        if("va1" in district):
            trumpva1.add(tw["user"]["id"])
        if("va2" in district):
            trumpva2.add(tw["user"]["id"])
        if("va3" in district):
            trumpva3.add(tw["user"]["id"])
        if("va4" in district):
            trumpva4.add(tw["user"]["id"])
        if("va5" in district):
            trumpva5.add(tw["user"]["id"])
        if("va6" in district):
            trumpva6.add(tw["user"]["id"])
        if("va7" in district):
            trumpva7.add(tw["user"]["id"])
        if("va8" in district):
            trumpva8.add(tw["user"]["id"])
        if("va9" in district):
            trumpva9.add(tw["user"]["id"])
        if("va10" in district):
            trumpva10.add(tw["user"]["id"])
        if("va11" in district):
            trumpva11.add(tw["user"]["id"])
        if("il1" in district):
            trumpil1.add(tw["user"]["id"])
        if("il2" in district):
            trumpil2.add(tw["user"]["id"])
        if("il3" in district):
            trumpil3.add(tw["user"]["id"])
        if("il4" in district):
            trumpil4.add(tw["user"]["id"])
        if("il5" in district):
            trumpil5.add(tw["user"]["id"])
        if("il6" in district):
            trumpil6.add(tw["user"]["id"])
        if("il7" in district):
            trumpil7.add(tw["user"]["id"])
        if("il8" in district):
            trumpil8.add(tw["user"]["id"])
        if("il9" in district):
            trumpil9.add(tw["user"]["id"])
        if("il10" in district):
            trumpil10.add(tw["user"]["id"])
        if("il11" in district):
            trumpil11.add(tw["user"]["id"])
        if("il12" in district):
            trumpil12.add(tw["user"]["id"])
        if("il13" in district):
            trumpil13.add(tw["user"]["id"])
        if("il14" in district):
            trumpil14.add(tw["user"]["id"])
        if("il15" in district):
            trumpil15.add(tw["user"]["id"])
        if("il16" in district):
            trumpil16.add(tw["user"]["id"])
        if("il17" in district):
            trumpil17.add(tw["user"]["id"])
        if("il18" in district):
            trumpil18.add(tw["user"]["id"])
        if("de1" in district):
            trumpde1.add(tw["user"]["id"])
        if("vt1" in district):
            trumpvt1.add(tw["user"]["id"])
        if("ut1" in district):
            trumput1.add(tw["user"]["id"])
        if("ut2" in district):
            trumput2.add(tw["user"]["id"])
        if("ut3" in district):
            trumput3.add(tw["user"]["id"])
        if("ut4" in district):
            trumput4.add(tw["user"]["id"])
        if("ne1" in district):
            trumpne1.add(tw["user"]["id"])
        if("ne2" in district):
            trumpne2.add(tw["user"]["id"])
        if("ne3" in district):
            trumpne3.add(tw["user"]["id"])
        if("ak1" in district):
            trumpak1.add(tw["user"]["id"])
        if("wy1" in district):
            trumpwy1.add(tw["user"]["id"])
        if("al1" in district):
            trumpal1.add(tw["user"]["id"])
        if("al2" in district):
            trumpal2.add(tw["user"]["id"])
        if("al3" in district):
            trumpal3.add(tw["user"]["id"])
        if("al4" in district):
            trumpal4.add(tw["user"]["id"])
        if("al5" in district):
            trumpal5.add(tw["user"]["id"])
        if("al6" in district):
            trumpal6.add(tw["user"]["id"])
        if("al7" in district):
            trumpal7.add(tw["user"]["id"])
        if("tn1" in district):
            trumptn1.add(tw["user"]["id"])
        if("tn2" in district):
            trumptn2.add(tw["user"]["id"])
        if("tn3" in district):
            trumptn3.add(tw["user"]["id"])
        if("tn4" in district):
            trumptn4.add(tw["user"]["id"])
        if("tn5" in district):
            trumptn5.add(tw["user"]["id"])
        if("tn6" in district):
            trumptn6.add(tw["user"]["id"])
        if("tn7" in district):
            trumptn7.add(tw["user"]["id"])
        if("tn8" in district):
            trumptn8.add(tw["user"]["id"])
        if("tn9" in district):
            trumptn9.add(tw["user"]["id"])
        if("nd1" in district):
            trumpnd1.add(tw["user"]["id"])
        if("sd1" in district):
            trumpsd1.add(tw["user"]["id"])
        if("wv1" in district):
            trumpwv1.add(tw["user"]["id"])
        if("wv2" in district):
            trumpwv2.add(tw["user"]["id"])
        if("wv3" in district):
            trumpwv3.add(tw["user"]["id"])
        if("ar1" in district):
            trumpar1.add(tw["user"]["id"])
        if("ar2" in district):
            trumpar2.add(tw["user"]["id"])
        if("ar3" in district):
            trumpar3.add(tw["user"]["id"])
        if("ar4" in district):
            trumpar4.add(tw["user"]["id"])
    district = sortloc(["#biden2020", "#voteblue"], tw["user"]["location"], tw["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            bidenmo1.add(tw["user"]["id"])
        if("mo2" in district):
            bidenmo2.add(tw["user"]["id"])
        if("mo3" in district):
            bidenmo3.add(tw["user"]["id"])
        if("mo4" in district):
            bidenmo4.add(tw["user"]["id"])
        if("mo5" in district):
            bidenmo5.add(tw["user"]["id"])
        if("mo6" in district):
            bidenmo6.add(tw["user"]["id"])
        if("mo7" in district):
            bidenmo7.add(tw["user"]["id"])
        if("mo8" in district):
            bidenmo8.add(tw["user"]["id"])
        if("sc1" in district):
            bidensc1.add(tw["user"]["id"])
        if("sc2" in district):
            bidensc2.add(tw["user"]["id"])
        if("sc3" in district):
            bidensc3.add(tw["user"]["id"])
        if("sc4" in district):
            bidensc4.add(tw["user"]["id"])
        if("sc5" in district):
            bidensc5.add(tw["user"]["id"])
        if("sc6" in district):
            bidensc6.add(tw["user"]["id"])
        if("sc7" in district):
            bidensc7.add(tw["user"]["id"])
        if("ky1" in district):
            bidenky1.add(tw["user"]["id"])
        if("ky2" in district):
            bidenky2.add(tw["user"]["id"])
        if("ky3" in district):
            bidenky3.add(tw["user"]["id"])
        if("ky4" in district):
            bidenky4.add(tw["user"]["id"])
        if("ky5" in district):
            bidenky5.add(tw["user"]["id"])
        if("ky6" in district):
            bidenky6.add(tw["user"]["id"])
        if("ok1" in district):
            bidenok1.add(tw["user"]["id"])
        if("ok2" in district):
            bidenok2.add(tw["user"]["id"])
        if("ok3" in district):
            bidenok3.add(tw["user"]["id"])
        if("ok4" in district):
            bidenok4.add(tw["user"]["id"])
        if("ok5" in district):
            bidenok5.add(tw["user"]["id"])
        if("ia1" in district):
            bidenia1.add(tw["user"]["id"])
        if("ia2" in district):
            bidenia2.add(tw["user"]["id"])
        if("ia3" in district):
            bidenia3.add(tw["user"]["id"])
        if("ia4" in district):
            bidenia4.add(tw["user"]["id"])
        if("ks1" in district):
            bidenks1.add(tw["user"]["id"])
        if("ks2" in district):
            bidenks2.add(tw["user"]["id"])
        if("ks3" in district):
            bidenks3.add(tw["user"]["id"])
        if("ks4" in district):
            bidenks4.add(tw["user"]["id"])
        if("ca1" in district):
            bidenca1.add(tw["user"]["id"])
        if("ca2" in district):
            bidenca2.add(tw["user"]["id"])
        if("ca3" in district):
            bidenca3.add(tw["user"]["id"])
        if("ca4" in district):
            bidenca4.add(tw["user"]["id"])
        if("ca5" in district):
            bidenca5.add(tw["user"]["id"])
        if("ca6" in district):
            bidenca6.add(tw["user"]["id"])
        if("ca7" in district):
            bidenca7.add(tw["user"]["id"])
        if("ca8" in district):
            bidenca8.add(tw["user"]["id"])
        if("ca9" in district):
            bidenca9.add(tw["user"]["id"])
        if("ca10" in district):
            bidenca10.add(tw["user"]["id"])
        if("ca11" in district):
            bidenca11.add(tw["user"]["id"])
        if("ca12" in district):
            bidenca12.add(tw["user"]["id"])
        if("ca13" in district):
            bidenca13.add(tw["user"]["id"])
        if("ca14" in district):
            bidenca14.add(tw["user"]["id"])
        if("ca15" in district):
            bidenca15.add(tw["user"]["id"])
        if("ca16" in district):
            bidenca16.add(tw["user"]["id"])
        if("ca17" in district):
            bidenca17.add(tw["user"]["id"])
        if("ca18" in district):
            bidenca18.add(tw["user"]["id"])
        if("ca19" in district):
            bidenca19.add(tw["user"]["id"])
        if("ca20" in district):
            bidenca20.add(tw["user"]["id"])
        if("ca21" in district):
            bidenca21.add(tw["user"]["id"])
        if("ca22" in district):
            bidenca22.add(tw["user"]["id"])
        if("ca23" in district):
            bidenca23.add(tw["user"]["id"])
        if("ca24" in district):
            bidenca24.add(tw["user"]["id"])
        if("ca25" in district):
            bidenca25.add(tw["user"]["id"])
        if("ca26" in district):
            bidenca26.add(tw["user"]["id"])
        if("ca27" in district):
            bidenca27.add(tw["user"]["id"])
        if("ca28" in district):
            bidenca28.add(tw["user"]["id"])
        if("ca29" in district):
            bidenca29.add(tw["user"]["id"])
        if("ca30" in district):
            bidenca30.add(tw["user"]["id"])
        if("ca31" in district):
            bidenca31.add(tw["user"]["id"])
        if("ca32" in district):
            bidenca32.add(tw["user"]["id"])
        if("ca33" in district):
            bidenca33.add(tw["user"]["id"])
        if("ca34" in district):
            bidenca34.add(tw["user"]["id"])
        if("ca35" in district):
            bidenca35.add(tw["user"]["id"])
        if("ca36" in district):
            bidenca36.add(tw["user"]["id"])
        if("ca37" in district):
            bidenca37.add(tw["user"]["id"])
        if("ca38" in district):
            bidenca38.add(tw["user"]["id"])
        if("ca39" in district):
            bidenca39.add(tw["user"]["id"])
        if("ca40" in district):
            bidenca40.add(tw["user"]["id"])
        if("ca41" in district):
            bidenca41.add(tw["user"]["id"])
        if("ca42" in district):
            bidenca42.add(tw["user"]["id"])
        if("ca43" in district):
            bidenca43.add(tw["user"]["id"])
        if("ca44" in district):
            bidenca44.add(tw["user"]["id"])
        if("ca45" in district):
            bidenca45.add(tw["user"]["id"])
        if("ca46" in district):
            bidenca46.add(tw["user"]["id"])
        if("ca47" in district):
            bidenca47.add(tw["user"]["id"])
        if("ca48" in district):
            bidenca48.add(tw["user"]["id"])
        if("ca49" in district):
            bidenca49.add(tw["user"]["id"])
        if("ca50" in district):
            bidenca50.add(tw["user"]["id"])
        if("ca51" in district):
            bidenca51.add(tw["user"]["id"])
        if("ca52" in district):
            bidenca52.add(tw["user"]["id"])
        if("ca53" in district):
            bidenca53.add(tw["user"]["id"])
        if("la1" in district):
            bidenla1.add(tw["user"]["id"])
        if("la2" in district):
            bidenla2.add(tw["user"]["id"])
        if("la3" in district):
            bidenla3.add(tw["user"]["id"])
        if("la4" in district):
            bidenla4.add(tw["user"]["id"])
        if("la5" in district):
            bidenla5.add(tw["user"]["id"])
        if("la6" in district):
            bidenla6.add(tw["user"]["id"])
        if("ct1" in district):
            bidenct1.add(tw["user"]["id"])
        if("ct2" in district):
            bidenct2.add(tw["user"]["id"])
        if("ct3" in district):
            bidenct3.add(tw["user"]["id"])
        if("ct4" in district):
            bidenct4.add(tw["user"]["id"])
        if("ct5" in district):
            bidenct5.add(tw["user"]["id"])
        if("mt1" in district):
            bidenmt1.add(tw["user"]["id"])
        if("ms1" in district):
            bidenms1.add(tw["user"]["id"])
        if("ms2" in district):
            bidenms2.add(tw["user"]["id"])
        if("ms3" in district):
            bidenms3.add(tw["user"]["id"])
        if("ms4" in district):
            bidenms4.add(tw["user"]["id"])
        if("pa1" in district):
            bidenpa1.add(tw["user"]["id"])
        if("pa2" in district):
            bidenpa2.add(tw["user"]["id"])
        if("pa3" in district):
            bidenpa3.add(tw["user"]["id"])
        if("pa4" in district):
            bidenpa4.add(tw["user"]["id"])
        if("pa5" in district):
            bidenpa5.add(tw["user"]["id"])
        if("pa6" in district):
            bidenpa6.add(tw["user"]["id"])
        if("pa7" in district):
            bidenpa7.add(tw["user"]["id"])
        if("pa8" in district):
            bidenpa8.add(tw["user"]["id"])
        if("pa9" in district):
            bidenpa9.add(tw["user"]["id"])
        if("pa10" in district):
            bidenpa10.add(tw["user"]["id"])
        if("pa11" in district):
            bidenpa11.add(tw["user"]["id"])
        if("pa12" in district):
            bidenpa12.add(tw["user"]["id"])
        if("pa13" in district):
            bidenpa13.add(tw["user"]["id"])
        if("pa14" in district):
            bidenpa14.add(tw["user"]["id"])
        if("pa15" in district):
            bidenpa15.add(tw["user"]["id"])
        if("pa16" in district):
            bidenpa16.add(tw["user"]["id"])
        if("pa17" in district):
            bidenpa17.add(tw["user"]["id"])
        if("pa18" in district):
            bidenpa18.add(tw["user"]["id"])
        if("oh1" in district):
            bidenoh1.add(tw["user"]["id"])
        if("oh2" in district):
            bidenoh2.add(tw["user"]["id"])
        if("oh3" in district):
            bidenoh3.add(tw["user"]["id"])
        if("oh4" in district):
            bidenoh4.add(tw["user"]["id"])
        if("oh5" in district):
            bidenoh5.add(tw["user"]["id"])
        if("oh6" in district):
            bidenoh6.add(tw["user"]["id"])
        if("oh7" in district):
            bidenoh7.add(tw["user"]["id"])
        if("oh8" in district):
            bidenoh8.add(tw["user"]["id"])
        if("oh9" in district):
            bidenoh9.add(tw["user"]["id"])
        if("oh10" in district):
            bidenoh10.add(tw["user"]["id"])
        if("oh11" in district):
            bidenoh11.add(tw["user"]["id"])
        if("oh12" in district):
            bidenoh12.add(tw["user"]["id"])
        if("oh13" in district):
            bidenoh13.add(tw["user"]["id"])
        if("oh14" in district):
            bidenoh14.add(tw["user"]["id"])
        if("oh15" in district):
            bidenoh15.add(tw["user"]["id"])
        if("oh16" in district):
            bidenoh16.add(tw["user"]["id"])
        if("fl1" in district):
            bidenfl1.add(tw["user"]["id"])
        if("fl2" in district):
            bidenfl2.add(tw["user"]["id"])
        if("fl3" in district):
            bidenfl3.add(tw["user"]["id"])
        if("fl4" in district):
            bidenfl4.add(tw["user"]["id"])
        if("fl5" in district):
            bidenfl5.add(tw["user"]["id"])
        if("fl6" in district):
            bidenfl6.add(tw["user"]["id"])
        if("fl7" in district):
            bidenfl7.add(tw["user"]["id"])
        if("fl8" in district):
            bidenfl8.add(tw["user"]["id"])
        if("fl9" in district):
            bidenfl9.add(tw["user"]["id"])
        if("fl10" in district):
            bidenfl10.add(tw["user"]["id"])
        if("fl11" in district):
            bidenfl11.add(tw["user"]["id"])
        if("fl12" in district):
            bidenfl12.add(tw["user"]["id"])
        if("fl13" in district):
            bidenfl13.add(tw["user"]["id"])
        if("fl14" in district):
            bidenfl14.add(tw["user"]["id"])
        if("fl15" in district):
            bidenfl15.add(tw["user"]["id"])
        if("fl16" in district):
            bidenfl16.add(tw["user"]["id"])
        if("fl17" in district):
            bidenfl17.add(tw["user"]["id"])
        if("fl18" in district):
            bidenfl18.add(tw["user"]["id"])
        if("fl19" in district):
            bidenfl19.add(tw["user"]["id"])
        if("fl20" in district):
            bidenfl20.add(tw["user"]["id"])
        if("fl21" in district):
            bidenfl21.add(tw["user"]["id"])
        if("fl22" in district):
            bidenfl22.add(tw["user"]["id"])
        if("fl23" in district):
            bidenfl23.add(tw["user"]["id"])
        if("fl24" in district):
            bidenfl24.add(tw["user"]["id"])
        if("fl25" in district):
            bidenfl25.add(tw["user"]["id"])
        if("fl26" in district):
            bidenfl26.add(tw["user"]["id"])
        if("fl27" in district):
            bidenfl27.add(tw["user"]["id"])
        if("wa1" in district):
            bidenwa1.add(tw["user"]["id"])
        if("wa2" in district):
            bidenwa2.add(tw["user"]["id"])
        if("wa3" in district):
            bidenwa3.add(tw["user"]["id"])
        if("wa4" in district):
            bidenwa4.add(tw["user"]["id"])
        if("wa5" in district):
            bidenwa5.add(tw["user"]["id"])
        if("wa6" in district):
            bidenwa6.add(tw["user"]["id"])
        if("wa7" in district):
            bidenwa7.add(tw["user"]["id"])
        if("wa8" in district):
            bidenwa8.add(tw["user"]["id"])
        if("wa9" in district):
            bidenwa9.add(tw["user"]["id"])
        if("wa10" in district):
            bidenwa10.add(tw["user"]["id"])
        if("hi1" in district):
            bidenhi1.add(tw["user"]["id"])
        if("hi2" in district):
            bidenhi2.add(tw["user"]["id"])
        if("nj1" in district):
            bidennj1.add(tw["user"]["id"])
        if("nj2" in district):
            bidennj2.add(tw["user"]["id"])
        if("nj3" in district):
            bidennj3.add(tw["user"]["id"])
        if("nj4" in district):
            bidennj4.add(tw["user"]["id"])
        if("nj5" in district):
            bidennj5.add(tw["user"]["id"])
        if("nj6" in district):
            bidennj6.add(tw["user"]["id"])
        if("nj7" in district):
            bidennj7.add(tw["user"]["id"])
        if("nj8" in district):
            bidennj8.add(tw["user"]["id"])
        if("nj9" in district):
            bidennj9.add(tw["user"]["id"])
        if("nj10" in district):
            bidennj10.add(tw["user"]["id"])
        if("nj11" in district):
            bidennj11.add(tw["user"]["id"])
        if("nj12" in district):
            bidennj12.add(tw["user"]["id"])
        if("ny1" in district):
            bidenny1.add(tw["user"]["id"])
        if("ny2" in district):
            bidenny2.add(tw["user"]["id"])
        if("ny3" in district):
            bidenny3.add(tw["user"]["id"])
        if("ny4" in district):
            bidenny4.add(tw["user"]["id"])
        if("ny5" in district):
            bidenny5.add(tw["user"]["id"])
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            bidenny6.add(tw["user"]["id"])
            bidenny7.add(tw["user"]["id"])
            bidenny8.add(tw["user"]["id"])
            bidenny9.add(tw["user"]["id"])
            bidenny10.add(tw["user"]["id"])
            bidenny11.add(tw["user"]["id"])
            bidenny12.add(tw["user"]["id"])
            bidenny13.add(tw["user"]["id"])
            bidenny14.add(tw["user"]["id"])
            bidenny15.add(tw["user"]["id"])
        if("ny16" in district):
            bidenny16.add(tw["user"]["id"])
        if("ny17" in district):
            bidenny17.add(tw["user"]["id"])
        if("ny18" in district):
            bidenny18.add(tw["user"]["id"])
        if("ny19" in district):
            bidenny19.add(tw["user"]["id"])
        if("ny20" in district):
            bidenny20.add(tw["user"]["id"])
        if("ny21" in district):
            bidenny21.add(tw["user"]["id"])
        if("ny22" in district):
            bidenny22.add(tw["user"]["id"])
        if("ny23" in district):
            bidenny23.add(tw["user"]["id"])
        if("ny24" in district):
            bidenny24.add(tw["user"]["id"])
        if("ny25" in district):
            bidenny25.add(tw["user"]["id"])
        if("ny26" in district):
            bidenny26.add(tw["user"]["id"])
        if("ny27" in district):
            bidenny27.add(tw["user"]["id"])
        if("ri1" in district):
            bidenri1.add(tw["user"]["id"])
        if("ri2" in district):
            bidenri2.add(tw["user"]["id"])
        if("mn1" in district):
            bidenmn1.add(tw["user"]["id"])
        if("mn2" in district):
            bidenmn2.add(tw["user"]["id"])
        if("mn3" in district):
            bidenmn3.add(tw["user"]["id"])
        if("mn4" in district):
            bidenmn4.add(tw["user"]["id"])
        if("mn5" in district):
            bidenmn5.add(tw["user"]["id"])
        if("mn6" in district):
            bidenmn6.add(tw["user"]["id"])
        if("mn7" in district):
            bidenmn7.add(tw["user"]["id"])
        if("mn8" in district):
            bidenmn8.add(tw["user"]["id"])
        if("mi1" in district):
            bidenmi1.add(tw["user"]["id"])
        if("mi2" in district):
            bidenmi2.add(tw["user"]["id"])
        if("mi3" in district):
            bidenmi3.add(tw["user"]["id"])
        if("mi4" in district):
            bidenmi4.add(tw["user"]["id"])
        if("mi5" in district):
            bidenmi5.add(tw["user"]["id"])
        if("mi6" in district):
            bidenmi6.add(tw["user"]["id"])
        if("mi7" in district):
            bidenmi7.add(tw["user"]["id"])
        if("mi8" in district):
            bidenmi8.add(tw["user"]["id"])
        if("mi9" in district):
            bidenmi9.add(tw["user"]["id"])
        if("mi10" in district):
            bidenmi10.add(tw["user"]["id"])
        if("mi11" in district):
            bidenmi11.add(tw["user"]["id"])
        if("mi12" in district):
            bidenmi12.add(tw["user"]["id"])
        if("mi13" in district):
            bidenmi13.add(tw["user"]["id"])
        if("mi14" in district):
            bidenmi14.add(tw["user"]["id"])
        if("wi1" in district):
            bidenwi1.add(tw["user"]["id"])
        if("wi2" in district):
            bidenwi2.add(tw["user"]["id"])
        if("wi3" in district):
            bidenwi3.add(tw["user"]["id"])
        if("wi4" in district):
            bidenwi4.add(tw["user"]["id"])
        if("wi5" in district):
            bidenwi5.add(tw["user"]["id"])
        if("wi6" in district):
            bidenwi6.add(tw["user"]["id"])
        if("wi7" in district):
            bidenwi7.add(tw["user"]["id"])
        if("wi8" in district):
            bidenwi8.add(tw["user"]["id"])
        if("or1" in district):
            bidenor1.add(tw["user"]["id"])
        if("or2" in district):
            bidenor2.add(tw["user"]["id"])
        if("or3" in district):
            bidenor3.add(tw["user"]["id"])
        if("or4" in district):
            bidenor4.add(tw["user"]["id"])
        if("or5" in district):
            bidenor5.add(tw["user"]["id"])
        if("md1" in district):
            bidenmd1.add(tw["user"]["id"])
        if("md2" in district):
            bidenmd2.add(tw["user"]["id"])
        if("md3" in district):
            bidenmd3.add(tw["user"]["id"])
        if("md4" in district):
            bidenmd4.add(tw["user"]["id"])
        if("md5" in district):
            bidenmd5.add(tw["user"]["id"])
        if("md6" in district):
            bidenmd6.add(tw["user"]["id"])
        if("md7" in district):
            bidenmd7.add(tw["user"]["id"])
        if("md8" in district):
            bidenmd8.add(tw["user"]["id"])
        if("ma1" in district):
            bidenma1.add(tw["user"]["id"])
        if("ma2" in district):
            bidenma2.add(tw["user"]["id"])
        if("ma3" in district):
            bidenma3.add(tw["user"]["id"])
        if("ma4" in district):
            bidenma4.add(tw["user"]["id"])
        if("ma5" in district):
            bidenma5.add(tw["user"]["id"])
        if("ma6" in district):
            bidenma6.add(tw["user"]["id"])
        if("ma7" in district):
            bidenma7.add(tw["user"]["id"])
        if("ma8" in district):
            bidenma8.add(tw["user"]["id"])
        if("ma9" in district):
            bidenma9.add(tw["user"]["id"])
        if("me1" in district):
            bidenme1.add(tw["user"]["id"])
        if("me2" in district):
            bidenme2.add(tw["user"]["id"])
        if("id1" in district):
            bidenid1.add(tw["user"]["id"])
        if("id2" in district):
            bidenid2.add(tw["user"]["id"])
        if("nc1" in district):
            bidennc1.add(tw["user"]["id"])
        if("nc2" in district):
            bidennc2.add(tw["user"]["id"])
        if("nc3" in district):
            bidennc3.add(tw["user"]["id"])
        if("nc4" in district):
            bidennc4.add(tw["user"]["id"])
        if("nc5" in district):
            bidennc5.add(tw["user"]["id"])
        if("nc6" in district):
            bidennc6.add(tw["user"]["id"])
        if("nc7" in district):
            bidennc7.add(tw["user"]["id"])
        if("nc8" in district):
            bidennc8.add(tw["user"]["id"])
        if("nc9" in district):
            bidennc9.add(tw["user"]["id"])
        if("nc10" in district):
            bidennc10.add(tw["user"]["id"])
        if("nc11" in district):
            bidennc11.add(tw["user"]["id"])
        if("nc12" in district):
            bidennc12.add(tw["user"]["id"])
        if("nc13" in district):
            bidennc13.add(tw["user"]["id"])
        if("nh1" in district):
            bidennh1.add(tw["user"]["id"])
        if("nh2" in district):
            bidennh2.add(tw["user"]["id"])
        if("nv1" in district):
            bidennv1.add(tw["user"]["id"])
        if("nv2" in district):
            bidennv2.add(tw["user"]["id"])
        if("nv3" in district):
            bidennv3.add(tw["user"]["id"])
        if("nv4" in district):
            bidennv4.add(tw["user"]["id"])
        if("co1" in district):
            bidenco1.add(tw["user"]["id"])
        if("co2" in district):
            bidenco2.add(tw["user"]["id"])
        if("co3" in district):
            bidenco3.add(tw["user"]["id"])
        if("co4" in district):
            bidenco4.add(tw["user"]["id"])
        if("co5" in district):
            bidenco5.add(tw["user"]["id"])
        if("co6" in district):
            bidenco6.add(tw["user"]["id"])
        if("co7" in district):
            bidenco7.add(tw["user"]["id"])
        if("nm1" in district):
            bidennm1.add(tw["user"]["id"])
        if("nm2" in district):
            bidennm2.add(tw["user"]["id"])
        if("nm3" in district):
            bidennm3.add(tw["user"]["id"])
        if("az1" in district):
            bidenaz1.add(tw["user"]["id"])
        if("az2" in district):
            bidenaz2.add(tw["user"]["id"])
        if("az3" in district):
            bidenaz3.add(tw["user"]["id"])
        if("az4" in district):
            bidenaz4.add(tw["user"]["id"])
        if("az5" in district):
            bidenaz5.add(tw["user"]["id"])
        if("az6" in district):
            bidenaz6.add(tw["user"]["id"])
        if("az7" in district):
            bidenaz7.add(tw["user"]["id"])
        if("az8" in district):
            bidenaz8.add(tw["user"]["id"])
        if("az9" in district):
            bidenaz9.add(tw["user"]["id"])
        if("ga1" in district):
            bidenga1.add(tw["user"]["id"])
        if("ga2" in district):
            bidenga2.add(tw["user"]["id"])
        if("ga3" in district):
            bidenga3.add(tw["user"]["id"])
        if("ga4" in district):
            bidenga4.add(tw["user"]["id"])
        if("ga5" in district):
            bidenga5.add(tw["user"]["id"])
        if("ga6" in district):
            bidenga6.add(tw["user"]["id"])
        if("ga7" in district):
            bidenga7.add(tw["user"]["id"])
        if("ga8" in district):
            bidenga8.add(tw["user"]["id"])
        if("ga9" in district):
            bidenga9.add(tw["user"]["id"])
        if("ga10" in district):
            bidenga10.add(tw["user"]["id"])
        if("ga11" in district):
            bidenga11.add(tw["user"]["id"])
        if("ga12" in district):
            bidenga12.add(tw["user"]["id"])
        if("ga13" in district):
            bidenga13.add(tw["user"]["id"])
        if("ga14" in district):
            bidenga14.add(tw["user"]["id"])
        if("tx1" in district):
            bidentx1.add(tw["user"]["id"])
        if("tx2" in district):
            bidentx2.add(tw["user"]["id"])
        if("tx3" in district):
            bidentx3.add(tw["user"]["id"])
        if("tx4" in district):
            bidentx4.add(tw["user"]["id"])
        if("tx5" in district):
            bidentx5.add(tw["user"]["id"])
        if("tx6" in district):
            bidentx6.add(tw["user"]["id"])
        if("tx7" in district):
            bidentx7.add(tw["user"]["id"])
        if("tx8" in district):
            bidentx8.add(tw["user"]["id"])
        if("tx9" in district):
            bidentx9.add(tw["user"]["id"])
        if("tx10" in district):
            bidentx10.add(tw["user"]["id"])
        if("tx11" in district):
            bidentx11.add(tw["user"]["id"])
        if("tx12" in district):
            bidentx12.add(tw["user"]["id"])
        if("tx13" in district):
            bidentx13.add(tw["user"]["id"])
        if("tx14" in district):
            bidentx14.add(tw["user"]["id"])
        if("tx15" in district):
            bidentx15.add(tw["user"]["id"])
        if("tx16" in district):
            bidentx16.add(tw["user"]["id"])
        if("tx17" in district):
            bidentx17.add(tw["user"]["id"])
        if("tx18" in district):
            bidentx18.add(tw["user"]["id"])
        if("tx19" in district):
            bidentx19.add(tw["user"]["id"])
        if("tx20" in district):
            bidentx20.add(tw["user"]["id"])
        if("tx21" in district):
            bidentx21.add(tw["user"]["id"])
        if("tx22" in district):
            bidentx22.add(tw["user"]["id"])
        if("tx23" in district):
            bidentx23.add(tw["user"]["id"])
        if("tx24" in district):
            bidentx24.add(tw["user"]["id"])
        if("tx25" in district):
            bidentx25.add(tw["user"]["id"])
        if("tx26" in district):
            bidentx26.add(tw["user"]["id"])
        if("tx27" in district):
            bidentx27.add(tw["user"]["id"])
        if("tx28" in district):
            bidentx28.add(tw["user"]["id"])
        if("tx29" in district):
            bidentx29.add(tw["user"]["id"])
        if("tx30" in district):
            bidentx30.add(tw["user"]["id"])
        if("tx31" in district):
            bidentx31.add(tw["user"]["id"])
        if("tx32" in district):
            bidentx32.add(tw["user"]["id"])
        if("tx33" in district):
            bidentx33.add(tw["user"]["id"])
        if("tx34" in district):
            bidentx34.add(tw["user"]["id"])
        if("tx35" in district):
            bidentx35.add(tw["user"]["id"])
        if("tx36" in district):
            bidentx36.add(tw["user"]["id"])
        if("in1" in district):
            bidenin1.add(tw["user"]["id"])
        if("in2" in district):
            bidenin2.add(tw["user"]["id"])
        if("in3" in district):
            bidenin3.add(tw["user"]["id"])
        if("in4" in district):
            bidenin4.add(tw["user"]["id"])
        if("in5" in district):
            bidenin5.add(tw["user"]["id"])
        if("in6" in district):
            bidenin6.add(tw["user"]["id"])
        if("in7" in district):
            bidenin7.add(tw["user"]["id"])
        if("in8" in district):
            bidenin8.add(tw["user"]["id"])
        if("in9" in district):
            bidenin9.add(tw["user"]["id"])
        if("va1" in district):
            bidenva1.add(tw["user"]["id"])
        if("va2" in district):
            bidenva2.add(tw["user"]["id"])
        if("va3" in district):
            bidenva3.add(tw["user"]["id"])
        if("va4" in district):
            bidenva4.add(tw["user"]["id"])
        if("va5" in district):
            bidenva5.add(tw["user"]["id"])
        if("va6" in district):
            bidenva6.add(tw["user"]["id"])
        if("va7" in district):
            bidenva7.add(tw["user"]["id"])
        if("va8" in district):
            bidenva8.add(tw["user"]["id"])
        if("va9" in district):
            bidenva9.add(tw["user"]["id"])
        if("va10" in district):
            bidenva10.add(tw["user"]["id"])
        if("va11" in district):
            bidenva11.add(tw["user"]["id"])
        if("il1" in district):
            bidenil1.add(tw["user"]["id"])
        if("il2" in district):
            bidenil2.add(tw["user"]["id"])
        if("il3" in district):
            bidenil3.add(tw["user"]["id"])
        if("il4" in district):
            bidenil4.add(tw["user"]["id"])
        if("il5" in district):
            bidenil5.add(tw["user"]["id"])
        if("il6" in district):
            bidenil6.add(tw["user"]["id"])
        if("il7" in district):
            bidenil7.add(tw["user"]["id"])
        if("il8" in district):
            bidenil8.add(tw["user"]["id"])
        if("il9" in district):
            bidenil9.add(tw["user"]["id"])
        if("il10" in district):
            bidenil10.add(tw["user"]["id"])
        if("il11" in district):
            bidenil11.add(tw["user"]["id"])
        if("il12" in district):
            bidenil12.add(tw["user"]["id"])
        if("il13" in district):
            bidenil13.add(tw["user"]["id"])
        if("il14" in district):
            bidenil14.add(tw["user"]["id"])
        if("il15" in district):
            bidenil15.add(tw["user"]["id"])
        if("il16" in district):
            bidenil16.add(tw["user"]["id"])
        if("il17" in district):
            bidenil17.add(tw["user"]["id"])
        if("il18" in district):
            bidenil18.add(tw["user"]["id"])
        if("de1" in district):
            bidende1.add(tw["user"]["id"])
        if("vt1" in district):
            bidenvt1.add(tw["user"]["id"])
        if("ut1" in district):
            bidenut1.add(tw["user"]["id"])
        if("ut2" in district):
            bidenut2.add(tw["user"]["id"])
        if("ut3" in district):
            bidenut3.add(tw["user"]["id"])
        if("ut4" in district):
            bidenut4.add(tw["user"]["id"])
        if("ne1" in district):
            bidenne1.add(tw["user"]["id"])
        if("ne2" in district):
            bidenne2.add(tw["user"]["id"])
        if("ne3" in district):
            bidenne3.add(tw["user"]["id"])
        if("ak1" in district):
            bidenak1.add(tw["user"]["id"])
        if("wy1" in district):
            bidenwy1.add(tw["user"]["id"])
        if("al1" in district):
            bidenal1.add(tw["user"]["id"])
        if("al2" in district):
            bidenal2.add(tw["user"]["id"])
        if("al3" in district):
            bidenal3.add(tw["user"]["id"])
        if("al4" in district):
            bidenal4.add(tw["user"]["id"])
        if("al5" in district):
            bidenal5.add(tw["user"]["id"])
        if("al6" in district):
            bidenal6.add(tw["user"]["id"])
        if("al7" in district):
            bidenal7.add(tw["user"]["id"])
        if("tn1" in district):
            bidentn1.add(tw["user"]["id"])
        if("tn2" in district):
            bidentn2.add(tw["user"]["id"])
        if("tn3" in district):
            bidentn3.add(tw["user"]["id"])
        if("tn4" in district):
            bidentn4.add(tw["user"]["id"])
        if("tn5" in district):
            bidentn5.add(tw["user"]["id"])
        if("tn6" in district):
            bidentn6.add(tw["user"]["id"])
        if("tn7" in district):
            bidentn7.add(tw["user"]["id"])
        if("tn8" in district):
            bidentn8.add(tw["user"]["id"])
        if("tn9" in district):
            bidentn9.add(tw["user"]["id"])
        if("nd1" in district):
            bidennd1.add(tw["user"]["id"])
        if("sd1" in district):
            bidensd1.add(tw["user"]["id"])
        if("wv1" in district):
            bidenwv1.add(tw["user"]["id"])
        if("wv2" in district):
            bidenwv2.add(tw["user"]["id"])
        if("wv3" in district):
            bidenwv3.add(tw["user"]["id"])
        if("ar1" in district):
            bidenar1.add(tw["user"]["id"])
        if("ar2" in district):
            bidenar2.add(tw["user"]["id"])
        if("ar3" in district):
            bidenar3.add(tw["user"]["id"])
        if("ar4" in district):
            bidenar4.add(tw["user"]["id"])






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
print("Trump: ", (len(trumpak1)/(len(trumpak1)+len(bidenak1))))
print("votes ", len(trumpak1))
print("Biden: ",(len(bidenak1)/(len(trumpak1)+len(bidenak1))))
print("votes ", len(bidenak1))
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
print("Trump: ", (len(trumpde1)/(len(trumpde1)+len(bidende1))))
print("votes ", len(trumpde1))
print("Biden: ",(len(bidende1)/(len(trumpde1)+len(bidende1))))
print("votes ", len(bidende1))
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
print("Trump: ", (len(trumpsd1)/(len(trumpsd1)+len(bidensd1))))
print("votes ", len(trumpsd1))
print("Biden: ",(len(bidensd1)/(len(trumpsd1)+len(bidensd1))))
print("votes ", len(bidensd1))
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
print("Massachusetts 8")
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
print("Trump: ", (len(trumpnj1)/(len(trumpnj1)+len(bidennj1))))
print("votes ", trumpnj1votes)
print("Biden: ",(len(bidennj1)/(len(trumpnj1)+len(bidennj1))))
print("votes ", bidennj1votes)
print("New Jersey 2")
trumpnj2votes = (len(trumpnj2)/(len(trumpnj2)+len(bidennj2)))*272542
bidennj2votes = (len(bidennj2)/(len(trumpnj2)+len(bidennj2)))*272542
print("Trump: ", (len(trumpnj2)/(len(trumpnj2)+len(bidennj2))))
print("votes ", trumpnj2votes)
print("Biden: ",(len(bidennj2)/(len(trumpnj2)+len(bidennj2))))
print("votes ", bidennj2votes)
print("New Jersey 3")
trumpnj3votes = (len(trumpnj3)/(len(trumpnj3)+len(bidennj3)))*292734
bidennj3votes = (len(bidennj3)/(len(trumpnj3)+len(bidennj3)))*292734
print("Trump: ", (len(trumpnj3)/(len(trumpnj3)+len(bidennj3))))
print("votes ", trumpnj3votes)
print("Biden: ",(len(bidennj3)/(len(trumpnj3)+len(bidennj3))))
print("votes ", bidennj3votes)
print("New Jersey 4")
trumpnj4votes = (len(trumpnj4)/(len(trumpnj4)+len(bidennj4)))*314510
bidennj4votes = (len(bidennj4)/(len(trumpnj4)+len(bidennj4)))*314510
print("Trump: ", (len(trumpnj4)/(len(trumpnj4)+len(bidennj4))))
print("votes ", trumpnj4votes)
print("Biden: ",(len(bidennj4)/(len(trumpnj4)+len(bidennj4))))
print("votes ", bidennj4votes)
print("New Jersey 5")
trumpnj5votes = (len(trumpnj5)/(len(trumpnj5)+len(bidennj5)))*303506
bidennj5votes = (len(bidennj5)/(len(trumpnj5)+len(bidennj5)))*303506
print("Trump: ", (len(trumpnj5)/(len(trumpnj5)+len(bidennj5))))
print("votes ", trumpnj5votes)
print("Biden: ",(len(bidennj5)/(len(trumpnj5)+len(bidennj5))))
print("votes ", bidennj5votes)
print("New Jersey 6")
trumpnj6votes = (len(trumpnj6)/(len(trumpnj6)+len(bidennj6)))*236584
bidennj6votes = (len(bidennj6)/(len(trumpnj6)+len(bidennj6)))*236584
print("Trump: ", (len(trumpnj6)/(len(trumpnj6)+len(bidennj6))))
print("votes ", trumpnj6votes)
print("Biden: ",(len(bidennj6)/(len(trumpnj6)+len(bidennj6))))
print("votes ", bidennj6votes)
print("New Jersey 7")
trumpnj7votes = (len(trumpnj7)/(len(trumpnj7)+len(bidennj7)))*330659
bidennj7votes = (len(bidennj7)/(len(trumpnj7)+len(bidennj7)))*330659
print("Trump: ", (len(trumpnj7)/(len(trumpnj7)+len(bidennj7))))
print("votes ", trumpnj7votes)
print("Biden: ",(len(bidennj7)/(len(trumpnj7)+len(bidennj7))))
print("votes ", bidennj7votes)
print("New Jersey 8")
trumpnj8votes = (len(trumpnj8)/(len(trumpnj8)+len(bidennj8)))*154466
bidennj8votes = (len(bidennj8)/(len(trumpnj8)+len(bidennj8)))*154466
print("Trump: ", (len(trumpnj8)/(len(trumpnj8)+len(bidennj8))))
print("votes ", trumpnj8votes)
print("Biden: ",(len(bidennj8)/(len(trumpnj8)+len(bidennj8))))
print("votes ", bidennj8votes)
print("New Jersey 9")
trumpnj9votes = (len(trumpnj9)/(len(trumpnj9)+len(bidennj9)))*213207
bidennj9votes = (len(bidennj9)/(len(trumpnj9)+len(bidennj9)))*213207
print("Trump: ", (len(trumpnj9)/(len(trumpnj9)+len(bidennj9))))
print("votes ", trumpnj9votes)
print("Biden: ",(len(bidennj9)/(len(trumpnj9)+len(bidennj9))))
print("votes ", bidennj9votes)
print("New Jersey 10")
trumpnj10votes = (len(trumpnj10)/(len(trumpnj10)+len(bidennj10)))*207043
bidennj10votes = (len(bidennj10)/(len(trumpnj10)+len(bidennj10)))*207043
print("Trump: ", (len(trumpnj10)/(len(trumpnj10)+len(bidennj10))))
print("votes ", trumpnj10votes)
print("Biden: ",(len(bidennj10)/(len(trumpnj10)+len(bidennj10))))
print("votes ", bidennj10votes)
print("New Jersey 11")
trumpnj11votes = (len(trumpnj11)/(len(trumpnj11)+len(bidennj11)))*320770
bidennj11votes = (len(bidennj11)/(len(trumpnj11)+len(bidennj11)))*320770
print("Trump: ", (len(trumpnj11)/(len(trumpnj11)+len(bidennj11))))
print("votes ", trumpnj11votes)
print("Biden: ",(len(bidennj11)/(len(trumpnj11)+len(bidennj11))))
print("votes ", bidennj11votes)
print("New Jersey 12")
trumpnj12votes = (len(trumpnj12)/(len(trumpnj12)+len(bidennj12)))*246016
bidennj12votes = (len(bidennj12)/(len(trumpnj12)+len(bidennj12)))*246016
print("Trump: ", (len(trumpnj12)/(len(trumpnj12)+len(bidennj12))))
print("votes ", trumpnj12votes)
print("Biden: ",(len(bidennj12)/(len(trumpnj12)+len(bidennj12))))
print("votes ", bidennj12votes)
totalnjvotestrump = trumpnj1votes+trumpnj2votes+trumpnj3votes+trumpnj4votes+trumpnj5votes+trumpnj6votes+trumpnj7votes+trumpnj8votes+trumpnj9votes+trumpnj10votes+trumpnj11votes+trumpnj12votes
totalnjvotesbiden = bidennj1votes+bidennj2votes+bidennj3votes+bidennj4votes+bidennj5votes+bidennj6votes+bidennj7votes+bidennj8votes+bidennj9votes+bidennj10votes+bidennj11votes+bidennj12votes
print("TOTAL TRUMP VOTES: ", totalnjvotestrump/(totalnjvotestrump+totalnjvotesbiden))
print("TOTAL BIDEN VOTES: ", totalnjvotesbiden/(totalnjvotestrump+totalnjvotesbiden))
print("")
print("New Mexico")
print("Trump: ", (len(trumpnm)/(len(trumpnm)+len(bidennm))))
print("Biden: ",(len(bidennm)/(len(trumpnm)+len(bidennm))))
print("New Mexico 1")
print("Trump: ", (len(trumpnm1)/(len(trumpnm1)+len(bidennm1))))
print("votes ", len(trumpnm1))
print("Biden: ",(len(bidennm1)/(len(trumpnm1)+len(bidennm1))))
print("votes ", len(bidennm1))
trumpnm1votes = (len(trumpnm1)/(len(trumpnm1)+len(bidennm1)))*275441
bidennm1votes = (len(bidennm1)/(len(trumpnm1)+len(bidennm1)))*275441
print("New Mexico 2")
print("Trump: ", (len(trumpnm2)/(len(trumpnm2)+len(bidennm2))))
print("votes ", len(trumpnm2))
print("Biden: ",(len(bidennm2)/(len(trumpnm2)+len(bidennm2))))
print("votes ", len(bidennm2))
trumpnm2votes = (len(trumpnm2)/(len(trumpnm2)+len(bidennm2)))*227013
bidennm2votes = (len(bidennm2)/(len(trumpnm2)+len(bidennm2)))*227013
print("New Mexico 3")
print("Trump: ", (len(trumpnm3)/(len(trumpnm3)+len(bidennm3))))
print("votes ", len(trumpnm3))
print("Biden: ",(len(bidennm3)/(len(trumpnm3)+len(bidennm3))))
print("votes ", len(bidennm3))
trumpnm3votes = (len(trumpnm3)/(len(trumpnm3)+len(bidennm3)))*268377
bidennm3votes = (len(bidennm3)/(len(trumpnm3)+len(bidennm3)))*268377
totalnmvotestrump = trumpnm1votes+trumpnm2votes+trumpnm3votes
totalnmvotesbiden = bidennm1votes+bidennm2votes+bidennm3votes
print("TOTAL TRUMP VOTES: ", totalnmvotestrump/(totalnmvotestrump+totalnmvotesbiden))
print("TOTAL BIDEN VOTES: ", totalnmvotesbiden/(totalnmvotestrump+totalnmvotesbiden))
print("")
print("Nebraska")
print("Trump: ", (len(trumpne)/(len(trumpne)+len(bidenne))))
print("Biden: ",(len(bidenne)/(len(trumpne)+len(bidenne))))
print("Nebraska 1")
trumpne1votes = (len(trumpne1)/(len(trumpne1)+len(bidenne1)))*1
bidenne1votes = (len(bidenne1)/(len(trumpne1)+len(bidenne1)))*1
print("Trump: ", (len(trumpne1)/(len(trumpne1)+len(bidenne1))))
print("votes ", len(trumpne1))
print("Biden: ",(len(bidenne1)/(len(trumpne1)+len(bidenne1))))
print("votes ", len(bidenne1))
print("Nebraska 2")
trumpne2votes = (len(trumpne2)/(len(trumpne2)+len(bidenne2)))*1
bidenne2votes = (len(bidenne2)/(len(trumpne2)+len(bidenne2)))*1
print("Trump: ", (len(trumpne2)/(len(trumpne2)+len(bidenne2))))
print("votes ", len(trumpne2))
print("Biden: ",(len(bidenne2)/(len(trumpne2)+len(bidenne2))))
print("votes ", len(bidenne2))
print("Nebraska 3")
trumpne3votes = (len(trumpne3)/(len(trumpne3)+len(bidenne3)))*1
bidenne3votes = (len(bidenne3)/(len(trumpne3)+len(bidenne3)))*1
print("Trump: ", (len(trumpne3)/(len(trumpne3)+len(bidenne3))))
print("votes ", len(trumpne3))
print("Biden: ",(len(bidenne3)/(len(trumpne3)+len(bidenne3))))
print("votes ", len(bidenne3))
totalnevotestrump = trumpne1votes+trumpne2votes+trumpne3votes
totalnevotesbiden = bidenne1votes+bidenne2votes+bidenne3votes
print("TOTAL TRUMP VOTES: ", totalnevotestrump/(totalnevotestrump+totalnevotesbiden))
print("TOTAL BIDEN VOTES: ", totalnevotesbiden/(totalnevotestrump+totalnevotesbiden))
print("")
print("New Hampshire")
print("Trump: ", (len(trumpnh)/(len(trumpnh)+len(bidennh))))
print("Biden: ",(len(bidennh)/(len(trumpnh)+len(bidennh))))
print("New Hampshire 1")
trumpnh1votes = (len(trumpnh1)/(len(trumpnh1)+len(bidennh1)))*318839
bidennh1votes = (len(bidennh1)/(len(trumpnh1)+len(bidennh1)))*318839
print("Trump: ", (len(trumpnh1)/(len(trumpnh1)+len(bidennh1))))
print("votes ", len(trumpnh1))
print("Biden: ",(len(bidennh1)/(len(trumpnh1)+len(bidennh1))))
print("votes ", len(bidennh1))
print("New Hampshire 2")
trumpnh2votes = (len(trumpnh2)/(len(trumpnh2)+len(bidennh2)))*333346
bidennh2votes = (len(bidennh2)/(len(trumpnh2)+len(bidennh2)))*333346
print("Trump: ", (len(trumpnh2)/(len(trumpnh2)+len(bidennh2))))
print("votes ", len(trumpnh2))
print("Biden: ",(len(bidennh2)/(len(trumpnh2)+len(bidennh2))))
print("votes ", len(bidennh2))
totalnhvotestrump = trumpnh1votes+trumpnh2votes
totalnhvotesbiden = bidennh1votes+bidennh2votes
print("TOTAL TRUMP VOTES: ", totalnhvotestrump/(totalnhvotestrump+totalnhvotesbiden))
print("TOTAL BIDEN VOTES: ", totalnhvotesbiden/(totalnhvotestrump+totalnhvotesbiden))
print("")
print("Nevada")
print("Trump: ", (len(trumpnv)/(len(trumpnv)+len(bidennv))))
print("Biden: ",(len(bidennv)/(len(trumpnv)+len(bidennv))))
print("Nevada 1")
trumpnv1votes = (len(trumpnv1)/(len(trumpnv1)+len(bidennv1)))*170098
bidennv1votes = (len(bidennv1)/(len(trumpnv1)+len(bidennv1)))*170098
print("Trump: ", (len(trumpnv1)/(len(trumpnv1)+len(bidennv1))))
print("votes ", trumpnv1votes)
print("Biden: ",(len(bidennv1)/(len(trumpnv1)+len(bidennv1))))
print("votes ", bidennv1votes)
print("Nevada 2")
trumpnv2votes = (len(trumpnv2)/(len(trumpnv2)+len(bidennv2)))*297847
bidennv2votes = (len(bidennv2)/(len(trumpnv2)+len(bidennv2)))*297847
print("Trump: ", (len(trumpnv2)/(len(trumpnv2)+len(bidennv2))))
print("votes ", trumpnv2votes)
print("Biden: ",(len(bidennv2)/(len(trumpnv2)+len(bidennv2))))
print("votes ", bidennv2votes)
print("Nevada 3")
trumpnv3votes = (len(trumpnv3)/(len(trumpnv3)+len(bidennv3)))*289379
bidennv3votes = (len(bidennv3)/(len(trumpnv3)+len(bidennv3)))*289379
print("Trump: ", (len(trumpnv3)/(len(trumpnv3)+len(bidennv3))))
print("votes ", trumpnv3votes)
print("Biden: ",(len(bidennv3)/(len(trumpnv3)+len(bidennv3))))
print("votes ", bidennv3votes)
print("Nevada 4")
trumpnv4votes = (len(trumpnv4)/(len(trumpnv4)+len(bidennv4)))*246900
bidennv4votes = (len(bidennv4)/(len(trumpnv4)+len(bidennv4)))*246900
print("Trump: ", (len(trumpnv4)/(len(trumpnv4)+len(bidennv4))))
print("votes ", trumpnv4votes)
print("Biden: ",(len(bidennv4)/(len(trumpnv4)+len(bidennv4))))
print("votes ", bidennv4votes)
totalnvvotestrump = trumpnv1votes+trumpnv2votes+trumpnv3votes+trumpnv4votes
totalnvvotesbiden = bidennv1votes+bidennv2votes+bidennv3votes+bidennv4votes
print("TOTAL TRUMP VOTES: ", totalnvvotestrump/(totalnvvotestrump+totalnvvotesbiden))
print("TOTAL BIDEN VOTES: ", totalnvvotesbiden/(totalnvvotestrump+totalnvvotesbiden))
print("")
print("North Carolina")
print("Trump: ", (len(trumpnc)/(len(trumpnc)+len(bidennc))))
print("Biden: ",(len(bidennc)/(len(trumpnc)+len(bidennc))))
print("North Carolina 1")
trumpnc1votes = (len(trumpnc1)/(len(trumpnc1)+len(bidennc1)))*338571
bidennc1votes = (len(bidennc1)/(len(trumpnc1)+len(bidennc1)))*338571
print("Trump: ", (len(trumpnc1)/(len(trumpnc1)+len(bidennc1))))
print("votes ", trumpnc1votes)
print("Biden: ",(len(bidennc1)/(len(trumpnc1)+len(bidennc1))))
print("votes ", bidennc1votes)
print("North Carolina 2")
trumpnc2votes = (len(trumpnc2)/(len(trumpnc2)+len(bidennc2)))*386641
bidennc2votes = (len(bidennc2)/(len(trumpnc2)+len(bidennc2)))*386641
print("Trump: ", (len(trumpnc2)/(len(trumpnc2)+len(bidennc2))))
print("votes ", trumpnc2votes)
print("Biden: ",(len(bidennc2)/(len(trumpnc2)+len(bidennc2))))
print("votes ", bidennc2votes)
print("North Carolina 3")
trumpnc3votes = (len(trumpnc3)/(len(trumpnc3)+len(bidennc3)))*318857
bidennc3votes = (len(bidennc3)/(len(trumpnc3)+len(bidennc3)))*318857
print("Trump: ", (len(trumpnc3)/(len(trumpnc3)+len(bidennc3))))
print("votes ", trumpnc3votes)
print("Biden: ",(len(bidennc3)/(len(trumpnc3)+len(bidennc3))))
print("votes ", bidennc3votes)
print("North Carolina 4")
trumpnc4votes = (len(trumpnc4)/(len(trumpnc4)+len(bidennc4)))*403832
bidennc4votes = (len(bidennc4)/(len(trumpnc4)+len(bidennc4)))*403832
print("Trump: ", (len(trumpnc4)/(len(trumpnc4)+len(bidennc4))))
print("votes ", trumpnc4votes)
print("Biden: ",(len(bidennc4)/(len(trumpnc4)+len(bidennc4))))
print("votes ", bidennc4votes)
print("North Carolina 5")
trumpnc5votes = (len(trumpnc5)/(len(trumpnc5)+len(bidennc5)))*350540
bidennc5votes = (len(bidennc5)/(len(trumpnc5)+len(bidennc5)))*350540
print("Trump: ", (len(trumpnc5)/(len(trumpnc5)+len(bidennc5))))
print("votes ", trumpnc5votes)
print("Biden: ",(len(bidennc5)/(len(trumpnc5)+len(bidennc5))))
print("votes ", bidennc5votes)
print("North Carolina 6")
trumpnc6votes = (len(trumpnc6)/(len(trumpnc6)+len(bidennc6)))*347453
bidennc6votes = (len(bidennc6)/(len(trumpnc6)+len(bidennc6)))*347453
print("Trump: ", (len(trumpnc6)/(len(trumpnc6)+len(bidennc6))))
print("votes ", trumpnc6votes)
print("Biden: ",(len(bidennc6)/(len(trumpnc6)+len(bidennc6))))
print("votes ", bidennc6votes)
print("North Carolina 7")
trumpnc7votes = (len(trumpnc7)/(len(trumpnc7)+len(bidennc7)))*344277
bidennc7votes = (len(bidennc7)/(len(trumpnc7)+len(bidennc7)))*344277
print("Trump: ", (len(trumpnc7)/(len(trumpnc7)+len(bidennc7))))
print("votes ", trumpnc7votes)
print("Biden: ",(len(bidennc7)/(len(trumpnc7)+len(bidennc7))))
print("votes ", bidennc7votes)
print("North Carolina 8")
trumpnc8votes = (len(trumpnc8)/(len(trumpnc8)+len(bidennc8)))*319337
bidennc8votes = (len(bidennc8)/(len(trumpnc8)+len(bidennc8)))*319337
print("Trump: ", (len(trumpnc8)/(len(trumpnc8)+len(bidennc8))))
print("votes ", trumpnc8votes)
print("Biden: ",(len(bidennc8)/(len(trumpnc8)+len(bidennc8))))
print("votes ", bidennc8votes)
print("North Carolina 9")
trumpnc9votes = (len(trumpnc9)/(len(trumpnc9)+len(bidennc9)))*328995
bidennc9votes = (len(bidennc9)/(len(trumpnc9)+len(bidennc9)))*328995
print("Trump: ", (len(trumpnc9)/(len(trumpnc9)+len(bidennc9))))
print("votes ", trumpnc9votes)
print("Biden: ",(len(bidennc9)/(len(trumpnc9)+len(bidennc9))))
print("votes ", bidennc9votes)
print("North Carolina 10")
trumpnc10votes = (len(trumpnc10)/(len(trumpnc10)+len(bidennc10)))*347703
bidennc10votes = (len(bidennc10)/(len(trumpnc10)+len(bidennc10)))*347703
print("Trump: ", (len(trumpnc10)/(len(trumpnc10)+len(bidennc10))))
print("votes ", trumpnc10votes)
print("Biden: ",(len(bidennc10)/(len(trumpnc10)+len(bidennc10))))
print("votes ", bidennc10votes)
print("North Carolina 11")
trumpnc11votes = (len(trumpnc11)/(len(trumpnc11)+len(bidennc11)))*357102
bidennc11votes = (len(bidennc11)/(len(trumpnc11)+len(bidennc11)))*357102
print("Trump: ", (len(trumpnc11)/(len(trumpnc11)+len(bidennc11))))
print("votes ", trumpnc11votes)
print("Biden: ",(len(bidennc11)/(len(trumpnc11)+len(bidennc11))))
print("votes ", bidennc11votes)
print("North Carolina 12")
trumpnc12votes = (len(trumpnc12)/(len(trumpnc12)+len(bidennc12)))*346693
bidennc12votes = (len(bidennc12)/(len(trumpnc12)+len(bidennc12)))*346693
print("Trump: ", (len(trumpnc12)/(len(trumpnc12)+len(bidennc12))))
print("votes ", trumpnc12votes)
print("Biden: ",(len(bidennc12)/(len(trumpnc12)+len(bidennc12))))
print("votes ", bidennc12votes)
print("North Carolina 13")
trumpnc13votes = (len(trumpnc13)/(len(trumpnc13)+len(bidennc13)))*350427
bidennc13votes = (len(bidennc13)/(len(trumpnc13)+len(bidennc13)))*350427
print("Trump: ", (len(trumpnc13)/(len(trumpnc13)+len(bidennc13))))
print("votes ", trumpnc13votes)
print("Biden: ",(len(bidennc13)/(len(trumpnc13)+len(bidennc13))))
print("votes ", bidennc13votes)
totalncvotestrump = trumpnc1votes+trumpnc2votes+trumpnc3votes+trumpnc4votes+trumpnc5votes+trumpnc6votes+trumpnc7votes+trumpnc8votes+trumpnc9votes+trumpnc10votes+trumpnc11votes+trumpnc12votes+trumpnc13votes
totalncvotesbiden = bidennc1votes+bidennc2votes+bidennc3votes+bidennc4votes+bidennc5votes+bidennc6votes+bidennc7votes+bidennc8votes+bidennc9votes+bidennc10votes+bidennc11votes+bidennc12votes+bidennc13votes
print("TOTAL TRUMP VOTES: ", totalncvotestrump/(totalncvotestrump+totalncvotesbiden))
print("TOTAL BIDEN VOTES: ", totalncvotesbiden/(totalncvotestrump+totalncvotesbiden))
print("")
print("Oklahoma")
print("Trump: ", (len(trumpok)/(len(trumpok)+len(bidenok))))
print("Biden: ",(len(bidenok)/(len(trumpok)+len(bidenok))))
print("Oklahoma 1")
trumpok1votes = (len(trumpok1)/(len(trumpok1)+len(bidenok1)))*1
bidenok1votes = (len(bidenok1)/(len(trumpok1)+len(bidenok1)))*1
print("Trump: ", (len(trumpok1)/(len(trumpok1)+len(bidenok1))))
print("votes ", trumpok1votes)
print("Biden: ",(len(bidenok1)/(len(trumpok1)+len(bidenok1))))
print("votes ", bidenok1votes)
print("Oklahoma 2")
trumpok2votes = (len(trumpok2)/(len(trumpok2)+len(bidenok2)))*1
bidenok2votes = (len(bidenok2)/(len(trumpok2)+len(bidenok2)))*1
print("Trump: ", (len(trumpok2)/(len(trumpok2)+len(bidenok2))))
print("votes ", trumpok2votes)
print("Biden: ",(len(bidenok2)/(len(trumpok2)+len(bidenok2))))
print("votes ", bidenok2votes)
print("Oklahoma 3")
trumpok3votes = (len(trumpok3)/(len(trumpok3)+len(bidenok3)))*1
bidenok3votes = (len(bidenok3)/(len(trumpok3)+len(bidenok3)))*1
print("Trump: ", (len(trumpok3)/(len(trumpok3)+len(bidenok3))))
print("votes ", trumpok3votes)
print("Biden: ",(len(bidenok3)/(len(trumpok3)+len(bidenok3))))
print("votes ", bidenok3votes)
print("Oklahoma 4")
trumpok4votes = (len(trumpok4)/(len(trumpok4)+len(bidenok4)))*1
bidenok4votes = (len(bidenok4)/(len(trumpok4)+len(bidenok4)))*1
print("Trump: ", (len(trumpok4)/(len(trumpok4)+len(bidenok4))))
print("votes ", trumpok4votes)
print("Biden: ",(len(bidenok4)/(len(trumpok4)+len(bidenok4))))
print("votes ", bidenok4votes)
print("Oklahoma 5")
trumpok5votes = (len(trumpok5)/(len(trumpok5)+len(bidenok5)))*1
bidenok5votes = (len(bidenok5)/(len(trumpok5)+len(bidenok5)))*1
print("Trump: ", (len(trumpok5)/(len(trumpok5)+len(bidenok5))))
print("votes ", trumpok5votes)
print("Biden: ",(len(bidenok5)/(len(trumpok5)+len(bidenok5))))
print("votes ", bidenok5votes)
totalokvotestrump = trumpok1votes+trumpok2votes+trumpok3votes+trumpok4votes+trumpok5votes
totalokvotesbiden = bidenok1votes+bidenok2votes+bidenok3votes+bidenok4votes+bidenok5votes
print("TOTAL TRUMP VOTES: ", totalokvotestrump/(totalokvotestrump+totalokvotesbiden))
print("TOTAL BIDEN VOTES: ", totalokvotesbiden/(totalokvotestrump+totalokvotesbiden))
print("")
print("New York")
print("Trump: ", (len(trumpny)/(len(trumpny)+len(bidenny))))
print("Biden: ",(len(bidenny)/(len(trumpny)+len(bidenny))))
print("New York 1")
trumpny1votes = (len(trumpny1)/(len(trumpny1)+len(bidenny1)))*1
bidenny1votes = (len(bidenny1)/(len(trumpny1)+len(bidenny1)))*1
print("Trump: ", (len(trumpny1)/(len(trumpny1)+len(bidenny1))))
print("votes ", trumpny1votes)
print("Biden: ",(len(bidenny1)/(len(trumpny1)+len(bidenny1))))
print("votes ", bidenny1votes)
print("New York 2")
trumpny2votes = (len(trumpny2)/(len(trumpny2)+len(bidenny2)))*1
bidenny2votes = (len(bidenny2)/(len(trumpny2)+len(bidenny2)))*1
print("Trump: ", (len(trumpny2)/(len(trumpny2)+len(bidenny2))))
print("votes ", trumpny2votes)
print("Biden: ",(len(bidenny2)/(len(trumpny2)+len(bidenny2))))
print("votes ", bidenny2votes)
print("New York 3")
trumpny3votes = (len(trumpny3)/(len(trumpny3)+len(bidenny3)))*1
bidenny3votes = (len(bidenny3)/(len(trumpny3)+len(bidenny3)))*1
print("Trump: ", (len(trumpny3)/(len(trumpny3)+len(bidenny3))))
print("votes ", trumpny3votes)
print("Biden: ",(len(bidenny3)/(len(trumpny3)+len(bidenny3))))
print("votes ", bidenny3votes)
print("New York 4")
trumpny4votes = (len(trumpny4)/(len(trumpny4)+len(bidenny4)))*1
bidenny4votes = (len(bidenny4)/(len(trumpny4)+len(bidenny4)))*1
print("Trump: ", (len(trumpny4)/(len(trumpny4)+len(bidenny4))))
print("votes ", trumpny4votes)
print("Biden: ",(len(bidenny4)/(len(trumpny4)+len(bidenny4))))
print("votes ", bidenny4votes)
print("New York 5")
trumpny5votes = (len(trumpny5)/(len(trumpny5)+len(bidenny5)))*1
bidenny5votes = (len(bidenny5)/(len(trumpny5)+len(bidenny5)))*1
print("Trump: ", (len(trumpny5)/(len(trumpny5)+len(bidenny5))))
print("votes ", trumpny5votes)
print("Biden: ",(len(bidenny5)/(len(trumpny5)+len(bidenny5))))
print("votes ", bidenny5votes)
print("New York 6")
trumpny6votes = (len(trumpny6)/(len(trumpny6)+len(bidenny6)))*1
bidenny6votes = (len(bidenny6)/(len(trumpny6)+len(bidenny6)))*1
print("Trump: ", (len(trumpny6)/(len(trumpny6)+len(bidenny6))))
print("votes ", trumpny6votes)
print("Biden: ",(len(bidenny6)/(len(trumpny6)+len(bidenny6))))
print("votes ", bidenny6votes)
print("New York 7")
trumpny7votes = (len(trumpny7)/(len(trumpny7)+len(bidenny7)))*1
bidenny7votes = (len(bidenny7)/(len(trumpny7)+len(bidenny7)))*1
print("Trump: ", (len(trumpny7)/(len(trumpny7)+len(bidenny7))))
print("votes ", trumpny7votes)
print("Biden: ",(len(bidenny7)/(len(trumpny7)+len(bidenny7))))
print("votes ", bidenny7votes)
print("New York 8")
trumpny8votes = (len(trumpny8)/(len(trumpny8)+len(bidenny8)))*1
bidenny8votes = (len(bidenny8)/(len(trumpny8)+len(bidenny8)))*1
print("Trump: ", (len(trumpny8)/(len(trumpny8)+len(bidenny8))))
print("votes ", trumpny8votes)
print("Biden: ",(len(bidenny8)/(len(trumpny8)+len(bidenny8))))
print("votes ", bidenny8votes)
print("New York 9")
trumpny9votes = (len(trumpny9)/(len(trumpny9)+len(bidenny9)))*1
bidenny9votes = (len(bidenny9)/(len(trumpny9)+len(bidenny9)))*1
print("Trump: ", (len(trumpny9)/(len(trumpny9)+len(bidenny9))))
print("votes ", trumpny9votes)
print("Biden: ",(len(bidenny9)/(len(trumpny9)+len(bidenny9))))
print("votes ", bidenny9votes)
print("New York 10")
trumpny10votes = (len(trumpny10)/(len(trumpny10)+len(bidenny10)))*1
bidenny10votes = (len(bidenny10)/(len(trumpny10)+len(bidenny10)))*1
print("Trump: ", (len(trumpny10)/(len(trumpny10)+len(bidenny10))))
print("votes ", trumpny10votes)
print("Biden: ",(len(bidenny10)/(len(trumpny10)+len(bidenny10))))
print("votes ", bidenny10votes)
print("New York 11")
trumpny11votes = (len(trumpny11)/(len(trumpny11)+len(bidenny11)))*1
bidenny11votes = (len(bidenny11)/(len(trumpny11)+len(bidenny11)))*1
print("Trump: ", (len(trumpny11)/(len(trumpny11)+len(bidenny11))))
print("votes ", trumpny11votes)
print("Biden: ",(len(bidenny11)/(len(trumpny11)+len(bidenny11))))
print("votes ", bidenny11votes)
print("New York 12")
trumpny12votes = (len(trumpny12)/(len(trumpny12)+len(bidenny12)))*1
bidenny12votes = (len(bidenny12)/(len(trumpny12)+len(bidenny12)))*1
print("Trump: ", (len(trumpny12)/(len(trumpny12)+len(bidenny12))))
print("votes ", trumpny12votes)
print("Biden: ",(len(bidenny12)/(len(trumpny12)+len(bidenny12))))
print("votes ", bidenny12votes)
print("New York 13")
trumpny13votes = (len(trumpny13)/(len(trumpny13)+len(bidenny13)))*1
bidenny13votes = (len(bidenny13)/(len(trumpny13)+len(bidenny13)))*1
print("Trump: ", (len(trumpny13)/(len(trumpny13)+len(bidenny13))))
print("votes ", trumpny13votes)
print("Biden: ",(len(bidenny13)/(len(trumpny13)+len(bidenny13))))
print("votes ", bidenny13votes)
print("New York 14")
trumpny14votes = (len(trumpny14)/(len(trumpny14)+len(bidenny14)))*1
bidenny14votes = (len(bidenny14)/(len(trumpny14)+len(bidenny14)))*1
print("Trump: ", (len(trumpny14)/(len(trumpny14)+len(bidenny14))))
print("votes ", trumpny14votes)
print("Biden: ",(len(bidenny14)/(len(trumpny14)+len(bidenny14))))
print("votes ", bidenny14votes)
print("New York 15")
trumpny15votes = (len(trumpny15)/(len(trumpny15)+len(bidenny15)))*1
bidenny15votes = (len(bidenny15)/(len(trumpny15)+len(bidenny15)))*1
print("Trump: ", (len(trumpny15)/(len(trumpny15)+len(bidenny15))))
print("votes ", trumpny15votes)
print("Biden: ",(len(bidenny15)/(len(trumpny15)+len(bidenny15))))
print("votes ", bidenny15votes)
print("New York 16")
trumpny16votes = (len(trumpny16)/(len(trumpny16)+len(bidenny16)))*1
bidenny16votes = (len(bidenny16)/(len(trumpny16)+len(bidenny16)))*1
print("Trump: ", (len(trumpny16)/(len(trumpny16)+len(bidenny16))))
print("votes ", trumpny16votes)
print("Biden: ",(len(bidenny16)/(len(trumpny16)+len(bidenny16))))
print("votes ", bidenny16votes)
print("New York 17")
trumpny17votes = (len(trumpny17)/(len(trumpny17)+len(bidenny17)))*1
bidenny17votes = (len(bidenny17)/(len(trumpny17)+len(bidenny17)))*1
print("Trump: ", (len(trumpny17)/(len(trumpny17)+len(bidenny17))))
print("votes ", trumpny17votes)
print("Biden: ",(len(bidenny17)/(len(trumpny17)+len(bidenny17))))
print("votes ", bidenny17votes)
print("New York 18")
trumpny18votes = (len(trumpny18)/(len(trumpny18)+len(bidenny18)))*1
bidenny18votes = (len(bidenny18)/(len(trumpny18)+len(bidenny18)))*1
print("Trump: ", (len(trumpny18)/(len(trumpny18)+len(bidenny18))))
print("votes ", trumpny18votes)
print("Biden: ",(len(bidenny18)/(len(trumpny18)+len(bidenny18))))
print("votes ", bidenny18votes)
print("New York 19")
trumpny19votes = (len(trumpny19)/(len(trumpny19)+len(bidenny19)))*1
bidenny19votes = (len(bidenny19)/(len(trumpny19)+len(bidenny19)))*1
print("Trump: ", (len(trumpny19)/(len(trumpny19)+len(bidenny19))))
print("votes ", trumpny19votes)
print("Biden: ",(len(bidenny19)/(len(trumpny19)+len(bidenny19))))
print("votes ", bidenny19votes)
print("New York 20")
trumpny20votes = (len(trumpny20)/(len(trumpny20)+len(bidenny20)))*1
bidenny20votes = (len(bidenny20)/(len(trumpny20)+len(bidenny20)))*1
print("Trump: ", (len(trumpny20)/(len(trumpny20)+len(bidenny20))))
print("votes ", trumpny20votes)
print("Biden: ",(len(bidenny20)/(len(trumpny20)+len(bidenny20))))
print("votes ", bidenny20votes)
print("New York 21")
trumpny21votes = (len(trumpny21)/(len(trumpny21)+len(bidenny21)))*1
bidenny21votes = (len(bidenny21)/(len(trumpny21)+len(bidenny21)))*1
print("Trump: ", (len(trumpny21)/(len(trumpny21)+len(bidenny21))))
print("votes ", trumpny21votes)
print("Biden: ",(len(bidenny21)/(len(trumpny21)+len(bidenny21))))
print("votes ", bidenny21votes)
print("New York 22")
trumpny22votes = (len(trumpny22)/(len(trumpny22)+len(bidenny22)))*1
bidenny22votes = (len(bidenny22)/(len(trumpny22)+len(bidenny22)))*1
print("Trump: ", (len(trumpny22)/(len(trumpny22)+len(bidenny22))))
print("votes ", trumpny22votes)
print("Biden: ",(len(bidenny22)/(len(trumpny22)+len(bidenny22))))
print("votes ", bidenny22votes)
print("New York 23")
trumpny23votes = (len(trumpny23)/(len(trumpny23)+len(bidenny23)))*1
bidenny23votes = (len(bidenny23)/(len(trumpny23)+len(bidenny23)))*1
print("Trump: ", (len(trumpny23)/(len(trumpny23)+len(bidenny23))))
print("votes ", trumpny23votes)
print("Biden: ",(len(bidenny23)/(len(trumpny23)+len(bidenny23))))
print("votes ", bidenny23votes)
print("New York 24")
trumpny24votes = (len(trumpny24)/(len(trumpny24)+len(bidenny24)))*1
bidenny24votes = (len(bidenny24)/(len(trumpny24)+len(bidenny24)))*1
print("Trump: ", (len(trumpny24)/(len(trumpny24)+len(bidenny24))))
print("votes ", trumpny24votes)
print("Biden: ",(len(bidenny24)/(len(trumpny24)+len(bidenny24))))
print("votes ", bidenny24votes)
print("New York 25")
trumpny25votes = (len(trumpny25)/(len(trumpny25)+len(bidenny25)))*1
bidenny25votes = (len(bidenny25)/(len(trumpny25)+len(bidenny25)))*1
print("Trump: ", (len(trumpny25)/(len(trumpny25)+len(bidenny25))))
print("votes ", trumpny25votes)
print("Biden: ",(len(bidenny25)/(len(trumpny25)+len(bidenny25))))
print("votes ", bidenny25votes)
print("New York 26")
trumpny26votes = (len(trumpny26)/(len(trumpny26)+len(bidenny26)))*1
bidenny26votes = (len(bidenny26)/(len(trumpny26)+len(bidenny26)))*1
print("Trump: ", (len(trumpny26)/(len(trumpny26)+len(bidenny26))))
print("votes ", trumpny26votes)
print("Biden: ",(len(bidenny26)/(len(trumpny26)+len(bidenny26))))
print("votes ", bidenny26votes)
print("New York 27")
trumpny27votes = (len(trumpny27)/(len(trumpny27)+len(bidenny27)))*1
bidenny27votes = (len(bidenny27)/(len(trumpny27)+len(bidenny27)))*1
print("Trump: ", (len(trumpny27)/(len(trumpny27)+len(bidenny27))))
print("votes ", trumpny27votes)
print("Biden: ",(len(bidenny27)/(len(trumpny27)+len(bidenny27))))
print("votes ", bidenny27votes)
totalnyvotestrump = trumpny1votes+trumpny2votes+trumpny3votes+trumpny4votes+trumpny5votes+trumpny6votes+trumpny7votes+trumpny8votes+trumpny9votes+trumpny10votes+trumpny11votes+trumpny12votes+trumpny13votes+trumpny14votes+trumpny15votes+trumpny16votes+trumpny17votes+trumpny18votes+trumpny19votes+trumpny20votes+trumpny21votes+trumpny22votes+trumpny23votes+trumpny24votes+trumpny25votes+trumpny26votes+trumpny27votes
totalnyvotesbiden = bidenny1votes+bidenny2votes+bidenny3votes+bidenny4votes+bidenny5votes+bidenny6votes+bidenny7votes+bidenny8votes+bidenny9votes+bidenny10votes+bidenny11votes+bidenny12votes+bidenny13votes+bidenny14votes+bidenny15votes+bidenny16votes+bidenny17votes+bidenny18votes+bidenny19votes+bidenny20votes+bidenny21votes+bidenny22votes+bidenny23votes+bidenny24votes+bidenny25votes+bidenny26votes+bidenny27votes
print("TOTAL TRUMP VOTES: ", totalnyvotestrump/(totalnyvotestrump+totalnyvotesbiden))
print("TOTAL BIDEN VOTES: ", totalnyvotesbiden/(totalnyvotestrump+totalnyvotesbiden))
print("")
print("North Dakota")
print("Trump: ", (len(trumpnd)/(len(trumpnd)+len(bidennd))))
print("Biden: ",(len(bidennd)/(len(trumpnd)+len(bidennd))))
print("North Dakota 1")
print("Trump: ", (len(trumpnd1)/(len(trumpnd1)+len(bidennd1))))
print("votes ", len(trumpnd1))
print("Biden: ",(len(bidennd1)/(len(trumpnd1)+len(bidennd1))))
print("votes ", len(bidennd1))
print("")
print("Montana")
print("Trump: ", (len(trumpmt)/(len(trumpmt)+len(bidenmt))))
print("Biden: ",(len(bidenmt)/(len(trumpmt)+len(bidenmt))))
print("Montana 1")
print("Trump: ", (len(trumpmt1)/(len(trumpmt1)+len(bidenmt1))))
print("votes ", len(trumpmt1))
print("Biden: ",(len(bidenmt1)/(len(trumpmt1)+len(bidenmt1))))
print("votes ", len(bidenmt1))
print("")
print("Wyoming")
print("Trump: ", (len(trumpwy)/(len(trumpwy)+len(bidenwy))))
print("Biden: ",(len(bidenwy)/(len(trumpwy)+len(bidenwy))))
print("Wyoming 1")
print("Trump: ", (len(trumpwy1)/(len(trumpwy1)+len(bidenwy1))))
print("votes ", len(trumpwy1))
print("Biden: ",(len(bidenwy1)/(len(trumpwy1)+len(bidenwy1))))
print("votes ", len(bidenwy1))
print("")
print("Vermont")
print("Trump: ", (len(trumpvt)/(len(trumpvt)+len(bidenvt))))
print("Biden: ",(len(bidenvt)/(len(trumpvt)+len(bidenvt))))
print("Vermont 1")
print("Trump: ", (len(trumpvt1)/(len(trumpvt1)+len(bidenvt1))))
print("votes ", len(trumpvt1))
print("Biden: ",(len(bidenvt1)/(len(trumpvt1)+len(bidenvt1))))
print("votes ", len(bidenvt1))
print("")
print("Ohio")
print("Trump: ", (len(trumpoh)/(len(trumpoh)+len(bidenoh))))
print("Biden: ",(len(bidenoh)/(len(trumpoh)+len(bidenoh))))
print("Ohio 1")
trumpoh1votes = (len(trumpoh1)/(len(trumpoh1)+len(bidenoh1)))*344562
bidenoh1votes = (len(bidenoh1)/(len(trumpoh1)+len(bidenoh1)))*344562
print("Trump: ", (len(trumpoh1)/(len(trumpoh1)+len(bidenoh1))))
print("votes ", trumpoh1votes)
print("Biden: ",(len(bidenoh1)/(len(trumpoh1)+len(bidenoh1))))
print("votes ", bidenoh1votes)
print("Ohio 2")
trumpoh2votes = (len(trumpoh2)/(len(trumpoh2)+len(bidenoh2)))*323124
bidenoh2votes = (len(bidenoh2)/(len(trumpoh2)+len(bidenoh2)))*323124
print("Trump: ", (len(trumpoh2)/(len(trumpoh2)+len(bidenoh2))))
print("votes ", trumpoh2votes)
print("Biden: ",(len(bidenoh2)/(len(trumpoh2)+len(bidenoh2))))
print("votes ", bidenoh2votes)
print("Ohio 3")
trumpoh3votes = (len(trumpoh3)/(len(trumpoh3)+len(bidenoh3)))*277576
bidenoh3votes = (len(bidenoh3)/(len(trumpoh3)+len(bidenoh3)))*277576
print("Trump: ", (len(trumpoh3)/(len(trumpoh3)+len(bidenoh3))))
print("votes ", trumpoh3votes)
print("Biden: ",(len(bidenoh3)/(len(trumpoh3)+len(bidenoh3))))
print("votes ", bidenoh3votes)
print("Ohio 4")
trumpoh4votes = (len(trumpoh4)/(len(trumpoh4)+len(bidenoh4)))*302003
bidenoh4votes = (len(bidenoh4)/(len(trumpoh4)+len(bidenoh4)))*302003
print("Trump: ", (len(trumpoh4)/(len(trumpoh4)+len(bidenoh4))))
print("votes ", trumpoh4votes)
print("Biden: ",(len(bidenoh4)/(len(trumpoh4)+len(bidenoh4))))
print("votes ", bidenoh4votes)
print("Ohio 5")
trumpoh5votes = (len(trumpoh5)/(len(trumpoh5)+len(bidenoh5)))*338081
bidenoh5votes = (len(bidenoh5)/(len(trumpoh5)+len(bidenoh5)))*338081
print("Trump: ", (len(trumpoh5)/(len(trumpoh5)+len(bidenoh5))))
print("votes ", trumpoh5votes)
print("Biden: ",(len(bidenoh5)/(len(trumpoh5)+len(bidenoh5))))
print("votes ", bidenoh5votes)
print("Ohio 6")
trumpoh6votes = (len(trumpoh6)/(len(trumpoh6)+len(bidenoh6)))*296115
bidenoh6votes = (len(bidenoh6)/(len(trumpoh6)+len(bidenoh6)))*296115
print("Trump: ", (len(trumpoh6)/(len(trumpoh6)+len(bidenoh6))))
print("votes ", trumpoh6votes)
print("Biden: ",(len(bidenoh6)/(len(trumpoh6)+len(bidenoh6))))
print("votes ", bidenoh6votes)
print("Ohio 7")
trumpoh7votes = (len(trumpoh7)/(len(trumpoh7)+len(bidenoh7)))*281748
bidenoh7votes = (len(bidenoh7)/(len(trumpoh7)+len(bidenoh7)))*281748
print("Trump: ", (len(trumpoh7)/(len(trumpoh7)+len(bidenoh7))))
print("votes ", trumpoh7votes)
print("Biden: ",(len(bidenoh7)/(len(trumpoh7)+len(bidenoh7))))
print("votes ", bidenoh7votes)
print("Ohio 8")
trumpoh8votes = (len(trumpoh8)/(len(trumpoh8)+len(bidenoh8)))*304766
bidenoh8votes = (len(bidenoh8)/(len(trumpoh8)+len(bidenoh8)))*304766
print("Trump: ", (len(trumpoh8)/(len(trumpoh8)+len(bidenoh8))))
print("votes ", trumpoh8votes)
print("Biden: ",(len(bidenoh8)/(len(trumpoh8)+len(bidenoh8))))
print("votes ", bidenoh8votes)
print("Ohio 9")
trumpoh9votes = (len(trumpoh9)/(len(trumpoh9)+len(bidenoh9)))*274237
bidenoh9votes = (len(bidenoh9)/(len(trumpoh9)+len(bidenoh9)))*274237
print("Trump: ", (len(trumpoh9)/(len(trumpoh9)+len(bidenoh9))))
print("votes ", trumpoh9votes)
print("Biden: ",(len(bidenoh9)/(len(trumpoh9)+len(bidenoh9))))
print("votes ", bidenoh9votes)
print("Ohio 10")
trumpoh10votes = (len(trumpoh10)/(len(trumpoh10)+len(bidenoh10)))*316203
bidenoh10votes = (len(bidenoh10)/(len(trumpoh10)+len(bidenoh10)))*316203
print("Trump: ", (len(trumpoh10)/(len(trumpoh10)+len(bidenoh10))))
print("votes ", trumpoh10votes)
print("Biden: ",(len(bidenoh10)/(len(trumpoh10)+len(bidenoh10))))
print("votes ", bidenoh10votes)
print("Ohio 11")
trumpoh11votes = (len(trumpoh11)/(len(trumpoh11)+len(bidenoh11)))*291351
bidenoh11votes = (len(bidenoh11)/(len(trumpoh11)+len(bidenoh11)))*291351
print("Trump: ", (len(trumpoh11)/(len(trumpoh11)+len(bidenoh11))))
print("votes ", trumpoh11votes)
print("Biden: ",(len(bidenoh11)/(len(trumpoh11)+len(bidenoh11))))
print("votes ", bidenoh11votes)
print("Ohio 12")
trumpoh12votes = (len(trumpoh12)/(len(trumpoh12)+len(bidenoh12)))*353425
bidenoh12votes = (len(bidenoh12)/(len(trumpoh12)+len(bidenoh12)))*353425
print("Trump: ", (len(trumpoh12)/(len(trumpoh12)+len(bidenoh12))))
print("votes ", trumpoh12votes)
print("Biden: ",(len(bidenoh12)/(len(trumpoh12)+len(bidenoh12))))
print("votes ", bidenoh12votes)
print("Ohio 13")
trumpoh13votes = (len(trumpoh13)/(len(trumpoh13)+len(bidenoh13)))*300742
bidenoh13votes = (len(bidenoh13)/(len(trumpoh13)+len(bidenoh13)))*300742
print("Trump: ", (len(trumpoh13)/(len(trumpoh13)+len(bidenoh13))))
print("votes ", trumpoh13votes)
print("Biden: ",(len(bidenoh13)/(len(trumpoh13)+len(bidenoh13))))
print("votes ", bidenoh13votes)
print("Ohio 14")
trumpoh14votes = (len(trumpoh14)/(len(trumpoh14)+len(bidenoh14)))*342165
bidenoh14votes = (len(bidenoh14)/(len(trumpoh14)+len(bidenoh14)))*342165
print("Trump: ", (len(trumpoh14)/(len(trumpoh14)+len(bidenoh14))))
print("votes ", trumpoh14votes)
print("Biden: ",(len(bidenoh14)/(len(trumpoh14)+len(bidenoh14))))
print("votes ", bidenoh14votes)
print("Ohio 15")
trumpoh15votes = (len(trumpoh15)/(len(trumpoh15)+len(bidenoh15)))*326458
bidenoh15votes = (len(bidenoh15)/(len(trumpoh15)+len(bidenoh15)))*326458
print("Trump: ", (len(trumpoh15)/(len(trumpoh15)+len(bidenoh15))))
print("votes ", trumpoh15votes)
print("Biden: ",(len(bidenoh15)/(len(trumpoh15)+len(bidenoh15))))
print("votes ", bidenoh15votes)
print("Ohio 16")
trumpoh16votes = (len(trumpoh16)/(len(trumpoh16)+len(bidenoh16)))*338791
bidenoh16votes = (len(bidenoh16)/(len(trumpoh16)+len(bidenoh16)))*338791
print("Trump: ", (len(trumpoh16)/(len(trumpoh16)+len(bidenoh16))))
print("votes ", trumpoh16votes)
print("Biden: ",(len(bidenoh16)/(len(trumpoh16)+len(bidenoh16))))
print("votes ", bidenoh16votes)
totalohvotestrump = trumpoh1votes+trumpoh2votes+trumpoh3votes+trumpoh4votes+trumpoh5votes+trumpoh6votes+trumpoh7votes+trumpoh8votes+trumpoh9votes+trumpoh10votes+trumpoh11votes+trumpoh12votes+trumpoh13votes+trumpoh14votes+trumpoh15votes+trumpoh16votes
totalohvotesbiden = bidenoh1votes+bidenoh2votes+bidenoh3votes+bidenoh4votes+bidenoh5votes+bidenoh6votes+bidenoh7votes+bidenoh8votes+bidenoh9votes+bidenoh10votes+bidenoh11votes+bidenoh12votes+bidenoh13votes+bidenoh14votes+bidenoh15votes+bidenoh16votes
print("TOTAL TRUMP VOTES: ", totalohvotestrump/(totalohvotestrump+totalohvotesbiden))
print("TOTAL BIDEN VOTES: ", totalohvotesbiden/(totalohvotestrump+totalohvotesbiden))
print("")
print("Oregon")
print("Trump: ", (len(trumpor)/(len(trumpor)+len(bidenor))))
print("Biden: ",(len(bidenor)/(len(trumpor)+len(bidenor))))
print("Oregon 1")
trumpor1votes = (len(trumpor1)/(len(trumpor1)+len(bidenor1)))*336685
bidenor1votes = (len(bidenor1)/(len(trumpor1)+len(bidenor1)))*336685
print("Trump: ", (len(trumpor1)/(len(trumpor1)+len(bidenor1))))
print("votes ", trumpor1votes)
print("Biden: ",(len(bidenor1)/(len(trumpor1)+len(bidenor1))))
print("votes ", bidenor1votes)
print("Oregon 2")
trumpor2votes = (len(trumpor2)/(len(trumpor2)+len(bidenor2)))*370562
bidenor2votes = (len(bidenor2)/(len(trumpor2)+len(bidenor2)))*370562
print("Trump: ", (len(trumpor2)/(len(trumpor2)+len(bidenor2))))
print("votes ", trumpor2votes)
print("Biden: ",(len(bidenor2)/(len(trumpor2)+len(bidenor2))))
print("votes ", bidenor2votes)
print("Oregon 3")
trumpor3votes = (len(trumpor3)/(len(trumpor3)+len(bidenor3)))*352976
bidenor3votes = (len(bidenor3)/(len(trumpor3)+len(bidenor3)))*352976
print("Trump: ", (len(trumpor3)/(len(trumpor3)+len(bidenor3))))
print("votes ", trumpor3votes)
print("Biden: ",(len(bidenor3)/(len(trumpor3)+len(bidenor3))))
print("votes ", bidenor3votes)
print("Oregon 4")
trumpor4votes = (len(trumpor4)/(len(trumpor4)+len(bidenor4)))*371713
bidenor4votes = (len(bidenor4)/(len(trumpor4)+len(bidenor4)))*371713
print("Trump: ", (len(trumpor4)/(len(trumpor4)+len(bidenor4))))
print("votes ", trumpor4votes)
print("Biden: ",(len(bidenor4)/(len(trumpor4)+len(bidenor4))))
print("votes ", bidenor4votes)
print("Oregon 5")
trumpor5votes = (len(trumpor5)/(len(trumpor5)+len(bidenor5)))*322244
bidenor5votes = (len(bidenor5)/(len(trumpor5)+len(bidenor5)))*322244
print("Trump: ", (len(trumpor5)/(len(trumpor5)+len(bidenor5))))
print("votes ", trumpor5votes)
print("Biden: ",(len(bidenor5)/(len(trumpor5)+len(bidenor5))))
print("votes ", bidenor5votes)
totalorvotestrump = trumpor1votes+trumpor2votes+trumpor3votes+trumpor4votes+trumpor5votes
totalorvotesbiden = bidenor1votes+bidenor2votes+bidenor3votes+bidenor4votes+bidenor5votes
print("TOTAL TRUMP VOTES: ", totalorvotestrump/(totalorvotestrump+totalorvotesbiden))
print("TOTAL BIDEN VOTES: ", totalorvotesbiden/(totalorvotestrump+totalorvotesbiden))
print("")
print("Hawaii")
print("Trump: ", (len(trumphi)/(len(trumphi)+len(bidenhi))))
print("Biden: ",(len(bidenhi)/(len(trumphi)+len(bidenhi))))
print("Hawaii 1")
trumphi1votes = (len(trumphi1)/(len(trumphi1)+len(bidenhi1)))*173112
bidenhi1votes = (len(bidenhi1)/(len(trumphi1)+len(bidenhi1)))*173112
print("Trump: ", (len(trumphi1)/(len(trumphi1)+len(bidenhi1))))
print("votes ", len(trumphi1))
print("Biden: ",(len(bidenhi1)/(len(trumphi1)+len(bidenhi1))))
print("votes ", len(bidenhi1))
print("Hawaii 2")
trumphi2votes = (len(trumphi2)/(len(trumphi2)+len(bidenhi2)))*210491
bidenhi2votes = (len(bidenhi2)/(len(trumphi2)+len(bidenhi2)))*210491
print("Trump: ", (len(trumphi2)/(len(trumphi2)+len(bidenhi2))))
print("votes ", len(trumphi2))
print("Biden: ",(len(bidenhi2)/(len(trumphi2)+len(bidenhi2))))
print("votes ", len(bidenhi2))
totalhivotestrump = trumphi1votes+trumphi2votes
totalhivotesbiden = bidenhi1votes+bidenhi2votes
print("TOTAL TRUMP VOTES: ", totalhivotestrump/(totalhivotestrump+totalhivotesbiden))
print("TOTAL BIDEN VOTES: ", totalhivotesbiden/(totalhivotestrump+totalhivotesbiden))
print("")
print("Texas")
print("Trump: ", (len(trumptx)/(len(trumptx)+len(bidentx))))
print("Biden: ",(len(bidentx)/(len(trumptx)+len(bidentx))))
print("Texas 1")
trumptx1votes = (len(trumptx1)/(len(trumptx1)+len(bidentx1)))*1
bidentx1votes = (len(bidentx1)/(len(trumptx1)+len(bidentx1)))*1
print("Trump: ", (len(trumptx1)/(len(trumptx1)+len(bidentx1))))
print("votes ", trumptx1votes)
print("Biden: ",(len(bidentx1)/(len(trumptx1)+len(bidentx1))))
print("votes ", bidentx1votes)
print("Texas 2")
trumptx2votes = (len(trumptx2)/(len(trumptx2)+len(bidentx2)))*1
bidentx2votes = (len(bidentx2)/(len(trumptx2)+len(bidentx2)))*1
print("Trump: ", (len(trumptx2)/(len(trumptx2)+len(bidentx2))))
print("votes ", trumptx2votes)
print("Biden: ",(len(bidentx2)/(len(trumptx2)+len(bidentx2))))
print("votes ", bidentx2votes)
print("Texas 3")
trumptx3votes = (len(trumptx3)/(len(trumptx3)+len(bidentx3)))*1
bidentx3votes = (len(bidentx3)/(len(trumptx3)+len(bidentx3)))*1
print("Trump: ", (len(trumptx3)/(len(trumptx3)+len(bidentx3))))
print("votes ", trumptx3votes)
print("Biden: ",(len(bidentx3)/(len(trumptx3)+len(bidentx3))))
print("votes ", bidentx3votes)
print("Texas 4")
trumptx4votes = (len(trumptx4)/(len(trumptx4)+len(bidentx4)))*1
bidentx4votes = (len(bidentx4)/(len(trumptx4)+len(bidentx4)))*1
print("Trump: ", (len(trumptx4)/(len(trumptx4)+len(bidentx4))))
print("votes ", trumptx4votes)
print("Biden: ",(len(bidentx4)/(len(trumptx4)+len(bidentx4))))
print("votes ", bidentx4votes)
print("Texas 5")
trumptx5votes = (len(trumptx5)/(len(trumptx5)+len(bidentx5)))*1
bidentx5votes = (len(bidentx5)/(len(trumptx5)+len(bidentx5)))*1
print("Trump: ", (len(trumptx5)/(len(trumptx5)+len(bidentx5))))
print("votes ", trumptx5votes)
print("Biden: ",(len(bidentx5)/(len(trumptx5)+len(bidentx5))))
print("votes ", bidentx5votes)
print("Texas 6")
trumptx6votes = (len(trumptx6)/(len(trumptx6)+len(bidentx6)))*1
bidentx6votes = (len(bidentx6)/(len(trumptx6)+len(bidentx6)))*1
print("Trump: ", (len(trumptx6)/(len(trumptx6)+len(bidentx6))))
print("votes ", trumptx6votes)
print("Biden: ",(len(bidentx6)/(len(trumptx6)+len(bidentx6))))
print("votes ", bidentx6votes)
print("Texas 7")
trumptx7votes = (len(trumptx7)/(len(trumptx7)+len(bidentx7)))*1
bidentx7votes = (len(bidentx7)/(len(trumptx7)+len(bidentx7)))*1
print("Trump: ", (len(trumptx7)/(len(trumptx7)+len(bidentx7))))
print("votes ", trumptx7votes)
print("Biden: ",(len(bidentx7)/(len(trumptx7)+len(bidentx7))))
print("votes ", bidentx7votes)
print("Texas 8")
trumptx8votes = (len(trumptx8)/(len(trumptx8)+len(bidentx8)))*1
bidentx8votes = (len(bidentx8)/(len(trumptx8)+len(bidentx8)))*1
print("Trump: ", (len(trumptx8)/(len(trumptx8)+len(bidentx8))))
print("votes ", trumptx8votes)
print("Biden: ",(len(bidentx8)/(len(trumptx8)+len(bidentx8))))
print("votes ", bidentx8votes)
print("Texas 9")
trumptx9votes = (len(trumptx9)/(len(trumptx9)+len(bidentx9)))*1
bidentx9votes = (len(bidentx9)/(len(trumptx9)+len(bidentx9)))*1
print("Trump: ", (len(trumptx9)/(len(trumptx9)+len(bidentx9))))
print("votes ", trumptx9votes)
print("Biden: ",(len(bidentx9)/(len(trumptx9)+len(bidentx9))))
print("votes ", bidentx9votes)
print("Texas 10")
trumptx10votes = (len(trumptx10)/(len(trumptx10)+len(bidentx10)))*1
bidentx10votes = (len(bidentx10)/(len(trumptx10)+len(bidentx10)))*1
print("Trump: ", (len(trumptx10)/(len(trumptx10)+len(bidentx10))))
print("votes ", trumptx10votes)
print("Biden: ",(len(bidentx10)/(len(trumptx10)+len(bidentx10))))
print("votes ", bidentx10votes)
print("Texas 11")
trumptx11votes = (len(trumptx11)/(len(trumptx11)+len(bidentx11)))*1
bidentx11votes = (len(bidentx11)/(len(trumptx11)+len(bidentx11)))*1
print("Trump: ", (len(trumptx11)/(len(trumptx11)+len(bidentx11))))
print("votes ", trumptx11votes)
print("Biden: ",(len(bidentx11)/(len(trumptx11)+len(bidentx11))))
print("votes ", bidentx11votes)
print("Texas 12")
trumptx12votes = (len(trumptx12)/(len(trumptx12)+len(bidentx12)))*1
bidentx12votes = (len(bidentx12)/(len(trumptx12)+len(bidentx12)))*1
print("Trump: ", (len(trumptx12)/(len(trumptx12)+len(bidentx12))))
print("votes ", trumptx12votes)
print("Biden: ",(len(bidentx12)/(len(trumptx12)+len(bidentx12))))
print("votes ", bidentx12votes)
print("Texas 13")
trumptx13votes = (len(trumptx13)/(len(trumptx13)+len(bidentx13)))*1
bidentx13votes = (len(bidentx13)/(len(trumptx13)+len(bidentx13)))*1
print("Trump: ", (len(trumptx13)/(len(trumptx13)+len(bidentx13))))
print("votes ", trumptx13votes)
print("Biden: ",(len(bidentx13)/(len(trumptx13)+len(bidentx13))))
print("votes ", bidentx13votes)
print("Texas 14")
trumptx14votes = (len(trumptx14)/(len(trumptx14)+len(bidentx14)))*1
bidentx14votes = (len(bidentx14)/(len(trumptx14)+len(bidentx14)))*1
print("Trump: ", (len(trumptx14)/(len(trumptx14)+len(bidentx14))))
print("votes ", trumptx14votes)
print("Biden: ",(len(bidentx14)/(len(trumptx14)+len(bidentx14))))
print("votes ", bidentx14votes)
print("Texas 15")
trumptx15votes = (len(trumptx15)/(len(trumptx15)+len(bidentx15)))*1
bidentx15votes = (len(bidentx15)/(len(trumptx15)+len(bidentx15)))*1
print("Trump: ", (len(trumptx15)/(len(trumptx15)+len(bidentx15))))
print("votes ", trumptx15votes)
print("Biden: ",(len(bidentx15)/(len(trumptx15)+len(bidentx15))))
print("votes ", bidentx15votes)
print("Texas 16")
trumptx16votes = (len(trumptx16)/(len(trumptx16)+len(bidentx16)))*1
bidentx16votes = (len(bidentx16)/(len(trumptx16)+len(bidentx16)))*1
print("Trump: ", (len(trumptx16)/(len(trumptx16)+len(bidentx16))))
print("votes ", trumptx16votes)
print("Biden: ",(len(bidentx16)/(len(trumptx16)+len(bidentx16))))
print("votes ", bidentx16votes)
print("Texas 17")
trumptx17votes = (len(trumptx17)/(len(trumptx17)+len(bidentx17)))*1
bidentx17votes = (len(bidentx17)/(len(trumptx17)+len(bidentx17)))*1
print("Trump: ", (len(trumptx17)/(len(trumptx17)+len(bidentx17))))
print("votes ", trumptx17votes)
print("Biden: ",(len(bidentx17)/(len(trumptx17)+len(bidentx17))))
print("votes ", bidentx17votes)
print("Texas 18")
trumptx18votes = (len(trumptx18)/(len(trumptx18)+len(bidentx18)))*1
bidentx18votes = (len(bidentx18)/(len(trumptx18)+len(bidentx18)))*1
print("Trump: ", (len(trumptx18)/(len(trumptx18)+len(bidentx18))))
print("votes ", trumptx18votes)
print("Biden: ",(len(bidentx18)/(len(trumptx18)+len(bidentx18))))
print("votes ", bidentx18votes)
print("Texas 19")
trumptx19votes = (len(trumptx19)/(len(trumptx19)+len(bidentx19)))*1
bidentx19votes = (len(bidentx19)/(len(trumptx19)+len(bidentx19)))*1
print("Trump: ", (len(trumptx19)/(len(trumptx19)+len(bidentx19))))
print("votes ", trumptx19votes)
print("Biden: ",(len(bidentx19)/(len(trumptx19)+len(bidentx19))))
print("votes ", bidentx19votes)
print("Texas 20")
trumptx20votes = (len(trumptx20)/(len(trumptx20)+len(bidentx20)))*1
bidentx20votes = (len(bidentx20)/(len(trumptx20)+len(bidentx20)))*1
print("Trump: ", (len(trumptx20)/(len(trumptx20)+len(bidentx20))))
print("votes ", trumptx20votes)
print("Biden: ",(len(bidentx20)/(len(trumptx20)+len(bidentx20))))
print("votes ", bidentx20votes)
print("Texas 21")
trumptx21votes = (len(trumptx21)/(len(trumptx21)+len(bidentx21)))*1
bidentx21votes = (len(bidentx21)/(len(trumptx21)+len(bidentx21)))*1
print("Trump: ", (len(trumptx21)/(len(trumptx21)+len(bidentx21))))
print("votes ", trumptx21votes)
print("Biden: ",(len(bidentx21)/(len(trumptx21)+len(bidentx21))))
print("votes ", bidentx21votes)
print("Texas 22")
trumptx22votes = (len(trumptx22)/(len(trumptx22)+len(bidentx22)))*1
bidentx22votes = (len(bidentx22)/(len(trumptx22)+len(bidentx22)))*1
print("Trump: ", (len(trumptx22)/(len(trumptx22)+len(bidentx22))))
print("votes ", trumptx22votes)
print("Biden: ",(len(bidentx22)/(len(trumptx22)+len(bidentx22))))
print("votes ", bidentx22votes)
print("Texas 23")
trumptx23votes = (len(trumptx23)/(len(trumptx23)+len(bidentx23)))*1
bidentx23votes = (len(bidentx23)/(len(trumptx23)+len(bidentx23)))*1
print("Trump: ", (len(trumptx23)/(len(trumptx23)+len(bidentx23))))
print("votes ", trumptx23votes)
print("Biden: ",(len(bidentx23)/(len(trumptx23)+len(bidentx23))))
print("votes ", bidentx23votes)
print("Texas 24")
trumptx24votes = (len(trumptx24)/(len(trumptx24)+len(bidentx24)))*1
bidentx24votes = (len(bidentx24)/(len(trumptx24)+len(bidentx24)))*1
print("Trump: ", (len(trumptx24)/(len(trumptx24)+len(bidentx24))))
print("votes ", trumptx24votes)
print("Biden: ",(len(bidentx24)/(len(trumptx24)+len(bidentx24))))
print("votes ", bidentx24votes)
print("Texas 25")
trumptx25votes = (len(trumptx25)/(len(trumptx25)+len(bidentx25)))*1
bidentx25votes = (len(bidentx25)/(len(trumptx25)+len(bidentx25)))*1
print("Trump: ", (len(trumptx25)/(len(trumptx25)+len(bidentx25))))
print("votes ", trumptx25votes)
print("Biden: ",(len(bidentx25)/(len(trumptx25)+len(bidentx25))))
print("votes ", bidentx25votes)
print("Texas 26")
trumptx26votes = (len(trumptx26)/(len(trumptx26)+len(bidentx26)))*1
bidentx26votes = (len(bidentx26)/(len(trumptx26)+len(bidentx26)))*1
print("Trump: ", (len(trumptx26)/(len(trumptx26)+len(bidentx26))))
print("votes ", trumptx26votes)
print("Biden: ",(len(bidentx26)/(len(trumptx26)+len(bidentx26))))
print("votes ", bidentx26votes)
print("Texas 27")
trumptx27votes = (len(trumptx27)/(len(trumptx27)+len(bidentx27)))*1
bidentx27votes = (len(bidentx27)/(len(trumptx27)+len(bidentx27)))*1
print("Trump: ", (len(trumptx27)/(len(trumptx27)+len(bidentx27))))
print("votes ", trumptx27votes)
print("Biden: ",(len(bidentx27)/(len(trumptx27)+len(bidentx27))))
print("votes ", bidentx27votes)
print("Texas 28")
trumptx28votes = (len(trumptx28)/(len(trumptx28)+len(bidentx28)))*1
bidentx28votes = (len(bidentx28)/(len(trumptx28)+len(bidentx28)))*1
print("Trump: ", (len(trumptx28)/(len(trumptx28)+len(bidentx28))))
print("votes ", trumptx28votes)
print("Biden: ",(len(bidentx28)/(len(trumptx28)+len(bidentx28))))
print("votes ", bidentx28votes)
print("Texas 29")
trumptx29votes = (len(trumptx29)/(len(trumptx29)+len(bidentx29)))*1
bidentx29votes = (len(bidentx29)/(len(trumptx29)+len(bidentx29)))*1
print("Trump: ", (len(trumptx29)/(len(trumptx29)+len(bidentx29))))
print("votes ", trumptx29votes)
print("Biden: ",(len(bidentx29)/(len(trumptx29)+len(bidentx29))))
print("votes ", bidentx29votes)
print("Texas 30")
trumptx30votes = (len(trumptx30)/(len(trumptx30)+len(bidentx30)))*1
bidentx30votes = (len(bidentx30)/(len(trumptx30)+len(bidentx30)))*1
print("Trump: ", (len(trumptx30)/(len(trumptx30)+len(bidentx30))))
print("votes ", trumptx30votes)
print("Biden: ",(len(bidentx30)/(len(trumptx30)+len(bidentx30))))
print("votes ", bidentx30votes)
print("Texas 31")
trumptx31votes = (len(trumptx31)/(len(trumptx31)+len(bidentx31)))*1
bidentx31votes = (len(bidentx31)/(len(trumptx31)+len(bidentx31)))*1
print("Trump: ", (len(trumptx31)/(len(trumptx31)+len(bidentx31))))
print("votes ", trumptx31votes)
print("Biden: ",(len(bidentx31)/(len(trumptx31)+len(bidentx31))))
print("votes ", bidentx31votes)
print("Texas 32")
trumptx32votes = (len(trumptx32)/(len(trumptx32)+len(bidentx32)))*1
bidentx32votes = (len(bidentx32)/(len(trumptx32)+len(bidentx32)))*1
print("Trump: ", (len(trumptx32)/(len(trumptx32)+len(bidentx32))))
print("votes ", trumptx32votes)
print("Biden: ",(len(bidentx32)/(len(trumptx32)+len(bidentx32))))
print("votes ", bidentx32votes)
print("Texas 33")
trumptx33votes = (len(trumptx33)/(len(trumptx33)+len(bidentx33)))*1
bidentx33votes = (len(bidentx33)/(len(trumptx33)+len(bidentx33)))*1
print("Trump: ", (len(trumptx33)/(len(trumptx33)+len(bidentx33))))
print("votes ", trumptx33votes)
print("Biden: ",(len(bidentx33)/(len(trumptx33)+len(bidentx33))))
print("votes ", bidentx33votes)
print("Texas 34")
trumptx34votes = (len(trumptx34)/(len(trumptx34)+len(bidentx34)))*1
bidentx34votes = (len(bidentx34)/(len(trumptx34)+len(bidentx34)))*1
print("Trump: ", (len(trumptx34)/(len(trumptx34)+len(bidentx34))))
print("votes ", trumptx34votes)
print("Biden: ",(len(bidentx34)/(len(trumptx34)+len(bidentx34))))
print("votes ", bidentx34votes)
print("Texas 35")
trumptx35votes = (len(trumptx35)/(len(trumptx35)+len(bidentx35)))*1
bidentx35votes = (len(bidentx35)/(len(trumptx35)+len(bidentx35)))*1
print("Trump: ", (len(trumptx35)/(len(trumptx35)+len(bidentx35))))
print("votes ", trumptx35votes)
print("Biden: ",(len(bidentx35)/(len(trumptx35)+len(bidentx35))))
print("votes ", bidentx35votes)
print("Texas 36")
trumptx36votes = (len(trumptx36)/(len(trumptx36)+len(bidentx36)))*1
bidentx36votes = (len(bidentx36)/(len(trumptx36)+len(bidentx36)))*1
print("Trump: ", (len(trumptx36)/(len(trumptx36)+len(bidentx36))))
print("votes ", trumptx36votes)
print("Biden: ",(len(bidentx36)/(len(trumptx36)+len(bidentx36))))
print("votes ", bidentx36votes)
totaltxvotestrump = trumptx1votes+trumptx2votes+trumptx3votes+trumptx4votes+trumptx5votes+trumptx6votes+trumptx7votes+trumptx8votes+trumptx9votes+trumptx10votes+trumptx11votes+trumptx12votes+trumptx13votes+trumptx14votes+trumptx15votes+trumptx16votes+trumptx17votes+trumptx18votes+trumptx19votes+trumptx20votes+trumptx21votes+trumptx22votes+trumptx23votes+trumptx24votes+trumptx25votes+trumptx26votes+trumptx27votes+trumptx28votes+trumptx29votes+trumptx30votes+trumptx31votes+trumptx32votes+trumptx33votes+trumptx34votes+trumptx35votes+trumptx36votes
totaltxvotesbiden = bidentx1votes+bidentx2votes+bidentx3votes+bidentx4votes+bidentx5votes+bidentx6votes+bidentx7votes+bidentx8votes+bidentx9votes+bidentx10votes+bidentx11votes+bidentx12votes+bidentx13votes+bidentx14votes+bidentx15votes+bidentx16votes+bidentx17votes+bidentx18votes+bidentx19votes+bidentx20votes+bidentx21votes+bidentx22votes+bidentx23votes+bidentx24votes+bidentx25votes+bidentx26votes+bidentx27votes+bidentx28votes+bidentx29votes+bidentx30votes+bidentx31votes+bidentx32votes+bidentx33votes+bidentx34votes+bidentx35votes+bidentx36votes
print("TOTAL TRUMP VOTES: ", totaltxvotestrump/(totaltxvotestrump+totaltxvotesbiden))
print("TOTAL BIDEN VOTES: ", totaltxvotesbiden/(totaltxvotestrump+totaltxvotesbiden))
print("")
print("Kentucky")
print("Trump: ", (len(trumpky)/(len(trumpky)+len(bidenky))))
print("Biden: ",(len(bidenky)/(len(trumpky)+len(bidenky))))
print("Kentucky 1")
trumpky1votes = (len(trumpky1)/(len(trumpky1)+len(bidenky1)))*1
bidenky1votes = (len(bidenky1)/(len(trumpky1)+len(bidenky1)))*1
print("Trump: ", (len(trumpky1)/(len(trumpky1)+len(bidenky1))))
print("votes ", trumpky1votes)
print("Biden: ",(len(bidenky1)/(len(trumpky1)+len(bidenky1))))
print("votes ", bidenky1votes)
print("Kentucky 2")
trumpky2votes = (len(trumpky2)/(len(trumpky2)+len(bidenky2)))*1
bidenky2votes = (len(bidenky2)/(len(trumpky2)+len(bidenky2)))*1
print("Trump: ", (len(trumpky2)/(len(trumpky2)+len(bidenky2))))
print("votes ", trumpky2votes)
print("Biden: ",(len(bidenky2)/(len(trumpky2)+len(bidenky2))))
print("votes ", bidenky2votes)
print("Kentucky 3")
trumpky3votes = (len(trumpky3)/(len(trumpky3)+len(bidenky3)))*1
bidenky3votes = (len(bidenky3)/(len(trumpky3)+len(bidenky3)))*1
print("Trump: ", (len(trumpky3)/(len(trumpky3)+len(bidenky3))))
print("votes ", trumpky3votes)
print("Biden: ",(len(bidenky3)/(len(trumpky3)+len(bidenky3))))
print("votes ", bidenky3votes)
print("Kentucky 4")
trumpky4votes = (len(trumpky4)/(len(trumpky4)+len(bidenky4)))*1
bidenky4votes = (len(bidenky4)/(len(trumpky4)+len(bidenky4)))*1
print("Trump: ", (len(trumpky4)/(len(trumpky4)+len(bidenky4))))
print("votes ", trumpky4votes)
print("Biden: ",(len(bidenky4)/(len(trumpky4)+len(bidenky4))))
print("votes ", bidenky4votes)
print("Kentucky 5")
trumpky5votes = (len(trumpky5)/(len(trumpky5)+len(bidenky5)))*1
bidenky5votes = (len(bidenky5)/(len(trumpky5)+len(bidenky5)))*1
print("Trump: ", (len(trumpky5)/(len(trumpky5)+len(bidenky5))))
print("votes ", trumpky5votes)
print("Biden: ",(len(bidenky5)/(len(trumpky5)+len(bidenky5))))
print("votes ", bidenky5votes)
print("Kentucky 6")
trumpky6votes = (len(trumpky6)/(len(trumpky6)+len(bidenky6)))*1
bidenky6votes = (len(bidenky6)/(len(trumpky6)+len(bidenky6)))*1
print("Trump: ", (len(trumpky6)/(len(trumpky6)+len(bidenky6))))
print("votes ", trumpky6votes)
print("Biden: ",(len(bidenky6)/(len(trumpky6)+len(bidenky6))))
print("votes ", bidenky6votes)
totalkyvotestrump = trumpky1votes+trumpky2votes+trumpky3votes+trumpky4votes+trumpky5votes+trumpky6votes
totalkyvotesbiden = bidenky1votes+bidenky2votes+bidenky3votes+bidenky4votes+bidenky5votes+bidenky6votes
print("TOTAL TRUMP VOTES: ", totalkyvotestrump/(totalkyvotestrump+totalkyvotesbiden))
print("TOTAL BIDEN VOTES: ", totalkyvotesbiden/(totalkyvotestrump+totalkyvotesbiden))
print("")
print("Tennessee")
print("Trump: ", (len(trumptn)/(len(trumptn)+len(bidentn))))
print("Biden: ",(len(bidentn)/(len(trumptn)+len(bidentn))))
print("Tennessee 1")
trumptn1votes = (len(trumptn1)/(len(trumptn1)+len(bidentn1)))*235076
bidentn1votes = (len(bidentn1)/(len(trumptn1)+len(bidentn1)))*235076
print("Trump: ", (len(trumptn1)/(len(trumptn1)+len(bidentn1))))
print("votes ", trumptn1votes)
print("Biden: ",(len(bidentn1)/(len(trumptn1)+len(bidentn1))))
print("votes ", bidentn1votes)
print("Tennessee 2")
trumptn2votes = (len(trumptn2)/(len(trumptn2)+len(bidentn2)))*280686
bidentn2votes = (len(bidentn2)/(len(trumptn2)+len(bidentn2)))*280686
print("Trump: ", (len(trumptn2)/(len(trumptn2)+len(bidentn2))))
print("votes ", trumptn2votes)
print("Biden: ",(len(bidentn2)/(len(trumptn2)+len(bidentn2))))
print("votes ", bidentn2votes)
print("Tennessee 3")
trumptn3votes = (len(trumptn3)/(len(trumptn3)+len(bidentn3)))*253104
bidentn3votes = (len(bidentn3)/(len(trumptn3)+len(bidentn3)))*253104
print("Trump: ", (len(trumptn3)/(len(trumptn3)+len(bidentn3))))
print("votes ", trumptn3votes)
print("Biden: ",(len(bidentn3)/(len(trumptn3)+len(bidentn3))))
print("votes ", bidentn3votes)
print("Tennessee 4")
trumptn4votes = (len(trumptn4)/(len(trumptn4)+len(bidentn4)))*254612
bidentn4votes = (len(bidentn4)/(len(trumptn4)+len(bidentn4)))*254612
print("Trump: ", (len(trumptn4)/(len(trumptn4)+len(bidentn4))))
print("votes ", trumptn4votes)
print("Biden: ",(len(bidentn4)/(len(trumptn4)+len(bidentn4))))
print("votes ", bidentn4votes)
print("Tennessee 5")
trumptn5votes = (len(trumptn5)/(len(trumptn5)+len(bidentn5)))*272949
bidentn5votes = (len(bidentn5)/(len(trumptn5)+len(bidentn5)))*272949
print("Trump: ", (len(trumptn5)/(len(trumptn5)+len(bidentn5))))
print("votes ", trumptn5votes)
print("Biden: ",(len(bidentn5)/(len(trumptn5)+len(bidentn5))))
print("votes ", bidentn5votes)
print("Tennessee 6")
trumptn6votes = (len(trumptn6)/(len(trumptn6)+len(bidentn6)))*263978
bidentn6votes = (len(bidentn6)/(len(trumptn6)+len(bidentn6)))*263978
print("Trump: ", (len(trumptn6)/(len(trumptn6)+len(bidentn6))))
print("votes ", trumptn6votes)
print("Biden: ",(len(bidentn6)/(len(trumptn6)+len(bidentn6))))
print("votes ", bidentn6votes)
print("Tennessee 7")
trumptn7votes = (len(trumptn7)/(len(trumptn7)+len(bidentn7)))*263995
bidentn7votes = (len(bidentn7)/(len(trumptn7)+len(bidentn7)))*263995
print("Trump: ", (len(trumptn7)/(len(trumptn7)+len(bidentn7))))
print("votes ", trumptn7votes)
print("Biden: ",(len(bidentn7)/(len(trumptn7)+len(bidentn7))))
print("votes ", bidentn7votes)
print("Tennessee 8")
trumptn8votes = (len(trumptn8)/(len(trumptn8)+len(bidentn8)))*263779
bidentn8votes = (len(bidentn8)/(len(trumptn8)+len(bidentn8)))*263779
print("Trump: ", (len(trumptn8)/(len(trumptn8)+len(bidentn8))))
print("votes ", trumptn8votes)
print("Biden: ",(len(bidentn8)/(len(trumptn8)+len(bidentn8))))
print("votes ", bidentn8votes)
print("Tennessee 9")
trumptn9votes = (len(trumptn9)/(len(trumptn9)+len(bidentn9)))*210491
bidentn9votes = (len(bidentn9)/(len(trumptn9)+len(bidentn9)))*210491
print("Trump: ", (len(trumptn9)/(len(trumptn9)+len(bidentn9))))
print("votes ", trumptn9votes)
print("Biden: ",(len(bidentn9)/(len(trumptn9)+len(bidentn9))))
print("votes ", bidentn9votes)
totaltnvotestrump = trumptn1votes+trumptn2votes+trumptn3votes+trumptn4votes+trumptn5votes+trumptn6votes+trumptn7votes+trumptn8votes+trumptn9votes
totaltnvotesbiden = bidentn1votes+bidentn2votes+bidentn3votes+bidentn4votes+bidentn5votes+bidentn6votes+bidentn7votes+bidentn8votes+bidentn9votes
print("TOTAL TRUMP VOTES: ", totaltnvotestrump/(totaltnvotestrump+totaltnvotesbiden))
print("TOTAL BIDEN VOTES: ", totaltnvotesbiden/(totaltnvotestrump+totaltnvotesbiden))
print("")
print("Wisconsin")
print("Trump: ", (len(trumpwi)/(len(trumpwi)+len(bidenwi))))
print("Biden: ",(len(bidenwi)/(len(trumpwi)+len(bidenwi))))
print("Wisconsin 1")
trumpwi1votes = (len(trumpwi1)/(len(trumpwi1)+len(bidenwi1)))*1
bidenwi1votes = (len(bidenwi1)/(len(trumpwi1)+len(bidenwi1)))*1
print("Trump: ", (len(trumpwi1)/(len(trumpwi1)+len(bidenwi1))))
print("votes ", trumpwi1votes)
print("Biden: ",(len(bidenwi1)/(len(trumpwi1)+len(bidenwi1))))
print("votes ", bidenwi1votes)
print("Wisconsin 2")
trumpwi2votes = (len(trumpwi2)/(len(trumpwi2)+len(bidenwi2)))*1
bidenwi2votes = (len(bidenwi2)/(len(trumpwi2)+len(bidenwi2)))*1
print("Trump: ", (len(trumpwi2)/(len(trumpwi2)+len(bidenwi2))))
print("votes ", trumpwi2votes)
print("Biden: ",(len(bidenwi2)/(len(trumpwi2)+len(bidenwi2))))
print("votes ", bidenwi2votes)
print("Wisconsin 3")
trumpwi3votes = (len(trumpwi3)/(len(trumpwi3)+len(bidenwi3)))*1
bidenwi3votes = (len(bidenwi3)/(len(trumpwi3)+len(bidenwi3)))*1
print("Trump: ", (len(trumpwi3)/(len(trumpwi3)+len(bidenwi3))))
print("votes ", trumpwi3votes)
print("Biden: ",(len(bidenwi3)/(len(trumpwi3)+len(bidenwi3))))
print("votes ", bidenwi3votes)
print("Wisconsin 4")
trumpwi4votes = (len(trumpwi4)/(len(trumpwi4)+len(bidenwi4)))*1
bidenwi4votes = (len(bidenwi4)/(len(trumpwi4)+len(bidenwi4)))*1
print("Trump: ", (len(trumpwi4)/(len(trumpwi4)+len(bidenwi4))))
print("votes ", trumpwi4votes)
print("Biden: ",(len(bidenwi4)/(len(trumpwi4)+len(bidenwi4))))
print("votes ", bidenwi4votes)
print("Wisconsin 5")
trumpwi5votes = (len(trumpwi5)/(len(trumpwi5)+len(bidenwi5)))*1
bidenwi5votes = (len(bidenwi5)/(len(trumpwi5)+len(bidenwi5)))*1
print("Trump: ", (len(trumpwi5)/(len(trumpwi5)+len(bidenwi5))))
print("votes ", trumpwi5votes)
print("Biden: ",(len(bidenwi5)/(len(trumpwi5)+len(bidenwi5))))
print("votes ", bidenwi5votes)
print("Wisconsin 6")
trumpwi6votes = (len(trumpwi6)/(len(trumpwi6)+len(bidenwi6)))*1
bidenwi6votes = (len(bidenwi6)/(len(trumpwi6)+len(bidenwi6)))*1
print("Trump: ", (len(trumpwi6)/(len(trumpwi6)+len(bidenwi6))))
print("votes ", trumpwi6votes)
print("Biden: ",(len(bidenwi6)/(len(trumpwi6)+len(bidenwi6))))
print("votes ", bidenwi6votes)
print("Wisconsin 7")
trumpwi7votes = (len(trumpwi7)/(len(trumpwi7)+len(bidenwi7)))*1
bidenwi7votes = (len(bidenwi7)/(len(trumpwi7)+len(bidenwi7)))*1
print("Trump: ", (len(trumpwi7)/(len(trumpwi7)+len(bidenwi7))))
print("votes ", trumpwi7votes)
print("Biden: ",(len(bidenwi7)/(len(trumpwi7)+len(bidenwi7))))
print("votes ", bidenwi7votes)
print("Wisconsin 8")
trumpwi8votes = (len(trumpwi8)/(len(trumpwi8)+len(bidenwi8)))*1
bidenwi8votes = (len(bidenwi8)/(len(trumpwi8)+len(bidenwi8)))*1
print("Trump: ", (len(trumpwi8)/(len(trumpwi8)+len(bidenwi8))))
print("votes ", trumpwi8votes)
print("Biden: ",(len(bidenwi8)/(len(trumpwi8)+len(bidenwi8))))
print("votes ", bidenwi8votes)
totalwivotestrump = trumpwi1votes+trumpwi2votes+trumpwi3votes+trumpwi4votes+trumpwi5votes+trumpwi6votes+trumpwi7votes+trumpwi8votes
totalwivotesbiden = bidenwi1votes+bidenwi2votes+bidenwi3votes+bidenwi4votes+bidenwi5votes+bidenwi6votes+bidenwi7votes+bidenwi8votes
print("TOTAL TRUMP VOTES: ", totalwivotestrump/(totalwivotestrump+totalwivotesbiden))
print("TOTAL BIDEN VOTES: ", totalwivotesbiden/(totalwivotestrump+totalwivotesbiden))
print("")
print("Rhode Island")
print("Trump: ", (len(trumpri)/(len(trumpri)+len(bidenri))))
print("Biden: ",(len(bidenri)/(len(trumpri)+len(bidenri))))
print("Rhode Island 1")
print("Trump: ", (len(trumpri1)/(len(trumpri1)+len(bidenri1))))
print("votes ", len(trumpri1))
print("Biden: ",(len(bidenri1)/(len(trumpri1)+len(bidenri1))))
print("votes ", len(bidenri1))
trumpri1votes = (len(trumpri1)/(len(trumpri1)+len(bidenri1)))*199880
bidenri1votes = (len(bidenri1)/(len(trumpri1)+len(bidenri1)))*199880
print("Rhode Island 2")
print("Trump: ", (len(trumpri2)/(len(trumpri2)+len(bidenri2))))
print("votes ", len(trumpri2))
print("Biden: ",(len(bidenri2)/(len(trumpri2)+len(bidenri2))))
print("votes ", len(bidenri2))
trumpri2votes = (len(trumpri2)/(len(trumpri2)+len(bidenri2)))*201886
bidenri2votes = (len(bidenri2)/(len(trumpri2)+len(bidenri2)))*201886
totalrivotestrump = trumpri1votes+trumpri2votes
totalrivotesbiden = bidenri1votes+bidenri2votes
print("TOTAL TRUMP VOTES: ", totalrivotestrump/(totalrivotestrump+totalrivotesbiden))
print("TOTAL BIDEN VOTES: ", totalrivotesbiden/(totalrivotestrump+totalrivotesbiden))
print("")
print("Idaho")
print("Trump: ", (len(trumpid)/(len(trumpid)+len(bidenid))))
print("Biden: ",(len(bidenid)/(len(trumpid)+len(bidenid))))
print("Idaho 1")
trumpid1votes = (len(trumpid1)/(len(trumpid1)+len(bidenid1)))*347432
bidenid1votes = (len(bidenid1)/(len(trumpid1)+len(bidenid1)))*347432
print("Trump: ", (len(trumpid1)/(len(trumpid1)+len(bidenid1))))
print("votes ", len(trumpid1))
print("Biden: ",(len(bidenid1)/(len(trumpid1)+len(bidenid1))))
print("votes ", len(bidenid1))
print("Idaho 2")
trumpid2votes = (len(trumpid2)/(len(trumpid2)+len(bidenid2)))*306137
bidenid2votes = (len(bidenid2)/(len(trumpid2)+len(bidenid2)))*306137
print("Trump: ", (len(trumpid2)/(len(trumpid2)+len(bidenid2))))
print("votes ", len(trumpid2))
print("Biden: ",(len(bidenid2)/(len(trumpid2)+len(bidenid2))))
print("votes ", len(bidenid2))
totalidvotestrump = trumpid1votes+trumpid2votes
totalidvotesbiden = bidenid1votes+bidenid2votes
print("TOTAL TRUMP VOTES: ", totalidvotestrump/(totalidvotestrump+totalidvotesbiden))
print("TOTAL BIDEN VOTES: ", totalidvotesbiden/(totalidvotestrump+totalidvotesbiden))
print("")
print("Connecticut")
print("Trump: ", (len(trumpct)/(len(trumpct)+len(bidenct))))
print("Biden: ",(len(bidenct)/(len(trumpct)+len(bidenct))))
print("Connecticut 1")
trumpct1votes = (len(trumpct1)/(len(trumpct1)+len(bidenct1)))*297254
bidenct1votes = (len(bidenct1)/(len(trumpct1)+len(bidenct1)))*297254
print("Trump: ", (len(trumpct1)/(len(trumpct1)+len(bidenct1))))
print("votes ", trumpct1votes)
print("Biden: ",(len(bidenct1)/(len(trumpct1)+len(bidenct1))))
print("votes ", bidenct1votes)
print("Connecticut 2")
trumpct2votes = (len(trumpct2)/(len(trumpct2)+len(bidenct2)))*319171
bidenct2votes = (len(bidenct2)/(len(trumpct2)+len(bidenct2)))*319171
print("Trump: ", (len(trumpct2)/(len(trumpct2)+len(bidenct2))))
print("votes ", trumpct2votes)
print("Biden: ",(len(bidenct2)/(len(trumpct2)+len(bidenct2))))
print("votes ", bidenct2votes)
print("Connecticut 3")
trumpct3votes = (len(trumpct3)/(len(trumpct3)+len(bidenct3)))*304270
bidenct3votes = (len(bidenct3)/(len(trumpct3)+len(bidenct3)))*304270
print("Trump: ", (len(trumpct3)/(len(trumpct3)+len(bidenct3))))
print("votes ", trumpct3votes)
print("Biden: ",(len(bidenct3)/(len(trumpct3)+len(bidenct3))))
print("votes ", bidenct3votes)
print("Connecticut 4")
trumpct4votes = (len(trumpct4)/(len(trumpct4)+len(bidenct4)))*309558
bidenct4votes = (len(bidenct4)/(len(trumpct4)+len(bidenct4)))*309558
print("Trump: ", (len(trumpct4)/(len(trumpct4)+len(bidenct4))))
print("votes ", trumpct4votes)
print("Biden: ",(len(bidenct4)/(len(trumpct4)+len(bidenct4))))
print("votes ", bidenct4votes)
print("Connecticut 5")
trumpct5votes = (len(trumpct5)/(len(trumpct5)+len(bidenct5)))*301630
bidenct5votes = (len(bidenct5)/(len(trumpct5)+len(bidenct5)))*301630
print("Trump: ", (len(trumpct5)/(len(trumpct5)+len(bidenct5))))
print("votes ", trumpct5votes)
print("Biden: ",(len(bidenct5)/(len(trumpct5)+len(bidenct5))))
print("votes ", bidenct5votes)
totalctvotestrump = trumpct1votes+trumpct2votes+trumpct3votes+trumpct4votes+trumpct5votes
totalctvotesbiden = bidenct1votes+bidenct2votes+bidenct3votes+bidenct4votes+bidenct5votes
print("TOTAL TRUMP VOTES: ", totalctvotestrump/(totalctvotestrump+totalctvotesbiden))
print("TOTAL BIDEN VOTES: ", totalctvotesbiden/(totalctvotestrump+totalctvotesbiden))
print("")
print("Kansas")
print("Trump: ", (len(trumpks)/(len(trumpks)+len(bidenks))))
print("Biden: ",(len(bidenks)/(len(trumpks)+len(bidenks))))
print("Kansas 1")
trumpks1votes = (len(trumpks1)/(len(trumpks1)+len(bidenks1)))*382720
bidenks1votes = (len(bidenks1)/(len(trumpks1)+len(bidenks1)))*382720
print("Trump: ", (len(trumpks1)/(len(trumpks1)+len(bidenks1))))
print("votes ", trumpks1votes)
print("Biden: ",(len(bidenks1)/(len(trumpks1)+len(bidenks1))))
print("votes ", bidenks1votes)
print("Kansas 2")
trumpks2votes = (len(trumpks2)/(len(trumpks2)+len(bidenks2)))*368331
bidenks2votes = (len(bidenks2)/(len(trumpks2)+len(bidenks2)))*368331
print("Trump: ", (len(trumpks2)/(len(trumpks2)+len(bidenks2))))
print("votes ", trumpks2votes)
print("Biden: ",(len(bidenks2)/(len(trumpks2)+len(bidenks2))))
print("votes ", bidenks2votes)
print("Kansas 3")
trumpks3votes = (len(trumpks3)/(len(trumpks3)+len(bidenks3)))*363044
bidenks3votes = (len(bidenks3)/(len(trumpks3)+len(bidenks3)))*363044
print("Trump: ", (len(trumpks3)/(len(trumpks3)+len(bidenks3))))
print("votes ", trumpks3votes)
print("Biden: ",(len(bidenks3)/(len(trumpks3)+len(bidenks3))))
print("votes ", bidenks3votes)
print("Kansas 4")
trumpks4votes = (len(trumpks4)/(len(trumpks4)+len(bidenks4)))*367860
bidenks4votes = (len(bidenks4)/(len(trumpks4)+len(bidenks4)))*367860
print("Trump: ", (len(trumpks4)/(len(trumpks4)+len(bidenks4))))
print("votes ", trumpks4votes)
print("Biden: ",(len(bidenks4)/(len(trumpks4)+len(bidenks4))))
print("votes ", bidenks4votes)
totalksvotestrump = trumpks1votes+trumpks2votes+trumpks3votes+trumpks4votes
totalksvotesbiden = bidenks1votes+bidenks2votes+bidenks3votes+bidenks4votes
print("TOTAL TRUMP VOTES: ", totalksvotestrump/(totalksvotestrump+totalksvotesbiden))
print("TOTAL BIDEN VOTES: ", totalksvotesbiden/(totalksvotestrump+totalksvotesbiden))
print("")
print("Utah")
print("Trump: ", (len(trumput)/(len(trumput)+len(bidenut))))
print("Biden: ",(len(bidenut)/(len(trumput)+len(bidenut))))
print("Utah 1")
trumput1votes = (len(trumput1)/(len(trumput1)+len(bidenut1)))*222509
bidenut1votes = (len(bidenut1)/(len(trumput1)+len(bidenut1)))*222509
print("Trump: ", (len(trumput1)/(len(trumput1)+len(bidenut1))))
print("votes ", trumput1votes)
print("Biden: ",(len(bidenut1)/(len(trumput1)+len(bidenut1))))
print("votes ", bidenut1votes)
print("Utah 2")
trumput2votes = (len(trumput2)/(len(trumput2)+len(bidenut2)))*232969
bidenut2votes = (len(bidenut2)/(len(trumput2)+len(bidenut2)))*232969
print("Trump: ", (len(trumput2)/(len(trumput2)+len(bidenut2))))
print("votes ", trumput2votes)
print("Biden: ",(len(bidenut2)/(len(trumput2)+len(bidenut2))))
print("votes ", bidenut2votes)
print("Utah 3")
trumput3votes = (len(trumput3)/(len(trumput3)+len(bidenut3)))*254847
bidenut3votes = (len(bidenut3)/(len(trumput3)+len(bidenut3)))*254847
print("Trump: ", (len(trumput3)/(len(trumput3)+len(bidenut3))))
print("votes ", trumput3votes)
print("Biden: ",(len(bidenut3)/(len(trumput3)+len(bidenut3))))
print("votes ", bidenut3votes)
print("Utah 4")
trumput4votes = (len(trumput4)/(len(trumput4)+len(bidenut4)))*219743
bidenut4votes = (len(bidenut4)/(len(trumput4)+len(bidenut4)))*219743
print("Trump: ", (len(trumput4)/(len(trumput4)+len(bidenut4))))
print("votes ", trumput4votes)
print("Biden: ",(len(bidenut4)/(len(trumput4)+len(bidenut4))))
print("votes ", bidenut4votes)
totalutvotestrump = trumput1votes+trumput2votes+trumput3votes+trumput4votes
totalutvotesbiden = bidenut1votes+bidenut2votes+bidenut3votes+bidenut4votes
print("TOTAL TRUMP VOTES: ", totalutvotestrump/(totalutvotestrump+totalutvotesbiden))
print("TOTAL BIDEN VOTES: ", totalutvotesbiden/(totalutvotestrump+totalutvotesbiden))
print("")
print("Iowa")
print("Trump: ", (len(trumpia)/(len(trumpia)+len(bidenia))))
print("Biden: ",(len(bidenia)/(len(trumpia)+len(bidenia))))
print("Iowa 1")
trumpia1votes = (len(trumpia1)/(len(trumpia1)+len(bidenia1)))*382720
bidenia1votes = (len(bidenia1)/(len(trumpia1)+len(bidenia1)))*382720
print("Trump: ", (len(trumpia1)/(len(trumpia1)+len(bidenia1))))
print("votes ", trumpia1votes)
print("Biden: ",(len(bidenia1)/(len(trumpia1)+len(bidenia1))))
print("votes ", bidenia1votes)
print("Iowa 2")
trumpia2votes = (len(trumpia2)/(len(trumpia2)+len(bidenia2)))*368331
bidenia2votes = (len(bidenia2)/(len(trumpia2)+len(bidenia2)))*368331
print("Trump: ", (len(trumpia2)/(len(trumpia2)+len(bidenia2))))
print("votes ", trumpia2votes)
print("Biden: ",(len(bidenia2)/(len(trumpia2)+len(bidenia2))))
print("votes ", bidenia2votes)
print("Iowa 3")
trumpia3votes = (len(trumpia3)/(len(trumpia3)+len(bidenia3)))*363044
bidenia3votes = (len(bidenia3)/(len(trumpia3)+len(bidenia3)))*363044
print("Trump: ", (len(trumpia3)/(len(trumpia3)+len(bidenia3))))
print("votes ", trumpia3votes)
print("Biden: ",(len(bidenia3)/(len(trumpia3)+len(bidenia3))))
print("votes ", bidenia3votes)
print("Iowa 4")
trumpia4votes = (len(trumpia4)/(len(trumpia4)+len(bidenia4)))*367860
bidenia4votes = (len(bidenia4)/(len(trumpia4)+len(bidenia4)))*367860
print("Trump: ", (len(trumpia4)/(len(trumpia4)+len(bidenia4))))
print("votes ", trumpia4votes)
print("Biden: ",(len(bidenia4)/(len(trumpia4)+len(bidenia4))))
print("votes ", bidenia4votes)
totaliavotestrump = trumpia1votes+trumpia2votes+trumpia3votes+trumpia4votes
totaliavotesbiden = bidenia1votes+bidenia2votes+bidenia3votes+bidenia4votes
print("TOTAL TRUMP VOTES: ", totaliavotestrump/(totaliavotestrump+totaliavotesbiden))
print("TOTAL BIDEN VOTES: ", totaliavotesbiden/(totaliavotestrump+totaliavotesbiden))
print("")
print("Illinois")
print("Trump: ", (len(trumpil)/(len(trumpil)+len(bidenil))))
print("Biden: ",(len(bidenil)/(len(trumpil)+len(bidenil))))
print("Illinois 1")
trumpil1votes = (len(trumpil1)/(len(trumpil1)+len(bidenil1)))*1
bidenil1votes = (len(bidenil1)/(len(trumpil1)+len(bidenil1)))*1
print("Trump: ", (len(trumpil1)/(len(trumpil1)+len(bidenil1))))
print("votes ", trumpil1votes)
print("Biden: ",(len(bidenil1)/(len(trumpil1)+len(bidenil1))))
print("votes ", bidenil1votes)
print("Illinois 2")
trumpil2votes = (len(trumpil2)/(len(trumpil2)+len(bidenil2)))*1
bidenil2votes = (len(bidenil2)/(len(trumpil2)+len(bidenil2)))*1
print("Trump: ", (len(trumpil2)/(len(trumpil2)+len(bidenil2))))
print("votes ", trumpil2votes)
print("Biden: ",(len(bidenil2)/(len(trumpil2)+len(bidenil2))))
print("votes ", bidenil2votes)
print("Illinois 3")
trumpil3votes = (len(trumpil3)/(len(trumpil3)+len(bidenil3)))*1
bidenil3votes = (len(bidenil3)/(len(trumpil3)+len(bidenil3)))*1
print("Trump: ", (len(trumpil3)/(len(trumpil3)+len(bidenil3))))
print("votes ", trumpil3votes)
print("Biden: ",(len(bidenil3)/(len(trumpil3)+len(bidenil3))))
print("votes ", bidenil3votes)
print("Illinois 4")
trumpil4votes = (len(trumpil4)/(len(trumpil4)+len(bidenil4)))*1
bidenil4votes = (len(bidenil4)/(len(trumpil4)+len(bidenil4)))*1
print("Trump: ", (len(trumpil4)/(len(trumpil4)+len(bidenil4))))
print("votes ", trumpil4votes)
print("Biden: ",(len(bidenil4)/(len(trumpil4)+len(bidenil4))))
print("votes ", bidenil4votes)
print("Illinois 5")
trumpil5votes = (len(trumpil5)/(len(trumpil5)+len(bidenil5)))*1
bidenil5votes = (len(bidenil5)/(len(trumpil5)+len(bidenil5)))*1
print("Trump: ", (len(trumpil5)/(len(trumpil5)+len(bidenil5))))
print("votes ", trumpil5votes)
print("Biden: ",(len(bidenil5)/(len(trumpil5)+len(bidenil5))))
print("votes ", bidenil5votes)
print("Illinois 6")
trumpil6votes = (len(trumpil6)/(len(trumpil6)+len(bidenil6)))*1
bidenil6votes = (len(bidenil6)/(len(trumpil6)+len(bidenil6)))*1
print("Trump: ", (len(trumpil6)/(len(trumpil6)+len(bidenil6))))
print("votes ", trumpil6votes)
print("Biden: ",(len(bidenil6)/(len(trumpil6)+len(bidenil6))))
print("votes ", bidenil6votes)
print("Illinois 7")
trumpil7votes = (len(trumpil7)/(len(trumpil7)+len(bidenil7)))*1
bidenil7votes = (len(bidenil7)/(len(trumpil7)+len(bidenil7)))*1
print("Trump: ", (len(trumpil7)/(len(trumpil7)+len(bidenil7))))
print("votes ", trumpil7votes)
print("Biden: ",(len(bidenil7)/(len(trumpil7)+len(bidenil7))))
print("votes ", bidenil7votes)
print("Illinois 8")
trumpil8votes = (len(trumpil8)/(len(trumpil8)+len(bidenil8)))*1
bidenil8votes = (len(bidenil8)/(len(trumpil8)+len(bidenil8)))*1
print("Trump: ", (len(trumpil8)/(len(trumpil8)+len(bidenil8))))
print("votes ", trumpil8votes)
print("Biden: ",(len(bidenil8)/(len(trumpil8)+len(bidenil8))))
print("votes ", bidenil8votes)
print("Illinois 9")
trumpil9votes = (len(trumpil9)/(len(trumpil9)+len(bidenil9)))*1
bidenil9votes = (len(bidenil9)/(len(trumpil9)+len(bidenil9)))*1
print("Trump: ", (len(trumpil9)/(len(trumpil9)+len(bidenil9))))
print("votes ", trumpil9votes)
print("Biden: ",(len(bidenil9)/(len(trumpil9)+len(bidenil9))))
print("votes ", bidenil9votes)
print("Illinois 10")
trumpil10votes = (len(trumpil10)/(len(trumpil10)+len(bidenil10)))*1
bidenil10votes = (len(bidenil10)/(len(trumpil10)+len(bidenil10)))*1
print("Trump: ", (len(trumpil10)/(len(trumpil10)+len(bidenil10))))
print("votes ", trumpil10votes)
print("Biden: ",(len(bidenil10)/(len(trumpil10)+len(bidenil10))))
print("votes ", bidenil10votes)
print("Illinois 11")
trumpil11votes = (len(trumpil11)/(len(trumpil11)+len(bidenil11)))*1
bidenil11votes = (len(bidenil11)/(len(trumpil11)+len(bidenil11)))*1
print("Trump: ", (len(trumpil11)/(len(trumpil11)+len(bidenil11))))
print("votes ", trumpil11votes)
print("Biden: ",(len(bidenil11)/(len(trumpil11)+len(bidenil11))))
print("votes ", bidenil11votes)
print("Illinois 12")
trumpil12votes = (len(trumpil12)/(len(trumpil12)+len(bidenil12)))*1
bidenil12votes = (len(bidenil12)/(len(trumpil12)+len(bidenil12)))*1
print("Trump: ", (len(trumpil12)/(len(trumpil12)+len(bidenil12))))
print("votes ", trumpil12votes)
print("Biden: ",(len(bidenil12)/(len(trumpil12)+len(bidenil12))))
print("votes ", bidenil12votes)
print("Illinois 13")
trumpil13votes = (len(trumpil13)/(len(trumpil13)+len(bidenil13)))*1
bidenil13votes = (len(bidenil13)/(len(trumpil13)+len(bidenil13)))*1
print("Trump: ", (len(trumpil13)/(len(trumpil13)+len(bidenil13))))
print("votes ", trumpil13votes)
print("Biden: ",(len(bidenil13)/(len(trumpil13)+len(bidenil13))))
print("votes ", bidenil13votes)
print("Illinois 14")
trumpil14votes = (len(trumpil14)/(len(trumpil14)+len(bidenil14)))*1
bidenil14votes = (len(bidenil14)/(len(trumpil14)+len(bidenil14)))*1
print("Trump: ", (len(trumpil14)/(len(trumpil14)+len(bidenil14))))
print("votes ", trumpil14votes)
print("Biden: ",(len(bidenil14)/(len(trumpil14)+len(bidenil14))))
print("votes ", bidenil14votes)
print("Illinois 15")
trumpil15votes = (len(trumpil15)/(len(trumpil15)+len(bidenil15)))*1
bidenil15votes = (len(bidenil15)/(len(trumpil15)+len(bidenil15)))*1
print("Trump: ", (len(trumpil15)/(len(trumpil15)+len(bidenil15))))
print("votes ", trumpil15votes)
print("Biden: ",(len(bidenil15)/(len(trumpil15)+len(bidenil15))))
print("votes ", bidenil15votes)
print("Illinois 16")
trumpil16votes = (len(trumpil16)/(len(trumpil16)+len(bidenil16)))*1
bidenil16votes = (len(bidenil16)/(len(trumpil16)+len(bidenil16)))*1
print("Trump: ", (len(trumpil16)/(len(trumpil16)+len(bidenil16))))
print("votes ", trumpil16votes)
print("Biden: ",(len(bidenil16)/(len(trumpil16)+len(bidenil16))))
print("votes ", bidenil16votes)
print("Illinois 17")
trumpil17votes = (len(trumpil17)/(len(trumpil17)+len(bidenil17)))*1
bidenil17votes = (len(bidenil17)/(len(trumpil17)+len(bidenil17)))*1
print("Trump: ", (len(trumpil17)/(len(trumpil17)+len(bidenil17))))
print("votes ", trumpil17votes)
print("Biden: ",(len(bidenil17)/(len(trumpil17)+len(bidenil17))))
print("votes ", bidenil17votes)
print("Illinois 18")
trumpil18votes = (len(trumpil18)/(len(trumpil18)+len(bidenil18)))*1
bidenil18votes = (len(bidenil18)/(len(trumpil18)+len(bidenil18)))*1
print("Trump: ", (len(trumpil18)/(len(trumpil18)+len(bidenil18))))
print("votes ", trumpil18votes)
print("Biden: ",(len(bidenil18)/(len(trumpil18)+len(bidenil18))))
print("votes ", bidenil18votes)
totalilvotestrump = trumpil1votes+trumpil2votes+trumpil3votes+trumpil4votes+trumpil5votes+trumpil6votes+trumpil7votes+trumpil8votes+trumpil9votes+trumpil10votes+trumpil11votes+trumpil12votes+trumpil13votes+trumpil14votes+trumpil15votes+trumpil16votes+trumpil17votes+trumpil18votes
totalilvotesbiden = bidenil1votes+bidenil2votes+bidenil3votes+bidenil4votes+bidenil5votes+bidenil6votes+bidenil7votes+bidenil8votes+bidenil9votes+bidenil10votes+bidenil11votes+bidenil12votes+bidenil13votes+bidenil14votes+bidenil15votes+bidenil16votes+bidenil17votes+bidenil18votes
print("TOTAL TRUMP VOTES: ", totalilvotestrump/(totalilvotestrump+totalilvotesbiden))
print("TOTAL BIDEN VOTES: ", totalilvotesbiden/(totalilvotestrump+totalilvotesbiden))

with open("/Volumes/TOSHIBA_BACKUP/iterate2sortlocsave.txt", 'wb') as f:
	pickle.dump([trumpmo, bidenmo, trumpmo1, bidenmo1, trumpmo2, bidenmo2, trumpmo3, bidenmo3, trumpmo4, bidenmo4, trumpmo5, bidenmo5, trumpmo6, bidenmo6, trumpmo7, bidenmo7, trumpmo8, bidenmo8, trumpco, bidenco, trumpco1, bidenco1, trumpco2, bidenco2, trumpco3, bidenco3, trumpco4, bidenco4, trumpco5, bidenco5, trumpco6, bidenco6, trumpco7, bidenco7, trumpsc, bidensc, trumpsc1, bidensc1, trumpsc2, bidensc2, trumpsc3, bidensc3, trumpsc4, bidensc4, trumpsc5, bidensc5, trumpsc6, bidensc6, trumpsc7, bidensc7, trumpmn, bidenmn, trumpmn1, bidenmn1, trumpmn2, bidenmn2, trumpmn3, bidenmn3, trumpmn4, bidenmn4, trumpmn5, bidenmn5, trumpmn6, bidenmn6, trumpmn7, bidenmn7, trumpmn8, bidenmn8, trumpin, bidenin, trumpin1, bidenin1, trumpin2, bidenin2, trumpin3, bidenin3, trumpin4, bidenin4, trumpin5, bidenin5, trumpin6, bidenin6, trumpin7, bidenin7, trumpin8, bidenin8, trumpin9, bidenin9, trumpmd, bidenmd, trumpmd1, bidenmd1, trumpmd2, bidenmd2, trumpmd3, bidenmd3, trumpmd4, bidenmd4, trumpmd5, bidenmd5, trumpmd6, bidenmd6, trumpmd7, bidenmd7, trumpmd8, bidenmd8, trumpsd, bidensd, trumpsd1, bidensd1, trumpvt, bidenvt, trumpvt1, bidenvt1, trumpnd, bidennd, trumpnd1, bidennd1, trumpde, bidende, trumpde1, bidende1, trumpmt, bidenmt, trumpmt1, bidenmt1, trumpne, bidenne, trumpne1, bidenne1, trumpne2, bidenne2, trumpne3, bidenne3, trumpmi, bidenmi, trumpmi1, bidenmi1, trumpmi2, bidenmi2, trumpmi3, bidenmi3, trumpmi4, bidenmi4, trumpmi5, bidenmi5, trumpmi6, bidenmi6, trumpmi7, bidenmi7, trumpmi8, bidenmi8, trumpmi9, bidenmi9, trumpmi10, bidenmi10, trumpmi11, bidenmi11, trumpmi12, bidenmi12, trumpmi13, bidenmi13, trumpmi14, bidenmi14, trumpma, bidenma, trumpma1, bidenma1, trumpma2, bidenma2, trumpma3, bidenma3, trumpma4, bidenma4, trumpma5, bidenma5, trumpma6, bidenma6, trumpma7, bidenma7, trumpma8, bidenma8, trumpma9, bidenma9, trumpva, bidenva, trumpva1, bidenva1, trumpva2, bidenva2, trumpva3, bidenva3, trumpva4, bidenva4, trumpva5, bidenva5, trumpva6, bidenva6, trumpva7, bidenva7, trumpva8, bidenva8, trumpva9, bidenva9, trumpva10, bidenva10, trumpva11, bidenva11, trumpme, bidenme, trumpme1, bidenme1, trumpme2, bidenme2, trumpid, bidenid, trumpid1, bidenid1, trumpid2, bidenid2, trumpwi, bidenwi, trumpwi1, bidenwi1, trumpwi2, bidenwi2, trumpwi3, bidenwi3, trumpwi4, bidenwi4, trumpwi5, bidenwi5, trumpwi6, bidenwi6, trumpwi7, bidenwi7, trumpwi8, bidenwi8, trumpwv, bidenwv, trumpwv1, bidenwv1, trumpwv2, bidenwv2, trumpwv3, bidenwv3, trumpia, bidenia, trumpia1, bidenia1, trumpia2, bidenia2, trumpia3, bidenia3, trumpia4, bidenia4, trumpms, bidenms, trumpms1, bidenms1, trumpms2, bidenms2, trumpms3, bidenms3, trumpms4, bidenms4, trumphi, bidenhi, trumphi1, bidenhi1, trumphi2, bidenhi2, trumpri, bidenri, trumpri1, bidenri1, trumpri2, bidenri2, trumpwa, bidenwa, trumpwa1, bidenwa1, trumpwa2, bidenwa2, trumpwa3, bidenwa3, trumpwa4, bidenwa4, trumpwa5, bidenwa5, trumpwa6, bidenwa6, trumpwa7, bidenwa7, trumpwa8, bidenwa8, trumpwa9, bidenwa9, trumpwa10, bidenwa10, trumpfl, bidenfl, trumpfl1, bidenfl1, trumpfl2, bidenfl2, trumpfl3, bidenfl3, trumpfl4, bidenfl4, trumpfl5, bidenfl5, trumpfl6, bidenfl6, trumpfl7, bidenfl7, trumpfl8, bidenfl8, trumpfl9, bidenfl9, trumpfl10, bidenfl10, trumpfl11, bidenfl11, trumpfl12, bidenfl12, trumpfl13, bidenfl13, trumpfl14, bidenfl14, trumpfl15, bidenfl15, trumpfl16, bidenfl16, trumpfl17, bidenfl17, trumpfl18, bidenfl18, trumpfl19, bidenfl19, trumpfl20, bidenfl20, trumpfl21, bidenfl21, trumpfl22, bidenfl22, trumpfl23, bidenfl23, trumpfl24, bidenfl24, trumpfl25, bidenfl25, trumpfl26, bidenfl26, trumpfl27, bidenfl27, trumpal, bidenal, trumpal1, bidenal1, trumpal2, bidenal2, trumpal3, bidenal3, trumpal4, bidenal4, trumpal5, bidenal5, trumpal6, bidenal6, trumpal7, bidenal7, trumpil, bidenil, trumpil1, bidenil1, trumpil2, bidenil2, trumpil3, bidenil3, trumpil4, bidenil4, trumpil5, bidenil5, trumpil6, bidenil6, trumpil7, bidenil7, trumpil8, bidenil8, trumpil9, bidenil9, trumpil10, bidenil10, trumpil11, bidenil11, trumpil12, bidenil12, trumpil13, bidenil13, trumpil14, bidenil14, trumpil15, bidenil15, trumpil16, bidenil16, trumpil17, bidenil17, trumpil18, bidenil18, trumpca, bidenca, trumpca1, bidenca1, trumpca2, bidenca2, trumpca3, bidenca3, trumpca4, bidenca4, trumpca5, bidenca5, trumpca6, bidenca6, trumpca7, bidenca7, trumpca8, bidenca8, trumpca9, bidenca9, trumpca10, bidenca10, trumpca11, bidenca11, trumpca12, bidenca12, trumpca13, bidenca13, trumpca14, bidenca14, trumpca15, bidenca15, trumpca16, bidenca16, trumpca17, bidenca17, trumpca18, bidenca18, trumpca19, bidenca19, trumpca20, bidenca20, trumpca21, bidenca21, trumpca22, bidenca22, trumpca23, bidenca23, trumpca24, bidenca24, trumpca25, bidenca25, trumpca26, bidenca26, trumpca27, bidenca27, trumpca28, bidenca28, trumpca29, bidenca29, trumpca30, bidenca30, trumpca31, bidenca31, trumpca32, bidenca32, trumpca33, bidenca33, trumpca34, bidenca34, trumpca35, bidenca35, trumpca36, bidenca36, trumpca37, bidenca37, trumpca38, bidenca38, trumpca39, bidenca39, trumpca40, bidenca40, trumpca41, bidenca41, trumpca42, bidenca42, trumpca43, bidenca43, trumpca44, bidenca44, trumpca45, bidenca45, trumpca46, bidenca46, trumpca47, bidenca47, trumpca48, bidenca48, trumpca49, bidenca49, trumpca50, bidenca50, trumpca51, bidenca51, trumpca52, bidenca52, trumpca53, bidenca53, trumpks, bidenks, trumpks1, bidenks1, trumpks2, bidenks2, trumpks3, bidenks3, trumpks4, bidenks4, trumpga, bidenga, trumpga1, bidenga1, trumpga2, bidenga2, trumpga3, bidenga3, trumpga4, bidenga4, trumpga5, bidenga5, trumpga6, bidenga6, trumpga7, bidenga7, trumpga8, bidenga8, trumpga9, bidenga9, trumpga10, bidenga10, trumpga11, bidenga11, trumpga12, bidenga12, trumpga13, bidenga13, trumpga14, bidenga14, trumpaz, bidenaz, trumpaz1, bidenaz1, trumpaz2, bidenaz2, trumpaz3, bidenaz3, trumpaz4, bidenaz4, trumpaz5, bidenaz5, trumpaz6, bidenaz6, trumpaz7, bidenaz7, trumpaz8, bidenaz8, trumpaz9, bidenaz9, trumpak, bidenak, trumpak1, bidenak1, trumpar, bidenar, trumpar1, bidenar1, trumpar2, bidenar2, trumpar3, bidenar3, trumpar4, bidenar4, trumpnj, bidennj, trumpnj1, bidennj1, trumpnj2, bidennj2, trumpnj3, bidennj3, trumpnj4, bidennj4, trumpnj5, bidennj5, trumpnj6, bidennj6, trumpnj7, bidennj7, trumpnj8, bidennj8, trumpnj9, bidennj9, trumpnj10, bidennj10, trumpnj11, bidennj11, trumpnj12, bidennj12, trumpnv, bidennv, trumpnv1, bidennv1, trumpnv2, bidennv2, trumpnv3, bidennv3, trumpnv4, bidennv4, trumpnh, bidennh, trumpnh1, bidennh1, trumpnh2, bidennh2, trumpnc, bidennc, trumpnc1, bidennc1, trumpnc2, bidennc2, trumpnc3, bidennc3, trumpnc4, bidennc4, trumpnc5, bidennc5, trumpnc6, bidennc6, trumpnc7, bidennc7, trumpnc8, bidennc8, trumpnc9, bidennc9, trumpnc10, bidennc10, trumpnc11, bidennc11, trumpnc12, bidennc12, trumpnc13, bidennc13, trumptx, bidentx, trumptx1, bidentx1, trumptx2, bidentx2, trumptx3, bidentx3, trumptx4, bidentx4, trumptx5, bidentx5, trumptx6, bidentx6, trumptx7, bidentx7, trumptx8, bidentx8, trumptx9, bidentx9, trumptx10, bidentx10, trumptx11, bidentx11, trumptx12, bidentx12, trumptx13, bidentx13, trumptx14, bidentx14, trumptx15, bidentx15, trumptx16, bidentx16, trumptx17, bidentx17, trumptx18, bidentx18, trumptx19, bidentx19, trumptx20, bidentx20, trumptx21, bidentx21, trumptx22, bidentx22, trumptx23, bidentx23, trumptx24, bidentx24, trumptx25, bidentx25, trumptx26, bidentx26, trumptx27, bidentx27, trumptx28, bidentx28, trumptx29, bidentx29, trumptx30, bidentx30, trumptx31, bidentx31, trumptx32, bidentx32, trumptx33, bidentx33, trumptx34, bidentx34, trumptx35, bidentx35, trumptx36, bidentx36, trumptn, bidentn, trumptn1, bidentn1, trumptn2, bidentn2, trumptn3, bidentn3, trumptn4, bidentn4, trumptn5, bidentn5, trumptn6, bidentn6, trumptn7, bidentn7, trumptn8, bidentn8, trumptn9, bidentn9, trumpnm, bidennm, trumpnm1, bidennm1, trumpnm2, bidennm2, trumpnm3, bidennm3, trumpny, bidenny, trumpny1, bidenny1, trumpny2, bidenny2, trumpny3, bidenny3, trumpny4, bidenny4, trumpny5, bidenny5, trumpny6, bidenny6, trumpny7, bidenny7, trumpny8, bidenny8, trumpny9, bidenny9, trumpny10, bidenny10, trumpny11, bidenny11, trumpny12, bidenny12, trumpny13, bidenny13, trumpny14, bidenny14, trumpny15, bidenny15, trumpny16, bidenny16, trumpny17, bidenny17, trumpny18, bidenny18, trumpny19, bidenny19, trumpny20, bidenny20, trumpny21, bidenny21, trumpny22, bidenny22, trumpny23, bidenny23, trumpny24, bidenny24, trumpny25, bidenny25, trumpny26, bidenny26, trumpny27, bidenny27, trumpwy, bidenwy, trumpwy1, bidenwy1, trumppa, bidenpa, trumppa1, bidenpa1, trumppa2, bidenpa2, trumppa3, bidenpa3, trumppa4, bidenpa4, trumppa5, bidenpa5, trumppa6, bidenpa6, trumppa7, bidenpa7, trumppa8, bidenpa8, trumppa9, bidenpa9, trumppa10, bidenpa10, trumppa11, bidenpa11, trumppa12, bidenpa12, trumppa13, bidenpa13, trumppa14, bidenpa14, trumppa15, bidenpa15, trumppa16, bidenpa16, trumppa17, bidenpa17, trumppa18, bidenpa18, trumpct, bidenct, trumpct1, bidenct1, trumpct2, bidenct2, trumpct3, bidenct3, trumpct4, bidenct4, trumpct5, bidenct5, trumpky, bidenky, trumpky1, bidenky1, trumpky2, bidenky2, trumpky3, bidenky3, trumpky4, bidenky4, trumpky5, bidenky5, trumpky6, bidenky6, trumpla, bidenla, trumpla1, bidenla1, trumpla2, bidenla2, trumpla3, bidenla3, trumpla4, bidenla4, trumpla5, bidenla5, trumpla6, bidenla6, trumpok, bidenok, trumpok1, bidenok1, trumpok2, bidenok2, trumpok3, bidenok3, trumpok4, bidenok4, trumpok5, bidenok5, trumput, bidenut, trumput1, bidenut1, trumput2, bidenut2, trumput3, bidenut3, trumput4, bidenut4, trumpoh, bidenoh, trumpoh1, bidenoh1, trumpoh2, bidenoh2, trumpoh3, bidenoh3, trumpoh4, bidenoh4, trumpoh5, bidenoh5, trumpoh6, bidenoh6, trumpoh7, bidenoh7, trumpoh8, bidenoh8, trumpoh9, bidenoh9, trumpoh10, bidenoh10, trumpoh11, bidenoh11, trumpoh12, bidenoh12, trumpoh13, bidenoh13, trumpoh14, bidenoh14, trumpoh15, bidenoh15, trumpoh16, bidenoh16, trumpor, bidenor, trumpor1, bidenor1, trumpor2, bidenor2, trumpor3, bidenor3, trumpor4, bidenor4, trumpor5, bidenor5], f)


