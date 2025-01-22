import tensorflow as tf
import numpy as np

from newsapi import NewsApiClient





model = None
output_class = [ "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)__Common_rust",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape__Esca(Black_Measles)",
    "Grape__Leaf_blight(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange__Haunglongbing(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,bell__Bacterial_spot",
    "Pepper,bell__healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"]





data = {
    "Apple___Apple_scab":
	["Apple scab, caused by the fungus Venturia inaequalis, is a common and potentially serious disease that affects apple trees.<br><br><br><strong>What can we do ?</strong><br><br>• Timing: Apply fungicides preventatively, especially during critical periods of growth. Early-season treatments are essential.<br>"
    "• Fungicide Selection: Consult with local agricultural extension services for recommendations on effective fungicides. Copper-based fungicides are commonly used for Apple Scab control.<br><br>"
    "• Rotating Fungicides: Rotate between different fungicides to minimize the risk of resistance development.<br><br>"
    "• Plant Resistant Cultivars: Choose apple varieties that are known to be resistant or less susceptible to Apple Scab. Resistant cultivars can significantly reduce the need for chemical treatments.<br><br>",
	"vk2jm3aMa2Q?si", "HsYIIzZhRic?si"],
"Apple___Black_rot":
	["Black Rot is a fungal disease that commonly affects apple trees, caused by the pathogen Botryosphaeria obtusa. Here are strategies to manage and prevent Black Rot in apple orchards.<br><br><br><strong>What can we do ?</strong><br><br>• Timing: Apply fungicides preventatively during critical growth stages, especially during the blossom and fruit development periods.<br><br>"
    "• Fungicide Selection: Use fungicides recommended for Black Rot control. Copper-based fungicides and those containing active ingredients like myclobutanil or pyraclostrobin may be effective.<br><br>"
    "• Regular Applications: Follow a regular spray schedule based on the recommendations of local agricultural extension services.<br><br>"
    "• Pruning: Prune apple trees to improve air circulation and light penetration, reducing humidity and creating an environment less favorable for the fungus.<br><br>",
	"OLfYtg8Qugs?si", "oTtz_qDCG5Y?si"],
"Apple___Cedar_apple_rust":
	["Cedar Apple Rust is a fungal disease caused by the pathogen Gymnosporangium juniperi-virginianae. It affects apple and other fruit trees, as well as certain juniper species.<br><br><br><strong>What can we do ?</strong><br><br>•Timing: Apply fungicides preventatively during critical periods of growth, especially during the spring when the rust spores are released.<br><br>"
    "• Fungicide Selection: Use fungicides specifically recommended for Cedar Apple Rust control. Copper-based fungicides and those containing active ingredients like myclobutanil or triadimefon may be effective.<br><br>"
    "• Regular Applications: Follow a regular spray schedule based on the recommendations of local agricultural extension services.<br><br>"
    "• Remove Alternate Hosts: Cedar Apple Rust requires both apple trees and certain juniper species as hosts. If possible, remove nearby juniper trees or manage them to reduce the spread of spores.<br><br>",
	"ynCBHri2zDk?si","ZMLCdmsm_7E?si"],
"Apple___healthy":
	["A healthy apple tree exhibits several characteristics that indicate its overall well-being and optimal growth.<br><br><br><strong>What can we do ?</strong><br><br>• Vibrant Foliage: Healthy apple trees have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Trunk and Branches: The trunk and branches of a healthy apple tree are sturdy and well-formed, providing structural support for the entire tree.<br><br>"
    "• Uniform Growth: Healthy trees show uniform growth with well-distributed branches. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy apple trees produce abundant flowers during the blooming season. The presence of flowers is crucial for the development of fruit.<br><br>",
	"2qmwr_sXqMY?si", "TGSrby6DmJM?si"],
"Blueberry___healthy":
	["A healthy blueberry plant exhibits several characteristics that indicate its overall well-being and optimal growth. <br><br><br><strong>What can we do ?</strong><br><br>• Vibrant Foliage: Healthy blueberry plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Stems and Branches: The stems and branches of a healthy blueberry plant are sturdy and well-formed, providing structural support for the entire plant.<br><br>"
    "• Uniform Growth: Healthy plants show uniform growth with well-distributed branches. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy blueberry plants produce abundant flowers during the blooming season. The presence of flowers is crucial for the development of fruit.<br><br>",
	"dte4yLhvO0Q?si", "5tOVmMb6P08?si"],
"Cherry_(including_sour)___Powdery_mildew":
	["Powdery mildew is a common fungal disease that can affect cherry trees, including sour cherry varieties.<br><br><br><strong>What can we do ?</strong><br><br>• Timing: Apply fungicides preventatively, especially during periods of active growth and when conditions are favorable for powdery mildew development.<br><br>"
    "• Fungicide Selection: Choose fungicides specifically formulated for controlling powdery mildew on cherry trees. Fungicides containing sulfur, neem oil, or other fungicidal active ingredients may be effective.<br><br>"
    "• Regular Applications: Follow a regular spray schedule based on the recommendations of local agricultural extension services.<br><br>"
    "• Pruning: Prune cherry trees to improve air circulation and light penetration, reducing humidity and creating an environment less favorable for powdery mildew.<br><br>",
	"4GYpcXncLCg?si", "A_xsjZ139g4?si"],
"Cherry_(including_sour)___healthy":
	["A healthy cherry tree, including sour cherry varieties, exhibits several characteristics that indicate overall well-being and optimal growth. <br><br><br><strong>What can we do ?</strong><br><br>• Vibrant Foliage: Healthy cherry trees have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Trunk and Branches: The trunk and branches of a healthy cherry tree are sturdy and well-formed, providing structural support for the entire tree.<br><br>"
    "•Uniform Growth: Healthy trees show uniform growth with well-distributed branches. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy cherry trees produce abundant flowers during the blooming season. The presence of flowers is crucial for the development of fruit.<br><br>",
	"nuZUMsnbEeo?si", "JJ2QsU5cC14?si"],
"Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":
	["Cercospora leaf spot and gray leaf spot are two distinct foliar diseases that can affect corn (maize) crops. <br><br><br><strong>What can we do ?</strong><br><br>• Symptoms: Cercospora leaf spot appears as small, oval to elongated lesions with a tan center and dark brown to purple borders. These lesions may coalesce, forming larger spots. The disease often starts in the lower canopy and progresses upward.<br><br>"
    "• Favorable Conditions: Warm and humid weather, along with prolonged periods of leaf wetness, create favorable conditions for Cercospora leaf spot.<br><br>"
    "•Fungicides: Application of fungicides, especially those containing triazoles, may be effective when applied preventatively or at the early stages of the disease.<br><br>"
    "• Crop Rotation: Crop rotation can help reduce the inoculum in the soil.<br><br>",
	"7kLHlbFhTDU?si", "107Xz8HslXM?si"],
"Corn_(maize)__Common_rust":
	["Common rust, caused by the fungus Puccinia sorghi, is a foliar disease that can affect corn (maize) crops. <br><br><br><strong>What can we do ?</strong><br><br> • Rusty Pustules: Common rust appears as small, round to elongated, reddish-brown to orange pustules on the upper and lower surfaces of leaves.<br><br>"
    "• Spore Production: These pustules contain masses of rust-colored spores that can be easily rubbed off.<br><br>"
    "• Moisture and Moderate Temperatures: Common rust tends to develop and spread in conditions of moderate temperatures (between 60°F to 77°F or 15°C to 25°C) and high humidity.<br><br>"
    "• Resistant Varieties: Planting corn hybrids that are resistant to common rust is a key strategy. Resistant varieties can significantly reduce the severity of the disease.<br><br>",
	"KUXGyLtu84Q?si", "YXsCA59qTDc?si"],
"Corn_(maize)___Northern_Leaf_Blight":
	["Northern leaf blight, caused by the fungus Setosphaeria turcica (formerly known as Exserohilum turcicum), is a common foliar disease that affects corn (maize) crops. <br><br><br><strong>What can we do ?</strong><br><br> • Lesions: Northern leaf blight lesions are typically long, elliptical, and cigar-shaped with tan to gray centers and dark brown to reddish-brown borders.<br><br>"
    "•Lesion Distribution: Lesions often appear linear along the length of the leaf, and severe infections can lead to extensive damage.<br><br>"
    "• Warm and Humid Weather: Northern leaf blight thrives in warm and humid conditions. Moderate temperatures between 68°F to 77°F (20°C to 25°C) are conducive to disease development.<br><br>"
    "• Resistant Varieties: Planting corn hybrids with genetic resistance to Northern leaf blight is a key strategy. Resistant varieties can significantly reduce the severity of the disease.<br><br>",
	"OmoAjymdVi4?si", "0-iNHLa4Q5c?si"],
"Corn_(maize)___healthy":
	["A healthy corn (maize) plant exhibits several characteristics that indicate overall well-being and optimal growth.<br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy corn plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Stems: The stems of a healthy corn plant are sturdy and able to support the weight of the plant.<br><br>"
    "• Uniform Growth: Healthy corn plants show uniform growth with well-developed leaves arranged in a spiral pattern around the stem.<br><br>"
    "• Tassel and Silks: A healthy corn plant develops a tassel at the top, which is the male reproductive structure. Silks emerge from ears, the female reproductive structures, and are a sign of healthy pollination.<br><br>",
	"qk1y_mnym2g?si", "5kGa9Bo7ILY?si"],
"Grape___Black_rot":
	["Black rot is a common and destructive fungal disease that affects grapevines. It is caused by the fungus Guignardia bidwellii.<br><br><br><strong>What can we do ?</strong><br><br> • Timing: Apply fungicides preventatively during critical growth stages, such as bud break, bloom, and post-bloom.<br><br>"
    "•Fungicide Selection: Use fungicides specifically recommended for black rot control. Common fungicides include those containing active ingredients such as captan, mancozeb, or strobilurins.<br><br>"
    "•Regular Applications: Follow a regular spray schedule based on the recommendations of local agricultural extension services.<br><br>"
    "• Pruning: Prune grapevines to improve air circulation and sunlight penetration, reducing humidity and creating an environment less favorable for the fungus.<br><br>",
	"hguN_6cHDls?si", "R38gR9OaE4Q?si"],
"Grape__Esca(Black_Measles)":
	["Esca, often referred to as Black Measles, is a complex grapevine disease that affects the wood and leaves of grapevines. It is caused by multiple fungi, including Phaeoacremonium spp., Phaeomoniella chlamydospora, and Fomitiporia mediterranea.<br><br><br><strong>What can we do ?</strong><br><br> • Pruning: Prune grapevines carefully, and promptly remove and destroy any wood showing symptoms of Esca, including black streaking in the wood.<br><br>"
    "• Sterilize Pruning Tools: Disinfect pruning tools between cuts and after working on infected vines to prevent the spread of the disease.<br><br>"
    "• Plant Resistant Cultivars: Consider planting grape varieties that are known to be less susceptible to Esca. Resistant cultivars can help reduce the severity of the disease.<br><br>"
    "• Minimize Wounding: Avoid unnecessary wounding of grapevines, as wounds provide entry points for the pathogens associated with Esca.<br><br>",
	"YrEvq_jXiWE?si", "3SRMRi_7WUM?si"],
"Grape__Leaf_blight(Isariopsis_Leaf_Spot)":
	["Isariopsis Leaf Spot, caused by the fungus Isariopsis griseola, is a fungal disease that primarily affects the leaves of grapevines. <br><br><br><strong>What can we do ?</strong><br><br>• Timing: Apply fungicides preventatively during critical periods of growth, such as during the growing season when conditions are favorable for disease development.<br><br>"
    "• Fungicide Selection: Use fungicides specifically recommended for Isariopsis Leaf Spot control. Copper-based fungicides or those containing other active ingredients effective against the pathogen may be used.<br><br>"
    "• Regular Applications: Follow a regular spray schedule based on the recommendations of local agricultural extension services.<br><br>"
    "• Pruning: Prune grapevines to improve air circulation and sunlight penetration, reducing humidity and creating an environment less favorable for the fungus.<br><br>",
	"agIwEBm7Zao?si", "2Wq8TKBXJWY?si"],
"Grape___healthy":
	["A healthy grapevine exhibits several characteristics that indicate overall well-being and optimal growth. <br><br><br><strong>What can we do ?</strong><br><br>• Vibrant Foliage: Healthy grapevines have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Trunk and Canes: The trunk and canes of a healthy grapevine are sturdy and well-formed, providing structural support for the entire plant.<br><br>"
    "•Uniform Growth: Healthy vines show uniform growth with well-distributed shoots and canes. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy grapevines produce abundant flowers during the blooming season. The presence of flowers is crucial for the development of fruit.<br><br>",
	"YrEvq_jXiWE?si", "WVk21qyDeFw?si"],
"Orange__Haunglongbing(Citrus_greening)":
	["Huanglongbing (HLB), also known as citrus greening, is a devastating citrus disease caused by the bacterium Candidatus Liberibacter asiaticus. This disease affects citrus trees, including oranges, and is transmitted by the Asian citrus psyllid (Diaphorina citri)<br><br><br><strong>What can we do ?</strong><br><br> • Insecticide Applications: Implement regular insecticide applications to control the population of the Asian citrus psyllid, the vector of the HLB bacterium.<br><br>"
    "• Early Detection: Monitor for the presence of psyllids and treat early to prevent the spread of the disease.<br><br>"
    "• Use Certified Plants: Source citrus plants only from certified nurseries that adhere to disease-free practices.<br><br>"
    "• Quarantine Measures: Implement quarantine measures to prevent the introduction of infected plants into new areas.<br><br>",
	"W5mg3lv9sTI?si", "vbaei--w7gc?si"],
"Peach___Bacterial_spot":
	["Bacterial spot is a common and damaging bacterial disease affecting peach trees. It is caused by the bacterium Xanthomonas arboricola pv. pruni. <br><br><br><strong>What can we do ?</strong><br><br> • Bactericides: Copper-based sprays, such as copper hydroxide or copper sulfate, are commonly used as bactericides. These sprays can help manage bacterial spot when applied preventatively.<br><br>"
    "•Copper + Fungicide Combinations: Some fungicides with copper compounds may have additional benefits in managing bacterial spot. Consult with local extension services for specific recommendations.<br><br>"
    "•Early Spring: Begin sprays in early spring before bud break to protect emerging leaves and blossoms.<br><br>"
    "•Regular Schedule: Follow a regular spray schedule throughout the growing season, especially during periods of warm and wet weather favorable for bacterial spot development.<br><br>",
	"4NNwYY9XHcg?si", "BrCtisN_xVQ?si"],
"Peach___healthy":
	["A healthy peach tree exhibits several characteristics that indicate overall well-being and optimal growth.<br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy peach trees have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "•Sturdy Trunk and Branches: The trunk and major branches of a healthy peach tree are sturdy and well-formed, providing structural support for the entire tree.<br><br>"
    "• Uniform Growth: Healthy peach trees show uniform growth with well-distributed branches and shoots. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy peach trees produce abundant blossoms during the blooming season. The presence of flowers is crucial for the development of fruit.<br><br>",
	"LwDmsd-nOrg?si", "BrCtisN_xVQ?si"],
"Pepper,bell__Bacterial_spot":
	["Bacterial spot is a common bacterial disease affecting pepper plants, including bell peppers. It is caused by the bacterium Xanthomonas campestris pv. vesicatoria.<br><br><br><strong>What can we do ?</strong><br><br> • Copper Compounds: Copper-based sprays, such as copper hydroxide or copper sulfate, are commonly used as bactericides. These can help manage bacterial spot when applied preventatively.<br><br>"
    "• Copper + Fungicide Combinations: Some fungicides containing copper compounds may have additional benefits in managing bacterial spot. Consult with local extension services for specific recommendations.<br><br>"
    "• Early Treatment: Begin sprays early in the growing season, especially during periods of warm and humid weather when bacterial spot is more likely to develop.<br><br>"
    "•Regular Schedule: Follow a regular spray schedule throughout the growing season, especially during periods of high risk.<br><br>",
	"fRhQsWX1SL4?si", "vTcPoDX0i5k?si"],
"Pepper,bell__healthy":
	["A healthy bell pepper plant exhibits several characteristics that indicate overall well-being and optimal growth.<br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy bell pepper plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Stems and Branches: The stems and branches of a healthy bell pepper plant are sturdy and able to support the weight of the plant and fruit.<br><br>"
    "• Uniform Growth: Healthy plants show uniform growth with well-distributed branches and leaves. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy bell pepper plants produce abundant flowers, which are essential for the development of fruit.<br><br>",
	"ktmlMk9AhLg?si", "LFPqVu6Hhwc?si"],
"Potato___Early_blight":
	["Early blight is a common fungal disease that affects potato plants. It is caused by the fungus Alternaria solani.<br><br><br><strong>What can we do ?</strong><br><br>• Copper-based Fungicides: Copper-based fungicides can help manage early blight when applied preventatively.<br><br>"
    "• Mancozeb or Chlorothalonil: Fungicides containing mancozeb or chlorothalonil are effective against early blight. Apply according to the recommended schedule and dosage.<br><br>"
    "• Early Season Treatment: Begin fungicide applications early in the growing season, especially during periods of warm and humid weather that favor disease development.<br><br>"
    "•Regular Applications: Follow a regular spray schedule based on the recommendations of local agricultural extension services.<br><br>",
	"EVP4YTTRTjc?si", "scK2Jk0J4c?si"],
"Potato___Late_blight":
	["Late blight is a destructive fungal disease that affects potatoes and other plants in the Solanaceae family. It is caused by the oomycete pathogen Phytophthora infestans. <br><br><br><strong>What can we do ?</strong><br><br>• Leaf Lesions: Late blight symptoms often start with dark, water-soaked lesions on the leaves, usually surrounded by a pale halo.<br><br>"
    "•Rapid Spreading: The lesions can quickly expand, and affected areas may appear brown or black, giving the foliage a burned or scorched appearance.<br><br>"
    "• White Fungal Growth: Under humid conditions, a fuzzy, white fungal growth may be visible on the undersides of leaves and on affected stems.<br><br>"
    "•Tubers: Late blight can also infect potato tubers, causing dark, firm lesions that may lead to rotting during storage.<br><br>",
	"LndNbmlfrLs?si", "9SizVOPRpQc?si"],
"Potato___healthy":
	["A healthy potato plant exhibits several characteristics that indicate overall well-being and optimal growth. <br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy potato plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Stems and Upright Growth: The stems of a healthy potato plant are sturdy, and the plant exhibits upright growth. This indicates good structural integrity.<br><br>"
    "• Uniform Growth: Healthy plants show uniform growth with well-distributed leaves and stems. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy potato plants produce abundant flowers, which are essential for the formation of tubers.<br><br>",
	"1CoYHrz371o?si", "4f7b7_ND9eQ?si"],
"Raspberry___healthy":
	["A healthy raspberry plant exhibits several characteristics that indicate overall well-being and optimal growth. <br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy raspberry plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Canes: The canes of a healthy raspberry plant are sturdy and upright, providing structural support for the plant.<br><br>"
    "• Uniform Growth: Healthy plants show uniform growth with well-distributed canes and leaves. There should be no signs of stunted or distorted growth.<br><br>"
    "• Abundant Flowering: Healthy raspberry plants produce abundant flowers during the blooming season. The presence of flowers is crucial for the development of fruit.<br><br>",
	"PAPzJE__m3A?si", "wK0MKROrS1c?si"],
"Soybean___healthy":
	["A healthy soybean plant exhibits several characteristics that indicate overall well-being and optimal growth.<br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy soybean plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Stems: The stems of a healthy soybean plant are sturdy and upright, providing structural support for the plant.<br><br>"
    "• Uniform Growth: Healthy plants show uniform growth with well-distributed stems and leaves. There should be no signs of stunted or distorted growth.<br><br>"
    "•Abundant Leaf Canopy: A healthy soybean plant develops a full and abundant leaf canopy, optimizing photosynthesis for robust growth.<br><br>",
	"M0FWNAEYw10?si", "l5uogKpbuyc?si"],
"Squash___Powdery_mildew":
	["Powdery mildew is a common fungal disease that affects various plants, including squash. It is caused by different species of fungi, such as Podosphaera spp. and Erysiphe spp.<br><br><br><strong>What can we do ?</strong><br><br> • Sulfur-based Fungicides: Sulfur-based fungicides are effective against powdery mildew. They can be applied as a preventive measure or at the first sign of symptoms.<br><br>"
    "• Horticultural Oils: Neem oil or other horticultural oils can be effective against powdery mildew. These oils disrupt the fungal membranes and inhibit their growth.<br><br>"
    "•Early Treatment: Begin fungicide applications early in the growing season, especially during periods of warm and dry weather that favor powdery mildew development.<br><br>"
    "• Regular Applications: Follow a regular spray schedule, particularly if the environmental conditions are conducive to powdery mildew.<br><br>",
	"A_xsjZ139g4?si", "0m-0KBoE9sw?si"],
"Strawberry___Leaf_scorch":
	["Leaf scorch in strawberries can be caused by various factors, including diseases, environmental stress, or nutrient deficiencies. One of the common diseases associated with leaf scorch in strawberries is Strawberry Leaf Scorch, caused by the bacterium Xanthomonas fragariae.<br><br><br><strong>What can we do ?</strong><br><br> • Proper Plant Spacing: Ensure proper spacing between strawberry plants to improve air circulation and reduce humidity, which can contribute to disease development.<br><br>"
    "• Mulching: Apply a layer of organic mulch around strawberry plants to maintain consistent soil moisture, suppress weeds, and prevent soil splash onto leaves.<br><br>"
    "•Remove Infected Plant Material: Promptly remove and destroy any leaves or plants showing signs of leaf scorch. This helps prevent the spread of the disease within the strawberry patch.<br><br>"
    "• Avoid Overhead Irrigation: Minimize overhead irrigation to keep foliage dry. Use drip irrigation or soaker hoses to deliver water directly to the soil.<br><br>",
	"vLQwcDE2RvY?si", "U2zM7ZjBPxQ?si"],
"Strawberry___healthy":
	["A healthy strawberry plant exhibits several characteristics that indicate overall well-being and optimal growth.<br><br><br><strong>What can we do ?</strong><br><br> • Vibrant Foliage: Healthy strawberry plants have lush, green foliage. The leaves should be free from discoloration, yellowing, or abnormal spots.<br><br>"
    "• Sturdy Crowns: The crown is the part of the plant where the roots and leaves meet. In healthy strawberries, the crown should be firm and free from signs of rot or damage.<br><br>"
    "• Uniform Growth: Healthy plants show uniform growth with well-distributed leaves and stems. There should be no signs of stunted or distorted growth.<br><br>"
    "•Abundant Flowering: Healthy strawberry plants produce abundant flowers, which are essential for the development of fruit.<br><br>",
	"X056zfLnimk?si", "x1tpsjnYZyo?si"],
"Tomato___Bacterial_spot":
	["Bacterial spot is a common bacterial disease that affects tomatoes. It is caused by the bacterium Xanthomonas campestris pv. vesicatoria. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to bacterial spot. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any plants showing signs of bacterial spot, including leaves, stems, and fruit. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Copper Fungicides: Copper-based fungicides can be effective against bacterial spot. Apply these sprays according to recommended rates and schedules. Copper helps to manage bacterial diseases.<br><br>"
    "• Beneficial Bacteria: Some beneficial bacteria can compete with the pathogenic bacteria causing bacterial spot. These beneficial bacteria may be available in commercial products.<br><br>",
	"E0PxQbmxjYM?si", "jONPVKSvFW0?si"],
"Tomato___Early_blight":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___Late_blight":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___Leaf_Mold":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___Septoria_leaf_spot":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      

"Tomato___Spider_mites Two-spotted_spider_mite":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___Target_Spot":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___Tomato_Yellow_Leaf_Curl_Virus":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___Tomato_mosaic_virus":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],
      
"Tomato___healthy":
	["Early blight is a common fungal disease that affects tomatoes. It is caused by the fungus Alternaria solani. <br><br><br><strong>What can we do ?</strong><br><br> • Choose Resistant Cultivars: Select tomato varieties that are bred for resistance to early blight. Resistant cultivars can significantly reduce the impact of the disease.<br><br>"
    "• Rotate Crops: Avoid planting tomatoes or other solanaceous crops in the same location year after year. Implement a multi-year crop rotation to break the disease cycle.<br><br>"
    "• Remove Infected Plant Material: Promptly remove and destroy any leaves, stems, or fruit showing signs of early blight. This helps prevent the spread of the disease within the tomato patch.<br><br>"
    "• Adequate Plant Spacing: Ensure proper spacing between tomato plants to improve air circulation. Increased airflow helps reduce humidity, which can discourage early blight development.<br><br>",
	"2GYD7aVBFtg?si", "WGilXCaj0Zs?si"],



}

def load_artifacts():
    global model
    model = tf.keras.models.load_model("plantDisease.h5" , compile = False)

def get_news(predicted_value):
    # Init News API
    newsapi = NewsApiClient(api_key='a9417c9fb6594acb8d02fdf627cb9bce')

    # Get top headlines related to the predicted disease
    top_headlines = newsapi.get_top_headlines(q=predicted_value, language='en')

    return top_headlines['articles']
   

def classify_Disease(image_path):
	global model, output_class
	test_image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
	test_image = tf.keras.preprocessing.image.img_to_array(test_image) / 255
	test_image = np.expand_dims(test_image, axis = 0)
	predicted_array = model.predict(test_image)
	predicted_value = output_class[np.argmax(predicted_array)]
	return predicted_value, data[predicted_value][0], data[predicted_value][1], data[predicted_value][2]



    

