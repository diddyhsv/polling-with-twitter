import sys
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


# mo1tl, mo1tb, mo1tw, mo1bl, mo1bb, mo1bw = [], [], [], [], [], []
# co1tl, co1tb, co1tw, co1bl, co1bb, co1bw = [], [], [], [], [], []
# sc1tl, sc1tb, sc1tw, sc1bl, sc1bb, sc1bw = [], [], [], [], [], []
# mn1tl, mn1tb, mn1tw, mn1bl, mn1bb, mn1bw = [], [], [], [], [], []
# in1tl, in1tb, in1tw, in1bl, in1bb, in1bw = [], [], [], [], [], []
# md1tl, md1tb, md1tw, md1bl, md1bb, md1bw = [], [], [], [], [], []
# sd1tl, sd1tb, sd1tw, sd1bl, sd1bb, sd1bw =  [], [], [], [], [], []
# vt1tl, vt1tb, vt1tw, vt1bl, vt1bb, vt1bw =  [], [], [], [], [], []
# nd1tl, nd1tb, nd1tw, nd1bl, nd1bb, nd1bw =  [], [], [], [], [], []
# de1tl, de1tb, de1tw, de1bl, de1bb, de1bw =  [], [], [], [], [], []
# mt1tl, mt1tb, mt1tw, mt1bl, mt1bb, mt1bw =  [], [], [], [], [], []
# ne1tl, ne1tb, ne1tw, ne1bl, ne1bb, ne1bw = [], [], [], [], [], []
# ma1tl, ma1tb, ma1tw, ma1bl, ma1bb, ma1bw = [], [], [], [], [], []
# va1tl, va1tb, va1tw, va1bl, va1bb, va1bw = [], [], [], [], [], []
# me1tl, me1tb, me1tw, me1bl, me1bb, me1bw = [], [], [], [], [], []
# id1tl, id1tb, id1tw, id1bl, id1bb, id1bw = [], [], [], [], [], []
# wi1tl, wi1tb, wi1tw, wi1bl, wi1bb, wi1bw = [], [], [], [], [], []
# wv1tl, wv1tb, wv1tw, wv1bl, wv1bb, wv1bw = [], [], [], [], [], []
# ia1tl, ia1tb, ia1tw, ia1bl, ia1bb, ia1bw = [], [], [], [], [], []
# ms1tl, ms1tb, ms1tw, ms1bl, ms1bb, ms1bw = [], [], [], [], [], []
# hi1tl, hi1tb, hi1tw, hi1bl, hi1bb, hi1bw = [], [], [], [], [], []
# ri1bl, ri1bb, ri1bw, ri1tl, ri1tb, ri1tw = [], [], [], [], [], []
# wa1tl, wa1tb, wa1tw, wa1bl, wa1bb, wa1bw = [], [], [], [], [], []
# fl1tl, fl1tb, fl1tw, fl1bl, fl1bb, fl1bw = [], [], [], [], [], []
# al1tl, al1tb, al1tw, al1bl, al1bb, al1bw = [], [], [], [], [], []
# il1tl, il1tb, il1tw, il1bl, il1bb, il1bw = [], [], [], [], [], []
# ca1tl, ca1tb, ca1tw, ca1bl, ca1bb, ca1bw = [], [], [], [], [], []
# ks1tl, ks1tb, ks1tw, ks1bl, ks1bb, ks1bw = [], [], [], [], [], []
# ga1tl, ga1tb, ga1tw, ga1bl, ga1bb, ga1bw = [], [], [], [], [], []
# az1tl, az1tb, az1tw, az1bl, az1bb, az1bw = [], [], [], [], [], []
# ak1tl, ak1tb, ak1tw, ak1bl, ak1bb, ak1bw =  [], [], [], [], [], []
# ar1tl, ar1tb, ar1tw, ar1bl, ar1bb, ar1bw = [], [], [], [], [], []
# nj1tl, nj1tb, nj1tw, nj1bl, nj1bb, nj1bw = [], [], [], [], [], []
# nv1tl, nv1tb, nv1tw, nv1bl, nv1bb, nv1bw = [], [], [], [], [], []
# nh1tl, nh1tb, nh1tw, nh1bl, nh1bb, nh1bw = [], [], [], [], [], []
# nc1tl, nc1tb, nc1tw, nc1bl, nc1bb, nc1bw = [], [], [], [], [], []
# tx1tl, tx1tb, tx1tw, tx1bl, tx1bb, tx1bw = [], [], [], [], [], []
# tn1tl, tn1tb, tn1tw, tn1bl, tn1bb, tn1bw = [], [], [], [], [], []
# nm1tl, nm1tb, nm1tw, nm1bl, nm1bb, nm1bw = [], [], [], [], [], []
# ny1tl, ny1tb, ny1tw, ny1bl, ny1bb, ny1bw = [], [], [], [], [], []
# wy1tl, wy1tb, wy1tw, wy1bl, wy1bb, wy1bw =  [], [], [], [], [], []
# pa1tl, pa1tb, pa1tw, pa1bl, pa1bb, pa1bw = [], [], [], [], [], []
# ct1tl, ct1tb, ct1tw, ct1bl, ct1bb, ct1bw = [], [], [], [], [], []
# ky1tl, ky1tb, ky1tw, ky1bl, ky1bb, ky1bw = [], [], [], [], [], []
# la1tl, la1tb, la1tw, la1bl, la1bb, la1bw = [], [], [], [], [], []
# ok1tl, ok1tb, ok1tw, ok1bl, ok1bb, ok1bw = [], [], [], [], [], []
# ut1tl, ut1tb, ut1tw, ut1bl, ut1bb, ut1bw = [], [], [], [], [], []
# oh1tl, oh1tb, oh1tw, oh1bl, oh1bb, oh1bw = [], [], [], [], [], []
# or1tl, or1tb, or1tw, or1bl, or1bb, or1bw=  [], [], [], [], [], []
# mi1tl, mi1tb, mi1tw, mi1bl, mi1bb, mi1bw=  [], [], [], [], [], []

