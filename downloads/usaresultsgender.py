import sys
sys.path.append("..")
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import pickle
from sortlocation import sortloc


results = []
bidendistricts = 0
trumpdistricts = 0

#black = woman; latino = man; white = others

# def sortEthnic(lat, bla, whi, tw):
# 	if("garcia" in tw["user"]["name"].lower() or "rodriguez" in tw["user"]["name"].lower() or "martinez" in tw["user"]["name"].lower() or "hernandez" in tw["user"]["name"].lower() or "Lopez" in tw["user"]["name"] or "gonzalez" in tw["user"]["name"].lower() or "Perez" in tw["user"]["name"] or "sanchez" in tw["user"]["name"].lower() or "ramirez" in tw["user"]["name"].lower() or "torres" in tw["user"]["name"].lower() or "flores" in tw["user"]["name"].lower() or "rivera" in tw["user"]["name"].lower() or "Gomez" in tw["user"]["name"] or "Diaz" in tw["user"]["name"] or "Reyes" in tw["user"]["name"] or "morales" in tw["user"]["name"].lower() or "Cruz" in tw["user"]["name"] or "Ortiz" in tw["user"]["name"] or "gutierrez" in tw["user"]["name"].lower() or "chavez" in tw["user"]["name"].lower() or "Ramos" in tw["user"]["name"] or "gonzales" in tw["user"]["name"].lower() or "Ruiz" in tw["user"]["name"] or "alvarez" in tw["user"]["name"].lower() or "mendoza" in tw["user"]["name"].lower() or "vasquez" in tw["user"]["name"].lower() or "castillo" in tw["user"]["name"].lower() or "jimenez" in tw["user"]["name"].lower() or "moreno" in tw["user"]["name"].lower() or "romero" in tw["user"]["name"].lower() or "herrera" in tw["user"]["name"].lower() or "medina" in tw["user"]["name"].lower() or "aguilar" in tw["user"]["name"].lower() or "Garza" in tw["user"]["name"] or "castro" in tw["user"]["name"].lower() or "vargas" in tw["user"]["name"].lower() or "fernandez" in tw["user"]["name"].lower() or "guzman" in tw["user"]["name"].lower() or "Munoz" in tw["user"]["name"] or "mendez" in tw["user"]["name"].lower() or "salazar" in tw["user"]["name"].lower() or "Soto" in tw["user"]["name"] or "delgado" in tw["user"]["name"].lower() or "Pena" in tw["user"]["name"] or "Rios" in tw["user"]["name"] or "alvarado" in tw["user"]["name"].lower() or "sandoval" in tw["user"]["name"].lower() or "contreras" in tw["user"]["name"].lower() or "valdez" in tw["user"]["name"].lower() or "guerrero" in tw["user"]["name"].lower() or "ortega" in tw["user"]["name"].lower() or "estrada" in tw["user"]["name"].lower() or "Nunez" in tw["user"]["name"] or "maldonado" in tw["user"]["name"].lower() or "Vega" in tw["user"]["name"] or "vazquez" in tw["user"]["name"].lower() or "santiago" in tw["user"]["name"].lower() or "dominguez" in tw["user"]["name"].lower() or "espinoza" in tw["user"]["name"].lower() or "Silva" in tw["user"]["name"] or "padilla" in tw["user"]["name"].lower() or "marquez" in tw["user"]["name"].lower() or "cortez" in tw["user"]["name"].lower() or "Rojas" in tw["user"]["name"] or "acosta" in tw["user"]["name"].lower() or "figueroa" in tw["user"]["name"].lower() or "Luna" in tw["user"]["name"] or "juarez" in tw["user"]["name"].lower() or "navarro" in tw["user"]["name"].lower() or "campos" in tw["user"]["name"].lower() or "molina" in tw["user"]["name"].lower() or "Avila" in tw["user"]["name"] or "Ayala" in tw["user"]["name"] or "Mejia" in tw["user"]["name"] or "carrillo" in tw["user"]["name"].lower() or "Duran" in tw["user"]["name"] or "santos" in tw["user"]["name"].lower() or "salinas" in tw["user"]["name"].lower() or "robles" in tw["user"]["name"].lower() or "Solis" in tw["user"]["name"] or "Lara" in tw["user"]["name"] or "cervantes" in tw["user"]["name"].lower() or "aguirre" in tw["user"]["name"].lower() or "deleon" in tw["user"]["name"].lower() or "Ochoa" in tw["user"]["name"] or "miranda" in tw["user"]["name"].lower() or "cardenas" in tw["user"]["name"].lower() or "trujillo" in tw["user"]["name"].lower() or "velasquez" in tw["user"]["name"].lower() or "fuentes" in tw["user"]["name"].lower() or "cabrera" in tw["user"]["name"].lower() or "Leon" in tw["user"]["name"] or "Rivas" in tw["user"]["name"] or "montoya" in tw["user"]["name"].lower() or "calderon" in tw["user"]["name"].lower() or "Colon" in tw["user"]["name"] or "serrano" in tw["user"]["name"].lower() or "gallegos" in tw["user"]["name"].lower() or "rosales" in tw["user"]["name"].lower() or "castaneda" in tw["user"]["name"].lower() or "villarreal" in tw["user"]["name"].lower() or "guerra" in tw["user"]["name"].lower() or "trevino" in tw["user"]["name"].lower() or "pacheco" in tw["user"]["name"].lower() or "ibarra" in tw["user"]["name"].lower() or "valencia" in tw["user"]["name"].lower() or "macias" in tw["user"]["name"].lower() or "camacho" in tw["user"]["name"].lower() or "Salas" in tw["user"]["name"] or "orozco" in tw["user"]["name"].lower() or "Roman" in tw["user"]["name"] or "zamora" in tw["user"]["name"].lower() or "suarez" in tw["user"]["name"].lower() or "franco" in tw["user"]["name"].lower() or "barrera" in tw["user"]["name"].lower() or "mercado" in tw["user"]["name"].lower() or "santana" in tw["user"]["name"].lower() or "valenzuela" in tw["user"]["name"].lower() or "escobar" in tw["user"]["name"].lower() or "rangel" in tw["user"]["name"].lower() or "melendez" in tw["user"]["name"].lower() or "Velez" in tw["user"]["name"] or "lozano" in tw["user"]["name"].lower() or "velazquez" in tw["user"]["name"].lower() or "Arias" in tw["user"]["name"] or "Mora" in tw["user"]["name"] or "delacruz" in tw["user"]["name"].lower() or "galvan" in tw["user"]["name"].lower() or "zuniga" in tw["user"]["name"].lower() or "Cantu" in tw["user"]["name"] or "villanueva" in tw["user"]["name"].lower() or "Meza" in tw["user"]["name"] or "acevedo" in tw["user"]["name"].lower() or "cisneros" in tw["user"]["name"].lower() or "arroyo" in tw["user"]["name"].lower() or "pineda" in tw["user"]["name"].lower() or "andrade" in tw["user"]["name"].lower() or "Tapia" in tw["user"]["name"] or "Sosa" in tw["user"]["name"] or "Villa" in tw["user"]["name"] or "Rocha" in tw["user"]["name"] or "Rubio" in tw["user"]["name"] or "zavala" in tw["user"]["name"].lower() or "montes" in tw["user"]["name"].lower() or "Ponce" in tw["user"]["name"] or "bonilla" in tw["user"]["name"].lower() or "arellano" in tw["user"]["name"].lower() or "rosario" in tw["user"]["name"].lower() or "davila" in tw["user"]["name"].lower() or "villegas" in tw["user"]["name"].lower() or "huerta" in tw["user"]["name"].lower() or "Mata" in tw["user"]["name"] or "beltran" in tw["user"]["name"].lower() or "barajas" in tw["user"]["name"].lower() or "benitez" in tw["user"]["name"].lower() or "esparza" in tw["user"]["name"].lower() or "cordova" in tw["user"]["name"].lower() or "murillo" in tw["user"]["name"].lower() or "salgado" in tw["user"]["name"].lower() or "Rosas" in tw["user"]["name"] or "cuevas" in tw["user"]["name"].lower() or "palacios" in tw["user"]["name"].lower() or "guevara" in tw["user"]["name"].lower() or "quintero" in tw["user"]["name"].lower() or "lucero" in tw["user"]["name"].lower() or "medrano" in tw["user"]["name"].lower() or "bautista" in tw["user"]["name"].lower() or "Lugo" in tw["user"]["name"] or "dejesus" in tw["user"]["name"].lower() or "espinosa" in tw["user"]["name"].lower() or "Marin" in tw["user"]["name"] or "cortes" in tw["user"]["name"].lower() or "magana" in tw["user"]["name"].lower() or "quintana" in tw["user"]["name"].lower() or "corona" in tw["user"]["name"].lower() or "Trejo" in tw["user"]["name"] or "bernal" in tw["user"]["name"].lower() or "nieves" in tw["user"]["name"].lower() or "villalobos" in tw["user"]["name"].lower() or "enriquez" in tw["user"]["name"].lower() or "Reyna" in tw["user"]["name"] or "jaramillo" in tw["user"]["name"].lower() or "Saenz" in tw["user"]["name"] or "quinones" in tw["user"]["name"].lower() or "delarosa" in tw["user"]["name"].lower() or "avalos" in tw["user"]["name"].lower() or "esquivel" in tw["user"]["name"].lower() or "Nava" in tw["user"]["name"] or "Cano" in tw["user"]["name"] or "Bravo" in tw["user"]["name"] or "duarte" in tw["user"]["name"].lower() or "galindo" in tw["user"]["name"].lower() or "correa" in tw["user"]["name"].lower() or "Parra" in tw["user"]["name"] or "rodriquez" in tw["user"]["name"].lower() or "saldana" in tw["user"]["name"].lower() or "Leal" in tw["user"]["name"] or "sierra" in tw["user"]["name"].lower() or "blanco" in tw["user"]["name"].lower() or "becerra" in tw["user"]["name"].lower() or "carrasco" in tw["user"]["name"].lower() or "portillo" in tw["user"]["name"].lower() or "Tovar" in tw["user"]["name"] or "alfaro" in tw["user"]["name"].lower() or "Vera" in tw["user"]["name"] or "zapata" in tw["user"]["name"].lower() or "Muniz" in tw["user"]["name"] or "cardona" in tw["user"]["name"].lower() or "Vigil" in tw["user"]["name"] or "saucedo" in tw["user"]["name"].lower() or "Baez" in tw["user"]["name"] or "hurtado" in tw["user"]["name"].lower() or "Amaya" in tw["user"]["name"] or "escobedo" in tw["user"]["name"].lower() or "peralta" in tw["user"]["name"].lower() or "arredondo" in tw["user"]["name"].lower() or "aguilera" in tw["user"]["name"].lower() or "zepeda" in tw["user"]["name"].lower() or "rosado" in tw["user"]["name"].lower() or "hinojosa" in tw["user"]["name"].lower() or "renteria" in tw["user"]["name"].lower() or "gallardo" in tw["user"]["name"].lower() or "barrios" in tw["user"]["name"].lower() or "Felix" in tw["user"]["name"] or "castellanos" in tw["user"]["name"].lower() or "Baca" in tw["user"]["name"] or "segura" in tw["user"]["name"].lower() or "guillen" in tw["user"]["name"].lower() or "cordero" in tw["user"]["name"].lower() or "chacon" in tw["user"]["name"].lower() or "Valle" in tw["user"]["name"] or "coronado" in tw["user"]["name"].lower() or "delatorre" in tw["user"]["name"].lower() or "Vela" in tw["user"]["name"] or "alonso" in tw["user"]["name"].lower() or "velasco" in tw["user"]["name"].lower() or "madrigal" in tw["user"]["name"].lower() or "carranza" in tw["user"]["name"].lower() or "quiroz" in tw["user"]["name"].lower() or "Romo" in tw["user"]["name"] or "madrid" in tw["user"]["name"].lower() or "montano" in tw["user"]["name"].lower() or "Serna" in tw["user"]["name"] or "ybarra" in tw["user"]["name"].lower() or "caballero" in tw["user"]["name"].lower() or "burgos" in tw["user"]["name"].lower() or "ventura" in tw["user"]["name"].lower() or "olvera" in tw["user"]["name"].lower() or "Rosa" in tw["user"]["name"] or "varela" in tw["user"]["name"].lower() or "Leyva" in tw["user"]["name"] or "quezada" in tw["user"]["name"].lower() or "bermudez" in tw["user"]["name"].lower() or "benavides" in tw["user"]["name"].lower() or "aragon" in tw["user"]["name"].lower() or "aviles" in tw["user"]["name"].lower() or "Uribe" in tw["user"]["name"] or "Pagan" in tw["user"]["name"] or "paredes" in tw["user"]["name"].lower() or "osorio" in tw["user"]["name"].lower() or "Yanez" in tw["user"]["name"] or "Nieto" in tw["user"]["name"] or "carmona" in tw["user"]["name"].lower() or "granados" in tw["user"]["name"].lower() or "Gil" in tw["user"]["name"] or "montalvo" in tw["user"]["name"].lower() or "casillas" in tw["user"]["name"].lower() or "Lujan" in tw["user"]["name"] or "bustamante" in tw["user"]["name"].lower() or "Rico" in tw["user"]["name"] or "Anaya" in tw["user"]["name"] or "ornelas" in tw["user"]["name"].lower() or "olivares" in tw["user"]["name"].lower() or "canales" in tw["user"]["name"].lower() or "Gamez" in tw["user"]["name"] or "cuellar" in tw["user"]["name"].lower() or "Lemus" in tw["user"]["name"] or "Prado" in tw["user"]["name"] or "barragan" in tw["user"]["name"].lower() or "Paz" in tw["user"]["name"] or "Pina" in tw["user"]["name"] or "reynoso" in tw["user"]["name"].lower() or "valadez" in tw["user"]["name"].lower() or "navarrete" in tw["user"]["name"].lower() or "Otero" in tw["user"]["name"] or "aleman" in tw["user"]["name"].lower() or "marrero" in tw["user"]["name"].lower() or "olivas" in tw["user"]["name"].lower() or "arevalo" in tw["user"]["name"].lower() or "ojeda" in tw["user"]["name"].lower() or "fonseca" in tw["user"]["name"].lower() or "quintanilla" in tw["user"]["name"].lower() or "solano" in tw["user"]["name"].lower() or "escamilla" in tw["user"]["name"].lower() or "feliciano" in tw["user"]["name"].lower() or "tellez" in tw["user"]["name"].lower() or "sepulveda" in tw["user"]["name"].lower() or "orellana" in tw["user"]["name"].lower() or "arreola" in tw["user"]["name"].lower() or "betancourt" in tw["user"]["name"].lower() or "carbajal" in tw["user"]["name"].lower() or "amador" in tw["user"]["name"].lower() or "sotelo" in tw["user"]["name"].lower() or "hidalgo" in tw["user"]["name"].lower() or "ocampo" in tw["user"]["name"].lower() or "rendon" in tw["user"]["name"].lower() or "venegas" in tw["user"]["name"].lower() or "negron" in tw["user"]["name"].lower() or "banuelos" in tw["user"]["name"].lower() or "patino" in tw["user"]["name"].lower() or "cavazos" in tw["user"]["name"].lower() or "torrez" in tw["user"]["name"].lower() or "Matos" in tw["user"]["name"] or "Casas" in tw["user"]["name"] or "godinez" in tw["user"]["name"].lower() or "valdes" in tw["user"]["name"].lower() or "longoria" in tw["user"]["name"].lower() or "ledesma" in tw["user"]["name"].lower() or "alaniz" in tw["user"]["name"].lower() or "aranda" in tw["user"]["name"].lower() or "prieto" in tw["user"]["name"].lower() or "vallejo" in tw["user"]["name"].lower() or "polanco" in tw["user"]["name"].lower() or "zarate" in tw["user"]["name"].lower() or "pulido" in tw["user"]["name"].lower() or "Arce" in tw["user"]["name"] or "barraza" in tw["user"]["name"].lower() or "Mena" in tw["user"]["name"] or "alonzo" in tw["user"]["name"].lower() or "gamboa" in tw["user"]["name"].lower() or "arteaga" in tw["user"]["name"].lower() or "escalante" in tw["user"]["name"].lower() or "valentin" in tw["user"]["name"].lower() or "galvez" in tw["user"]["name"].lower() or "Brito" in tw["user"]["name"] or "Cerda" in tw["user"]["name"] or "zaragoza" in tw["user"]["name"].lower() or "nevarez" in tw["user"]["name"].lower() or "chavarria" in tw["user"]["name"].lower() or "saldivar" in tw["user"]["name"].lower() or "corral" in tw["user"]["name"].lower() or "saavedra" in tw["user"]["name"].lower() or "marroquin" in tw["user"]["name"].lower() or "Chapa" in tw["user"]["name"] or "mireles" in tw["user"]["name"].lower() or "crespo" in tw["user"]["name"].lower() or "arriaga" in tw["user"]["name"].lower() or "covarrubias" in tw["user"]["name"].lower() or "salcedo" in tw["user"]["name"].lower() or "holguin" in tw["user"]["name"].lower() or "Moya" in tw["user"]["name"] or "alcala" in tw["user"]["name"].lower() or "linares" in tw["user"]["name"].lower() or "heredia" in tw["user"]["name"].lower() or "Ceja" in tw["user"]["name"] or "barrientos" in tw["user"]["name"].lower() or "aponte" in tw["user"]["name"].lower() or "montanez" in tw["user"]["name"].lower() or "najera" in tw["user"]["name"].lower() or "cornejo" in tw["user"]["name"].lower() or "alarcon" in tw["user"]["name"].lower() or "ontiveros" in tw["user"]["name"].lower() or "anguiano" in tw["user"]["name"].lower() or "soriano" in tw["user"]["name"].lower() or "pimentel" in tw["user"]["name"].lower() or "elizondo" in tw["user"]["name"].lower() or "zambrano" in tw["user"]["name"].lower() or "rincon" in tw["user"]["name"].lower() or "mondragon" in tw["user"]["name"].lower() or "cazares" in tw["user"]["name"].lower() or "robledo" in tw["user"]["name"].lower() or "Acuna" in tw["user"]["name"] or "Bueno" in tw["user"]["name"] or "bustos" in tw["user"]["name"] or "Adame" in tw["user"]["name"] or "balderas" in tw["user"]["name"].lower() or "delossantos" in tw["user"]["name"].lower() or "toledo" in tw["user"]["name"].lower() or "valdivia" in tw["user"]["name"].lower() or "naranjo" in tw["user"]["name"].lower() or "perales" in tw["user"]["name"].lower() or "delgadillo" in tw["user"]["name"].lower() or "puente" in tw["user"]["name"].lower() or "Frias" in tw["user"]["name"] or "Vidal" in tw["user"]["name"] or "guajardo" in tw["user"]["name"].lower() or "negrete" in tw["user"]["name"].lower() or "collazo" in tw["user"]["name"].lower() or "Abreu" in tw["user"]["name"] or "ceballos" in tw["user"]["name"].lower() or "jaimes" in tw["user"]["name"].lower() or "batista" in tw["user"]["name"].lower() or "irizarry" in tw["user"]["name"].lower() or "espinal" in tw["user"]["name"].lower() or "carrera" in tw["user"]["name"].lower() or "tamayo" in tw["user"]["name"].lower() or "pantoja" in tw["user"]["name"].lower() or "Oliva" in tw["user"]["name"] or "espino" in tw["user"]["name"].lower() or "benavidez" in tw["user"]["name"].lower() or "ordonez" in tw["user"]["name"].lower() or "noriega" in tw["user"]["name"].lower() or "almanza" in tw["user"]["name"].lower() or "urbina" in tw["user"]["name"].lower() or "Limon" in tw["user"]["name"] or "gaytan" in tw["user"]["name"].lower() or "montero" in tw["user"]["name"].lower() or "archuleta" in tw["user"]["name"].lower() or "armenta" in tw["user"]["name"].lower() or "Banda" in tw["user"]["name"] or "farias" in tw["user"]["name"].lower() or "tejeda" in tw["user"]["name"].lower() or "fierro" in tw["user"]["name"].lower() or "mojica" in tw["user"]["name"].lower() or "solorzano" in tw["user"]["name"].lower() or "villasenor" in tw["user"]["name"].lower() or "Mesa" in tw["user"]["name"] or "Mares" in tw["user"]["name"] or "tirado" in tw["user"]["name"].lower() or "Lira" in tw["user"]["name"] or "aguayo" in tw["user"]["name"].lower() or "Lerma" in tw["user"]["name"] or "argueta" in tw["user"]["name"].lower() or "Palma" in tw["user"]["name"] or "Jaime" in tw["user"]["name"] or "aquino" in tw["user"]["name"].lower() or "alicea" in tw["user"]["name"].lower() or "Soria" in tw["user"]["name"] or "solorio" in tw["user"]["name"].lower() or "Jasso" in tw["user"]["name"] or "valles" in tw["user"]["name"].lower() or "garibay" in tw["user"]["name"].lower() or "cintron" in tw["user"]["name"].lower() or "centeno" in tw["user"]["name"].lower() or "preciado" in tw["user"]["name"].lower() or "Loera" in tw["user"]["name"] or "henriquez" in tw["user"]["name"].lower() or "briones" in tw["user"]["name"].lower() or "armendariz" in tw["user"]["name"].lower() or "Giron" in tw["user"]["name"] or "lomeli" in tw["user"]["name"].lower() or "caraballo" in tw["user"]["name"].lower() or "berrios" in tw["user"]["name"].lower() or "barbosa" in tw["user"]["name"].lower() or "Garay" in tw["user"]["name"] or "tejada" in tw["user"]["name"].lower() or "Loya" in tw["user"]["name"] or "angulo" in tw["user"]["name"].lower() or "regalado" in tw["user"]["name"].lower() or "apodaca" in tw["user"]["name"].lower() or "Mota" in tw["user"]["name"] or "duenas" in tw["user"]["name"].lower() or "jauregui" in tw["user"]["name"].lower() or "segovia" in tw["user"]["name"].lower() or "Ulloa" in tw["user"]["name"] or "araujo" in tw["user"]["name"].lower() or "monroy" in tw["user"]["name"].lower() or "roldan" in tw["user"]["name"].lower() or "porras" in tw["user"]["name"].lower() or "padron" in tw["user"]["name"].lower() or "cadena" in tw["user"]["name"].lower() or "vergara" in tw["user"]["name"].lower() or "alcantar" in tw["user"]["name"].lower() or "delagarza" in tw["user"]["name"].lower() or "ferrer" in tw["user"]["name"].lower() or "delvalle" in tw["user"]["name"].lower() or "munguia" in tw["user"]["name"].lower() or "fajardo" in tw["user"]["name"].lower() or "pedraza" in tw["user"]["name"].lower() or "santillan" in tw["user"]["name"].lower() or "Razo" in tw["user"]["name"] or "aparicio" in tw["user"]["name"].lower() or "carlos" in tw["user"]["name"].lower() or "salcido" in tw["user"]["name"].lower() or "quinonez" in tw["user"]["name"].lower() or "Roque" in tw["user"]["name"] or "sauceda" in tw["user"]["name"].lower() or "estrella" in tw["user"]["name"].lower() or "falcon" in tw["user"]["name"].lower() or "carreon" in tw["user"]["name"].lower() or "briseno" in tw["user"]["name"].lower() or "florez" in tw["user"]["name"].lower() or "llamas" in tw["user"]["name"].lower() or "cepeda" in tw["user"]["name"].lower() or "olivarez" in tw["user"]["name"].lower() or "camarena" in tw["user"]["name"].lower() or "altamirano" in tw["user"]["name"].lower() or "ruelas" in tw["user"]["name"].lower() or "botello" in tw["user"]["name"].lower() or "resendez" in tw["user"]["name"].lower() or "Urena" in tw["user"]["name"] or "millan" in tw["user"]["name"].lower() or "Alba" in tw["user"]["name"] or "Perea" in tw["user"]["name"] or "ruvalcaba" in tw["user"]["name"].lower() or "sifuentes" in tw["user"]["name"].lower() or "pedroza" in tw["user"]["name"].lower() or "Ramon" in tw["user"]["name"] or "terrazas" in tw["user"]["name"].lower() or "corrales" in tw["user"]["name"].lower()):
# 		lat.add(tw["user"]["id"])
# 	elif("Deion" in tw["user"]["name"] or "deiondre" in tw["user"]["name"].lower() or "Dele" in tw["user"]["name"] or "denzel" in tw["user"]["name"].lower() or "dewayne" in tw["user"]["name"].lower() or "dikembe" in tw["user"]["name"].lower() or "duante" in tw["user"]["name"].lower() or "Jamar" in tw["user"]["name"] or "jevonte" in tw["user"]["name"].lower() or "kadeem" in tw["user"]["name"].lower() or "kendis" in tw["user"]["name"].lower() or "kentay" in tw["user"]["name"].lower() or "keshawn" in tw["user"]["name"].lower() or "khalon" in tw["user"]["name"].lower() or "Kofi" in tw["user"]["name"] or "kwamin" in tw["user"]["name"].lower() or "Kyan" in tw["user"]["name"] or "kyrone" in tw["user"]["name"].lower() or "la vonn" in tw["user"]["name"].lower() or "Lado" in tw["user"]["name"] or "Laken" in tw["user"]["name"] or "lakista" in tw["user"]["name"].lower() or "lamech" in tw["user"]["name"].lower() or "lavaughn" in tw["user"]["name"].lower() or "lebron" in tw["user"]["name"].lower() or "lisimba" in tw["user"]["name"].lower() or "ludacris" in tw["user"]["name"].lower() or "mablevi" in tw["user"]["name"].lower() or "marques" in tw["user"]["name"].lower() or "mashawn" in tw["user"]["name"].lower() or "montraie" in tw["user"]["name"].lower() or "mykelti" in tw["user"]["name"].lower() or "nabulung" in tw["user"]["name"].lower() or "Naeem" in tw["user"]["name"] or "napoleon" in tw["user"]["name"].lower() or "obiajulu" in tw["user"]["name"].lower() or "quaashie" in tw["user"]["name"].lower() or "quaddus" in tw["user"]["name"].lower() or "quadrees" in tw["user"]["name"].lower() or "quannell" in tw["user"]["name"].lower() or "quarren" in tw["user"]["name"].lower() or "quashawn" in tw["user"]["name"].lower() or "quintavius" in tw["user"]["name"].lower() or "quoitrel" in tw["user"]["name"].lower() or "Raimy" in tw["user"]["name"] or "rashon" in tw["user"]["name"].lower() or "Razi" in tw["user"]["name"] or "roshaun" in tw["user"]["name"].lower() or "runako" in tw["user"]["name"].lower() or "Salim" in tw["user"]["name"] or "beyonce" in tw["user"]["name"].lower() or "cassietta" in tw["user"]["name"].lower() or "cleotha" in tw["user"]["name"].lower() or "dericia" in tw["user"]["name"].lower() or "gaynelle" in tw["user"]["name"].lower() or "kacondra" in tw["user"]["name"].lower() or "kanesha" in tw["user"]["name"].lower() or "keilantra" in tw["user"]["name"].lower() or "keshon" in tw["user"]["name"].lower() or "lachelle" in tw["user"]["name"].lower() or "Lakin" in tw["user"]["name"] or "lanelle" in tw["user"]["name"].lower() or "laquanna" in tw["user"]["name"].lower() or "laqueta" in tw["user"]["name"].lower() or "laquinta" in tw["user"]["name"].lower() or "lashawn" in tw["user"]["name"].lower() or "latanya" in tw["user"]["name"].lower() or "latonya" in tw["user"]["name"].lower() or "latoya" in tw["user"]["name"].lower() or "mekell" in tw["user"]["name"].lower() or "moesha" in tw["user"]["name"].lower() or "muncel" in tw["user"]["name"].lower() or "Najwa" in tw["user"]["name"] or "nakeisha" in tw["user"]["name"].lower() or "nichelle" in tw["user"]["name"].lower() or "niesha" in tw["user"]["name"].lower() or "quanella" in tw["user"]["name"].lower() or "quanesha" in tw["user"]["name"].lower() or "quisha" in tw["user"]["name"].lower() or "ranielle" in tw["user"]["name"].lower() or "ronnell" in tw["user"]["name"].lower() or "shandra" in tw["user"]["name"].lower() or "shaquana" in tw["user"]["name"].lower() or "shateque" in tw["user"]["name"].lower() or "sidone" in tw["user"]["name"].lower() or "talaitha" in tw["user"]["name"].lower() or "talisa" in tw["user"]["name"].lower() or "talisha" in tw["user"]["name"].lower() or "tamika" in tw["user"]["name"].lower() or "tamira" in tw["user"]["name"].lower() or "tamyra" in tw["user"]["name"].lower() or "tanasha" in tw["user"]["name"].lower() or "tandice" in tw["user"]["name"].lower() or "tanginika" in tw["user"]["name"].lower() or "taniel" in tw["user"]["name"].lower() or "tanisha" in tw["user"]["name"].lower() or "tariana" in tw["user"]["name"].lower() or "temima" in tw["user"]["name"].lower() or "shaquille" in tw["user"]["name"].lower() or "shevon" in tw["user"]["name"].lower() or "shontae" in tw["user"]["name"].lower() or "sulaiman" in tw["user"]["name"].lower() or "tabansi" in tw["user"]["name"].lower() or "tabari" in tw["user"]["name"].lower() or "tamarius" in tw["user"]["name"].lower() or "tavarius" in tw["user"]["name"].lower() or "Tavon" in tw["user"]["name"] or "tevaughn" in tw["user"]["name"].lower() or "Tevin" in tw["user"]["name"] or "Trory" in tw["user"]["name"] or "tyrell" in tw["user"]["name"].lower() or "Uba" in tw["user"]["name"] or "Ulan" in tw["user"]["name"] or "Uzoma" in tw["user"]["name"] or "vandwon" in tw["user"]["name"].lower() or "vashon" in tw["user"]["name"].lower() or "veltry" in tw["user"]["name"].lower() or "verlyn" in tw["user"]["name"].lower() or "voshon" in tw["user"]["name"].lower() or "xayvion" in tw["user"]["name"].lower() or "xyshaun" in tw["user"]["name"].lower() or "yobachi" in tw["user"]["name"].lower() or "Zaid" in tw["user"]["name"] or "Zareb" in tw["user"]["name"] or "zashawn" in tw["user"]["name"].lower() or "timberly" in tw["user"]["name"].lower() or "tyesha" in tw["user"]["name"].lower() or "tyrina" in tw["user"]["name"].lower() or "tyronica" in tw["user"]["name"].lower() or "velinda" in tw["user"]["name"].lower() or "wyetta" in tw["user"]["name"].lower() or "Yetty" in tw["user"]["name"] or "jackson" in tw["user"]["name"].lower() or "washington" in tw["user"]["name"].lower() or "Banks" in tw["user"]["name"] or "jefferson" in tw["user"]["name"].lower() or "mosley" in tw["user"]["name"].lower() or "booker" in tw["user"]["name"].lower() or "alston" in tw["user"]["name"].lower() or "gaines" in tw["user"]["name"].lower() or "dorsey" in tw["user"]["name"].lower() or "battle" in tw["user"]["name"].lower() or "pierre" in tw["user"]["name"].lower() or "rivers" in tw["user"]["name"].lower() or "mccray" in tw["user"]["name"].lower() or "ruffin" in tw["user"]["name"].lower() or "hairston" in tw["user"]["name"].lower() or "muhammad" in tw["user"]["name"].lower() or "Heard" in tw["user"]["name"] or "starks" in tw["user"]["name"].lower() or "Epps" in tw["user"]["name"] or "chatman" in tw["user"]["name"].lower() or "samuel" in tw["user"]["name"].lower() or "Louis" in tw["user"]["name"] or "samuels" in tw["user"]["name"].lower() or "smalls" in tw["user"]["name"].lower() or "william" in tw["user"]["name"].lower() or "peoples" in tw["user"]["name"].lower() or "Paige" in tw["user"]["name"] or "mcneal" in tw["user"]["name"].lower() or "mcclendon" in tw["user"]["name"].lower() or "lockett" in tw["user"]["name"].lower() or "Mims" in tw["user"]["name"] or "Diggs" in tw["user"]["name"] or "randle" in tw["user"]["name"].lower() or "woodson" in tw["user"]["name"].lower() or "Myles" in tw["user"]["name"] or "calloway" in tw["user"]["name"].lower() or "Jean" in tw["user"]["name"] or "dawkins" in tw["user"]["name"].lower() or "boykin" in tw["user"]["name"].lower() or "braxton" in tw["user"]["name"].lower() or "Lyles" in tw["user"]["name"] or "bellamy" in tw["user"]["name"].lower() or "bethea" in tw["user"]["name"].lower() or "mcnair" in tw["user"]["name"].lower() or "felder" in tw["user"]["name"].lower() or "witherspoon" in tw["user"]["name"].lower() or "lofton" in tw["user"]["name"].lower() or "francois" in tw["user"]["name"].lower() or "Grier" in tw["user"]["name"] or "darden" in tw["user"]["name"].lower() or "Artis" in tw["user"]["name"] or "scales" in tw["user"]["name"].lower() or "hollins" in tw["user"]["name"].lower() or "singletary" in tw["user"]["name"].lower() or "bowens" in tw["user"]["name"].lower() or "gooden" in tw["user"]["name"].lower() or "stallworth" in tw["user"]["name"].lower() or "Jeter" in tw["user"]["name"] or "mcmillian" in tw["user"]["name"].lower() or "Spann" in tw["user"]["name"] or "faison" in tw["user"]["name"].lower() or "edmond" in tw["user"]["name"].lower() or "Mckoy" in tw["user"]["name"] or "armstead" in tw["user"]["name"].lower() or "tolliver" in tw["user"]["name"].lower() or "drayton" in tw["user"]["name"].lower() or "antoine" in tw["user"]["name"].lower() or "riddick" in tw["user"]["name"].lower() or "batiste" in tw["user"]["name"].lower() or "mcduffie" in tw["user"]["name"].lower() or "barksdale" in tw["user"]["name"].lower() or "belton" in tw["user"]["name"].lower() or "baptiste" in tw["user"]["name"].lower() or "pinkney" in tw["user"]["name"].lower() or "Ivory" in tw["user"]["name"] or "Cooks" in tw["user"]["name"] or "toliver" in tw["user"]["name"].lower() or "archie" in tw["user"]["name"].lower() or "mclaurin" in tw["user"]["name"].lower() or "Lomax" in tw["user"]["name"] or "buford" in tw["user"]["name"].lower() or "purnell" in tw["user"]["name"].lower() or "reddick" in tw["user"]["name"].lower() or "quarles" in tw["user"]["name"].lower() or "royster" in tw["user"]["name"].lower() or "shorter" in tw["user"]["name"].lower() or "ashford" in tw["user"]["name"].lower() or "worthy" in tw["user"]["name"].lower() or "Canty" in tw["user"]["name"] or "Mosby" in tw["user"]["name"] or "outlaw" in tw["user"]["name"].lower() or "Cobbs" in tw["user"]["name"] or "gadson" in tw["user"]["name"].lower() or "pinckney" in tw["user"]["name"].lower() or "mickens" in tw["user"]["name"].lower() or "etienne" in tw["user"]["name"].lower() or "mccants" in tw["user"]["name"].lower() or "roundtree" in tw["user"]["name"].lower() or "Trice" in tw["user"]["name"] or "capers" in tw["user"]["name"].lower() or "spearman" in tw["user"]["name"].lower() or "Macon" in tw["user"]["name"] or "Batts" in tw["user"]["name"] or "billups" in tw["user"]["name"].lower() or "jeanbaptiste" in tw["user"]["name"].lower() or "council" in tw["user"]["name"].lower() or "merriweather" in tw["user"]["name"].lower() or "weatherspoon" in tw["user"]["name"].lower() or "Towns" in tw["user"]["name"] or "luckett" in tw["user"]["name"].lower() or "mcclinton" in tw["user"]["name"].lower() or "winfield" in tw["user"]["name"].lower() or "sherrod" in tw["user"]["name"].lower() or "broadnax" in tw["user"]["name"].lower() or "guyton" in tw["user"]["name"].lower() or "pettway" in tw["user"]["name"].lower() or "upshaw" in tw["user"]["name"].lower() or "spruill" in tw["user"]["name"].lower() or "pleasant" in tw["user"]["name"].lower() or "crayton" in tw["user"]["name"].lower() or "dabney" in tw["user"]["name"].lower() or "Larry" in tw["user"]["name"] or "frierson" in tw["user"]["name"].lower() or "thompkins" in tw["user"]["name"].lower() or "Gayle" in tw["user"]["name"] or "toussaint" in tw["user"]["name"].lower() or "fairley" in tw["user"]["name"].lower() or "heyward" in tw["user"]["name"].lower() or "staten" in tw["user"]["name"].lower() or "rayford" in tw["user"]["name"].lower() or "conyers" in tw["user"]["name"].lower() or "lampkin" in tw["user"]["name"].lower() or "sturdivant" in tw["user"]["name"].lower() or "macklin" in tw["user"]["name"].lower() or "Pride" in tw["user"]["name"] or "Moten" in tw["user"]["name"] or "alexis" in tw["user"]["name"].lower() or "abdullah" in tw["user"]["name"].lower() or "mcgriff" in tw["user"]["name"].lower() or "gladney" in tw["user"]["name"].lower() or "boykins" in tw["user"]["name"].lower() or "moultrie" in tw["user"]["name"].lower() or "Dancy" in tw["user"]["name"] or "Mapp" in tw["user"]["name"] or "Wyche" in tw["user"]["name"] or "alfred" in tw["user"]["name"].lower() or "moorer" in tw["user"]["name"].lower() or "townes" in tw["user"]["name"].lower() or "dinkins" in tw["user"]["name"].lower() or "blanks" in tw["user"]["name"].lower() or "phillip" in tw["user"]["name"].lower() or "Bibbs" in tw["user"]["name"] or "augustin" in tw["user"]["name"].lower() or "lattimore" in tw["user"]["name"].lower() or "hardaway" in tw["user"]["name"].lower() or "liggins" in tw["user"]["name"].lower() or "newson" in tw["user"]["name"].lower() or "favors" in tw["user"]["name"].lower() or "bracey" in tw["user"]["name"].lower() or "alleyne" in tw["user"]["name"].lower() or "Rolle" in tw["user"]["name"] or "pierrelouis" in tw["user"]["name"].lower() or "Kyles" in tw["user"]["name"] or "Coney" in tw["user"]["name"] or "Moton" in tw["user"]["name"] or "polite" in tw["user"]["name"].lower() or "chisolm" in tw["user"]["name"].lower() or "dandridge" in tw["user"]["name"].lower() or "Bey" in tw["user"]["name"] or "Mingo" in tw["user"]["name"] or "dowdell" in tw["user"]["name"].lower() or "cofield" in tw["user"]["name"].lower() or "shabazz" in tw["user"]["name"].lower() or "rembert" in tw["user"]["name"].lower() or "claiborne" in tw["user"]["name"].lower() or "hatchett" in tw["user"]["name"].lower() or "Cage" in tw["user"]["name"] or "cheeks" in tw["user"]["name"].lower() or "celestine" in tw["user"]["name"].lower() or "pegues" in tw["user"]["name"].lower() or "brookins" in tw["user"]["name"].lower() or "Powe" in tw["user"]["name"] or "brockington" in tw["user"]["name"].lower() or "beamon" in tw["user"]["name"].lower() or "jeanlouis" in tw["user"]["name"].lower() or "kirksey" in tw["user"]["name"].lower() or "Suber" in tw["user"]["name"] or "edward" in tw["user"]["name"].lower() or "dortch" in tw["user"]["name"].lower() or "Buggs" in tw["user"]["name"] or "beckford" in tw["user"]["name"].lower() or "benford" in tw["user"]["name"].lower() or "boddie" in tw["user"]["name"].lower() or "dantzler" in tw["user"]["name"].lower() or "Rhone" in tw["user"]["name"] or "pettiford" in tw["user"]["name"].lower() or "Jiles" in tw["user"]["name"] or "Leak" in tw["user"]["name"] or "Silas" in tw["user"]["name"] or "Geter" in tw["user"]["name"] or "jamerson" in tw["user"]["name"].lower() or "baskerville" in tw["user"]["name"].lower() or "mcgruder" in tw["user"]["name"].lower() or "Cadet" in tw["user"]["name"] or "vereen" in tw["user"]["name"].lower() or "eugene" in tw["user"]["name"].lower() or "Womenhear" in tw["user"]["name"].lower() or "gilliard" in tw["user"]["name"].lower() or "brathwaite" in tw["user"]["name"].lower() or "spikes" in tw["user"]["name"].lower() or "diallo" in tw["user"]["name"].lower() or "rankins" in tw["user"]["name"].lower() or "mahone" in tw["user"]["name"].lower() or "jemison" in tw["user"]["name"].lower() or "Yancy" in tw["user"]["name"] or "dingle" in tw["user"]["name"].lower() or "session" in tw["user"]["name"].lower() or "fowlkes" in tw["user"]["name"].lower() or "kamara" in tw["user"]["name"].lower() or "pettaway" in tw["user"]["name"].lower() or "Desir" in tw["user"]["name"] or "rozier" in tw["user"]["name"].lower() or "Eaddy" in tw["user"]["name"] or "middlebrooks" in tw["user"]["name"].lower() or "weathersby" in tw["user"]["name"].lower() or "muldrow" in tw["user"]["name"].lower() or "Tyus" in tw["user"]["name"] or "Belle" in tw["user"]["name"] or "stroman" in tw["user"]["name"].lower() or "shavers" in tw["user"]["name"].lower() or "hughley" in tw["user"]["name"].lower() or "hardeman" in tw["user"]["name"].lower() or "jeanpierre" in tw["user"]["name"].lower() or "Ealy" in tw["user"]["name"] or "cureton" in tw["user"]["name"].lower() or "Nealy" in tw["user"]["name"] or "gadsden" in tw["user"]["name"].lower() or "gatling" in tw["user"]["name"].lower() or "Maye" in tw["user"]["name"] or "littles" in tw["user"]["name"].lower() or "norfleet" in tw["user"]["name"].lower() or "fortson" in tw["user"]["name"].lower() or "Daye" in tw["user"]["name"] or "portis" in tw["user"]["name"].lower() or "dunston" in tw["user"]["name"].lower() or "whitted" in tw["user"]["name"].lower() or "glasper" in tw["user"]["name"].lower() or "narcisse" in tw["user"]["name"].lower() or "Rumph" in tw["user"]["name"] or "Govan" in tw["user"]["name"] or "debose" in tw["user"]["name"].lower() or "marable" in tw["user"]["name"].lower() or "dunson" in tw["user"]["name"].lower() or "Chery" in tw["user"]["name"] or "ceasar" in tw["user"]["name"].lower() or "mensah" in tw["user"]["name"].lower() or "woolfolk" in tw["user"]["name"].lower() or "braggs" in tw["user"]["name"].lower() or "applewhite" in tw["user"]["name"].lower() or "latimore" in tw["user"]["name"].lower() or "mccree" in tw["user"]["name"].lower() or "mccullum" in tw["user"]["name"].lower() or "swinton" in tw["user"]["name"].lower() or "Gales" in tw["user"]["name"] or "wigfall" in tw["user"]["name"].lower() or "fluker" in tw["user"]["name"].lower() or "toomer" in tw["user"]["name"].lower()):
# 		bla.add(tw["user"]["id"])
# 	else:
# 		whi.add(tw["user"]["id"])

def sortEthnic(lat, bla, whi, tw):
	if("Liam" in tw["user"]["name"] or "Noah" in tw["user"]["name"] or "William" in tw["user"]["name"] or "James" in tw["user"]["name"] or "Logan" in tw["user"]["name"] or "Benjamin" in tw["user"]["name"] or "Mason" in tw["user"]["name"] or "Elijah" in tw["user"]["name"] or "Oliver" in tw["user"]["name"] or "Jacob" in tw["user"]["name"] or "Lucas" in tw["user"]["name"] or "Michael" in tw["user"]["name"] or "Alexander" in tw["user"]["name"] or "Ethan" in tw["user"]["name"] or "Daniel" in tw["user"]["name"] or "Matthew" in tw["user"]["name"] or "Aiden" in tw["user"]["name"] or "Henry" in tw["user"]["name"] or "Joseph" in tw["user"]["name"] or "Jackson" in tw["user"]["name"] or "Samuel" in tw["user"]["name"] or "Sebastian" in tw["user"]["name"] or "David" in tw["user"]["name"] or "Carter" in tw["user"]["name"] or "Wyatt" in tw["user"]["name"] or "Jayden" in tw["user"]["name"] or "John" in tw["user"]["name"] or "Owen" in tw["user"]["name"] or "Dylan" in tw["user"]["name"] or "Luke" in tw["user"]["name"] or "Gabriel" in tw["user"]["name"] or "Anthony" in tw["user"]["name"] or "Isaac" in tw["user"]["name"] or "Grayson" in tw["user"]["name"] or "Jack" in tw["user"]["name"] or "Julian" in tw["user"]["name"] or "Levi" in tw["user"]["name"] or "Christopher" in tw["user"]["name"] or "Joshua" in tw["user"]["name"] or "Andrew" in tw["user"]["name"] or "Lincoln" in tw["user"]["name"] or "Mateo" in tw["user"]["name"] or "Ryan" in tw["user"]["name"] or "Jaxon" in tw["user"]["name"] or "Nathan" in tw["user"]["name"] or "Aaron" in tw["user"]["name"] or "Isaiah" in tw["user"]["name"] or "Thomas" in tw["user"]["name"] or "Charles" in tw["user"]["name"] or "Caleb" in tw["user"]["name"] or "Josiah" in tw["user"]["name"] or "Christian" in tw["user"]["name"] or "Hunter" in tw["user"]["name"] or "Eli" in tw["user"]["name"] or "Jonathan" in tw["user"]["name"] or "Connor" in tw["user"]["name"] or "Landon" in tw["user"]["name"] or "Adrian" in tw["user"]["name"] or "Asher" in tw["user"]["name"] or "Cameron" in tw["user"]["name"] or "Leo" in tw["user"]["name"] or "Theodore" in tw["user"]["name"] or "Jeremiah" in tw["user"]["name"] or "Hudson" in tw["user"]["name"] or "Robert" in tw["user"]["name"] or "Easton" in tw["user"]["name"] or "Nolan" in tw["user"]["name"] or "Nicholas" in tw["user"]["name"] or "Ezra" in tw["user"]["name"] or "Colton" in tw["user"]["name"] or "Angel" in tw["user"]["name"] or "Brayden" in tw["user"]["name"] or "Jordan" in tw["user"]["name"] or "Dominic" in tw["user"]["name"] or "Austin" in tw["user"]["name"] or "Ian" in tw["user"]["name"] or "Adam" in tw["user"]["name"] or "Elias" in tw["user"]["name"] or "Jaxson" in tw["user"]["name"] or "Greyson" in tw["user"]["name"] or "Jose" in tw["user"]["name"] or "Ezekiel" in tw["user"]["name"] or "Carson" in tw["user"]["name"] or "Evan" in tw["user"]["name"] or "Maverick" in tw["user"]["name"] or "Bryson" in tw["user"]["name"] or "Jace" in tw["user"]["name"] or "Cooper" in tw["user"]["name"] or "Xavier" in tw["user"]["name"] or "Parker" in tw["user"]["name"] or "Roman" in tw["user"]["name"] or "Jason" in tw["user"]["name"] or "Santiago" in tw["user"]["name"] or "Chase" in tw["user"]["name"] or "Sawyer" in tw["user"]["name"] or "Gavin" in tw["user"]["name"] or "Leonardo" in tw["user"]["name"] or "Kayden" in tw["user"]["name"] or "Ayden" in tw["user"]["name"] or "Jameson" in tw["user"]["name"] or "Kevin" in tw["user"]["name"] or "Bentley" in tw["user"]["name"] or "Zachary" in tw["user"]["name"] or "Everett" in tw["user"]["name"] or "Axel" in tw["user"]["name"] or "Tyler" in tw["user"]["name"] or "Micah" in tw["user"]["name"] or "Vincent" in tw["user"]["name"] or "Weston" in tw["user"]["name"] or "Miles" in tw["user"]["name"] or "Wesley" in tw["user"]["name"] or "Nathaniel" in tw["user"]["name"] or "Harrison" in tw["user"]["name"] or "Brandon" in tw["user"]["name"] or "Cole" in tw["user"]["name"] or "Declan" in tw["user"]["name"] or "Luis" in tw["user"]["name"] or "Braxton" in tw["user"]["name"] or "Damian" in tw["user"]["name"] or "Silas" in tw["user"]["name"] or "Tristan" in tw["user"]["name"] or "Ryder" in tw["user"]["name"] or "Bennett" in tw["user"]["name"] or "George" in tw["user"]["name"] or "Emmett" in tw["user"]["name"] or "Justin" in tw["user"]["name"] or "Kai" in tw["user"]["name"] or "Max" in tw["user"]["name"] or "Diego" in tw["user"]["name"] or "Luca" in tw["user"]["name"] or "Ryker" in tw["user"]["name"] or "Carlos" in tw["user"]["name"] or "Maxwell" in tw["user"]["name"] or "Kingston" in tw["user"]["name"] or "Ivan" in tw["user"]["name"] or "Maddox" in tw["user"]["name"] or "Juan" in tw["user"]["name"] or "Ashton" in tw["user"]["name"] or "Jayce" in tw["user"]["name"] or "Rowan" in tw["user"]["name"] or "Kaiden" in tw["user"]["name"] or "Giovanni" in tw["user"]["name"] or "Eric" in tw["user"]["name"] or "Jesus" in tw["user"]["name"] or "Calvin" in tw["user"]["name"] or "Abel" in tw["user"]["name"] or "King" in tw["user"]["name"] or "Camden" in tw["user"]["name"] or "Amir" in tw["user"]["name"] or "Blake" in tw["user"]["name"] or "Alex" in tw["user"]["name"] or "Brody" in tw["user"]["name"] or "Malachi" in tw["user"]["name"] or "Emmanuel" in tw["user"]["name"] or "Jonah" in tw["user"]["name"] or "Beau" in tw["user"]["name"] or "Jude" in tw["user"]["name"] or "Antonio" in tw["user"]["name"] or "Alan" in tw["user"]["name"] or "Elliott" in tw["user"]["name"] or "Elliot" in tw["user"]["name"] or "Waylon" in tw["user"]["name"] or "Xander" in tw["user"]["name"] or "Timothy" in tw["user"]["name"] or "Victor" in tw["user"]["name"] or "Bryce" in tw["user"]["name"] or "Finn" in tw["user"]["name"] or "Brantley" in tw["user"]["name"] or "Edward" in tw["user"]["name"] or "Abraham" in tw["user"]["name"] or "Patrick" in tw["user"]["name"] or "Grant" in tw["user"]["name"] or "Karter" in tw["user"]["name"] or "Hayden" in tw["user"]["name"] or "Richard" in tw["user"]["name"] or "Miguel" in tw["user"]["name"] or "Joel" in tw["user"]["name"] or "Gael" in tw["user"]["name"] or "Tucker" in tw["user"]["name"] or "Rhett" in tw["user"]["name"] or "Avery" in tw["user"]["name"] or "Steven" in tw["user"]["name"] or "Graham" in tw["user"]["name"] or "Kaleb" in tw["user"]["name"] or "Jasper" in tw["user"]["name"] or "Jesse" in tw["user"]["name"] or "Matteo" in tw["user"]["name"] or "Dean" in tw["user"]["name"] or "Zayden" in tw["user"]["name"] or "Preston" in tw["user"]["name"] or "August" in tw["user"]["name"] or "Oscar" in tw["user"]["name"] or "Jeremy" in tw["user"]["name"] or "Alejandro" in tw["user"]["name"] or "Marcus" in tw["user"]["name"] or "Dawson" in tw["user"]["name"] or "Lorenzo" in tw["user"]["name"] or "Messiah" in tw["user"]["name"] or "Zion" in tw["user"]["name"] or "Maximus" in tw["user"]["name"] or "River" in tw["user"]["name"] or "Zane" in tw["user"]["name"] or "Mark" in tw["user"]["name"] or "Brooks" in tw["user"]["name"] or "Nicolas" in tw["user"]["name"] or "Paxton" in tw["user"]["name"] or "Judah" in tw["user"]["name"] or "Emiliano" in tw["user"]["name"] or "Kaden" in tw["user"]["name"] or "Bryan" in tw["user"]["name"] or "Kyle" in tw["user"]["name"] or "Myles" in tw["user"]["name"] or "Peter" in tw["user"]["name"] or "Charlie" in tw["user"]["name"] or "Kyrie" in tw["user"]["name"] or "Thiago" in tw["user"]["name"] or "Brian" in tw["user"]["name"] or "Kenneth" in tw["user"]["name"] or "Andres" in tw["user"]["name"] or "Lukas" in tw["user"]["name"] or "Aidan" in tw["user"]["name"] or "Jax" in tw["user"]["name"] or "Caden" in tw["user"]["name"] or "Milo" in tw["user"]["name"] or "Paul" in tw["user"]["name"] or "Beckett" in tw["user"]["name"] or "Brady" in tw["user"]["name"] or "Colin" in tw["user"]["name"] or "Omar" in tw["user"]["name"] or "Bradley" in tw["user"]["name"] or "Javier" in tw["user"]["name"] or "Knox" in tw["user"]["name"] or "Jaden" in tw["user"]["name"] or "Barrett" in tw["user"]["name"] or "Israel" in tw["user"]["name"] or "Matias" in tw["user"]["name"] or "Jorge" in tw["user"]["name"] or "Zander" in tw["user"]["name"] or "Derek" in tw["user"]["name"] or "Josue" in tw["user"]["name"] or "Cayden" in tw["user"]["name"] or "Holden" in tw["user"]["name"] or "Griffin" in tw["user"]["name"] or "Arthur" in tw["user"]["name"] or "Leon" in tw["user"]["name"] or "Felix" in tw["user"]["name"] or "Remington" in tw["user"]["name"] or "Jake" in tw["user"]["name"] or "Killian" in tw["user"]["name"] or "Clayton" in tw["user"]["name"] or "Sean" in tw["user"]["name"] or "Adriel" in tw["user"]["name"] or "Riley" in tw["user"]["name"] or "Archer" in tw["user"]["name"] or "Legend" in tw["user"]["name"] or "Erick" in tw["user"]["name"] or "Enzo" in tw["user"]["name"] or "Corbin" in tw["user"]["name"] or "Francisco" in tw["user"]["name"] or "Dallas" in tw["user"]["name"] or "Emilio" in tw["user"]["name"] or "Gunner" in tw["user"]["name"] or "Simon" in tw["user"]["name"] or "Andre" in tw["user"]["name"] or "Walter" in tw["user"]["name"] or "Damien" in tw["user"]["name"] or "Chance" in tw["user"]["name"] or "Phoenix" in tw["user"]["name"] or "Colt" in tw["user"]["name"] or "Tanner" in tw["user"]["name"] or "Stephen" in tw["user"]["name"] or "Kameron" in tw["user"]["name"] or "Tobias" in tw["user"]["name"] or "Manuel" in tw["user"]["name"] or "Amari" in tw["user"]["name"] or "Emerson" in tw["user"]["name"] or "Louis" in tw["user"]["name"] or "Cody" in tw["user"]["name"] or "Finley" in tw["user"]["name"] or "Iker" in tw["user"]["name"] or "Martin" in tw["user"]["name"] or "Rafael" in tw["user"]["name"] or "Nash" in tw["user"]["name"] or "Beckham" in tw["user"]["name"] or "Cash" in tw["user"]["name"] or "Karson" in tw["user"]["name"] or "Rylan" in tw["user"]["name"] or "Reid" in tw["user"]["name"] or "Theo" in tw["user"]["name"] or "Ace" in tw["user"]["name"] or "Eduardo" in tw["user"]["name"] or "Spencer" in tw["user"]["name"] or "Raymond" in tw["user"]["name"] or "Maximiliano" in tw["user"]["name"] or "Anderson" in tw["user"]["name"] or "Ronan" in tw["user"]["name"] or "Lane" in tw["user"]["name"] or "Cristian" in tw["user"]["name"] or "Titus" in tw["user"]["name"] or "Travis" in tw["user"]["name"] or "Jett" in tw["user"]["name"] or "Ricardo" in tw["user"]["name"] or "Bodhi" in tw["user"]["name"] or "Gideon" in tw["user"]["name"] or "Jaiden" in tw["user"]["name"] or "Fernando" in tw["user"]["name"] or "Mario" in tw["user"]["name"] or "Conor" in tw["user"]["name"] or "Keegan" in tw["user"]["name"] or "Ali" in tw["user"]["name"] or "Cesar" in tw["user"]["name"] or "Ellis" in tw["user"]["name"] or "Jayceon" in tw["user"]["name"] or "Walker" in tw["user"]["name"] or "Cohen" in tw["user"]["name"] or "Arlo" in tw["user"]["name"] or "Hector" in tw["user"]["name"] or "Dante" in tw["user"]["name"] or "Kyler" in tw["user"]["name"] or "Garrett" in tw["user"]["name"] or "Donovan" in tw["user"]["name"] or "Seth" in tw["user"]["name"] or "Jeffrey" in tw["user"]["name"] or "Tyson" in tw["user"]["name"] or "Jase" in tw["user"]["name"] or "Desmond" in tw["user"]["name"] or "Caiden" in tw["user"]["name"] or "Gage" in tw["user"]["name"] or "Atlas" in tw["user"]["name"] or "Major" in tw["user"]["name"] or "Devin" in tw["user"]["name"] or "Edwin" in tw["user"]["name"] or "Angelo" in tw["user"]["name"] or "Orion" in tw["user"]["name"] or "Conner" in tw["user"]["name"] or "Julius" in tw["user"]["name"] or "Marco" in tw["user"]["name"] or "Jensen" in tw["user"]["name"] or "Daxton" in tw["user"]["name"] or "Peyton" in tw["user"]["name"] or "Zayn" in tw["user"]["name"] or "Collin" in tw["user"]["name"] or "Jaylen" in tw["user"]["name"] or "Dakota" in tw["user"]["name"] or "Prince" in tw["user"]["name"] or "Johnny" in tw["user"]["name"] or "Kayson" in tw["user"]["name"] or "Cruz" in tw["user"]["name"] or "Hendrix" in tw["user"]["name"] or "Atticus" in tw["user"]["name"] or "Troy" in tw["user"]["name"] or "Kane" in tw["user"]["name"] or "Edgar" in tw["user"]["name"] or "Sergio" in tw["user"]["name"] or "Kash" in tw["user"]["name"] or "Marshall" in tw["user"]["name"] or "Johnathan" in tw["user"]["name"] or "Romeo" in tw["user"]["name"] or "Shane" in tw["user"]["name"] or "Warren" in tw["user"]["name"] or "Joaquin" in tw["user"]["name"] or "Wade" in tw["user"]["name"] or "Leonel" in tw["user"]["name"] or "Trevor" in tw["user"]["name"] or "Dominick" in tw["user"]["name"] or "Muhammad" in tw["user"]["name"] or "Erik" in tw["user"]["name"] or "Odin" in tw["user"]["name"] or "Quinn" in tw["user"]["name"] or "Jaxton" in tw["user"]["name"] or "Dalton" in tw["user"]["name"] or "Nehemiah" in tw["user"]["name"] or "Frank" in tw["user"]["name"] or "Grady" in tw["user"]["name"] or "Gregory" in tw["user"]["name"] or "Andy" in tw["user"]["name"] or "Solomon" in tw["user"]["name"] or "Malik" in tw["user"]["name"] or "Rory" in tw["user"]["name"] or "Clark" in tw["user"]["name"] or "Reed" in tw["user"]["name"] or "Harvey" in tw["user"]["name"] or "Zayne" in tw["user"]["name"] or "Jay" in tw["user"]["name"] or "Jared" in tw["user"]["name"] or "Noel" in tw["user"]["name"] or "Shawn" in tw["user"]["name"] or "Fabian" in tw["user"]["name"] or "Ibrahim" in tw["user"]["name"] or "Adonis" in tw["user"]["name"] or "Ismael" in tw["user"]["name"] or "Pedro" in tw["user"]["name"] or "Leland" in tw["user"]["name"] or "Malakai" in tw["user"]["name"] or "Malcolm" in tw["user"]["name"] or "Alexis" in tw["user"]["name"] or "Kason" in tw["user"]["name"] or "Porter" in tw["user"]["name"] or "Sullivan" in tw["user"]["name"] or "Raiden" in tw["user"]["name"] or "Allen" in tw["user"]["name"] or "Ari" in tw["user"]["name"] or "Russell" in tw["user"]["name"] or "Princeton" in tw["user"]["name"] or "Winston" in tw["user"]["name"] or "Kendrick" in tw["user"]["name"] or "Roberto" in tw["user"]["name"] or "Lennox" in tw["user"]["name"] or "Hayes" in tw["user"]["name"] or "Finnegan" in tw["user"]["name"] or "Nasir" in tw["user"]["name"] or "Kade" in tw["user"]["name"] or "Nico" in tw["user"]["name"] or "Emanuel" in tw["user"]["name"] or "Landen" in tw["user"]["name"] or "Moises" in tw["user"]["name"] or "Ruben" in tw["user"]["name"] or "Hugo" in tw["user"]["name"] or "Abram" in tw["user"]["name"] or "Adan" in tw["user"]["name"] or "Khalil" in tw["user"]["name"] or "Zaiden" in tw["user"]["name"] or "Augustus" in tw["user"]["name"] or "Marcos" in tw["user"]["name"] or "Philip" in tw["user"]["name"] or "Phillip" in tw["user"]["name"] or "Cyrus" in tw["user"]["name"] or "Esteban" in tw["user"]["name"] or "Braylen" in tw["user"]["name"] or "Albert" in tw["user"]["name"] or "Bruce" in tw["user"]["name"] or "Kamden" in tw["user"]["name"] or "Lawson" in tw["user"]["name"] or "Jamison" in tw["user"]["name"] or "Sterling" in tw["user"]["name"] or "Damon" in tw["user"]["name"] or "Gunnar" in tw["user"]["name"] or "Kyson" in tw["user"]["name"] or "Luka" in tw["user"]["name"] or "Franklin" in tw["user"]["name"] or "Ezequiel" in tw["user"]["name"] or "Pablo" in tw["user"]["name"] or "Derrick" in tw["user"]["name"] or "Zachariah" in tw["user"]["name"] or "Cade" in tw["user"]["name"] or "Jonas" in tw["user"]["name"] or "Dexter" in tw["user"]["name"] or "Kolton" in tw["user"]["name"] or "Remy" in tw["user"]["name"] or "Hank" in tw["user"]["name"] or "Tate" in tw["user"]["name"] or "Trenton" in tw["user"]["name"] or "Kian" in tw["user"]["name"] or "Drew" in tw["user"]["name"] or "Mohamed" in tw["user"]["name"] or "Dax" in tw["user"]["name"] or "Rocco" in tw["user"]["name"] or "Bowen" in tw["user"]["name"] or "Mathias" in tw["user"]["name"] or "Ronald" in tw["user"]["name"] or "Francis" in tw["user"]["name"] or "Matthias" in tw["user"]["name"] or "Milan" in tw["user"]["name"] or "Maximilian" in tw["user"]["name"] or "Royce" in tw["user"]["name"] or "Skyler" in tw["user"]["name"] or "Corey" in tw["user"]["name"] or "Kasen" in tw["user"]["name"] or "Drake" in tw["user"]["name"] or "Gerardo" in tw["user"]["name"] or "Jayson" in tw["user"]["name"] or "Sage" in tw["user"]["name"] or "Braylon" in tw["user"]["name"] or "Benson" in tw["user"]["name"] or "Moses" in tw["user"]["name"] or "Alijah" in tw["user"]["name"] or "Rhys" in tw["user"]["name"] or "Otto" in tw["user"]["name"] or "Oakley" in tw["user"]["name"] or "Armando" in tw["user"]["name"] or "Jaime" in tw["user"]["name"] or "Nixon" in tw["user"]["name"] or "Saul" in tw["user"]["name"] or "Scott" in tw["user"]["name"] or "Brycen" in tw["user"]["name"] or "Ariel" in tw["user"]["name"] or "Enrique" in tw["user"]["name"] or "Donald" in tw["user"]["name"] or "Chandler" in tw["user"]["name"] or "Asa" in tw["user"]["name"] or "Eden" in tw["user"]["name"] or "Davis" in tw["user"]["name"] or "Keith" in tw["user"]["name"] or "Frederick" in tw["user"]["name"] or "Rowen" in tw["user"]["name"] or "Lawrence" in tw["user"]["name"] or "Leonidas" in tw["user"]["name"] or "Aden" in tw["user"]["name"] or "Julio" in tw["user"]["name"] or "Darius" in tw["user"]["name"] or "Johan" in tw["user"]["name"] or "Deacon" in tw["user"]["name"] or "Cason" in tw["user"]["name"] or "Danny" in tw["user"]["name"] or "Nikolai" in tw["user"]["name"] or "Taylor" in tw["user"]["name"] or "Alec" in tw["user"]["name"] or "Royal" in tw["user"]["name"] or "Armani" in tw["user"]["name"] or "Kieran" in tw["user"]["name"] or "Luciano" in tw["user"]["name"] or "Omari" in tw["user"]["name"] or "Rodrigo" in tw["user"]["name"] or "Arjun" in tw["user"]["name"] or "Ahmed" in tw["user"]["name"] or "Brendan" in tw["user"]["name"] or "Cullen" in tw["user"]["name"] or "Raul" in tw["user"]["name"] or "Raphael" in tw["user"]["name"] or "Ronin" in tw["user"]["name"] or "Brock" in tw["user"]["name"] or "Pierce" in tw["user"]["name"] or "Alonzo" in tw["user"]["name"] or "Casey" in tw["user"]["name"] or "Dillon" in tw["user"]["name"] or "Uriel" in tw["user"]["name"] or "Dustin" in tw["user"]["name"] or "Gianni" in tw["user"]["name"] or "Roland" in tw["user"]["name"] or "Landyn" in tw["user"]["name"] or "Kobe" in tw["user"]["name"] or "Dorian" in tw["user"]["name"] or "Emmitt" in tw["user"]["name"] or "Ryland" in tw["user"]["name"] or "Apollo" in tw["user"]["name"] or "Aarav" in tw["user"]["name"] or "Roy" in tw["user"]["name"] or "Duke" in tw["user"]["name"] or "Quentin" in tw["user"]["name"] or "Sam" in tw["user"]["name"] or "Lewis" in tw["user"]["name"] or "Tony" in tw["user"]["name"] or "Uriah" in tw["user"]["name"] or "Dennis" in tw["user"]["name"] or "Moshe" in tw["user"]["name"] or "Isaias" in tw["user"]["name"] or "Braden" in tw["user"]["name"] or "Quinton" in tw["user"]["name"] or "Cannon" in tw["user"]["name"] or "Ayaan" in tw["user"]["name"] or "Mathew" in tw["user"]["name"] or "Kellan" in tw["user"]["name"] or "Niko" in tw["user"]["name"] or "Edison" in tw["user"]["name"] or "Izaiah" in tw["user"]["name"] or "Jerry" in tw["user"]["name"] or "Gustavo" in tw["user"]["name"] or "Jamari" in tw["user"]["name"] or "Marvin" in tw["user"]["name"] or "Mauricio" in tw["user"]["name"] or "Ahmad" in tw["user"]["name"] or "Mohammad" in tw["user"]["name"] or "Justice" in tw["user"]["name"] or "Trey" in tw["user"]["name"] or "Elian" in tw["user"]["name"] or "Mohammed" in tw["user"]["name"] or "Sincere" in tw["user"]["name"] or "Yusuf" in tw["user"]["name"] or "Arturo" in tw["user"]["name"] or "Callen" in tw["user"]["name"] or "Rayan" in tw["user"]["name"] or "Keaton" in tw["user"]["name"] or "Wilder" in tw["user"]["name"] or "Mekhi" in tw["user"]["name"] or "Memphis" in tw["user"]["name"] or "Cayson" in tw["user"]["name"] or "Conrad" in tw["user"]["name"] or "Kaison" in tw["user"]["name"] or "Kyree" in tw["user"]["name"] or "Soren" in tw["user"]["name"] or "Colby" in tw["user"]["name"] or "Bryant" in tw["user"]["name"] or "Lucian" in tw["user"]["name"] or "Alfredo" in tw["user"]["name"] or "Cassius" in tw["user"]["name"] or "Marcelo" in tw["user"]["name"] or "Nikolas" in tw["user"]["name"] or "Brennan" in tw["user"]["name"] or "Darren" in tw["user"]["name"] or "Jasiah" in tw["user"]["name"] or "Jimmy" in tw["user"]["name"] or "Lionel" in tw["user"]["name"] or "Reece" in tw["user"]["name"] or "Ty" in tw["user"]["name"] or "Chris" in tw["user"]["name"] or "Forrest" in tw["user"]["name"] or "Korbin" in tw["user"]["name"] or "Tatum" in tw["user"]["name"] or "Jalen" in tw["user"]["name"] or "Santino" in tw["user"]["name"] or "Case" in tw["user"]["name"] or "Leonard" in tw["user"]["name"] or "Alvin" in tw["user"]["name"] or "Issac" in tw["user"]["name"] or "Bo" in tw["user"]["name"] or "Quincy" in tw["user"]["name"] or "Mack" in tw["user"]["name"] or "Samson" in tw["user"]["name"] or "Rex" in tw["user"]["name"] or "Alberto" in tw["user"]["name"] or "Callum" in tw["user"]["name"] or "Curtis" in tw["user"]["name"] or "Hezekiah" in tw["user"]["name"] or "Finnley" in tw["user"]["name"] or "Briggs" in tw["user"]["name"] or "Kamari" in tw["user"]["name"] or "Zeke" in tw["user"]["name"] or "Raylan" in tw["user"]["name"] or "Neil" in tw["user"]["name"] or "Titan" in tw["user"]["name"] or "Julien" in tw["user"]["name"] or "Kellen" in tw["user"]["name"] or "Devon" in tw["user"]["name"] or "Kylan" in tw["user"]["name"] or "Roger" in tw["user"]["name"] or "Axton" in tw["user"]["name"] or "Carl" in tw["user"]["name"] or "Douglas" in tw["user"]["name"] or "Larry" in tw["user"]["name"] or "Crosby" in tw["user"]["name"] or "Fletcher" in tw["user"]["name"] or "Makai" in tw["user"]["name"] or "Nelson" in tw["user"]["name"] or "Hamza" in tw["user"]["name"] or "Lance" in tw["user"]["name"] or "Alden" in tw["user"]["name"] or "Gary" in tw["user"]["name"] or "Wilson" in tw["user"]["name"] or "Alessandro" in tw["user"]["name"] or "Ares" in tw["user"]["name"] or "Kashton" in tw["user"]["name"] or "Bruno" in tw["user"]["name"] or "Jakob" in tw["user"]["name"] or "Stetson" in tw["user"]["name"] or "Zain" in tw["user"]["name"] or "Cairo" in tw["user"]["name"] or "Nathanael" in tw["user"]["name"] or "Byron" in tw["user"]["name"] or "Harry" in tw["user"]["name"] or "Harley" in tw["user"]["name"] or "Mitchell" in tw["user"]["name"] or "Maurice" in tw["user"]["name"] or "Orlando" in tw["user"]["name"] or "Kingsley" in tw["user"]["name"] or "Kaysen" in tw["user"]["name"] or "Sylas" in tw["user"]["name"] or "Trent" in tw["user"]["name"] or "Ramon" in tw["user"]["name"] or "Boston" in tw["user"]["name"] or "Lucca" in tw["user"]["name"] or "Noe" in tw["user"]["name"] or "Jagger" in tw["user"]["name"] or "Reyansh" in tw["user"]["name"] or "Vihaan" in tw["user"]["name"] or "Randy" in tw["user"]["name"] or "Thaddeus" in tw["user"]["name"] or "Lennon" in tw["user"]["name"] or "Kannon" in tw["user"]["name"] or "Kohen" in tw["user"]["name"] or "Tristen" in tw["user"]["name"] or "Valentino" in tw["user"]["name"] or "Maxton" in tw["user"]["name"] or "Salvador" in tw["user"]["name"] or "Abdiel" in tw["user"]["name"] or "Langston" in tw["user"]["name"] or "Rohan" in tw["user"]["name"] or "Kristopher" in tw["user"]["name"] or "Yosef" in tw["user"]["name"] or "Rayden" in tw["user"]["name"] or "Lee" in tw["user"]["name"] or "Callan" in tw["user"]["name"] or "Tripp" in tw["user"]["name"] or "Deandre" in tw["user"]["name"] or "Joe" in tw["user"]["name"] or "Morgan" in tw["user"]["name"] or "Dariel" in tw["user"]["name"] or "Colten" in tw["user"]["name"] or "Reese" in tw["user"]["name"] or "Jedidiah" in tw["user"]["name"] or "Ricky" in tw["user"]["name"] or "Bronson" in tw["user"]["name"] or "Terry" in tw["user"]["name"] or "Eddie" in tw["user"]["name"] or "Jefferson" in tw["user"]["name"] or "Lachlan" in tw["user"]["name"] or "Layne" in tw["user"]["name"] or "Clay" in tw["user"]["name"] or "Madden" in tw["user"]["name"] or "Jamir" in tw["user"]["name"] or "Tomas" in tw["user"]["name"] or "Kareem" in tw["user"]["name"] or "Stanley" in tw["user"]["name"] or "Brayan" in tw["user"]["name"] or "Amos" in tw["user"]["name"] or "Kase" in tw["user"]["name"] or "Kristian" in tw["user"]["name"] or "Clyde" in tw["user"]["name"] or "Ernesto" in tw["user"]["name"] or "Tommy" in tw["user"]["name"] or "Casen" in tw["user"]["name"] or "Ford" in tw["user"]["name"] or "Crew" in tw["user"]["name"] or "Braydon" in tw["user"]["name"] or "Brecken" in tw["user"]["name"] or "Hassan" in tw["user"]["name"] or "Axl" in tw["user"]["name"] or "Boone" in tw["user"]["name"] or "Leandro" in tw["user"]["name"] or "Samir" in tw["user"]["name"] or "Jaziel" in tw["user"]["name"] or "Magnus" in tw["user"]["name"] or "Abdullah" in tw["user"]["name"] or "Yousef" in tw["user"]["name"] or "Branson" in tw["user"]["name"] or "Jadiel" in tw["user"]["name"] or "Jaxen" in tw["user"]["name"] or "Layton" in tw["user"]["name"] or "Franco" in tw["user"]["name"] or "Ben" in tw["user"]["name"] or "Grey" in tw["user"]["name"] or "Kelvin" in tw["user"]["name"] or "Chaim" in tw["user"]["name"] or "Demetrius" in tw["user"]["name"] or "Blaine" in tw["user"]["name"] or "Ridge" in tw["user"]["name"] or "Colson" in tw["user"]["name"] or "Melvin" in tw["user"]["name"] or "Anakin" in tw["user"]["name"] or "Aryan" in tw["user"]["name"] or "Lochlan" in tw["user"]["name"] or "Jon" in tw["user"]["name"] or "Canaan" in tw["user"]["name"] or "Dash" in tw["user"]["name"] or "Zechariah" in tw["user"]["name"] or "Alonso" in tw["user"]["name"] or "Otis" in tw["user"]["name"] or "Zaire" in tw["user"]["name"] or "Marcel" in tw["user"]["name"] or "Brett" in tw["user"]["name"] or "Stefan" in tw["user"]["name"] or "Aldo" in tw["user"]["name"] or "Jeffery" in tw["user"]["name"] or "Baylor" in tw["user"]["name"] or "Talon" in tw["user"]["name"] or "Dominik" in tw["user"]["name"] or "Flynn" in tw["user"]["name"] or "Carmelo" in tw["user"]["name"] or "Dane" in tw["user"]["name"] or "Jamal" in tw["user"]["name"] or "Kole" in tw["user"]["name"] or "Enoch" in tw["user"]["name"] or "Graysen" in tw["user"]["name"] or "Kye" in tw["user"]["name"] or "Vicente" in tw["user"]["name"] or "Fisher" in tw["user"]["name"] or "Ray" in tw["user"]["name"] or "Fox" in tw["user"]["name"] or "Jamie" in tw["user"]["name"] or "Rey" in tw["user"]["name"] or "Zaid" in tw["user"]["name"] or "Allan" in tw["user"]["name"] or "Emery" in tw["user"]["name"] or "Gannon" in tw["user"]["name"] or "Joziah" in tw["user"]["name"] or "Rodney" in tw["user"]["name"] or "Juelz" in tw["user"]["name"] or "Sonny" in tw["user"]["name"] or "Terrance" in tw["user"]["name"] or "Zyaire" in tw["user"]["name"] or "Augustine" in tw["user"]["name"] or "Cory" in tw["user"]["name"] or "Felipe" in tw["user"]["name"] or "Aron" in tw["user"]["name"] or "Jacoby" in tw["user"]["name"] or "Harlan" in tw["user"]["name"] or "Marc" in tw["user"]["name"] or "Bobby" in tw["user"]["name"] or "Joey" in tw["user"]["name"] or "Anson" in tw["user"]["name"] or "Huxley" in tw["user"]["name"] or "Marlon" in tw["user"]["name"] or "Anders" in tw["user"]["name"] or "Guillermo" in tw["user"]["name"] or "Payton" in tw["user"]["name"] or "Castiel" in tw["user"]["name"] or "Damari" in tw["user"]["name"] or "Shepherd" in tw["user"]["name"] or "Azariah" in tw["user"]["name"] or "Harold" in tw["user"]["name"] or "Harper" in tw["user"]["name"] or "Henrik" in tw["user"]["name"] or "Houston" in tw["user"]["name"] or "Kairo" in tw["user"]["name"] or "Willie" in tw["user"]["name"] or "Elisha" in tw["user"]["name"] or "Ameer" in tw["user"]["name"] or "Emory" in tw["user"]["name"] or "Skylar" in tw["user"]["name"] or "Sutton" in tw["user"]["name"] or "Alfonso" in tw["user"]["name"] or "Brentley" in tw["user"]["name"] or "Toby" in tw["user"]["name"] or "Blaze" in tw["user"]["name"] or "Eugene" in tw["user"]["name"] or "Shiloh" in tw["user"]["name"] or "Wayne" in tw["user"]["name"] or "Darian" in tw["user"]["name"] or "Gordon" in tw["user"]["name"] or "London" in tw["user"]["name"] or "Bodie" in tw["user"]["name"] or "Jordy" in tw["user"]["name"] or "Jermaine" in tw["user"]["name"] or "Denver" in tw["user"]["name"] or "Gerald" in tw["user"]["name"] or "Merrick" in tw["user"]["name"] or "Musa" in tw["user"]["name"] or "Vincenzo" in tw["user"]["name"] or "Kody" in tw["user"]["name"] or "Yahir" in tw["user"]["name"] or "Brodie" in tw["user"]["name"] or "Trace" in tw["user"]["name"] or "Darwin" in tw["user"]["name"] or "Tadeo" in tw["user"]["name"] or "Bentlee" in tw["user"]["name"] or "Billy" in tw["user"]["name"] or "Hugh" in tw["user"]["name"] or "Reginald" in tw["user"]["name"] or "Vance" in tw["user"]["name"] or "Westin" in tw["user"]["name"] or "Cain" in tw["user"]["name"] or "Arian" in tw["user"]["name"] or "Dayton" in tw["user"]["name"] or "Javion" in tw["user"]["name"] or "Terrence" in tw["user"]["name"] or "Brysen" in tw["user"]["name"] or "Jaxxon" in tw["user"]["name"] or "Thatcher" in tw["user"]["name"] or "Landry" in tw["user"]["name"] or "Rene" in tw["user"]["name"] or "Westley" in tw["user"]["name"] or "Miller" in tw["user"]["name"] or "Alvaro" in tw["user"]["name"] or "Cristiano" in tw["user"]["name"] or "Eliseo" in tw["user"]["name"] or "Ephraim" in tw["user"]["name"] or "Adrien" in tw["user"]["name"] or "Jerome" in tw["user"]["name"] or "Khalid" in tw["user"]["name"] or "Aydin" in tw["user"]["name"] or "Mayson" in tw["user"]["name"] or "Alfred" in tw["user"]["name"] or "Duncan" in tw["user"]["name"] or "Junior" in tw["user"]["name"] or "Kendall" in tw["user"]["name"] or "Zavier" in tw["user"]["name"] or "Koda" in tw["user"]["name"] or "Maison" in tw["user"]["name"] or "Caspian" in tw["user"]["name"] or "Maxim" in tw["user"]["name"] or "Kace" in tw["user"]["name"] or "Zackary" in tw["user"]["name"] or "Rudy" in tw["user"]["name"] or "Coleman" in tw["user"]["name"] or "Keagan" in tw["user"]["name"] or "Kolten" in tw["user"]["name"] or "Maximo" in tw["user"]["name"] or "Dario" in tw["user"]["name"] or "Davion" in tw["user"]["name"] or "Kalel" in tw["user"]["name"] or "Briar" in tw["user"]["name"] or "Jairo" in tw["user"]["name"] or "Misael" in tw["user"]["name"] or "Rogelio" in tw["user"]["name"] or "Terrell" in tw["user"]["name"] or "Heath" in tw["user"]["name"] or "Micheal" in tw["user"]["name"] or "Wesson" in tw["user"]["name"] or "Aaden" in tw["user"]["name"] or "Brixton" in tw["user"]["name"] or "Draven" in tw["user"]["name"] or "Xzavier" in tw["user"]["name"] or "Darrell" in tw["user"]["name"] or "Keanu" in tw["user"]["name"] or "Ronnie" in tw["user"]["name"] or "Konnor" in tw["user"]["name"] or "Will" in tw["user"]["name"] or "Dangelo" in tw["user"]["name"] or "Frankie" in tw["user"]["name"] or "Kamryn" in tw["user"]["name"] or "Salvatore" in tw["user"]["name"] or "Santana" in tw["user"]["name"] or "Shaun" in tw["user"]["name"] or "Coen" in tw["user"]["name"] or "Leighton" in tw["user"]["name"] or "Mustafa" in tw["user"]["name"] or "Reuben" in tw["user"]["name"] or "Ayan" in tw["user"]["name"] or "Blaise" in tw["user"]["name"] or "Dimitri" in tw["user"]["name"] or "Keenan" in tw["user"]["name"] or "Van" in tw["user"]["name"] or "Achilles" in tw["user"]["name"] or "Channing" in tw["user"]["name"] or "Ishaan" in tw["user"]["name"] or "Wells" in tw["user"]["name"] or "Benton" in tw["user"]["name"] or "Lamar" in tw["user"]["name"] or "Nova" in tw["user"]["name"] or "Yahya" in tw["user"]["name"] or "Dilan" in tw["user"]["name"] or "Gibson" in tw["user"]["name"] or "Camdyn" in tw["user"]["name"] or "Ulises" in tw["user"]["name"] or "Alexzander" in tw["user"]["name"] or "Valentin" in tw["user"]["name"] or "Shepard" in tw["user"]["name"] or "Alistair" in tw["user"]["name"] or "Eason" in tw["user"]["name"] or "Kaiser" in tw["user"]["name"] or "Leroy" in tw["user"]["name"] or "Zayd" in tw["user"]["name"] or "Camilo" in tw["user"]["name"] or "Markus" in tw["user"]["name"] or "Foster" in tw["user"]["name"] or "Davian" in tw["user"]["name"] or "Dwayne" in tw["user"]["name"] or "Jabari" in tw["user"]["name"] or "Judson" in tw["user"]["name"] or "Koa" in tw["user"]["name"] or "Yehuda" in tw["user"]["name"] or "Lyric" in tw["user"]["name"] or "Tristian" in tw["user"]["name"] or "Agustin" in tw["user"]["name"] or "Bridger" in tw["user"]["name"] or "Vivaan" in tw["user"]["name"] or "Brayson" in tw["user"]["name"] or "Emmet" in tw["user"]["name"] or "Marley" in tw["user"]["name"] or "Mike" in tw["user"]["name"] or "Nickolas" in tw["user"]["name"] or "Kenny" in tw["user"]["name"] or "Leif" in tw["user"]["name"] or "Bjorn" in tw["user"]["name"] or "Ignacio" in tw["user"]["name"] or "Rocky" in tw["user"]["name"] or "Chad" in tw["user"]["name"] or "Gatlin" in tw["user"]["name"] or "Greysen" in tw["user"]["name"] or "Kyng" in tw["user"]["name"] or "Randall" in tw["user"]["name"] or "Reign" in tw["user"]["name"] or "Vaughn" in tw["user"]["name"] or "Jessie" in tw["user"]["name"] or "Louie" in tw["user"]["name"] or "Shmuel" in tw["user"]["name"] or "Zahir" in tw["user"]["name"] or "Ernest" in tw["user"]["name"] or "Javon" in tw["user"]["name"] or "Khari" in tw["user"]["name"] or "Reagan" in tw["user"]["name"] or "Avi" in tw["user"]["name"] or "Ira" in tw["user"]["name"] or "Ledger" in tw["user"]["name"] or "Simeon" in tw["user"]["name"] or "Yadiel" in tw["user"]["name"] or "Maddux" in tw["user"]["name"] or "Seamus" in tw["user"]["name"] or "Jad" in tw["user"]["name"] or "Jeremias" in tw["user"]["name"] or "Kylen" in tw["user"]["name"] or "Rashad" in tw["user"]["name"] or "Santos" in tw["user"]["name"] or "Cedric" in tw["user"]["name"] or "Craig" in tw["user"]["name"] or "Dominique" in tw["user"]["name"] or "Gianluca" in tw["user"]["name"] or "Jovanni" in tw["user"]["name"] or "Bishop" in tw["user"]["name"] or "Brenden" in tw["user"]["name"] or "Anton" in tw["user"]["name"] or "Camron" in tw["user"]["name"] or "Giancarlo" in tw["user"]["name"] or "Lyle" in tw["user"]["name"] or "Alaric" in tw["user"]["name"] or "Decker" in tw["user"]["name"] or "Eliezer" in tw["user"]["name"] or "Ramiro" in tw["user"]["name"] or "Yisroel" in tw["user"]["name"] or "Howard" in tw["user"]["name"] or "Jaxx" in tw["user"]["name"]):
		lat.append(tw["user"]["id"])
	elif("Emma" in tw["user"]["name"] or "Olivia" in tw["user"]["name"] or "Ava" in tw["user"]["name"] or "Isabella" in tw["user"]["name"] or "Sophia" in tw["user"]["name"] or "Charlotte" in tw["user"]["name"] or "Mia" in tw["user"]["name"] or "Amelia" in tw["user"]["name"] or "Harper" in tw["user"]["name"] or "Evelyn" in tw["user"]["name"] or "Abigail" in tw["user"]["name"] or "Emily" in tw["user"]["name"] or "Elizabeth" in tw["user"]["name"] or "Mila" in tw["user"]["name"] or "Ella" in tw["user"]["name"] or "Avery" in tw["user"]["name"] or "Sofia" in tw["user"]["name"] or "Camila" in tw["user"]["name"] or "Aria" in tw["user"]["name"] or "Scarlett" in tw["user"]["name"] or "Victoria" in tw["user"]["name"] or "Madison" in tw["user"]["name"] or "Luna" in tw["user"]["name"] or "Grace" in tw["user"]["name"] or "Chloe" in tw["user"]["name"] or "Penelope" in tw["user"]["name"] or "Layla" in tw["user"]["name"] or "Riley" in tw["user"]["name"] or "Zoey" in tw["user"]["name"] or "Nora" in tw["user"]["name"] or "Lily" in tw["user"]["name"] or "Eleanor" in tw["user"]["name"] or "Hannah" in tw["user"]["name"] or "Lillian" in tw["user"]["name"] or "Addison" in tw["user"]["name"] or "Aubrey" in tw["user"]["name"] or "Ellie" in tw["user"]["name"] or "Stella" in tw["user"]["name"] or "Natalie" in tw["user"]["name"] or "Zoe" in tw["user"]["name"] or "Leah" in tw["user"]["name"] or "Hazel" in tw["user"]["name"] or "Violet" in tw["user"]["name"] or "Aurora" in tw["user"]["name"] or "Savannah" in tw["user"]["name"] or "Audrey" in tw["user"]["name"] or "Brooklyn" in tw["user"]["name"] or "Bella" in tw["user"]["name"] or "Claire" in tw["user"]["name"] or "Skylar" in tw["user"]["name"] or "Lucy" in tw["user"]["name"] or "Paisley" in tw["user"]["name"] or "Everly" in tw["user"]["name"] or "Anna" in tw["user"]["name"] or "Caroline" in tw["user"]["name"] or "Nova" in tw["user"]["name"] or "Genesis" in tw["user"]["name"] or "Emilia" in tw["user"]["name"] or "Kennedy" in tw["user"]["name"] or "Samantha" in tw["user"]["name"] or "Maya" in tw["user"]["name"] or "Willow" in tw["user"]["name"] or "Kinsley" in tw["user"]["name"] or "Naomi" in tw["user"]["name"] or "Aaliyah" in tw["user"]["name"] or "Elena" in tw["user"]["name"] or "Sarah" in tw["user"]["name"] or "Ariana" in tw["user"]["name"] or "Allison" in tw["user"]["name"] or "Gabriella" in tw["user"]["name"] or "Alice" in tw["user"]["name"] or "Madelyn" in tw["user"]["name"] or "Cora" in tw["user"]["name"] or "Ruby" in tw["user"]["name"] or "Eva" in tw["user"]["name"] or "Serenity" in tw["user"]["name"] or "Autumn" in tw["user"]["name"] or "Adeline" in tw["user"]["name"] or "Hailey" in tw["user"]["name"] or "Gianna" in tw["user"]["name"] or "Valentina" in tw["user"]["name"] or "Isla" in tw["user"]["name"] or "Eliana" in tw["user"]["name"] or "Quinn" in tw["user"]["name"] or "Nevaeh" in tw["user"]["name"] or "Ivy" in tw["user"]["name"] or "Sadie" in tw["user"]["name"] or "Piper" in tw["user"]["name"] or "Lydia" in tw["user"]["name"] or "Alexa" in tw["user"]["name"] or "Josephine" in tw["user"]["name"] or "Emery" in tw["user"]["name"] or "Julia" in tw["user"]["name"] or "Delilah" in tw["user"]["name"] or "Arianna" in tw["user"]["name"] or "Vivian" in tw["user"]["name"] or "Kaylee" in tw["user"]["name"] or "Sophie" in tw["user"]["name"] or "Brielle" in tw["user"]["name"] or "Madeline" in tw["user"]["name"] or "Peyton" in tw["user"]["name"] or "Rylee" in tw["user"]["name"] or "Clara" in tw["user"]["name"] or "Hadley" in tw["user"]["name"] or "Melanie" in tw["user"]["name"] or "Mackenzie" in tw["user"]["name"] or "Reagan" in tw["user"]["name"] or "Adalynn" in tw["user"]["name"] or "Liliana" in tw["user"]["name"] or "Aubree" in tw["user"]["name"] or "Jade" in tw["user"]["name"] or "Katherine" in tw["user"]["name"] or "Isabelle" in tw["user"]["name"] or "Natalia" in tw["user"]["name"] or "Raelynn" in tw["user"]["name"] or "Maria" in tw["user"]["name"] or "Athena" in tw["user"]["name"] or "Ximena" in tw["user"]["name"] or "Arya" in tw["user"]["name"] or "Leilani" in tw["user"]["name"] or "Taylor" in tw["user"]["name"] or "Faith" in tw["user"]["name"] or "Rose" in tw["user"]["name"] or "Kylie" in tw["user"]["name"] or "Alexandra" in tw["user"]["name"] or "Mary" in tw["user"]["name"] or "Margaret" in tw["user"]["name"] or "Lyla" in tw["user"]["name"] or "Ashley" in tw["user"]["name"] or "Amaya" in tw["user"]["name"] or "Eliza" in tw["user"]["name"] or "Brianna" in tw["user"]["name"] or "Bailey" in tw["user"]["name"] or "Andrea" in tw["user"]["name"] or "Khloe" in tw["user"]["name"] or "Jasmine" in tw["user"]["name"] or "Melody" in tw["user"]["name"] or "Iris" in tw["user"]["name"] or "Isabel" in tw["user"]["name"] or "Norah" in tw["user"]["name"] or "Annabelle" in tw["user"]["name"] or "Valeria" in tw["user"]["name"] or "Emerson" in tw["user"]["name"] or "Adalyn" in tw["user"]["name"] or "Ryleigh" in tw["user"]["name"] or "Eden" in tw["user"]["name"] or "Emersyn" in tw["user"]["name"] or "Anastasia" in tw["user"]["name"] or "Kayla" in tw["user"]["name"] or "Alyssa" in tw["user"]["name"] or "Juliana" in tw["user"]["name"] or "Charlie" in tw["user"]["name"] or "Esther" in tw["user"]["name"] or "Ariel" in tw["user"]["name"] or "Cecilia" in tw["user"]["name"] or "Valerie" in tw["user"]["name"] or "Alina" in tw["user"]["name"] or "Molly" in tw["user"]["name"] or "Reese" in tw["user"]["name"] or "Aliyah" in tw["user"]["name"] or "Lilly" in tw["user"]["name"] or "Parker" in tw["user"]["name"] or "Finley" in tw["user"]["name"] or "Morgan" in tw["user"]["name"] or "Sydney" in tw["user"]["name"] or "Jordyn" in tw["user"]["name"] or "Eloise" in tw["user"]["name"] or "Trinity" in tw["user"]["name"] or "Daisy" in tw["user"]["name"] or "Kimberly" in tw["user"]["name"] or "Lauren" in tw["user"]["name"] or "Genevieve" in tw["user"]["name"] or "Sara" in tw["user"]["name"] or "Arabella" in tw["user"]["name"] or "Harmony" in tw["user"]["name"] or "Elise" in tw["user"]["name"] or "Remi" in tw["user"]["name"] or "Teagan" in tw["user"]["name"] or "Alexis" in tw["user"]["name"] or "London" in tw["user"]["name"] or "Sloane" in tw["user"]["name"] or "Laila" in tw["user"]["name"] or "Lucia" in tw["user"]["name"] or "Diana" in tw["user"]["name"] or "Juliette" in tw["user"]["name"] or "Sienna" in tw["user"]["name"] or "Elliana" in tw["user"]["name"] or "Londyn" in tw["user"]["name"] or "Ayla" in tw["user"]["name"] or "Callie" in tw["user"]["name"] or "Gracie" in tw["user"]["name"] or "Josie" in tw["user"]["name"] or "Amara" in tw["user"]["name"] or "Jocelyn" in tw["user"]["name"] or "Daniela" in tw["user"]["name"] or "Everleigh" in tw["user"]["name"] or "Mya" in tw["user"]["name"] or "Rachel" in tw["user"]["name"] or "Summer" in tw["user"]["name"] or "Alana" in tw["user"]["name"] or "Brooke" in tw["user"]["name"] or "Alaina" in tw["user"]["name"] or "Mckenzie" in tw["user"]["name"] or "Catherine" in tw["user"]["name"] or "Amy" in tw["user"]["name"] or "Presley" in tw["user"]["name"] or "Journee" in tw["user"]["name"] or "Rosalie" in tw["user"]["name"] or "Ember" in tw["user"]["name"] or "Brynlee" in tw["user"]["name"] or "Rowan" in tw["user"]["name"] or "Joanna" in tw["user"]["name"] or "Paige" in tw["user"]["name"] or "Rebecca" in tw["user"]["name"] or "Ana" in tw["user"]["name"] or "Sawyer" in tw["user"]["name"] or "Mariah" in tw["user"]["name"] or "Nicole" in tw["user"]["name"] or "Brooklynn" in tw["user"]["name"] or "Payton" in tw["user"]["name"] or "Marley" in tw["user"]["name"] or "Fiona" in tw["user"]["name"] or "Georgia" in tw["user"]["name"] or "Lila" in tw["user"]["name"] or "Harley" in tw["user"]["name"] or "Adelyn" in tw["user"]["name"] or "Alivia" in tw["user"]["name"] or "Noelle" in tw["user"]["name"] or "Gemma" in tw["user"]["name"] or "Vanessa" in tw["user"]["name"] or "Journey" in tw["user"]["name"] or "Makayla" in tw["user"]["name"] or "Angelina" in tw["user"]["name"] or "Adaline" in tw["user"]["name"] or "Catalina" in tw["user"]["name"] or "Alayna" in tw["user"]["name"] or "Julianna" in tw["user"]["name"] or "Leila" in tw["user"]["name"] or "Lola" in tw["user"]["name"] or "Adriana" in tw["user"]["name"] or "June" in tw["user"]["name"] or "Juliet" in tw["user"]["name"] or "Jayla" in tw["user"]["name"] or "River" in tw["user"]["name"] or "Tessa" in tw["user"]["name"] or "Lia" in tw["user"]["name"] or "Dakota" in tw["user"]["name"] or "Delaney" in tw["user"]["name"] or "Selena" in tw["user"]["name"] or "Blakely" in tw["user"]["name"] or "Ada" in tw["user"]["name"] or "Camille" in tw["user"]["name"] or "Zara" in tw["user"]["name"] or "Malia" in tw["user"]["name"] or "Hope" in tw["user"]["name"] or "Samara" in tw["user"]["name"] or "Vera" in tw["user"]["name"] or "Mckenna" in tw["user"]["name"] or "Briella" in tw["user"]["name"] or "Izabella" in tw["user"]["name"] or "Hayden" in tw["user"]["name"] or "Raegan" in tw["user"]["name"] or "Michelle" in tw["user"]["name"] or "Angela" in tw["user"]["name"] or "Ruth" in tw["user"]["name"] or "Freya" in tw["user"]["name"] or "Kamila" in tw["user"]["name"] or "Vivienne" in tw["user"]["name"] or "Aspen" in tw["user"]["name"] or "Olive" in tw["user"]["name"] or "Kendall" in tw["user"]["name"] or "Elaina" in tw["user"]["name"] or "Thea" in tw["user"]["name"] or "Kali" in tw["user"]["name"] or "Destiny" in tw["user"]["name"] or "Amiyah" in tw["user"]["name"] or "Evangeline" in tw["user"]["name"] or "Cali" in tw["user"]["name"] or "Blake" in tw["user"]["name"] or "Elsie" in tw["user"]["name"] or "Juniper" in tw["user"]["name"] or "Alexandria" in tw["user"]["name"] or "Myla" in tw["user"]["name"] or "Ariella" in tw["user"]["name"] or "Kate" in tw["user"]["name"] or "Mariana" in tw["user"]["name"] or "Lilah" in tw["user"]["name"] or "Charlee" in tw["user"]["name"] or "Daleyza" in tw["user"]["name"] or "Nyla" in tw["user"]["name"] or "Jane" in tw["user"]["name"] or "Maggie" in tw["user"]["name"] or "Zuri" in tw["user"]["name"] or "Aniyah" in tw["user"]["name"] or "Lucille" in tw["user"]["name"] or "Leia" in tw["user"]["name"] or "Melissa" in tw["user"]["name"] or "Adelaide" in tw["user"]["name"] or "Amina" in tw["user"]["name"] or "Giselle" in tw["user"]["name"] or "Lena" in tw["user"]["name"] or "Camilla" in tw["user"]["name"] or "Miriam" in tw["user"]["name"] or "Millie" in tw["user"]["name"] or "Brynn" in tw["user"]["name"] or "Gabrielle" in tw["user"]["name"] or "Sage" in tw["user"]["name"] or "Annie" in tw["user"]["name"] or "Logan" in tw["user"]["name"] or "Lilliana" in tw["user"]["name"] or "Haven" in tw["user"]["name"] or "Jessica" in tw["user"]["name"] or "Kaia" in tw["user"]["name"] or "Magnolia" in tw["user"]["name"] or "Amira" in tw["user"]["name"] or "Adelynn" in tw["user"]["name"] or "Makenzie" in tw["user"]["name"] or "Stephanie" in tw["user"]["name"] or "Nina" in tw["user"]["name"] or "Phoebe" in tw["user"]["name"] or "Arielle" in tw["user"]["name"] or "Evie" in tw["user"]["name"] or "Lyric" in tw["user"]["name"] or "Alessandra" in tw["user"]["name"] or "Gabriela" in tw["user"]["name"] or "Paislee" in tw["user"]["name"] or "Raelyn" in tw["user"]["name"] or "Madilyn" in tw["user"]["name"] or "Paris" in tw["user"]["name"] or "Makenna" in tw["user"]["name"] or "Kinley" in tw["user"]["name"] or "Gracelyn" in tw["user"]["name"] or "Talia" in tw["user"]["name"] or "Maeve" in tw["user"]["name"] or "Rylie" in tw["user"]["name"] or "Kiara" in tw["user"]["name"] or "Evelynn" in tw["user"]["name"] or "Brinley" in tw["user"]["name"] or "Jacqueline" in tw["user"]["name"] or "Laura" in tw["user"]["name"] or "Gracelynn" in tw["user"]["name"] or "Lexi" in tw["user"]["name"] or "Ariah" in tw["user"]["name"] or "Fatima" in tw["user"]["name"] or "Jennifer" in tw["user"]["name"] or "Kehlani" in tw["user"]["name"] or "Alani" in tw["user"]["name"] or "Ariyah" in tw["user"]["name"] or "Luciana" in tw["user"]["name"] or "Allie" in tw["user"]["name"] or "Heidi" in tw["user"]["name"] or "Maci" in tw["user"]["name"] or "Phoenix" in tw["user"]["name"] or "Felicity" in tw["user"]["name"] or "Joy" in tw["user"]["name"] or "Kenzie" in tw["user"]["name"] or "Veronica" in tw["user"]["name"] or "Margot" in tw["user"]["name"] or "Addilyn" in tw["user"]["name"] or "Lana" in tw["user"]["name"] or "Cassidy" in tw["user"]["name"] or "Remington" in tw["user"]["name"] or "Saylor" in tw["user"]["name"] or "Ryan" in tw["user"]["name"] or "Keira" in tw["user"]["name"] or "Harlow" in tw["user"]["name"] or "Miranda" in tw["user"]["name"] or "Angel" in tw["user"]["name"] or "Amanda" in tw["user"]["name"] or "Daniella" in tw["user"]["name"] or "Royalty" in tw["user"]["name"] or "Gwendolyn" in tw["user"]["name"] or "Ophelia" in tw["user"]["name"] or "Heaven" in tw["user"]["name"] or "Jordan" in tw["user"]["name"] or "Madeleine" in tw["user"]["name"] or "Esmeralda" in tw["user"]["name"] or "Kira" in tw["user"]["name"] or "Miracle" in tw["user"]["name"] or "Elle" in tw["user"]["name"] or "Amari" in tw["user"]["name"] or "Danielle" in tw["user"]["name"] or "Daphne" in tw["user"]["name"] or "Willa" in tw["user"]["name"] or "Haley" in tw["user"]["name"] or "Gia" in tw["user"]["name"] or "Kaitlyn" in tw["user"]["name"] or "Oakley" in tw["user"]["name"] or "Kailani" in tw["user"]["name"] or "Winter" in tw["user"]["name"] or "Alicia" in tw["user"]["name"] or "Serena" in tw["user"]["name"] or "Nadia" in tw["user"]["name"] or "Aviana" in tw["user"]["name"] or "Demi" in tw["user"]["name"] or "Jada" in tw["user"]["name"] or "Braelynn" in tw["user"]["name"] or "Dylan" in tw["user"]["name"] or "Ainsley" in tw["user"]["name"] or "Alison" in tw["user"]["name"] or "Camryn" in tw["user"]["name"] or "Avianna" in tw["user"]["name"] or "Bianca" in tw["user"]["name"] or "Skyler" in tw["user"]["name"] or "Scarlet" in tw["user"]["name"] or "Maddison" in tw["user"]["name"] or "Nylah" in tw["user"]["name"] or "Sarai" in tw["user"]["name"] or "Regina" in tw["user"]["name"] or "Dahlia" in tw["user"]["name"] or "Nayeli" in tw["user"]["name"] or "Raven" in tw["user"]["name"] or "Helen" in tw["user"]["name"] or "Adrianna" in tw["user"]["name"] or "Averie" in tw["user"]["name"] or "Skye" in tw["user"]["name"] or "Kelsey" in tw["user"]["name"] or "Tatum" in tw["user"]["name"] or "Kensley" in tw["user"]["name"] or "Maliyah" in tw["user"]["name"] or "Erin" in tw["user"]["name"] or "Viviana" in tw["user"]["name"] or "Jenna" in tw["user"]["name"] or "Anaya" in tw["user"]["name"] or "Carolina" in tw["user"]["name"] or "Shelby" in tw["user"]["name"] or "Sabrina" in tw["user"]["name"] or "Mikayla" in tw["user"]["name"] or "Annalise" in tw["user"]["name"] or "Octavia" in tw["user"]["name"] or "Lennon" in tw["user"]["name"] or "Blair" in tw["user"]["name"] or "Carmen" in tw["user"]["name"] or "Yaretzi" in tw["user"]["name"] or "Kennedi" in tw["user"]["name"] or "Mabel" in tw["user"]["name"] or "Zariah" in tw["user"]["name"] or "Kyla" in tw["user"]["name"] or "Christina" in tw["user"]["name"] or "Selah" in tw["user"]["name"] or "Celeste" in tw["user"]["name"] or "Eve" in tw["user"]["name"] or "Mckinley" in tw["user"]["name"] or "Milani" in tw["user"]["name"] or "Frances" in tw["user"]["name"] or "Jimena" in tw["user"]["name"] or "Kylee" in tw["user"]["name"] or "Leighton" in tw["user"]["name"] or "Katie" in tw["user"]["name"] or "Aitana" in tw["user"]["name"] or "Kayleigh" in tw["user"]["name"] or "Sierra" in tw["user"]["name"] or "Kathryn" in tw["user"]["name"] or "Rosemary" in tw["user"]["name"] or "Jolene" in tw["user"]["name"] or "Alondra" in tw["user"]["name"] or "Elisa" in tw["user"]["name"] or "Helena" in tw["user"]["name"] or "Charleigh" in tw["user"]["name"] or "Hallie" in tw["user"]["name"] or "Lainey" in tw["user"]["name"] or "Avah" in tw["user"]["name"] or "Jazlyn" in tw["user"]["name"] or "Kamryn" in tw["user"]["name"] or "Mira" in tw["user"]["name"] or "Cheyenne" in tw["user"]["name"] or "Francesca" in tw["user"]["name"] or "Antonella" in tw["user"]["name"] or "Wren" in tw["user"]["name"] or "Chelsea" in tw["user"]["name"] or "Amber" in tw["user"]["name"] or "Emory" in tw["user"]["name"] or "Lorelei" in tw["user"]["name"] or "Nia" in tw["user"]["name"] or "Abby" in tw["user"]["name"] or "April" in tw["user"]["name"] or "Emelia" in tw["user"]["name"] or "Carter" in tw["user"]["name"] or "Aylin" in tw["user"]["name"] or "Cataleya" in tw["user"]["name"] or "Bethany" in tw["user"]["name"] or "Marlee" in tw["user"]["name"] or "Carly" in tw["user"]["name"] or "Kaylani" in tw["user"]["name"] or "Emely" in tw["user"]["name"] or "Liana" in tw["user"]["name"] or "Madelynn" in tw["user"]["name"] or "Cadence" in tw["user"]["name"] or "Matilda" in tw["user"]["name"] or "Sylvia" in tw["user"]["name"] or "Myra" in tw["user"]["name"] or "Fernanda" in tw["user"]["name"] or "Oaklyn" in tw["user"]["name"] or "Elianna" in tw["user"]["name"] or "Hattie" in tw["user"]["name"] or "Dayana" in tw["user"]["name"] or "Kendra" in tw["user"]["name"] or "Maisie" in tw["user"]["name"] or "Malaysia" in tw["user"]["name"] or "Kara" in tw["user"]["name"] or "Katelyn" in tw["user"]["name"] or "Maia" in tw["user"]["name"] or "Celine" in tw["user"]["name"] or "Cameron" in tw["user"]["name"] or "Renata" in tw["user"]["name"] or "Jayleen" in tw["user"]["name"] or "Charli" in tw["user"]["name"] or "Emmalyn" in tw["user"]["name"] or "Holly" in tw["user"]["name"] or "Azalea" in tw["user"]["name"] or "Leona" in tw["user"]["name"] or "Alejandra" in tw["user"]["name"] or "Bristol" in tw["user"]["name"] or "Collins" in tw["user"]["name"] or "Imani" in tw["user"]["name"] or "Meadow" in tw["user"]["name"] or "Alexia" in tw["user"]["name"] or "Edith" in tw["user"]["name"] or "Kaydence" in tw["user"]["name"] or "Leslie" in tw["user"]["name"] or "Lilith" in tw["user"]["name"] or "Kora" in tw["user"]["name"] or "Aisha" in tw["user"]["name"] or "Meredith" in tw["user"]["name"] or "Danna" in tw["user"]["name"] or "Wynter" in tw["user"]["name"] or "Emberly" in tw["user"]["name"] or "Julieta" in tw["user"]["name"] or "Michaela" in tw["user"]["name"] or "Alayah" in tw["user"]["name"] or "Jemma" in tw["user"]["name"] or "Reign" in tw["user"]["name"] or "Colette" in tw["user"]["name"] or "Kaliyah" in tw["user"]["name"] or "Elliott" in tw["user"]["name"] or "Johanna" in tw["user"]["name"] or "Remy" in tw["user"]["name"] or "Sutton" in tw["user"]["name"] or "Emmy" in tw["user"]["name"] or "Virginia" in tw["user"]["name"] or "Briana" in tw["user"]["name"] or "Oaklynn" in tw["user"]["name"] or "Adelina" in tw["user"]["name"] or "Everlee" in tw["user"]["name"] or "Megan" in tw["user"]["name"] or "Angelica" in tw["user"]["name"] or "Justice" in tw["user"]["name"] or "Mariam" in tw["user"]["name"] or "Khaleesi" in tw["user"]["name"] or "Macie" in tw["user"]["name"] or "Karsyn" in tw["user"]["name"] or "Alanna" in tw["user"]["name"] or "Aleah" in tw["user"]["name"] or "Mae" in tw["user"]["name"] or "Mallory" in tw["user"]["name"] or "Esme" in tw["user"]["name"] or "Skyla" in tw["user"]["name"] or "Madilynn" in tw["user"]["name"] or "Charley" in tw["user"]["name"] or "Allyson" in tw["user"]["name"] or "Hanna" in tw["user"]["name"] or "Shiloh" in tw["user"]["name"] or "Henley" in tw["user"]["name"] or "Macy" in tw["user"]["name"] or "Maryam" in tw["user"]["name"] or "Ivanna" in tw["user"]["name"] or "Ashlynn" in tw["user"]["name"] or "Lorelai" in tw["user"]["name"] or "Amora" in tw["user"]["name"] or "Ashlyn" in tw["user"]["name"] or "Sasha" in tw["user"]["name"] or "Baylee" in tw["user"]["name"] or "Beatrice" in tw["user"]["name"] or "Itzel" in tw["user"]["name"] or "Priscilla" in tw["user"]["name"] or "Marie" in tw["user"]["name"] or "Jayda" in tw["user"]["name"] or "Liberty" in tw["user"]["name"] or "Rory" in tw["user"]["name"] or "Alessia" in tw["user"]["name"] or "Alaia" in tw["user"]["name"] or "Janelle" in tw["user"]["name"] or "Kalani" in tw["user"]["name"] or "Gloria" in tw["user"]["name"] or "Sloan" in tw["user"]["name"] or "Dorothy" in tw["user"]["name"] or "Greta" in tw["user"]["name"] or "Julie" in tw["user"]["name"] or "Zahra" in tw["user"]["name"] or "Savanna" in tw["user"]["name"] or "Annabella" in tw["user"]["name"] or "Poppy" in tw["user"]["name"] or "Amalia" in tw["user"]["name"] or "Zaylee" in tw["user"]["name"] or "Cecelia" in tw["user"]["name"] or "Coraline" in tw["user"]["name"] or "Kimber" in tw["user"]["name"] or "Emmie" in tw["user"]["name"] or "Anne" in tw["user"]["name"] or "Karina" in tw["user"]["name"] or "Kassidy" in tw["user"]["name"] or "Kynlee" in tw["user"]["name"] or "Monroe" in tw["user"]["name"] or "Anahi" in tw["user"]["name"] or "Jaliyah" in tw["user"]["name"] or "Jazmin" in tw["user"]["name"] or "Maren" in tw["user"]["name"] or "Monica" in tw["user"]["name"] or "Siena" in tw["user"]["name"] or "Marilyn" in tw["user"]["name"] or "Reyna" in tw["user"]["name"] or "Kyra" in tw["user"]["name"] or "Lilian" in tw["user"]["name"] or "Jamie" in tw["user"]["name"] or "Melany" in tw["user"]["name"] or "Alaya" in tw["user"]["name"] or "Ariya" in tw["user"]["name"] or "Kelly" in tw["user"]["name"] or "Rosie" in tw["user"]["name"] or "Adley" in tw["user"]["name"] or "Dream" in tw["user"]["name"] or "Jaylah" in tw["user"]["name"] or "Laurel" in tw["user"]["name"] or "Jazmine" in tw["user"]["name"] or "Mina" in tw["user"]["name"] or "Karla" in tw["user"]["name"] or "Bailee" in tw["user"]["name"] or "Aubrie" in tw["user"]["name"] or "Katalina" in tw["user"]["name"] or "Melina" in tw["user"]["name"] or "Harlee" in tw["user"]["name"] or "Elliot" in tw["user"]["name"] or "Hayley" in tw["user"]["name"] or "Elaine" in tw["user"]["name"] or "Karen" in tw["user"]["name"] or "Dallas" in tw["user"]["name"] or "Irene" in tw["user"]["name"] or "Lylah" in tw["user"]["name"] or "Ivory" in tw["user"]["name"] or "Chaya" in tw["user"]["name"] or "Rosa" in tw["user"]["name"] or "Aleena" in tw["user"]["name"] or "Braelyn" in tw["user"]["name"] or "Nola" in tw["user"]["name"] or "Alma" in tw["user"]["name"] or "Leyla" in tw["user"]["name"] or "Pearl" in tw["user"]["name"] or "Addyson" in tw["user"]["name"] or "Roselyn" in tw["user"]["name"] or "Lacey" in tw["user"]["name"] or "Lennox" in tw["user"]["name"] or "Reina" in tw["user"]["name"] or "Aurelia" in tw["user"]["name"] or "Noa" in tw["user"]["name"] or "Janiyah" in tw["user"]["name"] or "Jessie" in tw["user"]["name"] or "Madisyn" in tw["user"]["name"] or "Saige" in tw["user"]["name"] or "Alia" in tw["user"]["name"] or "Tiana" in tw["user"]["name"] or "Astrid" in tw["user"]["name"] or "Cassandra" in tw["user"]["name"] or "Kyleigh" in tw["user"]["name"] or "Romina" in tw["user"]["name"] or "Stevie" in tw["user"]["name"] or "Haylee" in tw["user"]["name"] or "Zelda" in tw["user"]["name"] or "Lillie" in tw["user"]["name"] or "Aileen" in tw["user"]["name"] or "Brylee" in tw["user"]["name"] or "Eileen" in tw["user"]["name"] or "Yara" in tw["user"]["name"] or "Ensley" in tw["user"]["name"] or "Lauryn" in tw["user"]["name"] or "Giuliana" in tw["user"]["name"] or "Livia" in tw["user"]["name"] or "Anya" in tw["user"]["name"] or "Mikaela" in tw["user"]["name"] or "Palmer" in tw["user"]["name"] or "Lyra" in tw["user"]["name"] or "Mara" in tw["user"]["name"] or "Marina" in tw["user"]["name"] or "Kailey" in tw["user"]["name"] or "Liv" in tw["user"]["name"] or "Clementine" in tw["user"]["name"] or "Kenna" in tw["user"]["name"] or "Briar" in tw["user"]["name"] or "Emerie" in tw["user"]["name"] or "Galilea" in tw["user"]["name"] or "Tiffany" in tw["user"]["name"] or "Bonnie" in tw["user"]["name"] or "Elyse" in tw["user"]["name"] or "Cynthia" in tw["user"]["name"] or "Frida" in tw["user"]["name"] or "Kinslee" in tw["user"]["name"] or "Tatiana" in tw["user"]["name"] or "Joelle" in tw["user"]["name"] or "Armani" in tw["user"]["name"] or "Jolie" in tw["user"]["name"] or "Nalani" in tw["user"]["name"] or "Rayna" in tw["user"]["name"] or "Yareli" in tw["user"]["name"] or "Meghan" in tw["user"]["name"] or "Rebekah" in tw["user"]["name"] or "Addilynn" in tw["user"]["name"] or "Faye" in tw["user"]["name"] or "Zariyah" in tw["user"]["name"] or "Lea" in tw["user"]["name"] or "Aliza" in tw["user"]["name"] or "Julissa" in tw["user"]["name"] or "Lilyana" in tw["user"]["name"] or "Anika" in tw["user"]["name"] or "Kairi" in tw["user"]["name"] or "Aniya" in tw["user"]["name"] or "Noemi" in tw["user"]["name"] or "Angie" in tw["user"]["name"] or "Crystal" in tw["user"]["name"] or "Bridget" in tw["user"]["name"] or "Ari" in tw["user"]["name"] or "Davina" in tw["user"]["name"] or "Amelie" in tw["user"]["name"] or "Amirah" in tw["user"]["name"] or "Annika" in tw["user"]["name"] or "Elora" in tw["user"]["name"] or "Xiomara" in tw["user"]["name"] or "Linda" in tw["user"]["name"] or "Hana" in tw["user"]["name"] or "Laney" in tw["user"]["name"] or "Mercy" in tw["user"]["name"] or "Hadassah" in tw["user"]["name"] or "Madalyn" in tw["user"]["name"] or "Louisa" in tw["user"]["name"] or "Simone" in tw["user"]["name"] or "Kori" in tw["user"]["name"] or "Jillian" in tw["user"]["name"] or "Alena" in tw["user"]["name"] or "Malaya" in tw["user"]["name"] or "Miley" in tw["user"]["name"] or "Milan" in tw["user"]["name"] or "Sariyah" in tw["user"]["name"] or "Malani" in tw["user"]["name"] or "Clarissa" in tw["user"]["name"] or "Nala" in tw["user"]["name"] or "Princess" in tw["user"]["name"] or "Amani" in tw["user"]["name"] or "Analia" in tw["user"]["name"] or "Estella" in tw["user"]["name"] or "Milana" in tw["user"]["name"] or "Aya" in tw["user"]["name"] or "Chana" in tw["user"]["name"] or "Jayde" in tw["user"]["name"] or "Tenley" in tw["user"]["name"] or "Zaria" in tw["user"]["name"] or "Itzayana" in tw["user"]["name"] or "Penny" in tw["user"]["name"] or "Ailani" in tw["user"]["name"] or "Lara" in tw["user"]["name"] or "Aubriella" in tw["user"]["name"] or "Clare" in tw["user"]["name"] or "Lina" in tw["user"]["name"] or "Rhea" in tw["user"]["name"] or "Bria" in tw["user"]["name"] or "Thalia" in tw["user"]["name"] or "Keyla" in tw["user"]["name"] or "Haisley" in tw["user"]["name"] or "Ryann" in tw["user"]["name"] or "Addisyn" in tw["user"]["name"] or "Amaia" in tw["user"]["name"] or "Chanel" in tw["user"]["name"] or "Ellen" in tw["user"]["name"] or "Harmoni" in tw["user"]["name"] or "Aliana" in tw["user"]["name"] or "Tinsley" in tw["user"]["name"] or "Landry" in tw["user"]["name"] or "Paisleigh" in tw["user"]["name"] or "Lexie" in tw["user"]["name"] or "Myah" in tw["user"]["name"] or "Rylan" in tw["user"]["name"] or "Deborah" in tw["user"]["name"] or "Emilee" in tw["user"]["name"] or "Laylah" in tw["user"]["name"] or "Novalee" in tw["user"]["name"] or "Ellis" in tw["user"]["name"] or "Emmeline" in tw["user"]["name"] or "Avalynn" in tw["user"]["name"] or "Hadlee" in tw["user"]["name"] or "Legacy" in tw["user"]["name"] or "Braylee" in tw["user"]["name"] or "Elisabeth" in tw["user"]["name"] or "Kaylie" in tw["user"]["name"] or "Ansley" in tw["user"]["name"] or "Dior" in tw["user"]["name"] or "Paula" in tw["user"]["name"] or "Belen" in tw["user"]["name"] or "Corinne" in tw["user"]["name"] or "Maleah" in tw["user"]["name"] or "Martha" in tw["user"]["name"] or "Teresa" in tw["user"]["name"] or "Salma" in tw["user"]["name"] or "Louise" in tw["user"]["name"] or "Averi" in tw["user"]["name"] or "Lilianna" in tw["user"]["name"] or "Amiya" in tw["user"]["name"] or "Milena" in tw["user"]["name"] or "Royal" in tw["user"]["name"] or "Aubrielle" in tw["user"]["name"] or "Calliope" in tw["user"]["name"] or "Frankie" in tw["user"]["name"] or "Natasha" in tw["user"]["name"] or "Kamilah" in tw["user"]["name"] or "Meilani" in tw["user"]["name"] or "Raina" in tw["user"]["name"] or "Amayah" in tw["user"]["name"] or "Lailah" in tw["user"]["name"] or "Rayne" in tw["user"]["name"] or "Zaniyah" in tw["user"]["name"] or "Isabela" in tw["user"]["name"] or "Nathalie" in tw["user"]["name"] or "Miah" in tw["user"]["name"] or "Opal" in tw["user"]["name"] or "Kenia" in tw["user"]["name"] or "Azariah" in tw["user"]["name"] or "Hunter" in tw["user"]["name"] or "Tori" in tw["user"]["name"] or "Andi" in tw["user"]["name"] or "Keily" in tw["user"]["name"] or "Leanna" in tw["user"]["name"] or "Scarlette" in tw["user"]["name"] or "Jaelyn" in tw["user"]["name"] or "Saoirse" in tw["user"]["name"] or "Selene" in tw["user"]["name"] or "Dalary" in tw["user"]["name"] or "Lindsey" in tw["user"]["name"] or "Marianna" in tw["user"]["name"] or "Ramona" in tw["user"]["name"] or "Estelle" in tw["user"]["name"] or "Giovanna" in tw["user"]["name"] or "Holland" in tw["user"]["name"] or "Nancy" in tw["user"]["name"] or "Emmalynn" in tw["user"]["name"] or "Mylah" in tw["user"]["name"] or "Rosalee" in tw["user"]["name"] or "Sariah" in tw["user"]["name"] or "Zoie" in tw["user"]["name"] or "Blaire" in tw["user"]["name"] or "Lyanna" in tw["user"]["name"] or "Maxine" in tw["user"]["name"] or "Anais" in tw["user"]["name"] or "Dana" in tw["user"]["name"] or "Judith" in tw["user"]["name"] or "Kiera" in tw["user"]["name"] or "Jaelynn" in tw["user"]["name"] or "Noor" in tw["user"]["name"] or "Kai" in tw["user"]["name"] or "Adalee" in tw["user"]["name"] or "Oaklee" in tw["user"]["name"] or "Amaris" in tw["user"]["name"] or "Jaycee" in tw["user"]["name"] or "Belle" in tw["user"]["name"] or "Carolyn" in tw["user"]["name"] or "Della" in tw["user"]["name"] or "Karter" in tw["user"]["name"] or "Sky" in tw["user"]["name"] or "Treasure" in tw["user"]["name"] or "Vienna" in tw["user"]["name"] or "Jewel" in tw["user"]["name"] or "Rivka" in tw["user"]["name"] or "Rosalyn" in tw["user"]["name"] or "Alannah" in tw["user"]["name"] or "Ellianna" in tw["user"]["name"] or "Sunny" in tw["user"]["name"] or "Claudia" in tw["user"]["name"] or "Cara" in tw["user"]["name"] or "Hailee" in tw["user"]["name"] or "Estrella" in tw["user"]["name"] or "Harleigh" in tw["user"]["name"] or "Zhavia" in tw["user"]["name"] or "Alianna" in tw["user"]["name"] or "Brittany" in tw["user"]["name"] or "Jaylene" in tw["user"]["name"] or "Journi" in tw["user"]["name"] or "Marissa" in tw["user"]["name"] or "Mavis" in tw["user"]["name"] or "Iliana" in tw["user"]["name"] or "Jurnee" in tw["user"]["name"] or "Aislinn" in tw["user"]["name"] or "Alyson" in tw["user"]["name"] or "Elsa" in tw["user"]["name"] or "Kamiyah" in tw["user"]["name"] or "Kiana" in tw["user"]["name"] or "Lisa" in tw["user"]["name"] or "Arlette" in tw["user"]["name"] or "Kadence" in tw["user"]["name"] or "Kathleen" in tw["user"]["name"] or "Halle" in tw["user"]["name"] or "Erika" in tw["user"]["name"] or "Sylvie" in tw["user"]["name"] or "Adele" in tw["user"]["name"] or "Erica" in tw["user"]["name"] or "Veda" in tw["user"]["name"] or "Whitney" in tw["user"]["name"] or "Bexley" in tw["user"]["name"] or "Emmaline" in tw["user"]["name"] or "Guadalupe" in tw["user"]["name"] or "August" in tw["user"]["name"] or "Brynleigh" in tw["user"]["name"] or "Gwen" in tw["user"]["name"] or "Promise" in tw["user"]["name"] or "Alisson" in tw["user"]["name"] or "India" in tw["user"]["name"] or "Madalynn" in tw["user"]["name"] or "Paloma" in tw["user"]["name"] or "Patricia" in tw["user"]["name"] or "Samira" in tw["user"]["name"] or "Aliya" in tw["user"]["name"] or "Casey" in tw["user"]["name"] or "Jazlynn" in tw["user"]["name"] or "Paulina" in tw["user"]["name"] or "Dulce" in tw["user"]["name"] or "Kallie" in tw["user"]["name"] or "Perla" in tw["user"]["name"] or "Adrienne" in tw["user"]["name"] or "Alora" in tw["user"]["name"] or "Nataly" in tw["user"]["name"] or "Ayleen" in tw["user"]["name"] or "Christine" in tw["user"]["name"] or "Kaiya" in tw["user"]["name"] or "Ariadne" in tw["user"]["name"] or "Karlee" in tw["user"]["name"] or "Barbara" in tw["user"]["name"] or "Lillianna" in tw["user"]["name"] or "Raquel" in tw["user"]["name"] or "Saniyah" in tw["user"]["name"] or "Yamileth" in tw["user"]["name"] or "Arely" in tw["user"]["name"] or "Celia" in tw["user"]["name"] or "Heavenly" in tw["user"]["name"] or "Kaylin" in tw["user"]["name"] or "Marisol" in tw["user"]["name"] or "Marleigh" in tw["user"]["name"] or "Avalyn" in tw["user"]["name"] or "Berkley" in tw["user"]["name"] or "Kataleya" in tw["user"]["name"] or "Zainab" in tw["user"]["name"] or "Dani" in tw["user"]["name"] or "Egypt" in tw["user"]["name"] or "Joyce" in tw["user"]["name"] or "Kenley" in tw["user"]["name"] or "Annabel" in tw["user"]["name"] or "Kaelyn" in tw["user"]["name"] or "Etta" in tw["user"]["name"] or "Hadleigh" in tw["user"]["name"] or "Joselyn" in tw["user"]["name"] or "Luella" in tw["user"]["name"] or "Jaylee" in tw["user"]["name"] or "Zola" in tw["user"]["name"] or "Alisha" in tw["user"]["name"] or "Ezra" in tw["user"]["name"] or "Queen" in tw["user"]["name"] or "Amia" in tw["user"]["name"] or "Annalee" in tw["user"]["name"] or "Bellamy" in tw["user"]["name"] or "Paola" in tw["user"]["name"] or "Tinley" in tw["user"]["name"] or "Violeta" in tw["user"]["name"] or "Jenesis" in tw["user"]["name"] or "Arden" in tw["user"]["name"] or "Giana" in tw["user"]["name"] or "Wendy" in tw["user"]["name"] or "Ellison" in tw["user"]["name"] or "Florence" in tw["user"]["name"] or "Margo" in tw["user"]["name"] or "Naya" in tw["user"]["name"] or "Robin" in tw["user"]["name"] or "Sandra" in tw["user"]["name"] or "Scout" in tw["user"]["name"] or "Waverly" in tw["user"]["name"] or "Janessa" in tw["user"]["name"] or "Jayden" in tw["user"]["name"] or "Micah" in tw["user"]["name"] or "Novah" in tw["user"]["name"] or "Zora" in tw["user"]["name"] or "Ann" in tw["user"]["name"] or "Jana" in tw["user"]["name"] or "Taliyah" in tw["user"]["name"] or "Vada" in tw["user"]["name"] or "Giavanna" in tw["user"]["name"] or "Ingrid" in tw["user"]["name"] or "Valery" in tw["user"]["name"] or "Azaria" in tw["user"]["name"] or "Emmarie" in tw["user"]["name"] or "Esperanza" in tw["user"]["name"] or "Kailyn" in tw["user"]["name"] or "Aiyana" in tw["user"]["name"] or "Keilani" in tw["user"]["name"] or "Austyn" in tw["user"]["name"] or "Whitley" in tw["user"]["name"] or "Elina" in tw["user"]["name"] or "Kimora" in tw["user"]["name"] or "Maliah" in tw["user"]["name"]):
		bla.append(tw["user"]["id"])
	else:
		whi.append(tw["user"]["id"])

def calcResult(name, pop, blat, bbla, bwhi, tlat, tbla, twhi, percl, percb, percw):
	users = 0
	print(name)
	trlat, trbla, trwhi, bilat, bibla, biwhi = 0, 0, 0, 0, 0, 0
	print(f"Men ({percl*100}%)")
	if(not(len(set(tlat)) + len(set(blat)) < 1)):
		for user in blat:
			if(user in tlat):
				if(blat.count(user) > tlat.count(user)):
					try:
						while True:
							tlat.remove(user)
					except ValueError:
						pass
				if(tlat.count(user) > blat.count(user)):
					try:
						while True:
							blat.remove(user)
					except ValueError:
						pass
		for user in tlat:
			if(user in blat):
				if(blat.count(user) > tlat.count(user)):
					try:
						while True:
							tlat.remove(user)
					except ValueError:
						pass
				if(tlat.count(user) > blat.count(user)):
					try:
						while True:
							blat.remove(user)
					except ValueError:
						pass
		trlat = (len(set(tlat))/(len(set(tlat))+len(set(blat))))-(len(set(tlat).intersection(set(blat)))/(len(set(tlat))+len(set(blat)))/2)
		bilat = (len(set(blat))/(len(set(tlat))+len(set(blat))))-(len(set(tlat).intersection(set(blat)))/(len(set(tlat))+len(set(blat)))/2)
		print("Trump Men:", trlat)
		print("Biden Men:", bilat)
	else:
		print("No Latino Tweets Registered in This District")
	print(f"Women ({percb*100}%)")
	if(not(len(set(tbla)) + len(set(bbla)) < 1)):
		for user in bbla:
			if(user in tbla):
				if(bbla.count(user) > tbla.count(user)):
					try:
						while True:
							tbla.remove(user)
					except ValueError:
						pass
				if(tbla.count(user) > bbla.count(user)):
					try:
						while True:
							bbla.remove(user)
					except ValueError:
						pass
		for user in tbla:
			if(user in bbla):
				if(bbla.count(user) > tbla.count(user)):
					try:
						while True:
							tbla.remove(user)
					except ValueError:
						pass
				if(tbla.count(user) > bbla.count(user)):
					try:
						while True:
							bbla.remove(user)
					except ValueError:
						pass
		trbla = (len(set(tbla))/(len(set(tbla))+len(set(bbla))))-(len(set(tbla).intersection(set(bbla)))/(len(set(tbla))+len(set(bbla)))/2)
		bibla = (len(set(bbla))/(len(set(tbla))+len(set(bbla))))-(len(set(tbla).intersection(set(bbla)))/(len(set(tbla))+len(set(bbla)))/2)
		print("Trump Women:", trbla)
		print("Biden Women:", bibla)
	else:
		print("No Black Tweets Registered in This District")
	print(f"Unknowns ({percw*100}%)")
	if(not(len(set(twhi)) + len(set(bwhi)) < 1)):
		for user in bwhi:
			if(user in twhi):
				if(bwhi.count(user) > twhi.count(user)):
					try:
						while True:
							twhi.remove(user)
					except ValueError:
						pass
				if(twhi.count(user) > bwhi.count(user)):
					try:
						while True:
							bwhi.remove(user)
					except ValueError:
						pass
		for user in twhi:
			if(user in bwhi):
				if(bwhi.count(user) > twhi.count(user)):
					try:
						while True:
							twhi.remove(user)
					except ValueError:
						pass
				if(twhi.count(user) > bwhi.count(user)):
					try:
						while True:
							bwhi.remove(user)
					except ValueError:
						pass
		trwhi = (len(set(twhi))/(len(set(twhi))+len(set(bwhi))))-(len(set(twhi).intersection(set(bwhi)))/(len(set(twhi))+len(set(bwhi))/2))
		biwhi = (len(set(bwhi))/(len(set(twhi))+len(set(bwhi))))-(len(set(twhi).intersection(set(bwhi)))/(len(set(twhi))+len(set(bwhi))/2))
		print("Trump Unknowns:", trwhi)
		print("Biden Unknowns:", biwhi)
	else:
		print("No White Tweets Registered in This District")
	trumpvotes = (trlat*pop*percl)+(trbla*pop*percb)+(trwhi*pop*(1-percl-percb))
	bidenvotes = (bilat*pop*percl)+(bibla*pop*percb)+(biwhi*pop*(1-percl-percb))
	users = len(set(twhi)) + len(set(bwhi)) + len(set(tlat)) + len(set(blat)) + len(set(tbla)) + len(set(bbla))
	# trumpvotes = (trlat*pop*percl)+(trwhi*pop*percw)
	# bidenvotes = (bilat*pop*percl)+(biwhi*pop*percw)
	print("FINAL RESULT")
	print("TRUMP: ", (trumpvotes/pop)*100)
	print("BIDEN: ", (bidenvotes/pop)*100)
	print("Undecided: ", ((pop-trumpvotes-bidenvotes)/pop)*100)
	print("Total votes: ", users)
	print("")
	global bidendistricts
	global trumpdistricts
	if((trumpvotes/pop)*100 > (bidenvotes/pop)*100):
		trumpdistricts += 1
	elif((trumpvotes/pop)*100 < (bidenvotes/pop)*100):
		bidendistricts += 1

def calcStateResult(name, tlat, tbla, twhi, blat, bbla, bwhi, plat, pbla, pwhi):
	users = 0
	print(name)
	trlat, bilat, trbla, bibla, trwhi, biwhi = [], [], [], [], [], []
	for x in range(0,len(tlat)-1):
		if(not(len(tlat[x]) == 0 | len(blat[x]) == 0)):
			if(len(set(tlat[x]))+len(set(blat[x])) > 1):
				trlat.append(len(set(tlat[x]))/(len(set(tlat[x]))+len(set(blat[x]))))	#0.34, 0.44, 0.64
				bilat.append(len(set(blat[x]))/(len(set(tlat[x]))+len(set(blat[x]))))
				users += len(set(tlat[x])) + len (set(blat[x]))
	for x in range(0,len(tbla)-1):
		if(not(len(tbla[x]) == 0 | len(bbla[x]) == 0)):
			if(len(set(tbla[x]))+len(set(bbla[x])) > 1):
				trbla.append(len(set(tbla[x]))/(len(set(tbla[x]))+len(set(bbla[x]))))
				bibla.append(len(set(bbla[x]))/(len(set(tbla[x]))+len(set(bbla[x]))))
				users += len(set(tbla[x])) + len (set(bbla[x]))
	for x in range(0,len(twhi)-1):
		if(not(len(twhi[x]) == 0 | len(bwhi[x]) == 0)):
			if(len(set(twhi[x]))+len(set(bwhi[x])) > 1):
				trwhi.append(len(set(twhi[x]))/(len(set(twhi[x]))+len(set(bwhi[x]))))
				biwhi.append(len(set(bwhi[x]))/(len(set(twhi[x]))+len(set(bwhi[x]))))
				users += len(set(twhi[x])) + len (set(bwhi[x]))
	print(f"Men ({plat*100}%)")
	if(not(len(trlat) == 0 | len(bilat) == 0)):
		tl = sum(trlat)/len(trlat)
		bl = sum(bilat)/len(bilat)
		print("Trump Men: ", tl)
		print("Biden Men: ", bl)
	else:
		print("No Men here")
		tl, bl = 0, 0
	print(f"Women ({pbla*100}%)")
	if(not(len(trbla) == 0 | len(bibla) == 0)):
		tb = sum(trbla)/len(trbla)
		bb = sum(bibla)/len(bibla)
		print("Trump Women: ", tb)
		print("Biden Women: ", bb)
	else:
		print("No Women here")
		tb, bb = 0, 0
	print(f"Unknowns ({pwhi*100}%)")
	if(not(len(trwhi) == 0 | len(biwhi) == 0)):
		tw = sum(trwhi)/len(trwhi)
		bw = sum(biwhi)/len(biwhi)
		print("Trump Unknowns: ", tw)
		print("Biden Unknowns: ", bw)
	else:
		print("No Unknowns here")
		tw, bw = 0, 0
	print("TOTAL RESULT")
	print("TRUMP: ", (tl*plat)+(tb*pbla)+(tw*(1-plat-pbla)))
	print("BIDEN: ", (bl*plat)+(bb*pbla)+(bw*(1-plat-pbla)))
	print("Total Users: ", users)
	print("")
	results.append(name + " - Trump: " + str((tl*plat)+(tb*pbla)+(tw*(1-plat-pbla))) + "; Biden: " + str((bl*plat)+(bb*pbla)+(bw*(1-plat-pbla))))

#	results.append(name + " - Trump: " + str((tl*plat)+(tw*pwhi)) + "; Biden: " + str((bl*plat)+(bw*pwhi)))


# mo1tl, mo1tb, mo1tw, mo1bl, mo1bb, mo1bw, mo2tl, mo2tb, mo2tw, mo2bl, mo2bb, mo2bw, mo3tl, mo3tb, mo3tw, mo3bl, mo3bb, mo3bw, mo4tl, mo4tb, mo4tw, mo4bl, mo4bb, mo4bw, mo5tl, mo5tb, mo5tw, mo5bl, mo5bb, mo5bw, mo6tl, mo6tb, mo6tw, mo6bl, mo6bb, mo6bw, mo7tl, mo7tb, mo7tw, mo7bl, mo7bb, mo7bw, mo8tl, mo8tb, mo8tw, mo8bl, mo8bb, mo8bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# co1tl, co1tb, co1tw, co1bl, co1bb, co1bw, co2tl, co2tb, co2tw, co2bl, co2bb, co2bw, co3tl, co3tb, co3tw, co3bl, co3bb, co3bw, co4tl, co4tb, co4tw, co4bl, co4bb, co4bw, co5tl, co5tb, co5tw, co5bl, co5bb, co5bw, co6tl, co6tb, co6tw, co6bl, co6bb, co6bw, co7tl, co7tb, co7tw, co7bl, co7bb, co7bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# sc1tl, sc1tb, sc1tw, sc1bl, sc1bb, sc1bw, sc2tl, sc2tb, sc2tw, sc2bl, sc2bb, sc2bw, sc3tl, sc3tb, sc3tw, sc3bl, sc3bb, sc3bw, sc4tl, sc4tb, sc4tw, sc4bl, sc4bb, sc4bw, sc5tl, sc5tb, sc5tw, sc5bl, sc5bb, sc5bw, sc6bl, sc6bb, sc6bw, sc6tl, sc6tb, sc6tw, sc7tl, sc7tb, sc7tw, sc7bl, sc7bb, sc7bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# mn1tl, mn1tb, mn1tw, mn1bl, mn1bb, mn1bw, mn2tl, mn2tb, mn2tw, mn2bl, mn2bb, mn2bw, mn3tl, mn3tb, mn3tw, mn3bl, mn3bb, mn3bw, mn4tl, mn4tb, mn4tw, mn4bl, mn4bb, mn4bw, mn5tl, mn5tb, mn5tw, mn5bl, mn5bb, mn5bw, mn6tl, mn6tb, mn6tw, mn6bl, mn6bb, mn6bw, mn7tl, mn7tb, mn7tw, mn7bl, mn7bb, mn7bw, mn8tl, mn8tb, mn8tw, mn8bl, mn8bb, mn8bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# in1tl, in1tb, in1tw, in1bl, in1bb, in1bw, in2tl, in2tb, in2tw, in2bl, in2bb, in2bw, in3tl, in3tb, in3tw, in3bl, in3bb, in3bw, in4tl, in4tb, in4tw, in4bl, in4bb, in4bw, in5tl, in5tb, in5tw, in5bl, in5bb, in5bw, in6tl, in6tb, in6tw, in6bl, in6bb, in6bw, in7tl, in7tb, in7tw, in7bl, in7bb, in7bw, in8tl, in8tb, in8tw, in8bl, in8bb, in8bw, in9tl, in9tb, in9tw, in9bl, in9bb, in9bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# md1tl, md1tb, md1tw, md1bl, md1bb, md1bw, md2tl, md2tb, md2tw, md2bl, md2bb, md2bw, md3tl, md3tb, md3tw, md3bl, md3bb, md3bw, md4tl, md4tb, md4tw, md4bl, md4bb, md4bw, md5tl, md5tb, md5tw, md5bl, md5bb, md5bw, md6tl, md6tb, md6tw, md6bl, md6bb, md6bw, md7tl, md7tb, md7tw, md7bl, md7bb, md7bw, md8tl, md8tb, md8tw, md8bl, md8bb, md8bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# sd1tl, sd1tb, sd1tw, sd1bl, sd1bb, sd1bw =  [], [], [], [], [], []
# vt1tl, vt1tb, vt1tw, vt1bl, vt1bb, vt1bw =  [], [], [], [], [], []
# nd1tl, nd1tb, nd1tw, nd1bl, nd1bb, nd1bw =  [], [], [], [], [], []
# de1tl, de1tb, de1tw, de1bl, de1bb, de1bw =  [], [], [], [], [], []
# mt1tl, mt1tb, mt1tw, mt1bl, mt1bb, mt1bw =  [], [], [], [], [], []
# ne1tl, ne1tb, ne1tw, ne1bl, ne1bb, ne1bw, ne2tl, ne2tb, ne2tw, ne2bl, ne2bb, ne2bw, ne3tl, ne3tb, ne3tw, ne3bl, ne3bb, ne3bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# mi1tl, mi1tb, mi1tw, mi1bl, mi1bb, mi1bw, mi2tl, mi2tb, mi2tw, mi2bl, mi2bb, mi2bw, mi3tl, mi3tb, mi3tw, mi3bl, mi3bb, mi3bw, mi4tl, mi4tb, mi4tw, mi4bl, mi4bb, mi4bw, mi5tl, mi5tb, mi5tw, mi5bl, mi5bb, mi5bw, mi6tl, mi6tb, mi6tw, mi6bl, mi6bb, mi6bw, mi7tl, mi7tb, mi7tw, mi7bl, mi7bb, mi7bw, mi8tl, mi8tb, mi8tw, mi8bl, mi8bb, mi8bw, mi9tl, mi9tb, mi9tw, mi9bl, mi9bb, mi9bw, mi10tl, mi10tb, mi10tw, mi10bl, mi10bb, mi10bw, mi11tl, mi11tb, mi11tw, mi11bl, mi11bb, mi11bw, mi12tl, mi12tb, mi12tw, mi12bl, mi12bb, mi12bw, mi13tl, mi13tb, mi13tw, mi13bl, mi13bb, mi13bw, mi14tl, mi14tb, mi14tw, mi14bl, mi14bb, mi14bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ma1tl, ma1tb, ma1tw, ma1bl, ma1bb, ma1bw, ma2tl, ma2tb, ma2tw, ma2bl, ma2bb, ma2bw, ma3tl, ma3tb, ma3tw, ma3bl, ma3bb, ma3bw, ma4tl, ma4tb, ma4tw, ma4bl, ma4bb, ma4bw, ma5tl, ma5tb, ma5tw, ma5bl, ma5bb, ma5bw, ma6tl, ma6tb, ma6tw, ma6bl, ma6bb, ma6bw, ma7tl, ma7tb, ma7tw, ma7bl, ma7bb, ma7bw, ma8tl, ma8tb, ma8tw, ma8bl, ma8bb, ma8bw, ma9tl, ma9tb, ma9tw, ma9bl, ma9bb, ma9bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# va1tl, va1tb, va1tw, va1bl, va1bb, va1bw, va2tl, va2tb, va2tw, va2bl, va2bb, va2bw, va3tl, va3tb, va3tw, va3bl, va3bb, va3bw, va4tl, va4tb, va4tw, va4bl, va4bb, va4bw, va5tl, va5tb, va5tw, va5bl, va5bb, va5bw, va6tl, va6tb, va6tw, va6bl, va6bb, va6bw, va7tl, va7tb, va7tw, va7bl, va7bb, va7bw, va8tl, va8tb, va8tw, va8bl, va8bb, va8bw, va9tl, va9tb, va9tw, va9bl, va9bb, va9bw, va10tl, va10tb, va10tw, va10bl, va10bb, va10bw, va11tl, va11tb, va11tw, va11bl, va11bb, va11bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# me1tl, me1tb, me1tw, me1bl, me1bb, me1bw, me2tl, me2tb, me2tw, me2bl, me2bb, me2bw =  [], [], [], [], [], [], [], [], [], [], [], []
# id1tl, id1tb, id1tw, id1bl, id1bb, id1bw, id2tl, id2tb, id2tw, id2bl, id2bb, id2bw =  [], [], [], [], [], [], [], [], [], [], [], []
# wi1tl, wi1tb, wi1tw, wi1bl, wi1bb, wi1bw, wi2tl, wi2tb, wi2tw, wi2bl, wi2bb, wi2bw, wi3tl, wi3tb, wi3tw, wi3bl, wi3bb, wi3bw, wi4tl, wi4tb, wi4tw, wi4bl, wi4bb, wi4bw, wi5tl, wi5tb, wi5tw, wi5bl, wi5bb, wi5bw, wi6tl, wi6tb, wi6tw, wi6bl, wi6bb, wi6bw, wi7tl, wi7tb, wi7tw, wi7bl, wi7bb, wi7bw, wi8tl, wi8tb, wi8tw, wi8bl, wi8bb, wi8bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# wv1tl, wv1tb, wv1tw, wv1bl, wv1bb, wv1bw, wv2tl, wv2tb, wv2tw, wv2bl, wv2bb, wv2bw, wv3tl, wv3tb, wv3tw, wv3bl, wv3bb, wv3bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ia1tl, ia1tb, ia1tw, ia1bl, ia1bb, ia1bw, ia2tl, ia2tb, ia2tw, ia2bl, ia2bb, ia2bw, ia3tl, ia3tb, ia3tw, ia3bl, ia3bb, ia3bw, ia4tl, ia4tb, ia4tw, ia4bl, ia4bb, ia4bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ms1tl, ms1tb, ms1tw, ms1bl, ms1bb, ms1bw, ms2tl, ms2tb, ms2tw, ms2bl, ms2bb, ms2bw, ms3tl, ms3tb, ms3tw, ms3bl, ms3bb, ms3bw, ms4tl, ms4tb, ms4tw, ms4bl, ms4bb, ms4bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# hi1tl, hi1tb, hi1tw, hi1bl, hi1bb, hi1bw, hi2tl, hi2tb, hi2tw, hi2bl, hi2bb, hi2bw =  [], [], [], [], [], [], [], [], [], [], [], []
# ri1bl, ri1bb, ri1bw, ri1tl, ri1tb, ri1tw, ri2bl, ri2bb, ri2bw, ri2tl, ri2tb, ri2tw =  [], [], [], [], [], [], [], [], [], [], [], []
# wa1tl, wa1tb, wa1tw, wa1bl, wa1bb, wa1bw, wa2tl, wa2tb, wa2tw, wa2bl, wa2bb, wa2bw, wa3tl, wa3tb, wa3tw, wa3bl, wa3bb, wa3bw, wa4tl, wa4tb, wa4tw, wa4bl, wa4bb, wa4bw, wa5tl, wa5tb, wa5tw, wa5bl, wa5bb, wa5bw, wa6tl, wa6tb, wa6tw, wa6bl, wa6bb, wa6bw, wa7tl, wa7tb, wa7tw, wa7bl, wa7bb, wa7bw, wa8tl, wa8tb, wa8tw, wa8bl, wa8bb, wa8bw, wa9tl, wa9tb, wa9tw, wa9bl, wa9bb, wa9bw, wa10tl, wa10tb, wa10tw, wa10bl, wa10bb, wa10bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# fl1tl, fl1tb, fl1tw, fl1bl, fl1bb, fl1bw, fl2tl, fl2tb, fl2tw, fl2bl, fl2bb, fl2bw, fl3tl, fl3tb, fl3tw, fl3bl, fl3bb, fl3bw, fl4tl, fl4tb, fl4tw, fl4bl, fl4bb, fl4bw, fl5tl, fl5tb, fl5tw, fl5bl, fl5bb, fl5bw, fl6tl, fl6tb, fl6tw, fl6bl, fl6bb, fl6bw, fl7tl, fl7tb, fl7tw, fl7bl, fl7bb, fl7bw, fl8tl, fl8tb, fl8tw, fl8bl, fl8bb, fl8bw, fl9tl, fl9tb, fl9tw, fl9bl, fl9bb, fl9bw, fl10tl, fl10tb, fl10tw, fl10bl, fl10bb, fl10bw, fl11tl, fl11tb, fl11tw, fl11bl, fl11bb, fl11bw, fl12tl, fl12tb, fl12tw, fl12bl, fl12bb, fl12bw, fl13tl, fl13tb, fl13tw, fl13bl, fl13bb, fl13bw, fl14tl, fl14tb, fl14tw, fl14bl, fl14bb, fl14bw, fl15tl, fl15tb, fl15tw, fl15bl, fl15bb, fl15bw, fl16tl, fl16tb, fl16tw, fl16bl, fl16bb, fl16bw, fl17tl, fl17tb, fl17tw, fl17bl, fl17bb, fl17bw, fl18tl, fl18tb, fl18tw, fl18bl, fl18bb, fl18bw, fl19tl, fl19tb, fl19tw, fl19bl, fl19bb, fl19bw, fl20tl, fl20tb, fl20tw, fl20bl, fl20bb, fl20bw, fl21tl, fl21tb, fl21tw, fl21bl, fl21bb, fl21bw, fl22tl, fl22tb, fl22tw, fl22bl, fl22bb, fl22bw, fl23tl, fl23tb, fl23tw, fl23bl, fl23bb, fl23bw, fl24tl, fl24tb, fl24tw, fl24bl, fl24bb, fl24bw, fl25tl, fl25tb, fl25tw, fl25bl, fl25bb, fl25bw, fl26tl, fl26tb, fl26tw, fl26bl, fl26bb, fl26bw, fl27tl, fl27tb, fl27tw, fl27bl, fl27bb, fl27bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# al1tl, al1tb, al1tw, al1bl, al1bb, al1bw, al2tl, al2tb, al2tw, al2bl, al2bb, al2bw, al3tl, al3tb, al3tw, al3bl, al3bb, al3bw, al4tl, al4tb, al4tw, al4bl, al4bb, al4bw, al5tl, al5tb, al5tw, al5bl, al5bb, al5bw, al6tl, al6tb, al6tw, al6bl, al6bb, al6bw, al7bl, al7bb, al7bw, al7tl, al7tb, al7tw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# il1tl, il1tb, il1tw, il1bl, il1bb, il1bw, il2tl, il2tb, il2tw, il2bl, il2bb, il2bw, il3tl, il3tb, il3tw, il3bl, il3bb, il3bw, il4tl, il4tb, il4tw, il4bl, il4bb, il4bw, il5tl, il5tb, il5tw, il5bl, il5bb, il5bw, il6tl, il6tb, il6tw, il6bl, il6bb, il6bw, il7tl, il7tb, il7tw, il7bl, il7bb, il7bw, il8tl, il8tb, il8tw, il8bl, il8bb, il8bw, il9tl, il9tb, il9tw, il9bl, il9bb, il9bw, il10tl, il10tb, il10tw, il10bl, il10bb, il10bw, il11tl, il11tb, il11tw, il11bl, il11bb, il11bw, il12tl, il12tb, il12tw, il12bl, il12bb, il12bw, il13tl, il13tb, il13tw, il13bl, il13bb, il13bw, il14tl, il14tb, il14tw, il14bl, il14bb, il14bw, il15tl, il15tb, il15tw, il15bl, il15bb, il15bw, il16tl, il16tb, il16tw, il16bl, il16bb, il16bw, il17tl, il17tb, il17tw, il17bl, il17bb, il17bw, il18bl, il18bb, il18bw, il18tl, il18tb, il18tw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ca1tl, ca1tb, ca1tw, ca1bl, ca1bb, ca1bw, ca2tl, ca2tb, ca2tw, ca2bl, ca2bb, ca2bw, ca3tl, ca3tb, ca3tw, ca3bl, ca3bb, ca3bw, ca4tl, ca4tb, ca4tw, ca4bl, ca4bb, ca4bw, ca5tl, ca5tb, ca5tw, ca5bl, ca5bb, ca5bw, ca6tl, ca6tb, ca6tw, ca6bl, ca6bb, ca6bw, ca7tl, ca7tb, ca7tw, ca7bl, ca7bb, ca7bw, ca8tl, ca8tb, ca8tw, ca8bl, ca8bb, ca8bw, ca9tl, ca9tb, ca9tw, ca9bl, ca9bb, ca9bw, ca10tl, ca10tb, ca10tw, ca10bl, ca10bb, ca10bw, ca11tl, ca11tb, ca11tw, ca11bl, ca11bb, ca11bw, ca12tl, ca12tb, ca12tw, ca12bl, ca12bb, ca12bw, ca13tl, ca13tb, ca13tw, ca13bl, ca13bb, ca13bw, ca14tl, ca14tb, ca14tw, ca14bl, ca14bb, ca14bw, ca15tl, ca15tb, ca15tw, ca15bl, ca15bb, ca15bw, ca16tl, ca16tb, ca16tw, ca16bl, ca16bb, ca16bw, ca17tl, ca17tb, ca17tw, ca17bl, ca17bb, ca17bw, ca18tl, ca18tb, ca18tw, ca18bl, ca18bb, ca18bw, ca19bl, ca19bb, ca19bw, ca19tl, ca19tb, ca19tw, ca20tl, ca20tb, ca20tw, ca20bl, ca20bb, ca20bw, ca21tl, ca21tb, ca21tw, ca21bl, ca21bb, ca21bw, ca22tl, ca22tb, ca22tw, ca22bl, ca22bb, ca22bw, ca23tl, ca23tb, ca23tw, ca23bl, ca23bb, ca23bw, ca24tl, ca24tb, ca24tw, ca24bl, ca24bb, ca24bw, ca25tl, ca25tb, ca25tw, ca25bl, ca25bb, ca25bw, ca26tl, ca26tb, ca26tw, ca26bl, ca26bb, ca26bw, ca27tl, ca27tb, ca27tw, ca27bl, ca27bb, ca27bw, ca28tl, ca28tb, ca28tw, ca28bl, ca28bb, ca28bw, ca29tl, ca29tb, ca29tw, ca29bl, ca29bb, ca29bw, ca30tl, ca30tb, ca30tw, ca30bl, ca30bb, ca30bw, ca31tl, ca31tb, ca31tw, ca31bl, ca31bb, ca31bw, ca32tl, ca32tb, ca32tw, ca32bl, ca32bb, ca32bw, ca33tl, ca33tb, ca33tw, ca33bl, ca33bb, ca33bw, ca34tl, ca34tb, ca34tw, ca34bl, ca34bb, ca34bw, ca35tl, ca35tb, ca35tw, ca35bl, ca35bb, ca35bw, ca36tl, ca36tb, ca36tw, ca36bl, ca36bb, ca36bw, ca37tl, ca37tb, ca37tw, ca37bl, ca37bb, ca37bw, ca38tl, ca38tb, ca38tw, ca38bl, ca38bb, ca38bw, ca39tl, ca39tb, ca39tw, ca39bl, ca39bb, ca39bw, ca40tl, ca40tb, ca40tw, ca40bl, ca40bb, ca40bw, ca41tl, ca41tb, ca41tw, ca41bl, ca41bb, ca41bw, ca42tl, ca42tb, ca42tw, ca42bl, ca42bb, ca42bw, ca43tl, ca43tb, ca43tw, ca43bl, ca43bb, ca43bw, ca44tl, ca44tb, ca44tw, ca44bl, ca44bb, ca44bw, ca45tl, ca45tb, ca45tw, ca45bl, ca45bb, ca45bw, ca46tl, ca46tb, ca46tw, ca46bl, ca46bb, ca46bw, ca47tl, ca47tb, ca47tw, ca47bl, ca47bb, ca47bw, ca48tl, ca48tb, ca48tw, ca48bl, ca48bb, ca48bw, ca49tl, ca49tb, ca49tw, ca49bl, ca49bb, ca49bw, ca50tl, ca50tb, ca50tw, ca50bl, ca50bb, ca50bw, ca51tl, ca51tb, ca51tw, ca51bl, ca51bb, ca51bw, ca52tl, ca52tb, ca52tw, ca52bl, ca52bb, ca52bw, ca53tl, ca53tb, ca53tw, ca53bl, ca53bb, ca53bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ks1tl, ks1tb, ks1tw, ks1bl, ks1bb, ks1bw, ks2tl, ks2tb, ks2tw, ks2bl, ks2bb, ks2bw, ks3tl, ks3tb, ks3tw, ks3bl, ks3bb, ks3bw, ks4tl, ks4tb, ks4tw, ks4bl, ks4bb, ks4bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ga1tl, ga1tb, ga1tw, ga1bl, ga1bb, ga1bw, ga2tl, ga2tb, ga2tw, ga2bl, ga2bb, ga2bw, ga3tl, ga3tb, ga3tw, ga3bl, ga3bb, ga3bw, ga4tl, ga4tb, ga4tw, ga4bl, ga4bb, ga4bw, ga5tl, ga5tb, ga5tw, ga5bl, ga5bb, ga5bw, ga6tl, ga6tb, ga6tw, ga6bl, ga6bb, ga6bw, ga7tl, ga7tb, ga7tw, ga7bl, ga7bb, ga7bw, ga8tl, ga8tb, ga8tw, ga8bl, ga8bb, ga8bw, ga9tl, ga9tb, ga9tw, ga9bl, ga9bb, ga9bw, ga10tl, ga10tb, ga10tw, ga10bl, ga10bb, ga10bw, ga11tl, ga11tb, ga11tw, ga11bl, ga11bb, ga11bw, ga12tl, ga12tb, ga12tw, ga12bl, ga12bb, ga12bw, ga13tl, ga13tb, ga13tw, ga13bl, ga13bb, ga13bw, ga14tl, ga14tb, ga14tw, ga14bl, ga14bb, ga14bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# az1tl, az1tb, az1tw, az1bl, az1bb, az1bw, az2tl, az2tb, az2tw, az2bl, az2bb, az2bw, az3bl, az3bb, az3bw, az3tl, az3tb, az3tw, az4tl, az4tb, az4tw, az4bl, az4bb, az4bw, az5tl, az5tb, az5tw, az5bl, az5bb, az5bw, az6tl, az6tb, az6tw, az6bl, az6bb, az6bw, az7bl, az7bb, az7bw, az7tl, az7tb, az7tw, az8tl, az8tb, az8tw, az8bl, az8bb, az8bw, az9bl, az9bb, az9bw, az9tl, az9tb, az9tw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ak1tl, ak1tb, ak1tw, ak1bl, ak1bb, ak1bw =  [], [], [], [], [], []
# ar1tl, ar1tb, ar1tw, ar1bl, ar1bb, ar1bw, ar2tl, ar2tb, ar2tw, ar2bl, ar2bb, ar2bw, ar3tl, ar3tb, ar3tw, ar3bl, ar3bb, ar3bw, ar4tl, ar4tb, ar4tw, ar4bl, ar4bb, ar4bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# nj1tl, nj1tb, nj1tw, nj1bl, nj1bb, nj1bw, nj2tl, nj2tb, nj2tw, nj2bl, nj2bb, nj2bw, nj3tl, nj3tb, nj3tw, nj3bl, nj3bb, nj3bw, nj4tl, nj4tb, nj4tw, nj4bl, nj4bb, nj4bw, nj5tl, nj5tb, nj5tw, nj5bl, nj5bb, nj5bw, nj6tl, nj6tb, nj6tw, nj6bl, nj6bb, nj6bw, nj7tl, nj7tb, nj7tw, nj7bl, nj7bb, nj7bw, nj8tl, nj8tb, nj8tw, nj8bl, nj8bb, nj8bw, nj9tl, nj9tb, nj9tw, nj9bl, nj9bb, nj9bw, nj10tl, nj10tb, nj10tw, nj10bl, nj10bb, nj10bw, nj11tl, nj11tb, nj11tw, nj11bl, nj11bb, nj11bw, nj12tl, nj12tb, nj12tw, nj12bl, nj12bb, nj12bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# nv1tl, nv1tb, nv1tw, nv1bl, nv1bb, nv1bw, nv2tl, nv2tb, nv2tw, nv2bl, nv2bb, nv2bw, nv3tl, nv3tb, nv3tw, nv3bl, nv3bb, nv3bw, nv4tl, nv4tb, nv4tw, nv4bl, nv4bb, nv4bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# nh1tl, nh1tb, nh1tw, nh1bl, nh1bb, nh1bw, nh2tl, nh2tb, nh2tw, nh2bl, nh2bb, nh2bw =  [], [], [], [], [], [], [], [], [], [], [], []
# nc1tl, nc1tb, nc1tw, nc1bl, nc1bb, nc1bw, nc2tl, nc2tb, nc2tw, nc2bl, nc2bb, nc2bw, nc3tl, nc3tb, nc3tw, nc3bl, nc3bb, nc3bw, nc4tl, nc4tb, nc4tw, nc4bl, nc4bb, nc4bw, nc5tl, nc5tb, nc5tw, nc5bl, nc5bb, nc5bw, nc6tl, nc6tb, nc6tw, nc6bl, nc6bb, nc6bw, nc7tl, nc7tb, nc7tw, nc7bl, nc7bb, nc7bw, nc8tl, nc8tb, nc8tw, nc8bl, nc8bb, nc8bw, nc9tl, nc9tb, nc9tw, nc9bl, nc9bb, nc9bw, nc10tl, nc10tb, nc10tw, nc10bl, nc10bb, nc10bw, nc11tl, nc11tb, nc11tw, nc11bl, nc11bb, nc11bw, nc12tl, nc12tb, nc12tw, nc12bl, nc12bb, nc12bw, nc13tl, nc13tb, nc13tw, nc13bl, nc13bb, nc13bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# tx1tl, tx1tb, tx1tw, tx1bl, tx1bb, tx1bw, tx2tl, tx2tb, tx2tw, tx2bl, tx2bb, tx2bw, tx3tl, tx3tb, tx3tw, tx3bl, tx3bb, tx3bw, tx4tl, tx4tb, tx4tw, tx4bl, tx4bb, tx4bw, tx5tl, tx5tb, tx5tw, tx5bl, tx5bb, tx5bw, tx6tl, tx6tb, tx6tw, tx6bl, tx6bb, tx6bw, tx7tl, tx7tb, tx7tw, tx7bl, tx7bb, tx7bw, tx8tl, tx8tb, tx8tw, tx8bl, tx8bb, tx8bw, tx9tl, tx9tb, tx9tw, tx9bl, tx9bb, tx9bw, tx10tl, tx10tb, tx10tw, tx10bl, tx10bb, tx10bw, tx11tl, tx11tb, tx11tw, tx11bl, tx11bb, tx11bw, tx12tl, tx12tb, tx12tw, tx12bl, tx12bb, tx12bw, tx13tl, tx13tb, tx13tw, tx13bl, tx13bb, tx13bw, tx14tl, tx14tb, tx14tw, tx14bl, tx14bb, tx14bw, tx15tl, tx15tb, tx15tw, tx15bl, tx15bb, tx15bw, tx16tl, tx16tb, tx16tw, tx16bl, tx16bb, tx16bw, tx17tl, tx17tb, tx17tw, tx17bl, tx17bb, tx17bw, tx18tl, tx18tb, tx18tw, tx18bl, tx18bb, tx18bw, tx19tl, tx19tb, tx19tw, tx19bl, tx19bb, tx19bw, tx20tl, tx20tb, tx20tw, tx20bl, tx20bb, tx20bw, tx21tl, tx21tb, tx21tw, tx21bl, tx21bb, tx21bw, tx22tl, tx22tb, tx22tw, tx22bl, tx22bb, tx22bw, tx23tl, tx23tb, tx23tw, tx23bl, tx23bb, tx23bw, tx24tl, tx24tb, tx24tw, tx24bl, tx24bb, tx24bw, tx25tl, tx25tb, tx25tw, tx25bl, tx25bb, tx25bw, tx26tl, tx26tb, tx26tw, tx26bl, tx26bb, tx26bw, tx27tl, tx27tb, tx27tw, tx27bl, tx27bb, tx27bw, tx28tl, tx28tb, tx28tw, tx28bl, tx28bb, tx28bw, tx29tl, tx29tb, tx29tw, tx29bl, tx29bb, tx29bw, tx30tl, tx30tb, tx30tw, tx30bl, tx30bb, tx30bw, tx31tl, tx31tb, tx31tw, tx31bl, tx31bb, tx31bw, tx32tl, tx32tb, tx32tw, tx32bl, tx32bb, tx32bw, tx33tl, tx33tb, tx33tw, tx33bl, tx33bb, tx33bw, tx34tl, tx34tb, tx34tw, tx34bl, tx34bb, tx34bw, tx35tl, tx35tb, tx35tw, tx35bl, tx35bb, tx35bw, tx36tl, tx36tb, tx36tw, tx36bl, tx36bb, tx36bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# tn1tl, tn1tb, tn1tw, tn1bl, tn1bb, tn1bw, tn2tl, tn2tb, tn2tw, tn2bl, tn2bb, tn2bw, tn3tl, tn3tb, tn3tw, tn3bl, tn3bb, tn3bw, tn4tl, tn4tb, tn4tw, tn4bl, tn4bb, tn4bw, tn5bl, tn5bb, tn5bw, tn5tl, tn5tb, tn5tw, tn6tl, tn6tb, tn6tw, tn6bl, tn6bb, tn6bw, tn7tl, tn7tb, tn7tw, tn7bl, tn7bb, tn7bw, tn8tl, tn8tb, tn8tw, tn8bl, tn8bb, tn8bw, tn9bl, tn9bb, tn9bw, tn9tl, tn9tb, tn9tw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# nm1tl, nm1tb, nm1tw, nm1bl, nm1bb, nm1bw, nm2tl, nm2tb, nm2tw, nm2bl, nm2bb, nm2bw, nm3tl, nm3tb, nm3tw, nm3bl, nm3bb, nm3bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ny1tl, ny1tb, ny1tw, ny1bl, ny1bb, ny1bw, ny2tl, ny2tb, ny2tw, ny2bl, ny2bb, ny2bw, ny3tl, ny3tb, ny3tw, ny3bl, ny3bb, ny3bw, ny4tl, ny4tb, ny4tw, ny4bl, ny4bb, ny4bw, ny5tl, ny5tb, ny5tw, ny5bl, ny5bb, ny5bw, ny6tl, ny6tb, ny6tw, ny6bl, ny6bb, ny6bw, ny7tl, ny7tb, ny7tw, ny7bl, ny7bb, ny7bw, ny8tl, ny8tb, ny8tw, ny8bl, ny8bb, ny8bw, ny9tl, ny9tb, ny9tw, ny9bl, ny9bb, ny9bw, ny10tl, ny10tb, ny10tw, ny10bl, ny10bb, ny10bw, ny11tl, ny11tb, ny11tw, ny11bl, ny11bb, ny11bw, ny12tl, ny12tb, ny12tw, ny12bl, ny12bb, ny12bw, ny13tl, ny13tb, ny13tw, ny13bl, ny13bb, ny13bw, ny14tl, ny14tb, ny14tw, ny14bl, ny14bb, ny14bw, ny15tl, ny15tb, ny15tw, ny15bl, ny15bb, ny15bw, ny16tl, ny16tb, ny16tw, ny16bl, ny16bb, ny16bw, ny17tl, ny17tb, ny17tw, ny17bl, ny17bb, ny17bw, ny18tl, ny18tb, ny18tw, ny18bl, ny18bb, ny18bw, ny19tl, ny19tb, ny19tw, ny19bl, ny19bb, ny19bw, ny20tl, ny20tb, ny20tw, ny20bl, ny20bb, ny20bw, ny21tl, ny21tb, ny21tw, ny21bl, ny21bb, ny21bw, ny22tl, ny22tb, ny22tw, ny22bl, ny22bb, ny22bw, ny23tl, ny23tb, ny23tw, ny23bl, ny23bb, ny23bw, ny24tl, ny24tb, ny24tw, ny24bl, ny24bb, ny24bw, ny25tl, ny25tb, ny25tw, ny25bl, ny25bb, ny25bw, ny26tl, ny26tb, ny26tw, ny26bl, ny26bb, ny26bw, ny27tl, ny27tb, ny27tw, ny27bl, ny27bb, ny27bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# wy1tl, wy1tb, wy1tw, wy1bl, wy1bb, wy1bw =  [], [], [], [], [], []
# pa1tl, pa1tb, pa1tw, pa1bl, pa1bb, pa1bw, pa2tl, pa2tb, pa2tw, pa2bl, pa2bb, pa2bw, pa3tl, pa3tb, pa3tw, pa3bl, pa3bb, pa3bw, pa4tl, pa4tb, pa4tw, pa4bl, pa4bb, pa4bw, pa5tl, pa5tb, pa5tw, pa5bl, pa5bb, pa5bw, pa6tl, pa6tb, pa6tw, pa6bl, pa6bb, pa6bw, pa7tl, pa7tb, pa7tw, pa7bl, pa7bb, pa7bw, pa8tl, pa8tb, pa8tw, pa8bl, pa8bb, pa8bw, pa9tl, pa9tb, pa9tw, pa9bl, pa9bb, pa9bw, pa10tl, pa10tb, pa10tw, pa10bl, pa10bb, pa10bw, pa11tl, pa11tb, pa11tw, pa11bl, pa11bb, pa11bw, pa12tl, pa12tb, pa12tw, pa12bl, pa12bb, pa12bw, pa13tl, pa13tb, pa13tw, pa13bl, pa13bb, pa13bw, pa14tl, pa14tb, pa14tw, pa14bl, pa14bb, pa14bw, pa15tl, pa15tb, pa15tw, pa15bl, pa15bb, pa15bw, pa16tl, pa16tb, pa16tw, pa16bl, pa16bb, pa16bw, pa17tl, pa17tb, pa17tw, pa17bl, pa17bb, pa17bw, pa18tl, pa18tb, pa18tw, pa18bl, pa18bb, pa18bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ct1tl, ct1tb, ct1tw, ct1bl, ct1bb, ct1bw, ct2tl, ct2tb, ct2tw, ct2bl, ct2bb, ct2bw, ct3tl, ct3tb, ct3tw, ct3bl, ct3bb, ct3bw, ct4tl, ct4tb, ct4tw, ct4bl, ct4bb, ct4bw, ct5tl, ct5tb, ct5tw, ct5bl, ct5bb, ct5bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ky1tl, ky1tb, ky1tw, ky1bl, ky1bb, ky1bw, ky2tl, ky2tb, ky2tw, ky2bl, ky2bb, ky2bw, ky3tl, ky3tb, ky3tw, ky3bl, ky3bb, ky3bw, ky4tl, ky4tb, ky4tw, ky4bl, ky4bb, ky4bw, ky5tl, ky5tb, ky5tw, ky5bl, ky5bb, ky5bw, ky6tl, ky6tb, ky6tw, ky6bl, ky6bb, ky6bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# la1tl, la1tb, la1tw, la1bl, la1bb, la1bw, la2tl, la2tb, la2tw, la2bl, la2bb, la2bw, la3tl, la3tb, la3tw, la3bl, la3bb, la3bw, la4tl, la4tb, la4tw, la4bl, la4bb, la4bw, la5tl, la5tb, la5tw, la5bl, la5bb, la5bw, la6tl, la6tb, la6tw, la6bl, la6bb, la6bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ok1tl, ok1tb, ok1tw, ok1bl, ok1bb, ok1bw, ok2tl, ok2tb, ok2tw, ok2bl, ok2bb, ok2bw, ok3tl, ok3tb, ok3tw, ok3bl, ok3bb, ok3bw, ok4tl, ok4tb, ok4tw, ok4bl, ok4bb, ok4bw, ok5tl, ok5tb, ok5tw, ok5bl, ok5bb, ok5bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# ut1tl, ut1tb, ut1tw, ut1bl, ut1bb, ut1bw, ut2tl, ut2tb, ut2tw, ut2bl, ut2bb, ut2bw, ut3tl, ut3tb, ut3tw, ut3bl, ut3bb, ut3bw, ut4tl, ut4tb, ut4tw, ut4bl, ut4bb, ut4bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# oh1tl, oh1tb, oh1tw, oh1bl, oh1bb, oh1bw, oh2tl, oh2tb, oh2tw, oh2bl, oh2bb, oh2bw, oh3tl, oh3tb, oh3tw, oh3bl, oh3bb, oh3bw, oh4tl, oh4tb, oh4tw, oh4bl, oh4bb, oh4bw, oh5tl, oh5tb, oh5tw, oh5bl, oh5bb, oh5bw, oh6tl, oh6tb, oh6tw, oh6bl, oh6bb, oh6bw, oh7tl, oh7tb, oh7tw, oh7bl, oh7bb, oh7bw, oh8tl, oh8tb, oh8tw, oh8bl, oh8bb, oh8bw, oh9tl, oh9tb, oh9tw, oh9bl, oh9bb, oh9bw, oh10tl, oh10tb, oh10tw, oh10bl, oh10bb, oh10bw, oh11tl, oh11tb, oh11tw, oh11bl, oh11bb, oh11bw, oh12tl, oh12tb, oh12tw, oh12bl, oh12bb, oh12bw, oh13tl, oh13tb, oh13tw, oh13bl, oh13bb, oh13bw, oh14tl, oh14tb, oh14tw, oh14bl, oh14bb, oh14bw, oh15tl, oh15tb, oh15tw, oh15bl, oh15bb, oh15bw, oh16tl, oh16tb, oh16tw, oh16bl, oh16bb, oh16bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# or1tl, or1tb, or1tw, or1bl, or1bb, or1bw, or2tl, or2tb, or2tw, or2bl, or2bb, or2bw, or3tl, or3tb, or3tw, or3bl, or3bb, or3bw, or4tl, or4tb, or4tw, or4bl, or4bb, or4bw, or5tl, or5tb, or5tw, or5bl, or5bb, or5bw =  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

with open('/Volumes/TOSHIBA/usawithgender.txt', 'rb') as f:
	al1tl, al1tb, al1tw, al2tl, al2tb, al2tw, al3tl, al3tb, al3tw, al4tl, al4tb, al4tw, al5tl, al5tb, al5tw, al6tl, al6tb, al6tw, al7tl, al7tb, al7tw, al1bl, al1bb, al1bw, al2bl, al2bb, al2bw, al3bl, al3bb, al3bw, al4bl, al4bb, al4bw, al5bl, al5bb, al5bw, al6bl, al6bb, al6bw, al7bl, al7bb, al7bw, ak1tl, ak1tb, ak1tw, ak1bl, ak1bb, ak1bw, az1tl, az1tb, az1tw, az2tl, az2tb, az2tw, az3tl, az3tb, az3tw, az4tl, az4tb, az4tw, az5tl, az5tb, az5tw, az6tl, az6tb, az6tw, az7tl, az7tb, az7tw, az8tl, az8tb, az8tw, az9tl, az9tb, az9tw, az1bl, az1bb, az1bw, az2bl, az2bb, az2bw, az3bl, az3bb, az3bw, az4bl, az4bb, az4bw, az5bl, az5bb, az5bw, az6bl, az6bb, az6bw, az7bl, az7bb, az7bw, az8bl, az8bb, az8bw, az9bl, az9bb, az9bw, ar1bl, ar1bb, ar1bw, ar2bl, ar2bb, ar2bw, ar3bl, ar3bb, ar3bw, ar4bl, ar4bb, ar4bw, ar1tl, ar1tb, ar1tw, ar2tl, ar2tb, ar2tw, ar3tl, ar3tb, ar3tw, ar4tl, ar4tb, ar4tw, ak1bl, ak1bb, ak1bw, ca1tl, ca1tb, ca1tw, ca2tl, ca2tb, ca2tw, ca3tl, ca3tb, ca3tw, ca4tl, ca4tb, ca4tw, ca5tl, ca5tb, ca5tw, ca6tl, ca6tb, ca6tw, ca7tl, ca7tb, ca7tw, ca8tl, ca8tb, ca8tw, ca9tl, ca9tb, ca9tw, ca10tl, ca10tb, ca10tw, ca11tl, ca11tb, ca11tw, ca12tl, ca12tb, ca12tw, ca13tl, ca13tb, ca13tw, ca14tl, ca14tb, ca14tw, ca15tl, ca15tb, ca15tw, ca16tl, ca16tb, ca16tw, ca17tl, ca17tb, ca17tw, ca18tl, ca18tb, ca18tw, ca19tl, ca19tb, ca19tw, ca20tl, ca20tb, ca20tw, ca21tl, ca21tb, ca21tw, ca22tl, ca22tb, ca22tw, ca23tl, ca23tb, ca23tw, ca24tl, ca24tb, ca24tw, ca25tl, ca25tb, ca25tw, ca26tl, ca26tb, ca26tw, ca27tl, ca27tb, ca27tw, ca28tl, ca28tb, ca28tw, ca29tl, ca29tb, ca29tw, ca30tl, ca30tb, ca30tw, ca31tl, ca31tb, ca31tw, ca32tl, ca32tb, ca32tw, ca33tl, ca33tb, ca33tw, ca34tl, ca34tb, ca34tw, ca35tl, ca35tb, ca35tw, ca36tl, ca36tb, ca36tw, ca37tl, ca37tb, ca37tw, ca38tl, ca38tb, ca38tw, ca39tl, ca39tb, ca39tw, ca40tl, ca40tb, ca40tw, ca41tl, ca41tb, ca41tw, ca42tl, ca42tb, ca42tw, ca43tl, ca43tb, ca43tw, ca44tl, ca44tb, ca44tw, ca45tl, ca45tb, ca45tw, ca46tl, ca46tb, ca46tw, ca47tl, ca47tb, ca47tw, ca48tl, ca48tb, ca48tw, ca49tl, ca49tb, ca49tw, ca50tl, ca50tb, ca50tw, ca51tl, ca51tb, ca51tw, ca52tl, ca52tb, ca52tw, ca53tl, ca53tb, ca53tw, ca1bl, ca1bb, ca1bw, ca2bl, ca2bb, ca2bw, ca3bl, ca3bb, ca3bw, ca4bl, ca4bb, ca4bw, ca5bl, ca5bb, ca5bw, ca6bl, ca6bb, ca6bw, ca7bl, ca7bb, ca7bw, ca8bl, ca8bb, ca8bw, ca9bl, ca9bb, ca9bw, ca10bl, ca10bb, ca10bw, ca11bl, ca11bb, ca11bw, ca12bl, ca12bb, ca12bw, ca13bl, ca13bb, ca13bw, ca14bl, ca14bb, ca14bw, ca15bl, ca15bb, ca15bw, ca16bl, ca16bb, ca16bw, ca17bl, ca17bb, ca17bw, ca18bl, ca18bb, ca18bw, ca19bl, ca19bb, ca19bw, ca20bl, ca20bb, ca20bw, ca21bl, ca21bb, ca21bw, ca22bl, ca22bb, ca22bw, ca23bl, ca23bb, ca23bw, ca24bl, ca24bb, ca24bw, ca25bl, ca25bb, ca25bw, ca26bl, ca26bb, ca26bw, ca27bl, ca27bb, ca27bw, ca28bl, ca28bb, ca28bw, ca29bl, ca29bb, ca29bw, ca30bl, ca30bb, ca30bw, ca31bl, ca31bb, ca31bw, ca32bl, ca32bb, ca32bw, ca33bl, ca33bb, ca33bw, ca34bl, ca34bb, ca34bw, ca35bl, ca35bb, ca35bw, ca36bl, ca36bb, ca36bw, ca37bl, ca37bb, ca37bw, ca38bl, ca38bb, ca38bw, ca39bl, ca39bb, ca39bw, ca40bl, ca40bb, ca40bw, ca41bl, ca41bb, ca41bw, ca42bl, ca42bb, ca42bw, ca43bl, ca43bb, ca43bw, ca44bl, ca44bb, ca44bw, ca45bl, ca45bb, ca45bw, ca46bl, ca46bb, ca46bw, ca47bl, ca47bb, ca47bw, ca48bl, ca48bb, ca48bw, ca49bl, ca49bb, ca49bw, ca50bl, ca50bb, ca50bw, ca51bl, ca51bb, ca51bw, ca52bl, ca52bb, ca52bw, ca53bl, ca53bb, ca53bw, co1tl, co1tb, co1tw, co2tl, co2tb, co2tw, co3tl, co3tb, co3tw, co4tl, co4tb, co4tw, co5tl, co5tb, co5tw, co6tl, co6tb, co6tw, co7tl, co7tb, co7tw, co1bl, co1bb, co1bw, co2bl, co2bb, co2bw, co3bl, co3bb, co3bw, co4bl, co4bb, co4bw, co5bl, co5bb, co5bw, co6bl, co6bb, co6bw, co7bl, co7bb, co7bw, ct1bl, ct1bb, ct1bw, ct2bl, ct2bb, ct2bw, ct3bl, ct3bb, ct3bw, ct4bl, ct4bb, ct4bw, ct5bl, ct5bb, ct5bw, ct1tl, ct1tb, ct1tw, ct2tl, ct2tb, ct2tw, ct3tl, ct3tb, ct3tw, ct4tl, ct4tb, ct4tw, ct5tl, ct5tb, ct5tw, de1tl, de1tb, de1tw, de1bl, de1bb, de1bw, fl1bl, fl1bb, fl1bw, fl2bl, fl2bb, fl2bw, fl3bl, fl3bb, fl3bw, fl4bl, fl4bb, fl4bw, fl5bl, fl5bb, fl5bw, fl6bl, fl6bb, fl6bw, fl7bl, fl7bb, fl7bw, fl8bl, fl8bb, fl8bw, fl9bl, fl9bb, fl9bw, fl10bl, fl10bb, fl10bw, fl11bl, fl11bb, fl11bw, fl12bl, fl12bb, fl12bw, fl13bl, fl13bb, fl13bw, fl14bl, fl14bb, fl14bw, fl15bl, fl15bb, fl15bw, fl16bl, fl16bb, fl16bw, fl17bl, fl17bb, fl17bw, fl18bl, fl18bb, fl18bw, fl19bl, fl19bb, fl19bw, fl20bl, fl20bb, fl20bw, fl21bl, fl21bb, fl21bw, fl22bl, fl22bb, fl22bw, fl23bl, fl23bb, fl23bw, fl24bl, fl24bb, fl24bw, fl25bl, fl25bb, fl25bw, fl26bl, fl26bb, fl26bw, fl27bl, fl27bb, fl27bw, fl1tl, fl1tb, fl1tw, fl2tl, fl2tb, fl2tw, fl3tl, fl3tb, fl3tw, fl4tl, fl4tb, fl4tw, fl5tl, fl5tb, fl5tw, fl6tl, fl6tb, fl6tw, fl7tl, fl7tb, fl7tw, fl8tl, fl8tb, fl8tw, fl9tl, fl9tb, fl9tw, fl10tl, fl10tb, fl10tw, fl11tl, fl11tb, fl11tw, fl12tl, fl12tb, fl12tw, fl13tl, fl13tb, fl13tw, fl14tl, fl14tb, fl14tw, fl15tl, fl15tb, fl15tw, fl16tl, fl16tb, fl16tw, fl17tl, fl17tb, fl17tw, fl18tl, fl18tb, fl18tw, fl19tl, fl19tb, fl19tw, fl20tl, fl20tb, fl20tw, fl21tl, fl21tb, fl21tw, fl22tl, fl22tb, fl22tw, fl23tl, fl23tb, fl23tw, fl24tl, fl24tb, fl24tw, fl25tl, fl25tb, fl25tw, fl26tl, fl26tb, fl26tw, fl27tl, fl27tb, fl27tw, ga1tl, ga1tb, ga1tw, ga2tl, ga2tb, ga2tw, ga3tl, ga3tb, ga3tw, ga4tl, ga4tb, ga4tw, ga5tl, ga5tb, ga5tw, ga6tl, ga6tb, ga6tw, ga7tl, ga7tb, ga7tw, ga8tl, ga8tb, ga8tw, ga9tl, ga9tb, ga9tw, ga10tl, ga10tb, ga10tw, ga11tl, ga11tb, ga11tw, ga12tl, ga12tb, ga12tw, ga13tl, ga13tb, ga13tw, ga14tl, ga14tb, ga14tw, ga1bl, ga1bb, ga1bw, ga2bl, ga2bb, ga2bw, ga3bl, ga3bb, ga3bw, ga4bl, ga4bb, ga4bw, ga5bl, ga5bb, ga5bw, ga6bl, ga6bb, ga6bw, ga7bl, ga7bb, ga7bw, ga8bl, ga8bb, ga8bw, ga9bl, ga9bb, ga9bw, ga10bl, ga10bb, ga10bw, ga11bl, ga11bb, ga11bw, ga12bl, ga12bb, ga12bw, ga13bl, ga13bb, ga13bw, ga14bl, ga14bb, ga14bw, hi1tl, hi1tb, hi1tw, hi2tl, hi2tb, hi2tw, hi1bl, hi1bb, hi1bw, hi2bl, hi2bb, hi2bw, id1tl, id1tb, id1tw, id2tl, id2tb, id2tw, id1bl, id1bb, id1bw, id2bl, id2bb, id2bw, il1bl, il1bb, il1bw, il2bl, il2bb, il2bw, il3bl, il3bb, il3bw, il4bl, il4bb, il4bw, il5bl, il5bb, il5bw, il6bl, il6bb, il6bw, il7bl, il7bb, il7bw, il8bl, il8bb, il8bw, il9bl, il9bb, il9bw, il10bl, il10bb, il10bw, il11bl, il11bb, il11bw, il12bl, il12bb, il12bw, il13bl, il13bb, il13bw, il14bl, il14bb, il14bw, il15bl, il15bb, il15bw, il16bl, il16bb, il16bw, il17bl, il17bb, il17bw, il18bl, il18bb, il18bw, il1tl, il1tb, il1tw, il2tl, il2tb, il2tw, il3tl, il3tb, il3tw, il4tl, il4tb, il4tw, il5tl, il5tb, il5tw, il6tl, il6tb, il6tw, il7tl, il7tb, il7tw, il8tl, il8tb, il8tw, il9tl, il9tb, il9tw, il10tl, il10tb, il10tw, il11tl, il11tb, il11tw, il12tl, il12tb, il12tw, il13tl, il13tb, il13tw, il14tl, il14tb, il14tw, il15tl, il15tb, il15tw, il16tl, il16tb, il16tw, il17tl, il17tb, il17tw, il18tl, il18tb, il18tw, in1tl, in1tb, in1tw, in2tl, in2tb, in2tw, in3tl, in3tb, in3tw, in4tl, in4tb, in4tw, in5tl, in5tb, in5tw, in6tl, in6tb, in6tw, in7tl, in7tb, in7tw, in8tl, in8tb, in8tw, in9tl, in9tb, in9tw, in1bl, in1bb, in1bw, in2bl, in2bb, in2bw, in3bl, in3bb, in3bw, in4bl, in4bb, in4bw, in5bl, in5bb, in5bw, in6bl, in6bb, in6bw, in7bl, in7bb, in7bw, in8bl, in8bb, in8bw, in9bl, in9bb, in9bw, ia1tl, ia1tb, ia1tw, ia2tl, ia2tb, ia2tw, ia3tl, ia3tb, ia3tw, ia4tl, ia4tb, ia4tw, ia1bl, ia1bb, ia1bw, ia2bl, ia2bb, ia2bw, ia3bl, ia3bb, ia3bw, ia4bl, ia4bb, ia4bw, ks1tl, ks1tb, ks1tw, ks2tl, ks2tb, ks2tw, ks3tl, ks3tb, ks3tw, ks4tl, ks4tb, ks4tw, ks1bl, ks1bb, ks1bw, ks2bl, ks2bb, ks2bw, ks3bl, ks3bb, ks3bw, ks4bl, ks4bb, ks4bw, ky1tl, ky1tb, ky1tw, ky2tl, ky2tb, ky2tw, ky3tl, ky3tb, ky3tw, ky4tl, ky4tb, ky4tw, ky5tl, ky5tb, ky5tw, ky6tl, ky6tb, ky6tw, ky1bl, ky1bb, ky1bw, ky2bl, ky2bb, ky2bw, ky3bl, ky3bb, ky3bw, ky4bl, ky4bb, ky4bw, ky5bl, ky5bb, ky5bw, ky6bl, ky6bb, ky6bw, la1tl, la1tb, la1tw, la2tl, la2tb, la2tw, la3tl, la3tb, la3tw, la4tl, la4tb, la4tw, la5tl, la5tb, la5tw, la6tl, la6tb, la6tw, la1bl, la1bb, la1bw, la2bl, la2bb, la2bw, la3bl, la3bb, la3bw, la4bl, la4bb, la4bw, la5bl, la5bb, la5bw, la6bl, la6bb, la6bw, me1tl, me1tb, me1tw, me2tl, me2tb, me2tw, me1bl, me1bb, me1bw, me2bl, me2bb, me2bw, md1tl, md1tb, md1tw, md2tl, md2tb, md2tw, md3tl, md3tb, md3tw, md4tl, md4tb, md4tw, md5tl, md5tb, md5tw, md6tl, md6tb, md6tw, md7tl, md7tb, md7tw, md8tl, md8tb, md8tw, md1bl, md1bb, md1bw, md2bl, md2bb, md2bw, md3bl, md3bb, md3bw, md4bl, md4bb, md4bw, md5bl, md5bb, md5bw, md6bl, md6bb, md6bw, md7bl, md7bb, md7bw, md8bl, md8bb, md8bw, ma1tl, ma1tb, ma1tw, ma2tl, ma2tb, ma2tw, ma3tl, ma3tb, ma3tw, ma4tl, ma4tb, ma4tw, ma5tl, ma5tb, ma5tw, ma6tl, ma6tb, ma6tw, ma7tl, ma7tb, ma7tw, ma8tl, ma8tb, ma8tw, ma9tl, ma9tb, ma9tw, ma1bl, ma1bb, ma1bw, ma2bl, ma2bb, ma2bw, ma3bl, ma3bb, ma3bw, ma4bl, ma4bb, ma4bw, ma5bl, ma5bb, ma5bw, ma6bl, ma6bb, ma6bw, ma7bl, ma7bb, ma7bw, ma8bl, ma8bb, ma8bw, ma9bl, ma9bb, ma9bw, mi1bl, mi1bb, mi1bw, mi2bl, mi2bb, mi2bw, mi3bl, mi3bb, mi3bw, mi4bl, mi4bb, mi4bw, mi5bl, mi5bb, mi5bw, mi6bl, mi6bb, mi6bw, mi7bl, mi7bb, mi7bw, mi8bl, mi8bb, mi8bw, mi9bl, mi9bb, mi9bw, mi10bl, mi10bb, mi10bw, mi11bl, mi11bb, mi11bw, mi12bl, mi12bb, mi12bw, mi13bl, mi13bb, mi13bw, mi14bl, mi14bb, mi14bw, mi1tl, mi1tb, mi1tw, mi2tl, mi2tb, mi2tw, mi3tl, mi3tb, mi3tw, mi4tl, mi4tb, mi4tw, mi5tl, mi5tb, mi5tw, mi6tl, mi6tb, mi6tw, mi7tl, mi7tb, mi7tw, mi8tl, mi8tb, mi8tw, mi9tl, mi9tb, mi9tw, mi10tl, mi10tb, mi10tw, mi11tl, mi11tb, mi11tw, mi12tl, mi12tb, mi12tw, mi13tl, mi13tb, mi13tw, mi14tl, mi14tb, mi14tw, mn1tl, mn1tb, mn1tw, mn2tl, mn2tb, mn2tw, mn3tl, mn3tb, mn3tw, mn4tl, mn4tb, mn4tw, mn5tl, mn5tb, mn5tw, mn6tl, mn6tb, mn6tw, mn7tl, mn7tb, mn7tw, mn8tl, mn8tb, mn8tw, mn1bl, mn1bb, mn1bw, mn2bl, mn2bb, mn2bw, mn3bl, mn3bb, mn3bw, mn4bl, mn4bb, mn4bw, mn5bl, mn5bb, mn5bw, mn6bl, mn6bb, mn6bw, mn7bl, mn7bb, mn7bw, mn8bl, mn8bb, mn8bw, ms1tl, ms1tb, ms1tw, ms2tl, ms2tb, ms2tw, ms3tl, ms3tb, ms3tw, ms4tl, ms4tb, ms4tw, ms1bl, ms1bb, ms1bw, ms2bl, ms2bb, ms2bw, ms3bl, ms3bb, ms3bw, ms4bl, ms4bb, ms4bw, mo1tl, mo1tb, mo1tw, mo2tl, mo2tb, mo2tw, mo3tl, mo3tb, mo3tw, mo4tl, mo4tb, mo4tw, mo5tl, mo5tb, mo5tw, mo6tl, mo6tb, mo6tw, mo7tl, mo7tb, mo7tw, mo8tl, mo8tb, mo8tw, mo1bl, mo1bb, mo1bw, mo2bl, mo2bb, mo2bw, mo3bl, mo3bb, mo3bw, mo4bl, mo4bb, mo4bw, mo5bl, mo5bb, mo5bw, mo6bl, mo6bb, mo6bw, mo7bl, mo7bb, mo7bw, mo8bl, mo8bb, mo8bw, mt1tl, mt1tb, mt1tw, mt1bl, mt1bb, mt1bw, ne1tl, ne1tb, ne1tw, ne2tl, ne2tb, ne2tw, ne3tl, ne3tb, ne3tw, ne1bl, ne1bb, ne1bw, ne2bl, ne2bb, ne2bw, ne3bl, ne3bb, ne3bw, nv1tl, nv1tb, nv1tw, nv2tl, nv2tb, nv2tw, nv3tl, nv3tb, nv3tw, nv4tl, nv4tb, nv4tw, nv1bl, nv1bb, nv1bw, nv2bl, nv2bb, nv2bw, nv3bl, nv3bb, nv3bw, nv4bl, nv4bb, nv4bw, nh1tl, nh1tb, nh1tw, nh2tl, nh2tb, nh2tw, nh1bl, nh1bb, nh1bw, nh2bl, nh2bb, nh2bw, nj1bl, nj1bb, nj1bw, nj2bl, nj2bb, nj2bw, nj3bl, nj3bb, nj3bw, nj4bl, nj4bb, nj4bw, nj5bl, nj5bb, nj5bw, nj6bl, nj6bb, nj6bw, nj7bl, nj7bb, nj7bw, nj8bl, nj8bb, nj8bw, nj9bl, nj9bb, nj9bw, nj10bl, nj10bb, nj10bw, nj11bl, nj11bb, nj11bw, nj12bl, nj12bb, nj12bw, nj1tl, nj1tb, nj1tw, nj2tl, nj2tb, nj2tw, nj3tl, nj3tb, nj3tw, nj4tl, nj4tb, nj4tw, nj5tl, nj5tb, nj5tw, nj6tl, nj6tb, nj6tw, nj7tl, nj7tb, nj7tw, nj8tl, nj8tb, nj8tw, nj9tl, nj9tb, nj9tw, nj10tl, nj10tb, nj10tw, nj11tl, nj11tb, nj11tw, nj12tl, nj12tb, nj12tw, nm1tl, nm1tb, nm1tw, nm2tl, nm2tb, nm2tw, nm3tl, nm3tb, nm3tw, nm1bl, nm1bb, nm1bw, nm2bl, nm2bb, nm2bw, nm3bl, nm3bb, nm3bw, ny1tl, ny1tb, ny1tw, ny2tl, ny2tb, ny2tw, ny3tl, ny3tb, ny3tw, ny4tl, ny4tb, ny4tw, ny5tl, ny5tb, ny5tw, ny6tl, ny6tb, ny6tw, ny7tl, ny7tb, ny7tw, ny8tl, ny8tb, ny8tw, ny9tl, ny9tb, ny9tw, ny10tl, ny10tb, ny10tw, ny11tl, ny11tb, ny11tw, ny12tl, ny12tb, ny12tw, ny13tl, ny13tb, ny13tw, ny14tl, ny14tb, ny14tw, ny15tl, ny15tb, ny15tw, ny16tl, ny16tb, ny16tw, ny17tl, ny17tb, ny17tw, ny18tl, ny18tb, ny18tw, ny19tl, ny19tb, ny19tw, ny20tl, ny20tb, ny20tw, ny21tl, ny21tb, ny21tw, ny22tl, ny22tb, ny22tw, ny23tl, ny23tb, ny23tw, ny24tl, ny24tb, ny24tw, ny25tl, ny25tb, ny25tw, ny26tl, ny26tb, ny26tw, ny27tl, ny27tb, ny27tw, ny1bl, ny1bb, ny1bw, ny2bl, ny2bb, ny2bw, ny3bl, ny3bb, ny3bw, ny4bl, ny4bb, ny4bw, ny5bl, ny5bb, ny5bw, ny6bl, ny6bb, ny6bw, ny7bl, ny7bb, ny7bw, ny8bl, ny8bb, ny8bw, ny9bl, ny9bb, ny9bw, ny10bl, ny10bb, ny10bw, ny11bl, ny11bb, ny11bw, ny12bl, ny12bb, ny12bw, ny13bl, ny13bb, ny13bw, ny14bl, ny14bb, ny14bw, ny15bl, ny15bb, ny15bw, ny16bl, ny16bb, ny16bw, ny17bl, ny17bb, ny17bw, ny18bl, ny18bb, ny18bw, ny19bl, ny19bb, ny19bw, ny20bl, ny20bb, ny20bw, ny21bl, ny21bb, ny21bw, ny22bl, ny22bb, ny22bw, ny23bl, ny23bb, ny23bw, ny24bl, ny24bb, ny24bw, ny25bl, ny25bb, ny25bw, ny26bl, ny26bb, ny26bw, ny27bl, ny27bb, ny27bw, nc1bl, nc1bb, nc1bw, nc2bl, nc2bb, nc2bw, nc3bl, nc3bb, nc3bw, nc4bl, nc4bb, nc4bw, nc5bl, nc5bb, nc5bw, nc6bl, nc6bb, nc6bw, nc7bl, nc7bb, nc7bw, nc8bl, nc8bb, nc8bw, nc9bl, nc9bb, nc9bw, nc10bl, nc10bb, nc10bw, nc11bl, nc11bb, nc11bw, nc12bl, nc12bb, nc12bw, nc13bl, nc13bb, nc13bw, nc1tl, nc1tb, nc1tw, nc2tl, nc2tb, nc2tw, nc3tl, nc3tb, nc3tw, nc4tl, nc4tb, nc4tw, nc5tl, nc5tb, nc5tw, nc6tl, nc6tb, nc6tw, nc7tl, nc7tb, nc7tw, nc8tl, nc8tb, nc8tw, nc9tl, nc9tb, nc9tw, nc10tl, nc10tb, nc10tw, nc11tl, nc11tb, nc11tw, nc12tl, nc12tb, nc12tw, nc13tl, nc13tb, nc13tw, nd1tl, nd1tb, nd1tw, nd1bl, nd1bb, nd1bw, oh1bl, oh1bb, oh1bw, oh2bl, oh2bb, oh2bw, oh3bl, oh3bb, oh3bw, oh4bl, oh4bb, oh4bw, oh5bl, oh5bb, oh5bw, oh6bl, oh6bb, oh6bw, oh7bl, oh7bb, oh7bw, oh8bl, oh8bb, oh8bw, oh9bl, oh9bb, oh9bw, oh10bl, oh10bb, oh10bw, oh11bl, oh11bb, oh11bw, oh12bl, oh12bb, oh12bw, oh13bl, oh13bb, oh13bw, oh14bl, oh14bb, oh14bw, oh15bl, oh15bb, oh15bw, oh16bl, oh16bb, oh16bw, oh1tl, oh1tb, oh1tw, oh2tl, oh2tb, oh2tw, oh3tl, oh3tb, oh3tw, oh4tl, oh4tb, oh4tw, oh5tl, oh5tb, oh5tw, oh6tl, oh6tb, oh6tw, oh7tl, oh7tb, oh7tw, oh8tl, oh8tb, oh8tw, oh9tl, oh9tb, oh9tw, oh10tl, oh10tb, oh10tw, oh11tl, oh11tb, oh11tw, oh12tl, oh12tb, oh12tw, oh13tl, oh13tb, oh13tw, oh14tl, oh14tb, oh14tw, oh15tl, oh15tb, oh15tw, oh16tl, oh16tb, oh16tw, ok1tl, ok1tb, ok1tw, ok2tl, ok2tb, ok2tw, ok3tl, ok3tb, ok3tw, ok4tl, ok4tb, ok4tw, ok5tl, ok5tb, ok5tw, ok1bl, ok1bb, ok1bw, ok2bl, ok2bb, ok2bw, ok3bl, ok3bb, ok3bw, ok4bl, ok4bb, ok4bw, ok5bl, ok5bb, ok5bw, or1tl, or1tb, or1tw, or2tl, or2tb, or2tw, or3tl, or3tb, or3tw, or4tl, or4tb, or4tw, or5tl, or5tb, or5tw, or1bl, or1bb, or1bw, or2bl, or2bb, or2bw, or3bl, or3bb, or3bw, or4bl, or4bb, or4bw, or5bl, or5bb, or5bw, pa1bl, pa1bb, pa1bw, pa2bl, pa2bb, pa2bw, pa3bl, pa3bb, pa3bw, pa4bl, pa4bb, pa4bw, pa5bl, pa5bb, pa5bw, pa6bl, pa6bb, pa6bw, pa7bl, pa7bb, pa7bw, pa8bl, pa8bb, pa8bw, pa9bl, pa9bb, pa9bw, pa10bl, pa10bb, pa10bw, pa11bl, pa11bb, pa11bw, pa12bl, pa12bb, pa12bw, pa13bl, pa13bb, pa13bw, pa14bl, pa14bb, pa14bw, pa15bl, pa15bb, pa15bw, pa16bl, pa16bb, pa16bw, pa17bl, pa17bb, pa17bw, pa18bl, pa18bb, pa18bw, pa1tl, pa1tb, pa1tw, pa2tl, pa2tb, pa2tw, pa3tl, pa3tb, pa3tw, pa4tl, pa4tb, pa4tw, pa5tl, pa5tb, pa5tw, pa6tl, pa6tb, pa6tw, pa7tl, pa7tb, pa7tw, pa8tl, pa8tb, pa8tw, pa9tl, pa9tb, pa9tw, pa10tl, pa10tb, pa10tw, pa11tl, pa11tb, pa11tw, pa12tl, pa12tb, pa12tw, pa13tl, pa13tb, pa13tw, pa14tl, pa14tb, pa14tw, pa15tl, pa15tb, pa15tw, pa16tl, pa16tb, pa16tw, pa17tl, pa17tb, pa17tw, pa18tl, pa18tb, pa18tw, ri1tl, ri1tb, ri1tw, ri2tl, ri2tb, ri2tw, ri1bl, ri1bb, ri1bw, ri2bl, ri2bb, ri2bw, sc1tl, sc1tb, sc1tw, sc2tl, sc2tb, sc2tw, sc3tl, sc3tb, sc3tw, sc4tl, sc4tb, sc4tw, sc5tl, sc5tb, sc5tw, sc6tl, sc6tb, sc6tw, sc7tl, sc7tb, sc7tw, sc1bl, sc1bb, sc1bw, sc2bl, sc2bb, sc2bw, sc3bl, sc3bb, sc3bw, sc4bl, sc4bb, sc4bw, sc5bl, sc5bb, sc5bw, sc6bl, sc6bb, sc6bw, sc7bl, sc7bb, sc7bw, sd1tl, sd1tb, sd1tw, sd1bl, sd1bb, sd1bw, tn1tl, tn1tb, tn1tw, tn2tl, tn2tb, tn2tw, tn3tl, tn3tb, tn3tw, tn4tl, tn4tb, tn4tw, tn5tl, tn5tb, tn5tw, tn6tl, tn6tb, tn6tw, tn7tl, tn7tb, tn7tw, tn8tl, tn8tb, tn8tw, tn9tl, tn9tb, tn9tw, tn1bl, tn1bb, tn1bw, tn2bl, tn2bb, tn2bw, tn3bl, tn3bb, tn3bw, tn4bl, tn4bb, tn4bw, tn5bl, tn5bb, tn5bw, tn6bl, tn6bb, tn6bw, tn7bl, tn7bb, tn7bw, tn8bl, tn8bb, tn8bw, tn9bl, tn9bb, tn9bw, tx1tl, tx1tb, tx1tw, tx2tl, tx2tb, tx2tw, tx3tl, tx3tb, tx3tw, tx4tl, tx4tb, tx4tw, tx5tl, tx5tb, tx5tw, tx6tl, tx6tb, tx6tw, tx7tl, tx7tb, tx7tw, tx8tl, tx8tb, tx8tw, tx9tl, tx9tb, tx9tw, tx10tl, tx10tb, tx10tw, tx11tl, tx11tb, tx11tw, tx12tl, tx12tb, tx12tw, tx13tl, tx13tb, tx13tw, tx14tl, tx14tb, tx14tw, tx15tl, tx15tb, tx15tw, tx16tl, tx16tb, tx16tw, tx17tl, tx17tb, tx17tw, tx18tl, tx18tb, tx18tw, tx19tl, tx19tb, tx19tw, tx20tl, tx20tb, tx20tw, tx21tl, tx21tb, tx21tw, tx22tl, tx22tb, tx22tw, tx23tl, tx23tb, tx23tw, tx24tl, tx24tb, tx24tw, tx25tl, tx25tb, tx25tw, tx26tl, tx26tb, tx26tw, tx27tl, tx27tb, tx27tw, tx28tl, tx28tb, tx28tw, tx29tl, tx29tb, tx29tw, tx30tl, tx30tb, tx30tw, tx31tl, tx31tb, tx31tw, tx32tl, tx32tb, tx32tw, tx33tl, tx33tb, tx33tw, tx34tl, tx34tb, tx34tw, tx35tl, tx35tb, tx35tw, tx36tl, tx36tb, tx36tw, tx1bl, tx1bb, tx1bw, tx2bl, tx2bb, tx2bw, tx3bl, tx3bb, tx3bw, tx4bl, tx4bb, tx4bw, tx5bl, tx5bb, tx5bw, tx6bl, tx6bb, tx6bw, tx7bl, tx7bb, tx7bw, tx8bl, tx8bb, tx8bw, tx9bl, tx9bb, tx9bw, tx10bl, tx10bb, tx10bw, tx11bl, tx11bb, tx11bw, tx12bl, tx12bb, tx12bw, tx13bl, tx13bb, tx13bw, tx14bl, tx14bb, tx14bw, tx15bl, tx15bb, tx15bw, tx16bl, tx16bb, tx16bw, tx17bl, tx17bb, tx17bw, tx18bl, tx18bb, tx18bw, tx19bl, tx19bb, tx19bw, tx20bl, tx20bb, tx20bw, tx21bl, tx21bb, tx21bw, tx22bl, tx22bb, tx22bw, tx23bl, tx23bb, tx23bw, tx24bl, tx24bb, tx24bw, tx25bl, tx25bb, tx25bw, tx26bl, tx26bb, tx26bw, tx27bl, tx27bb, tx27bw, tx28bl, tx28bb, tx28bw, tx29bl, tx29bb, tx29bw, tx30bl, tx30bb, tx30bw, tx31bl, tx31bb, tx31bw, tx32bl, tx32bb, tx32bw, tx33bl, tx33bb, tx33bw, tx34bl, tx34bb, tx34bw, tx35bl, tx35bb, tx35bw, tx36bl, tx36bb, tx36bw, ut1tl, ut1tb, ut1tw, ut2tl, ut2tb, ut2tw, ut3tl, ut3tb, ut3tw, ut4tl, ut4tb, ut4tw, ut1bl, ut1bb, ut1bw, ut2bl, ut2bb, ut2bw, ut3bl, ut3bb, ut3bw, ut4bl, ut4bb, ut4bw, vt1tl, vt1tb, vt1tw, vt1bl, vt1bb, vt1bw, va1bl, va1bb, va1bw, va2bl, va2bb, va2bw, va3bl, va3bb, va3bw, va4bl, va4bb, va4bw, va5bl, va5bb, va5bw, va6bl, va6bb, va6bw, va7bl, va7bb, va7bw, va8bl, va8bb, va8bw, va9bl, va9bb, va9bw, va10bl, va10bb, va10bw, va11bl, va11bb, va11bw, va1tl, va1tb, va1tw, va2tl, va2tb, va2tw, va3tl, va3tb, va3tw, va4tl, va4tb, va4tw, va5tl, va5tb, va5tw, va6tl, va6tb, va6tw, va7tl, va7tb, va7tw, va8tl, va8tb, va8tw, va9tl, va9tb, va9tw, va10tl, va10tb, va10tw, va11tl, va11tb, va11tw, wa1bl, wa1bb, wa1bw, wa2bl, wa2bb, wa2bw, wa3bl, wa3bb, wa3bw, wa4bl, wa4bb, wa4bw, wa5bl, wa5bb, wa5bw, wa6bl, wa6bb, wa6bw, wa7bl, wa7bb, wa7bw, wa8bl, wa8bb, wa8bw, wa9bl, wa9bb, wa9bw, wa10bl, wa10bb, wa10bw, wa1tl, wa1tb, wa1tw, wa2tl, wa2tb, wa2tw, wa3tl, wa3tb, wa3tw, wa4tl, wa4tb, wa4tw, wa5tl, wa5tb, wa5tw, wa6tl, wa6tb, wa6tw, wa7tl, wa7tb, wa7tw, wa8tl, wa8tb, wa8tw, wa9tl, wa9tb, wa9tw, wa10tl, wa10tb, wa10tw, wv1tl, wv1tb, wv1tw, wv2tl, wv2tb, wv2tw, wv3tl, wv3tb, wv3tw, wv1bl, wv1bb, wv1bw, wv2bl, wv2bb, wv2bw, wv3bl, wv3bb, wv3bw, wi1tl, wi1tb, wi1tw, wi2tl, wi2tb, wi2tw, wi3tl, wi3tb, wi3tw, wi4tl, wi4tb, wi4tw, wi5tl, wi5tb, wi5tw, wi6tl, wi6tb, wi6tw, wi7tl, wi7tb, wi7tw, wi8tl, wi8tb, wi8tw, wi1bl, wi1bb, wi1bw, wi2bl, wi2bb, wi2bw, wi3bl, wi3bb, wi3bw, wi4bl, wi4bb, wi4bw, wi5bl, wi5bb, wi5bw, wi6bl, wi6bb, wi6bw, wi7bl, wi7bb, wi7bw, wi8bl, wi8bb, wi8bw, wy1tl, wy1tb, wy1tw, wy1bl, wy1bb, wy1bw = pickle.load(f)


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
    district = sortloc(["#trump2020", "#votered"], tw["user"]["location"], tw["retweeted_status"]["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            sortEthnic(mo1tl, mo1tb, mo1tw, tw)
        if("mo2" in district):
            sortEthnic(mo2tl, mo2tb, mo2tw, tw)
        if("mo3" in district):
            sortEthnic(mo3tl, mo3tb, mo3tw, tw)
        if("mo4" in district):
            sortEthnic(mo4tl, mo4tb, mo4tw, tw)
        if("mo5" in district):
            sortEthnic(mo5tl, mo5tb, mo5tw, tw)
        if("mo6" in district):
            sortEthnic(mo6tl, mo6tb, mo6tw, tw)
        if("mo7" in district):
            sortEthnic(mo7tl, mo7tb, mo7tw, tw)
        if("mo8" in district):
            sortEthnic(mo8tl, mo8tb, mo8tw, tw)
        if("sc1" in district):
            sortEthnic(sc1tl, sc1tb, sc1tw, tw)
        if("sc2" in district):
            sortEthnic(sc2tl, sc2tb, sc2tw, tw)
        if("sc3" in district):
            sortEthnic(sc3tl, sc3tb, sc3tw, tw)
        if("sc4" in district):
            sortEthnic(sc4tl, sc4tb, sc4tw, tw)
        if("sc5" in district):
            sortEthnic(sc5tl, sc5tb, sc5tw, tw)
        if("sc6" in district):
            sortEthnic(sc6tl, sc6tb, sc6tw, tw)
        if("sc7" in district):
            sortEthnic(sc7tl, sc7tb, sc7tw, tw)
        if("ky1" in district):
            sortEthnic(ky1tl, ky1tb, ky1tw, tw)
        if("ky2" in district):
            sortEthnic(ky2tl, ky2tb, ky2tw, tw)
        if("ky3" in district):
            sortEthnic(ky3tl, ky3tb, ky3tw, tw)
        if("ky4" in district):
            sortEthnic(ky4tl, ky4tb, ky4tw, tw)
        if("ky5" in district):
            sortEthnic(ky5tl, ky5tb, ky5tw, tw)
        if("ky6" in district):
            sortEthnic(ky6tl, ky6tb, ky6tw, tw)
        if("ok1" in district):
            sortEthnic(ok1tl, ok1tb, ok1tw, tw) #done
        if("ok2" in district):
            sortEthnic(ok2tl, ok2tb, ok2tw, tw)
        if("ok3" in district):
            sortEthnic(ok3tl, ok3tb, ok3tw, tw)	#done
        if("ok4" in district):
            sortEthnic(ok4tl, ok4tb, ok4tw, tw)	#done
        if("ok5" in district):
            sortEthnic(ok5tl, ok5tb, ok5tw, tw)
        if("ia1" in district):
            sortEthnic(ia1tl, ia1tb, ia1tw, tw) #done
        if("ia2" in district):
            sortEthnic(ia2tl, ia2tb, ia2tw, tw) #done
        if("ia3" in district):
            sortEthnic(ia3tl, ia3tb, ia3tw, tw)	#done
        if("ia4" in district):
            sortEthnic(ia4tl, ia4tb, ia4tw, tw)	#done
        if("ks1" in district):
            sortEthnic(ks1tl, ks1tb, ks1tw, tw) #done
        if("ks2" in district):
            sortEthnic(ks2tl, ks2tb, ks2tw, tw) #done
        if("ks3" in district):
            sortEthnic(ks3tl, ks3tb, ks3tw, tw)
        if("ks4" in district):
            sortEthnic(ks4tl, ks4tb, ks4tw, tw)
        if("ca1" in district):
            sortEthnic(ca1tl, ca1tb, ca1tw, tw) #done
        if("ca2" in district):
            sortEthnic(ca2tl, ca2tb, ca2tw, tw) #done
        if("ca3" in district):
            sortEthnic(ca3tl, ca3tb, ca3tw, tw)
        if("ca4" in district):
            sortEthnic(ca4tl, ca4tb, ca4tw, tw)
        if("ca5" in district):
            sortEthnic(ca5tl, ca5tb, ca5tw, tw) #done
        if("ca6" in district):
            sortEthnic(ca6tl, ca6tb, ca6tw, tw)
        if("ca7" in district):
            sortEthnic(ca7tl, ca7tb, ca7tw, tw) #done
        if("ca8" in district):
            sortEthnic(ca8tl, ca8tb, ca8tw, tw)
        if("ca9" in district):
            sortEthnic(ca9tl, ca9tb, ca9tw, tw) #done
        if("ca10" in district):
            sortEthnic(ca10tl, ca10tb, ca10tw, tw) #done
        if("ca11" in district):
            sortEthnic(ca11tl, ca11tb, ca11tw, tw)
        if("ca12" in district):
            sortEthnic(ca12tl, ca12tb, ca12tw, tw)
        if("ca13" in district):
            sortEthnic(ca13tl, ca13tb, ca13tw, tw)
        if("ca14" in district):
            sortEthnic(ca14tl, ca14tb, ca14tw, tw)
        if("ca15" in district):
            sortEthnic(ca15tl, ca15tb, ca15tw, tw)
        if("ca16" in district):
            sortEthnic(ca16tl, ca16tb, ca16tw, tw) #done
        if("ca17" in district):
            sortEthnic(ca17tl, ca17tb, ca17tw, tw) #done
        if("ca18" in district):
            sortEthnic(ca18tl, ca18tb, ca18tw, tw)
        if("ca19" in district):
            sortEthnic(ca19tl, ca19tb, ca19tw, tw) #done
        if("ca20" in district):
            sortEthnic(ca20tl, ca20tb, ca20tw, tw)
        if("ca21" in district):
            sortEthnic(ca21tl, ca21tb, ca21tw, tw)
        if("ca22" in district):
            sortEthnic(ca22tl, ca22tb, ca22tw, tw)
        if("ca23" in district):
            sortEthnic(ca23tl, ca23tb, ca23tw, tw)
        if("ca24" in district):
            sortEthnic(ca24tl, ca24tb, ca24tw, tw)
        if("ca25" in district):
            sortEthnic(ca25tl, ca25tb, ca25tw, tw)
        if("ca26" in district):
            sortEthnic(ca26tl, ca26tb, ca26tw, tw) #done
        if("ca27" in district):
            sortEthnic(ca27tl, ca27tb, ca27tw, tw)
        if("ca28" in district):
            sortEthnic(ca28tl, ca28tb, ca28tw, tw)
        if("ca29" in district):
            sortEthnic(ca29tl, ca29tb, ca29tw, tw)
        if("ca30" in district):
            sortEthnic(ca30tl, ca30tb, ca30tw, tw)
        if("ca31" in district):
            sortEthnic(ca31tl, ca31tb, ca31tw, tw) #done
        if("ca32" in district):
            sortEthnic(ca32tl, ca32tb, ca32tw, tw) #done
        if("ca33" in district):
            sortEthnic(ca33tl, ca33tb, ca33tw, tw)
        if("ca34" in district):
            sortEthnic(ca34tl, ca34tb, ca34tw, tw)
        if("ca35" in district):
            sortEthnic(ca35tl, ca35tb, ca35tw, tw) #done
        if("ca36" in district):
            sortEthnic(ca36tl, ca36tb, ca36tw, tw)
        if("ca37" in district):
            sortEthnic(ca37tl, ca37tb, ca37tw, tw) #done
        if("ca38" in district):
            sortEthnic(ca38tl, ca38tb, ca38tw, tw) #done
        if("ca39" in district):
            sortEthnic(ca39tl, ca39tb, ca39tw, tw)
        if("ca40" in district):
            sortEthnic(ca40tl, ca40tb, ca40tw, tw) #done
        if("ca41" in district):
            sortEthnic(ca41tl, ca41tb, ca41tw, tw) #done
        if("ca42" in district):
            sortEthnic(ca42tl, ca42tb, ca42tw, tw)
        if("ca43" in district):
            sortEthnic(ca43tl, ca43tb, ca43tw, tw)
        if("ca44" in district):
            sortEthnic(ca44tl, ca44tb, ca44tw, tw)
        if("ca45" in district):
            sortEthnic(ca45tl, ca45tb, ca45tw, tw)
        if("ca46" in district):
            sortEthnic(ca46tl, ca46tb, ca46tw, tw) #done
        if("ca47" in district):
            sortEthnic(ca47tl, ca47tb, ca47tw, tw)
        if("ca48" in district):
            sortEthnic(ca48tl, ca48tb, ca48tw, tw) #done
        if("ca49" in district):
            sortEthnic(ca49tl, ca49tb, ca49tw, tw) #done
        if("ca50" in district):
            sortEthnic(ca50tl, ca50tb, ca50tw, tw)
        if("ca51" in district):
            sortEthnic(ca51tl, ca51tb, ca51tw, tw) #done
        if("ca52" in district):
            sortEthnic(ca52tl, ca52tb, ca52tw, tw) #done
        if("ca53" in district):
            sortEthnic(ca53tl, ca53tb, ca53tw, tw) #done
        if("la1" in district):
            sortEthnic(la1tl, la1tb, la1tw, tw)
        if("la2" in district):
            sortEthnic(la2tl, la2tb, la2tw, tw) #done
        if("la3" in district):
            sortEthnic(la3tl, la3tb, la3tw, tw)
        if("la4" in district):
            sortEthnic(la4tl, la4tb, la4tw, tw)
        if("la5" in district):
            sortEthnic(la5tl, la5tb, la5tw, tw)
        if("la6" in district):
            sortEthnic(la6tl, la6tb, la6tw, tw)
        if("ct1" in district):
            sortEthnic(ct1tl, ct1tb, ct1tw, tw)
        if("ct2" in district):
            sortEthnic(ct2tl, ct2tb, ct2tw, tw) #done
        if("ct3" in district):
            sortEthnic(ct3tl, ct3tb, ct3tw, tw)
        if("ct4" in district):
            sortEthnic(ct4tl, ct4tb, ct4tw, tw)	 #done
        if("ct5" in district):
            sortEthnic(ct5tl, ct5tb, ct5tw, tw)
        if("mt1" in district):
            sortEthnic(mt1tl, mt1tb, mt1tw, tw) #done
        if("ms1" in district):
            sortEthnic(ms1tl, ms1tb, ms1tw, tw) #done
        if("ms2" in district):
            sortEthnic(ms2tl, ms2tb, ms2tw, tw)
        if("ms3" in district):
            sortEthnic(ms3tl, ms3tb, ms3tw, tw)
        if("ms4" in district):
            sortEthnic(ms4tl, ms4tb, ms4tw, tw)
        if("pa1" in district):
            sortEthnic(pa1tl, pa1tb, pa1tw, tw)
        if("pa2" in district):
            sortEthnic(pa2tl, pa2tb, pa2tw, tw) #done
        if("pa3" in district):
            sortEthnic(pa3tl, pa3tb, pa3tw, tw)	#done
        if("pa4" in district):
            sortEthnic(pa4tl, pa4tb, pa4tw, tw)	#done
        if("pa5" in district):
            sortEthnic(pa5tl, pa5tb, pa5tw, tw) #done
        if("pa6" in district):
            sortEthnic(pa6tl, pa6tb, pa6tw, tw)
        if("pa7" in district):
            sortEthnic(pa7tl, pa7tb, pa7tw, tw) #done
        if("pa8" in district):
            sortEthnic(pa8tl, pa8tb, pa8tw, tw) #done
        if("pa9" in district):
            sortEthnic(pa9tl, pa9tb, pa9tw, tw)
        if("pa10" in district):
            sortEthnic(pa10tl, pa10tb, pa10tw, tw) #done
        if("pa11" in district):
            sortEthnic(pa11tl, pa11tb, pa11tw, tw)
        if("pa12" in district):
            sortEthnic(pa12tl, pa12tb, pa12tw, tw) #done
        if("pa13" in district):
            sortEthnic(pa13tl, pa13tb, pa13tw, tw) #done
        if("pa14" in district):
            sortEthnic(pa14tl, pa14tb, pa14tw, tw)
        if("pa15" in district):
            sortEthnic(pa15tl, pa15tb, pa15tw, tw) #done
        if("pa16" in district):
            sortEthnic(pa16tl, pa16tb, pa16tw, tw) #done
        if("pa17" in district):
            sortEthnic(pa17tl, pa17tb, pa17tw, tw) #done
        if("pa18" in district):
            sortEthnic(pa18tl, pa18tb, pa18tw, tw) #done
        if("oh1" in district):
            sortEthnic(oh1tl, oh1tb, oh1tw, tw)
        if("oh2" in district):
            sortEthnic(oh2tl, oh2tb, oh2tw, tw)
        if("oh3" in district):
            sortEthnic(oh3tl, oh3tb, oh3tw, tw)
        if("oh4" in district):
            sortEthnic(oh4tl, oh4tb, oh4tw, tw)
        if("oh5" in district):
            sortEthnic(oh5tl, oh5tb, oh5tw, tw)
        if("oh6" in district):
            sortEthnic(oh6tl, oh6tb, oh6tw, tw)
        if("oh7" in district):
            sortEthnic(oh7tl, oh7tb, oh7tw, tw)
        if("oh8" in district):
            sortEthnic(oh8tl, oh8tb, oh8tw, tw)
        if("oh9" in district):
            sortEthnic(oh9tl, oh9tb, oh9tw, tw)
        if("oh10" in district):
            sortEthnic(oh10tl, oh10tb, oh10tw, tw)
        if("oh11" in district):
            sortEthnic(oh11tl, oh11tb, oh11tw, tw)
        if("oh12" in district):
            sortEthnic(oh12tl, oh12tb, oh12tw, tw)
        if("oh13" in district):
            sortEthnic(oh13tl, oh13tb, oh13tw, tw)
        if("oh14" in district):
            sortEthnic(oh14tl, oh14tb, oh14tw, tw)
        if("oh15" in district):
            sortEthnic(oh15tl, oh15tb, oh15tw, tw)
        if("oh16" in district):
            sortEthnic(oh16tl, oh16tb, oh16tw, tw)
        if("fl1" in district):
            sortEthnic(fl1tl, fl1tb, fl1tw, tw)
        if("fl2" in district):
            sortEthnic(fl2tl, fl2tb, fl2tw, tw)
        if("fl3" in district):
            sortEthnic(fl3tl, fl3tb, fl3tw, tw)
        if("fl4" in district):
            sortEthnic(fl4tl, fl4tb, fl4tw, tw)
        if("fl5" in district):
            sortEthnic(fl5tl, fl5tb, fl5tw, tw) #done
        if("fl6" in district):
            sortEthnic(fl6tl, fl6tb, fl6tw, tw)
        if("fl7" in district):
            sortEthnic(fl7tl, fl7tb, fl7tw, tw)
        if("fl8" in district):
            sortEthnic(fl8tl, fl8tb, fl8tw, tw)
        if("fl9" in district):
            sortEthnic(fl9tl, fl9tb, fl9tw, tw)
        if("fl10" in district):
            sortEthnic(fl10tl, fl10tb, fl10tw, tw)
        if("fl11" in district):
            sortEthnic(fl11tl, fl11tb, fl11tw, tw)
        if("fl12" in district):
            sortEthnic(fl12tl, fl12tb, fl12tw, tw)
        if("fl13" in district):
            sortEthnic(fl13tl, fl13tb, fl13tw, tw)
        if("fl14" in district):
            sortEthnic(fl14tl, fl14tb, fl14tw, tw)
        if("fl15" in district):
            sortEthnic(fl15tl, fl15tb, fl15tw, tw)
        if("fl16" in district):
            sortEthnic(fl16tl, fl16tb, fl16tw, tw)
        if("fl17" in district):
            sortEthnic(fl17tl, fl17tb, fl17tw, tw)
        if("fl18" in district):
            sortEthnic(fl18tl, fl18tb, fl18tw, tw)
        if("fl19" in district):
            sortEthnic(fl19tl, fl19tb, fl19tw, tw)
        if("fl20" in district):
            sortEthnic(fl20tl, fl20tb, fl20tw, tw)
        if("fl21" in district):
            sortEthnic(fl21tl, fl21tb, fl21tw, tw) #done
        if("fl22" in district):
            sortEthnic(fl22tl, fl22tb, fl22tw, tw)
        if("fl23" in district):
            sortEthnic(fl23tl, fl23tb, fl23tw, tw)
        if("fl24" in district):
            sortEthnic(fl24tl, fl24tb, fl24tw, tw)
        if("fl25" in district):
            sortEthnic(fl25tl, fl25tb, fl25tw, tw) #done
        if("fl26" in district):
            sortEthnic(fl26tl, fl26tb, fl26tw, tw) #done
        if("fl27" in district):
            sortEthnic(fl27tl, fl27tb, fl27tw, tw)
        if("wa1" in district):
            sortEthnic(wa1tl, wa1tb, wa1tw, tw)
        if("wa2" in district):
            sortEthnic(wa2tl, wa2tb, wa2tw, tw)
        if("wa3" in district):
            sortEthnic(wa3tl, wa3tb, wa3tw, tw)
        if("wa4" in district):
            sortEthnic(wa4tl, wa4tb, wa4tw, tw)
        if("wa5" in district):
            sortEthnic(wa5tl, wa5tb, wa5tw, tw)
        if("wa6" in district):
            sortEthnic(wa6tl, wa6tb, wa6tw, tw)
        if("wa7" in district):
            sortEthnic(wa7tl, wa7tb, wa7tw, tw)
        if("wa8" in district):
            sortEthnic(wa8tl, wa8tb, wa8tw, tw)
        if("wa9" in district):
            sortEthnic(wa9tl, wa9tb, wa9tw, tw)
        if("wa10" in district):
            sortEthnic(wa10tl, wa10tb, wa10tw, tw)
        if("hi1" in district):
            sortEthnic(hi1tl, hi1tb, hi1tw, tw) #done
        if("hi2" in district):
            sortEthnic(hi2tl, hi2tb, hi2tw, tw) #done
        if("nj1" in district):
            sortEthnic(nj1tl, nj1tb, nj1tw, tw) #done
        if("nj2" in district):
            sortEthnic(nj2tl, nj2tb, nj2tw, tw) #done
        if("nj3" in district):
            sortEthnic(nj3tl, nj3tb, nj3tw, tw)	#done
        if("nj4" in district):
            sortEthnic(nj4tl, nj4tb, nj4tw, tw)	#done
        if("nj5" in district):
            sortEthnic(nj5tl, nj5tb, nj5tw, tw) #done
        if("nj6" in district):
            sortEthnic(nj6tl, nj6tb, nj6tw, tw) #done
        if("nj7" in district):
            sortEthnic(nj7tl, nj7tb, nj7tw, tw) #done
        if("nj8" in district):
            sortEthnic(nj8tl, nj8tb, nj8tw, tw) #done
        if("nj9" in district):
            sortEthnic(nj9tl, nj9tb, nj9tw, tw) #done
        if("nj10" in district):
            sortEthnic(nj10tl, nj10tb, nj10tw, tw) #done
        if("nj11" in district):
            sortEthnic(nj11tl, nj11tb, nj11tw, tw) #done
        if("nj12" in district):
            sortEthnic(nj12tl, nj12tb, nj12tw, tw) #done
        if("ny1" in district):
            sortEthnic(ny1tl, ny1tb, ny1tw, tw) #done
        if("ny2" in district):
            sortEthnic(ny2tl, ny2tb, ny2tw, tw) #done
        if("ny3" in district):
            sortEthnic(ny3tl, ny3tb, ny3tw, tw)
        if("ny4" in district):
            sortEthnic(ny4tl, ny4tb, ny4tw, tw)
        if("ny5" in district):
            sortEthnic(ny5tl, ny5tb, ny5tw, tw)
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            sortEthnic(ny6tl, ny6tb, ny6tw, tw)
            sortEthnic(ny7tl, ny7tb, ny7tw, tw)
            sortEthnic(ny8tl, ny8tb, ny8tw, tw)
            sortEthnic(ny9tl, ny9tb, ny9tw, tw)
            sortEthnic(ny10tl, ny10tb, ny10tw, tw)
            sortEthnic(ny11tl, ny11tb, ny11tw, tw)
            sortEthnic(ny12tl, ny12tb, ny12tw, tw)
            sortEthnic(ny13tl, ny13tb, ny13tw, tw)
            sortEthnic(ny14tl, ny14tb, ny14tw, tw)
            sortEthnic(ny15tl, ny15tb, ny15tw, tw)
        if("ny16" in district):
            sortEthnic(ny16tl, ny16tb, ny16tw, tw)
        if("ny17" in district):
            sortEthnic(ny17tl, ny17tb, ny17tw, tw) #done
        if("ny18" in district):
            sortEthnic(ny18tl, ny18tb, ny18tw, tw)
        if("ny19" in district):
            sortEthnic(ny19tl, ny19tb, ny19tw, tw) #done
        if("ny20" in district):
            sortEthnic(ny20tl, ny20tb, ny20tw, tw)
        if("ny21" in district):
            sortEthnic(ny21tl, ny21tb, ny21tw, tw) #done
        if("ny22" in district):
            sortEthnic(ny22tl, ny22tb, ny22tw, tw) #done
        if("ny23" in district):
            sortEthnic(ny23tl, ny23tb, ny23tw, tw)
        if("ny24" in district):
            sortEthnic(ny24tl, ny24tb, ny24tw, tw)
        if("ny25" in district):
            sortEthnic(ny25tl, ny25tb, ny25tw, tw)
        if("ny26" in district):
            sortEthnic(ny26tl, ny26tb, ny26tw, tw)
        if("ny27" in district):
            sortEthnic(ny27tl, ny27tb, ny27tw, tw) #done
        if("ri1" in district):
            sortEthnic(ri1tl, ri1tb, ri1tw, tw)	#done
        if("ri2" in district):
            sortEthnic(ri2tl, ri2tb, ri2tw, tw)
        if("mn1" in district):
            sortEthnic(mn1tl, mn1tb, mn1tw, tw) #done
        if("mn2" in district):
            sortEthnic(mn2tl, mn2tb, mn2tw, tw)
        if("mn3" in district):
            sortEthnic(mn3tl, mn3tb, mn3tw, tw)	#done
        if("mn4" in district):
            sortEthnic(mn4tl, mn4tb, mn4tw, tw)
        if("mn5" in district):
            sortEthnic(mn5tl, mn5tb, mn5tw, tw) #done
        if("mn6" in district):
            sortEthnic(mn6tl, mn6tb, mn6tw, tw) #done
        if("mn7" in district):
            sortEthnic(mn7tl, mn7tb, mn7tw, tw) #done
        if("mn8" in district):
            sortEthnic(mn8tl, mn8tb, mn8tw, tw)
        if("mi1" in district):
            sortEthnic(mi1tl, mi1tb, mi1tw, tw)
        if("mi2" in district):
            sortEthnic(mi2tl, mi2tb, mi2tw, tw) #done
        if("mi3" in district):
            sortEthnic(mi3tl, mi3tb, mi3tw, tw)
        if("mi4" in district):
            sortEthnic(mi4tl, mi4tb, mi4tw, tw)	#done
        if("mi5" in district):
            sortEthnic(mi5tl, mi5tb, mi5tw, tw) #done
        if("mi6" in district):
            sortEthnic(mi6tl, mi6tb, mi6tw, tw)
        if("mi7" in district):
            sortEthnic(mi7tl, mi7tb, mi7tw, tw)
        if("mi8" in district):
            sortEthnic(mi8tl, mi8tb, mi8tw, tw)
        if("mi9" in district):
            sortEthnic(mi9tl, mi9tb, mi9tw, tw) #done
        if("mi10" in district):
            sortEthnic(mi10tl, mi10tb, mi10tw, tw) #done
        if("mi11" in district):
            sortEthnic(mi11tl, mi11tb, mi11tw, tw)
        if("mi12" in district):
            sortEthnic(mi12tl, mi12tb, mi12tw, tw)
        if("mi13" in district):
            sortEthnic(mi13tl, mi13tb, mi13tw, tw) #done
        if("mi14" in district):
            sortEthnic(mi14tl, mi14tb, mi14tw, tw) #done
        if("wi1" in district):
            sortEthnic(wi1tl, wi1tb, wi1tw, tw)
        if("wi2" in district):
            sortEthnic(wi2tl, wi2tb, wi2tw, tw)
        if("wi3" in district):
            sortEthnic(wi3tl, wi3tb, wi3tw, tw)	#done
        if("wi4" in district):
            sortEthnic(wi4tl, wi4tb, wi4tw, tw)
        if("wi5" in district):
            sortEthnic(wi5tl, wi5tb, wi5tw, tw) #done
        if("wi6" in district):
            sortEthnic(wi6tl, wi6tb, wi6tw, tw)
        if("wi7" in district):
            sortEthnic(wi7tl, wi7tb, wi7tw, tw) #done
        if("wi8" in district):
            sortEthnic(wi8tl, wi8tb, wi8tw, tw)
        if("or1" in district):
            sortEthnic(or1tl, or1tb, or1tw, tw)
        if("or2" in district):
            sortEthnic(or2tl, or2tb, or2tw, tw) #done
        if("or3" in district):
            sortEthnic(or3tl, or3tb, or3tw, tw)
        if("or4" in district):
            sortEthnic(or4tl, or4tb, or4tw, tw)
        if("or5" in district):
            sortEthnic(or5tl, or5tb, or5tw, tw)
        if("md1" in district):
            sortEthnic(md1tl, md1tb, md1tw, tw) #done
        if("md2" in district):
            sortEthnic(md2tl, md2tb, md2tw, tw)
        if("md3" in district):
            sortEthnic(md3tl, md3tb, md3tw, tw)	#done
        if("md4" in district):
            sortEthnic(md4tl, md4tb, md4tw, tw)	#done
        if("md5" in district):
            sortEthnic(md5tl, md5tb, md5tw, tw) #done
        if("md6" in district):
            sortEthnic(md6tl, md6tb, md6tw, tw) #done
        if("md7" in district):
            sortEthnic(md7tl, md7tb, md7tw, tw)
        if("md8" in district):
            sortEthnic(md8tl, md8tb, md8tw, tw)
        if("ma1" in district):
            sortEthnic(ma1tl, ma1tb, ma1tw, tw) #done
        if("ma2" in district):
            sortEthnic(ma2tl, ma2tb, ma2tw, tw)
        if("ma3" in district):
            sortEthnic(ma3tl, ma3tb, ma3tw, tw)	 #done
        if("ma4" in district):
            sortEthnic(ma4tl, ma4tb, ma4tw, tw)
        if("ma5" in district):
            sortEthnic(ma5tl, ma5tb, ma5tw, tw)
        if("ma6" in district):
            sortEthnic(ma6tl, ma6tb, ma6tw, tw)
        if("ma7" in district):
            sortEthnic(ma7tl, ma7tb, ma7tw, tw)
        if("ma8" in district):
            sortEthnic(ma8tl, ma8tb, ma8tw, tw)
        if("ma9" in district):
            sortEthnic(ma9tl, ma9tb, ma9tw, tw) #done
        if("me1" in district):
            sortEthnic(me1tl, me1tb, me1tw, tw) #done
        if("me2" in district):
            sortEthnic(me2tl, me2tb, me2tw, tw) #done
        if("id1" in district):
            sortEthnic(id1tl, id1tb, id1tw, tw) #done
        if("id2" in district):
            sortEthnic(id2tl, id2tb, id2tw, tw) #done
        if("nc1" in district):
            sortEthnic(nc1tl, nc1tb, nc1tw, tw)
        if("nc2" in district):
            sortEthnic(nc2tl, nc2tb, nc2tw, tw)
        if("nc3" in district):
            sortEthnic(nc3tl, nc3tb, nc3tw, tw)
        if("nc4" in district):
            sortEthnic(nc4tl, nc4tb, nc4tw, tw)
        if("nc5" in district):
            sortEthnic(nc5tl, nc5tb, nc5tw, tw)
        if("nc6" in district):
            sortEthnic(nc6tl, nc6tb, nc6tw, tw)
        if("nc7" in district):
            sortEthnic(nc7tl, nc7tb, nc7tw, tw)
        if("nc8" in district):
            sortEthnic(nc8tl, nc8tb, nc8tw, tw) #done
        if("nc9" in district):
            sortEthnic(nc9tl, nc9tb, nc9tw, tw)
        if("nc10" in district):
            sortEthnic(nc10tl, nc10tb, nc10tw, tw)
        if("nc11" in district):
            sortEthnic(nc11tl, nc11tb, nc11tw, tw)
        if("nc12" in district):
            sortEthnic(nc12tl, nc12tb, nc12tw, tw)
        if("nc13" in district):
            sortEthnic(nc13tl, nc13tb, nc13tw, tw)
        if("nh1" in district):
            sortEthnic(nh1tl, nh1tb, nh1tw, tw) #done
        if("nh2" in district):
            sortEthnic(nh2tl, nh2tb, nh2tw, tw) #done
        if("nv1" in district):
            sortEthnic(nv1tl, nv1tb, nv1tw, tw) #done
        if("nv2" in district):
            sortEthnic(nv2tl, nv2tb, nv2tw, tw)
        if("nv3" in district):
            sortEthnic(nv3tl, nv3tb, nv3tw, tw)
        if("nv4" in district):
            sortEthnic(nv4tl, nv4tb, nv4tw, tw)
        if("co1" in district):
            sortEthnic(co1tl, co1tb, co1tw, tw)
        if("co2" in district):
            sortEthnic(co2tl, co2tb, co2tw, tw) #done
        if("co3" in district):
            sortEthnic(co3tl, co3tb, co3tw, tw)
        if("co4" in district):
            sortEthnic(co4tl, co4tb, co4tw, tw)
        if("co5" in district):
            sortEthnic(co5tl, co5tb, co5tw, tw)
        if("co6" in district):
            sortEthnic(co6tl, co6tb, co6tw, tw) #done
        if("co7" in district):
            sortEthnic(co7tl, co7tb, co7tw, tw) #done
        if("nm1" in district):
            sortEthnic(nm1tl, nm1tb, nm1tw, tw) #done
        if("nm2" in district):
            sortEthnic(nm2tl, nm2tb, nm2tw, tw)
        if("nm3" in district):
            sortEthnic(nm3tl, nm3tb, nm3tw, tw) #done
        if("az1" in district):
            sortEthnic(az1tl, az1tb, az1tw, tw)
        if("az2" in district):
            sortEthnic(az2tl, az2tb, az2tw, tw)
        if("az3" in district):
            sortEthnic(az3tl, az3tb, az3tw, tw)		#done
        if("az4" in district):
            sortEthnic(az4tl, az4tb, az4tw, tw)
        if("az5" in district):
            sortEthnic(az5tl, az5tb, az5tw, tw)
        if("az6" in district):
            sortEthnic(az6tl, az6tb, az6tw, tw) #done
        if("az7" in district):
            sortEthnic(az7tl, az7tb, az7tw, tw)		#done
        if("az8" in district):
            sortEthnic(az8tl, az8tb, az8tw, tw)
        if("az9" in district):
            sortEthnic(az9tl, az9tb, az9tw, tw)			#done
        if("ga1" in district):
            sortEthnic(ga1tl, ga1tb, ga1tw, tw)
        if("ga2" in district):
            sortEthnic(ga2tl, ga2tb, ga2tw, tw)
        if("ga3" in district):
            sortEthnic(ga3tl, ga3tb, ga3tw, tw)	#done
        if("ga4" in district):
            sortEthnic(ga4tl, ga4tb, ga4tw, tw)
        if("ga5" in district):
            sortEthnic(ga5tl, ga5tb, ga5tw, tw)
        if("ga6" in district):
            sortEthnic(ga6tl, ga6tb, ga6tw, tw)
        if("ga7" in district):
            sortEthnic(ga7tl, ga7tb, ga7tw, tw)
        if("ga8" in district):
            sortEthnic(ga8tl, ga8tb, ga8tw, tw)
        if("ga9" in district):
            sortEthnic(ga9tl, ga9tb, ga9tw, tw)
        if("ga10" in district):
            sortEthnic(ga10tl, ga10tb, ga10tw, tw)
        if("ga11" in district):
            sortEthnic(ga11tl, ga11tb, ga11tw, tw)
        if("ga12" in district):
            sortEthnic(ga12tl, ga12tb, ga12tw, tw)
        if("ga13" in district):
            sortEthnic(ga13tl, ga13tb, ga13tw, tw)
        if("ga14" in district):
            sortEthnic(ga14tl, ga14tb, ga14tw, tw)
        if("tx1" in district):
            sortEthnic(tx1tl, tx1tb, tx1tw, tw) #done
        if("tx2" in district):
            sortEthnic(tx2tl, tx2tb, tx2tw, tw)
        if("tx3" in district):
            sortEthnic(tx3tl, tx3tb, tx3tw, tw)
        if("tx4" in district):
            sortEthnic(tx4tl, tx4tb, tx4tw, tw)
        if("tx5" in district):
            sortEthnic(tx5tl, tx5tb, tx5tw, tw) #done
        if("tx6" in district):
            sortEthnic(tx6tl, tx6tb, tx6tw, tw) #done
        if("tx7" in district):
            sortEthnic(tx7tl, tx7tb, tx7tw, tw)
        if("tx8" in district):
            sortEthnic(tx8tl, tx8tb, tx8tw, tw)
        if("tx9" in district):
            sortEthnic(tx9tl, tx9tb, tx9tw, tw)
        if("tx10" in district):
            sortEthnic(tx10tl, tx10tb, tx10tw, tw) #done
        if("tx11" in district):
            sortEthnic(tx11tl, tx11tb, tx11tw, tw)
        if("tx12" in district):
            sortEthnic(tx12tl, tx12tb, tx12tw, tw)
        if("tx13" in district):
            sortEthnic(tx13tl, tx13tb, tx13tw, tw)
        if("tx14" in district):
            sortEthnic(tx14tl, tx14tb, tx14tw, tw)
        if("tx15" in district):
            sortEthnic(tx15tl, tx15tb, tx15tw, tw)
        if("tx16" in district):
            sortEthnic(tx16tl, tx16tb, tx16tw, tw)
        if("tx17" in district):
            sortEthnic(tx17tl, tx17tb, tx17tw, tw)
        if("tx18" in district):
            sortEthnic(tx18tl, tx18tb, tx18tw, tw)
        if("tx19" in district):
            sortEthnic(tx19tl, tx19tb, tx19tw, tw)
        if("tx20" in district):
            sortEthnic(tx20tl, tx20tb, tx20tw, tw)
        if("tx21" in district):
            sortEthnic(tx21tl, tx21tb, tx21tw, tw)
        if("tx22" in district):
            sortEthnic(tx22tl, tx22tb, tx22tw, tw)
        if("tx23" in district):
            sortEthnic(tx23tl, tx23tb, tx23tw, tw)
        if("tx24" in district):
            sortEthnic(tx24tl, tx24tb, tx24tw, tw) #done
        if("tx25" in district):
            sortEthnic(tx25tl, tx25tb, tx25tw, tw)
        if("tx26" in district):
            sortEthnic(tx26tl, tx26tb, tx26tw, tw)
        if("tx27" in district):
            sortEthnic(tx27tl, tx27tb, tx27tw, tw)
        if("tx28" in district):
            sortEthnic(tx28tl, tx28tb, tx28tw, tw)
        if("tx29" in district):
            sortEthnic(tx29tl, tx29tb, tx29tw, tw)
        if("tx30" in district):
            sortEthnic(tx30tl, tx30tb, tx30tw, tw)
        if("tx31" in district):
            sortEthnic(tx31tl, tx31tb, tx31tw, tw)
        if("tx32" in district):
            sortEthnic(tx32tl, tx32tb, tx32tw, tw) #done
        if("tx33" in district):
            sortEthnic(tx33tl, tx33tb, tx33tw, tw)
        if("tx34" in district):
            sortEthnic(tx34tl, tx34tb, tx34tw, tw)
        if("tx35" in district):
            sortEthnic(tx35tl, tx35tb, tx35tw, tw)
        if("tx36" in district):
            sortEthnic(tx36tl, tx36tb, tx36tw, tw)
        if("in1" in district):
            sortEthnic(in1tl, in1tb, in1tw, tw)
        if("in2" in district):
            sortEthnic(in2tl, in2tb, in2tw, tw)
        if("in3" in district):
            sortEthnic(in3tl, in3tb, in3tw, tw)	 #done
        if("in4" in district):
            sortEthnic(in4tl, in4tb, in4tw, tw)
        if("in5" in district):
            sortEthnic(in5tl, in5tb, in5tw, tw)
        if("in6" in district):
            sortEthnic(in6tl, in6tb, in6tw, tw)
        if("in7" in district):
            sortEthnic(in7tl, in7tb, in7tw, tw)
        if("in8" in district):
            sortEthnic(in8tl, in8tb, in8tw, tw)
        if("in9" in district):
            sortEthnic(in9tl, in9tb, in9tw, tw)
        if("va1" in district):
            sortEthnic(va1tl, va1tb, va1tw, tw)
        if("va2" in district):
            sortEthnic(va2tl, va2tb, va2tw, tw)
        if("va3" in district):
            sortEthnic(va3tl, va3tb, va3tw, tw)
        if("va4" in district):
            sortEthnic(va4tl, va4tb, va4tw, tw)	#done
        if("va5" in district):
            sortEthnic(va5tl, va5tb, va5tw, tw)
        if("va6" in district):
            sortEthnic(va6tl, va6tb, va6tw, tw)
        if("va7" in district):
            sortEthnic(va7tl, va7tb, va7tw, tw)
        if("va8" in district):
            sortEthnic(va8tl, va8tb, va8tw, tw)
        if("va9" in district):
            sortEthnic(va9tl, va9tb, va9tw, tw)
        if("va10" in district):
            sortEthnic(va10tl, va10tb, va10tw, tw)
        if("va11" in district):
            sortEthnic(va11tl, va11tb, va11tw, tw)
        if("il1" in district):
            sortEthnic(il1tl, il1tb, il1tw, tw)
        if("il2" in district):
            sortEthnic(il2tl, il2tb, il2tw, tw)
        if("il3" in district):
            sortEthnic(il3tl, il3tb, il3tw, tw)
        if("il4" in district):
            sortEthnic(il4tl, il4tb, il4tw, tw)	#done
        if("il5" in district):
            sortEthnic(il5tl, il5tb, il5tw, tw)
        if("il6" in district):
            sortEthnic(il6tl, il6tb, il6tw, tw)
        if("il7" in district):
            sortEthnic(il7tl, il7tb, il7tw, tw)
        if("il8" in district):
            sortEthnic(il8tl, il8tb, il8tw, tw)
        if("il9" in district):
            sortEthnic(il9tl, il9tb, il9tw, tw)
        if("il10" in district):
            sortEthnic(il10tl, il10tb, il10tw, tw) #done
        if("il11" in district):
            sortEthnic(il11tl, il11tb, il11tw, tw)
        if("il12" in district):
            sortEthnic(il12tl, il12tb, il12tw, tw) #done
        if("il13" in district):
            sortEthnic(il13tl, il13tb, il13tw, tw)
        if("il14" in district):
            sortEthnic(il14tl, il14tb, il14tw, tw)#done
        if("il15" in district):
            sortEthnic(il15tl, il15tb, il15tw, tw) #done
        if("il16" in district):
            sortEthnic(il16tl, il16tb, il16tw, tw)
        if("il17" in district):
            sortEthnic(il17tl, il17tb, il17tw, tw)
        if("il18" in district):
            sortEthnic(il18tl, il18tb, il18tw, tw)
        if("de1" in district):
            sortEthnic(de1tl, de1tb, de1tw, tw) #done
        if("vt1" in district):
            sortEthnic(vt1tl, vt1tb, vt1tw, tw) #done
        if("ut1" in district):
            sortEthnic(ut1tl, ut1tb, ut1tw, tw)
        if("ut2" in district):
            sortEthnic(ut2tl, ut2tb, ut2tw, tw)
        if("ut3" in district):
            sortEthnic(ut3tl, ut3tb, ut3tw, tw)
        if("ut4" in district):
            sortEthnic(ut4tl, ut4tb, ut4tw, tw)
        if("ne1" in district):
            sortEthnic(ne1tl, ne1tb, ne1tw, tw)
        if("ne2" in district):
            sortEthnic(ne2tl, ne2tb, ne2tw, tw)
        if("ne3" in district):
            sortEthnic(ne3tl, ne3tb, ne3tw, tw)	#done
        if("ak1" in district):
            sortEthnic(ak1tl, ak1tb, ak1tw, tw) #done
        if("wy1" in district):
            sortEthnic(wy1tl, wy1tb, wy1tw, tw) #done
        if("al1" in district):
            sortEthnic(al1tl, al1tb, al1tw, tw)
        if("al2" in district):
            sortEthnic(al2tl, al2tb, al2tw, tw)
        if("al3" in district):
            sortEthnic(al3tl, al3tb, al3tw, tw)
        if("al4" in district):
            sortEthnic(al4tl, al4tb, al4tw, tw)
        if("al5" in district):
            sortEthnic(al5tl, al5tb, al5tw, tw)
        if("al6" in district):
            sortEthnic(al6tl, al6tb, al6tw, tw)
        if("al7" in district):
            sortEthnic(al7tl, al7tb, al7tw, tw)	#done
        if("tn1" in district):
            sortEthnic(tn1tl, tn1tb, tn1tw, tw)
        if("tn2" in district):
            sortEthnic(tn2tl, tn2tb, tn2tw, tw)
        if("tn3" in district):
            sortEthnic(tn3tl, tn3tb, tn3tw, tw)
        if("tn4" in district):
            sortEthnic(tn4tl, tn4tb, tn4tw, tw)
        if("tn5" in district):
            sortEthnic(tn5tl, tn5tb, tn5tw, tw)
        if("tn6" in district):
            sortEthnic(tn6tl, tn6tb, tn6tw, tw)
        if("tn7" in district):
            sortEthnic(tn7tl, tn7tb, tn7tw, tw)
        if("tn8" in district):
            sortEthnic(tn8tl, tn8tb, tn8tw, tw)
        if("tn9" in district):
            sortEthnic(tn9tl, tn9tb, tn9tw, tw)
        if("nd1" in district):
            sortEthnic(nd1tl, nd1tb, nd1tw, tw) #done
        if("sd1" in district):
            sortEthnic(sd1tl, sd1tb, sd1tw, tw) #done
        if("wv1" in district):
            sortEthnic(wv1tl, wv1tb, wv1tw, tw)
        if("wv2" in district):
            sortEthnic(wv2tl, wv2tb, wv2tw, tw)
        if("wv3" in district):
            sortEthnic(wv3tl, wv3tb, wv3tw, tw) #done
        if("ar1" in district):
            sortEthnic(ar1tl, ar1tb, ar1tw, tw) #done
        if("ar2" in district):
            sortEthnic(ar2tl, ar2tb, ar2tw, tw)
        if("ar3" in district):
            sortEthnic(ar3tl, ar3tb, ar3tw, tw)
        if("ar4" in district):
            sortEthnic(ar4tl, ar4tb, ar4tw, tw)
    district = sortloc(["#biden2020", "#voteblue"], tw["user"]["location"], tw["retweeted_status"]["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            sortEthnic(mo1bl, mo1bb, mo1bw, tw)
        if("mo2" in district):
            sortEthnic(mo2bl, mo2bb, mo2bw, tw)
        if("mo3" in district):
            sortEthnic(mo3bl, mo3bb, mo3bw, tw)
        if("mo4" in district):
            sortEthnic(mo4bl, mo4bb, mo4bw, tw)
        if("mo5" in district):
            sortEthnic(mo5bl, mo5bb, mo5bw, tw)
        if("mo6" in district):
            sortEthnic(mo6bl, mo6bb, mo6bw, tw)
        if("mo7" in district):
            sortEthnic(mo7bl, mo7bb, mo7bw, tw)
        if("mo8" in district):
            sortEthnic(mo8bl, mo8bb, mo8bw, tw)
        if("sc1" in district):
            sortEthnic(sc1bl, sc1bb, sc1bw, tw)
        if("sc2" in district):
            sortEthnic(sc2bl, sc2bb, sc2bw, tw)
        if("sc3" in district):
            sortEthnic(sc3bl, sc3bb, sc3bw, tw)
        if("sc4" in district):
            sortEthnic(sc4bl, sc4bb, sc4bw, tw)
        if("sc5" in district):
            sortEthnic(sc5bl, sc5bb, sc5bw, tw)
        if("sc6" in district):
            sortEthnic(sc6bl, sc6bb, sc6bw, tw)
        if("sc7" in district):
            sortEthnic(sc7bl, sc7bb, sc7bw, tw)
        if("ky1" in district):
            sortEthnic(ky1bl, ky1bb, ky1bw, tw)
        if("ky2" in district):
            sortEthnic(ky2bl, ky2bb, ky2bw, tw)
        if("ky3" in district):
            sortEthnic(ky3bl, ky3bb, ky3bw, tw)
        if("ky4" in district):
            sortEthnic(ky4bl, ky4bb, ky4bw, tw)
        if("ky5" in district):
            sortEthnic(ky5bl, ky5bb, ky5bw, tw)
        if("ky6" in district):
            sortEthnic(ky6bl, ky6bb, ky6bw, tw)
        if("ok1" in district):
            sortEthnic(ok1bl, ok1bb, ok1bw, tw) #done
        if("ok2" in district):
            sortEthnic(ok2bl, ok2bb, ok2bw, tw)
        if("ok3" in district):
            sortEthnic(ok3bl, ok3bb, ok3bw, tw)	#done
        if("ok4" in district):
            sortEthnic(ok4bl, ok4bb, ok4bw, tw)	#done
        if("ok5" in district):
            sortEthnic(ok5bl, ok5bb, ok5bw, tw)
        if("ia1" in district):
            sortEthnic(ia1bl, ia1bb, ia1bw, tw) #done
        if("ia2" in district):
            sortEthnic(ia2bl, ia2bb, ia2bw, tw) #done
        if("ia3" in district):
            sortEthnic(ia3bl, ia3bb, ia3bw, tw)	#done
        if("ia4" in district):
            sortEthnic(ia4bl, ia4bb, ia4bw, tw)	#done
        if("ks1" in district):
            sortEthnic(ks1bl, ks1bb, ks1bw, tw) #done
        if("ks2" in district):
            sortEthnic(ks2bl, ks2bb, ks2bw, tw) #done
        if("ks3" in district):
            sortEthnic(ks3bl, ks3bb, ks3bw, tw)
        if("ks4" in district):
            sortEthnic(ks4bl, ks4bb, ks4bw, tw)
        if("ca1" in district):
            sortEthnic(ca1bl, ca1bb, ca1bw, tw) #done
        if("ca2" in district):
            sortEthnic(ca2bl, ca2bb, ca2bw, tw) #done
        if("ca3" in district):
            sortEthnic(ca3bl, ca3bb, ca3bw, tw)
        if("ca4" in district):
            sortEthnic(ca4bl, ca4bb, ca4bw, tw)
        if("ca5" in district):
            sortEthnic(ca5bl, ca5bb, ca5bw, tw) #done
        if("ca6" in district):
            sortEthnic(ca6bl, ca6bb, ca6bw, tw)
        if("ca7" in district):
            sortEthnic(ca7bl, ca7bb, ca7bw, tw) #done
        if("ca8" in district):
            sortEthnic(ca8bl, ca8bb, ca8bw, tw)
        if("ca9" in district):
            sortEthnic(ca9bl, ca9bb, ca9bw, tw) #done
        if("ca10" in district):
            sortEthnic(ca10bl, ca10bb, ca10bw, tw) #done
        if("ca11" in district):
            sortEthnic(ca11bl, ca11bb, ca11bw, tw)
        if("ca12" in district):
            sortEthnic(ca12bl, ca12bb, ca12bw, tw)
        if("ca13" in district):
            sortEthnic(ca13bl, ca13bb, ca13bw, tw)
        if("ca14" in district):
            sortEthnic(ca14bl, ca14bb, ca14bw, tw)
        if("ca15" in district):
            sortEthnic(ca15bl, ca15bb, ca15bw, tw)
        if("ca16" in district):
            sortEthnic(ca16bl, ca16bb, ca16bw, tw) #done
        if("ca17" in district):
            sortEthnic(ca17bl, ca17bb, ca17bw, tw) #done
        if("ca18" in district):
            sortEthnic(ca18bl, ca18bb, ca18bw, tw)
        if("ca19" in district):
            sortEthnic(ca19bl, ca19bb, ca19bw, tw) #done
        if("ca20" in district):
            sortEthnic(ca20bl, ca20bb, ca20bw, tw)
        if("ca21" in district):
            sortEthnic(ca21bl, ca21bb, ca21bw, tw)
        if("ca22" in district):
            sortEthnic(ca22bl, ca22bb, ca22bw, tw)
        if("ca23" in district):
            sortEthnic(ca23bl, ca23bb, ca23bw, tw)
        if("ca24" in district):
            sortEthnic(ca24bl, ca24bb, ca24bw, tw)
        if("ca25" in district):
            sortEthnic(ca25bl, ca25bb, ca25bw, tw)
        if("ca26" in district):
            sortEthnic(ca26bl, ca26bb, ca26bw, tw) #done
        if("ca27" in district):
            sortEthnic(ca27bl, ca27bb, ca27bw, tw)
        if("ca28" in district):
            sortEthnic(ca28bl, ca28bb, ca28bw, tw)
        if("ca29" in district):
            sortEthnic(ca29bl, ca29bb, ca29bw, tw)
        if("ca30" in district):
            sortEthnic(ca30bl, ca30bb, ca30bw, tw)
        if("ca31" in district):
            sortEthnic(ca31bl, ca31bb, ca31bw, tw) #done
        if("ca32" in district):
            sortEthnic(ca32bl, ca32bb, ca32bw, tw) #done
        if("ca33" in district):
            sortEthnic(ca33bl, ca33bb, ca33bw, tw)
        if("ca34" in district):
            sortEthnic(ca34bl, ca34bb, ca34bw, tw)
        if("ca35" in district):
            sortEthnic(ca35bl, ca35bb, ca35bw, tw) #done
        if("ca36" in district):
            sortEthnic(ca36bl, ca36bb, ca36bw, tw)
        if("ca37" in district):
            sortEthnic(ca37bl, ca37bb, ca37bw, tw) #done
        if("ca38" in district):
            sortEthnic(ca38bl, ca38bb, ca38bw, tw) #done
        if("ca39" in district):
            sortEthnic(ca39bl, ca39bb, ca39bw, tw)
        if("ca40" in district):
            sortEthnic(ca40bl, ca40bb, ca40bw, tw) #done
        if("ca41" in district):
            sortEthnic(ca41bl, ca41bb, ca41bw, tw) #done
        if("ca42" in district):
            sortEthnic(ca42bl, ca42bb, ca42bw, tw)
        if("ca43" in district):
            sortEthnic(ca43bl, ca43bb, ca43bw, tw)
        if("ca44" in district):
            sortEthnic(ca44bl, ca44bb, ca44bw, tw)
        if("ca45" in district):
            sortEthnic(ca45bl, ca45bb, ca45bw, tw)
        if("ca46" in district):
            sortEthnic(ca46bl, ca46bb, ca46bw, tw) #done
        if("ca47" in district):
            sortEthnic(ca47bl, ca47bb, ca47bw, tw)
        if("ca48" in district):
            sortEthnic(ca48bl, ca48bb, ca48bw, tw) #done
        if("ca49" in district):
            sortEthnic(ca49bl, ca49bb, ca49bw, tw) #done
        if("ca50" in district):
            sortEthnic(ca50bl, ca50bb, ca50bw, tw)
        if("ca51" in district):
            sortEthnic(ca51bl, ca51bb, ca51bw, tw) #done
        if("ca52" in district):
            sortEthnic(ca52bl, ca52bb, ca52bw, tw) #done
        if("ca53" in district):
            sortEthnic(ca53bl, ca53bb, ca53bw, tw) #done
        if("la1" in district):
            sortEthnic(la1bl, la1bb, la1bw, tw)
        if("la2" in district):
            sortEthnic(la2bl, la2bb, la2bw, tw) #done
        if("la3" in district):
            sortEthnic(la3bl, la3bb, la3bw, tw)
        if("la4" in district):
            sortEthnic(la4bl, la4bb, la4bw, tw)
        if("la5" in district):
            sortEthnic(la5bl, la5bb, la5bw, tw)
        if("la6" in district):
            sortEthnic(la6bl, la6bb, la6bw, tw)
        if("ct1" in district):
            sortEthnic(ct1bl, ct1bb, ct1bw, tw)
        if("ct2" in district):
            sortEthnic(ct2bl, ct2bb, ct2bw, tw) #done
        if("ct3" in district):
            sortEthnic(ct3bl, ct3bb, ct3bw, tw)
        if("ct4" in district):
            sortEthnic(ct4bl, ct4bb, ct4bw, tw)	 #done
        if("ct5" in district):
            sortEthnic(ct5bl, ct5bb, ct5bw, tw)
        if("mt1" in district):
            sortEthnic(mt1bl, mt1bb, mt1bw, tw) #done
        if("ms1" in district):
            sortEthnic(ms1bl, ms1bb, ms1bw, tw) #done
        if("ms2" in district):
            sortEthnic(ms2bl, ms2bb, ms2bw, tw)
        if("ms3" in district):
            sortEthnic(ms3bl, ms3bb, ms3bw, tw)
        if("ms4" in district):
            sortEthnic(ms4bl, ms4bb, ms4bw, tw)
        if("pa1" in district):
            sortEthnic(pa1bl, pa1bb, pa1bw, tw)
        if("pa2" in district):
            sortEthnic(pa2bl, pa2bb, pa2bw, tw) #done
        if("pa3" in district):
            sortEthnic(pa3bl, pa3bb, pa3bw, tw)	#done
        if("pa4" in district):
            sortEthnic(pa4bl, pa4bb, pa4bw, tw)	#done
        if("pa5" in district):
            sortEthnic(pa5bl, pa5bb, pa5bw, tw) #done
        if("pa6" in district):
            sortEthnic(pa6bl, pa6bb, pa6bw, tw)
        if("pa7" in district):
            sortEthnic(pa7bl, pa7bb, pa7bw, tw) #done
        if("pa8" in district):
            sortEthnic(pa8bl, pa8bb, pa8bw, tw) #done
        if("pa9" in district):
            sortEthnic(pa9bl, pa9bb, pa9bw, tw)
        if("pa10" in district):
            sortEthnic(pa10bl, pa10bb, pa10bw, tw) #done
        if("pa11" in district):
            sortEthnic(pa11bl, pa11bb, pa11bw, tw)
        if("pa12" in district):
            sortEthnic(pa12bl, pa12bb, pa12bw, tw) #done
        if("pa13" in district):
            sortEthnic(pa13bl, pa13bb, pa13bw, tw) #done
        if("pa14" in district):
            sortEthnic(pa14bl, pa14bb, pa14bw, tw)
        if("pa15" in district):
            sortEthnic(pa15bl, pa15bb, pa15bw, tw) #done
        if("pa16" in district):
            sortEthnic(pa16bl, pa16bb, pa16bw, tw) #done
        if("pa17" in district):
            sortEthnic(pa17bl, pa17bb, pa17bw, tw) #done
        if("pa18" in district):
            sortEthnic(pa18bl, pa18bb, pa18bw, tw) #done
        if("oh1" in district):
            sortEthnic(oh1bl, oh1bb, oh1bw, tw)
        if("oh2" in district):
            sortEthnic(oh2bl, oh2bb, oh2bw, tw)
        if("oh3" in district):
            sortEthnic(oh3bl, oh3bb, oh3bw, tw)
        if("oh4" in district):
            sortEthnic(oh4bl, oh4bb, oh4bw, tw)
        if("oh5" in district):
            sortEthnic(oh5bl, oh5bb, oh5bw, tw)
        if("oh6" in district):
            sortEthnic(oh6bl, oh6bb, oh6bw, tw)
        if("oh7" in district):
            sortEthnic(oh7bl, oh7bb, oh7bw, tw)
        if("oh8" in district):
            sortEthnic(oh8bl, oh8bb, oh8bw, tw)
        if("oh9" in district):
            sortEthnic(oh9bl, oh9bb, oh9bw, tw)
        if("oh10" in district):
            sortEthnic(oh10bl, oh10bb, oh10bw, tw)
        if("oh11" in district):
            sortEthnic(oh11bl, oh11bb, oh11bw, tw)
        if("oh12" in district):
            sortEthnic(oh12bl, oh12bb, oh12bw, tw)
        if("oh13" in district):
            sortEthnic(oh13bl, oh13bb, oh13bw, tw)
        if("oh14" in district):
            sortEthnic(oh14bl, oh14bb, oh14bw, tw)
        if("oh15" in district):
            sortEthnic(oh15bl, oh15bb, oh15bw, tw)
        if("oh16" in district):
            sortEthnic(oh16bl, oh16bb, oh16bw, tw)
        if("fl1" in district):
            sortEthnic(fl1bl, fl1bb, fl1bw, tw)
        if("fl2" in district):
            sortEthnic(fl2bl, fl2bb, fl2bw, tw)
        if("fl3" in district):
            sortEthnic(fl3bl, fl3bb, fl3bw, tw)
        if("fl4" in district):
            sortEthnic(fl4bl, fl4bb, fl4bw, tw)
        if("fl5" in district):
            sortEthnic(fl5bl, fl5bb, fl5bw, tw) #done
        if("fl6" in district):
            sortEthnic(fl6bl, fl6bb, fl6bw, tw)
        if("fl7" in district):
            sortEthnic(fl7bl, fl7bb, fl7bw, tw)
        if("fl8" in district):
            sortEthnic(fl8bl, fl8bb, fl8bw, tw)
        if("fl9" in district):
            sortEthnic(fl9bl, fl9bb, fl9bw, tw)
        if("fl10" in district):
            sortEthnic(fl10bl, fl10bb, fl10bw, tw)
        if("fl11" in district):
            sortEthnic(fl11bl, fl11bb, fl11bw, tw)
        if("fl12" in district):
            sortEthnic(fl12bl, fl12bb, fl12bw, tw)
        if("fl13" in district):
            sortEthnic(fl13bl, fl13bb, fl13bw, tw)
        if("fl14" in district):
            sortEthnic(fl14bl, fl14bb, fl14bw, tw)
        if("fl15" in district):
            sortEthnic(fl15bl, fl15bb, fl15bw, tw)
        if("fl16" in district):
            sortEthnic(fl16bl, fl16bb, fl16bw, tw)
        if("fl17" in district):
            sortEthnic(fl17bl, fl17bb, fl17bw, tw)
        if("fl18" in district):
            sortEthnic(fl18bl, fl18bb, fl18bw, tw)
        if("fl19" in district):
            sortEthnic(fl19bl, fl19bb, fl19bw, tw)
        if("fl20" in district):
            sortEthnic(fl20bl, fl20bb, fl20bw, tw)
        if("fl21" in district):
            sortEthnic(fl21bl, fl21bb, fl21bw, tw) #done
        if("fl22" in district):
            sortEthnic(fl22bl, fl22bb, fl22bw, tw)
        if("fl23" in district):
            sortEthnic(fl23bl, fl23bb, fl23bw, tw)
        if("fl24" in district):
            sortEthnic(fl24bl, fl24bb, fl24bw, tw)
        if("fl25" in district):
            sortEthnic(fl25bl, fl25bb, fl25bw, tw) #done
        if("fl26" in district):
            sortEthnic(fl26bl, fl26bb, fl26bw, tw) #done
        if("fl27" in district):
            sortEthnic(fl27bl, fl27bb, fl27bw, tw)
        if("wa1" in district):
            sortEthnic(wa1bl, wa1bb, wa1bw, tw)
        if("wa2" in district):
            sortEthnic(wa2bl, wa2bb, wa2bw, tw)
        if("wa3" in district):
            sortEthnic(wa3bl, wa3bb, wa3bw, tw)
        if("wa4" in district):
            sortEthnic(wa4bl, wa4bb, wa4bw, tw)
        if("wa5" in district):
            sortEthnic(wa5bl, wa5bb, wa5bw, tw)
        if("wa6" in district):
            sortEthnic(wa6bl, wa6bb, wa6bw, tw)
        if("wa7" in district):
            sortEthnic(wa7bl, wa7bb, wa7bw, tw)
        if("wa8" in district):
            sortEthnic(wa8bl, wa8bb, wa8bw, tw)
        if("wa9" in district):
            sortEthnic(wa9bl, wa9bb, wa9bw, tw)
        if("wa10" in district):
            sortEthnic(wa10bl, wa10bb, wa10bw, tw)
        if("hi1" in district):
            sortEthnic(hi1bl, hi1bb, hi1bw, tw) #done
        if("hi2" in district):
            sortEthnic(hi2bl, hi2bb, hi2bw, tw) #done
        if("nj1" in district):
            sortEthnic(nj1bl, nj1bb, nj1bw, tw) #done
        if("nj2" in district):
            sortEthnic(nj2bl, nj2bb, nj2bw, tw) #done
        if("nj3" in district):
            sortEthnic(nj3bl, nj3bb, nj3bw, tw)	#done
        if("nj4" in district):
            sortEthnic(nj4bl, nj4bb, nj4bw, tw)	#done
        if("nj5" in district):
            sortEthnic(nj5bl, nj5bb, nj5bw, tw) #done
        if("nj6" in district):
            sortEthnic(nj6bl, nj6bb, nj6bw, tw) #done
        if("nj7" in district):
            sortEthnic(nj7bl, nj7bb, nj7bw, tw) #done
        if("nj8" in district):
            sortEthnic(nj8bl, nj8bb, nj8bw, tw) #done
        if("nj9" in district):
            sortEthnic(nj9bl, nj9bb, nj9bw, tw) #done
        if("nj10" in district):
            sortEthnic(nj10bl, nj10bb, nj10bw, tw) #done
        if("nj11" in district):
            sortEthnic(nj11bl, nj11bb, nj11bw, tw) #done
        if("nj12" in district):
            sortEthnic(nj12bl, nj12bb, nj12bw, tw) #done
        if("ny1" in district):
            sortEthnic(ny1bl, ny1bb, ny1bw, tw) #done
        if("ny2" in district):
            sortEthnic(ny2bl, ny2bb, ny2bw, tw) #done
        if("ny3" in district):
            sortEthnic(ny3bl, ny3bb, ny3bw, tw)
        if("ny4" in district):
            sortEthnic(ny4bl, ny4bb, ny4bw, tw)
        if("ny5" in district):
            sortEthnic(ny5bl, ny5bb, ny5bw, tw)
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            sortEthnic(ny6bl, ny6bb, ny6bw, tw)
            sortEthnic(ny7bl, ny7bb, ny7bw, tw)
            sortEthnic(ny8bl, ny8bb, ny8bw, tw)
            sortEthnic(ny9bl, ny9bb, ny9bw, tw)
            sortEthnic(ny10bl, ny10bb, ny10bw, tw)
            sortEthnic(ny11bl, ny11bb, ny11bw, tw)
            sortEthnic(ny12bl, ny12bb, ny12bw, tw)
            sortEthnic(ny13bl, ny13bb, ny13bw, tw)
            sortEthnic(ny14bl, ny14bb, ny14bw, tw)
            sortEthnic(ny15bl, ny15bb, ny15bw, tw)
        if("ny16" in district):
            sortEthnic(ny16bl, ny16bb, ny16bw, tw)
        if("ny17" in district):
            sortEthnic(ny17bl, ny17bb, ny17bw, tw) #done
        if("ny18" in district):
            sortEthnic(ny18bl, ny18bb, ny18bw, tw)
        if("ny19" in district):
            sortEthnic(ny19bl, ny19bb, ny19bw, tw) #done
        if("ny20" in district):
            sortEthnic(ny20bl, ny20bb, ny20bw, tw)
        if("ny21" in district):
            sortEthnic(ny21bl, ny21bb, ny21bw, tw) #done
        if("ny22" in district):
            sortEthnic(ny22bl, ny22bb, ny22bw, tw) #done
        if("ny23" in district):
            sortEthnic(ny23bl, ny23bb, ny23bw, tw)
        if("ny24" in district):
            sortEthnic(ny24bl, ny24bb, ny24bw, tw)
        if("ny25" in district):
            sortEthnic(ny25bl, ny25bb, ny25bw, tw)
        if("ny26" in district):
            sortEthnic(ny26bl, ny26bb, ny26bw, tw)
        if("ny27" in district):
            sortEthnic(ny27bl, ny27bb, ny27bw, tw) #done
        if("ri1" in district):
            sortEthnic(ri1bl, ri1bb, ri1bw, tw)	#done
        if("ri2" in district):
            sortEthnic(ri2bl, ri2bb, ri2bw, tw)
        if("mn1" in district):
            sortEthnic(mn1bl, mn1bb, mn1bw, tw) #done
        if("mn2" in district):
            sortEthnic(mn2bl, mn2bb, mn2bw, tw)
        if("mn3" in district):
            sortEthnic(mn3bl, mn3bb, mn3bw, tw)	#done
        if("mn4" in district):
            sortEthnic(mn4bl, mn4bb, mn4bw, tw)
        if("mn5" in district):
            sortEthnic(mn5bl, mn5bb, mn5bw, tw) #done
        if("mn6" in district):
            sortEthnic(mn6bl, mn6bb, mn6bw, tw) #done
        if("mn7" in district):
            sortEthnic(mn7bl, mn7bb, mn7bw, tw) #done
        if("mn8" in district):
            sortEthnic(mn8bl, mn8bb, mn8bw, tw)
        if("mi1" in district):
            sortEthnic(mi1bl, mi1bb, mi1bw, tw)
        if("mi2" in district):
            sortEthnic(mi2bl, mi2bb, mi2bw, tw) #done
        if("mi3" in district):
            sortEthnic(mi3bl, mi3bb, mi3bw, tw)
        if("mi4" in district):
            sortEthnic(mi4bl, mi4bb, mi4bw, tw)	#done
        if("mi5" in district):
            sortEthnic(mi5bl, mi5bb, mi5bw, tw) #done
        if("mi6" in district):
            sortEthnic(mi6bl, mi6bb, mi6bw, tw)
        if("mi7" in district):
            sortEthnic(mi7bl, mi7bb, mi7bw, tw)
        if("mi8" in district):
            sortEthnic(mi8bl, mi8bb, mi8bw, tw)
        if("mi9" in district):
            sortEthnic(mi9bl, mi9bb, mi9bw, tw) #done
        if("mi10" in district):
            sortEthnic(mi10bl, mi10bb, mi10bw, tw) #done
        if("mi11" in district):
            sortEthnic(mi11bl, mi11bb, mi11bw, tw)
        if("mi12" in district):
            sortEthnic(mi12bl, mi12bb, mi12bw, tw)
        if("mi13" in district):
            sortEthnic(mi13bl, mi13bb, mi13bw, tw) #done
        if("mi14" in district):
            sortEthnic(mi14bl, mi14bb, mi14bw, tw) #done
        if("wi1" in district):
            sortEthnic(wi1bl, wi1bb, wi1bw, tw)
        if("wi2" in district):
            sortEthnic(wi2bl, wi2bb, wi2bw, tw)
        if("wi3" in district):
            sortEthnic(wi3bl, wi3bb, wi3bw, tw)	#done
        if("wi4" in district):
            sortEthnic(wi4bl, wi4bb, wi4bw, tw)
        if("wi5" in district):
            sortEthnic(wi5bl, wi5bb, wi5bw, tw) #done
        if("wi6" in district):
            sortEthnic(wi6bl, wi6bb, wi6bw, tw)
        if("wi7" in district):
            sortEthnic(wi7bl, wi7bb, wi7bw, tw) #done
        if("wi8" in district):
            sortEthnic(wi8bl, wi8bb, wi8bw, tw)
        if("or1" in district):
            sortEthnic(or1bl, or1bb, or1bw, tw)
        if("or2" in district):
            sortEthnic(or2bl, or2bb, or2bw, tw) #done
        if("or3" in district):
            sortEthnic(or3bl, or3bb, or3bw, tw)
        if("or4" in district):
            sortEthnic(or4bl, or4bb, or4bw, tw)
        if("or5" in district):
            sortEthnic(or5bl, or5bb, or5bw, tw)
        if("md1" in district):
            sortEthnic(md1bl, md1bb, md1bw, tw) #done
        if("md2" in district):
            sortEthnic(md2bl, md2bb, md2bw, tw)
        if("md3" in district):
            sortEthnic(md3bl, md3bb, md3bw, tw)	#done
        if("md4" in district):
            sortEthnic(md4bl, md4bb, md4bw, tw)	#done
        if("md5" in district):
            sortEthnic(md5bl, md5bb, md5bw, tw) #done
        if("md6" in district):
            sortEthnic(md6bl, md6bb, md6bw, tw) #done
        if("md7" in district):
            sortEthnic(md7bl, md7bb, md7bw, tw)
        if("md8" in district):
            sortEthnic(md8bl, md8bb, md8bw, tw)
        if("ma1" in district):
            sortEthnic(ma1bl, ma1bb, ma1bw, tw) #done
        if("ma2" in district):
            sortEthnic(ma2bl, ma2bb, ma2bw, tw)
        if("ma3" in district):
            sortEthnic(ma3bl, ma3bb, ma3bw, tw)	 #done
        if("ma4" in district):
            sortEthnic(ma4bl, ma4bb, ma4bw, tw)
        if("ma5" in district):
            sortEthnic(ma5bl, ma5bb, ma5bw, tw)
        if("ma6" in district):
            sortEthnic(ma6bl, ma6bb, ma6bw, tw)
        if("ma7" in district):
            sortEthnic(ma7bl, ma7bb, ma7bw, tw)
        if("ma8" in district):
            sortEthnic(ma8bl, ma8bb, ma8bw, tw)
        if("ma9" in district):
            sortEthnic(ma9bl, ma9bb, ma9bw, tw) #done
        if("me1" in district):
            sortEthnic(me1bl, me1bb, me1bw, tw) #done
        if("me2" in district):
            sortEthnic(me2bl, me2bb, me2bw, tw) #done
        if("id1" in district):
            sortEthnic(id1bl, id1bb, id1bw, tw) #done
        if("id2" in district):
            sortEthnic(id2bl, id2bb, id2bw, tw) #done
        if("nc1" in district):
            sortEthnic(nc1bl, nc1bb, nc1bw, tw)
        if("nc2" in district):
            sortEthnic(nc2bl, nc2bb, nc2bw, tw)
        if("nc3" in district):
            sortEthnic(nc3bl, nc3bb, nc3bw, tw)
        if("nc4" in district):
            sortEthnic(nc4bl, nc4bb, nc4bw, tw)
        if("nc5" in district):
            sortEthnic(nc5bl, nc5bb, nc5bw, tw)
        if("nc6" in district):
            sortEthnic(nc6bl, nc6bb, nc6bw, tw)
        if("nc7" in district):
            sortEthnic(nc7bl, nc7bb, nc7bw, tw)
        if("nc8" in district):
            sortEthnic(nc8bl, nc8bb, nc8bw, tw) #done
        if("nc9" in district):
            sortEthnic(nc9bl, nc9bb, nc9bw, tw)
        if("nc10" in district):
            sortEthnic(nc10bl, nc10bb, nc10bw, tw)
        if("nc11" in district):
            sortEthnic(nc11bl, nc11bb, nc11bw, tw)
        if("nc12" in district):
            sortEthnic(nc12bl, nc12bb, nc12bw, tw)
        if("nc13" in district):
            sortEthnic(nc13bl, nc13bb, nc13bw, tw)
        if("nh1" in district):
            sortEthnic(nh1bl, nh1bb, nh1bw, tw) #done
        if("nh2" in district):
            sortEthnic(nh2bl, nh2bb, nh2bw, tw) #done
        if("nv1" in district):
            sortEthnic(nv1bl, nv1bb, nv1bw, tw) #done
        if("nv2" in district):
            sortEthnic(nv2bl, nv2bb, nv2bw, tw)
        if("nv3" in district):
            sortEthnic(nv3bl, nv3bb, nv3bw, tw)
        if("nv4" in district):
            sortEthnic(nv4bl, nv4bb, nv4bw, tw)
        if("co1" in district):
            sortEthnic(co1bl, co1bb, co1bw, tw)
        if("co2" in district):
            sortEthnic(co2bl, co2bb, co2bw, tw) #done
        if("co3" in district):
            sortEthnic(co3bl, co3bb, co3bw, tw)
        if("co4" in district):
            sortEthnic(co4bl, co4bb, co4bw, tw)
        if("co5" in district):
            sortEthnic(co5bl, co5bb, co5bw, tw)
        if("co6" in district):
            sortEthnic(co6bl, co6bb, co6bw, tw) #done
        if("co7" in district):
            sortEthnic(co7bl, co7bb, co7bw, tw) #done
        if("nm1" in district):
            sortEthnic(nm1bl, nm1bb, nm1bw, tw) #done
        if("nm2" in district):
            sortEthnic(nm2bl, nm2bb, nm2bw, tw)
        if("nm3" in district):
            sortEthnic(nm3bl, nm3bb, nm3bw, tw) #done
        if("az1" in district):
            sortEthnic(az1bl, az1bb, az1bw, tw)
        if("az2" in district):
            sortEthnic(az2bl, az2bb, az2bw, tw)
        if("az3" in district):
            sortEthnic(az3bl, az3bb, az3bw, tw)		#done
        if("az4" in district):
            sortEthnic(az4bl, az4bb, az4bw, tw)
        if("az5" in district):
            sortEthnic(az5bl, az5bb, az5bw, tw)
        if("az6" in district):
            sortEthnic(az6bl, az6bb, az6bw, tw) #done
        if("az7" in district):
            sortEthnic(az7bl, az7bb, az7bw, tw)		#done
        if("az8" in district):
            sortEthnic(az8bl, az8bb, az8bw, tw)
        if("az9" in district):
            sortEthnic(az9bl, az9bb, az9bw, tw)			#done
        if("ga1" in district):
            sortEthnic(ga1bl, ga1bb, ga1bw, tw)
        if("ga2" in district):
            sortEthnic(ga2bl, ga2bb, ga2bw, tw)
        if("ga3" in district):
            sortEthnic(ga3bl, ga3bb, ga3bw, tw)	#done
        if("ga4" in district):
            sortEthnic(ga4bl, ga4bb, ga4bw, tw)
        if("ga5" in district):
            sortEthnic(ga5bl, ga5bb, ga5bw, tw)
        if("ga6" in district):
            sortEthnic(ga6bl, ga6bb, ga6bw, tw)
        if("ga7" in district):
            sortEthnic(ga7bl, ga7bb, ga7bw, tw)
        if("ga8" in district):
            sortEthnic(ga8bl, ga8bb, ga8bw, tw)
        if("ga9" in district):
            sortEthnic(ga9bl, ga9bb, ga9bw, tw)
        if("ga10" in district):
            sortEthnic(ga10bl, ga10bb, ga10bw, tw)
        if("ga11" in district):
            sortEthnic(ga11bl, ga11bb, ga11bw, tw)
        if("ga12" in district):
            sortEthnic(ga12bl, ga12bb, ga12bw, tw)
        if("ga13" in district):
            sortEthnic(ga13bl, ga13bb, ga13bw, tw)
        if("ga14" in district):
            sortEthnic(ga14bl, ga14bb, ga14bw, tw)
        if("tx1" in district):
            sortEthnic(tx1bl, tx1bb, tx1bw, tw) #done
        if("tx2" in district):
            sortEthnic(tx2bl, tx2bb, tx2bw, tw)
        if("tx3" in district):
            sortEthnic(tx3bl, tx3bb, tx3bw, tw)
        if("tx4" in district):
            sortEthnic(tx4bl, tx4bb, tx4bw, tw)
        if("tx5" in district):
            sortEthnic(tx5bl, tx5bb, tx5bw, tw) #done
        if("tx6" in district):
            sortEthnic(tx6bl, tx6bb, tx6bw, tw) #done
        if("tx7" in district):
            sortEthnic(tx7bl, tx7bb, tx7bw, tw)
        if("tx8" in district):
            sortEthnic(tx8bl, tx8bb, tx8bw, tw)
        if("tx9" in district):
            sortEthnic(tx9bl, tx9bb, tx9bw, tw)
        if("tx10" in district):
            sortEthnic(tx10bl, tx10bb, tx10bw, tw) #done
        if("tx11" in district):
            sortEthnic(tx11bl, tx11bb, tx11bw, tw)
        if("tx12" in district):
            sortEthnic(tx12bl, tx12bb, tx12bw, tw)
        if("tx13" in district):
            sortEthnic(tx13bl, tx13bb, tx13bw, tw)
        if("tx14" in district):
            sortEthnic(tx14bl, tx14bb, tx14bw, tw)
        if("tx15" in district):
            sortEthnic(tx15bl, tx15bb, tx15bw, tw)
        if("tx16" in district):
            sortEthnic(tx16bl, tx16bb, tx16bw, tw)
        if("tx17" in district):
            sortEthnic(tx17bl, tx17bb, tx17bw, tw)
        if("tx18" in district):
            sortEthnic(tx18bl, tx18bb, tx18bw, tw)
        if("tx19" in district):
            sortEthnic(tx19bl, tx19bb, tx19bw, tw)
        if("tx20" in district):
            sortEthnic(tx20bl, tx20bb, tx20bw, tw)
        if("tx21" in district):
            sortEthnic(tx21bl, tx21bb, tx21bw, tw)
        if("tx22" in district):
            sortEthnic(tx22bl, tx22bb, tx22bw, tw)
        if("tx23" in district):
            sortEthnic(tx23bl, tx23bb, tx23bw, tw)
        if("tx24" in district):
            sortEthnic(tx24bl, tx24bb, tx24bw, tw) #done
        if("tx25" in district):
            sortEthnic(tx25bl, tx25bb, tx25bw, tw)
        if("tx26" in district):
            sortEthnic(tx26bl, tx26bb, tx26bw, tw)
        if("tx27" in district):
            sortEthnic(tx27bl, tx27bb, tx27bw, tw)
        if("tx28" in district):
            sortEthnic(tx28bl, tx28bb, tx28bw, tw)
        if("tx29" in district):
            sortEthnic(tx29bl, tx29bb, tx29bw, tw)
        if("tx30" in district):
            sortEthnic(tx30bl, tx30bb, tx30bw, tw)
        if("tx31" in district):
            sortEthnic(tx31bl, tx31bb, tx31bw, tw)
        if("tx32" in district):
            sortEthnic(tx32bl, tx32bb, tx32bw, tw) #done
        if("tx33" in district):
            sortEthnic(tx33bl, tx33bb, tx33bw, tw)
        if("tx34" in district):
            sortEthnic(tx34bl, tx34bb, tx34bw, tw)
        if("tx35" in district):
            sortEthnic(tx35bl, tx35bb, tx35bw, tw)
        if("tx36" in district):
            sortEthnic(tx36bl, tx36bb, tx36bw, tw)
        if("in1" in district):
            sortEthnic(in1bl, in1bb, in1bw, tw)
        if("in2" in district):
            sortEthnic(in2bl, in2bb, in2bw, tw)
        if("in3" in district):
            sortEthnic(in3bl, in3bb, in3bw, tw)	 #done
        if("in4" in district):
            sortEthnic(in4bl, in4bb, in4bw, tw)
        if("in5" in district):
            sortEthnic(in5bl, in5bb, in5bw, tw)
        if("in6" in district):
            sortEthnic(in6bl, in6bb, in6bw, tw)
        if("in7" in district):
            sortEthnic(in7bl, in7bb, in7bw, tw)
        if("in8" in district):
            sortEthnic(in8bl, in8bb, in8bw, tw)
        if("in9" in district):
            sortEthnic(in9bl, in9bb, in9bw, tw)
        if("va1" in district):
            sortEthnic(va1bl, va1bb, va1bw, tw)
        if("va2" in district):
            sortEthnic(va2bl, va2bb, va2bw, tw)
        if("va3" in district):
            sortEthnic(va3bl, va3bb, va3bw, tw)
        if("va4" in district):
            sortEthnic(va4bl, va4bb, va4bw, tw)	#done
        if("va5" in district):
            sortEthnic(va5bl, va5bb, va5bw, tw)
        if("va6" in district):
            sortEthnic(va6bl, va6bb, va6bw, tw)
        if("va7" in district):
            sortEthnic(va7bl, va7bb, va7bw, tw)
        if("va8" in district):
            sortEthnic(va8bl, va8bb, va8bw, tw)
        if("va9" in district):
            sortEthnic(va9bl, va9bb, va9bw, tw)
        if("va10" in district):
            sortEthnic(va10bl, va10bb, va10bw, tw)
        if("va11" in district):
            sortEthnic(va11bl, va11bb, va11bw, tw)
        if("il1" in district):
            sortEthnic(il1bl, il1bb, il1bw, tw)
        if("il2" in district):
            sortEthnic(il2bl, il2bb, il2bw, tw)
        if("il3" in district):
            sortEthnic(il3bl, il3bb, il3bw, tw)
        if("il4" in district):
            sortEthnic(il4bl, il4bb, il4bw, tw)	#done
        if("il5" in district):
            sortEthnic(il5bl, il5bb, il5bw, tw)
        if("il6" in district):
            sortEthnic(il6bl, il6bb, il6bw, tw)
        if("il7" in district):
            sortEthnic(il7bl, il7bb, il7bw, tw)
        if("il8" in district):
            sortEthnic(il8bl, il8bb, il8bw, tw)
        if("il9" in district):
            sortEthnic(il9bl, il9bb, il9bw, tw)
        if("il10" in district):
            sortEthnic(il10bl, il10bb, il10bw, tw) #done
        if("il11" in district):
            sortEthnic(il11bl, il11bb, il11bw, tw)
        if("il12" in district):
            sortEthnic(il12bl, il12bb, il12bw, tw) #done
        if("il13" in district):
            sortEthnic(il13bl, il13bb, il13bw, tw)
        if("il14" in district):
            sortEthnic(il14bl, il14bb, il14bw, tw)#done
        if("il15" in district):
            sortEthnic(il15bl, il15bb, il15bw, tw) #done
        if("il16" in district):
            sortEthnic(il16bl, il16bb, il16bw, tw)
        if("il17" in district):
            sortEthnic(il17bl, il17bb, il17bw, tw)
        if("il18" in district):
            sortEthnic(il18bl, il18bb, il18bw, tw)
        if("de1" in district):
            sortEthnic(de1bl, de1bb, de1bw, tw) #done
        if("vt1" in district):
            sortEthnic(vt1bl, vt1bb, vt1bw, tw) #done
        if("ut1" in district):
            sortEthnic(ut1bl, ut1bb, ut1bw, tw)
        if("ut2" in district):
            sortEthnic(ut2bl, ut2bb, ut2bw, tw)
        if("ut3" in district):
            sortEthnic(ut3bl, ut3bb, ut3bw, tw)
        if("ut4" in district):
            sortEthnic(ut4bl, ut4bb, ut4bw, tw)
        if("ne1" in district):
            sortEthnic(ne1bl, ne1bb, ne1bw, tw)
        if("ne2" in district):
            sortEthnic(ne2bl, ne2bb, ne2bw, tw)
        if("ne3" in district):
            sortEthnic(ne3bl, ne3bb, ne3bw, tw)	#done
        if("ak1" in district):
            sortEthnic(ak1bl, ak1bb, ak1bw, tw) #done
        if("wy1" in district):
            sortEthnic(wy1bl, wy1bb, wy1bw, tw) #done
        if("al1" in district):
            sortEthnic(al1bl, al1bb, al1bw, tw)
        if("al2" in district):
            sortEthnic(al2bl, al2bb, al2bw, tw)
        if("al3" in district):
            sortEthnic(al3bl, al3bb, al3bw, tw)
        if("al4" in district):
            sortEthnic(al4bl, al4bb, al4bw, tw)
        if("al5" in district):
            sortEthnic(al5bl, al5bb, al5bw, tw)
        if("al6" in district):
            sortEthnic(al6bl, al6bb, al6bw, tw)
        if("al7" in district):
            sortEthnic(al7bl, al7bb, al7bw, tw)	#done
        if("tn1" in district):
            sortEthnic(tn1bl, tn1bb, tn1bw, tw)
        if("tn2" in district):
            sortEthnic(tn2bl, tn2bb, tn2bw, tw)
        if("tn3" in district):
            sortEthnic(tn3bl, tn3bb, tn3bw, tw)
        if("tn4" in district):
            sortEthnic(tn4bl, tn4bb, tn4bw, tw)
        if("tn5" in district):
            sortEthnic(tn5bl, tn5bb, tn5bw, tw)
        if("tn6" in district):
            sortEthnic(tn6bl, tn6bb, tn6bw, tw)
        if("tn7" in district):
            sortEthnic(tn7bl, tn7bb, tn7bw, tw)
        if("tn8" in district):
            sortEthnic(tn8bl, tn8bb, tn8bw, tw)
        if("tn9" in district):
            sortEthnic(tn9bl, tn9bb, tn9bw, tw)
        if("nd1" in district):
            sortEthnic(nd1bl, nd1bb, nd1bw, tw) #done
        if("sd1" in district):
            sortEthnic(sd1bl, sd1bb, sd1bw, tw) #done
        if("wv1" in district):
            sortEthnic(wv1bl, wv1bb, wv1bw, tw)
        if("wv2" in district):
            sortEthnic(wv2bl, wv2bb, wv2bw, tw)
        if("wv3" in district):
            sortEthnic(wv3bl, wv3bb, wv3bw, tw) #done
        if("ar1" in district):
            sortEthnic(ar1bl, ar1bb, ar1bw, tw) #done
        if("ar2" in district):
            sortEthnic(ar2bl, ar2bb, ar2bw, tw)
        if("ar3" in district):
            sortEthnic(ar3bl, ar3bb, ar3bw, tw)
        if("ar4" in district):
            sortEthnic(ar4bl, ar4bb, ar4bw, tw)

cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
    district = sortloc(["#trump2020", "#votered"], tw["user"]["location"], tw["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            sortEthnic(mo1tl, mo1tb, mo1tw, tw)
        if("mo2" in district):
            sortEthnic(mo2tl, mo2tb, mo2tw, tw)
        if("mo3" in district):
            sortEthnic(mo3tl, mo3tb, mo3tw, tw)
        if("mo4" in district):
            sortEthnic(mo4tl, mo4tb, mo4tw, tw)
        if("mo5" in district):
            sortEthnic(mo5tl, mo5tb, mo5tw, tw)
        if("mo6" in district):
            sortEthnic(mo6tl, mo6tb, mo6tw, tw)
        if("mo7" in district):
            sortEthnic(mo7tl, mo7tb, mo7tw, tw)
        if("mo8" in district):
            sortEthnic(mo8tl, mo8tb, mo8tw, tw)
        if("sc1" in district):
            sortEthnic(sc1tl, sc1tb, sc1tw, tw)
        if("sc2" in district):
            sortEthnic(sc2tl, sc2tb, sc2tw, tw)
        if("sc3" in district):
            sortEthnic(sc3tl, sc3tb, sc3tw, tw)
        if("sc4" in district):
            sortEthnic(sc4tl, sc4tb, sc4tw, tw)
        if("sc5" in district):
            sortEthnic(sc5tl, sc5tb, sc5tw, tw)
        if("sc6" in district):
            sortEthnic(sc6tl, sc6tb, sc6tw, tw)
        if("sc7" in district):
            sortEthnic(sc7tl, sc7tb, sc7tw, tw)
        if("ky1" in district):
            sortEthnic(ky1tl, ky1tb, ky1tw, tw)
        if("ky2" in district):
            sortEthnic(ky2tl, ky2tb, ky2tw, tw)
        if("ky3" in district):
            sortEthnic(ky3tl, ky3tb, ky3tw, tw)
        if("ky4" in district):
            sortEthnic(ky4tl, ky4tb, ky4tw, tw)
        if("ky5" in district):
            sortEthnic(ky5tl, ky5tb, ky5tw, tw)
        if("ky6" in district):
            sortEthnic(ky6tl, ky6tb, ky6tw, tw)
        if("ok1" in district):
            sortEthnic(ok1tl, ok1tb, ok1tw, tw) #done
        if("ok2" in district):
            sortEthnic(ok2tl, ok2tb, ok2tw, tw)
        if("ok3" in district):
            sortEthnic(ok3tl, ok3tb, ok3tw, tw)	#done
        if("ok4" in district):
            sortEthnic(ok4tl, ok4tb, ok4tw, tw)	#done
        if("ok5" in district):
            sortEthnic(ok5tl, ok5tb, ok5tw, tw)
        if("ia1" in district):
            sortEthnic(ia1tl, ia1tb, ia1tw, tw) #done
        if("ia2" in district):
            sortEthnic(ia2tl, ia2tb, ia2tw, tw) #done
        if("ia3" in district):
            sortEthnic(ia3tl, ia3tb, ia3tw, tw)	#done
        if("ia4" in district):
            sortEthnic(ia4tl, ia4tb, ia4tw, tw)	#done
        if("ks1" in district):
            sortEthnic(ks1tl, ks1tb, ks1tw, tw) #done
        if("ks2" in district):
            sortEthnic(ks2tl, ks2tb, ks2tw, tw) #done
        if("ks3" in district):
            sortEthnic(ks3tl, ks3tb, ks3tw, tw)
        if("ks4" in district):
            sortEthnic(ks4tl, ks4tb, ks4tw, tw)
        if("ca1" in district):
            sortEthnic(ca1tl, ca1tb, ca1tw, tw) #done
        if("ca2" in district):
            sortEthnic(ca2tl, ca2tb, ca2tw, tw) #done
        if("ca3" in district):
            sortEthnic(ca3tl, ca3tb, ca3tw, tw)
        if("ca4" in district):
            sortEthnic(ca4tl, ca4tb, ca4tw, tw)
        if("ca5" in district):
            sortEthnic(ca5tl, ca5tb, ca5tw, tw) #done
        if("ca6" in district):
            sortEthnic(ca6tl, ca6tb, ca6tw, tw)
        if("ca7" in district):
            sortEthnic(ca7tl, ca7tb, ca7tw, tw) #done
        if("ca8" in district):
            sortEthnic(ca8tl, ca8tb, ca8tw, tw)
        if("ca9" in district):
            sortEthnic(ca9tl, ca9tb, ca9tw, tw) #done
        if("ca10" in district):
            sortEthnic(ca10tl, ca10tb, ca10tw, tw) #done
        if("ca11" in district):
            sortEthnic(ca11tl, ca11tb, ca11tw, tw)
        if("ca12" in district):
            sortEthnic(ca12tl, ca12tb, ca12tw, tw)
        if("ca13" in district):
            sortEthnic(ca13tl, ca13tb, ca13tw, tw)
        if("ca14" in district):
            sortEthnic(ca14tl, ca14tb, ca14tw, tw)
        if("ca15" in district):
            sortEthnic(ca15tl, ca15tb, ca15tw, tw)
        if("ca16" in district):
            sortEthnic(ca16tl, ca16tb, ca16tw, tw) #done
        if("ca17" in district):
            sortEthnic(ca17tl, ca17tb, ca17tw, tw) #done
        if("ca18" in district):
            sortEthnic(ca18tl, ca18tb, ca18tw, tw)
        if("ca19" in district):
            sortEthnic(ca19tl, ca19tb, ca19tw, tw) #done
        if("ca20" in district):
            sortEthnic(ca20tl, ca20tb, ca20tw, tw)
        if("ca21" in district):
            sortEthnic(ca21tl, ca21tb, ca21tw, tw)
        if("ca22" in district):
            sortEthnic(ca22tl, ca22tb, ca22tw, tw)
        if("ca23" in district):
            sortEthnic(ca23tl, ca23tb, ca23tw, tw)
        if("ca24" in district):
            sortEthnic(ca24tl, ca24tb, ca24tw, tw)
        if("ca25" in district):
            sortEthnic(ca25tl, ca25tb, ca25tw, tw)
        if("ca26" in district):
            sortEthnic(ca26tl, ca26tb, ca26tw, tw) #done
        if("ca27" in district):
            sortEthnic(ca27tl, ca27tb, ca27tw, tw)
        if("ca28" in district):
            sortEthnic(ca28tl, ca28tb, ca28tw, tw)
        if("ca29" in district):
            sortEthnic(ca29tl, ca29tb, ca29tw, tw)
        if("ca30" in district):
            sortEthnic(ca30tl, ca30tb, ca30tw, tw)
        if("ca31" in district):
            sortEthnic(ca31tl, ca31tb, ca31tw, tw) #done
        if("ca32" in district):
            sortEthnic(ca32tl, ca32tb, ca32tw, tw) #done
        if("ca33" in district):
            sortEthnic(ca33tl, ca33tb, ca33tw, tw)
        if("ca34" in district):
            sortEthnic(ca34tl, ca34tb, ca34tw, tw)
        if("ca35" in district):
            sortEthnic(ca35tl, ca35tb, ca35tw, tw) #done
        if("ca36" in district):
            sortEthnic(ca36tl, ca36tb, ca36tw, tw)
        if("ca37" in district):
            sortEthnic(ca37tl, ca37tb, ca37tw, tw) #done
        if("ca38" in district):
            sortEthnic(ca38tl, ca38tb, ca38tw, tw) #done
        if("ca39" in district):
            sortEthnic(ca39tl, ca39tb, ca39tw, tw)
        if("ca40" in district):
            sortEthnic(ca40tl, ca40tb, ca40tw, tw) #done
        if("ca41" in district):
            sortEthnic(ca41tl, ca41tb, ca41tw, tw) #done
        if("ca42" in district):
            sortEthnic(ca42tl, ca42tb, ca42tw, tw)
        if("ca43" in district):
            sortEthnic(ca43tl, ca43tb, ca43tw, tw)
        if("ca44" in district):
            sortEthnic(ca44tl, ca44tb, ca44tw, tw)
        if("ca45" in district):
            sortEthnic(ca45tl, ca45tb, ca45tw, tw)
        if("ca46" in district):
            sortEthnic(ca46tl, ca46tb, ca46tw, tw) #done
        if("ca47" in district):
            sortEthnic(ca47tl, ca47tb, ca47tw, tw)
        if("ca48" in district):
            sortEthnic(ca48tl, ca48tb, ca48tw, tw) #done
        if("ca49" in district):
            sortEthnic(ca49tl, ca49tb, ca49tw, tw) #done
        if("ca50" in district):
            sortEthnic(ca50tl, ca50tb, ca50tw, tw)
        if("ca51" in district):
            sortEthnic(ca51tl, ca51tb, ca51tw, tw) #done
        if("ca52" in district):
            sortEthnic(ca52tl, ca52tb, ca52tw, tw) #done
        if("ca53" in district):
            sortEthnic(ca53tl, ca53tb, ca53tw, tw) #done
        if("la1" in district):
            sortEthnic(la1tl, la1tb, la1tw, tw)
        if("la2" in district):
            sortEthnic(la2tl, la2tb, la2tw, tw) #done
        if("la3" in district):
            sortEthnic(la3tl, la3tb, la3tw, tw)
        if("la4" in district):
            sortEthnic(la4tl, la4tb, la4tw, tw)
        if("la5" in district):
            sortEthnic(la5tl, la5tb, la5tw, tw)
        if("la6" in district):
            sortEthnic(la6tl, la6tb, la6tw, tw)
        if("ct1" in district):
            sortEthnic(ct1tl, ct1tb, ct1tw, tw)
        if("ct2" in district):
            sortEthnic(ct2tl, ct2tb, ct2tw, tw) #done
        if("ct3" in district):
            sortEthnic(ct3tl, ct3tb, ct3tw, tw)
        if("ct4" in district):
            sortEthnic(ct4tl, ct4tb, ct4tw, tw)	 #done
        if("ct5" in district):
            sortEthnic(ct5tl, ct5tb, ct5tw, tw)
        if("mt1" in district):
            sortEthnic(mt1tl, mt1tb, mt1tw, tw) #done
        if("ms1" in district):
            sortEthnic(ms1tl, ms1tb, ms1tw, tw) #done
        if("ms2" in district):
            sortEthnic(ms2tl, ms2tb, ms2tw, tw)
        if("ms3" in district):
            sortEthnic(ms3tl, ms3tb, ms3tw, tw)
        if("ms4" in district):
            sortEthnic(ms4tl, ms4tb, ms4tw, tw)
        if("pa1" in district):
            sortEthnic(pa1tl, pa1tb, pa1tw, tw)
        if("pa2" in district):
            sortEthnic(pa2tl, pa2tb, pa2tw, tw) #done
        if("pa3" in district):
            sortEthnic(pa3tl, pa3tb, pa3tw, tw)	#done
        if("pa4" in district):
            sortEthnic(pa4tl, pa4tb, pa4tw, tw)	#done
        if("pa5" in district):
            sortEthnic(pa5tl, pa5tb, pa5tw, tw) #done
        if("pa6" in district):
            sortEthnic(pa6tl, pa6tb, pa6tw, tw)
        if("pa7" in district):
            sortEthnic(pa7tl, pa7tb, pa7tw, tw) #done
        if("pa8" in district):
            sortEthnic(pa8tl, pa8tb, pa8tw, tw) #done
        if("pa9" in district):
            sortEthnic(pa9tl, pa9tb, pa9tw, tw)
        if("pa10" in district):
            sortEthnic(pa10tl, pa10tb, pa10tw, tw) #done
        if("pa11" in district):
            sortEthnic(pa11tl, pa11tb, pa11tw, tw)
        if("pa12" in district):
            sortEthnic(pa12tl, pa12tb, pa12tw, tw) #done
        if("pa13" in district):
            sortEthnic(pa13tl, pa13tb, pa13tw, tw) #done
        if("pa14" in district):
            sortEthnic(pa14tl, pa14tb, pa14tw, tw)
        if("pa15" in district):
            sortEthnic(pa15tl, pa15tb, pa15tw, tw) #done
        if("pa16" in district):
            sortEthnic(pa16tl, pa16tb, pa16tw, tw) #done
        if("pa17" in district):
            sortEthnic(pa17tl, pa17tb, pa17tw, tw) #done
        if("pa18" in district):
            sortEthnic(pa18tl, pa18tb, pa18tw, tw) #done
        if("oh1" in district):
            sortEthnic(oh1tl, oh1tb, oh1tw, tw)
        if("oh2" in district):
            sortEthnic(oh2tl, oh2tb, oh2tw, tw)
        if("oh3" in district):
            sortEthnic(oh3tl, oh3tb, oh3tw, tw)
        if("oh4" in district):
            sortEthnic(oh4tl, oh4tb, oh4tw, tw)
        if("oh5" in district):
            sortEthnic(oh5tl, oh5tb, oh5tw, tw)
        if("oh6" in district):
            sortEthnic(oh6tl, oh6tb, oh6tw, tw)
        if("oh7" in district):
            sortEthnic(oh7tl, oh7tb, oh7tw, tw)
        if("oh8" in district):
            sortEthnic(oh8tl, oh8tb, oh8tw, tw)
        if("oh9" in district):
            sortEthnic(oh9tl, oh9tb, oh9tw, tw)
        if("oh10" in district):
            sortEthnic(oh10tl, oh10tb, oh10tw, tw)
        if("oh11" in district):
            sortEthnic(oh11tl, oh11tb, oh11tw, tw)
        if("oh12" in district):
            sortEthnic(oh12tl, oh12tb, oh12tw, tw)
        if("oh13" in district):
            sortEthnic(oh13tl, oh13tb, oh13tw, tw)
        if("oh14" in district):
            sortEthnic(oh14tl, oh14tb, oh14tw, tw)
        if("oh15" in district):
            sortEthnic(oh15tl, oh15tb, oh15tw, tw)
        if("oh16" in district):
            sortEthnic(oh16tl, oh16tb, oh16tw, tw)
        if("fl1" in district):
            sortEthnic(fl1tl, fl1tb, fl1tw, tw)
        if("fl2" in district):
            sortEthnic(fl2tl, fl2tb, fl2tw, tw)
        if("fl3" in district):
            sortEthnic(fl3tl, fl3tb, fl3tw, tw)
        if("fl4" in district):
            sortEthnic(fl4tl, fl4tb, fl4tw, tw)
        if("fl5" in district):
            sortEthnic(fl5tl, fl5tb, fl5tw, tw) #done
        if("fl6" in district):
            sortEthnic(fl6tl, fl6tb, fl6tw, tw)
        if("fl7" in district):
            sortEthnic(fl7tl, fl7tb, fl7tw, tw)
        if("fl8" in district):
            sortEthnic(fl8tl, fl8tb, fl8tw, tw)
        if("fl9" in district):
            sortEthnic(fl9tl, fl9tb, fl9tw, tw)
        if("fl10" in district):
            sortEthnic(fl10tl, fl10tb, fl10tw, tw)
        if("fl11" in district):
            sortEthnic(fl11tl, fl11tb, fl11tw, tw)
        if("fl12" in district):
            sortEthnic(fl12tl, fl12tb, fl12tw, tw)
        if("fl13" in district):
            sortEthnic(fl13tl, fl13tb, fl13tw, tw)
        if("fl14" in district):
            sortEthnic(fl14tl, fl14tb, fl14tw, tw)
        if("fl15" in district):
            sortEthnic(fl15tl, fl15tb, fl15tw, tw)
        if("fl16" in district):
            sortEthnic(fl16tl, fl16tb, fl16tw, tw)
        if("fl17" in district):
            sortEthnic(fl17tl, fl17tb, fl17tw, tw)
        if("fl18" in district):
            sortEthnic(fl18tl, fl18tb, fl18tw, tw)
        if("fl19" in district):
            sortEthnic(fl19tl, fl19tb, fl19tw, tw)
        if("fl20" in district):
            sortEthnic(fl20tl, fl20tb, fl20tw, tw)
        if("fl21" in district):
            sortEthnic(fl21tl, fl21tb, fl21tw, tw) #done
        if("fl22" in district):
            sortEthnic(fl22tl, fl22tb, fl22tw, tw)
        if("fl23" in district):
            sortEthnic(fl23tl, fl23tb, fl23tw, tw)
        if("fl24" in district):
            sortEthnic(fl24tl, fl24tb, fl24tw, tw)
        if("fl25" in district):
            sortEthnic(fl25tl, fl25tb, fl25tw, tw) #done
        if("fl26" in district):
            sortEthnic(fl26tl, fl26tb, fl26tw, tw) #done
        if("fl27" in district):
            sortEthnic(fl27tl, fl27tb, fl27tw, tw)
        if("wa1" in district):
            sortEthnic(wa1tl, wa1tb, wa1tw, tw)
        if("wa2" in district):
            sortEthnic(wa2tl, wa2tb, wa2tw, tw)
        if("wa3" in district):
            sortEthnic(wa3tl, wa3tb, wa3tw, tw)
        if("wa4" in district):
            sortEthnic(wa4tl, wa4tb, wa4tw, tw)
        if("wa5" in district):
            sortEthnic(wa5tl, wa5tb, wa5tw, tw)
        if("wa6" in district):
            sortEthnic(wa6tl, wa6tb, wa6tw, tw)
        if("wa7" in district):
            sortEthnic(wa7tl, wa7tb, wa7tw, tw)
        if("wa8" in district):
            sortEthnic(wa8tl, wa8tb, wa8tw, tw)
        if("wa9" in district):
            sortEthnic(wa9tl, wa9tb, wa9tw, tw)
        if("wa10" in district):
            sortEthnic(wa10tl, wa10tb, wa10tw, tw)
        if("hi1" in district):
            sortEthnic(hi1tl, hi1tb, hi1tw, tw) #done
        if("hi2" in district):
            sortEthnic(hi2tl, hi2tb, hi2tw, tw) #done
        if("nj1" in district):
            sortEthnic(nj1tl, nj1tb, nj1tw, tw) #done
        if("nj2" in district):
            sortEthnic(nj2tl, nj2tb, nj2tw, tw) #done
        if("nj3" in district):
            sortEthnic(nj3tl, nj3tb, nj3tw, tw)	#done
        if("nj4" in district):
            sortEthnic(nj4tl, nj4tb, nj4tw, tw)	#done
        if("nj5" in district):
            sortEthnic(nj5tl, nj5tb, nj5tw, tw) #done
        if("nj6" in district):
            sortEthnic(nj6tl, nj6tb, nj6tw, tw) #done
        if("nj7" in district):
            sortEthnic(nj7tl, nj7tb, nj7tw, tw) #done
        if("nj8" in district):
            sortEthnic(nj8tl, nj8tb, nj8tw, tw) #done
        if("nj9" in district):
            sortEthnic(nj9tl, nj9tb, nj9tw, tw) #done
        if("nj10" in district):
            sortEthnic(nj10tl, nj10tb, nj10tw, tw) #done
        if("nj11" in district):
            sortEthnic(nj11tl, nj11tb, nj11tw, tw) #done
        if("nj12" in district):
            sortEthnic(nj12tl, nj12tb, nj12tw, tw) #done
        if("ny1" in district):
            sortEthnic(ny1tl, ny1tb, ny1tw, tw) #done
        if("ny2" in district):
            sortEthnic(ny2tl, ny2tb, ny2tw, tw) #done
        if("ny3" in district):
            sortEthnic(ny3tl, ny3tb, ny3tw, tw)
        if("ny4" in district):
            sortEthnic(ny4tl, ny4tb, ny4tw, tw)
        if("ny5" in district):
            sortEthnic(ny5tl, ny5tb, ny5tw, tw)
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            sortEthnic(ny6tl, ny6tb, ny6tw, tw)
            sortEthnic(ny7tl, ny7tb, ny7tw, tw)
            sortEthnic(ny8tl, ny8tb, ny8tw, tw)
            sortEthnic(ny9tl, ny9tb, ny9tw, tw)
            sortEthnic(ny10tl, ny10tb, ny10tw, tw)
            sortEthnic(ny11tl, ny11tb, ny11tw, tw)
            sortEthnic(ny12tl, ny12tb, ny12tw, tw)
            sortEthnic(ny13tl, ny13tb, ny13tw, tw)
            sortEthnic(ny14tl, ny14tb, ny14tw, tw)
            sortEthnic(ny15tl, ny15tb, ny15tw, tw)
        if("ny16" in district):
            sortEthnic(ny16tl, ny16tb, ny16tw, tw)
        if("ny17" in district):
            sortEthnic(ny17tl, ny17tb, ny17tw, tw) #done
        if("ny18" in district):
            sortEthnic(ny18tl, ny18tb, ny18tw, tw)
        if("ny19" in district):
            sortEthnic(ny19tl, ny19tb, ny19tw, tw) #done
        if("ny20" in district):
            sortEthnic(ny20tl, ny20tb, ny20tw, tw)
        if("ny21" in district):
            sortEthnic(ny21tl, ny21tb, ny21tw, tw) #done
        if("ny22" in district):
            sortEthnic(ny22tl, ny22tb, ny22tw, tw) #done
        if("ny23" in district):
            sortEthnic(ny23tl, ny23tb, ny23tw, tw)
        if("ny24" in district):
            sortEthnic(ny24tl, ny24tb, ny24tw, tw)
        if("ny25" in district):
            sortEthnic(ny25tl, ny25tb, ny25tw, tw)
        if("ny26" in district):
            sortEthnic(ny26tl, ny26tb, ny26tw, tw)
        if("ny27" in district):
            sortEthnic(ny27tl, ny27tb, ny27tw, tw) #done
        if("ri1" in district):
            sortEthnic(ri1tl, ri1tb, ri1tw, tw)	#done
        if("ri2" in district):
            sortEthnic(ri2tl, ri2tb, ri2tw, tw)
        if("mn1" in district):
            sortEthnic(mn1tl, mn1tb, mn1tw, tw) #done
        if("mn2" in district):
            sortEthnic(mn2tl, mn2tb, mn2tw, tw)
        if("mn3" in district):
            sortEthnic(mn3tl, mn3tb, mn3tw, tw)	#done
        if("mn4" in district):
            sortEthnic(mn4tl, mn4tb, mn4tw, tw)
        if("mn5" in district):
            sortEthnic(mn5tl, mn5tb, mn5tw, tw) #done
        if("mn6" in district):
            sortEthnic(mn6tl, mn6tb, mn6tw, tw) #done
        if("mn7" in district):
            sortEthnic(mn7tl, mn7tb, mn7tw, tw) #done
        if("mn8" in district):
            sortEthnic(mn8tl, mn8tb, mn8tw, tw)
        if("mi1" in district):
            sortEthnic(mi1tl, mi1tb, mi1tw, tw)
        if("mi2" in district):
            sortEthnic(mi2tl, mi2tb, mi2tw, tw) #done
        if("mi3" in district):
            sortEthnic(mi3tl, mi3tb, mi3tw, tw)
        if("mi4" in district):
            sortEthnic(mi4tl, mi4tb, mi4tw, tw)	#done
        if("mi5" in district):
            sortEthnic(mi5tl, mi5tb, mi5tw, tw) #done
        if("mi6" in district):
            sortEthnic(mi6tl, mi6tb, mi6tw, tw)
        if("mi7" in district):
            sortEthnic(mi7tl, mi7tb, mi7tw, tw)
        if("mi8" in district):
            sortEthnic(mi8tl, mi8tb, mi8tw, tw)
        if("mi9" in district):
            sortEthnic(mi9tl, mi9tb, mi9tw, tw) #done
        if("mi10" in district):
            sortEthnic(mi10tl, mi10tb, mi10tw, tw) #done
        if("mi11" in district):
            sortEthnic(mi11tl, mi11tb, mi11tw, tw)
        if("mi12" in district):
            sortEthnic(mi12tl, mi12tb, mi12tw, tw)
        if("mi13" in district):
            sortEthnic(mi13tl, mi13tb, mi13tw, tw) #done
        if("mi14" in district):
            sortEthnic(mi14tl, mi14tb, mi14tw, tw) #done
        if("wi1" in district):
            sortEthnic(wi1tl, wi1tb, wi1tw, tw)
        if("wi2" in district):
            sortEthnic(wi2tl, wi2tb, wi2tw, tw)
        if("wi3" in district):
            sortEthnic(wi3tl, wi3tb, wi3tw, tw)	#done
        if("wi4" in district):
            sortEthnic(wi4tl, wi4tb, wi4tw, tw)
        if("wi5" in district):
            sortEthnic(wi5tl, wi5tb, wi5tw, tw) #done
        if("wi6" in district):
            sortEthnic(wi6tl, wi6tb, wi6tw, tw)
        if("wi7" in district):
            sortEthnic(wi7tl, wi7tb, wi7tw, tw) #done
        if("wi8" in district):
            sortEthnic(wi8tl, wi8tb, wi8tw, tw)
        if("or1" in district):
            sortEthnic(or1tl, or1tb, or1tw, tw)
        if("or2" in district):
            sortEthnic(or2tl, or2tb, or2tw, tw) #done
        if("or3" in district):
            sortEthnic(or3tl, or3tb, or3tw, tw)
        if("or4" in district):
            sortEthnic(or4tl, or4tb, or4tw, tw)
        if("or5" in district):
            sortEthnic(or5tl, or5tb, or5tw, tw)
        if("md1" in district):
            sortEthnic(md1tl, md1tb, md1tw, tw) #done
        if("md2" in district):
            sortEthnic(md2tl, md2tb, md2tw, tw)
        if("md3" in district):
            sortEthnic(md3tl, md3tb, md3tw, tw)	#done
        if("md4" in district):
            sortEthnic(md4tl, md4tb, md4tw, tw)	#done
        if("md5" in district):
            sortEthnic(md5tl, md5tb, md5tw, tw) #done
        if("md6" in district):
            sortEthnic(md6tl, md6tb, md6tw, tw) #done
        if("md7" in district):
            sortEthnic(md7tl, md7tb, md7tw, tw)
        if("md8" in district):
            sortEthnic(md8tl, md8tb, md8tw, tw)
        if("ma1" in district):
            sortEthnic(ma1tl, ma1tb, ma1tw, tw) #done
        if("ma2" in district):
            sortEthnic(ma2tl, ma2tb, ma2tw, tw)
        if("ma3" in district):
            sortEthnic(ma3tl, ma3tb, ma3tw, tw)	 #done
        if("ma4" in district):
            sortEthnic(ma4tl, ma4tb, ma4tw, tw)
        if("ma5" in district):
            sortEthnic(ma5tl, ma5tb, ma5tw, tw)
        if("ma6" in district):
            sortEthnic(ma6tl, ma6tb, ma6tw, tw)
        if("ma7" in district):
            sortEthnic(ma7tl, ma7tb, ma7tw, tw)
        if("ma8" in district):
            sortEthnic(ma8tl, ma8tb, ma8tw, tw)
        if("ma9" in district):
            sortEthnic(ma9tl, ma9tb, ma9tw, tw) #done
        if("me1" in district):
            sortEthnic(me1tl, me1tb, me1tw, tw) #done
        if("me2" in district):
            sortEthnic(me2tl, me2tb, me2tw, tw) #done
        if("id1" in district):
            sortEthnic(id1tl, id1tb, id1tw, tw) #done
        if("id2" in district):
            sortEthnic(id2tl, id2tb, id2tw, tw) #done
        if("nc1" in district):
            sortEthnic(nc1tl, nc1tb, nc1tw, tw)
        if("nc2" in district):
            sortEthnic(nc2tl, nc2tb, nc2tw, tw)
        if("nc3" in district):
            sortEthnic(nc3tl, nc3tb, nc3tw, tw)
        if("nc4" in district):
            sortEthnic(nc4tl, nc4tb, nc4tw, tw)
        if("nc5" in district):
            sortEthnic(nc5tl, nc5tb, nc5tw, tw)
        if("nc6" in district):
            sortEthnic(nc6tl, nc6tb, nc6tw, tw)
        if("nc7" in district):
            sortEthnic(nc7tl, nc7tb, nc7tw, tw)
        if("nc8" in district):
            sortEthnic(nc8tl, nc8tb, nc8tw, tw) #done
        if("nc9" in district):
            sortEthnic(nc9tl, nc9tb, nc9tw, tw)
        if("nc10" in district):
            sortEthnic(nc10tl, nc10tb, nc10tw, tw)
        if("nc11" in district):
            sortEthnic(nc11tl, nc11tb, nc11tw, tw)
        if("nc12" in district):
            sortEthnic(nc12tl, nc12tb, nc12tw, tw)
        if("nc13" in district):
            sortEthnic(nc13tl, nc13tb, nc13tw, tw)
        if("nh1" in district):
            sortEthnic(nh1tl, nh1tb, nh1tw, tw) #done
        if("nh2" in district):
            sortEthnic(nh2tl, nh2tb, nh2tw, tw) #done
        if("nv1" in district):
            sortEthnic(nv1tl, nv1tb, nv1tw, tw) #done
        if("nv2" in district):
            sortEthnic(nv2tl, nv2tb, nv2tw, tw)
        if("nv3" in district):
            sortEthnic(nv3tl, nv3tb, nv3tw, tw)
        if("nv4" in district):
            sortEthnic(nv4tl, nv4tb, nv4tw, tw)
        if("co1" in district):
            sortEthnic(co1tl, co1tb, co1tw, tw)
        if("co2" in district):
            sortEthnic(co2tl, co2tb, co2tw, tw) #done
        if("co3" in district):
            sortEthnic(co3tl, co3tb, co3tw, tw)
        if("co4" in district):
            sortEthnic(co4tl, co4tb, co4tw, tw)
        if("co5" in district):
            sortEthnic(co5tl, co5tb, co5tw, tw)
        if("co6" in district):
            sortEthnic(co6tl, co6tb, co6tw, tw) #done
        if("co7" in district):
            sortEthnic(co7tl, co7tb, co7tw, tw) #done
        if("nm1" in district):
            sortEthnic(nm1tl, nm1tb, nm1tw, tw) #done
        if("nm2" in district):
            sortEthnic(nm2tl, nm2tb, nm2tw, tw)
        if("nm3" in district):
            sortEthnic(nm3tl, nm3tb, nm3tw, tw) #done
        if("az1" in district):
            sortEthnic(az1tl, az1tb, az1tw, tw)
        if("az2" in district):
            sortEthnic(az2tl, az2tb, az2tw, tw)
        if("az3" in district):
            sortEthnic(az3tl, az3tb, az3tw, tw)		#done
        if("az4" in district):
            sortEthnic(az4tl, az4tb, az4tw, tw)
        if("az5" in district):
            sortEthnic(az5tl, az5tb, az5tw, tw)
        if("az6" in district):
            sortEthnic(az6tl, az6tb, az6tw, tw) #done
        if("az7" in district):
            sortEthnic(az7tl, az7tb, az7tw, tw)		#done
        if("az8" in district):
            sortEthnic(az8tl, az8tb, az8tw, tw)
        if("az9" in district):
            sortEthnic(az9tl, az9tb, az9tw, tw)			#done
        if("ga1" in district):
            sortEthnic(ga1tl, ga1tb, ga1tw, tw)
        if("ga2" in district):
            sortEthnic(ga2tl, ga2tb, ga2tw, tw)
        if("ga3" in district):
            sortEthnic(ga3tl, ga3tb, ga3tw, tw)	#done
        if("ga4" in district):
            sortEthnic(ga4tl, ga4tb, ga4tw, tw)
        if("ga5" in district):
            sortEthnic(ga5tl, ga5tb, ga5tw, tw)
        if("ga6" in district):
            sortEthnic(ga6tl, ga6tb, ga6tw, tw)
        if("ga7" in district):
            sortEthnic(ga7tl, ga7tb, ga7tw, tw)
        if("ga8" in district):
            sortEthnic(ga8tl, ga8tb, ga8tw, tw)
        if("ga9" in district):
            sortEthnic(ga9tl, ga9tb, ga9tw, tw)
        if("ga10" in district):
            sortEthnic(ga10tl, ga10tb, ga10tw, tw)
        if("ga11" in district):
            sortEthnic(ga11tl, ga11tb, ga11tw, tw)
        if("ga12" in district):
            sortEthnic(ga12tl, ga12tb, ga12tw, tw)
        if("ga13" in district):
            sortEthnic(ga13tl, ga13tb, ga13tw, tw)
        if("ga14" in district):
            sortEthnic(ga14tl, ga14tb, ga14tw, tw)
        if("tx1" in district):
            sortEthnic(tx1tl, tx1tb, tx1tw, tw) #done
        if("tx2" in district):
            sortEthnic(tx2tl, tx2tb, tx2tw, tw)
        if("tx3" in district):
            sortEthnic(tx3tl, tx3tb, tx3tw, tw)
        if("tx4" in district):
            sortEthnic(tx4tl, tx4tb, tx4tw, tw)
        if("tx5" in district):
            sortEthnic(tx5tl, tx5tb, tx5tw, tw) #done
        if("tx6" in district):
            sortEthnic(tx6tl, tx6tb, tx6tw, tw) #done
        if("tx7" in district):
            sortEthnic(tx7tl, tx7tb, tx7tw, tw)
        if("tx8" in district):
            sortEthnic(tx8tl, tx8tb, tx8tw, tw)
        if("tx9" in district):
            sortEthnic(tx9tl, tx9tb, tx9tw, tw)
        if("tx10" in district):
            sortEthnic(tx10tl, tx10tb, tx10tw, tw) #done
        if("tx11" in district):
            sortEthnic(tx11tl, tx11tb, tx11tw, tw)
        if("tx12" in district):
            sortEthnic(tx12tl, tx12tb, tx12tw, tw)
        if("tx13" in district):
            sortEthnic(tx13tl, tx13tb, tx13tw, tw)
        if("tx14" in district):
            sortEthnic(tx14tl, tx14tb, tx14tw, tw)
        if("tx15" in district):
            sortEthnic(tx15tl, tx15tb, tx15tw, tw)
        if("tx16" in district):
            sortEthnic(tx16tl, tx16tb, tx16tw, tw)
        if("tx17" in district):
            sortEthnic(tx17tl, tx17tb, tx17tw, tw)
        if("tx18" in district):
            sortEthnic(tx18tl, tx18tb, tx18tw, tw)
        if("tx19" in district):
            sortEthnic(tx19tl, tx19tb, tx19tw, tw)
        if("tx20" in district):
            sortEthnic(tx20tl, tx20tb, tx20tw, tw)
        if("tx21" in district):
            sortEthnic(tx21tl, tx21tb, tx21tw, tw)
        if("tx22" in district):
            sortEthnic(tx22tl, tx22tb, tx22tw, tw)
        if("tx23" in district):
            sortEthnic(tx23tl, tx23tb, tx23tw, tw)
        if("tx24" in district):
            sortEthnic(tx24tl, tx24tb, tx24tw, tw) #done
        if("tx25" in district):
            sortEthnic(tx25tl, tx25tb, tx25tw, tw)
        if("tx26" in district):
            sortEthnic(tx26tl, tx26tb, tx26tw, tw)
        if("tx27" in district):
            sortEthnic(tx27tl, tx27tb, tx27tw, tw)
        if("tx28" in district):
            sortEthnic(tx28tl, tx28tb, tx28tw, tw)
        if("tx29" in district):
            sortEthnic(tx29tl, tx29tb, tx29tw, tw)
        if("tx30" in district):
            sortEthnic(tx30tl, tx30tb, tx30tw, tw)
        if("tx31" in district):
            sortEthnic(tx31tl, tx31tb, tx31tw, tw)
        if("tx32" in district):
            sortEthnic(tx32tl, tx32tb, tx32tw, tw) #done
        if("tx33" in district):
            sortEthnic(tx33tl, tx33tb, tx33tw, tw)
        if("tx34" in district):
            sortEthnic(tx34tl, tx34tb, tx34tw, tw)
        if("tx35" in district):
            sortEthnic(tx35tl, tx35tb, tx35tw, tw)
        if("tx36" in district):
            sortEthnic(tx36tl, tx36tb, tx36tw, tw)
        if("in1" in district):
            sortEthnic(in1tl, in1tb, in1tw, tw)
        if("in2" in district):
            sortEthnic(in2tl, in2tb, in2tw, tw)
        if("in3" in district):
            sortEthnic(in3tl, in3tb, in3tw, tw)	 #done
        if("in4" in district):
            sortEthnic(in4tl, in4tb, in4tw, tw)
        if("in5" in district):
            sortEthnic(in5tl, in5tb, in5tw, tw)
        if("in6" in district):
            sortEthnic(in6tl, in6tb, in6tw, tw)
        if("in7" in district):
            sortEthnic(in7tl, in7tb, in7tw, tw)
        if("in8" in district):
            sortEthnic(in8tl, in8tb, in8tw, tw)
        if("in9" in district):
            sortEthnic(in9tl, in9tb, in9tw, tw)
        if("va1" in district):
            sortEthnic(va1tl, va1tb, va1tw, tw)
        if("va2" in district):
            sortEthnic(va2tl, va2tb, va2tw, tw)
        if("va3" in district):
            sortEthnic(va3tl, va3tb, va3tw, tw)
        if("va4" in district):
            sortEthnic(va4tl, va4tb, va4tw, tw)	#done
        if("va5" in district):
            sortEthnic(va5tl, va5tb, va5tw, tw)
        if("va6" in district):
            sortEthnic(va6tl, va6tb, va6tw, tw)
        if("va7" in district):
            sortEthnic(va7tl, va7tb, va7tw, tw)
        if("va8" in district):
            sortEthnic(va8tl, va8tb, va8tw, tw)
        if("va9" in district):
            sortEthnic(va9tl, va9tb, va9tw, tw)
        if("va10" in district):
            sortEthnic(va10tl, va10tb, va10tw, tw)
        if("va11" in district):
            sortEthnic(va11tl, va11tb, va11tw, tw)
        if("il1" in district):
            sortEthnic(il1tl, il1tb, il1tw, tw)
        if("il2" in district):
            sortEthnic(il2tl, il2tb, il2tw, tw)
        if("il3" in district):
            sortEthnic(il3tl, il3tb, il3tw, tw)
        if("il4" in district):
            sortEthnic(il4tl, il4tb, il4tw, tw)	#done
        if("il5" in district):
            sortEthnic(il5tl, il5tb, il5tw, tw)
        if("il6" in district):
            sortEthnic(il6tl, il6tb, il6tw, tw)
        if("il7" in district):
            sortEthnic(il7tl, il7tb, il7tw, tw)
        if("il8" in district):
            sortEthnic(il8tl, il8tb, il8tw, tw)
        if("il9" in district):
            sortEthnic(il9tl, il9tb, il9tw, tw)
        if("il10" in district):
            sortEthnic(il10tl, il10tb, il10tw, tw) #done
        if("il11" in district):
            sortEthnic(il11tl, il11tb, il11tw, tw)
        if("il12" in district):
            sortEthnic(il12tl, il12tb, il12tw, tw) #done
        if("il13" in district):
            sortEthnic(il13tl, il13tb, il13tw, tw)
        if("il14" in district):
            sortEthnic(il14tl, il14tb, il14tw, tw)#done
        if("il15" in district):
            sortEthnic(il15tl, il15tb, il15tw, tw) #done
        if("il16" in district):
            sortEthnic(il16tl, il16tb, il16tw, tw)
        if("il17" in district):
            sortEthnic(il17tl, il17tb, il17tw, tw)
        if("il18" in district):
            sortEthnic(il18tl, il18tb, il18tw, tw)
        if("de1" in district):
            sortEthnic(de1tl, de1tb, de1tw, tw) #done
        if("vt1" in district):
            sortEthnic(vt1tl, vt1tb, vt1tw, tw) #done
        if("ut1" in district):
            sortEthnic(ut1tl, ut1tb, ut1tw, tw)
        if("ut2" in district):
            sortEthnic(ut2tl, ut2tb, ut2tw, tw)
        if("ut3" in district):
            sortEthnic(ut3tl, ut3tb, ut3tw, tw)
        if("ut4" in district):
            sortEthnic(ut4tl, ut4tb, ut4tw, tw)
        if("ne1" in district):
            sortEthnic(ne1tl, ne1tb, ne1tw, tw)
        if("ne2" in district):
            sortEthnic(ne2tl, ne2tb, ne2tw, tw)
        if("ne3" in district):
            sortEthnic(ne3tl, ne3tb, ne3tw, tw)	#done
        if("ak1" in district):
            sortEthnic(ak1tl, ak1tb, ak1tw, tw) #done
        if("wy1" in district):
            sortEthnic(wy1tl, wy1tb, wy1tw, tw) #done
        if("al1" in district):
            sortEthnic(al1tl, al1tb, al1tw, tw)
        if("al2" in district):
            sortEthnic(al2tl, al2tb, al2tw, tw)
        if("al3" in district):
            sortEthnic(al3tl, al3tb, al3tw, tw)
        if("al4" in district):
            sortEthnic(al4tl, al4tb, al4tw, tw)
        if("al5" in district):
            sortEthnic(al5tl, al5tb, al5tw, tw)
        if("al6" in district):
            sortEthnic(al6tl, al6tb, al6tw, tw)
        if("al7" in district):
            sortEthnic(al7tl, al7tb, al7tw, tw)	#done
        if("tn1" in district):
            sortEthnic(tn1tl, tn1tb, tn1tw, tw)
        if("tn2" in district):
            sortEthnic(tn2tl, tn2tb, tn2tw, tw)
        if("tn3" in district):
            sortEthnic(tn3tl, tn3tb, tn3tw, tw)
        if("tn4" in district):
            sortEthnic(tn4tl, tn4tb, tn4tw, tw)
        if("tn5" in district):
            sortEthnic(tn5tl, tn5tb, tn5tw, tw)
        if("tn6" in district):
            sortEthnic(tn6tl, tn6tb, tn6tw, tw)
        if("tn7" in district):
            sortEthnic(tn7tl, tn7tb, tn7tw, tw)
        if("tn8" in district):
            sortEthnic(tn8tl, tn8tb, tn8tw, tw)
        if("tn9" in district):
            sortEthnic(tn9tl, tn9tb, tn9tw, tw)
        if("nd1" in district):
            sortEthnic(nd1tl, nd1tb, nd1tw, tw) #done
        if("sd1" in district):
            sortEthnic(sd1tl, sd1tb, sd1tw, tw) #done
        if("wv1" in district):
            sortEthnic(wv1tl, wv1tb, wv1tw, tw)
        if("wv2" in district):
            sortEthnic(wv2tl, wv2tb, wv2tw, tw)
        if("wv3" in district):
            sortEthnic(wv3tl, wv3tb, wv3tw, tw) #done
        if("ar1" in district):
            sortEthnic(ar1tl, ar1tb, ar1tw, tw) #done
        if("ar2" in district):
            sortEthnic(ar2tl, ar2tb, ar2tw, tw)
        if("ar3" in district):
            sortEthnic(ar3tl, ar3tb, ar3tw, tw)
        if("ar4" in district):
            sortEthnic(ar4tl, ar4tb, ar4tw, tw)
    district = sortloc(["#biden2020", "#voteblue"], tw["user"]["location"], tw["full_text"].lower())
    if(district != "null"):
        if("mo1" in district):
            sortEthnic(mo1bl, mo1bb, mo1bw, tw)
        if("mo2" in district):
            sortEthnic(mo2bl, mo2bb, mo2bw, tw)
        if("mo3" in district):
            sortEthnic(mo3bl, mo3bb, mo3bw, tw)
        if("mo4" in district):
            sortEthnic(mo4bl, mo4bb, mo4bw, tw)
        if("mo5" in district):
            sortEthnic(mo5bl, mo5bb, mo5bw, tw)
        if("mo6" in district):
            sortEthnic(mo6bl, mo6bb, mo6bw, tw)
        if("mo7" in district):
            sortEthnic(mo7bl, mo7bb, mo7bw, tw)
        if("mo8" in district):
            sortEthnic(mo8bl, mo8bb, mo8bw, tw)
        if("sc1" in district):
            sortEthnic(sc1bl, sc1bb, sc1bw, tw)
        if("sc2" in district):
            sortEthnic(sc2bl, sc2bb, sc2bw, tw)
        if("sc3" in district):
            sortEthnic(sc3bl, sc3bb, sc3bw, tw)
        if("sc4" in district):
            sortEthnic(sc4bl, sc4bb, sc4bw, tw)
        if("sc5" in district):
            sortEthnic(sc5bl, sc5bb, sc5bw, tw)
        if("sc6" in district):
            sortEthnic(sc6bl, sc6bb, sc6bw, tw)
        if("sc7" in district):
            sortEthnic(sc7bl, sc7bb, sc7bw, tw)
        if("ky1" in district):
            sortEthnic(ky1bl, ky1bb, ky1bw, tw)
        if("ky2" in district):
            sortEthnic(ky2bl, ky2bb, ky2bw, tw)
        if("ky3" in district):
            sortEthnic(ky3bl, ky3bb, ky3bw, tw)
        if("ky4" in district):
            sortEthnic(ky4bl, ky4bb, ky4bw, tw)
        if("ky5" in district):
            sortEthnic(ky5bl, ky5bb, ky5bw, tw)
        if("ky6" in district):
            sortEthnic(ky6bl, ky6bb, ky6bw, tw)
        if("ok1" in district):
            sortEthnic(ok1bl, ok1bb, ok1bw, tw) #done
        if("ok2" in district):
            sortEthnic(ok2bl, ok2bb, ok2bw, tw)
        if("ok3" in district):
            sortEthnic(ok3bl, ok3bb, ok3bw, tw)	#done
        if("ok4" in district):
            sortEthnic(ok4bl, ok4bb, ok4bw, tw)	#done
        if("ok5" in district):
            sortEthnic(ok5bl, ok5bb, ok5bw, tw)
        if("ia1" in district):
            sortEthnic(ia1bl, ia1bb, ia1bw, tw) #done
        if("ia2" in district):
            sortEthnic(ia2bl, ia2bb, ia2bw, tw) #done
        if("ia3" in district):
            sortEthnic(ia3bl, ia3bb, ia3bw, tw)	#done
        if("ia4" in district):
            sortEthnic(ia4bl, ia4bb, ia4bw, tw)	#done
        if("ks1" in district):
            sortEthnic(ks1bl, ks1bb, ks1bw, tw) #done
        if("ks2" in district):
            sortEthnic(ks2bl, ks2bb, ks2bw, tw) #done
        if("ks3" in district):
            sortEthnic(ks3bl, ks3bb, ks3bw, tw)
        if("ks4" in district):
            sortEthnic(ks4bl, ks4bb, ks4bw, tw)
        if("ca1" in district):
            sortEthnic(ca1bl, ca1bb, ca1bw, tw) #done
        if("ca2" in district):
            sortEthnic(ca2bl, ca2bb, ca2bw, tw) #done
        if("ca3" in district):
            sortEthnic(ca3bl, ca3bb, ca3bw, tw)
        if("ca4" in district):
            sortEthnic(ca4bl, ca4bb, ca4bw, tw)
        if("ca5" in district):
            sortEthnic(ca5bl, ca5bb, ca5bw, tw) #done
        if("ca6" in district):
            sortEthnic(ca6bl, ca6bb, ca6bw, tw)
        if("ca7" in district):
            sortEthnic(ca7bl, ca7bb, ca7bw, tw) #done
        if("ca8" in district):
            sortEthnic(ca8bl, ca8bb, ca8bw, tw)
        if("ca9" in district):
            sortEthnic(ca9bl, ca9bb, ca9bw, tw) #done
        if("ca10" in district):
            sortEthnic(ca10bl, ca10bb, ca10bw, tw) #done
        if("ca11" in district):
            sortEthnic(ca11bl, ca11bb, ca11bw, tw)
        if("ca12" in district):
            sortEthnic(ca12bl, ca12bb, ca12bw, tw)
        if("ca13" in district):
            sortEthnic(ca13bl, ca13bb, ca13bw, tw)
        if("ca14" in district):
            sortEthnic(ca14bl, ca14bb, ca14bw, tw)
        if("ca15" in district):
            sortEthnic(ca15bl, ca15bb, ca15bw, tw)
        if("ca16" in district):
            sortEthnic(ca16bl, ca16bb, ca16bw, tw) #done
        if("ca17" in district):
            sortEthnic(ca17bl, ca17bb, ca17bw, tw) #done
        if("ca18" in district):
            sortEthnic(ca18bl, ca18bb, ca18bw, tw)
        if("ca19" in district):
            sortEthnic(ca19bl, ca19bb, ca19bw, tw) #done
        if("ca20" in district):
            sortEthnic(ca20bl, ca20bb, ca20bw, tw)
        if("ca21" in district):
            sortEthnic(ca21bl, ca21bb, ca21bw, tw)
        if("ca22" in district):
            sortEthnic(ca22bl, ca22bb, ca22bw, tw)
        if("ca23" in district):
            sortEthnic(ca23bl, ca23bb, ca23bw, tw)
        if("ca24" in district):
            sortEthnic(ca24bl, ca24bb, ca24bw, tw)
        if("ca25" in district):
            sortEthnic(ca25bl, ca25bb, ca25bw, tw)
        if("ca26" in district):
            sortEthnic(ca26bl, ca26bb, ca26bw, tw) #done
        if("ca27" in district):
            sortEthnic(ca27bl, ca27bb, ca27bw, tw)
        if("ca28" in district):
            sortEthnic(ca28bl, ca28bb, ca28bw, tw)
        if("ca29" in district):
            sortEthnic(ca29bl, ca29bb, ca29bw, tw)
        if("ca30" in district):
            sortEthnic(ca30bl, ca30bb, ca30bw, tw)
        if("ca31" in district):
            sortEthnic(ca31bl, ca31bb, ca31bw, tw) #done
        if("ca32" in district):
            sortEthnic(ca32bl, ca32bb, ca32bw, tw) #done
        if("ca33" in district):
            sortEthnic(ca33bl, ca33bb, ca33bw, tw)
        if("ca34" in district):
            sortEthnic(ca34bl, ca34bb, ca34bw, tw)
        if("ca35" in district):
            sortEthnic(ca35bl, ca35bb, ca35bw, tw) #done
        if("ca36" in district):
            sortEthnic(ca36bl, ca36bb, ca36bw, tw)
        if("ca37" in district):
            sortEthnic(ca37bl, ca37bb, ca37bw, tw) #done
        if("ca38" in district):
            sortEthnic(ca38bl, ca38bb, ca38bw, tw) #done
        if("ca39" in district):
            sortEthnic(ca39bl, ca39bb, ca39bw, tw)
        if("ca40" in district):
            sortEthnic(ca40bl, ca40bb, ca40bw, tw) #done
        if("ca41" in district):
            sortEthnic(ca41bl, ca41bb, ca41bw, tw) #done
        if("ca42" in district):
            sortEthnic(ca42bl, ca42bb, ca42bw, tw)
        if("ca43" in district):
            sortEthnic(ca43bl, ca43bb, ca43bw, tw)
        if("ca44" in district):
            sortEthnic(ca44bl, ca44bb, ca44bw, tw)
        if("ca45" in district):
            sortEthnic(ca45bl, ca45bb, ca45bw, tw)
        if("ca46" in district):
            sortEthnic(ca46bl, ca46bb, ca46bw, tw) #done
        if("ca47" in district):
            sortEthnic(ca47bl, ca47bb, ca47bw, tw)
        if("ca48" in district):
            sortEthnic(ca48bl, ca48bb, ca48bw, tw) #done
        if("ca49" in district):
            sortEthnic(ca49bl, ca49bb, ca49bw, tw) #done
        if("ca50" in district):
            sortEthnic(ca50bl, ca50bb, ca50bw, tw)
        if("ca51" in district):
            sortEthnic(ca51bl, ca51bb, ca51bw, tw) #done
        if("ca52" in district):
            sortEthnic(ca52bl, ca52bb, ca52bw, tw) #done
        if("ca53" in district):
            sortEthnic(ca53bl, ca53bb, ca53bw, tw) #done
        if("la1" in district):
            sortEthnic(la1bl, la1bb, la1bw, tw)
        if("la2" in district):
            sortEthnic(la2bl, la2bb, la2bw, tw) #done
        if("la3" in district):
            sortEthnic(la3bl, la3bb, la3bw, tw)
        if("la4" in district):
            sortEthnic(la4bl, la4bb, la4bw, tw)
        if("la5" in district):
            sortEthnic(la5bl, la5bb, la5bw, tw)
        if("la6" in district):
            sortEthnic(la6bl, la6bb, la6bw, tw)
        if("ct1" in district):
            sortEthnic(ct1bl, ct1bb, ct1bw, tw)
        if("ct2" in district):
            sortEthnic(ct2bl, ct2bb, ct2bw, tw) #done
        if("ct3" in district):
            sortEthnic(ct3bl, ct3bb, ct3bw, tw)
        if("ct4" in district):
            sortEthnic(ct4bl, ct4bb, ct4bw, tw)	 #done
        if("ct5" in district):
            sortEthnic(ct5bl, ct5bb, ct5bw, tw)
        if("mt1" in district):
            sortEthnic(mt1bl, mt1bb, mt1bw, tw) #done
        if("ms1" in district):
            sortEthnic(ms1bl, ms1bb, ms1bw, tw) #done
        if("ms2" in district):
            sortEthnic(ms2bl, ms2bb, ms2bw, tw)
        if("ms3" in district):
            sortEthnic(ms3bl, ms3bb, ms3bw, tw)
        if("ms4" in district):
            sortEthnic(ms4bl, ms4bb, ms4bw, tw)
        if("pa1" in district):
            sortEthnic(pa1bl, pa1bb, pa1bw, tw)
        if("pa2" in district):
            sortEthnic(pa2bl, pa2bb, pa2bw, tw) #done
        if("pa3" in district):
            sortEthnic(pa3bl, pa3bb, pa3bw, tw)	#done
        if("pa4" in district):
            sortEthnic(pa4bl, pa4bb, pa4bw, tw)	#done
        if("pa5" in district):
            sortEthnic(pa5bl, pa5bb, pa5bw, tw) #done
        if("pa6" in district):
            sortEthnic(pa6bl, pa6bb, pa6bw, tw)
        if("pa7" in district):
            sortEthnic(pa7bl, pa7bb, pa7bw, tw) #done
        if("pa8" in district):
            sortEthnic(pa8bl, pa8bb, pa8bw, tw) #done
        if("pa9" in district):
            sortEthnic(pa9bl, pa9bb, pa9bw, tw)
        if("pa10" in district):
            sortEthnic(pa10bl, pa10bb, pa10bw, tw) #done
        if("pa11" in district):
            sortEthnic(pa11bl, pa11bb, pa11bw, tw)
        if("pa12" in district):
            sortEthnic(pa12bl, pa12bb, pa12bw, tw) #done
        if("pa13" in district):
            sortEthnic(pa13bl, pa13bb, pa13bw, tw) #done
        if("pa14" in district):
            sortEthnic(pa14bl, pa14bb, pa14bw, tw)
        if("pa15" in district):
            sortEthnic(pa15bl, pa15bb, pa15bw, tw) #done
        if("pa16" in district):
            sortEthnic(pa16bl, pa16bb, pa16bw, tw) #done
        if("pa17" in district):
            sortEthnic(pa17bl, pa17bb, pa17bw, tw) #done
        if("pa18" in district):
            sortEthnic(pa18bl, pa18bb, pa18bw, tw) #done
        if("oh1" in district):
            sortEthnic(oh1bl, oh1bb, oh1bw, tw)
        if("oh2" in district):
            sortEthnic(oh2bl, oh2bb, oh2bw, tw)
        if("oh3" in district):
            sortEthnic(oh3bl, oh3bb, oh3bw, tw)
        if("oh4" in district):
            sortEthnic(oh4bl, oh4bb, oh4bw, tw)
        if("oh5" in district):
            sortEthnic(oh5bl, oh5bb, oh5bw, tw)
        if("oh6" in district):
            sortEthnic(oh6bl, oh6bb, oh6bw, tw)
        if("oh7" in district):
            sortEthnic(oh7bl, oh7bb, oh7bw, tw)
        if("oh8" in district):
            sortEthnic(oh8bl, oh8bb, oh8bw, tw)
        if("oh9" in district):
            sortEthnic(oh9bl, oh9bb, oh9bw, tw)
        if("oh10" in district):
            sortEthnic(oh10bl, oh10bb, oh10bw, tw)
        if("oh11" in district):
            sortEthnic(oh11bl, oh11bb, oh11bw, tw)
        if("oh12" in district):
            sortEthnic(oh12bl, oh12bb, oh12bw, tw)
        if("oh13" in district):
            sortEthnic(oh13bl, oh13bb, oh13bw, tw)
        if("oh14" in district):
            sortEthnic(oh14bl, oh14bb, oh14bw, tw)
        if("oh15" in district):
            sortEthnic(oh15bl, oh15bb, oh15bw, tw)
        if("oh16" in district):
            sortEthnic(oh16bl, oh16bb, oh16bw, tw)
        if("fl1" in district):
            sortEthnic(fl1bl, fl1bb, fl1bw, tw)
        if("fl2" in district):
            sortEthnic(fl2bl, fl2bb, fl2bw, tw)
        if("fl3" in district):
            sortEthnic(fl3bl, fl3bb, fl3bw, tw)
        if("fl4" in district):
            sortEthnic(fl4bl, fl4bb, fl4bw, tw)
        if("fl5" in district):
            sortEthnic(fl5bl, fl5bb, fl5bw, tw) #done
        if("fl6" in district):
            sortEthnic(fl6bl, fl6bb, fl6bw, tw)
        if("fl7" in district):
            sortEthnic(fl7bl, fl7bb, fl7bw, tw)
        if("fl8" in district):
            sortEthnic(fl8bl, fl8bb, fl8bw, tw)
        if("fl9" in district):
            sortEthnic(fl9bl, fl9bb, fl9bw, tw)
        if("fl10" in district):
            sortEthnic(fl10bl, fl10bb, fl10bw, tw)
        if("fl11" in district):
            sortEthnic(fl11bl, fl11bb, fl11bw, tw)
        if("fl12" in district):
            sortEthnic(fl12bl, fl12bb, fl12bw, tw)
        if("fl13" in district):
            sortEthnic(fl13bl, fl13bb, fl13bw, tw)
        if("fl14" in district):
            sortEthnic(fl14bl, fl14bb, fl14bw, tw)
        if("fl15" in district):
            sortEthnic(fl15bl, fl15bb, fl15bw, tw)
        if("fl16" in district):
            sortEthnic(fl16bl, fl16bb, fl16bw, tw)
        if("fl17" in district):
            sortEthnic(fl17bl, fl17bb, fl17bw, tw)
        if("fl18" in district):
            sortEthnic(fl18bl, fl18bb, fl18bw, tw)
        if("fl19" in district):
            sortEthnic(fl19bl, fl19bb, fl19bw, tw)
        if("fl20" in district):
            sortEthnic(fl20bl, fl20bb, fl20bw, tw)
        if("fl21" in district):
            sortEthnic(fl21bl, fl21bb, fl21bw, tw) #done
        if("fl22" in district):
            sortEthnic(fl22bl, fl22bb, fl22bw, tw)
        if("fl23" in district):
            sortEthnic(fl23bl, fl23bb, fl23bw, tw)
        if("fl24" in district):
            sortEthnic(fl24bl, fl24bb, fl24bw, tw)
        if("fl25" in district):
            sortEthnic(fl25bl, fl25bb, fl25bw, tw) #done
        if("fl26" in district):
            sortEthnic(fl26bl, fl26bb, fl26bw, tw) #done
        if("fl27" in district):
            sortEthnic(fl27bl, fl27bb, fl27bw, tw)
        if("wa1" in district):
            sortEthnic(wa1bl, wa1bb, wa1bw, tw)
        if("wa2" in district):
            sortEthnic(wa2bl, wa2bb, wa2bw, tw)
        if("wa3" in district):
            sortEthnic(wa3bl, wa3bb, wa3bw, tw)
        if("wa4" in district):
            sortEthnic(wa4bl, wa4bb, wa4bw, tw)
        if("wa5" in district):
            sortEthnic(wa5bl, wa5bb, wa5bw, tw)
        if("wa6" in district):
            sortEthnic(wa6bl, wa6bb, wa6bw, tw)
        if("wa7" in district):
            sortEthnic(wa7bl, wa7bb, wa7bw, tw)
        if("wa8" in district):
            sortEthnic(wa8bl, wa8bb, wa8bw, tw)
        if("wa9" in district):
            sortEthnic(wa9bl, wa9bb, wa9bw, tw)
        if("wa10" in district):
            sortEthnic(wa10bl, wa10bb, wa10bw, tw)
        if("hi1" in district):
            sortEthnic(hi1bl, hi1bb, hi1bw, tw) #done
        if("hi2" in district):
            sortEthnic(hi2bl, hi2bb, hi2bw, tw) #done
        if("nj1" in district):
            sortEthnic(nj1bl, nj1bb, nj1bw, tw) #done
        if("nj2" in district):
            sortEthnic(nj2bl, nj2bb, nj2bw, tw) #done
        if("nj3" in district):
            sortEthnic(nj3bl, nj3bb, nj3bw, tw)	#done
        if("nj4" in district):
            sortEthnic(nj4bl, nj4bb, nj4bw, tw)	#done
        if("nj5" in district):
            sortEthnic(nj5bl, nj5bb, nj5bw, tw) #done
        if("nj6" in district):
            sortEthnic(nj6bl, nj6bb, nj6bw, tw) #done
        if("nj7" in district):
            sortEthnic(nj7bl, nj7bb, nj7bw, tw) #done
        if("nj8" in district):
            sortEthnic(nj8bl, nj8bb, nj8bw, tw) #done
        if("nj9" in district):
            sortEthnic(nj9bl, nj9bb, nj9bw, tw) #done
        if("nj10" in district):
            sortEthnic(nj10bl, nj10bb, nj10bw, tw) #done
        if("nj11" in district):
            sortEthnic(nj11bl, nj11bb, nj11bw, tw) #done
        if("nj12" in district):
            sortEthnic(nj12bl, nj12bb, nj12bw, tw) #done
        if("ny1" in district):
            sortEthnic(ny1bl, ny1bb, ny1bw, tw) #done
        if("ny2" in district):
            sortEthnic(ny2bl, ny2bb, ny2bw, tw) #done
        if("ny3" in district):
            sortEthnic(ny3bl, ny3bb, ny3bw, tw)
        if("ny4" in district):
            sortEthnic(ny4bl, ny4bb, ny4bw, tw)
        if("ny5" in district):
            sortEthnic(ny5bl, ny5bb, ny5bw, tw)
        if("ny6" in district or "ny7" in district or "ny8" in district or "ny9" in district or "ny10" in district or "ny11" in district or "ny12" in district or "ny13" in district or "ny14" in district or "ny15" in district):
            sortEthnic(ny6bl, ny6bb, ny6bw, tw)
            sortEthnic(ny7bl, ny7bb, ny7bw, tw)
            sortEthnic(ny8bl, ny8bb, ny8bw, tw)
            sortEthnic(ny9bl, ny9bb, ny9bw, tw)
            sortEthnic(ny10bl, ny10bb, ny10bw, tw)
            sortEthnic(ny11bl, ny11bb, ny11bw, tw)
            sortEthnic(ny12bl, ny12bb, ny12bw, tw)
            sortEthnic(ny13bl, ny13bb, ny13bw, tw)
            sortEthnic(ny14bl, ny14bb, ny14bw, tw)
            sortEthnic(ny15bl, ny15bb, ny15bw, tw)
        if("ny16" in district):
            sortEthnic(ny16bl, ny16bb, ny16bw, tw)
        if("ny17" in district):
            sortEthnic(ny17bl, ny17bb, ny17bw, tw) #done
        if("ny18" in district):
            sortEthnic(ny18bl, ny18bb, ny18bw, tw)
        if("ny19" in district):
            sortEthnic(ny19bl, ny19bb, ny19bw, tw) #done
        if("ny20" in district):
            sortEthnic(ny20bl, ny20bb, ny20bw, tw)
        if("ny21" in district):
            sortEthnic(ny21bl, ny21bb, ny21bw, tw) #done
        if("ny22" in district):
            sortEthnic(ny22bl, ny22bb, ny22bw, tw) #done
        if("ny23" in district):
            sortEthnic(ny23bl, ny23bb, ny23bw, tw)
        if("ny24" in district):
            sortEthnic(ny24bl, ny24bb, ny24bw, tw)
        if("ny25" in district):
            sortEthnic(ny25bl, ny25bb, ny25bw, tw)
        if("ny26" in district):
            sortEthnic(ny26bl, ny26bb, ny26bw, tw)
        if("ny27" in district):
            sortEthnic(ny27bl, ny27bb, ny27bw, tw) #done
        if("ri1" in district):
            sortEthnic(ri1bl, ri1bb, ri1bw, tw)	#done
        if("ri2" in district):
            sortEthnic(ri2bl, ri2bb, ri2bw, tw)
        if("mn1" in district):
            sortEthnic(mn1bl, mn1bb, mn1bw, tw) #done
        if("mn2" in district):
            sortEthnic(mn2bl, mn2bb, mn2bw, tw)
        if("mn3" in district):
            sortEthnic(mn3bl, mn3bb, mn3bw, tw)	#done
        if("mn4" in district):
            sortEthnic(mn4bl, mn4bb, mn4bw, tw)
        if("mn5" in district):
            sortEthnic(mn5bl, mn5bb, mn5bw, tw) #done
        if("mn6" in district):
            sortEthnic(mn6bl, mn6bb, mn6bw, tw) #done
        if("mn7" in district):
            sortEthnic(mn7bl, mn7bb, mn7bw, tw) #done
        if("mn8" in district):
            sortEthnic(mn8bl, mn8bb, mn8bw, tw)
        if("mi1" in district):
            sortEthnic(mi1bl, mi1bb, mi1bw, tw)
        if("mi2" in district):
            sortEthnic(mi2bl, mi2bb, mi2bw, tw) #done
        if("mi3" in district):
            sortEthnic(mi3bl, mi3bb, mi3bw, tw)
        if("mi4" in district):
            sortEthnic(mi4bl, mi4bb, mi4bw, tw)	#done
        if("mi5" in district):
            sortEthnic(mi5bl, mi5bb, mi5bw, tw) #done
        if("mi6" in district):
            sortEthnic(mi6bl, mi6bb, mi6bw, tw)
        if("mi7" in district):
            sortEthnic(mi7bl, mi7bb, mi7bw, tw)
        if("mi8" in district):
            sortEthnic(mi8bl, mi8bb, mi8bw, tw)
        if("mi9" in district):
            sortEthnic(mi9bl, mi9bb, mi9bw, tw) #done
        if("mi10" in district):
            sortEthnic(mi10bl, mi10bb, mi10bw, tw) #done
        if("mi11" in district):
            sortEthnic(mi11bl, mi11bb, mi11bw, tw)
        if("mi12" in district):
            sortEthnic(mi12bl, mi12bb, mi12bw, tw)
        if("mi13" in district):
            sortEthnic(mi13bl, mi13bb, mi13bw, tw) #done
        if("mi14" in district):
            sortEthnic(mi14bl, mi14bb, mi14bw, tw) #done
        if("wi1" in district):
            sortEthnic(wi1bl, wi1bb, wi1bw, tw)
        if("wi2" in district):
            sortEthnic(wi2bl, wi2bb, wi2bw, tw)
        if("wi3" in district):
            sortEthnic(wi3bl, wi3bb, wi3bw, tw)	#done
        if("wi4" in district):
            sortEthnic(wi4bl, wi4bb, wi4bw, tw)
        if("wi5" in district):
            sortEthnic(wi5bl, wi5bb, wi5bw, tw) #done
        if("wi6" in district):
            sortEthnic(wi6bl, wi6bb, wi6bw, tw)
        if("wi7" in district):
            sortEthnic(wi7bl, wi7bb, wi7bw, tw) #done
        if("wi8" in district):
            sortEthnic(wi8bl, wi8bb, wi8bw, tw)
        if("or1" in district):
            sortEthnic(or1bl, or1bb, or1bw, tw)
        if("or2" in district):
            sortEthnic(or2bl, or2bb, or2bw, tw) #done
        if("or3" in district):
            sortEthnic(or3bl, or3bb, or3bw, tw)
        if("or4" in district):
            sortEthnic(or4bl, or4bb, or4bw, tw)
        if("or5" in district):
            sortEthnic(or5bl, or5bb, or5bw, tw)
        if("md1" in district):
            sortEthnic(md1bl, md1bb, md1bw, tw) #done
        if("md2" in district):
            sortEthnic(md2bl, md2bb, md2bw, tw)
        if("md3" in district):
            sortEthnic(md3bl, md3bb, md3bw, tw)	#done
        if("md4" in district):
            sortEthnic(md4bl, md4bb, md4bw, tw)	#done
        if("md5" in district):
            sortEthnic(md5bl, md5bb, md5bw, tw) #done
        if("md6" in district):
            sortEthnic(md6bl, md6bb, md6bw, tw) #done
        if("md7" in district):
            sortEthnic(md7bl, md7bb, md7bw, tw)
        if("md8" in district):
            sortEthnic(md8bl, md8bb, md8bw, tw)
        if("ma1" in district):
            sortEthnic(ma1bl, ma1bb, ma1bw, tw) #done
        if("ma2" in district):
            sortEthnic(ma2bl, ma2bb, ma2bw, tw)
        if("ma3" in district):
            sortEthnic(ma3bl, ma3bb, ma3bw, tw)	 #done
        if("ma4" in district):
            sortEthnic(ma4bl, ma4bb, ma4bw, tw)
        if("ma5" in district):
            sortEthnic(ma5bl, ma5bb, ma5bw, tw)
        if("ma6" in district):
            sortEthnic(ma6bl, ma6bb, ma6bw, tw)
        if("ma7" in district):
            sortEthnic(ma7bl, ma7bb, ma7bw, tw)
        if("ma8" in district):
            sortEthnic(ma8bl, ma8bb, ma8bw, tw)
        if("ma9" in district):
            sortEthnic(ma9bl, ma9bb, ma9bw, tw) #done
        if("me1" in district):
            sortEthnic(me1bl, me1bb, me1bw, tw) #done
        if("me2" in district):
            sortEthnic(me2bl, me2bb, me2bw, tw) #done
        if("id1" in district):
            sortEthnic(id1bl, id1bb, id1bw, tw) #done
        if("id2" in district):
            sortEthnic(id2bl, id2bb, id2bw, tw) #done
        if("nc1" in district):
            sortEthnic(nc1bl, nc1bb, nc1bw, tw)
        if("nc2" in district):
            sortEthnic(nc2bl, nc2bb, nc2bw, tw)
        if("nc3" in district):
            sortEthnic(nc3bl, nc3bb, nc3bw, tw)
        if("nc4" in district):
            sortEthnic(nc4bl, nc4bb, nc4bw, tw)
        if("nc5" in district):
            sortEthnic(nc5bl, nc5bb, nc5bw, tw)
        if("nc6" in district):
            sortEthnic(nc6bl, nc6bb, nc6bw, tw)
        if("nc7" in district):
            sortEthnic(nc7bl, nc7bb, nc7bw, tw)
        if("nc8" in district):
            sortEthnic(nc8bl, nc8bb, nc8bw, tw) #done
        if("nc9" in district):
            sortEthnic(nc9bl, nc9bb, nc9bw, tw)
        if("nc10" in district):
            sortEthnic(nc10bl, nc10bb, nc10bw, tw)
        if("nc11" in district):
            sortEthnic(nc11bl, nc11bb, nc11bw, tw)
        if("nc12" in district):
            sortEthnic(nc12bl, nc12bb, nc12bw, tw)
        if("nc13" in district):
            sortEthnic(nc13bl, nc13bb, nc13bw, tw)
        if("nh1" in district):
            sortEthnic(nh1bl, nh1bb, nh1bw, tw) #done
        if("nh2" in district):
            sortEthnic(nh2bl, nh2bb, nh2bw, tw) #done
        if("nv1" in district):
            sortEthnic(nv1bl, nv1bb, nv1bw, tw) #done
        if("nv2" in district):
            sortEthnic(nv2bl, nv2bb, nv2bw, tw)
        if("nv3" in district):
            sortEthnic(nv3bl, nv3bb, nv3bw, tw)
        if("nv4" in district):
            sortEthnic(nv4bl, nv4bb, nv4bw, tw)
        if("co1" in district):
            sortEthnic(co1bl, co1bb, co1bw, tw)
        if("co2" in district):
            sortEthnic(co2bl, co2bb, co2bw, tw) #done
        if("co3" in district):
            sortEthnic(co3bl, co3bb, co3bw, tw)
        if("co4" in district):
            sortEthnic(co4bl, co4bb, co4bw, tw)
        if("co5" in district):
            sortEthnic(co5bl, co5bb, co5bw, tw)
        if("co6" in district):
            sortEthnic(co6bl, co6bb, co6bw, tw) #done
        if("co7" in district):
            sortEthnic(co7bl, co7bb, co7bw, tw) #done
        if("nm1" in district):
            sortEthnic(nm1bl, nm1bb, nm1bw, tw) #done
        if("nm2" in district):
            sortEthnic(nm2bl, nm2bb, nm2bw, tw)
        if("nm3" in district):
            sortEthnic(nm3bl, nm3bb, nm3bw, tw) #done
        if("az1" in district):
            sortEthnic(az1bl, az1bb, az1bw, tw)
        if("az2" in district):
            sortEthnic(az2bl, az2bb, az2bw, tw)
        if("az3" in district):
            sortEthnic(az3bl, az3bb, az3bw, tw)		#done
        if("az4" in district):
            sortEthnic(az4bl, az4bb, az4bw, tw)
        if("az5" in district):
            sortEthnic(az5bl, az5bb, az5bw, tw)
        if("az6" in district):
            sortEthnic(az6bl, az6bb, az6bw, tw) #done
        if("az7" in district):
            sortEthnic(az7bl, az7bb, az7bw, tw)		#done
        if("az8" in district):
            sortEthnic(az8bl, az8bb, az8bw, tw)
        if("az9" in district):
            sortEthnic(az9bl, az9bb, az9bw, tw)			#done
        if("ga1" in district):
            sortEthnic(ga1bl, ga1bb, ga1bw, tw)
        if("ga2" in district):
            sortEthnic(ga2bl, ga2bb, ga2bw, tw)
        if("ga3" in district):
            sortEthnic(ga3bl, ga3bb, ga3bw, tw)	#done
        if("ga4" in district):
            sortEthnic(ga4bl, ga4bb, ga4bw, tw)
        if("ga5" in district):
            sortEthnic(ga5bl, ga5bb, ga5bw, tw)
        if("ga6" in district):
            sortEthnic(ga6bl, ga6bb, ga6bw, tw)
        if("ga7" in district):
            sortEthnic(ga7bl, ga7bb, ga7bw, tw)
        if("ga8" in district):
            sortEthnic(ga8bl, ga8bb, ga8bw, tw)
        if("ga9" in district):
            sortEthnic(ga9bl, ga9bb, ga9bw, tw)
        if("ga10" in district):
            sortEthnic(ga10bl, ga10bb, ga10bw, tw)
        if("ga11" in district):
            sortEthnic(ga11bl, ga11bb, ga11bw, tw)
        if("ga12" in district):
            sortEthnic(ga12bl, ga12bb, ga12bw, tw)
        if("ga13" in district):
            sortEthnic(ga13bl, ga13bb, ga13bw, tw)
        if("ga14" in district):
            sortEthnic(ga14bl, ga14bb, ga14bw, tw)
        if("tx1" in district):
            sortEthnic(tx1bl, tx1bb, tx1bw, tw) #done
        if("tx2" in district):
            sortEthnic(tx2bl, tx2bb, tx2bw, tw)
        if("tx3" in district):
            sortEthnic(tx3bl, tx3bb, tx3bw, tw)
        if("tx4" in district):
            sortEthnic(tx4bl, tx4bb, tx4bw, tw)
        if("tx5" in district):
            sortEthnic(tx5bl, tx5bb, tx5bw, tw) #done
        if("tx6" in district):
            sortEthnic(tx6bl, tx6bb, tx6bw, tw) #done
        if("tx7" in district):
            sortEthnic(tx7bl, tx7bb, tx7bw, tw)
        if("tx8" in district):
            sortEthnic(tx8bl, tx8bb, tx8bw, tw)
        if("tx9" in district):
            sortEthnic(tx9bl, tx9bb, tx9bw, tw)
        if("tx10" in district):
            sortEthnic(tx10bl, tx10bb, tx10bw, tw) #done
        if("tx11" in district):
            sortEthnic(tx11bl, tx11bb, tx11bw, tw)
        if("tx12" in district):
            sortEthnic(tx12bl, tx12bb, tx12bw, tw)
        if("tx13" in district):
            sortEthnic(tx13bl, tx13bb, tx13bw, tw)
        if("tx14" in district):
            sortEthnic(tx14bl, tx14bb, tx14bw, tw)
        if("tx15" in district):
            sortEthnic(tx15bl, tx15bb, tx15bw, tw)
        if("tx16" in district):
            sortEthnic(tx16bl, tx16bb, tx16bw, tw)
        if("tx17" in district):
            sortEthnic(tx17bl, tx17bb, tx17bw, tw)
        if("tx18" in district):
            sortEthnic(tx18bl, tx18bb, tx18bw, tw)
        if("tx19" in district):
            sortEthnic(tx19bl, tx19bb, tx19bw, tw)
        if("tx20" in district):
            sortEthnic(tx20bl, tx20bb, tx20bw, tw)
        if("tx21" in district):
            sortEthnic(tx21bl, tx21bb, tx21bw, tw)
        if("tx22" in district):
            sortEthnic(tx22bl, tx22bb, tx22bw, tw)
        if("tx23" in district):
            sortEthnic(tx23bl, tx23bb, tx23bw, tw)
        if("tx24" in district):
            sortEthnic(tx24bl, tx24bb, tx24bw, tw) #done
        if("tx25" in district):
            sortEthnic(tx25bl, tx25bb, tx25bw, tw)
        if("tx26" in district):
            sortEthnic(tx26bl, tx26bb, tx26bw, tw)
        if("tx27" in district):
            sortEthnic(tx27bl, tx27bb, tx27bw, tw)
        if("tx28" in district):
            sortEthnic(tx28bl, tx28bb, tx28bw, tw)
        if("tx29" in district):
            sortEthnic(tx29bl, tx29bb, tx29bw, tw)
        if("tx30" in district):
            sortEthnic(tx30bl, tx30bb, tx30bw, tw)
        if("tx31" in district):
            sortEthnic(tx31bl, tx31bb, tx31bw, tw)
        if("tx32" in district):
            sortEthnic(tx32bl, tx32bb, tx32bw, tw) #done
        if("tx33" in district):
            sortEthnic(tx33bl, tx33bb, tx33bw, tw)
        if("tx34" in district):
            sortEthnic(tx34bl, tx34bb, tx34bw, tw)
        if("tx35" in district):
            sortEthnic(tx35bl, tx35bb, tx35bw, tw)
        if("tx36" in district):
            sortEthnic(tx36bl, tx36bb, tx36bw, tw)
        if("in1" in district):
            sortEthnic(in1bl, in1bb, in1bw, tw)
        if("in2" in district):
            sortEthnic(in2bl, in2bb, in2bw, tw)
        if("in3" in district):
            sortEthnic(in3bl, in3bb, in3bw, tw)	 #done
        if("in4" in district):
            sortEthnic(in4bl, in4bb, in4bw, tw)
        if("in5" in district):
            sortEthnic(in5bl, in5bb, in5bw, tw)
        if("in6" in district):
            sortEthnic(in6bl, in6bb, in6bw, tw)
        if("in7" in district):
            sortEthnic(in7bl, in7bb, in7bw, tw)
        if("in8" in district):
            sortEthnic(in8bl, in8bb, in8bw, tw)
        if("in9" in district):
            sortEthnic(in9bl, in9bb, in9bw, tw)
        if("va1" in district):
            sortEthnic(va1bl, va1bb, va1bw, tw)
        if("va2" in district):
            sortEthnic(va2bl, va2bb, va2bw, tw)
        if("va3" in district):
            sortEthnic(va3bl, va3bb, va3bw, tw)
        if("va4" in district):
            sortEthnic(va4bl, va4bb, va4bw, tw)	#done
        if("va5" in district):
            sortEthnic(va5bl, va5bb, va5bw, tw)
        if("va6" in district):
            sortEthnic(va6bl, va6bb, va6bw, tw)
        if("va7" in district):
            sortEthnic(va7bl, va7bb, va7bw, tw)
        if("va8" in district):
            sortEthnic(va8bl, va8bb, va8bw, tw)
        if("va9" in district):
            sortEthnic(va9bl, va9bb, va9bw, tw)
        if("va10" in district):
            sortEthnic(va10bl, va10bb, va10bw, tw)
        if("va11" in district):
            sortEthnic(va11bl, va11bb, va11bw, tw)
        if("il1" in district):
            sortEthnic(il1bl, il1bb, il1bw, tw)
        if("il2" in district):
            sortEthnic(il2bl, il2bb, il2bw, tw)
        if("il3" in district):
            sortEthnic(il3bl, il3bb, il3bw, tw)
        if("il4" in district):
            sortEthnic(il4bl, il4bb, il4bw, tw)	#done
        if("il5" in district):
            sortEthnic(il5bl, il5bb, il5bw, tw)
        if("il6" in district):
            sortEthnic(il6bl, il6bb, il6bw, tw)
        if("il7" in district):
            sortEthnic(il7bl, il7bb, il7bw, tw)
        if("il8" in district):
            sortEthnic(il8bl, il8bb, il8bw, tw)
        if("il9" in district):
            sortEthnic(il9bl, il9bb, il9bw, tw)
        if("il10" in district):
            sortEthnic(il10bl, il10bb, il10bw, tw) #done
        if("il11" in district):
            sortEthnic(il11bl, il11bb, il11bw, tw)
        if("il12" in district):
            sortEthnic(il12bl, il12bb, il12bw, tw) #done
        if("il13" in district):
            sortEthnic(il13bl, il13bb, il13bw, tw)
        if("il14" in district):
            sortEthnic(il14bl, il14bb, il14bw, tw)#done
        if("il15" in district):
            sortEthnic(il15bl, il15bb, il15bw, tw) #done
        if("il16" in district):
            sortEthnic(il16bl, il16bb, il16bw, tw)
        if("il17" in district):
            sortEthnic(il17bl, il17bb, il17bw, tw)
        if("il18" in district):
            sortEthnic(il18bl, il18bb, il18bw, tw)
        if("de1" in district):
            sortEthnic(de1bl, de1bb, de1bw, tw) #done
        if("vt1" in district):
            sortEthnic(vt1bl, vt1bb, vt1bw, tw) #done
        if("ut1" in district):
            sortEthnic(ut1bl, ut1bb, ut1bw, tw)
        if("ut2" in district):
            sortEthnic(ut2bl, ut2bb, ut2bw, tw)
        if("ut3" in district):
            sortEthnic(ut3bl, ut3bb, ut3bw, tw)
        if("ut4" in district):
            sortEthnic(ut4bl, ut4bb, ut4bw, tw)
        if("ne1" in district):
            sortEthnic(ne1bl, ne1bb, ne1bw, tw)
        if("ne2" in district):
            sortEthnic(ne2bl, ne2bb, ne2bw, tw)
        if("ne3" in district):
            sortEthnic(ne3bl, ne3bb, ne3bw, tw)	#done
        if("ak1" in district):
            sortEthnic(ak1bl, ak1bb, ak1bw, tw) #done
        if("wy1" in district):
            sortEthnic(wy1bl, wy1bb, wy1bw, tw) #done
        if("al1" in district):
            sortEthnic(al1bl, al1bb, al1bw, tw)
        if("al2" in district):
            sortEthnic(al2bl, al2bb, al2bw, tw)
        if("al3" in district):
            sortEthnic(al3bl, al3bb, al3bw, tw)
        if("al4" in district):
            sortEthnic(al4bl, al4bb, al4bw, tw)
        if("al5" in district):
            sortEthnic(al5bl, al5bb, al5bw, tw)
        if("al6" in district):
            sortEthnic(al6bl, al6bb, al6bw, tw)
        if("al7" in district):
            sortEthnic(al7bl, al7bb, al7bw, tw)	#done
        if("tn1" in district):
            sortEthnic(tn1bl, tn1bb, tn1bw, tw)
        if("tn2" in district):
            sortEthnic(tn2bl, tn2bb, tn2bw, tw)
        if("tn3" in district):
            sortEthnic(tn3bl, tn3bb, tn3bw, tw)
        if("tn4" in district):
            sortEthnic(tn4bl, tn4bb, tn4bw, tw)
        if("tn5" in district):
            sortEthnic(tn5bl, tn5bb, tn5bw, tw)
        if("tn6" in district):
            sortEthnic(tn6bl, tn6bb, tn6bw, tw)
        if("tn7" in district):
            sortEthnic(tn7bl, tn7bb, tn7bw, tw)
        if("tn8" in district):
            sortEthnic(tn8bl, tn8bb, tn8bw, tw)
        if("tn9" in district):
            sortEthnic(tn9bl, tn9bb, tn9bw, tw)
        if("nd1" in district):
            sortEthnic(nd1bl, nd1bb, nd1bw, tw) #done
        if("sd1" in district):
            sortEthnic(sd1bl, sd1bb, sd1bw, tw) #done
        if("wv1" in district):
            sortEthnic(wv1bl, wv1bb, wv1bw, tw)
        if("wv2" in district):
            sortEthnic(wv2bl, wv2bb, wv2bw, tw)
        if("wv3" in district):
            sortEthnic(wv3bl, wv3bb, wv3bw, tw) #done
        if("ar1" in district):
            sortEthnic(ar1bl, ar1bb, ar1bw, tw) #done
        if("ar2" in district):
            sortEthnic(ar2bl, ar2bb, ar2bw, tw)
        if("ar3" in district):
            sortEthnic(ar3bl, ar3bb, ar3bw, tw)
        if("ar4" in district):
            sortEthnic(ar4bl, ar4bb, ar4bw, tw)



calcResult("Arizona 1", 759663, az1bl, az1bb, az1bw, az1tl, az1tb, az1tw, 0.45, 0.51, 0.04)
calcResult("Arizona 2", 713631, az2bl, az2bb, az2bw, az2tl, az2tb, az2tw, 0.45, 0.51, 0.04)
calcResult("Arizona 3", 761488, az3bl, az3bb, az3bw, az3tl, az3tb, az3tw, 0.45, 0.51, 0.04)
calcResult("Arizona 4", 739374, az4bl, az4bb, az4bw, az4tl, az4tb, az4tw, 0.45, 0.51, 0.04)
calcResult("Arizona 5", 789400, az5bl, az5bb, az5bw, az5tl, az5tb, az5tw, 0.45, 0.51, 0.04)
calcResult("Arizona 6", 749808, az6bl, az6bb, az6bw, az6tl, az6tb, az6tw, 0.45, 0.51, 0.04)
calcResult("Arizona 7", 769597, az7bl, az7bb, az7bw, az7tl, az7tb, az7tw, 0.45, 0.51, 0.04)
calcResult("Arizona 8", 794820, az8bl, az8bb, az8bw, az8tl, az8tb, az8tw, 0.45, 0.51, 0.04)
calcResult("Arizona 9", 777123, az7bl, az7bb, az7bw, az7tl, az7tb, az7tw, 0.45, 0.51, 0.04)
aztlat = [az1tl,az2tl,az3tl,az4tl,az5tl,az6tl,az7tl,az8tl,az9tl]
aztbla = [az1tb,az2tb,az3tb,az4tb,az5tb,az6tb,az7tb,az8tb,az9tb]
aztwhi = [az1tw,az2tw,az3tw,az4tw,az5tw,az6tw,az7tw,az8tw,az9tw]
azblat = [az1bl,az2bl,az3bl,az4bl,az5bl,az6bl,az7bl,az8bl,az9bl]
azbbla = [az1bb,az2bb,az3bb,az4bb,az5bb,az6bb,az7bb,az8bb,az9bb]
azbwhi = [az1bw,az2bw,az3bw,az4bw,az5bw,az6bw,az7bw,az8bw,az9bw]
calcStateResult("TOTAL ARIZONA", aztlat, aztbla, aztwhi, azblat, azbbla, azbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Arkansas 1", 724622, ar1bl, ar1bb, ar1bw, ar1tl, ar1tb, ar1tw, 0.45, 0.51, 0.04)
calcResult("Arkansas 2", 761348, ar2bl, ar2bb, ar2bw, ar2tl, ar2tb, ar2tw, 0.45, 0.51, 0.04)
calcResult("Arkansas 3", 782717, ar3bl, ar3bb, ar3bw, ar3tl, ar3tb, ar3tw, 0.45, 0.51, 0.04)
calcResult("Arkansas 4", 711737, ar4bl, ar4bb, ar4bw, ar4tl, ar4tb, ar4tw, 0.45, 0.51, 0.04)
artlat = [ar1tl,ar2tl,ar3tl,ar4tl]
artbla = [ar1tb,ar2tb,ar3tb,ar4tb]
artwhi = [ar1tw,ar2tw,ar3tw,ar4tw]
arblat = [ar1bl,ar2bl,ar3bl,ar4bl]
arbbla = [ar1bb,ar2bb,ar3bb,ar4bb]
arbwhi = [ar1bw,ar2bw,ar3bw,ar4bw]
calcStateResult("TOTAL ARKANSAS", artlat, artbla, artwhi, arblat, arbbla, arbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Alabama 1", 715346, al1bl, al1bb, al1bw, al1tl, al1tb, al1tw, 0.45, 0.51, 0.04)
calcResult("Alabama 2", 678122, al2bl, al2bb, al2bw, al2tl, al2tb, al2tw, 0.45, 0.51, 0.04)
calcResult("Alabama 3", 709482, al3bl, al3bb, al3bw, al3tl, al3tb, al3tw, 0.45, 0.51, 0.04)
calcResult("Alabama 4", 683273, al4bl, al4bb, al4bw, al4tl, al4tb, al4tw, 0.45, 0.51, 0.04)
calcResult("Alabama 5", 712529, al5bl, al5bb, al5bw, al5tl, al5tb, al5tw, 0.45, 0.51, 0.04)
calcResult("Alabama 6", 706308, al6bl, al6bb, al6bw, al6tl, al6tb, al6tw, 0.45, 0.51, 0.04)
calcResult("Alabama 7", 665630, al7bl, al7bb, al7bw, al7tl, al7tb, al7tw, 0.45, 0.51, 0.04 )
altlat = [al1tl,al2tl,al3tl,al4tl,al5tl,al6tl,al7tl]
altbla = [al1tb,al2tb,al3tb,al4tb,al5tb,al6tb,al7tb]
altwhi = [al1tw,al2tw,al3tw,al4tw,al5tw,al6tw,al7tw]
alblat = [al1bl,al2bl,al3bl,al4bl,al5bl,al6bl,al7bl]
albbla = [al1bb,al2bb,al3bb,al4bb,al5bb,al6bb,al7bb]
albwhi = [al1bw,al2bw,al3bw,al4bw,al5bw,al6bw,al7bw]
calcStateResult("TOTAL ALABAMA", altlat, altbla, altwhi, alblat, albbla, albwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Colorado 1", 812843, co1bl, co1bb, co1bw, co1tl, co1tb, co1tw, 0.45, 0.51, 0.04)
calcResult("Colorado 2", 803470, co2bl, co2bb, co2bw, co2tl, co2tb, co2tw, 0.45, 0.51, 0.04)
calcResult("Colorado 3", 738119, co3bl, co3bb, co3bw, co3tl, co3tb, co3tw, 0.45, 0.51, 0.04)
calcResult("Colorado 4", 795836, co4bl, co4bb, co4bw, co4tl, co4tb, co4tw, 0.45, 0.51, 0.04)
calcResult("Colorado 5", 786939, co5bl, co5bb, co5bw, co5tl, co5tb, co5tw, 0.45, 0.51, 0.04)
calcResult("Colorado 6", 813566, co6bl, co6bb, co6bw, co6tl, co6tb, co6tw, 0.45, 0.51, 0.04)
calcResult("Colorado 7", 789772, co7bl, co7bb, co7bw, co7tl, co7tb, co7tw, 0.45, 0.51, 0.04)
cotlat = [co1tl,co2tl,co3tl,co4tl,co5tl,co6tl,co7tl]
cotbla = [co1tb,co2tb,co3tb,co4tb,co5tb,co6tb,co7tb]
cotwhi = [co1tw,co2tw,co3tw,co4tw,co5tw,co6tw,co7tw]
coblat = [co1bl,co2bl,co3bl,co4bl,co5bl,co6bl,co7bl]
cobbla = [co1bb,co2bb,co3bb,co4bb,co5bb,co6bb,co7bb]
cobwhi = [co1bw,co2bw,co3bw,co4bw,co5bw,co6bw,co7bw]
calcStateResult("TOTAL COLORADO", cotlat, cotbla, cotwhi, coblat, cobbla, cobwhi, 0.45, 0.51, 0.04)
print("")
calcResult("California 1", 704012, ca1bl, ca1bb, ca1bw, ca1tl, ca1tb, ca1tw, 0.45, 0.51, 0.04)
calcResult("California 2", 722370, ca2bl, ca2bb, ca2bw, ca2tl, ca2tb, ca2tw, 0.45, 0.51, 0.04)
calcResult("California 3", 748104, ca3bl, ca3bb, ca3bw, ca3tl, ca3tb, ca3tw, 0.45, 0.51, 0.04)
calcResult("California 4", 754525, ca4bl, ca4bb, ca4bw, ca4tl, ca4tb, ca4tw, 0.45, 0.51, 0.04)
calcResult("California 5", 700443, ca5bl, ca5bb, ca5bw, ca5tl, ca5tb, ca5tw, 0.45, 0.51, 0.04)
calcResult("California 6", 664468, ca6bl, ca6bb, ca6bw, ca6tl, ca6tb, ca6tw, 0.45, 0.51, 0.04)
calcResult("California 7", 655708, ca7bl, ca7bb, ca7bw, ca7tl, ca7tb, ca7tw, 0.45, 0.51, 0.04)
calcResult("California 8", 666827, ca8bl, ca8bb, ca8bw, ca8tl, ca8tb, ca8tw, 0.45, 0.51, 0.04)
calcResult("California 9", 648766, ca9bl, ca9bb, ca9bw, ca9tl, ca9tb, ca9tw, 0.45, 0.51, 0.04)
calcResult("California 10", 714750, ca10bl, ca10bb, ca10bw, ca10tl, ca10tb, ca10tw, 0.45, 0.51, 0.04)
calcResult("California 11", 796753, ca11bl, ca11bb, ca11bw, ca11tl, ca11tb, ca11tw, 0.45, 0.51, 0.04)
calcResult("California 12", 651322, ca12bl, ca12bb, ca12bw, ca12tl, ca12tb, ca12tw, 0.45, 0.51, 0.04)
calcResult("California 13", 665318, ca13bl, ca13bb, ca13bw, ca13tl, ca13tb, ca13tw, 0.45, 0.51, 0.04)
calcResult("California 14", 653935, ca14bl, ca14bb, ca14bw, ca14tl, ca14tb, ca14tw, 0.45, 0.51, 0.04)
calcResult("California 15", 677605, ca15bl, ca15bb, ca15bw, ca15tl, ca15tb, ca15tw, 0.45, 0.51, 0.04)
calcResult("California 16", 676880, ca16bl, ca16bb, ca16bw, ca16tl, ca16tb, ca16tw, 0.45, 0.51, 0.04)
calcResult("California 17", 664240, ca17bl, ca17bb, ca17bw, ca17tl, ca17tb, ca17tw, 0.45, 0.51, 0.04)
calcResult("California 18", 723607, ca18bl, ca18bb, ca18bw, ca18tl, ca18tb, ca18tw, 0.45, 0.51, 0.04)
calcResult("California 19", 757337, ca19bl, ca19bb, ca19bw, ca19tl, ca19tb, ca19tw, 0.45, 0.51, 0.04 )
calcResult("California 20", 744350, ca20bl, ca20bb, ca20bw, ca20tl, ca20tb, ca20tw, 0.45, 0.51, 0.04)
calcResult("California 21", 784186, ca21bl, ca21bb, ca21bw, ca21tl, ca21tb, ca21tw, 0.45, 0.51, 0.04)
calcResult("California 22", 797084, ca22bl, ca22bb, ca22bw, ca22tl, ca22tb, ca22tw, 0.45, 0.51, 0.04)
calcResult("California 23", 747852, ca23bl, ca23bb, ca23bw, ca23tl, ca23tb, ca23tw, 0.45, 0.51, 0.04)
calcResult("California 24", 681622, ca24bl, ca24bb, ca24bw, ca24tl, ca24tb, ca24tw, 0.45, 0.51, 0.04)
calcResult("California 25", 844320, ca25bl, ca25bb, ca25bw, ca25tl, ca25tb, ca25tw, 0.45, 0.51, 0.04)
calcResult("California 26", 691452, ca26bl, ca26bb, ca26bw, ca26tl, ca26tb, ca26tw, 0.45, 0.51, 0.04)
calcResult("California 27", 684496, ca27bl, ca27bb, ca27bw, ca27tl, ca27tb, ca27tw, 0.45, 0.51, 0.04)
calcResult("California 28", 660194, ca28bl, ca28bb, ca28bw, ca28tl, ca28tb, ca28tw, 0.45, 0.51, 0.04)
calcResult("California 29", 642138, ca29bl, ca29bb, ca29bw, ca29tl, ca29tb, ca29tw, 0.45, 0.51, 0.04)
calcResult("California 30", 662319, ca30bl, ca30bb, ca30bw, ca30tl, ca30tb, ca30tw, 0.45, 0.51, 0.04)
calcResult("California 31", 611336, ca31bl, ca31bb, ca31bw, ca31tl, ca31tb, ca31tw, 0.45, 0.51, 0.04)
calcResult("California 32", 642236, ca32bl, ca32bb, ca32bw, ca32tl, ca32tb, ca32tw, 0.45, 0.51, 0.04)
calcResult("California 33", 637122, ca33bl, ca33bb, ca33bw, ca33tl, ca33tb, ca33tw, 0.45, 0.51, 0.04)
calcResult("California 34", 654303, ca34bl, ca34bb, ca34bw, ca34tl, ca34tb, ca34tw, 0.45, 0.51, 0.04)
calcResult("California 35", 662413, ca35bl, ca35bb, ca35bw, ca35tl, ca35tb, ca35tw, 0.45, 0.51, 0.04)
calcResult("California 36", 750645, ca36bl, ca36bb, ca36bw, ca36tl, ca36tb, ca36tw, 0.45, 0.51, 0.04)
calcResult("California 37", 738174, ca37bl, ca37bb, ca37bw, ca37tl, ca37tb, ca37tw, 0.45, 0.51, 0.04)
calcResult("California 38", 641410, ca38bl, ca38bb, ca38bw, ca38tl, ca38tb, ca38tw, 0.45, 0.51, 0.04)
calcResult("California 39", 643155, ca39bl, ca39bb, ca39bw, ca39tl, ca39tb, ca39tw, 0.45, 0.51, 0.04)
calcResult("California 40", 665653, ca40bl, ca40bb, ca40bw, ca40tl, ca40tb, ca40tw, 0.45, 0.51, 0.04)
calcResult("California 41", 797133, ca41bl, ca41bb, ca41bw, ca41tl, ca41tb, ca41tw, 0.45, 0.51, 0.04)
calcResult("California 42", 667638, ca42bl, ca42bb, ca42bw, ca42tl, ca42tb, ca42tw, 0.45, 0.51, 0.04)
calcResult("California 43", 735581, ca43bl, ca43bb, ca43bw, ca43tl, ca43tb, ca43tw, 0.45, 0.51, 0.04)
calcResult("California 44", 712204, ca44bl, ca44bb, ca44bw, ca44tl, ca44tb, ca44tw, 0.45, 0.51, 0.04)
calcResult("California 45", 914209, ca45bl, ca45bb, ca45bw, ca45tl, ca45tb, ca45tw, 0.45, 0.51, 0.04)
calcResult("California 46", 734649, ca46bl, ca46bb, ca46bw, ca46tl, ca46tb, ca46tw, 0.45, 0.51, 0.04)
calcResult("California 47", 631422, ca47bl, ca47bb, ca47bw, ca47tl, ca47tb, ca47tw, 0.45, 0.51, 0.04)
calcResult("California 48", 727833, ca48bl, ca48bb, ca48bw, ca48tl, ca48tb, ca48tw, 0.45, 0.51, 0.04)
calcResult("California 49", 717823, ca49bl, ca49bb, ca49bw, ca49tl, ca49tb, ca49tw, 0.45, 0.51, 0.04)
calcResult("California 50", 730427, ca50bl, ca50bb, ca50bw, ca50tl, ca50tb, ca50tw, 0.45, 0.51, 0.04)
calcResult("California 51", 743982, ca51bl, ca51bb, ca51bw, ca51tl, ca51tb, ca51tw, 0.45, 0.51, 0.04)
calcResult("California 52", 713904, ca52bl, ca52bb, ca52bw, ca52tl, ca52tb, ca52tw, 0.45, 0.51, 0.04)
calcResult("California 53", 741909, ca53bl, ca53bb, ca53bw, ca53tl, ca53tb, ca53tw, 0.45, 0.51, 0.04)
catlat = [ca1tl,ca2tl,ca3tl,ca4tl,ca5tl,ca6tl,ca7tl,ca8tl,ca9tl,ca10tl,ca11tl,ca12tl,ca13tl,ca14tl,ca15tl,ca16tl,ca17tl,ca18tl, ca19tl,ca20tl,ca21tl,ca22tl,ca23tl,ca24tl,ca25tl,ca26tl,ca27tl,ca28tl,ca29tl,ca30tl,ca31tl,ca32tl,ca33tl,ca34tl,ca35tl,ca36tl,ca37tl,ca38tl,ca39tl,ca40tl,ca41tl,ca42tl,ca43tl,ca44tl,ca45tl,ca46tl,ca47tl,ca48tl,ca49tl,ca50tl,ca51tl,ca52tl,ca53tl]
catbla = [ca1tb,ca2tb,ca3tb,ca4tb,ca5tb,ca6tb,ca7tb,ca8tb,ca9tb,ca10tb,ca11tb,ca12tb,ca13tb,ca14tb,ca15tb,ca16tb,ca17tb,ca18tb, ca19tb,ca20tb,ca21tb,ca22tb,ca23tb,ca24tb,ca25tb,ca26tb,ca27tb,ca28tb,ca29tb,ca30tb,ca31tb,ca32tb,ca33tb,ca34tb,ca35tb,ca36tb,ca37tb,ca38tb,ca39tb,ca40tb,ca41tb,ca42tb,ca43tb,ca44tb,ca45tb,ca46tb,ca47tb,ca48tb,ca49tb,ca50tb,ca51tb,ca52tb,ca53tb]
catwhi = [ca1tw,ca2tw,ca3tw,ca4tw,ca5tw,ca6tw,ca7tw,ca8tw,ca9tw,ca10tw,ca11tw,ca12tw,ca13tw,ca14tw,ca15tw,ca16tw,ca17tw,ca18tw, ca19tw,ca20tw,ca21tw,ca22tw,ca23tw,ca24tw,ca25tw,ca26tw,ca27tw,ca28tw,ca29tw,ca30tw,ca31tw,ca32tw,ca33tw,ca34tw,ca35tw,ca36tw,ca37tw,ca38tw,ca39tw,ca40tw,ca41tw,ca42tw,ca43tw,ca44tw,ca45tw,ca46tw,ca47tw,ca48tw,ca49tw,ca50tw,ca51tw,ca52tw,ca53tw]
cablat = [ca1bl,ca2bl,ca3bl,ca4bl,ca5bl,ca6bl,ca7bl,ca8bl,ca9bl,ca10bl,ca11bl,ca12bl,ca13bl,ca14bl,ca15bl,ca16bl,ca17bl,ca18bl, ca19bl,ca20bl,ca21bl,ca22bl,ca23bl,ca24bl,ca25bl,ca26bl,ca27bl,ca28bl,ca29bl,ca30bl,ca31bl,ca32bl,ca33bl,ca34bl,ca35bl,ca36bl,ca37bl,ca38bl,ca39bl,ca40bl,ca41bl,ca42bl,ca43bl,ca44bl,ca45bl,ca46bl,ca47bl,ca48bl,ca49bl,ca50bl,ca51bl,ca52bl,ca53bl]
cabbla = [ca1bb,ca2bb,ca3bb,ca4bb,ca5bb,ca6bb,ca7bb,ca8bb,ca9bb,ca10bb,ca11bb,ca12bb,ca13bb,ca14bb,ca15bb,ca16bb,ca17bb,ca18bb, ca19bb,ca20bb,ca21bb,ca22bb,ca23bb,ca24bb,ca25bb,ca26bb,ca27bb,ca28bb,ca29bb,ca30bb,ca31bb,ca32bb,ca33bb,ca34bb,ca35bb,ca36bb,ca37bb,ca38bb,ca39bb,ca40bb,ca41bb,ca42bb,ca43bb,ca44bb,ca45bb,ca46bb,ca47bb,ca48bb,ca49bb,ca50bb,ca51bb,ca52bb,ca53bb]
cabwhi = [ca1bw,ca2bw,ca3bw,ca4bw,ca5bw,ca6bw,ca7bw,ca8bw,ca9bw,ca10bw,ca11bw,ca12bw,ca13bw,ca14bw,ca15bw,ca16bw,ca17bw,ca18bw, ca19bw,ca20bw,ca21bw,ca22bw,ca23bw,ca24bw,ca25bw,ca26bw,ca27bw,ca28bw,ca29bw,ca30bw,ca31bw,ca32bw,ca33bw,ca34bw,ca35bw,ca36bw,ca37bw,ca38bw,ca39bw,ca40bw,ca41bw,ca42bw,ca43bw,ca44bw,ca45bw,ca46bw,ca47bw,ca48bw,ca49bw,ca50bw,ca51bw,ca52bw,ca53bw]
calcStateResult("TOTAL CALIFORNIA", catlat, catbla, catwhi, cablat, cabbla, cabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Connecticut 1", 710509, ct1bl, ct1bb, ct1bw, ct1tl, ct1tb, ct1tw, 0.45, 0.51, 0.04)
calcResult("Connecticut 2", 705217, ct2bl, ct2bb, ct2bw, ct2tl, ct2tb, ct2tw, 0.45, 0.51, 0.04)
calcResult("Connecticut 3", 716547, ct3bl, ct3bb, ct3bw, ct3tl, ct3tb, ct3tw, 0.45, 0.51, 0.04)
calcResult("Connecticut 4", 716549, ct4bl, ct4bb, ct4bw, ct4tl, ct4tb, ct4tw, 0.45, 0.51, 0.04)
calcResult("Connecticut 5", 718295, ct5bl, ct5bb, ct5bw, ct5tl, ct5tb, ct5tw, 0.45, 0.51, 0.04)
cttlat = [ct1tl,ct2tl,ct3tl,ct4tl,ct5tl]
cttbla = [ct1tb,ct2tb,ct3tb,ct4tb,ct5tb]
cttwhi = [ct1tw,ct2tw,ct3tw,ct4tw,ct5tw]
ctblat = [ct1bl,ct2bl,ct3bl,ct4bl,ct5bl]
ctbbla = [ct1bb,ct2bb,ct3bb,ct4bb,ct5bb]
ctbwhi = [ct1bw,ct2bw,ct3bw,ct4bw,ct5bw]
calcStateResult("TOTAL CONNECTICUT", cttlat, cttbla, cttwhi, ctblat, ctbbla, ctbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Georgia 1", 734172, ga1bl, ga1bb, ga1bw, ga1tl, ga1tb, ga1tw, 0.45, 0.51, 0.04)
calcResult("Georgia 2", 672244, ga2bl, ga2bb, ga2bw, ga2tl, ga2tb, ga2tw, 0.45, 0.51, 0.04)
calcResult("Georgia 3", 729810, ga3bl, ga3bb, ga3bw, ga3tl, ga3tb, ga3tw, 0.45, 0.51, 0.04)
calcResult("Georgia 4", 752273, ga4bl, ga4bb, ga4bw, ga4tl, ga4tb, ga4tw, 0.45, 0.51, 0.04)
calcResult("Georgia 5", 793039, ga5bl, ga5bb, ga5bw, ga5tl, ga5tb, ga5tw, 0.45, 0.51, 0.04)
calcResult("Georgia 6", 756389, ga6bl, ga6bb, ga6bw, ga6tl, ga6tb, ga6tw, 0.45, 0.51, 0.04)
calcResult("Georgia 7", 789864, ga7bl, ga7bb, ga7bw, ga7tl, ga7tb, ga7tw, 0.45, 0.51, 0.04)
calcResult("Georgia 8", 710108, ga8bl, ga8bb, ga8bw, ga8tl, ga8tb, ga8tw, 0.45, 0.51, 0.04)
calcResult("Georgia 9", 736075, ga9bl, ga9bb, ga9bw, ga9tl, ga9tb, ga9tw, 0.45, 0.51, 0.04)
calcResult("Georgia 10", 741464, ga10bl, ga10bb, ga10bw, ga10tl, ga10tb, ga10tw, 0.45, 0.51, 0.04)
calcResult("Georgia 11", 764184, ga11bl, ga11bb, ga11bw, ga11tl, ga11tb, ga11tw, 0.45, 0.51, 0.04)
calcResult("Georgia 12", 722937, ga12bl, ga12bb, ga12bw, ga12tl, ga12tb, ga12tw, 0.45, 0.51, 0.04)
calcResult("Georgia 13", 757521, ga13bl, ga13bb, ga13bw, ga13tl, ga13tb, ga13tw, 0.45, 0.51, 0.04)
calcResult("Georgia 14", 710176, ga14bl, ga14bb, ga14bw, ga14tl, ga14tb, ga14tw, 0.45, 0.51, 0.04)
gatlat = [ga1tl,ga2tl,ga3tl,ga4tl,ga5tl,ga6tl,ga7tl,ga8tl,ga9tl,ga10tl,ga11tl,ga12tl,ga13tl,ga14tl]
gatbla = [ga1tb,ga2tb,ga3tb,ga4tb,ga5tb,ga6tb,ga7tb,ga8tb,ga9tb,ga10tb,ga11tb,ga12tb,ga13tb,ga14tb]
gatwhi = [ga1tw,ga2tw,ga3tw,ga4tw,ga5tw,ga6tw,ga7tw,ga8tw,ga9tw,ga10tw,ga11tw,ga12tw,ga13tw,ga14tw]
gablat = [ga1bl,ga2bl,ga3bl,ga4bl,ga5bl,ga6bl,ga7bl,ga8bl,ga9bl,ga10bl,ga11bl,ga12bl,ga13bl,ga14bl]
gabbla = [ga1bb,ga2bb,ga3bb,ga4bb,ga5bb,ga6bb,ga7bb,ga8bb,ga9bb,ga10bb,ga11bb,ga12bb,ga13bb,ga14bb]
gabwhi = [ga1bw,ga2bw,ga3bw,ga4bw,ga5bw,ga6bw,ga7bw,ga8bw,ga9bw,ga10bw,ga11bw,ga12bw,ga13bw,ga14bw]
calcStateResult("TOTAL GEORGIA", gatlat, gatbla, gatwhi, gablat, gabbla, gabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Florida 1", 762506, fl1bl, fl1bb, fl1bw, fl1tl, fl1tb, fl1tw, 0.45, 0.51, 0.04)
calcResult("Florida 2", 720418, fl2bl, fl2bb, fl2bw, fl2tl, fl2tb, fl2tw, 0.45, 0.51, 0.04)
calcResult("Florida 3", 732088, fl3bl, fl3bb, fl3bw, fl3tl, fl3tb, fl3tw, 0.45, 0.51, 0.04)
calcResult("Florida 4", 778620, fl4bl, fl4bb, fl4bw, fl4tl, fl4tb, fl4tw, 0.45, 0.51, 0.04)
calcResult("Florida 5", 728346, fl5bl, fl5bb, fl5bw, fl5tl, fl5tb, fl5tw, 0.45, 0.51, 0.04)
calcResult("Florida 6", 765005, fl6bl, fl6bb, fl6bw, fl6tl, fl6tb, fl6tw, 0.45, 0.51, 0.04)
calcResult("Florida 7", 762326, fl7bl, fl7bb, fl7bw, fl7tl, fl7tb, fl7tw, 0.45, 0.51, 0.04)
calcResult("Florida 8", 744430, fl8bl, fl8bb, fl8bw, fl8tl, fl8tb, fl8tw, 0.45, 0.51, 0.04)
calcResult("Florida 9", 832753, fl9bl, fl9bb, fl9bw, fl9tl, fl9tb, fl9tw, 0.45, 0.51, 0.04)
calcResult("Florida 10", 791447, fl10bl, fl10bb, fl10bw, fl10tl, fl10tb, fl10tw, 0.45, 0.51, 0.04)
calcResult("Florida 11", 758331, fl11bl, fl11bb, fl11bw, fl11tl, fl11tb, fl11tw, 0.45, 0.51, 0.04)
calcResult("Florida 12", 760472, fl12bl, fl12bb, fl12bw, fl12tl, fl12tb, fl12tw, 0.45, 0.51, 0.04)
calcResult("Florida 13", 728996, fl13bl, fl13bb, fl13bw, fl13tl, fl13tb, fl13tw, 0.45, 0.51, 0.04)
calcResult("Florida 14", 769968, fl14bl, fl14bb, fl14bw, fl14tl, fl14tb, fl14tw, 0.45, 0.51, 0.04)
calcResult("Florida 15", 762822, fl15bl, fl15bb, fl15bw, fl15tl, fl15tb, fl15tw, 0.45, 0.51, 0.04)
calcResult("Florida 16", 814209, fl16bl, fl16bb, fl16bw, fl16tl, fl16tb, fl16tw, 0.45, 0.51, 0.04)
calcResult("Florida 17", 768138, fl17bl, fl17bb, fl17bw, fl17tl, fl17tb, fl17tw, 0.45, 0.51, 0.04)
calcResult("Florida 18", 754652, fl18bl, fl18bb, fl18bw, fl18tl, fl18tb, fl18tw, 0.45, 0.51, 0.04)
calcResult("Florida 19", 799332, fl19bl, fl19bb, fl19bw, fl19tl, fl19tb, fl19tw, 0.45, 0.51, 0.04)
calcResult("Florida 20", 794621, fl20bl, fl20bb, fl20bw, fl20tl, fl20tb, fl20tw, 0.45, 0.51, 0.04)
calcResult("Florida 21", 758201, fl21bl, fl21bb, fl21bw, fl21tl, fl21tb, fl21tw, 0.45, 0.51, 0.04)
calcResult("Florida 22", 737019, fl22bl, fl22bb, fl22bw, fl22tl, fl22tb, fl22tw, 0.45, 0.51, 0.04)
calcResult("Florida 23", 749377, fl23bl, fl23bb, fl23bw, fl23tl, fl23tb, fl23tw, 0.45, 0.51, 0.04)
calcResult("Florida 24", 749624, fl24bl, fl24bb, fl24bw, fl24tl, fl24tb, fl24tw, 0.45, 0.51, 0.04)
calcResult("Florida 25", 763628, fl25bl, fl25bb, fl25bw, fl25tl, fl25tb, fl25tw, 0.45, 0.51, 0.04)
calcResult("Florida 26", 788816, fl26bl, fl26bb, fl26bw, fl26tl, fl26tb, fl26tw, 0.45, 0.51, 0.04)
calcResult("Florida 27", 747049, fl27bl, fl27bb, fl27bw, fl27tl, fl27tb, fl27tw, 0.45, 0.51, 0.04)
fltlat = [fl1tl,fl2tl,fl3tl,fl4tl,fl5tl,fl6tl,fl7tl,fl8tl,fl9tl,fl10tl,fl11tl,fl12tl,fl13tl,fl14tl,fl15tl,fl16tl,fl17tl,fl18tl,fl19tl,fl20tl,fl21tl,fl22tl,fl23tl,fl24tl,fl25tl,fl26tl,fl27tl]
fltbla = [fl1tb,fl2tb,fl3tb,fl4tb,fl5tb,fl6tb,fl7tb,fl8tb,fl9tb,fl10tb,fl11tb,fl12tb,fl13tb,fl14tb,fl15tb,fl16tb,fl17tb,fl18tb,fl19tb,fl20tb,fl21tb,fl22tb,fl23tb,fl24tb,fl25tb,fl26tb,fl27tb]
fltwhi = [fl1tw,fl2tw,fl3tw,fl4tw,fl5tw,fl6tw,fl7tw,fl8tw,fl9tw,fl10tw,fl11tw,fl12tw,fl13tw,fl14tw,fl15tw,fl16tw,fl17tw,fl18tw,fl19tw,fl20tw,fl21tw,fl22tw,fl23tw,fl24tw,fl25tw,fl26tw,fl27tw]
flblat = [fl1bl,fl2bl,fl3bl,fl4bl,fl5bl,fl6bl,fl7bl,fl8bl,fl9bl,fl10bl,fl11bl,fl12bl,fl13bl,fl14bl,fl15bl,fl16bl,fl17bl,fl18bl,fl19bl,fl20bl,fl21bl,fl22bl,fl23bl,fl24bl,fl25bl,fl26bl,fl27bl]
flbbla = [fl1bb,fl2bb,fl3bb,fl4bb,fl5bb,fl6bb,fl7bb,fl8bb,fl9bb,fl10bb,fl11bb,fl12bb,fl13bb,fl14bb,fl15bb,fl16bb,fl17bb,fl18bb,fl19bb,fl20bb,fl21bb,fl22bb,fl23bb,fl24bb,fl25bb,fl26bb,fl27bb]
flbwhi = [fl1bw,fl2bw,fl3bw,fl4bw,fl5bw,fl6bw,fl7bw,fl8bw,fl9bw,fl10bw,fl11bw,fl12bw,fl13bw,fl14bw,fl15bw,fl16bw,fl17bw,fl18bw,fl19bw,fl20bw,fl21bw,fl22bw,fl23bw,fl24bw,fl25bw,fl26bw,fl27bw]
calcStateResult("TOTAL FLORIDA", fltlat, fltbla, fltwhi, flblat, flbbla, flbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Indiana 1", 714756, in1bl, in1bb, in1bw, in1tl, in1tb, in1tw, 0.45, 0.51, 0.04)
calcResult("Indiana 2", 723483, in2bl, in2bb, in2bw, in2tl, in2tb, in2tw, 0.45, 0.51, 0.04)
calcResult("Indiana 3", 747060, in3bl, in3bb, in3bw, in3tl, in3tb, in3tw, 0.45, 0.51, 0.04)
calcResult("Indiana 4", 768025, in4bl, in4bb, in4bw, in4tl, in4tb, in4tw, 0.45, 0.51, 0.04)
calcResult("Indiana 5", 784462, in5bl, in5bb, in5bw, in5tl, in5tb, in5tw, 0.45, 0.51, 0.04)
calcResult("Indiana 6", 719771, in6bl, in6bb, in6bw, in6tl, in6tb, in6tw, 0.45, 0.51, 0.04)
calcResult("Indiana 7", 760466, in7bl, in7bb, in7bw, in7tl, in7tb, in7tw, 0.45, 0.51, 0.04)
calcResult("Indiana 8", 718591, in8bl, in8bb, in8bw, in8tl, in8tb, in8tw, 0.45, 0.51, 0.04)
calcResult("Indiana 9", 755264, in9bl, in9bb, in9bw, in9tl, in9tb, in9tw, 0.45, 0.51, 0.04)
intlat = [in1tl,in2tl,in3tl,in4tl,in5tl,in6tl,in7tl,in8tl,in9tl]
intbla = [in1tb,in2tb,in3tb,in4tb,in5tb,in6tb,in7tb,in8tb,in9tb]
intwhi = [in1tw,in2tw,in3tw,in4tw,in5tw,in6tw,in7tw,in8tw,in9tw]
inblat = [in1bl,in2bl,in3bl,in4bl,in5bl,in6bl,in7bl,in8bl,in9bl]
inbbla = [in1bb,in2bb,in3bb,in4bb,in5bb,in6bb,in7bb,in8bb,in9bb]
inbwhi = [in1bw,in2bw,in3bw,in4bw,in5bw,in6bw,in7bw,in8bw,in9bw]
calcStateResult("TOTAL INDIANA", intlat, intbla, intwhi, inblat, inbbla, inbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Iowa 1", 773628, ia1bl, ia1bb, ia1bw, ia1tl, ia1tb, ia1tw, 0.45, 0.51, 0.04)
calcResult("Iowa 2", 783983, ia2bl, ia2bb, ia2bw, ia2tl, ia2tb, ia2tw, 0.45, 0.51, 0.04)
calcResult("Iowa 3", 843598, ia3bl, ia3bb, ia3bw, ia3tl, ia3tb, ia3tw, 0.45, 0.51, 0.04)
calcResult("Iowa 4", 754936, ia4bl, ia4bb, ia4bw, ia4tl, ia4tb, ia4tw, 0.45, 0.51, 0.04)
iatlat = [ia1tl,ia2tl,ia3tl,ia4tl]
iatbla = [ia1tb,ia2tb,ia3tb,ia4tb]
iatwhi = [ia1tw,ia2tw,ia3tw,ia4tw]
iablat = [ia1bl,ia2bl,ia3bl,ia4bl]
iabbla = [ia1bb,ia2bb,ia3bb,ia4bb]
iabwhi = [ia1bw,ia2bw,ia3bw,ia4bw]
calcStateResult("TOTAL IOWA", iatlat, iatbla, iatwhi, iablat, iabbla, iabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Illinois 1", 706550, il1bl, il1bb, il1bw, il1tl, il1tb, il1tw, 0.45, 0.51, 0.04)
calcResult("Illinois 2", 694459, il2bl, il2bb, il2bw, il2tl, il2tb, il2tw, 0.45, 0.51, 0.04)
calcResult("Illinois 3", 704050, il3bl, il3bb, il3bw, il3tl, il3tb, il3tw, 0.45, 0.51, 0.04)
calcResult("Illinois 4", 702062, il4bl, il4bb, il4bw, il4tl, il4tb, il4tw, 0.45, 0.51, 0.04)
calcResult("Illinois 5", 743699, il5bl, il5bb, il5bw, il5tl, il5tb, il5tw, 0.45, 0.51, 0.04)
calcResult("Illinois 6", 712712, il6bl, il6bb, il6bw, il6tl, il6tb, il6tw, 0.45, 0.51, 0.04)
calcResult("Illinois 7", 707513, il7bl, il7bb, il7bw, il7tl, il7tb, il7tw, 0.45, 0.51, 0.04)
calcResult("Illinois 8", 724644, il8bl, il8bb, il8bw, il8tl, il8tb, il8tw, 0.45, 0.51, 0.04)
calcResult("Illinois 9", 715584, il9bl, il9bb, il9bw, il9tl, il9tb, il9tw, 0.45, 0.51, 0.04)
calcResult("Illinois 10", 705564, il10bl, il10bb, il10bw, il10tl, il10tb, il10tw, 0.45, 0.51, 0.04)
calcResult("Illinois 11", 722745, il11bl, il11bb, il11bw, il11tl, il11tb, il11tw, 0.45, 0.51, 0.04)
calcResult("Illinois 12", 713289, il12bl, il12bb, il12bw, il12tl, il12tb, il12tw, 0.45, 0.51, 0.04)
calcResult("Illinois 13", 712716, il13bl, il13bb, il13bw, il13tl, il13tb, il13tw, 0.45, 0.51, 0.04)
calcResult("Illinois 14", 718232, il14bl, il14bb, il14bw, il14tl, il14tb, il14tw, 0.45, 0.51, 0.04)
calcResult("Illinois 15", 715066, il15bl, il15bb, il15bw, il15tl, il15tb, il15tw, 0.45, 0.51, 0.04)
calcResult("Illinois 16", 713830, il16bl, il16bb, il16bw, il16tl, il16tb, il16tw, 0.45, 0.51, 0.04)
calcResult("Illinois 17", 711719, il17bl, il17bb, il17bw, il17tl, il17tb, il17tw, 0.45, 0.51, 0.04)
calcResult("Illinois 18", 707238, il18bl, il18bb, il18bw, il18tl, il18tb, il18tw, 0.45, 0.51, 0.04 )
iltlat = [il1tl,il18tl,il2tl,il3tl,il4tl,il5tl,il6tl,il7tl,il8tl,il9tl,il10tl,il11tl,il12tl,il13tl,il14tl,il15tl,il16tl,il17tl,il18tl]
iltbla = [il1tb,il18tb,il2tb,il3tb,il4tb,il5tb,il6tb,il7tb,il8tb,il9tb,il10tb,il11tb,il12tb,il13tb,il14tb,il15tb,il16tb,il17tb,il18tb]
iltwhi = [il1tw,il18tw,il2tw,il3tw,il4tw,il5tw,il6tw,il7tw,il8tw,il9tw,il10tw,il11tw,il12tw,il13tw,il14tw,il15tw,il16tw,il17tw,il18tw]
ilblat = [il1bl,il2bl,il18bl,il3bl,il4bl,il5bl,il6bl,il7bl,il8bl,il9bl,il10bl,il11bl,il12bl,il13bl,il14bl,il15bl,il16bl,il17bl,il18bl]
ilbbla = [il1bb,il2bb,il18bb,il3bb,il4bb,il5bb,il6bb,il7bb,il8bb,il9bb,il10bb,il11bb,il12bb,il13bb,il14bb,il15bb,il16bb,il17bb,il18bb]
ilbwhi = [il1bw,il2bw,il18bw,il3bw,il4bw,il5bw,il6bw,il7bw,il8bw,il9bw,il10bw,il11bw,il12bw,il13bw,il14bw,il15bw,il16bw,il17bw,il18bw]
calcStateResult("TOTAL ILLINOIS", iltlat, iltbla, iltwhi, ilblat, ilbbla, ilbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Idaho 1", 912950, id1bl, id1bb, id1bw, id1tl, id1tb, id1tw, 0.45, 0.51, 0.04)
calcResult("Idaho 2", 841258, id2bl, id2bb, id2bw, id2tl, id2tb, id2tw, 0.45, 0.51, 0.04)
idtlat = [id1tl,id2tl]
idtbla = [id1tb,id2tb]
idtwhi = [id1tw,id2tw]
idblat = [id1bl,id2bl]
idbbla = [id1bb,id2bb]
idbwhi = [id1bw,id2bw]
calcStateResult("TOTAL IDAHO", idtlat, idtbla, idtwhi, idblat, idbbla, idbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Kansas 1", 725222, ks1bl, ks1bb, ks1bw, ks1tl, ks1tb, ks1tw, 0.45, 0.51, 0.04)
calcResult("Kansas 2", 715752, ks2bl, ks2bb, ks2bw, ks2tl, ks2tb, ks2tw, 0.45, 0.51, 0.04)
calcResult("Kansas 3", 672124, ks3bl, ks3bb, ks3bw, ks3tl, ks3tb, ks3tw, 0.45, 0.51, 0.04)
calcResult("Kansas 4", 672101, ks4bl, ks4bb, ks4bw, ks4tl, ks4tb, ks4tw, 0.45, 0.51, 0.04)
kstlat = [ks1tl,ks2tl,ks3tl,ks4tl]
kstbla = [ks1tb,ks2tb,ks3tb,ks4tb]
kstwhi = [ks1tw,ks2tw,ks3tw,ks4tw]
ksblat = [ks1bl,ks2bl,ks3bl,ks4bl]
ksbbla = [ks1bb,ks2bb,ks3bb,ks4bb]
ksbwhi = [ks1bw,ks2bw,ks3bw,ks4bw]
calcStateResult("TOTAL KANSAS", kstlat, kstbla, kstwhi, ksblat, ksbbla, ksbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Kentucky 1", 717739, ky1bl, ky1bb, ky1bw, ky1tl, ky1tb, ky1tw, 0.45, 0.51, 0.04)
calcResult("Kentucky 2", 754967, ky2bl, ky2bb, ky2bw, ky2tl, ky2tb, ky2tw, 0.45, 0.51, 0.04)
calcResult("Kentucky 3", 740860, ky3bl, ky3bb, ky3bw, ky3tl, ky3tb, ky3tw, 0.45, 0.51, 0.04)
calcResult("Kentucky 4", 754502, ky4bl, ky4bb, ky4bw, ky4tl, ky4tb, ky4tw, 0.45, 0.51, 0.04)
calcResult("Kentucky 5", 703315, ky5bl, ky5bb, ky5bw, ky5tl, ky5tb, ky5tw, 0.45, 0.51, 0.04)
calcResult("Kentucky 6", 765591, ky6bl, ky6bb, ky6bw, ky6tl, ky6tb, ky6tw, 0.45, 0.51, 0.04)
kytlat = [ky1tl,ky2tl,ky3tl,ky4tl,ky5tl,ky6tl]
kytbla = [ky1tb,ky2tb,ky3tb,ky4tb,ky5tb,ky6tb]
kytwhi = [ky1tw,ky2tw,ky3tw,ky4tw,ky5tw,ky6tw]
kyblat = [ky1bl,ky2bl,ky3bl,ky4bl,ky5bl,ky6bl]
kybbla = [ky1bb,ky2bb,ky3bb,ky4bb,ky5bb,ky6bb]
kybwhi = [ky1bw,ky2bw,ky3bw,ky4bw,ky5bw,ky6bw]
calcStateResult("TOTAL KENTUCKY", kytlat, kytbla, kytwhi, kyblat, kybbla, kybwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Louisiana 1", 803427, la1bl, la1bb, la1bw, la1tl, la1tb, la1tw, 0.45, 0.51, 0.04)
calcResult("Louisiana 2", 792390, la2bl, la2bb, la2bw, la2tl, la2tb, la2tw, 0.45, 0.51, 0.04)
calcResult("Louisiana 3", 785686, la3bl, la3bb, la3bw, la3tl, la3tb, la3tw, 0.45, 0.51, 0.04)
calcResult("Louisiana 4", 753181, la4bl, la4bb, la4bw, la4tl, la4tb, la4tw, 0.45, 0.51, 0.04)
calcResult("Louisiana 5", 748306, la5bl, la5bb, la5bw, la5tl, la5tb, la5tw, 0.45, 0.51, 0.04)
calcResult("Louisiana 6", 798676, la6bl, la6bb, la6bw, la6tl, la6tb, la6tw, 0.45, 0.51, 0.04)
latlat = [la1tl,la2tl,la3tl,la4tl,la5tl,la6tl]
latbla = [la1tb,la2tb,la3tb,la4tb,la5tb,la6tb]
latwhi = [la1tw,la2tw,la3tw,la4tw,la5tw,la6tw]
lablat = [la1bl,la2bl,la3bl,la4bl,la5bl,la6bl]
labbla = [la1bb,la2bb,la3bb,la4bb,la5bb,la6bb]
labwhi = [la1bw,la2bw,la3bw,la4bw,la5bw,la6bw]
calcStateResult("TOTAL LOUISIANA", latlat, latbla, latwhi, lablat, labbla, labwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Maine 1", 683279, me1bl, me1bb, me1bw, me1tl, me1tb, me1tw, 0.45, 0.51, 0.04)
calcResult("Maine 2", 652869, me2bl, me2bb, me2bw, me2tl, me2tb, me2tw, 0.45, 0.51, 0.04)
metlat = [me1tl,me2tl]
metbla = [me1tb,me2tb]
metwhi = [me1tw,me2tw]
meblat = [me1bl,me2bl]
mebbla = [me1bb,me2bb]
mebwhi = [me1bw,me2bw]
calcStateResult("TOTAL MAINE", metlat, metbla, metwhi, meblat, mebbla, mebwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Maryland 1", 662062, md1bl, md1bb, md1bw, md1tl, md1tb, md1tw, 0.45, 0.51, 0.04)
calcResult("Maryland 2", 745135, md2bl, md2bb, md2bw, md2tl, md2tb, md2tw, 0.45, 0.51, 0.04)
calcResult("Maryland 3", 662062, md3bl, md3bb, md3bw, md3tl, md3tb, md3tw, 0.45, 0.51, 0.04)
calcResult("Maryland 4", 662062, md4bl, md4bb, md4bw, md4tl, md4tb, md4tw, 0.45, 0.51, 0.04)
calcResult("Maryland 5", 662060, md5bl, md5bb, md5bw, md5tl, md5tb, md5tw, 0.45, 0.51, 0.04)
calcResult("Maryland 6", 761921, md6bl, md6bb, md6bw, md6tl, md6tb, md6tw, 0.45, 0.51, 0.04)
calcResult("Maryland 7", 662060, md7bl, md7bb, md7bw, md7tl, md7tb, md7tw, 0.45, 0.51, 0.04)
calcResult("Maryland 8", 756076, md8bl, md8bb, md8bw, md8tl, md8tb, md8tw, 0.45, 0.51, 0.04)
mdtlat = [md1tl,md2tl,md3tl,md4tl,md5tl,md6tl,md7tl,md8tl]
mdtbla = [md1tb,md2tb,md3tb,md4tb,md5tb,md6tb,md7tb,md8tb]
mdtwhi = [md1tw,md2tw,md3tw,md4tw,md5tw,md6tw,md7tw,md8tw]
mdblat = [md1bl,md2bl,md3bl,md4bl,md5bl,md6bl,md7bl,md8bl]
mdbbla = [md1bb,md2bb,md3bb,md4bb,md5bb,md6bb,md7bb,md8bb]
mdbwhi = [md1bw,md2bw,md3bw,md4bw,md5bw,md6bw,md7bw,md8bw]
calcStateResult("TOTAL MARYLAND", mdtlat, mdtbla, mdtwhi, mdblat, mdbbla, mdbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Massachusetts 1", 634479, ma1bl, ma1bb, ma1bw, ma1tl, ma1tb, ma1tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 2", 661045, ma2bl, ma2bb, ma2bw, ma2tl, ma2tb, ma2tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 3", 664919, ma3bl, ma3bb, ma3bw, ma3tl, ma3tb, ma3tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 4", 656083, ma4bl, ma4bb, ma4bw, ma4tl, ma4tb, ma4tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 5", 662269, ma5bl, ma5bb, ma5bw, ma5tl, ma5tb, ma5tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 6", 636554, ma6bl, ma6bb, ma6bw, ma6tl, ma6tb, ma6tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 7", 648162, ma7bl, ma7bb, ma7bw, ma7tl, ma7tb, ma7tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 8", 764789, ma8bl, ma8bb, ma8bw, ma8tl, ma8tb, ma8tw, 0.45, 0.51, 0.04)
calcResult("Massachusetts 9", 650381, ma9bl, ma9bb, ma9bw, ma9tl, ma9tb, ma9tw, 0.45, 0.51, 0.04)
matlat = [ma1tl,ma2tl,ma3tl,ma4tl,ma5tl,ma6tl,ma7tl,ma8tl,ma9tl]
matbla = [ma1tb,ma2tb,ma3tb,ma4tb,ma5tb,ma6tb,ma7tb,ma8tb,ma9tb]
matwhi = [ma1tw,ma2tw,ma3tw,ma4tw,ma5tw,ma6tw,ma7tw,ma8tw,ma9tw]
mablat = [ma1bl,ma2bl,ma3bl,ma4bl,ma5bl,ma6bl,ma7bl,ma8bl,ma9bl]
mabbla = [ma1bb,ma2bb,ma3bb,ma4bb,ma5bb,ma6bb,ma7bb,ma8bb,ma9bb]
mabwhi = [ma1bw,ma2bw,ma3bw,ma4bw,ma5bw,ma6bw,ma7bw,ma8bw,ma9bw]
calcStateResult("TOTAL MASSACHUSETTS", matlat, matbla, matwhi, mablat, mabbla, mabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Michigan 1", 699621, mi1bl, mi1bb, mi1bw, mi1tl, mi1tb, mi1tw, 0.45, 0.51, 0.04)
calcResult("Michigan 2", 743361, mi2bl, mi2bb, mi2bw, mi2tl, mi2tb, mi2tw, 0.45, 0.51, 0.04)
calcResult("Michigan 3", 749975, mi3bl, mi3bb, mi3bw, mi3tl, mi3tb, mi3tw, 0.45, 0.51, 0.04)
calcResult("Michigan 4", 704592, mi4bl, mi4bb, mi4bw, mi4tl, mi4tb, mi4tw, 0.45, 0.51, 0.04)
calcResult("Michigan 5", 671115, mi5bl, mi5bb, mi5bw, mi5tl, mi5tb, mi5tw, 0.45, 0.51, 0.04)
calcResult("Michigan 6", 705974, mi6bl, mi6bb, mi6bw, mi6tl, mi6tb, mi6tw, 0.45, 0.51, 0.04)
calcResult("Michigan 7", 705974, mi7bl, mi7bb, mi7bw, mi7tl, mi7tb, mi7tw, 0.45, 0.51, 0.04)
calcResult("Michigan 8", 705918, mi8bl, mi8bb, mi8bw, mi8tl, mi8tb, mi8tw, 0.45, 0.51, 0.04)
calcResult("Michigan 9", 705975, mi9bl, mi9bb, mi9bw, mi9tl, mi9tb, mi9tw, 0.45, 0.51, 0.04)
calcResult("Michigan 10", 705974, mi10bl, mi10bb, mi10bw, mi10tl, mi10tb, mi10tw, 0.45, 0.51, 0.04)
calcResult("Michigan 11", 733920, mi11bl, mi11bb, mi11bw, mi11tl, mi11tb, mi11tw, 0.45, 0.51, 0.04)
calcResult("Michigan 12", 705974, mi12bl, mi12bb, mi12bw, mi12tl, mi12tb, mi12tw, 0.45, 0.51, 0.04)
calcResult("Michigan 13", 705974, mi13bl, mi13bb, mi13bw, mi13tl, mi13tb, mi13tw, 0.45, 0.51, 0.04)
calcResult("Michigan 14", 705974, mi14bl, mi14bb, mi14bw, mi14tl, mi14tb, mi14tw, 0.45, 0.51, 0.04)
mitlat = [mi1tl,mi2tl,mi3tl,mi4tl,mi5tl,mi6tl,mi7tl,mi8tl,mi9tl,mi10tl,mi11tl,mi12tl,mi13tl,mi14tl]
mitbla = [mi1tb,mi2tb,mi3tb,mi4tb,mi5tb,mi6tb,mi7tb,mi8tb,mi9tb,mi10tb,mi11tb,mi12tb,mi13tb,mi14tb]
mitwhi = [mi1tw,mi2tw,mi3tw,mi4tw,mi5tw,mi6tw,mi7tw,mi8tw,mi9tw,mi10tw,mi11tw,mi12tw,mi13tw,mi14tw]
miblat = [mi1bl,mi2bl,mi3bl,mi4bl,mi5bl,mi6bl,mi7bl,mi8bl,mi9bl,mi10bl,mi11bl,mi12bl,mi13bl,mi14bl]
mibbla = [mi1bb,mi2bb,mi3bb,mi4bb,mi5bb,mi6bb,mi7bb,mi8bb,mi9bb,mi10bb,mi11bb,mi12bb,mi13bb,mi14bb]
mibwhi = [mi1bw,mi2bw,mi3bw,mi4bw,mi5bw,mi6bw,mi7bw,mi8bw,mi9bw,mi10bw,mi11bw,mi12bw,mi13bw,mi14bw]
calcStateResult("TOTAL MICHIGAN", mitlat, mitbla, mitwhi, miblat, mibbla, mibwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Mississippi 1", 762914, ms1bl, ms1bb, ms1bw, ms1tl, ms1tb, ms1tw, 0.45, 0.51, 0.04)
calcResult("Mississippi 2", 711164, ms2bl, ms2bb, ms2bw, ms2tl, ms2tb, ms2tw, 0.45, 0.51, 0.04)
calcResult("Mississippi 3", 711115, ms3bl, ms3bb, ms3bw, ms3tl, ms3tb, ms3tw, 0.45, 0.51, 0.04)
calcResult("Mississippi 4", 711219, ms4bl, ms4bb, ms4bw, ms4tl, ms4tb, ms4tw, 0.45, 0.51, 0.04)
mstlat = [ms1tl,ms2tl,ms3tl,ms4tl]
mstbla = [ms1tb,ms2tb,ms3tb,ms4tb]
mstwhi = [ms1tw,ms2tw,ms3tw,ms4tw]
msblat = [ms1bl,ms2bl,ms3bl,ms4bl]
msbbla = [ms1bb,ms2bb,ms3bb,ms4bb]
msbwhi = [ms1bw,ms2bw,ms3bw,ms4bw]
calcStateResult("TOTAL MISSISSIPPI", mstlat, mstbla, mstwhi, msblat, msbbla, msbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Missouri 1", 728365, mo1bl, mo1bb, mo1bw, mo1tl, mo1tb, mo1tw, 0.45, 0.51, 0.04)
calcResult("Missouri 2", 706622, mo2bl, mo2bb, mo2bw, mo2tl, mo2tb, mo2tw, 0.45, 0.51, 0.04)
calcResult("Missouri 3", 625251, mo3bl, mo3bb, mo3bw, mo3tl, mo3tb, mo3tw, 0.45, 0.51, 0.04)
calcResult("Missouri 4", 679375, mo4bl, mo4bb, mo4bw, mo4tl, mo4tb, mo4tw, 0.45, 0.51, 0.04)
calcResult("Missouri 5", 757920, mo5bl, mo5bb, mo5bw, mo5tl, mo5tb, mo5tw, 0.45, 0.51, 0.04)
calcResult("Missouri 6", 693974, mo6bl, mo6bb, mo6bw, mo6tl, mo6tb, mo6tw, 0.45, 0.51, 0.04)
calcResult("Missouri 7", 748406, mo7bl, mo7bb, mo7bw, mo7tl, mo7tb, mo7tw, 0.45, 0.51, 0.04)
calcResult("Missouri 8", 749444, mo8bl, mo8bb, mo8bw, mo8tl, mo8tb, mo8tw, 0.45, 0.51, 0.04)
motlat = [mo1tl,mo2tl,mo3tl,mo4tl,mo5tl,mo6tl,mo7tl,mo8tl]
motbla = [mo1tb,mo2tb,mo3tb,mo4tb,mo5tb,mo6tb,mo7tb,mo8tb]
motwhi = [mo1tw,mo2tw,mo3tw,mo4tw,mo5tw,mo6tw,mo7tw,mo8tw]
moblat = [mo1bl,mo2bl,mo3bl,mo4bl,mo5bl,mo6bl,mo7bl,mo8bl]
mobbla = [mo1bb,mo2bb,mo3bb,mo4bb,mo5bb,mo6bb,mo7bb,mo8bb]
mobwhi = [mo1bw,mo2bw,mo3bw,mo4bw,mo5bw,mo6bw,mo7bw,mo8bw]
calcStateResult("TOTAL MISSOURI", motlat, motbla, motwhi, moblat, mobbla, mobwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Minnesota 1", 678418, mn1bl, mn1bb, mn1bw, mn1tl, mn1tb, mn1tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 2", 714141, mn2bl, mn2bb, mn2bw, mn2tl, mn2tb, mn2tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 3", 723994, mn3bl, mn3bb, mn3bw, mn3tl, mn3tb, mn3tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 4", 717766, mn4bl, mn4bb, mn4bw, mn4tl, mn4tb, mn4tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 5", 718802, mn5bl, mn5bb, mn5bw, mn5tl, mn5tb, mn5tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 6", 722715, mn6bl, mn6bb, mn6bw, mn6tl, mn6tb, mn6tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 7", 663069, mn7bl, mn7bb, mn7bw, mn7tl, mn7tb, mn7tw, 0.45, 0.51, 0.04)
calcResult("Minnesota 8", 672274, mn8bl, mn8bb, mn8bw, mn8tl, mn8tb, mn8tw, 0.45, 0.51, 0.04)
mntlat = [mn1tl,mn2tl,mn3tl,mn4tl,mn5tl,mn6tl,mn7tl,mn8tl]
mntbla = [mn1tb,mn2tb,mn3tb,mn4tb,mn5tb,mn6tb,mn7tb,mn8tb]
mntwhi = [mn1tw,mn2tw,mn3tw,mn4tw,mn5tw,mn6tw,mn7tw,mn8tw]
mnblat = [mn1bl,mn2bl,mn3bl,mn4bl,mn5bl,mn6bl,mn7bl,mn8bl]
mnbbla = [mn1bb,mn2bb,mn3bb,mn4bb,mn5bb,mn6bb,mn7bb,mn8bb]
mnbwhi = [mn1bw,mn2bw,mn3bw,mn4bw,mn5bw,mn6bw,mn7bw,mn8bw]
calcStateResult("TOTAL MINNESOTA", mntlat, mntbla, mntwhi, mnblat, mnbbla, mnbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("New Jersey 1", 729675, nj1bl, nj1bb, nj1bw, nj1tl, nj1tb, nj1tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 2", 713380, nj2bl, nj2bb, nj2bw, nj2tl, nj2tb, nj2tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 3", 742905, nj3bl, nj3bb, nj3bw, nj3tl, nj3tb, nj3tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 4", 756825, nj4bl, nj4bb, nj4bw, nj4tl, nj4tb, nj4tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 5", 746385, nj5bl, nj5bb, nj5bw, nj5tl, nj5tb, nj5tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 6", 742483, nj6bl, nj6bb, nj6bw, nj6tl, nj6tb, nj6tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 7", 754222, nj7bl, nj7bb, nj7bw, nj7tl, nj7tb, nj7tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 8", 777484, nj8bl, nj8bb, nj8bw, nj8tl, nj8tb, nj8tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 9", 769504, nj9bl, nj9bb, nj9bw, nj9tl, nj9tb, nj9tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 10", 781893, nj10bl, nj10bb, nj10bw, nj10tl, nj10tb, nj10tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 11", 729569, nj11bl, nj11bb, nj11bw, nj11tl, nj11tb, nj11tw, 0.45, 0.51, 0.04)
calcResult("New Jersey 12", 758189, nj12bl, nj12bb, nj12bw, nj12tl, nj12tb, nj12tw, 0.45, 0.51, 0.04)
njtlat = [nj1tl,nj2tl,nj3tl,nj4tl,nj5tl,nj6tl,nj7tl,nj8tl,nj9tl,nj10tl,nj11tl,nj12tl]
njtbla = [nj1tb,nj2tb,nj3tb,nj4tb,nj5tb,nj6tb,nj7tb,nj8tb,nj9tb,nj10tb,nj11tb,nj12tb]
njtwhi = [nj1tw,nj2tw,nj3tw,nj4tw,nj5tw,nj6tw,nj7tw,nj8tw,nj9tw,nj10tw,nj11tw,nj12tw]
njblat = [nj1bl,nj2bl,nj3bl,nj4bl,nj5bl,nj6bl,nj7bl,nj8bl,nj9bl,nj10bl,nj11bl,nj12bl]
njbbla = [nj1bb,nj2bb,nj3bb,nj4bb,nj5bb,nj6bb,nj7bb,nj8bb,nj9bb,nj10bb,nj11bb,nj12bb]
njbwhi = [nj1bw,nj2bw,nj3bw,nj4bw,nj5bw,nj6bw,nj7bw,nj8bw,nj9bw,nj10bw,nj11bw,nj12bw]
calcStateResult("TOTAL NEW JERSEY", njtlat, njtbla, njtwhi, njblat, njbbla, njbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("New Mexico 1", 690571, nm1bl, nm1bb, nm1bw, nm1tl, nm1tb, nm1tw, 0.45, 0.51, 0.04)
calcResult("New Mexico 2", 606406, nm2bl, nm2bb, nm2bw, nm2tl, nm2tb, nm2tw, 0.45, 0.51, 0.04)
calcResult("New Mexico 3", 698251, nm3bl, nm3bb, nm3bw, nm3tl, nm3tb, nm3tw, 0.45, 0.51, 0.04)
nmtlat = [nm1tl,nm2tl,nm3tl]
nmtbla = [nm1tb,nm2tb,nm3tb]
nmtwhi = [nm1tw,nm2tw,nm3tw]
nmblat = [nm1bl,nm2bl,nm3bl]
nmbbla = [nm1bb,nm2bb,nm3bb]
nmbwhi = [nm1bw,nm2bw,nm3bw]
calcStateResult("TOTAL NEW MEXICO", nmtlat, nmtbla, nmtwhi, nmblat, nmbbla, nmbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Nebraska 1", 616728, ne1bl, ne1bb, ne1bw, ne1tl, ne1tb, ne1tw, 0.45, 0.51, 0.04)
calcResult("Nebraska 2", 652870, ne2bl, ne2bb, ne2bw, ne2tl, ne2tb, ne2tw, 0.45, 0.51, 0.04)
calcResult("Nebraska 3", 602579, ne3bl, ne3bb, ne3bw, ne3tl, ne3tb, ne3tw, 0.45, 0.51, 0.04)
netlat = [ne1tl,ne2tl,ne3tl]
netbla = [ne1tb,ne2tb,ne3tb]
netwhi = [ne1tw,ne2tw,ne3tw]
neblat = [ne1bl,ne2bl,ne3bl]
nebbla = [ne1bb,ne2bb,ne3bb]
nebwhi = [ne1bw,ne2bw,ne3bw]
calcStateResult("TOTAL NEBRASKA", netlat, netbla, netwhi, neblat, nebbla, nebwhi, 0.45, 0.51, 0.04)
print("")
calcResult("New Hampshire 1", 673194, nh1bl, nh1bb, nh1bw, nh1tl, nh1tb, nh1tw, 0.45, 0.51, 0.04)
calcResult("New Hampshire 2", 669601, nh2bl, nh2bb, nh2bw, nh2tl, nh2tb, nh2tw, 0.45, 0.51, 0.04)
nhtlat = [nh1tl,nh2tl]
nhtbla = [nh1tb,nh2tb]
nhtwhi = [nh1tw,nh2tw]
nhblat = [nh1bl,nh2bl]
nhbbla = [nh1bb,nh2bb]
nhbwhi = [nh1bw,nh2bw]
calcStateResult("TOTAL NEW HAMPSHIRE", nhtlat, nhtbla, nhtwhi, nhblat, nhbbla, nhbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Nevada 1", 722331, nv1bl, nv1bb, nv1bw, nv1tl, nv1tb, nv1tw, 0.45, 0.51, 0.04)
calcResult("Nevada 2", 713779, nv2bl, nv2bb, nv2bw, nv2tl, nv2tb, nv2tw, 0.45, 0.51, 0.04)
calcResult("Nevada 3", 779908, nv3bl, nv3bb, nv3bw, nv3tl, nv3tb, nv3tw, 0.45, 0.51, 0.04)
calcResult("Nevada 4", 724040, nv4bl, nv4bb, nv4bw, nv4tl, nv4tb, nv4tw, 0.45, 0.51, 0.04)
nvtlat = [nv1tl,nv2tl,nv3tl,nv4tl]
nvtbla = [nv1tb,nv2tb,nv3tb,nv4tb]
nvtwhi = [nv1tw,nv2tw,nv3tw,nv4tw]
nvblat = [nv1bl,nv2bl,nv3bl,nv4bl]
nvbbla = [nv1bb,nv2bb,nv3bb,nv4bb]
nvbwhi = [nv1bw,nv2bw,nv3bw,nv4bw]
calcStateResult("TOTAL NEVADA", nvtlat, nvtbla, nvtwhi, nvblat, nvbbla, nvbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("North Carolina 1", 750278, nc1bl, nc1bb, nc1bw, nc1tl, nc1tb, nc1tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 2", 819899, nc2bl, nc2bb, nc2bw, nc2tl, nc2tb, nc2tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 3", 749823, nc3bl, nc3bb, nc3bw, nc3tl, nc3tb, nc3tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 4", 847032, nc4bl, nc4bb, nc4bw, nc4tl, nc4tb, nc4tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 5", 751232, nc5bl, nc5bb, nc5bw, nc5tl, nc5tb, nc5tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 6", 763491, nc6bl, nc6bb, nc6bw, nc6tl, nc6tb, nc6tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 7", 780442, nc7bl, nc7bb, nc7bw, nc7tl, nc7tb, nc7tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 8", 774967, nc8bl, nc8bb, nc8bw, nc8tl, nc8tb, nc8tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 9", 778477, nc9bl, nc9bb, nc9bw, nc9tl, nc9tb, nc9tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 10", 759453, nc10bl, nc10bb, nc10bw, nc10tl, nc10tb, nc10tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 11", 768166, nc11bl, nc11bb, nc11bw, nc11tl, nc11tb, nc11tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 12", 849357, nc12bl, nc12bb, nc12bw, nc12tl, nc12tb, nc12tw, 0.45, 0.51, 0.04)
calcResult("North Carolina 13", 768213, nc13bl, nc13bb, nc13bw, nc13tl, nc13tb, nc13tw, 0.45, 0.51, 0.04)
nctlat = [nc1tl,nc2tl,nc3tl,nc4tl,nc5tl,nc6tl,nc7tl,nc8tl,nc9tl,nc10tl,nc11tl,nc12tl,nc13tl]
nctbla = [nc1tb,nc2tb,nc3tb,nc4tb,nc5tb,nc6tb,nc7tb,nc8tb,nc9tb,nc10tb,nc11tb,nc12tb,nc13tb]
nctwhi = [nc1tw,nc2tw,nc3tw,nc4tw,nc5tw,nc6tw,nc7tw,nc8tw,nc9tw,nc10tw,nc11tw,nc12tw,nc13tw]
ncblat = [nc1bl,nc2bl,nc3bl,nc4bl,nc5bl,nc6bl,nc7bl,nc8bl,nc9bl,nc10bl,nc11bl,nc12bl,nc13bl]
ncbbla = [nc1bb,nc2bb,nc3bb,nc4bb,nc5bb,nc6bb,nc7bb,nc8bb,nc9bb,nc10bb,nc11bb,nc12bb,nc13bb]
ncbwhi = [nc1bw,nc2bw,nc3bw,nc4bw,nc5bw,nc6bw,nc7bw,nc8bw,nc9bw,nc10bw,nc11bw,nc12bw,nc13bw]
calcStateResult("TOTAL NORTH CAROLINA", nctlat, nctbla, nctwhi, ncblat, ncbbla, ncbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("New York 1", 717707, ny1bl, ny1bb, ny1bw, ny1tl, ny1tb, ny1tw, 0.45, 0.51, 0.04)
calcResult("New York 2", 717708, ny2bl, ny2bb, ny2bw, ny2tl, ny2tb, ny2tw, 0.45, 0.51, 0.04)
calcResult("New York 3", 717707, ny3bl, ny3bb, ny3bw, ny3tl, ny3tb, ny3tw, 0.45, 0.51, 0.04)
calcResult("New York 4", 717708, ny4bl, ny4bb, ny4bw, ny4tl, ny4tb, ny4tw, 0.45, 0.51, 0.04)
calcResult("New York 5", 717708, ny5bl, ny5bb, ny5bw, ny5tl, ny5tb, ny5tw, 0.45, 0.51, 0.04)
calcResult("New York 6", 717707, ny6bl, ny6bb, ny6bw, ny6tl, ny6tb, ny6tw, 0.45, 0.51, 0.04)
calcResult("New York 7", 717708, ny7bl, ny7bb, ny7bw, ny7tl, ny7tb, ny7tw, 0.45, 0.51, 0.04)
calcResult("New York 8", 717708, ny8bl, ny8bb, ny8bw, ny8tl, ny8tb, ny8tw, 0.45, 0.51, 0.04)
calcResult("New York 9", 717708, ny9bl, ny9bb, ny9bw, ny9tl, ny9tb, ny9tw, 0.45, 0.51, 0.04)
calcResult("New York 10", 717707, ny10bl, ny10bb, ny10bw, ny10tl, ny10tb, ny10tw, 0.45, 0.51, 0.04)
calcResult("New York 11", 717708, ny11bl, ny11bb, ny11bw, ny11tl, ny11tb, ny11tw, 0.45, 0.51, 0.04)
calcResult("New York 12", 717707, ny12bl, ny12bb, ny12bw, ny12tl, ny12tb, ny12tw, 0.45, 0.51, 0.04)
calcResult("New York 13", 717707, ny13bl, ny13bb, ny13bw, ny13tl, ny13tb, ny13tw, 0.45, 0.51, 0.04)
calcResult("New York 14", 706440, ny14bl, ny14bb, ny14bw, ny14tl, ny14tb, ny14tw, 0.45, 0.51, 0.04)
calcResult("New York 15", 743959, ny15bl, ny15bb, ny15bw, ny15tl, ny15tb, ny15tw, 0.45, 0.51, 0.04)
calcResult("New York 16", 732981, ny16bl, ny16bb, ny16bw, ny16tl, ny16tb, ny16tw, 0.45, 0.51, 0.04)
calcResult("New York 17", 741445, ny17bl, ny17bb, ny17bw, ny17tl, ny17tb, ny17tw, 0.45, 0.51, 0.04)
calcResult("New York 18", 722226, ny18bl, ny18bb, ny18bw, ny18tl, ny18tb, ny18tw, 0.45, 0.51, 0.04)
calcResult("New York 19", 700310, ny19bl, ny19bb, ny19bw, ny19tl, ny19tb, ny19tw, 0.45, 0.51, 0.04)
calcResult("New York 20", 722529, ny20bl, ny20bb, ny20bw, ny20tl, ny20tb, ny20tw, 0.45, 0.51, 0.04)
calcResult("New York 21", 701112, ny21bl, ny21bb, ny21bw, ny21tl, ny21tb, ny21tw, 0.45, 0.51, 0.04)
calcResult("New York 22", 697372, ny22bl, ny22bb, ny22bw, ny22tl, ny22tb, ny22tw, 0.45, 0.51, 0.04)
calcResult("New York 23", 693764, ny23bl, ny23bb, ny23bw, ny23tl, ny23tb, ny23tw, 0.45, 0.51, 0.04)
calcResult("New York 24", 701664, ny24bl, ny24bb, ny24bw, ny24tl, ny24tb, ny24tw, 0.45, 0.51, 0.04)
calcResult("New York 25", 718565, ny25bl, ny25bb, ny25bw, ny25tl, ny25tb, ny25tw, 0.45, 0.51, 0.04)
calcResult("New York 26", 707190, ny26bl, ny26bb, ny26bw, ny26tl, ny26tb, ny26tw, 0.45, 0.51, 0.04)
calcResult("New York 27", 712904, ny27bl, ny27bb, ny27bw, ny27tl, ny27tb, ny27tw, 0.45, 0.51, 0.04)
nytlat = [ny1tl,ny2tl,ny3tl,ny4tl,ny5tl,ny6tl,ny7tl,ny8tl,ny9tl,ny10tl,ny11tl,ny12tl,ny13tl,ny14tl,ny15tl,ny16tl,ny17tl,ny18tl,ny19tl,ny20tl,ny21tl,ny22tl,ny23tl,ny24tl,ny25tl,ny26tl,ny27tl]
nytbla = [ny1tb,ny2tb,ny3tb,ny4tb,ny5tb,ny6tb,ny7tb,ny8tb,ny9tb,ny10tb,ny11tb,ny12tb,ny13tb,ny14tb,ny15tb,ny16tb,ny17tb,ny18tb,ny19tb,ny20tb,ny21tb,ny22tb,ny23tb,ny24tb,ny25tb,ny26tb,ny27tb]
nytwhi = [ny1tw,ny2tw,ny3tw,ny4tw,ny5tw,ny6tw,ny7tw,ny8tw,ny9tw,ny10tw,ny11tw,ny12tw,ny13tw,ny14tw,ny15tw,ny16tw,ny17tw,ny18tw,ny19tw,ny20tw,ny21tw,ny22tw,ny23tw,ny24tw,ny25tw,ny26tw,ny27tw]
nyblat = [ny1bl,ny2bl,ny3bl,ny4bl,ny5bl,ny6bl,ny7bl,ny8bl,ny9bl,ny10bl,ny11bl,ny12bl,ny13bl,ny14bl,ny15bl,ny16bl,ny17bl,ny18bl,ny19bl,ny20bl,ny21bl,ny22bl,ny23bl,ny24bl,ny25bl,ny26bl,ny27bl]
nybbla = [ny1bb,ny2bb,ny3bb,ny4bb,ny5bb,ny6bb,ny7bb,ny8bb,ny9bb,ny10bb,ny11bb,ny12bb,ny13bb,ny14bb,ny15bb,ny16bb,ny17bb,ny18bb,ny19bb,ny20bb,ny21bb,ny22bb,ny23bb,ny24bb,ny25bb,ny26bb,ny27bb]
nybwhi = [ny1bw,ny2bw,ny3bw,ny4bw,ny5bw,ny6bw,ny7bw,ny8bw,ny9bw,ny10bw,ny11bw,ny12bw,ny13bw,ny14bw,ny15bw,ny16bw,ny17bw,ny18bw,ny19bw,ny20bw,ny21bw,ny22bw,ny23bw,ny24bw,ny25bw,ny26bw,ny27bw]
calcStateResult("TOTAL NEW YORK", nytlat, nytbla, nytwhi, nyblat, nybbla, nybwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Ohio 1", 739216, oh1bl, oh1bb, oh1bw, oh1tl, oh1tb, oh1tw, 0.45, 0.51, 0.04)
calcResult("Ohio 2", 724451, oh2bl, oh2bb, oh2bw, oh2tl, oh2tb, oh2tw, 0.45, 0.51, 0.04)
calcResult("Ohio 3", 787306, oh3bl, oh3bb, oh3bw, oh3tl, oh3tb, oh3tw, 0.45, 0.51, 0.04)
calcResult("Ohio 4", 707219, oh4bl, oh4bb, oh4bw, oh4tl, oh4tb, oh4tw, 0.45, 0.51, 0.04)
calcResult("Ohio 5", 720730, oh5bl, oh5bb, oh5bw, oh5tl, oh5tb, oh5tw, 0.45, 0.51, 0.04)
calcResult("Ohio 6", 703190, oh6bl, oh6bb, oh6bw, oh6tl, oh6tb, oh6tw, 0.45, 0.51, 0.04)
calcResult("Ohio 7", 728336, oh7bl, oh7bb, oh7bw, oh7tl, oh7tb, oh7tw, 0.45, 0.51, 0.04)
calcResult("Ohio 8", 727853, oh8bl, oh8bb, oh8bw, oh8tl, oh8tb, oh8tw, 0.45, 0.51, 0.04)
calcResult("Ohio 9", 706201, oh9bl, oh9bb, oh9bw, oh9tl, oh9tb, oh9tw, 0.45, 0.51, 0.04)
calcResult("Ohio 10", 720354, oh10bl, oh10bb, oh10bw, oh10tl, oh10tb, oh10tw, 0.45, 0.51, 0.04)
calcResult("Ohio 11", 692226, oh11bl, oh11bb, oh11bw, oh11tl, oh11tb, oh11tw, 0.45, 0.51, 0.04)
calcResult("Ohio 12", 789634, oh12bl, oh12bb, oh12bw, oh12tl, oh12tb, oh12tw, 0.45, 0.51, 0.04)
calcResult("Ohio 13", 709683, oh13bl, oh13bb, oh13bw, oh13tl, oh13tb, oh13tw, 0.45, 0.51, 0.04)
calcResult("Ohio 14", 710875, oh14bl, oh14bb, oh14bw, oh14tl, oh14tb, oh14tw, 0.45, 0.51, 0.04)
calcResult("Ohio 15", 743623, oh15bl, oh15bb, oh15bw, oh15tl, oh15tb, oh15tw, 0.45, 0.51, 0.04)
calcResult("Ohio 16", 727600, oh16bl, oh16bb, oh16bw, oh16tl, oh16tb, oh16tw, 0.45, 0.51, 0.04)
ohtlat = [oh1tl,oh2tl,oh3tl,oh4tl,oh5tl,oh6tl,oh7tl,oh8tl,oh9tl,oh10tl,oh11tl,oh12tl,oh13tl,oh14tl,oh15tl,oh16tl]
ohtbla = [oh1tb,oh2tb,oh3tb,oh4tb,oh5tb,oh6tb,oh7tb,oh8tb,oh9tb,oh10tb,oh11tb,oh12tb,oh13tb,oh14tb,oh15tb,oh16tb]
ohtwhi = [oh1tw,oh2tw,oh3tw,oh4tw,oh5tw,oh6tw,oh7tw,oh8tw,oh9tw,oh10tw,oh11tw,oh12tw,oh13tw,oh14tw,oh15tw,oh16tw]
ohblat = [oh1bl,oh2bl,oh3bl,oh4bl,oh5bl,oh6bl,oh7bl,oh8bl,oh9bl,oh10bl,oh11bl,oh12bl,oh13bl,oh14bl,oh15bl,oh16bl]
ohbbla = [oh1bb,oh2bb,oh3bb,oh4bb,oh5bb,oh6bb,oh7bb,oh8bb,oh9bb,oh10bb,oh11bb,oh12bb,oh13bb,oh14bb,oh15bb,oh16bb]
ohbwhi = [oh1bw,oh2bw,oh3bw,oh4bw,oh5bw,oh6bw,oh7bw,oh8bw,oh9bw,oh10bw,oh11bw,oh12bw,oh13bw,oh14bw,oh15bw,oh16bw]
calcStateResult("TOTAL OHIO", ohtlat, ohtbla, ohtwhi, ohblat, ohbbla, ohbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Oregon 1", 844175, or1bl, or1bb, or1bw, or1tl, or1tb, or1tw, 0.45, 0.51, 0.04)
calcResult("Oregon 2", 684280, or2bl, or2bb, or2bw, or2tl, or2tb, or2tw, 0.45, 0.51, 0.04)
calcResult("Oregon 3", 684279, or3bl, or3bb, or3bw, or3tl, or3tb, or3tw, 0.45, 0.51, 0.04)
calcResult("Oregon 4", 684280, or4bl, or4bb, or4bw, or4tl, or4tb, or4tw, 0.45, 0.51, 0.04)
calcResult("Oregon 5", 684280, or5bl, or5bb, or5bw, or5tl, or5tb, or5tw, 0.45, 0.51, 0.04)
ortlat = [or1tl,or2tl,or3tl,or4tl,or5tl]
ortbla = [or1tb,or2tb,or3tb,or4tb,or5tb]
ortwhi = [or1tw,or2tw,or3tw,or4tw,or5tw]
orblat = [or1bl,or2bl,or3bl,or4bl,or5bl]
orbbla = [or1bb,or2bb,or3bb,or4bb,or5bb]
orbwhi = [or1bw,or2bw,or3bw,or4bw,or5bw]
calcStateResult("TOTAL OREGON", ortlat, ortbla, ortwhi, orblat, orbbla, orbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Oklahoma 1", 754310, ok1bl, ok1bb, ok1bw, ok1tl, ok1tb, ok1tw, 0.45, 0.51, 0.04)
calcResult("Oklahoma 2", 690131, ok2bl, ok2bb, ok2bw, ok2tl, ok2tb, ok2tw, 0.45, 0.51, 0.04)
calcResult("Oklahoma 3", 690131, ok3bl, ok3bb, ok3bw, ok3tl, ok3tb, ok3tw, 0.45, 0.51, 0.04)
calcResult("Oklahoma 4", 785424, ok4bl, ok4bb, ok4bw, ok4tl, ok4tb, ok4tw, 0.45, 0.51, 0.04)
calcResult("Oklahoma 5", 818162, ok5bl, ok5bb, ok5bw, ok5tl, ok5tb, ok5tw, 0.45, 0.51, 0.04)
oktlat = [ok1tl,ok2tl,ok3tl,ok4tl,ok5tl]
oktbla = [ok1tb,ok2tb,ok3tb,ok4tb,ok5tb]
oktwhi = [ok1tw,ok2tw,ok3tw,ok4tw,ok5tw]
okblat = [ok1bl,ok2bl,ok3bl,ok4bl,ok5bl]
okbbla = [ok1bb,ok2bb,ok3bb,ok4bb,ok5bb]
okbwhi = [ok1bw,ok2bw,ok3bw,ok4bw,ok5bw]
calcStateResult("TOTAL OKLAHOMA", oktlat, oktbla, oktwhi, okblat, okbbla, okbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Hawaii 1", 692981, hi1bl, hi1bb, hi1bw, hi1tl, hi1tb, hi1tw, 0.45, 0.51, 0.04)
calcResult("Hawaii 2", 699332, hi2bl, hi2bb, hi2bw, hi2tl, hi2tb, hi2tw, 0.45, 0.51, 0.04)
hitlat = [hi1tl,hi2tl]
hitbla = [hi1tb,hi2tb]
hitwhi = [hi1tw,hi2tw]
hiblat = [hi1bl,hi2bl]
hibbla = [hi1bb,hi2bb]
hibwhi = [hi1bw,hi2bw]
calcStateResult("TOTAL HAWAII", hitlat, hitbla, hitwhi, hiblat, hibbla, hibwhi, 0.45, 0.51, 0.04)
print("")
calcResult("South Carolina 1", 668668, sc1bl, sc1bb, sc1bw, sc1tl, sc1tb, sc1tw, 0.45, 0.51, 0.04)
calcResult("South Carolina 2", 668668, sc2bl, sc2bb, sc2bw, sc2tl, sc2tb, sc2tw, 0.45, 0.51, 0.04)
calcResult("South Carolina 3", 668668, sc3bl, sc3bb, sc3bw, sc3tl, sc3tb, sc3tw, 0.45, 0.51, 0.04)
calcResult("South Carolina 4", 709631, sc4bl, sc4bb, sc4bw, sc4tl, sc4tb, sc4tw, 0.45, 0.51, 0.04)
calcResult("South Carolina 5", 678910, sc5bl, sc5bb, sc5bw, sc5tl, sc5tb, sc5tw, 0.45, 0.51, 0.04)
calcResult("South Carolina 6", 668670, sc6bl, sc6bb, sc6bw, sc6tl, sc6tb, sc6tw, 0.45, 0.51, 0.04 )
calcResult("South Carolina 7", 667752, sc7bl, sc7bb, sc7bw, sc7tl, sc7tb, sc7tw, 0.45, 0.51, 0.04)
sctlat = [sc1tl,sc2tl,sc3tl,sc4tl,sc5tl, sc6tl, sc7tl]
sctbla = [sc1tb,sc2tb,sc3tb,sc4tb,sc5tb, sc6tb, sc7tb]
sctwhi = [sc1tw,sc2tw,sc3tw,sc4tw,sc5tw, sc6tw, sc7tw]
scblat = [sc1bl,sc2bl,sc3bl,sc4bl,sc5bl, sc6bl, sc7bl]
scbbla = [sc1bb,sc2bb,sc3bb,sc4bb,sc5bb, sc6bb, sc7bb]
scbwhi = [sc1bw,sc2bw,sc3bw,sc4bw,sc5bw, sc6bw, sc7bw]
calcStateResult("TOTAL SOUTH CAROLINA", sctlat, sctbla, sctwhi, scblat, scbbla, scbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Texas 1", 717735, tx1bl, tx1bb, tx1bw, tx1tl, tx1tb, tx1tw, 0.45, 0.51, 0.04)
calcResult("Texas 2", 779662, tx2bl, tx2bb, tx2bw, tx2tl, tx2tb, tx2tw, 0.45, 0.51, 0.04)
calcResult("Texas 3", 842800, tx3bl, tx3bb, tx3bw, tx3tl, tx3tb, tx3tw, 0.45, 0.51, 0.04)
calcResult("Texas 4", 747188, tx4bl, tx4bb, tx4bw, tx4tl, tx4tb, tx4tw, 0.45, 0.51, 0.04)
calcResult("Texas 5", 749808, tx5bl, tx5bb, tx5bw, tx5tl, tx5tb, tx5tw, 0.45, 0.51, 0.04)
calcResult("Texas 6", 770255, tx6bl, tx6bb, tx6bw, tx6tl, tx6tb, tx6tw, 0.45, 0.51, 0.04)
calcResult("Texas 7", 770606, tx7bl, tx7bb, tx7bw, tx7tl, tx7tb, tx7tw, 0.45, 0.51, 0.04)
calcResult("Texas 8", 813519, tx8bl, tx8bb, tx8bw, tx8tl, tx8tb, tx8tw, 0.45, 0.51, 0.04)
calcResult("Texas 9", 793923, tx9bl, tx9bb, tx9bw, tx9tl, tx9tb, tx9tw, 0.45, 0.51, 0.04)
calcResult("Texas 10", 823296, tx10bl, tx10bb, tx10bw, tx10tl, tx10tb, tx10tw, 0.45, 0.51, 0.04)
calcResult("Texas 11", 759136, tx11bl, tx11bb, tx11bw, tx11tl, tx11tb, tx11tw, 0.45, 0.51, 0.04)
calcResult("Texas 12", 806551, tx12bl, tx12bb, tx12bw, tx12tl, tx12tb, tx12tw, 0.45, 0.51, 0.04)
calcResult("Texas 13", 707421, tx13bl, tx13bb, tx13bw, tx13tl, tx13tb, tx13tw, 0.45, 0.51, 0.04)
calcResult("Texas 14", 753147, tx14bl, tx14bb, tx14bw, tx14tl, tx14tb, tx14tw, 0.45, 0.51, 0.04)
calcResult("Texas 15", 776887, tx15bl, tx15bb, tx15bw, tx15tl, tx15tb, tx15tw, 0.45, 0.51, 0.04)
calcResult("Texas 16", 742384, tx16bl, tx16bb, tx16bw, tx16tl, tx16tb, tx16tw, 0.45, 0.51, 0.04)
calcResult("Texas 17", 761922, tx17bl, tx17bb, tx17bw, tx17tl, tx17tb, tx17tw, 0.45, 0.51, 0.04)
calcResult("Texas 18", 787352, tx18bl, tx18bb, tx18bw, tx18tl, tx18tb, tx18tw, 0.45, 0.51, 0.04)
calcResult("Texas 19", 734532, tx19bl, tx19bb, tx19bw, tx19tl, tx19tb, tx19tw, 0.45, 0.51, 0.04)
calcResult("Texas 20", 791141, tx20bl, tx20bb, tx20bw, tx20tl, tx20tb, tx20tw, 0.45, 0.51, 0.04)
calcResult("Texas 21", 804470, tx21bl, tx21bb, tx21bw, tx21tl, tx21tb, tx21tw, 0.45, 0.51, 0.04)
calcResult("Texas 22", 881407, tx22bl, tx22bb, tx22bw, tx22tl, tx22tb, tx22tw, 0.45, 0.51, 0.04)
calcResult("Texas 23", 772944, tx23bl, tx23bb, tx23bw, tx23tl, tx23tb, tx23tw, 0.45, 0.51, 0.04)
calcResult("Texas 24", 790319, tx24bl, tx24bb, tx24bw, tx24tl, tx24tb, tx24tw, 0.45, 0.51, 0.04)
calcResult("Texas 25", 762897, tx25bl, tx25bb, tx25bw, tx25tl, tx25tb, tx25tw, 0.45, 0.51, 0.04)
calcResult("Texas 26", 845376, tx26bl, tx26bb, tx26bw, tx26tl, tx26tb, tx26tw, 0.45, 0.51, 0.04)
calcResult("Texas 27", 736778, tx27bl, tx27bb, tx27bw, tx27tl, tx27tb, tx27tw, 0.45, 0.51, 0.04)
calcResult("Texas 28", 736150, tx28bl, tx28bb, tx28bw, tx28tl, tx28tb, tx28tw, 0.45, 0.51, 0.04)
calcResult("Texas 29", 765403, tx29bl, tx29bb, tx29bw, tx29tl, tx29tb, tx29tw, 0.45, 0.51, 0.04)
calcResult("Texas 30", 749289, tx30bl, tx30bb, tx30bw, tx30tl, tx30tb, tx30tw, 0.45, 0.51, 0.04)
calcResult("Texas 31", 830908, tx31bl, tx31bb, tx31bw, tx31tl, tx31tb, tx31tw, 0.45, 0.51, 0.04)
calcResult("Texas 32", 753715, tx32bl, tx32bb, tx32bw, tx32tl, tx32tb, tx32tw, 0.45, 0.51, 0.04)
calcResult("Texas 33", 764730, tx33bl, tx33bb, tx33bw, tx33tl, tx33tb, tx33tw, 0.45, 0.51, 0.04)
calcResult("Texas 34", 723156, tx34bl, tx34bb, tx34bw, tx34tl, tx34tb, tx34tw, 0.45, 0.51, 0.04)
calcResult("Texas 35", 822601, tx35bl, tx35bb, tx35bw, tx35tl, tx35tb, tx35tw, 0.45, 0.51, 0.04)
calcResult("Texas 36", 732975, tx36bl, tx36bb, tx36bw, tx36tl, tx36tb, tx36tw, 0.45, 0.51, 0.04)
txtlat = [tx1tl,tx2tl,tx3tl,tx4tl,tx5tl,tx6tl,tx7tl,tx8tl,tx9tl,tx10tl,tx11tl,tx12tl,tx13tl,tx14tl,tx15tl,tx16tl,tx17tl,tx18tl,tx19tl,tx20tl,tx21tl,tx22tl,tx23tl,tx24tl,tx25tl,tx26tl,tx27tl,tx28tl,tx29tl,tx30tl,tx31tl,tx32tl,tx33tl,tx34tl,tx35tl,tx36tl]
txtbla = [tx1tb,tx2tb,tx3tb,tx4tb,tx5tb,tx6tb,tx7tb,tx8tb,tx9tb,tx10tb,tx11tb,tx12tb,tx13tb,tx14tb,tx15tb,tx16tb,tx17tb,tx18tb,tx19tb,tx20tb,tx21tb,tx22tb,tx23tb,tx24tb,tx25tb,tx26tb,tx27tb,tx28tb,tx29tb,tx30tb,tx31tb,tx32tb,tx33tb,tx34tb,tx35tb,tx36tb]
txtwhi = [tx1tw,tx2tw,tx3tw,tx4tw,tx5tw,tx6tw,tx7tw,tx8tw,tx9tw,tx10tw,tx11tw,tx12tw,tx13tw,tx14tw,tx15tw,tx16tw,tx17tw,tx18tw,tx19tw,tx20tw,tx21tw,tx22tw,tx23tw,tx24tw,tx25tw,tx26tw,tx27tw,tx28tw,tx29tw,tx30tw,tx31tw,tx32tw,tx33tw,tx34tw,tx35tw,tx36tw]
txblat = [tx1bl,tx2bl,tx3bl,tx4bl,tx5bl,tx6bl,tx7bl,tx8bl,tx9bl,tx10bl,tx11bl,tx12bl,tx13bl,tx14bl,tx15bl,tx16bl,tx17bl,tx18bl,tx19bl,tx20bl,tx21bl,tx22bl,tx23bl,tx24bl,tx25bl,tx26bl,tx27bl,tx28bl,tx29bl,tx30bl,tx31bl,tx32bl,tx33bl,tx34bl,tx35bl,tx36bl]
txbbla = [tx1bb,tx2bb,tx3bb,tx4bb,tx5bb,tx6bb,tx7bb,tx8bb,tx9bb,tx10bb,tx11bb,tx12bb,tx13bb,tx14bb,tx15bb,tx16bb,tx17bb,tx18bb,tx19bb,tx20bb,tx21bb,tx22bb,tx23bb,tx24bb,tx25bb,tx26bb,tx27bb,tx28bb,tx29bb,tx30bb,tx31bb,tx32bb,tx33bb,tx34bb,tx35bb,tx36bb]
txbwhi = [tx1bw,tx2bw,tx3bw,tx4bw,tx5bw,tx6bw,tx7bw,tx8bw,tx9bw,tx10bw,tx11bw,tx12bw,tx13bw,tx14bw,tx15bw,tx16bw,tx17bw,tx18bw,tx19bw,tx20bw,tx21bw,tx22bw,tx23bw,tx24bw,tx25bw,tx26bw,tx27bw,tx28bw,tx29bw,tx30bw,tx31bw,tx32bw,tx33bw,tx34bw,tx35bw,tx36bw]
calcStateResult("TOTAL TEXAS", txtlat, txtbla, txtwhi, txblat, txbbla, txbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Tennessee 1", 714504, tn1bl, tn1bb, tn1bw, tn1tl, tn1tb, tn1tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 2", 740182, tn2bl, tn2bb, tn2bw, tn2tl, tn2tb, tn2tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 3", 728254, tn3bl, tn3bb, tn3bw, tn3tl, tn3tb, tn3tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 4", 767655, tn4bl, tn4bb, tn4bw, tn4tl, tn4tb, tn4tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 5", 762535, tn5bl, tn5bb, tn5bw, tn5tl, tn5tb, tn5tw, 0.45, 0.51, 0.04 )
calcResult("Tennessee 6", 761538, tn6bl, tn6bb, tn6bw, tn6tl, tn6tb, tn6tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 7", 765730, tn7bl, tn7bb, tn7bw, tn7tl, tn7tb, tn7tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 8", 706468, tn8bl, tn8bb, tn8bw, tn8tl, tn8tb, tn8tw, 0.45, 0.51, 0.04)
calcResult("Tennessee 9", 704328, tn9bl, tn9bb, tn9bw, tn9tl, tn9tb, tn9tw, 0.45, 0.51, 0.04 )
tntlat = [tn1tl,tn2tl,tn3tl,tn4tl,tn5tl,tn6tl,tn7tl,tn8tl,tn9tl]
tntbla = [tn1tb,tn2tb,tn3tb,tn4tb,tn5tb,tn6tb,tn7tb,tn8tb,tn9tb]
tntwhi = [tn1tw,tn2tw,tn3tw,tn4tw,tn5tw,tn6tw,tn7tw,tn8tw,tn9tw]
tnblat = [tn1bl,tn2bl,tn3bl,tn4bl,tn5bl,tn6bl,tn7bl,tn8bl,tn9bl]
tnbbla = [tn1bb,tn2bb,tn3bb,tn4bb,tn5bb,tn6bb,tn7bb,tn8bb,tn9bb]
tnbwhi = [tn1bw,tn2bw,tn3bw,tn4bw,tn5bw,tn6bw,tn7bw,tn8bw,tn9bw]
calcStateResult("TOTAL TENNESSEE", tntlat, tntbla, tntwhi, tnblat, tnbbla, tnbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Pennsylvania 1", 655146, pa1bl, pa1bb, pa1bw, pa1tl, pa1tb, pa1tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 2", 722350, pa2bl, pa2bb, pa2bw, pa2tl, pa2tb, pa2tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 3", 646311, pa3bl, pa3bb, pa3bw, pa3tl, pa3tb, pa3tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 4", 647418, pa4bl, pa4bb, pa4bw, pa4tl, pa4tb, pa4tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 5", 646397, pa5bl, pa5bb, pa5bw, pa5tl, pa5tb, pa5tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 6", 646221, pa6bl, pa6bb, pa6bw, pa6tl, pa6tb, pa6tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 7", 692866, pa7bl, pa7bb, pa7bw, pa7tl, pa7tb, pa7tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 8", 646403, pa8bl, pa8bb, pa8bw, pa8tl, pa8tb, pa8tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 9", 646628, pa9bl, pa9bb, pa9bw, pa9tl, pa9tb, pa9tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 10", 669257, pa10bl, pa10bb, pa10bw, pa10tl, pa10tb, pa10tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 11", 687860, pa11bl, pa11bb, pa11bw, pa11tl, pa11tb, pa11tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 12", 612384, pa12bl, pa12bb, pa12bw, pa12tl, pa12tb, pa12tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 13", 646435, pa13bl, pa13bb, pa13bw, pa13tl, pa13tb, pa13tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 14", 646013, pa14bl, pa14bb, pa14bw, pa14tl, pa14tb, pa14tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 15", 680927, pa15bl, pa15bb, pa15bw, pa15tl, pa15tb, pa15tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 16", 686525, pa16bl, pa16bb, pa16bw, pa16tl, pa16tb, pa16tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 17", 681835, pa17bl, pa17bb, pa17bw, pa17tl, pa17tb, pa17tw, 0.45, 0.51, 0.04)
calcResult("Pennsylvania 18", 709728, pa18bl, pa18bb, pa18bw, pa18tl, pa18tb, pa18tw, 0.45, 0.51, 0.04)
patlat = [pa1tl,pa2tl,pa3tl,pa4tl,pa5tl,pa6tl,pa7tl,pa8tl,pa9tl,pa10tl,pa11tl,pa12tl,pa13tl,pa14tl,pa15tl,pa16tl,pa17tl,pa18tl]
patbla = [pa1tb,pa2tb,pa3tb,pa4tb,pa5tb,pa6tb,pa7tb,pa8tb,pa9tb,pa10tb,pa11tb,pa12tb,pa13tb,pa14tb,pa15tb,pa16tb,pa17tb,pa18tb]
patwhi = [pa1tw,pa2tw,pa3tw,pa4tw,pa5tw,pa6tw,pa7tw,pa8tw,pa9tw,pa10tw,pa11tw,pa12tw,pa13tw,pa14tw,pa15tw,pa16tw,pa17tw,pa18tw]
pablat = [pa1bl,pa2bl,pa3bl,pa4bl,pa5bl,pa6bl,pa7bl,pa8bl,pa9bl,pa10bl,pa11bl,pa12bl,pa13bl,pa14bl,pa15bl,pa16bl,pa17bl,pa18bl]
pabbla = [pa1bb,pa2bb,pa3bb,pa4bb,pa5bb,pa6bb,pa7bb,pa8bb,pa9bb,pa10bb,pa11bb,pa12bb,pa13bb,pa14bb,pa15bb,pa16bb,pa17bb,pa18bb]
pabwhi = [pa1bw,pa2bw,pa3bw,pa4bw,pa5bw,pa6bw,pa7bw,pa8bw,pa9bw,pa10bw,pa11bw,pa12bw,pa13bw,pa14bw,pa15bw,pa16bw,pa17bw,pa18bw]
calcStateResult("TOTAL PENNSYLVANIA", patlat, patbla, patwhi, pablat, pabbla, pabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Rhode Island 1", 539250, ri1bl, ri1bb, ri1bw, ri1tl, ri1tb, ri1tw, 0.45, 0.51, 0.04 )
calcResult("Rhode Island 2", 520389, ri2bl, ri2bb, ri2bw, ri2tl, ri2tb, ri2tw, 0.45, 0.51, 0.04 )
ritlat = [ri1tl, ri2tl]
ritbla = [ri1tb, ri2tb]
ritwhi = [ri1tw, ri2tw]
riblat = [ri1bl, ri2bl]
ribbla = [ri1bb, ri2bb]
ribwhi = [ri1bw, ri2bw]
calcStateResult("TOTAL RHODE ISLAND", ritlat, ritbla, ritwhi, riblat, ribbla, ribwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Utah 1", 100000, ut1bl, ut1bb, ut1bw, ut1tl, ut1tb, ut1tw, 0.45, 0.51, 0.04)
calcResult("Utah 2", 100000, ut2bl, ut2bb, ut2bw, ut2tl, ut2tb, ut2tw, 0.45, 0.51, 0.04)
calcResult("Utah 3", 100000, ut3bl, ut3bb, ut3bw, ut3tl, ut3tb, ut3tw, 0.45, 0.51, 0.04)
calcResult("Utah 4", 745786, ut4bl, ut4bb, ut4bw, ut4tl, ut4tb, ut4tw, 0.45, 0.51, 0.04)
uttlat = [ut1tl,ut2tl,ut3tl,ut4tl]
uttbla = [ut1tb,ut2tb,ut3tb,ut4tb]
uttwhi = [ut1tw,ut2tw,ut3tw,ut4tw]
utblat = [ut1bl,ut2bl,ut3bl,ut4bl]
utbbla = [ut1bb,ut2bb,ut3bb,ut4bb]
utbwhi = [ut1bw,ut2bw,ut3bw,ut4bw]
calcStateResult("TOTAL UTAH", uttlat, uttbla, uttwhi, utblat, utbbla, utbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Virginia 1", 776836, va1bl, va1bb, va1bw, va1tl, va1tb, va1tw, 0.45, 0.51, 0.04)
calcResult("Virginia 2", 745816, va2bl, va2bb, va2bw, va2tl, va2tb, va2tw, 0.45, 0.51, 0.04)
calcResult("Virginia 3", 739169, va3bl, va3bb, va3bw, va3tl, va3tb, va3tw, 0.45, 0.51, 0.04)
calcResult("Virginia 4", 764301, va4bl, va4bb, va4bw, va4tl, va4tb, va4tw, 0.45, 0.51, 0.04)
calcResult("Virginia 5", 735178, va5bl, va5bb, va5bw, va5tl, va5tb, va5tw, 0.45, 0.51, 0.04)
calcResult("Virginia 6", 754859, va6bl, va6bb, va6bw, va6tl, va6tb, va6tw, 0.45, 0.51, 0.04)
calcResult("Virginia 7", 790084, va7bl, va7bb, va7bw, va7tl, va7tb, va7tw, 0.45, 0.51, 0.04)
calcResult("Virginia 8", 783079, va8bl, va8bb, va8bw, va8tl, va8tb, va8tw, 0.45, 0.51, 0.04)
calcResult("Virginia 9", 704831, va9bl, va9bb, va9bw, va9tl, va9tb, va9tw, 0.45, 0.51, 0.04)
calcResult("Virginia 10", 827279, va10bl, va10bb, va10bw, va10tl, va10tb, va10tw, 0.45, 0.51, 0.04)
calcResult("Virginia 11", 802910, va11bl, va11bb, va11bw, va11tl, va11tb, va11tw, 0.45, 0.51, 0.04)
vatlat = [va1tl,va2tl,va3tl,va4tl,va5tl,va6tl,va7tl,va8tl,va9tl,va10tl,va11tl]
vatbla = [va1tb,va2tb,va3tb,va4tb,va5tb,va6tb,va7tb,va8tb,va9tb,va10tb,va11tb]
vatwhi = [va1tw,va2tw,va3tw,va4tw,va5tw,va6tw,va7tw,va8tw,va9tw,va10tw,va11tw]
vablat = [va1bl,va2bl,va3bl,va4bl,va5bl,va6bl,va7bl,va8bl,va9bl,va10bl,va11bl]
vabbla = [va1bb,va2bb,va3bb,va4bb,va5bb,va6bb,va7bb,va8bb,va9bb,va10bb,va11bb]
vabwhi = [va1bw,va2bw,va3bw,va4bw,va5bw,va6bw,va7bw,va8bw,va9bw,va10bw,va11bw]
calcStateResult("TOTAL VIRGINIA", vatlat, vatbla, vatwhi, vablat, vabbla, vabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Washington 1", 654904, wa1bl, wa1bb, wa1bw, wa1tl, wa1tb, wa1tw, 0.45, 0.51, 0.04)
calcResult("Washington 2", 654903, wa2bl, wa2bb, wa2bw, wa2tl, wa2tb, wa2tw, 0.45, 0.51, 0.04)
calcResult("Washington 3", 654898, wa3bl, wa3bb, wa3bw, wa3tl, wa3tb, wa3tw, 0.45, 0.51, 0.04)
calcResult("Washington 4", 654901, wa4bl, wa4bb, wa4bw, wa4tl, wa4tb, wa4tw, 0.45, 0.51, 0.04)
calcResult("Washington 5", 654904, wa5bl, wa5bb, wa5bw, wa5tl, wa5tb, wa5tw, 0.45, 0.51, 0.04)
calcResult("Washington 6", 654902, wa6bl, wa6bb, wa6bw, wa6tl, wa6tb, wa6tw, 0.45, 0.51, 0.04)
calcResult("Washington 7", 683158, wa7bl, wa7bb, wa7bw, wa7tl, wa7tb, wa7tw, 0.45, 0.51, 0.04)
calcResult("Washington 8", 672463, wa8bl, wa8bb, wa8bw, wa8tl, wa8tb, wa8tw, 0.45, 0.51, 0.04)
calcResult("Washington 9", 672460, wa9bl, wa9bb, wa9bw, wa9tl, wa9tb, wa9tw, 0.45, 0.51, 0.04)
calcResult("Washington 10", 685260, wa10bl, wa10bb, wa10bw, wa10tl, wa10tb, wa10tw, 0.45, 0.51, 0.04)
watlat = [wa1tl,wa2tl,wa3tl,wa4tl,wa5tl,wa6tl,wa7tl,wa8tl,wa9tl,wa10tl]
watbla = [wa1tb,wa2tb,wa3tb,wa4tb,wa5tb,wa6tb,wa7tb,wa8tb,wa9tb,wa10tb]
watwhi = [wa1tw,wa2tw,wa3tw,wa4tw,wa5tw,wa6tw,wa7tw,wa8tw,wa9tw,wa10tw]
wablat = [wa1bl,wa2bl,wa3bl,wa4bl,wa5bl,wa6bl,wa7bl,wa8bl,wa9bl,wa10bl]
wabbla = [wa1bb,wa2bb,wa3bb,wa4bb,wa5bb,wa6bb,wa7bb,wa8bb,wa9bb,wa10bb]
wabwhi = [wa1bw,wa2bw,wa3bw,wa4bw,wa5bw,wa6bw,wa7bw,wa8bw,wa9bw,wa10bw]
calcStateResult("TOTAL WASHINGTON", watlat, watbla, watwhi, wablat, wabbla, wabwhi, 0.45, 0.51, 0.04)
print("")
calcResult("West Virginia 1", 615991, wv1bl, wv1bb, wv1bw, wv1tl, wv1tb, wv1tw, 0.45, 0.51, 0.04)
calcResult("West Virginia 2", 648186, wv2bl, wv2bb, wv2bw, wv2tl, wv2tb, wv2tw, 0.45, 0.51, 0.04)
calcResult("West Virginia 3", 591121, wv3bl, wv3bb, wv3bw, wv3tl, wv3tb, wv3tw, 0.45, 0.51, 0.04)
wvtlat = [wv1tl,wv2tl,wv3tl]
wvtbla = [wv1tb,wv2tb,wv3tb]
wvtwhi = [wv1tw,wv2tw,wv3tw]
wvblat = [wv1bl,wv2bl,wv3bl]
wvbbla = [wv1bb,wv2bb,wv3bb]
wvbwhi = [wv1bw,wv2bw,wv3bw]
calcStateResult("TOTAL WEST VIRGINIA", wvtlat, wvtbla, wvtwhi, wvblat, wvbbla, wvbwhi, 0.45, 0.51, 0.04)
print("")
calcResult("Wisconsin 1", 717716, wi1bl, wi1bb, wi1bw, wi1tl, wi1tb, wi1tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 2", 768067, wi2bl, wi2bb, wi2bw, wi2tl, wi2tb, wi2tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 3", 724568, wi3bl, wi3bb, wi3bw, wi3tl, wi3tb, wi3tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 4", 710573, wi4bl, wi4bb, wi4bw, wi4tl, wi4tb, wi4tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 5", 731341, wi5bl, wi5bb, wi5bw, wi5tl, wi5tb, wi5tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 6", 714886, wi6bl, wi6bb, wi6bw, wi6tl, wi6tb, wi6tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 7", 710420, wi7bl, wi7bb, wi7bw, wi7tl, wi7tb, wi7tw, 0.45, 0.51, 0.04)
calcResult("Wisconsin 8", 735997, wi8bl, wi8bb, wi8bw, wi8tl, wi8tb, wi8tw, 0.45, 0.51, 0.04)
witlat = [wi1tl,wi2tl,wi3tl,wi4tl,wi5tl,wi6tl,wi7tl,wi8tl]
witbla = [wi1tb,wi2tb,wi3tb,wi4tb,wi5tb,wi6tb,wi7tb,wi8tb]
witwhi = [wi1tw,wi2tw,wi3tw,wi4tw,wi5tw,wi6tw,wi7tw,wi8tw]
wiblat = [wi1bl,wi2bl,wi3bl,wi4bl,wi5bl,wi6bl,wi7bl,wi8bl]
wibbla = [wi1bb,wi2bb,wi3bb,wi4bb,wi5bb,wi6bb,wi7bb,wi8bb]
wibwhi = [wi1bw,wi2bw,wi3bw,wi4bw,wi5bw,wi6bw,wi7bw,wi8bw]
calcStateResult("TOTAL WISCONSIN", witlat, witbla, witwhi, wiblat, wibbla, wibwhi, 0.45, 0.51, 0.04)
print("")
calcResult("DELAWARE", 973764, de1bl, de1bb, de1bw, de1tl, de1tb, de1tw, 0.45, 0.51, 0.04)
print("")
calcResult("NORTH DAKOTA", 762062, nd1bl, nd1bb, nd1bw, nd1tl, nd1tb, nd1tw, 0.45, 0.51, 0.04)
print("")
calcResult("SOUTH DAKOTA", 884659, sd1bl, sd1bb, sd1bw, sd1tl, sd1tb, sd1tw, 0.45, 0.51, 0.04)
print("")
calcResult("MONTANA", 1068778, mt1bl, mt1bb, mt1bw, mt1tl, mt1tb, mt1tw, 0.45, 0.51, 0.04)
print("")
calcResult("WYOMING", 578759, wy1bl, wy1bb, wy1bw, wy1tl, wy1tb, wy1tw, 0.45, 0.51, 0.04)
print("")
calcResult("ALASKA", 731545, ak1bl, ak1bb, ak1bw, ak1tl, ak1tb, ak1tw, 0.45, 0.51, 0.04)
print("")
calcResult("VERMONT", 623989, vt1bl, vt1bb, vt1bw, vt1tl, vt1tb, vt1tw, 0.45, 0.51, 0.04)


for str in results:
	print(str)
	print("")

print("")
print("Trump districts: ", trumpdistricts)
print("Biden districts: ", bidendistricts )


with open("/Volumes/TOSHIBA/usawithgender.txt", 'wb') as f:
	pickle.dump([al1tl, al1tb, al1tw, al2tl, al2tb, al2tw, al3tl, al3tb, al3tw, al4tl, al4tb, al4tw, al5tl, al5tb, al5tw, al6tl, al6tb, al6tw, al7tl, al7tb, al7tw, al1bl, al1bb, al1bw, al2bl, al2bb, al2bw, al3bl, al3bb, al3bw, al4bl, al4bb, al4bw, al5bl, al5bb, al5bw, al6bl, al6bb, al6bw, al7bl, al7bb, al7bw, ak1tl, ak1tb, ak1tw, ak1bl, ak1bb, ak1bw, az1tl, az1tb, az1tw, az2tl, az2tb, az2tw, az3tl, az3tb, az3tw, az4tl, az4tb, az4tw, az5tl, az5tb, az5tw, az6tl, az6tb, az6tw, az7tl, az7tb, az7tw, az8tl, az8tb, az8tw, az9tl, az9tb, az9tw, az1bl, az1bb, az1bw, az2bl, az2bb, az2bw, az3bl, az3bb, az3bw, az4bl, az4bb, az4bw, az5bl, az5bb, az5bw, az6bl, az6bb, az6bw, az7bl, az7bb, az7bw, az8bl, az8bb, az8bw, az9bl, az9bb, az9bw, ar1bl, ar1bb, ar1bw, ar2bl, ar2bb, ar2bw, ar3bl, ar3bb, ar3bw, ar4bl, ar4bb, ar4bw, ar1tl, ar1tb, ar1tw, ar2tl, ar2tb, ar2tw, ar3tl, ar3tb, ar3tw, ar4tl, ar4tb, ar4tw, ak1bl, ak1bb, ak1bw, ca1tl, ca1tb, ca1tw, ca2tl, ca2tb, ca2tw, ca3tl, ca3tb, ca3tw, ca4tl, ca4tb, ca4tw, ca5tl, ca5tb, ca5tw, ca6tl, ca6tb, ca6tw, ca7tl, ca7tb, ca7tw, ca8tl, ca8tb, ca8tw, ca9tl, ca9tb, ca9tw, ca10tl, ca10tb, ca10tw, ca11tl, ca11tb, ca11tw, ca12tl, ca12tb, ca12tw, ca13tl, ca13tb, ca13tw, ca14tl, ca14tb, ca14tw, ca15tl, ca15tb, ca15tw, ca16tl, ca16tb, ca16tw, ca17tl, ca17tb, ca17tw, ca18tl, ca18tb, ca18tw, ca19tl, ca19tb, ca19tw, ca20tl, ca20tb, ca20tw, ca21tl, ca21tb, ca21tw, ca22tl, ca22tb, ca22tw, ca23tl, ca23tb, ca23tw, ca24tl, ca24tb, ca24tw, ca25tl, ca25tb, ca25tw, ca26tl, ca26tb, ca26tw, ca27tl, ca27tb, ca27tw, ca28tl, ca28tb, ca28tw, ca29tl, ca29tb, ca29tw, ca30tl, ca30tb, ca30tw, ca31tl, ca31tb, ca31tw, ca32tl, ca32tb, ca32tw, ca33tl, ca33tb, ca33tw, ca34tl, ca34tb, ca34tw, ca35tl, ca35tb, ca35tw, ca36tl, ca36tb, ca36tw, ca37tl, ca37tb, ca37tw, ca38tl, ca38tb, ca38tw, ca39tl, ca39tb, ca39tw, ca40tl, ca40tb, ca40tw, ca41tl, ca41tb, ca41tw, ca42tl, ca42tb, ca42tw, ca43tl, ca43tb, ca43tw, ca44tl, ca44tb, ca44tw, ca45tl, ca45tb, ca45tw, ca46tl, ca46tb, ca46tw, ca47tl, ca47tb, ca47tw, ca48tl, ca48tb, ca48tw, ca49tl, ca49tb, ca49tw, ca50tl, ca50tb, ca50tw, ca51tl, ca51tb, ca51tw, ca52tl, ca52tb, ca52tw, ca53tl, ca53tb, ca53tw, ca1bl, ca1bb, ca1bw, ca2bl, ca2bb, ca2bw, ca3bl, ca3bb, ca3bw, ca4bl, ca4bb, ca4bw, ca5bl, ca5bb, ca5bw, ca6bl, ca6bb, ca6bw, ca7bl, ca7bb, ca7bw, ca8bl, ca8bb, ca8bw, ca9bl, ca9bb, ca9bw, ca10bl, ca10bb, ca10bw, ca11bl, ca11bb, ca11bw, ca12bl, ca12bb, ca12bw, ca13bl, ca13bb, ca13bw, ca14bl, ca14bb, ca14bw, ca15bl, ca15bb, ca15bw, ca16bl, ca16bb, ca16bw, ca17bl, ca17bb, ca17bw, ca18bl, ca18bb, ca18bw, ca19bl, ca19bb, ca19bw, ca20bl, ca20bb, ca20bw, ca21bl, ca21bb, ca21bw, ca22bl, ca22bb, ca22bw, ca23bl, ca23bb, ca23bw, ca24bl, ca24bb, ca24bw, ca25bl, ca25bb, ca25bw, ca26bl, ca26bb, ca26bw, ca27bl, ca27bb, ca27bw, ca28bl, ca28bb, ca28bw, ca29bl, ca29bb, ca29bw, ca30bl, ca30bb, ca30bw, ca31bl, ca31bb, ca31bw, ca32bl, ca32bb, ca32bw, ca33bl, ca33bb, ca33bw, ca34bl, ca34bb, ca34bw, ca35bl, ca35bb, ca35bw, ca36bl, ca36bb, ca36bw, ca37bl, ca37bb, ca37bw, ca38bl, ca38bb, ca38bw, ca39bl, ca39bb, ca39bw, ca40bl, ca40bb, ca40bw, ca41bl, ca41bb, ca41bw, ca42bl, ca42bb, ca42bw, ca43bl, ca43bb, ca43bw, ca44bl, ca44bb, ca44bw, ca45bl, ca45bb, ca45bw, ca46bl, ca46bb, ca46bw, ca47bl, ca47bb, ca47bw, ca48bl, ca48bb, ca48bw, ca49bl, ca49bb, ca49bw, ca50bl, ca50bb, ca50bw, ca51bl, ca51bb, ca51bw, ca52bl, ca52bb, ca52bw, ca53bl, ca53bb, ca53bw, co1tl, co1tb, co1tw, co2tl, co2tb, co2tw, co3tl, co3tb, co3tw, co4tl, co4tb, co4tw, co5tl, co5tb, co5tw, co6tl, co6tb, co6tw, co7tl, co7tb, co7tw, co1bl, co1bb, co1bw, co2bl, co2bb, co2bw, co3bl, co3bb, co3bw, co4bl, co4bb, co4bw, co5bl, co5bb, co5bw, co6bl, co6bb, co6bw, co7bl, co7bb, co7bw, ct1bl, ct1bb, ct1bw, ct2bl, ct2bb, ct2bw, ct3bl, ct3bb, ct3bw, ct4bl, ct4bb, ct4bw, ct5bl, ct5bb, ct5bw, ct1tl, ct1tb, ct1tw, ct2tl, ct2tb, ct2tw, ct3tl, ct3tb, ct3tw, ct4tl, ct4tb, ct4tw, ct5tl, ct5tb, ct5tw, de1tl, de1tb, de1tw, de1bl, de1bb, de1bw, fl1bl, fl1bb, fl1bw, fl2bl, fl2bb, fl2bw, fl3bl, fl3bb, fl3bw, fl4bl, fl4bb, fl4bw, fl5bl, fl5bb, fl5bw, fl6bl, fl6bb, fl6bw, fl7bl, fl7bb, fl7bw, fl8bl, fl8bb, fl8bw, fl9bl, fl9bb, fl9bw, fl10bl, fl10bb, fl10bw, fl11bl, fl11bb, fl11bw, fl12bl, fl12bb, fl12bw, fl13bl, fl13bb, fl13bw, fl14bl, fl14bb, fl14bw, fl15bl, fl15bb, fl15bw, fl16bl, fl16bb, fl16bw, fl17bl, fl17bb, fl17bw, fl18bl, fl18bb, fl18bw, fl19bl, fl19bb, fl19bw, fl20bl, fl20bb, fl20bw, fl21bl, fl21bb, fl21bw, fl22bl, fl22bb, fl22bw, fl23bl, fl23bb, fl23bw, fl24bl, fl24bb, fl24bw, fl25bl, fl25bb, fl25bw, fl26bl, fl26bb, fl26bw, fl27bl, fl27bb, fl27bw, fl1tl, fl1tb, fl1tw, fl2tl, fl2tb, fl2tw, fl3tl, fl3tb, fl3tw, fl4tl, fl4tb, fl4tw, fl5tl, fl5tb, fl5tw, fl6tl, fl6tb, fl6tw, fl7tl, fl7tb, fl7tw, fl8tl, fl8tb, fl8tw, fl9tl, fl9tb, fl9tw, fl10tl, fl10tb, fl10tw, fl11tl, fl11tb, fl11tw, fl12tl, fl12tb, fl12tw, fl13tl, fl13tb, fl13tw, fl14tl, fl14tb, fl14tw, fl15tl, fl15tb, fl15tw, fl16tl, fl16tb, fl16tw, fl17tl, fl17tb, fl17tw, fl18tl, fl18tb, fl18tw, fl19tl, fl19tb, fl19tw, fl20tl, fl20tb, fl20tw, fl21tl, fl21tb, fl21tw, fl22tl, fl22tb, fl22tw, fl23tl, fl23tb, fl23tw, fl24tl, fl24tb, fl24tw, fl25tl, fl25tb, fl25tw, fl26tl, fl26tb, fl26tw, fl27tl, fl27tb, fl27tw, ga1tl, ga1tb, ga1tw, ga2tl, ga2tb, ga2tw, ga3tl, ga3tb, ga3tw, ga4tl, ga4tb, ga4tw, ga5tl, ga5tb, ga5tw, ga6tl, ga6tb, ga6tw, ga7tl, ga7tb, ga7tw, ga8tl, ga8tb, ga8tw, ga9tl, ga9tb, ga9tw, ga10tl, ga10tb, ga10tw, ga11tl, ga11tb, ga11tw, ga12tl, ga12tb, ga12tw, ga13tl, ga13tb, ga13tw, ga14tl, ga14tb, ga14tw, ga1bl, ga1bb, ga1bw, ga2bl, ga2bb, ga2bw, ga3bl, ga3bb, ga3bw, ga4bl, ga4bb, ga4bw, ga5bl, ga5bb, ga5bw, ga6bl, ga6bb, ga6bw, ga7bl, ga7bb, ga7bw, ga8bl, ga8bb, ga8bw, ga9bl, ga9bb, ga9bw, ga10bl, ga10bb, ga10bw, ga11bl, ga11bb, ga11bw, ga12bl, ga12bb, ga12bw, ga13bl, ga13bb, ga13bw, ga14bl, ga14bb, ga14bw, hi1tl, hi1tb, hi1tw, hi2tl, hi2tb, hi2tw, hi1bl, hi1bb, hi1bw, hi2bl, hi2bb, hi2bw, id1tl, id1tb, id1tw, id2tl, id2tb, id2tw, id1bl, id1bb, id1bw, id2bl, id2bb, id2bw, il1bl, il1bb, il1bw, il2bl, il2bb, il2bw, il3bl, il3bb, il3bw, il4bl, il4bb, il4bw, il5bl, il5bb, il5bw, il6bl, il6bb, il6bw, il7bl, il7bb, il7bw, il8bl, il8bb, il8bw, il9bl, il9bb, il9bw, il10bl, il10bb, il10bw, il11bl, il11bb, il11bw, il12bl, il12bb, il12bw, il13bl, il13bb, il13bw, il14bl, il14bb, il14bw, il15bl, il15bb, il15bw, il16bl, il16bb, il16bw, il17bl, il17bb, il17bw, il18bl, il18bb, il18bw, il1tl, il1tb, il1tw, il2tl, il2tb, il2tw, il3tl, il3tb, il3tw, il4tl, il4tb, il4tw, il5tl, il5tb, il5tw, il6tl, il6tb, il6tw, il7tl, il7tb, il7tw, il8tl, il8tb, il8tw, il9tl, il9tb, il9tw, il10tl, il10tb, il10tw, il11tl, il11tb, il11tw, il12tl, il12tb, il12tw, il13tl, il13tb, il13tw, il14tl, il14tb, il14tw, il15tl, il15tb, il15tw, il16tl, il16tb, il16tw, il17tl, il17tb, il17tw, il18tl, il18tb, il18tw, in1tl, in1tb, in1tw, in2tl, in2tb, in2tw, in3tl, in3tb, in3tw, in4tl, in4tb, in4tw, in5tl, in5tb, in5tw, in6tl, in6tb, in6tw, in7tl, in7tb, in7tw, in8tl, in8tb, in8tw, in9tl, in9tb, in9tw, in1bl, in1bb, in1bw, in2bl, in2bb, in2bw, in3bl, in3bb, in3bw, in4bl, in4bb, in4bw, in5bl, in5bb, in5bw, in6bl, in6bb, in6bw, in7bl, in7bb, in7bw, in8bl, in8bb, in8bw, in9bl, in9bb, in9bw, ia1tl, ia1tb, ia1tw, ia2tl, ia2tb, ia2tw, ia3tl, ia3tb, ia3tw, ia4tl, ia4tb, ia4tw, ia1bl, ia1bb, ia1bw, ia2bl, ia2bb, ia2bw, ia3bl, ia3bb, ia3bw, ia4bl, ia4bb, ia4bw, ks1tl, ks1tb, ks1tw, ks2tl, ks2tb, ks2tw, ks3tl, ks3tb, ks3tw, ks4tl, ks4tb, ks4tw, ks1bl, ks1bb, ks1bw, ks2bl, ks2bb, ks2bw, ks3bl, ks3bb, ks3bw, ks4bl, ks4bb, ks4bw, ky1tl, ky1tb, ky1tw, ky2tl, ky2tb, ky2tw, ky3tl, ky3tb, ky3tw, ky4tl, ky4tb, ky4tw, ky5tl, ky5tb, ky5tw, ky6tl, ky6tb, ky6tw, ky1bl, ky1bb, ky1bw, ky2bl, ky2bb, ky2bw, ky3bl, ky3bb, ky3bw, ky4bl, ky4bb, ky4bw, ky5bl, ky5bb, ky5bw, ky6bl, ky6bb, ky6bw, la1tl, la1tb, la1tw, la2tl, la2tb, la2tw, la3tl, la3tb, la3tw, la4tl, la4tb, la4tw, la5tl, la5tb, la5tw, la6tl, la6tb, la6tw, la1bl, la1bb, la1bw, la2bl, la2bb, la2bw, la3bl, la3bb, la3bw, la4bl, la4bb, la4bw, la5bl, la5bb, la5bw, la6bl, la6bb, la6bw, me1tl, me1tb, me1tw, me2tl, me2tb, me2tw, me1bl, me1bb, me1bw, me2bl, me2bb, me2bw, md1tl, md1tb, md1tw, md2tl, md2tb, md2tw, md3tl, md3tb, md3tw, md4tl, md4tb, md4tw, md5tl, md5tb, md5tw, md6tl, md6tb, md6tw, md7tl, md7tb, md7tw, md8tl, md8tb, md8tw, md1bl, md1bb, md1bw, md2bl, md2bb, md2bw, md3bl, md3bb, md3bw, md4bl, md4bb, md4bw, md5bl, md5bb, md5bw, md6bl, md6bb, md6bw, md7bl, md7bb, md7bw, md8bl, md8bb, md8bw, ma1tl, ma1tb, ma1tw, ma2tl, ma2tb, ma2tw, ma3tl, ma3tb, ma3tw, ma4tl, ma4tb, ma4tw, ma5tl, ma5tb, ma5tw, ma6tl, ma6tb, ma6tw, ma7tl, ma7tb, ma7tw, ma8tl, ma8tb, ma8tw, ma9tl, ma9tb, ma9tw, ma1bl, ma1bb, ma1bw, ma2bl, ma2bb, ma2bw, ma3bl, ma3bb, ma3bw, ma4bl, ma4bb, ma4bw, ma5bl, ma5bb, ma5bw, ma6bl, ma6bb, ma6bw, ma7bl, ma7bb, ma7bw, ma8bl, ma8bb, ma8bw, ma9bl, ma9bb, ma9bw, mi1bl, mi1bb, mi1bw, mi2bl, mi2bb, mi2bw, mi3bl, mi3bb, mi3bw, mi4bl, mi4bb, mi4bw, mi5bl, mi5bb, mi5bw, mi6bl, mi6bb, mi6bw, mi7bl, mi7bb, mi7bw, mi8bl, mi8bb, mi8bw, mi9bl, mi9bb, mi9bw, mi10bl, mi10bb, mi10bw, mi11bl, mi11bb, mi11bw, mi12bl, mi12bb, mi12bw, mi13bl, mi13bb, mi13bw, mi14bl, mi14bb, mi14bw, mi1tl, mi1tb, mi1tw, mi2tl, mi2tb, mi2tw, mi3tl, mi3tb, mi3tw, mi4tl, mi4tb, mi4tw, mi5tl, mi5tb, mi5tw, mi6tl, mi6tb, mi6tw, mi7tl, mi7tb, mi7tw, mi8tl, mi8tb, mi8tw, mi9tl, mi9tb, mi9tw, mi10tl, mi10tb, mi10tw, mi11tl, mi11tb, mi11tw, mi12tl, mi12tb, mi12tw, mi13tl, mi13tb, mi13tw, mi14tl, mi14tb, mi14tw, mn1tl, mn1tb, mn1tw, mn2tl, mn2tb, mn2tw, mn3tl, mn3tb, mn3tw, mn4tl, mn4tb, mn4tw, mn5tl, mn5tb, mn5tw, mn6tl, mn6tb, mn6tw, mn7tl, mn7tb, mn7tw, mn8tl, mn8tb, mn8tw, mn1bl, mn1bb, mn1bw, mn2bl, mn2bb, mn2bw, mn3bl, mn3bb, mn3bw, mn4bl, mn4bb, mn4bw, mn5bl, mn5bb, mn5bw, mn6bl, mn6bb, mn6bw, mn7bl, mn7bb, mn7bw, mn8bl, mn8bb, mn8bw, ms1tl, ms1tb, ms1tw, ms2tl, ms2tb, ms2tw, ms3tl, ms3tb, ms3tw, ms4tl, ms4tb, ms4tw, ms1bl, ms1bb, ms1bw, ms2bl, ms2bb, ms2bw, ms3bl, ms3bb, ms3bw, ms4bl, ms4bb, ms4bw, mo1tl, mo1tb, mo1tw, mo2tl, mo2tb, mo2tw, mo3tl, mo3tb, mo3tw, mo4tl, mo4tb, mo4tw, mo5tl, mo5tb, mo5tw, mo6tl, mo6tb, mo6tw, mo7tl, mo7tb, mo7tw, mo8tl, mo8tb, mo8tw, mo1bl, mo1bb, mo1bw, mo2bl, mo2bb, mo2bw, mo3bl, mo3bb, mo3bw, mo4bl, mo4bb, mo4bw, mo5bl, mo5bb, mo5bw, mo6bl, mo6bb, mo6bw, mo7bl, mo7bb, mo7bw, mo8bl, mo8bb, mo8bw, mt1tl, mt1tb, mt1tw, mt1bl, mt1bb, mt1bw, ne1tl, ne1tb, ne1tw, ne2tl, ne2tb, ne2tw, ne3tl, ne3tb, ne3tw, ne1bl, ne1bb, ne1bw, ne2bl, ne2bb, ne2bw, ne3bl, ne3bb, ne3bw, nv1tl, nv1tb, nv1tw, nv2tl, nv2tb, nv2tw, nv3tl, nv3tb, nv3tw, nv4tl, nv4tb, nv4tw, nv1bl, nv1bb, nv1bw, nv2bl, nv2bb, nv2bw, nv3bl, nv3bb, nv3bw, nv4bl, nv4bb, nv4bw, nh1tl, nh1tb, nh1tw, nh2tl, nh2tb, nh2tw, nh1bl, nh1bb, nh1bw, nh2bl, nh2bb, nh2bw, nj1bl, nj1bb, nj1bw, nj2bl, nj2bb, nj2bw, nj3bl, nj3bb, nj3bw, nj4bl, nj4bb, nj4bw, nj5bl, nj5bb, nj5bw, nj6bl, nj6bb, nj6bw, nj7bl, nj7bb, nj7bw, nj8bl, nj8bb, nj8bw, nj9bl, nj9bb, nj9bw, nj10bl, nj10bb, nj10bw, nj11bl, nj11bb, nj11bw, nj12bl, nj12bb, nj12bw, nj1tl, nj1tb, nj1tw, nj2tl, nj2tb, nj2tw, nj3tl, nj3tb, nj3tw, nj4tl, nj4tb, nj4tw, nj5tl, nj5tb, nj5tw, nj6tl, nj6tb, nj6tw, nj7tl, nj7tb, nj7tw, nj8tl, nj8tb, nj8tw, nj9tl, nj9tb, nj9tw, nj10tl, nj10tb, nj10tw, nj11tl, nj11tb, nj11tw, nj12tl, nj12tb, nj12tw, nm1tl, nm1tb, nm1tw, nm2tl, nm2tb, nm2tw, nm3tl, nm3tb, nm3tw, nm1bl, nm1bb, nm1bw, nm2bl, nm2bb, nm2bw, nm3bl, nm3bb, nm3bw, ny1tl, ny1tb, ny1tw, ny2tl, ny2tb, ny2tw, ny3tl, ny3tb, ny3tw, ny4tl, ny4tb, ny4tw, ny5tl, ny5tb, ny5tw, ny6tl, ny6tb, ny6tw, ny7tl, ny7tb, ny7tw, ny8tl, ny8tb, ny8tw, ny9tl, ny9tb, ny9tw, ny10tl, ny10tb, ny10tw, ny11tl, ny11tb, ny11tw, ny12tl, ny12tb, ny12tw, ny13tl, ny13tb, ny13tw, ny14tl, ny14tb, ny14tw, ny15tl, ny15tb, ny15tw, ny16tl, ny16tb, ny16tw, ny17tl, ny17tb, ny17tw, ny18tl, ny18tb, ny18tw, ny19tl, ny19tb, ny19tw, ny20tl, ny20tb, ny20tw, ny21tl, ny21tb, ny21tw, ny22tl, ny22tb, ny22tw, ny23tl, ny23tb, ny23tw, ny24tl, ny24tb, ny24tw, ny25tl, ny25tb, ny25tw, ny26tl, ny26tb, ny26tw, ny27tl, ny27tb, ny27tw, ny1bl, ny1bb, ny1bw, ny2bl, ny2bb, ny2bw, ny3bl, ny3bb, ny3bw, ny4bl, ny4bb, ny4bw, ny5bl, ny5bb, ny5bw, ny6bl, ny6bb, ny6bw, ny7bl, ny7bb, ny7bw, ny8bl, ny8bb, ny8bw, ny9bl, ny9bb, ny9bw, ny10bl, ny10bb, ny10bw, ny11bl, ny11bb, ny11bw, ny12bl, ny12bb, ny12bw, ny13bl, ny13bb, ny13bw, ny14bl, ny14bb, ny14bw, ny15bl, ny15bb, ny15bw, ny16bl, ny16bb, ny16bw, ny17bl, ny17bb, ny17bw, ny18bl, ny18bb, ny18bw, ny19bl, ny19bb, ny19bw, ny20bl, ny20bb, ny20bw, ny21bl, ny21bb, ny21bw, ny22bl, ny22bb, ny22bw, ny23bl, ny23bb, ny23bw, ny24bl, ny24bb, ny24bw, ny25bl, ny25bb, ny25bw, ny26bl, ny26bb, ny26bw, ny27bl, ny27bb, ny27bw, nc1bl, nc1bb, nc1bw, nc2bl, nc2bb, nc2bw, nc3bl, nc3bb, nc3bw, nc4bl, nc4bb, nc4bw, nc5bl, nc5bb, nc5bw, nc6bl, nc6bb, nc6bw, nc7bl, nc7bb, nc7bw, nc8bl, nc8bb, nc8bw, nc9bl, nc9bb, nc9bw, nc10bl, nc10bb, nc10bw, nc11bl, nc11bb, nc11bw, nc12bl, nc12bb, nc12bw, nc13bl, nc13bb, nc13bw, nc1tl, nc1tb, nc1tw, nc2tl, nc2tb, nc2tw, nc3tl, nc3tb, nc3tw, nc4tl, nc4tb, nc4tw, nc5tl, nc5tb, nc5tw, nc6tl, nc6tb, nc6tw, nc7tl, nc7tb, nc7tw, nc8tl, nc8tb, nc8tw, nc9tl, nc9tb, nc9tw, nc10tl, nc10tb, nc10tw, nc11tl, nc11tb, nc11tw, nc12tl, nc12tb, nc12tw, nc13tl, nc13tb, nc13tw, nd1tl, nd1tb, nd1tw, nd1bl, nd1bb, nd1bw, oh1bl, oh1bb, oh1bw, oh2bl, oh2bb, oh2bw, oh3bl, oh3bb, oh3bw, oh4bl, oh4bb, oh4bw, oh5bl, oh5bb, oh5bw, oh6bl, oh6bb, oh6bw, oh7bl, oh7bb, oh7bw, oh8bl, oh8bb, oh8bw, oh9bl, oh9bb, oh9bw, oh10bl, oh10bb, oh10bw, oh11bl, oh11bb, oh11bw, oh12bl, oh12bb, oh12bw, oh13bl, oh13bb, oh13bw, oh14bl, oh14bb, oh14bw, oh15bl, oh15bb, oh15bw, oh16bl, oh16bb, oh16bw, oh1tl, oh1tb, oh1tw, oh2tl, oh2tb, oh2tw, oh3tl, oh3tb, oh3tw, oh4tl, oh4tb, oh4tw, oh5tl, oh5tb, oh5tw, oh6tl, oh6tb, oh6tw, oh7tl, oh7tb, oh7tw, oh8tl, oh8tb, oh8tw, oh9tl, oh9tb, oh9tw, oh10tl, oh10tb, oh10tw, oh11tl, oh11tb, oh11tw, oh12tl, oh12tb, oh12tw, oh13tl, oh13tb, oh13tw, oh14tl, oh14tb, oh14tw, oh15tl, oh15tb, oh15tw, oh16tl, oh16tb, oh16tw, ok1tl, ok1tb, ok1tw, ok2tl, ok2tb, ok2tw, ok3tl, ok3tb, ok3tw, ok4tl, ok4tb, ok4tw, ok5tl, ok5tb, ok5tw, ok1bl, ok1bb, ok1bw, ok2bl, ok2bb, ok2bw, ok3bl, ok3bb, ok3bw, ok4bl, ok4bb, ok4bw, ok5bl, ok5bb, ok5bw, or1tl, or1tb, or1tw, or2tl, or2tb, or2tw, or3tl, or3tb, or3tw, or4tl, or4tb, or4tw, or5tl, or5tb, or5tw, or1bl, or1bb, or1bw, or2bl, or2bb, or2bw, or3bl, or3bb, or3bw, or4bl, or4bb, or4bw, or5bl, or5bb, or5bw, pa1bl, pa1bb, pa1bw, pa2bl, pa2bb, pa2bw, pa3bl, pa3bb, pa3bw, pa4bl, pa4bb, pa4bw, pa5bl, pa5bb, pa5bw, pa6bl, pa6bb, pa6bw, pa7bl, pa7bb, pa7bw, pa8bl, pa8bb, pa8bw, pa9bl, pa9bb, pa9bw, pa10bl, pa10bb, pa10bw, pa11bl, pa11bb, pa11bw, pa12bl, pa12bb, pa12bw, pa13bl, pa13bb, pa13bw, pa14bl, pa14bb, pa14bw, pa15bl, pa15bb, pa15bw, pa16bl, pa16bb, pa16bw, pa17bl, pa17bb, pa17bw, pa18bl, pa18bb, pa18bw, pa1tl, pa1tb, pa1tw, pa2tl, pa2tb, pa2tw, pa3tl, pa3tb, pa3tw, pa4tl, pa4tb, pa4tw, pa5tl, pa5tb, pa5tw, pa6tl, pa6tb, pa6tw, pa7tl, pa7tb, pa7tw, pa8tl, pa8tb, pa8tw, pa9tl, pa9tb, pa9tw, pa10tl, pa10tb, pa10tw, pa11tl, pa11tb, pa11tw, pa12tl, pa12tb, pa12tw, pa13tl, pa13tb, pa13tw, pa14tl, pa14tb, pa14tw, pa15tl, pa15tb, pa15tw, pa16tl, pa16tb, pa16tw, pa17tl, pa17tb, pa17tw, pa18tl, pa18tb, pa18tw, ri1tl, ri1tb, ri1tw, ri2tl, ri2tb, ri2tw, ri1bl, ri1bb, ri1bw, ri2bl, ri2bb, ri2bw, sc1tl, sc1tb, sc1tw, sc2tl, sc2tb, sc2tw, sc3tl, sc3tb, sc3tw, sc4tl, sc4tb, sc4tw, sc5tl, sc5tb, sc5tw, sc6tl, sc6tb, sc6tw, sc7tl, sc7tb, sc7tw, sc1bl, sc1bb, sc1bw, sc2bl, sc2bb, sc2bw, sc3bl, sc3bb, sc3bw, sc4bl, sc4bb, sc4bw, sc5bl, sc5bb, sc5bw, sc6bl, sc6bb, sc6bw, sc7bl, sc7bb, sc7bw, sd1tl, sd1tb, sd1tw, sd1bl, sd1bb, sd1bw, tn1tl, tn1tb, tn1tw, tn2tl, tn2tb, tn2tw, tn3tl, tn3tb, tn3tw, tn4tl, tn4tb, tn4tw, tn5tl, tn5tb, tn5tw, tn6tl, tn6tb, tn6tw, tn7tl, tn7tb, tn7tw, tn8tl, tn8tb, tn8tw, tn9tl, tn9tb, tn9tw, tn1bl, tn1bb, tn1bw, tn2bl, tn2bb, tn2bw, tn3bl, tn3bb, tn3bw, tn4bl, tn4bb, tn4bw, tn5bl, tn5bb, tn5bw, tn6bl, tn6bb, tn6bw, tn7bl, tn7bb, tn7bw, tn8bl, tn8bb, tn8bw, tn9bl, tn9bb, tn9bw, tx1tl, tx1tb, tx1tw, tx2tl, tx2tb, tx2tw, tx3tl, tx3tb, tx3tw, tx4tl, tx4tb, tx4tw, tx5tl, tx5tb, tx5tw, tx6tl, tx6tb, tx6tw, tx7tl, tx7tb, tx7tw, tx8tl, tx8tb, tx8tw, tx9tl, tx9tb, tx9tw, tx10tl, tx10tb, tx10tw, tx11tl, tx11tb, tx11tw, tx12tl, tx12tb, tx12tw, tx13tl, tx13tb, tx13tw, tx14tl, tx14tb, tx14tw, tx15tl, tx15tb, tx15tw, tx16tl, tx16tb, tx16tw, tx17tl, tx17tb, tx17tw, tx18tl, tx18tb, tx18tw, tx19tl, tx19tb, tx19tw, tx20tl, tx20tb, tx20tw, tx21tl, tx21tb, tx21tw, tx22tl, tx22tb, tx22tw, tx23tl, tx23tb, tx23tw, tx24tl, tx24tb, tx24tw, tx25tl, tx25tb, tx25tw, tx26tl, tx26tb, tx26tw, tx27tl, tx27tb, tx27tw, tx28tl, tx28tb, tx28tw, tx29tl, tx29tb, tx29tw, tx30tl, tx30tb, tx30tw, tx31tl, tx31tb, tx31tw, tx32tl, tx32tb, tx32tw, tx33tl, tx33tb, tx33tw, tx34tl, tx34tb, tx34tw, tx35tl, tx35tb, tx35tw, tx36tl, tx36tb, tx36tw, tx1bl, tx1bb, tx1bw, tx2bl, tx2bb, tx2bw, tx3bl, tx3bb, tx3bw, tx4bl, tx4bb, tx4bw, tx5bl, tx5bb, tx5bw, tx6bl, tx6bb, tx6bw, tx7bl, tx7bb, tx7bw, tx8bl, tx8bb, tx8bw, tx9bl, tx9bb, tx9bw, tx10bl, tx10bb, tx10bw, tx11bl, tx11bb, tx11bw, tx12bl, tx12bb, tx12bw, tx13bl, tx13bb, tx13bw, tx14bl, tx14bb, tx14bw, tx15bl, tx15bb, tx15bw, tx16bl, tx16bb, tx16bw, tx17bl, tx17bb, tx17bw, tx18bl, tx18bb, tx18bw, tx19bl, tx19bb, tx19bw, tx20bl, tx20bb, tx20bw, tx21bl, tx21bb, tx21bw, tx22bl, tx22bb, tx22bw, tx23bl, tx23bb, tx23bw, tx24bl, tx24bb, tx24bw, tx25bl, tx25bb, tx25bw, tx26bl, tx26bb, tx26bw, tx27bl, tx27bb, tx27bw, tx28bl, tx28bb, tx28bw, tx29bl, tx29bb, tx29bw, tx30bl, tx30bb, tx30bw, tx31bl, tx31bb, tx31bw, tx32bl, tx32bb, tx32bw, tx33bl, tx33bb, tx33bw, tx34bl, tx34bb, tx34bw, tx35bl, tx35bb, tx35bw, tx36bl, tx36bb, tx36bw, ut1tl, ut1tb, ut1tw, ut2tl, ut2tb, ut2tw, ut3tl, ut3tb, ut3tw, ut4tl, ut4tb, ut4tw, ut1bl, ut1bb, ut1bw, ut2bl, ut2bb, ut2bw, ut3bl, ut3bb, ut3bw, ut4bl, ut4bb, ut4bw, vt1tl, vt1tb, vt1tw, vt1bl, vt1bb, vt1bw, va1bl, va1bb, va1bw, va2bl, va2bb, va2bw, va3bl, va3bb, va3bw, va4bl, va4bb, va4bw, va5bl, va5bb, va5bw, va6bl, va6bb, va6bw, va7bl, va7bb, va7bw, va8bl, va8bb, va8bw, va9bl, va9bb, va9bw, va10bl, va10bb, va10bw, va11bl, va11bb, va11bw, va1tl, va1tb, va1tw, va2tl, va2tb, va2tw, va3tl, va3tb, va3tw, va4tl, va4tb, va4tw, va5tl, va5tb, va5tw, va6tl, va6tb, va6tw, va7tl, va7tb, va7tw, va8tl, va8tb, va8tw, va9tl, va9tb, va9tw, va10tl, va10tb, va10tw, va11tl, va11tb, va11tw, wa1bl, wa1bb, wa1bw, wa2bl, wa2bb, wa2bw, wa3bl, wa3bb, wa3bw, wa4bl, wa4bb, wa4bw, wa5bl, wa5bb, wa5bw, wa6bl, wa6bb, wa6bw, wa7bl, wa7bb, wa7bw, wa8bl, wa8bb, wa8bw, wa9bl, wa9bb, wa9bw, wa10bl, wa10bb, wa10bw, wa1tl, wa1tb, wa1tw, wa2tl, wa2tb, wa2tw, wa3tl, wa3tb, wa3tw, wa4tl, wa4tb, wa4tw, wa5tl, wa5tb, wa5tw, wa6tl, wa6tb, wa6tw, wa7tl, wa7tb, wa7tw, wa8tl, wa8tb, wa8tw, wa9tl, wa9tb, wa9tw, wa10tl, wa10tb, wa10tw, wv1tl, wv1tb, wv1tw, wv2tl, wv2tb, wv2tw, wv3tl, wv3tb, wv3tw, wv1bl, wv1bb, wv1bw, wv2bl, wv2bb, wv2bw, wv3bl, wv3bb, wv3bw, wi1tl, wi1tb, wi1tw, wi2tl, wi2tb, wi2tw, wi3tl, wi3tb, wi3tw, wi4tl, wi4tb, wi4tw, wi5tl, wi5tb, wi5tw, wi6tl, wi6tb, wi6tw, wi7tl, wi7tb, wi7tw, wi8tl, wi8tb, wi8tw, wi1bl, wi1bb, wi1bw, wi2bl, wi2bb, wi2bw, wi3bl, wi3bb, wi3bw, wi4bl, wi4bb, wi4bw, wi5bl, wi5bb, wi5bw, wi6bl, wi6bb, wi6bw, wi7bl, wi7bb, wi7bw, wi8bl, wi8bb, wi8bw, wy1tl, wy1tb, wy1tw, wy1bl, wy1bb, wy1bw], f)


