import tensorflow as tf
import numpy as np

model = None
output_class = [ "Black-grass", "Charlock", "Cleavers", "Common Chickweed", "Common wheat",
    "Fat Hen", "Loose Silky-bent", "Maize", "Scentless Mayweed", "Shepherd’s Purse",
    "Small-flowered Cranesbill", "Sugar beet"]
data = {
"Black-grass":
	["Black Grass, also known as Ophiopogon planiscapus, is a unique and visually striking perennial grass species. It is native to Japan and belongs to the Asparagaceae family.<br><br><br><strong>Some intruiging Facts: </strong><br><br>Appearance: Black Grass is characterized by its dark, almost black, strappy leaves that provide a dramatic contrast in garden landscapes.<br>"
    "1. Growth Habit: It typically forms clumps and has a low-growing habit, making it an excellent ground cover in both sun and shade.<br><br>"
    "2. Flowering: In summer, small spikes of light pink or white flowers emerge, adding an interesting vertical element to its appearance.<br><br>"
    "3. Adaptability: Black Grass is known for its adaptability to various soil types and is relatively low-maintenance, making it a popular choice for ornamental gardening.<br><br>",
	"GK5v0Zg_JYs?si", "voBBxae_N-s?si"],
 "Charlock":
	["Charlock, scientifically known as Sinapis arvensis, is an annual or winter annual plant that belongs to the Brassicaceae family. It is commonly found in agricultural fields, gardens, and disturbed areas.<br><br><br><strong>Some intruiging Facts:</strong><br><br>• Donate gently-used clothing to local charities or thrift stores for reuse.<br><br>"
    "1.Identification: Charlock is characterized by its bright yellow flowers with four petals and can grow up to three feet tall. Its leaves are typically lobed and have a rough texture.<br><br>"
    "2. Habitat: This plant is often considered a weed and can thrive in a variety of environments, including cultivated fields, roadsides, and waste areas.<br><br>"
    "3. Flowering Season: Charlock blooms in late spring and early summer, producing clusters of yellow flowers that attract pollinators like bees and butterflies.<br><br>",
	"ep7ebWkXTfI?si", "qIpQbSjBv3A?si"],
"Cleavers":
	["Cleavers, scientifically known as Galium aparine, is an herbaceous annual plant belonging to the Rubiaceae family. It is commonly found in hedgerows, woodlands, and disturbed areas and is known for its clinging or sticky nature.<br><br><br><strong>Some intruiging Facts:</strong><br><br>•Take old electronics to authorized e-waste recycling centers or events.<br><br>"
    "1. Characteristics: Cleavers are easily identifiable by their whorls of narrow leaves and tiny, star-shaped white flowers. <br><br>"
    "2.Habitat: This plant is versatile and can thrive in a variety of environments, including gardens, fields, and along waterways. It often grows as a climbing or sprawling vine.<br><br>"
    "3.Traditional Uses: Cleavers have a history of medicinal use in various cultures. Traditionally, it has been used for its diuretic properties and as a mild lymphatic tonic. Some herbalists also use it in skin care preparations.<br><br>",
	"PTcrBvCJa44?si","8kir6b-8lyE?si"],
"Common Chickweed":
	["Common Chickweed, scientifically known as Stellaria media, is a cool-season annual plant belonging to the Caryophyllaceae family. It is a common and widespread weed found in gardens, lawns, and other disturbed areas.<br><br><br><strong>Some intruiging Facts:</strong><br><br>• Separate glass bottles and jars from other recyclables to ensure proper recycling.<br><br>"
    "1. Appearance: Common Chickweed has small, oval leaves arranged in opposite pairs along the stems.<br><br>"
    "2. Habitat: This weed thrives in moist and shady conditions but can adapt to a variety of environments, including lawns, gardens, and agricultural fields.<br><br>"
    "3. Edible Qualities: Despite being considered a weed, Common Chickweed is edible and has a mild flavor. It is rich in vitamins and minerals and can be used in salads, soups, or as a cooked green.<br><br>",
	"rHjgodRFpyg?si", "Rk6MFMEk-9Y?si"],
"Common wheat":
	["Belonging to the Triticum genus, common wheat (Triticum aestivum) is a major cereal grain. It's a staple food globally, known for its versatile uses.<br><br><br><strong>Some intruiging Facts:</strong><br><br>• Dispose of compact fluorescent lamps (CFLs) and fluorescent tubes at designated hazardous waste collection sites.<br><br>"
    "1. Staple Crop: Common wheat is a primary staple crop, providing a significant portion of the world's daily caloric intake.<br><br>"
    "2. Varieties: There are various varieties of common wheat, including hard and soft wheats, each suited for different culinary applications.<br><br>"
    "3. Gluten Content: Common wheat contains gluten, making it suitable for bread and pasta production but unsuitable for those with gluten-related disorders.<br><br>",
	"KsQiWRy4EfM?si", "iKw-ds4H4qQ?si"],
"Fat Hen":
	["Fat Hen, or Chenopodium album, is an annual weed with triangular leaves and white, small flowers. Found globally, it's edible and has historical medicinal uses.<br><br><br><strong>Some intruiging Facts:</strong><br><br>• Separate metal items such as aluminum cans and steel containers from your regular waste for recycling.<br><br>"
    "1. Edible Weed: Fat Hen is edible, and its leaves are consumed in various cultures, often cooked or used in salads.<br><br>"
    "2. Widespread Distribution: This weed is widespread, thriving in disturbed areas, gardens, and agricultural fields across different continents.<br><br>"
    "3. Historical Uses: Fat Hen has historical medicinal uses in traditional herbal medicine for ailments such as digestive issues and skin conditions.<br><br>",
	"nvDWEak7Pjk?si", "j4EDXIUh98w?si"],
"Loose Silky-bent":
	["Silky grass varieties are often used in landscaping to add a touch of elegance to gardens, borders, or decorative plantings.<br><br><br><strong>Some intruiging Facts:</strong><br><br>• Compost kitchen scraps like fruit and vegetable peels, coffee grounds, and eggshells in a backyard compost bin or pile.<br><br>"
    "1. Texture: This grass type typically has soft and silky leaves or blades.<br><br>"
    "2. Characteristics: It might exhibit a fine texture and a graceful appearance, making it suitable for ornamental purposes.<br><br>"
    "3. Common Uses: Soft and silky grasses are often used in landscaping to add a delicate and attractive element to gardens, lawns, or decorative plantings.<br><br>",
	"Kj6aCu-wSwo?si", "PotCA_QEB0k?si"],
 "Maize":
	["Maize, known as corn in North America, is a cereal grain that belongs to the grass family Poaceae. <br><br><br><strong>Some intruiging Facts:</strong><br><br>• Separate paper and cardboard materials from your regular trash for recycling.<br><br>"
    "1. Origin: Maize originated in the Americas and has been a staple food for various cultures for thousands of years.<br><br>"
    "2. Cultivation: It is a widely cultivated crop with varieties adapted to different climates and growing conditions. Maize is grown on every continent except Antarctica.<br><br>"
    "3. Uses: In addition to being a major food crop, maize is used in various products such as cornmeal, corn syrup, and biofuels. It is also a crucial feed for livestock.<br><br>",
	"RW_GpNciIuA?si", "d3GF1h1WLLc?si"],
"Scentless Mayweed":
	["Scentless mayweed, scientifically known as Tripleurospermum inodorum, is an annual plant in the Asteraceae family. <br><br><br><strong>Some intruiging Facts:</strong><br><br> • Sort plastic containers and packaging by their recycling codes, and place them in the appropriate recycling bins.<br><br>"
    "1. Appearance: Scentless mayweed features finely divided leaves and small, daisy-like flowers with white petals and yellow centers.<br><br>"
    "2. Habitat: Commonly found in disturbed areas, such as roadsides, fields, and waste places, scentless mayweed is adaptable to various soil types.<br><br>"
    "3. Scent: Unlike its relative, mayweed chamomile, scentless mayweed lives up to its name by lacking the strong, characteristic odor.<br><br>",
	"9Igrf-1lG_c?si", "ZdB9J5NEN94?si"],
      
       "Shepherd's Purse":
	["Shepherd's purse, scientifically known as Capsella bursa-pastoris, is an annual and winter annual weed that belongs to the Brassicaceae family.<br><br><br><strong>Some intruiging Facts:</strong><br><br> • Sort plastic containers and packaging by their recycling codes, and place them in the appropriate recycling bins.<br><br>"
    "1. Leaf Shape: Identified by its distinctive heart-shaped or triangular seed pods, resembling a purse, hence the name. The leaves are deeply lobed and often toothed.<br><br>"
    "2. Habitat: Commonly found in disturbed areas, gardens, fields, and along roadsides. It's highly adaptable and can thrive in various soil types.<br><br>"
    "3. Flowers: Small, white flowers with four petals that form in clusters at the top of the stems. Blooms from late winter to early autumn.<br><br>",
	"gq7u9IhCTDA?si", "d5UNyGahR88?si"],
      
      "Small-flowered Cranesbill":
	["Small-flowered cranesbill, scientifically known as Geranium pusillum, is a perennial herbaceous plant belonging to the Geraniaceae family.<br><br><br><strong>Some intruiging Facts:</strong><br><br> • Sort plastic containers and packaging by their recycling codes, and place them in the appropriate recycling bins.<br><br>"
    "1. Flowers: Small, pale pink to purple flowers with five petals, appearing from spring to early autumn. The flowers are typically 1 to 1.5 cm in diameter.<br><br>"
    "2. Leaves: The deeply lobed leaves are often palmate in shape, and the plant forms a low-growing, spreading habit.<br><br>"
    "3. Habitat: Commonly found in meadows, woodland edges, and grassy areas, small-flowered cranesbill is adaptable to various soil types.<br><br>",
	"t8xGc3nXSTY?si", "PotCA_QEB0k?si"],
      
      "Sugar beet":
	["Sugar beet, scientifically known as Beta vulgaris var. altissima, is a biennial plant cultivated for its high sugar content. <br><br><br><strong>Some intruiging Facts:</strong><br><br> • Sort plastic containers and packaging by their recycling codes, and place them in the appropriate recycling bins.<br><br>"
    "1. Root Crop: Sugar beet is primarily grown for its large, fleshy roots, which contain a high concentration of sucrose used in sugar production.<br><br>"
    "2. Appearance: The plant has a rosette of large, dark green leaves, and the edible, sugar-storing taproot is the main harvested part.<br><br>"
    "3. Sugar Extraction: The sugar is extracted from the beet's root through a process that involves slicing, diffusion, and crystallization.<br><br>",
	"i7GohHBMQwc?si", "bflT892Kchs?si"],
      
}


def load_artifacts():
    global model
    model = tf.keras.models.load_model("plantSeedlings.h5" , compile = False)
   

def classify_seedling(image_path):
	global model, output_class
	test_image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
	test_image = tf.keras.preprocessing.image.img_to_array(test_image) / 255
	test_image = np.expand_dims(test_image, axis = 0)
	predicted_array = model.predict(test_image)
	predicted_value = output_class[np.argmax(predicted_array)]
	return predicted_value, data[predicted_value][0], data[predicted_value][1], data[predicted_value][2]