with open("/Volumes/TOSHIBA_BACKUP/usastateswithgender.txt", 'rb') as f:
	al1tl, al1tb, al1tw, al1bl, al1bb, al1bw, ak1tl, ak1tb, ak1tw, ak1bl, ak1bb, ak1bw, az1tl, az1tb, az1tw, az1bl, az1bb, az1bw, ar1bl, ar1bb, ar1bw, ar1tl, ar1tb, ar1tw, ak1bl, ak1bb, ak1bw, ca1tl, ca1tb, ca1tw, ca1bl, ca1bb, ca1bw, co1tl, co1tb, co1tw, co1bl, co1bb, co1bw, ct1bl, ct1bb, ct1bw, ct1tl, ct1tb, ct1tw, de1tl, de1tb, de1tw, de1bl, de1bb, de1bw, fl1bl, fl1bb, fl1bw, fl1tl, fl1tb, fl1tw, ga1tl, ga1tb, ga1tw, ga1bl, ga1bb, ga1bw, hi1tl, hi1tb, hi1tw, hi1bl, hi1bb, hi1bw, id1tl, id1tb, id1tw, id1bl, id1bb, id1bw, il1bl, il1bb, il1bw, il1tl, il1tb, il1tw, in1tl, in1tb, in1tw, in1bl, in1bb, in1bw, ia1tl, ia1tb, ia1tw, ia1bl, ia1bb, ia1bw, ks1tl, ks1tb, ks1tw, ks1bl, ks1bb, ks1bw, ky1tl, ky1tb, ky1tw, ky1bl, ky1bb, ky1bw, la1tl, la1tb, la1tw, la1bl, la1bb, la1bw, me1tl, me1tb, me1tw, me1bl, me1bb, me1bw, md1tl, md1tb, md1tw, md1bl, md1bb, md1bw, ma1tl, ma1tb, ma1tw, ma1bl, ma1bb, ma1bw, mi1bl, mi1bb, mi1bw, mi1tl, mi1tb, mi1tw, mn1tl, mn1tb, mn1tw, mn1bl, mn1bb, mn1bw, ms1tl, ms1tb, ms1tw, ms1bl, ms1bb, ms1bw, mo1tl, mo1tb, mo1tw, mo1bl, mo1bb, mo1bw, mt1tl, mt1tb, mt1tw, mt1bl, mt1bb, mt1bw, ne1tl, ne1tb, ne1tw, ne1bl, ne1bb, ne1bw, nv1tl, nv1tb, nv1tw, nv1bl, nv1bb, nv1bw, nh1tl, nh1tb, nh1tw, nh1bl, nh1bb, nh1bw, nj1bl, nj1bb, nj1bw, nj1tl, nj1tb, nj1tw, nm1tl, nm1tb, nm1tw, nm1bl, nm1bb, nm1bw, ny1tl, ny1tb, ny1tw, ny1bl, ny1bb, ny1bw, nc1bl, nc1bb, nc1bw, nc1tl, nc1tb, nc1tw, nd1tl, nd1tb, nd1tw, nd1bl, nd1bb, nd1bw, oh1bl, oh1bb, oh1bw, oh1tl, oh1tb, oh1tw, ok1tl, ok1tb, ok1tw, ok1bl, ok1bb, ok1bw, or1tl, or1tb, or1tw, or1bl, or1bb, or1bw, pa1bl, pa1bb, pa1bw, pa1tl, pa1tb, pa1tw, ri1tl, ri1tb, ri1tw, ri1bl, ri1bb, ri1bw, sc1tl, sc1tb, sc1tw, sc1bl, sc1bb, sc1bw, sd1tl, sd1tb, sd1tw, sd1bl, sd1bb, sd1bw, tn1tl, tn1tb, tn1tw, tn1bl, tn1bb, tn1bw, tx1tl, tx1tb, tx1tw, tx1bl, tx1bb, tx1bw, ut1tl, ut1tb, ut1tw, ut1bl, ut1bb, ut1bw, vt1tl, vt1tb, vt1tw, vt1bl, vt1bb, vt1bw, va1bl, va1bb, va1bw, va1tl, va1tb, va1tw, wa1bl, wa1bb, wa1bw, wa1tl, wa1tb, wa1tw, wv1tl, wv1tb, wv1tw, wv1bl, wv1bb, wv1bw, wi1tl, wi1tb, wi1tw, wi1bl, wi1bb, wi1bw, wy1tl, wy1tb, wy1tw, wy1bl, wy1bb, wy1bw = pickle.load(f)


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
	if("#trump2020" in tw["retweeted_status"]["full_text"].lower() or "#votered" in tw["retweeted_status"]["full_text"].lower() ):
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
			sortEthnic(al1tl, al1tb, al1tw, tw)
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
			sortEthnic(ak1tl, ak1tb, ak1tw, tw)
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
			sortEthnic(az1tl, az1tb, az1tw, tw)
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
			sortEthnic(ar1tl, ar1tb, ar1tw, tw)
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower()):
			sortEthnic(ca1tl, ca1tb, ca1tw, tw)
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
			sortEthnic(co1tl, co1tb, co1tw, tw)
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
			sortEthnic(ct1tl, ct1tb, ct1tw, tw)
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
			sortEthnic(de1tl, de1tb, de1tw, tw)
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower()):
			sortEthnic(fl1tl, fl1tb, fl1tw, tw)
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
			sortEthnic(ga1tl, ga1tb, ga1tw, tw)
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower()):
			sortEthnic(hi1tl, hi1tb, hi1tw, tw)
		if(" ID" in tw["user"]["location"] or "idaho" in tw["user"]["location"].lower()):
			sortEthnic(id1tl, id1tb, id1tw, tw)
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower()):
			sortEthnic(il1tl, il1tb, il1tw, tw)
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
			sortEthnic(in1tl, in1tb, in1tw, tw)
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
			sortEthnic(ia1tl, ia1tb, ia1tw, tw)
		if(" KS" in tw["user"]["location"] or "kansas" in tw["user"]["location"].lower()):
			sortEthnic(ks1tl, ks1tb, ks1tw, tw)
		if(" KY" in tw["user"]["location"] or "kentucky" in tw["user"]["location"].lower()):
			sortEthnic(ky1tl, ky1tb, ky1tw, tw)
		if(" LA" in tw["user"]["location"] or "louisiana" in tw["user"]["location"].lower()):
			sortEthnic(la1tl, la1tb, la1tw, tw)
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
			sortEthnic(me1tl, me1tb, me1tw, tw)
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
			sortEthnic(md1tl, md1tb, md1tw, tw)
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower()):
			sortEthnic(ma1tl, ma1tb, ma1tw, tw)
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
			sortEthnic(mi1tl, mi1tb, mi1tw, tw)
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
			sortEthnic(mn1tl, mn1tb, mn1tw, tw) #done
		if(" MS" in tw["user"]["location"] or "mississippi" in tw["user"]["location"].lower()):
			sortEthnic(ms1tl, ms1tb, ms1tw, tw)
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
			sortEthnic(mo1tl, mo1tb, mo1tw, tw)	#done
		if(" MT" in tw["user"]["location"] or "montana" in tw["user"]["location"].lower()):
			sortEthnic(mt1tl, mt1tb, mt1tw, tw)	#done
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
			sortEthnic(ne1tl, ne1tb, ne1tw, tw)
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower()):
			sortEthnic(nv1tl, nv1tb, nv1tw, tw) #done
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
			sortEthnic(nh1tl, nh1tb, nh1tw, tw) #done
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
			sortEthnic(nj1tl, nj1tb, nj1tw, tw)	#done
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
			sortEthnic(nm1tl, nm1tb, nm1tw, tw)	#done
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
			sortEthnic(ny1tl, ny1tb, ny1tw, tw) #done
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
			sortEthnic(nc1tl, nc1tb, nc1tw, tw) #done
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
			sortEthnic(nd1tl, nd1tb, nd1tw, tw)
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
			sortEthnic(oh1tl, oh1tb, oh1tw, tw)
		if(" OK" in tw["user"]["location"] or "oklahoma" in tw["user"]["location"].lower()):
			sortEthnic(ok1tl, ok1tb, ok1tw, tw) #done
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
			sortEthnic(or1tl, or1tb, or1tw, tw) #done
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
			sortEthnic(pa1tl, pa1tb, pa1tw, tw)
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
			sortEthnic(ri1tl, ri1tb, ri1tw, tw)
		if(" SC" in tw["user"]["location"] or "south carolina" in tw["user"]["location"].lower()):
			sortEthnic(sc1tl, sc1tb, sc1tw, tw) #done
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
			sortEthnic(sd1tl, sd1tb, sd1tw, tw)
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
			sortEthnic(tn1tl, tn1tb, tn1tw, tw) #done
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
			sortEthnic(tx1tl, tx1tb, tx1tw, tw)
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
			sortEthnic(ut1tl, ut1tb, ut1tw, tw) #done
		if(" VT" in tw["user"]["location"] or "vermont" in tw["user"]["location"].lower()):
			sortEthnic(vt1tl, vt1tb, vt1tw, tw) #done
		if(" VA" in tw["user"]["location"] or ("virginia" in tw["user"]["location"].lower() and not "west virginia" in tw["user"]["location"].lower())):
			sortEthnic(va1tl, va1tb, va1tw, tw)
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
			sortEthnic(wa1tl, wa1tb, wa1tw, tw)
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
			sortEthnic(wv1tl, wv1tb, wv1tw, tw)
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
			sortEthnic(wi1tl, wi1tb, wi1tw, tw)
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
			sortEthnic(wy1tl, wy1tb, wy1tw, tw)
	if("#biden2020" in tw["retweeted_status"]["full_text"].lower() or "#voteblue" in tw["retweeted_status"]["full_text"].lower() ):
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
			sortEthnic(al1bl, al1bb, al1bw, tw)
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
			sortEthnic(ak1bl, ak1bb, ak1bw, tw)
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
			sortEthnic(az1bl, az1bb, az1bw, tw)
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
			sortEthnic(ar1bl, ar1bb, ar1bw, tw)
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower()):
			sortEthnic(ca1bl, ca1bb, ca1bw, tw)
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
			sortEthnic(co1bl, co1bb, co1bw, tw)
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
			sortEthnic(ct1bl, ct1bb, ct1bw, tw)
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
			sortEthnic(de1bl, de1bb, de1bw, tw)
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower()):
			sortEthnic(fl1bl, fl1bb, fl1bw, tw)
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
			sortEthnic(ga1bl, ga1bb, ga1bw, tw)
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower()):
			sortEthnic(hi1bl, hi1bb, hi1bw, tw)
		if(" ID" in tw["user"]["location"] or "idaho" in tw["user"]["location"].lower()):
			sortEthnic(id1bl, id1bb, id1bw, tw)
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower()):
			sortEthnic(il1bl, il1bb, il1bw, tw)
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
			sortEthnic(in1bl, in1bb, in1bw, tw)
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
			sortEthnic(ia1bl, ia1bb, ia1bw, tw)
		if(" KS" in tw["user"]["location"] or "kansas" in tw["user"]["location"].lower()):
			sortEthnic(ks1bl, ks1bb, ks1bw, tw)
		if(" KY" in tw["user"]["location"] or "kentucky" in tw["user"]["location"].lower()):
			sortEthnic(ky1bl, ky1bb, ky1bw, tw)
		if(" LA" in tw["user"]["location"] or "louisiana" in tw["user"]["location"].lower()):
			sortEthnic(la1bl, la1bb, la1bw, tw)
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
			sortEthnic(me1bl, me1bb, me1bw, tw)
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
			sortEthnic(md1bl, md1bb, md1bw, tw)
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower()):
			sortEthnic(ma1bl, ma1bb, ma1bw, tw)
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
			sortEthnic(mi1bl, mi1bb, mi1bw, tw)
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
			sortEthnic(mn1bl, mn1bb, mn1bw, tw) #done
		if(" MS" in tw["user"]["location"] or "mississippi" in tw["user"]["location"].lower()):
			sortEthnic(ms1bl, ms1bb, ms1bw, tw)
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
			sortEthnic(mo1bl, mo1bb, mo1bw, tw)	#done
		if(" MT" in tw["user"]["location"] or "montana" in tw["user"]["location"].lower()):
			sortEthnic(mt1bl, mt1bb, mt1bw, tw)	#done
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
			sortEthnic(ne1bl, ne1bb, ne1bw, tw)
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower()):
			sortEthnic(nv1bl, nv1bb, nv1bw, tw) #done
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
			sortEthnic(nh1bl, nh1bb, nh1bw, tw) #done
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
			sortEthnic(nj1bl, nj1bb, nj1bw, tw)	#done
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
			sortEthnic(nm1bl, nm1bb, nm1bw, tw)	#done
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
			sortEthnic(ny1bl, ny1bb, ny1bw, tw) #done
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
			sortEthnic(nc1bl, nc1bb, nc1bw, tw) #done
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
			sortEthnic(nd1bl, nd1bb, nd1bw, tw)
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
			sortEthnic(oh1bl, oh1bb, oh1bw, tw)
		if(" OK" in tw["user"]["location"] or "oklahoma" in tw["user"]["location"].lower()):
			sortEthnic(ok1bl, ok1bb, ok1bw, tw) #done
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
			sortEthnic(or1bl, or1bb, or1bw, tw) #done
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
			sortEthnic(pa1bl, pa1bb, pa1bw, tw)
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
			sortEthnic(ri1bl, ri1bb, ri1bw, tw)
		if(" SC" in tw["user"]["location"] or "south carolina" in tw["user"]["location"].lower()):
			sortEthnic(sc1bl, sc1bb, sc1bw, tw) #done
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
			sortEthnic(sd1bl, sd1bb, sd1bw, tw)
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
			sortEthnic(tn1bl, tn1bb, tn1bw, tw) #done
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
			sortEthnic(tx1bl, tx1bb, tx1bw, tw)
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
			sortEthnic(ut1bl, ut1bb, ut1bw, tw) #done
		if(" VT" in tw["user"]["location"] or "vermont" in tw["user"]["location"].lower()):
			sortEthnic(vt1bl, vt1bb, vt1bw, tw) #done
		if(" VA" in tw["user"]["location"] or ("virginia" in tw["user"]["location"].lower() and not "west virginia" in tw["user"]["location"].lower())):
			sortEthnic(va1bl, va1bb, va1bw, tw)
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
			sortEthnic(wa1bl, wa1bb, wa1bw, tw)
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
			sortEthnic(wv1bl, wv1bb, wv1bw, tw)
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
			sortEthnic(wi1bl, wi1bb, wi1bw, tw)
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
			sortEthnic(wy1bl, wy1bb, wy1bw, tw)
cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:	 
	if("#trump2020" in tw["full_text"].lower() or "#votered" in tw["full_text"].lower() ):
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
			sortEthnic(al1tl, al1tb, al1tw, tw)
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
			sortEthnic(ak1tl, ak1tb, ak1tw, tw)
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
			sortEthnic(az1tl, az1tb, az1tw, tw)
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
			sortEthnic(ar1tl, ar1tb, ar1tw, tw)
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower()):
			sortEthnic(ca1tl, ca1tb, ca1tw, tw)
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
			sortEthnic(co1tl, co1tb, co1tw, tw)
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
			sortEthnic(ct1tl, ct1tb, ct1tw, tw)
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
			sortEthnic(de1tl, de1tb, de1tw, tw)
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower()):
			sortEthnic(fl1tl, fl1tb, fl1tw, tw)
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
			sortEthnic(ga1tl, ga1tb, ga1tw, tw)
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower()):
			sortEthnic(hi1tl, hi1tb, hi1tw, tw)
		if(" ID" in tw["user"]["location"] or "idaho" in tw["user"]["location"].lower()):
			sortEthnic(id1tl, id1tb, id1tw, tw)
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower()):
			sortEthnic(il1tl, il1tb, il1tw, tw)
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
			sortEthnic(in1tl, in1tb, in1tw, tw)
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
			sortEthnic(ia1tl, ia1tb, ia1tw, tw)
		if(" KS" in tw["user"]["location"] or "kansas" in tw["user"]["location"].lower()):
			sortEthnic(ks1tl, ks1tb, ks1tw, tw)
		if(" KY" in tw["user"]["location"] or "kentucky" in tw["user"]["location"].lower()):
			sortEthnic(ky1tl, ky1tb, ky1tw, tw)
		if(" LA" in tw["user"]["location"] or "louisiana" in tw["user"]["location"].lower()):
			sortEthnic(la1tl, la1tb, la1tw, tw)
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
			sortEthnic(me1tl, me1tb, me1tw, tw)
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
			sortEthnic(md1tl, md1tb, md1tw, tw)
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower()):
			sortEthnic(ma1tl, ma1tb, ma1tw, tw)
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
			sortEthnic(mi1tl, mi1tb, mi1tw, tw)
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
			sortEthnic(mn1tl, mn1tb, mn1tw, tw) #done
		if(" MS" in tw["user"]["location"] or "mississippi" in tw["user"]["location"].lower()):
			sortEthnic(ms1tl, ms1tb, ms1tw, tw)
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
			sortEthnic(mo1tl, mo1tb, mo1tw, tw)	#done
		if(" MT" in tw["user"]["location"] or "montana" in tw["user"]["location"].lower()):
			sortEthnic(mt1tl, mt1tb, mt1tw, tw)	#done
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
			sortEthnic(ne1tl, ne1tb, ne1tw, tw)
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower()):
			sortEthnic(nv1tl, nv1tb, nv1tw, tw) #done
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
			sortEthnic(nh1tl, nh1tb, nh1tw, tw) #done
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
			sortEthnic(nj1tl, nj1tb, nj1tw, tw)	#done
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
			sortEthnic(nm1tl, nm1tb, nm1tw, tw)	#done
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
			sortEthnic(ny1tl, ny1tb, ny1tw, tw) #done
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
			sortEthnic(nc1tl, nc1tb, nc1tw, tw) #done
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
			sortEthnic(nd1tl, nd1tb, nd1tw, tw)
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
			sortEthnic(oh1tl, oh1tb, oh1tw, tw)
		if(" OK" in tw["user"]["location"] or "oklahoma" in tw["user"]["location"].lower()):
			sortEthnic(ok1tl, ok1tb, ok1tw, tw) #done
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
			sortEthnic(or1tl, or1tb, or1tw, tw) #done
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
			sortEthnic(pa1tl, pa1tb, pa1tw, tw)
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
			sortEthnic(ri1tl, ri1tb, ri1tw, tw)
		if(" SC" in tw["user"]["location"] or "south carolina" in tw["user"]["location"].lower()):
			sortEthnic(sc1tl, sc1tb, sc1tw, tw) #done
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
			sortEthnic(sd1tl, sd1tb, sd1tw, tw)
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
			sortEthnic(tn1tl, tn1tb, tn1tw, tw) #done
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
			sortEthnic(tx1tl, tx1tb, tx1tw, tw)
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
			sortEthnic(ut1tl, ut1tb, ut1tw, tw) #done
		if(" VT" in tw["user"]["location"] or "vermont" in tw["user"]["location"].lower()):
			sortEthnic(vt1tl, vt1tb, vt1tw, tw) #done
		if(" VA" in tw["user"]["location"] or ("virginia" in tw["user"]["location"].lower() and not "west virginia" in tw["user"]["location"].lower())):
			sortEthnic(va1tl, va1tb, va1tw, tw)
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
			sortEthnic(wa1tl, wa1tb, wa1tw, tw)
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
			sortEthnic(wv1tl, wv1tb, wv1tw, tw)
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
			sortEthnic(wi1tl, wi1tb, wi1tw, tw)
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
			sortEthnic(wy1tl, wy1tb, wy1tw, tw)
	if("#biden2020" in tw["full_text"].lower() or "#voteblue" in tw["full_text"].lower() ):
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
			sortEthnic(al1bl, al1bb, al1bw, tw)
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
			sortEthnic(ak1bl, ak1bb, ak1bw, tw)
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
			sortEthnic(az1bl, az1bb, az1bw, tw)
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
			sortEthnic(ar1bl, ar1bb, ar1bw, tw)
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower()):
			sortEthnic(ca1bl, ca1bb, ca1bw, tw)
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
			sortEthnic(co1bl, co1bb, co1bw, tw)
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
			sortEthnic(ct1bl, ct1bb, ct1bw, tw)
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
			sortEthnic(de1bl, de1bb, de1bw, tw)
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower()):
			sortEthnic(fl1bl, fl1bb, fl1bw, tw)
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
			sortEthnic(ga1bl, ga1bb, ga1bw, tw)
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower()):
			sortEthnic(hi1bl, hi1bb, hi1bw, tw)
		if(" ID" in tw["user"]["location"] or "idaho" in tw["user"]["location"].lower()):
			sortEthnic(id1bl, id1bb, id1bw, tw)
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower()):
			sortEthnic(il1bl, il1bb, il1bw, tw)
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
			sortEthnic(in1bl, in1bb, in1bw, tw)
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
			sortEthnic(ia1bl, ia1bb, ia1bw, tw)
		if(" KS" in tw["user"]["location"] or "kansas" in tw["user"]["location"].lower()):
			sortEthnic(ks1bl, ks1bb, ks1bw, tw)
		if(" KY" in tw["user"]["location"] or "kentucky" in tw["user"]["location"].lower()):
			sortEthnic(ky1bl, ky1bb, ky1bw, tw)
		if(" LA" in tw["user"]["location"] or "louisiana" in tw["user"]["location"].lower()):
			sortEthnic(la1bl, la1bb, la1bw, tw)
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
			sortEthnic(me1bl, me1bb, me1bw, tw)
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
			sortEthnic(md1bl, md1bb, md1bw, tw)
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower()):
			sortEthnic(ma1bl, ma1bb, ma1bw, tw)
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
			sortEthnic(mi1bl, mi1bb, mi1bw, tw)
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
			sortEthnic(mn1bl, mn1bb, mn1bw, tw) #done
		if(" MS" in tw["user"]["location"] or "mississippi" in tw["user"]["location"].lower()):
			sortEthnic(ms1bl, ms1bb, ms1bw, tw)
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
			sortEthnic(mo1bl, mo1bb, mo1bw, tw)	#done
		if(" MT" in tw["user"]["location"] or "montana" in tw["user"]["location"].lower()):
			sortEthnic(mt1bl, mt1bb, mt1bw, tw)	#done
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
			sortEthnic(ne1bl, ne1bb, ne1bw, tw)
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower()):
			sortEthnic(nv1bl, nv1bb, nv1bw, tw) #done
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
			sortEthnic(nh1bl, nh1bb, nh1bw, tw) #done
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
			sortEthnic(nj1bl, nj1bb, nj1bw, tw)	#done
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
			sortEthnic(nm1bl, nm1bb, nm1bw, tw)	#done
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
			sortEthnic(ny1bl, ny1bb, ny1bw, tw) #done
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
			sortEthnic(nc1bl, nc1bb, nc1bw, tw) #done
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
			sortEthnic(nd1bl, nd1bb, nd1bw, tw)
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
			sortEthnic(oh1bl, oh1bb, oh1bw, tw)
		if(" OK" in tw["user"]["location"] or "oklahoma" in tw["user"]["location"].lower()):
			sortEthnic(ok1bl, ok1bb, ok1bw, tw) #done
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
			sortEthnic(or1bl, or1bb, or1bw, tw) #done
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
			sortEthnic(pa1bl, pa1bb, pa1bw, tw)
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
			sortEthnic(ri1bl, ri1bb, ri1bw, tw)
		if(" SC" in tw["user"]["location"] or "south carolina" in tw["user"]["location"].lower()):
			sortEthnic(sc1bl, sc1bb, sc1bw, tw) #done
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
			sortEthnic(sd1bl, sd1bb, sd1bw, tw)
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
			sortEthnic(tn1bl, tn1bb, tn1bw, tw) #done
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
			sortEthnic(tx1bl, tx1bb, tx1bw, tw)
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
			sortEthnic(ut1bl, ut1bb, ut1bw, tw) #done
		if(" VT" in tw["user"]["location"] or "vermont" in tw["user"]["location"].lower()):
			sortEthnic(vt1bl, vt1bb, vt1bw, tw) #done
		if(" VA" in tw["user"]["location"] or ("virginia" in tw["user"]["location"].lower() and not "west virginia" in tw["user"]["location"].lower())):
			sortEthnic(va1bl, va1bb, va1bw, tw)
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
			sortEthnic(wa1bl, wa1bb, wa1bw, tw)
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
			sortEthnic(wv1bl, wv1bb, wv1bw, tw)
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
			sortEthnic(wi1bl, wi1bb, wi1bw, tw)
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
			sortEthnic(wy1bl, wy1bb, wy1bw, tw)


calcResult("Arizona", 759663, az1bl, az1bb, az1bw, az1tl, az1tb, az1tw, 0.4, 0.6, 0)
print("")
calcResult("Arkansas", 724622, ar1bl, ar1bb, ar1bw, ar1tl, ar1tb, ar1tw, 0.4, 0.6, 0)
print("")
calcResult("Alabama", 715346, al1bl, al1bb, al1bw, al1tl, al1tb, al1tw, 0.4, 0.6, 0)
print("")
calcResult("Colorado", 812843, co1bl, co1bb, co1bw, co1tl, co1tb, co1tw, 0.4, 0.6, 0)
print("")
calcResult("California", 704012, ca1bl, ca1bb, ca1bw, ca1tl, ca1tb, ca1tw, 0.4, 0.6, 0)
print("")
calcResult("Connecticut", 710509, ct1bl, ct1bb, ct1bw, ct1tl, ct1tb, ct1tw, 0.4, 0.6, 0)
print("")
calcResult("Georgia", 734172, ga1bl, ga1bb, ga1bw, ga1tl, ga1tb, ga1tw, 0.4, 0.6, 0)
print("")
calcResult("Florida", 762506, fl1bl, fl1bb, fl1bw, fl1tl, fl1tb, fl1tw, 0.4, 0.6, 0)
print("")
calcResult("Indiana", 714756, in1bl, in1bb, in1bw, in1tl, in1tb, in1tw, 0.4, 0.6, 0)
print("")
calcResult("Iowa", 773628, ia1bl, ia1bb, ia1bw, ia1tl, ia1tb, ia1tw, 0.4, 0.6, 0)
print("")
calcResult("Illinois", 706550, il1bl, il1bb, il1bw, il1tl, il1tb, il1tw, 0.4, 0.6, 0)
print("")
calcResult("Idaho", 912950, id1bl, id1bb, id1bw, id1tl, id1tb, id1tw, 0.4, 0.6, 0)
print("")
calcResult("Kansas", 725222, ks1bl, ks1bb, ks1bw, ks1tl, ks1tb, ks1tw, 0.4, 0.6, 0)
print("")
calcResult("Kentucky", 717739, ky1bl, ky1bb, ky1bw, ky1tl, ky1tb, ky1tw, 0.4, 0.6, 0)
print("")
calcResult("Louisiana", 803427, la1bl, la1bb, la1bw, la1tl, la1tb, la1tw, 0.4, 0.6, 0)
print("")
calcResult("Maine", 683279, me1bl, me1bb, me1bw, me1tl, me1tb, me1tw, 0.4, 0.6, 0)
print("")
calcResult("Maryland", 662062, md1bl, md1bb, md1bw, md1tl, md1tb, md1tw, 0.4, 0.6, 0)
print("")
calcResult("Massachusetts", 634479, ma1bl, ma1bb, ma1bw, ma1tl, ma1tb, ma1tw, 0.4, 0.6, 0)
print("")
calcResult("Michigan", 699621, mi1bl, mi1bb, mi1bw, mi1tl, mi1tb, mi1tw, 0.4, 0.6, 0)
print("")
calcResult("Mississippi", 762914, ms1bl, ms1bb, ms1bw, ms1tl, ms1tb, ms1tw, 0.4, 0.6, 0)
print("")
calcResult("Missouri", 728365, mo1bl, mo1bb, mo1bw, mo1tl, mo1tb, mo1tw, 0.4, 0.6, 0)
print("")
calcResult("Minnesota", 678418, mn1bl, mn1bb, mn1bw, mn1tl, mn1tb, mn1tw, 0.4, 0.6, 0)
print("")
calcResult("New Jersey", 729675, nj1bl, nj1bb, nj1bw, nj1tl, nj1tb, nj1tw, 0.4, 0.6, 0)
print("")
calcResult("New Mexico", 690571, nm1bl, nm1bb, nm1bw, nm1tl, nm1tb, nm1tw, 0.4, 0.6, 0)
print("")
calcResult("Nebraska", 616728, ne1bl, ne1bb, ne1bw, ne1tl, ne1tb, ne1tw, 0.4, 0.6, 0)
print("")
calcResult("New Hampshire", 673194, nh1bl, nh1bb, nh1bw, nh1tl, nh1tb, nh1tw, 0.4, 0.6, 0)
print("")
calcResult("Nevada", 722331, nv1bl, nv1bb, nv1bw, nv1tl, nv1tb, nv1tw, 0.4, 0.6, 0)
print("")
calcResult("North Carolina", 750278, nc1bl, nc1bb, nc1bw, nc1tl, nc1tb, nc1tw, 0.4, 0.6, 0)
print("")
calcResult("New York", 717707, ny1bl, ny1bb, ny1bw, ny1tl, ny1tb, ny1tw, 0.4, 0.6, 0)
print("")
calcResult("Ohio", 739216, oh1bl, oh1bb, oh1bw, oh1tl, oh1tb, oh1tw, 0.4, 0.6, 0)
print("")
calcResult("Oregon", 844175, or1bl, or1bb, or1bw, or1tl, or1tb, or1tw, 0.4, 0.6, 0)
print("")
calcResult("Oklahoma", 754310, ok1bl, ok1bb, ok1bw, ok1tl, ok1tb, ok1tw, 0.4, 0.6, 0)
print("")
calcResult("Hawaii", 692981, hi1bl, hi1bb, hi1bw, hi1tl, hi1tb, hi1tw, 0.4, 0.6, 0)
print("")
calcResult("South Carolina", 668668, sc1bl, sc1bb, sc1bw, sc1tl, sc1tb, sc1tw, 0.4, 0.6, 0)
print("")
calcResult("Texas", 717735, tx1bl, tx1bb, tx1bw, tx1tl, tx1tb, tx1tw, 0.4, 0.6, 0)
print("")
calcResult("Tennessee", 714504, tn1bl, tn1bb, tn1bw, tn1tl, tn1tb, tn1tw, 0.4, 0.6, 0)
print("")
calcResult("Pennsylvania", 655146, pa1bl, pa1bb, pa1bw, pa1tl, pa1tb, pa1tw, 0.4, 0.6, 0)
print("")
calcResult("Rhode Island", 539250, ri1bl, ri1bb, ri1bw, ri1tl, ri1tb, ri1tw, 0.4, 0.6, 0 )
print("")
calcResult("Utah", 100000, ut1bl, ut1bb, ut1bw, ut1tl, ut1tb, ut1tw, 0.4, 0.6, 0)
print("")
calcResult("Virginia", 776836, va1bl, va1bb, va1bw, va1tl, va1tb, va1tw, 0.4, 0.6, 0)
print("")
calcResult("Washington", 654904, wa1bl, wa1bb, wa1bw, wa1tl, wa1tb, wa1tw, 0.4, 0.6, 0)
print("")
calcResult("West Virginia", 615991, wv1bl, wv1bb, wv1bw, wv1tl, wv1tb, wv1tw, 0.4, 0.6, 0)
print("")
calcResult("Wisconsin", 717716, wi1bl, wi1bb, wi1bw, wi1tl, wi1tb, wi1tw, 0.4, 0.6, 0)
print("")
calcResult("DELAWARE", 973764, de1bl, de1bb, de1bw, de1tl, de1tb, de1tw, 0.4, 0.6, 0)
print("")
calcResult("NORTH DAKOTA", 762062, nd1bl, nd1bb, nd1bw, nd1tl, nd1tb, nd1tw, 0.4, 0.6, 0)
print("")
calcResult("SOUTH DAKOTA", 884659, sd1bl, sd1bb, sd1bw, sd1tl, sd1tb, sd1tw, 0.4, 0.6, 0)
print("")
calcResult("MONTANA", 1068778, mt1bl, mt1bb, mt1bw, mt1tl, mt1tb, mt1tw, 0.4, 0.6, 0)
print("")
calcResult("WYOMING", 578759, wy1bl, wy1bb, wy1bw, wy1tl, wy1tb, wy1tw, 0.4, 0.6, 0)
print("")
calcResult("ALASKA", 731545, ak1bl, ak1bb, ak1bw, ak1tl, ak1tb, ak1tw, 0.4, 0.6, 0)
print("")
calcResult("VERMONT", 623989, vt1bl, vt1bb, vt1bw, vt1tl, vt1tb, vt1tw, 0.4, 0.6, 0)


for str in results:
	print(str)
	print("")

print("")
print("Trump districts: ", trumpdistricts)
print("Biden districts: ", bidendistricts )


with open("/Volumes/TOSHIBA_BACKUP/usastateswithgender.txt", 'wb') as f:
	pickle.dump([al1tl, al1tb, al1tw, al1bl, al1bb, al1bw, ak1tl, ak1tb, ak1tw, ak1bl, ak1bb, ak1bw, az1tl, az1tb, az1tw, az1bl, az1bb, az1bw, ar1bl, ar1bb, ar1bw, ar1tl, ar1tb, ar1tw, ak1bl, ak1bb, ak1bw, ca1tl, ca1tb, ca1tw, ca1bl, ca1bb, ca1bw, co1tl, co1tb, co1tw, co1bl, co1bb, co1bw, ct1bl, ct1bb, ct1bw, ct1tl, ct1tb, ct1tw, de1tl, de1tb, de1tw, de1bl, de1bb, de1bw, fl1bl, fl1bb, fl1bw, fl1tl, fl1tb, fl1tw, ga1tl, ga1tb, ga1tw, ga1bl, ga1bb, ga1bw, hi1tl, hi1tb, hi1tw, hi1bl, hi1bb, hi1bw, id1tl, id1tb, id1tw, id1bl, id1bb, id1bw, il1bl, il1bb, il1bw, il1tl, il1tb, il1tw, in1tl, in1tb, in1tw, in1bl, in1bb, in1bw, ia1tl, ia1tb, ia1tw, ia1bl, ia1bb, ia1bw, ks1tl, ks1tb, ks1tw, ks1bl, ks1bb, ks1bw, ky1tl, ky1tb, ky1tw, ky1bl, ky1bb, ky1bw, la1tl, la1tb, la1tw, la1bl, la1bb, la1bw, me1tl, me1tb, me1tw, me1bl, me1bb, me1bw, md1tl, md1tb, md1tw, md1bl, md1bb, md1bw, ma1tl, ma1tb, ma1tw, ma1bl, ma1bb, ma1bw, mi1bl, mi1bb, mi1bw, mi1tl, mi1tb, mi1tw, mn1tl, mn1tb, mn1tw, mn1bl, mn1bb, mn1bw, ms1tl, ms1tb, ms1tw, ms1bl, ms1bb, ms1bw, mo1tl, mo1tb, mo1tw, mo1bl, mo1bb, mo1bw, mt1tl, mt1tb, mt1tw, mt1bl, mt1bb, mt1bw, ne1tl, ne1tb, ne1tw, ne1bl, ne1bb, ne1bw, nv1tl, nv1tb, nv1tw, nv1bl, nv1bb, nv1bw, nh1tl, nh1tb, nh1tw, nh1bl, nh1bb, nh1bw, nj1bl, nj1bb, nj1bw, nj1tl, nj1tb, nj1tw, nm1tl, nm1tb, nm1tw, nm1bl, nm1bb, nm1bw, ny1tl, ny1tb, ny1tw, ny1bl, ny1bb, ny1bw, nc1bl, nc1bb, nc1bw, nc1tl, nc1tb, nc1tw, nd1tl, nd1tb, nd1tw, nd1bl, nd1bb, nd1bw, oh1bl, oh1bb, oh1bw, oh1tl, oh1tb, oh1tw, ok1tl, ok1tb, ok1tw, ok1bl, ok1bb, ok1bw, or1tl, or1tb, or1tw, or1bl, or1bb, or1bw, pa1bl, pa1bb, pa1bw, pa1tl, pa1tb, pa1tw, ri1tl, ri1tb, ri1tw, ri1bl, ri1bb, ri1bw, sc1tl, sc1tb, sc1tw, sc1bl, sc1bb, sc1bw, sd1tl, sd1tb, sd1tw, sd1bl, sd1bb, sd1bw, tn1tl, tn1tb, tn1tw, tn1bl, tn1bb, tn1bw, tx1tl, tx1tb, tx1tw, tx1bl, tx1bb, tx1bw, ut1tl, ut1tb, ut1tw, ut1bl, ut1bb, ut1bw, vt1tl, vt1tb, vt1tw, vt1bl, vt1bb, vt1bw, va1bl, va1bb, va1bw, va1tl, va1tb, va1tw, wa1bl, wa1bb, wa1bw, wa1tl, wa1tb, wa1tw, wv1tl, wv1tb, wv1tw, wv1bl, wv1bb, wv1bw, wi1tl, wi1tb, wi1tw, wi1bl, wi1bb, wi1bw, wy1tl, wy1tb, wy1tw, wy1bl, wy1bb, wy1bw], f)


