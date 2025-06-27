# --------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/ETL-scripting
# Date        :March 27, 2025 to May 3, 2025
# Description : Insert Data into the MongoDB
# ----------------------------------------------------------------------------------------

from urllib.parse import quote_plus
from pymongo import MongoClient

# URL-encode the password
password = quote_plus('admin@369')

# MongoDB connection string with updated username and password
client = MongoClient(f'mongodb://admin:{password}@localhost:27017/amazon_records?authSource=admin')

# Select the database and collection
db = client['amazon_records']
collection = db['musical_instruments']

# Example data (from your JSON input)
data = [
    {
        "rating": 5.0,
        "title": "Nice",
        "text": "If I had a dollar for how many times I have played this CD...",
        "images": [],
        "asin": "B004RQ2IRG",
        "parent_asin": "B004RQ2IRG",
        "user_id": "AFUOYIZBU3MTBOLYKOJE5Z35MBDA",
        "timestamp": 1618972613292,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 5.0,
        "title": "Excellent",
        "text": "Awesome sound - can't wait to see them in person...",
        "images": [],
        "asin": "B0026UZEI0",
        "parent_asin": "B0026UZEI0",
        "user_id": "AHGAOIZVODNHYMNCBV4DECZH42UQ",
        "timestamp": 1308167525000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 5.0,
        "title": "Great service",
        "text": "This is a great CD. Good music and plays well...",
        "images": [],
        "asin": "B0055JSYHC",
        "parent_asin": "B0055JSYHC",
        "user_id": "AFGEM6BXCYHUILEOA3P2ZYBEF2TA",
        "timestamp": 1615838793006,
        "helpful_vote": 0,
        "verified_purchase": True
    },
     {
        "rating": 1.0,
        "title": "No good",
        "text": "These are not real German singers; they have accents. It is nothing like what was advertised. Music stinks.",
        "images": [],
        "asin": "B000F9SMUQ",
        "parent_asin": "B000F9SMUQ",
        "user_id": "AH3OG6QD6EDJGZRVCFKV4B66VWNQ",
        "timestamp": 1405219741000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 3.0,
        "title": "Cool concept, so-so execution...",
        "text": "I first heard this playing in a Nagoya shop and fell in love with the remix of Ke$ha's 'Tik Tok' (Ke$ha and Lady Gaga are EVERYWHERE in Japan), which then morphed into several other recent pop hits. When the salesgirl handed me the CD, I was pleased to see that it actually included thirty pop songs by the likes of Lady Gaga, Usher, La Roux, Katy Perry, Black-Eyed Peas, Ke$ha, etc. I researched more after I got home, and discovered that this Japanese label (Manhattan Records) exists solely to put out rerecorded and remixed dance CDs based on recent pop hits, the key word being rerecorded. I guessed as much as I was listening to the CD in-store; several of the soundalikes do a great job, others are just so-so. It's great for workouts, though, since the tracks fade one into another with no downtime (the bad side is that if you've got it in shuffle, the beginning of the next song, which is often in a different key, is kind of an awkward fade-out when not played in sequence).",
        "images": [],
        "asin": "B0049D1WVK",
        "parent_asin": "B0049D1WVK",
        "user_id": "AFW2PDT3AMT4X3PYQG7FJZH5FXFA",
        "timestamp": 1309029595000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 4.0,
        "title": "\"L'attaque des clones\" a satisfying taste of things to come.",
        "text": "I just saw \"Star Wars: L'attaque des clones\" last night (in Ste-Foy, Québec) at a sold-out show (it was playing in English at the theatre next door but I opted for the French version instead). First of all, the theatre itself was an experience: an immense screen that looked as large as an IMAX screen, intense surround THX sound, and the digital picture (even at that size) was amazingly crisp, the colors vibrant, and the sound effects were ear-splitting and exhilarating (especially the moments of silence that preceded the sonic depth charge explosions!) I have seen the other four Star Wars movies but avoided reading publicity and reviews for \"Attack of the Clones\" in order to enjoy every moment without worrying over a particular critic's faults with the film. This film is much darker than \"The Phantom Menace\" could have ever aspired to be. Lucas has moved from stilted, juvenile scriptwriting on \"TPM\" to (still) stilted, mythological, more adult scriptwriting on \"Attack of the Clones.\" Here we see Anakin as a headstrong, angry, frequently obnoxious young adult who loves backtalking, disobeying orders, and getting his way—a most dangerous thing when you are destined to become the most powerful Jedi of all time. The dialogue is very politically minded (I had to wonder at the \"separatist\" politics of the film, being in Québec) and the romance scenes feel wooden and awkward, but Natalie Portman and Hayden Christensen definitely have onscreen chemistry. (I have since read that Hayden purposely would flash a thumbs-up at the end of his takes so Lucas would have to reshoot the kissing scenes... I did get a laugh out of that.) Jar Jar Binks has (thankfully) been reduced to a few mere minutes of screentime, in which he manages to be (awkwardly) regal and somewhat less annoying than in Episode I. My favorite part of the \"Star Wars\" universe has always been the astonishing variety of aliens and alien languages... when I was a kid I wanted to be the one that came up with all the cool sounding languages spoken in the film (I still do as a matter of fact). As usual, Natalie Portman's costumes are to die for, incorporating Asian and European fashion influences while still managing to be gracefully fresh and exotic. Only one I could have done without was the black leather getup—elbow-high leather gloves and a black leather bustier, yet she's telling Anakin she's not interested in a romantic relationship... riiight (Curiously enough, Anakin wears black leather as well... and if you listen carefully you can hear a whole lot of leather creaking onscreen). Portman certainly runs around baring her abs-of-steel midriff for much of the film (along with being very braless in a very tight white jumpsuit, which I found tasteless and unnecessary... I mean, the costumers spent the last film and part of this one coming up with these gorgeous gowns and now they're raiding Lara Croft's closet?) The CGI imagery was breathtaking, especially the chase through Coruscant, the clone army, and all of the alien landscapes. John Williams' score incorporates themes from all of the previous \"Star Wars\" soundtracks, including the addition of a new love theme, \"Across the Stars.\" The fight scenes were white-knuckle intense and had me on the edge of my seat. The battle scene with all of the Jedis of all different species was *awesome,* as was Mace Windu's (Samuel L. Jackson) purple lightsaber... a first in \"Star Wars\" history. And Yoda: we finally see him in action and understand why he is the greatest living Jedi. Another first: Yoda is completely computer-animated, and is extremely lifelike. The French translation of the film was almost an exact translation from the English... I actually found that some of the dialogue flowed more smoothly in French. Understanding some of the alien accents (especially the metallic robot ones) was a bit of a challenge for me, but it adds to the fun. Lucas has effectively planted the seeds for the next and final chapter in the \"Star Wars\" saga, redeeming himself from the sometimes mediocre acting, wooden dialogue, and annoying creatures from \"The Phantom Menace.\" Episode II is full of treachery, death, assassination attempts, massacres, and battles between good and evil where right and wrong are sometimes obscured. Unlike Jake Lloyd, the child actor who played Anakin in \"The Phantom Menace,\" in Hayden we see Anakin torn between his inner feelings and his obligations as a Jedi... his romance with Padmé, the (implied) massacre of the Tusken camp, and his defiance, all pointing to his shift to the Dark Side of the Force. The film is rated PG, but it does contain some very intense moments: onscreen kissing and sexual tension of sorts, a decapitation, mutilation, creepy space caterpillars, a gladiator-style execution arena, a massacre and other intense battle scenes that might be disturbing to younger children. But overall it is a very worthy addition to the \"Star Wars\" universe. Can't wait for Episode III: \"Revenge of the Sith.\"",
        "images": [],
        "asin": "B00006H9N3",
        "parent_asin": "B00006H9N3",
        "user_id": "A2W99A2ZXN0D0Z",
        "timestamp": 1127702145000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 4.0,
        "title": "Best of the DJ D-Mix Series",
        "text": "I've purchased several DJ D-Mix albums, and this one is the best by far. It's got a good mix of current hits and classic dance tracks. The sound quality is top-notch, and it really gets the party started. Definitely worth the price.",
        "images": [],
        "asin": "B001H20IRK",
        "parent_asin": "B001H20IRK",
        "user_id": "A2N3K6B8Z3R9N3",
        "timestamp": 1378454967000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 5.0,
        "title": "Five Stars",
        "text": "Great product, highly recommend it!",
        "images": [],
        "asin": "B0032AEVHI",
        "parent_asin": "B0032AEVHI",
        "user_id": "A3M2Z7RXAA2X4P",
        "timestamp": 1453940803000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 2.0,
        "title": "Not as expected",
        "text": "The item did not match the description. The quality was subpar and not worth the price.",
        "images": [],
        "asin": "B002Y5J6H4",
        "parent_asin": "B002Y5J6H4",
        "user_id": "A1B3C4D5E6F7G8H9",
        "timestamp": 1556347203000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 4.0,
        "title": "Very Good",
        "text": "This is a very good product. It meets my needs and I would purchase it again.",
        "images": [],
        "asin": "B0054K2B2G",
        "parent_asin": "B0054K2B2G",
        "user_id": "A2C4D6E8F0G1H2J3",
        "timestamp": 1609459203000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 3.0,
        "title": "Average",
        "text": "It's an average product. Nothing exceptional about it, but it works.",
        "images": [],
        "asin": "B0042S5F3E",
        "parent_asin": "B0042S5F3E",
        "user_id": "A3E4F5G6H7I8J9K0",
        "timestamp": 1612329603000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 1.0,
        "title": "Disappointing",
        "text": "Very disappointed with this purchase. The product broke within a week.",
        "images": [],
        "asin": "B000N2Y9DU",
        "parent_asin": "B000N2Y9DU",
        "user_id": "A2B4C6D8E0F1G2H3",
        "timestamp": 1598400003000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 5.0,
        "title": "Excellent quality",
        "text": "The quality of this product is excellent. Highly recommend it for anyone looking for something reliable.",
        "images": [],
        "asin": "B0018O47O4",
        "parent_asin": "B0018O47O4",
        "user_id": "A4B6C8D0E1F2G3H4",
        "timestamp": 1618972613292,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 4.0,
        "title": "Great but expensive",
        "text": "The product is great and works well, but it is a bit pricey for what it offers.",
        "images": [],
        "asin": "B005F9H5G7",
        "parent_asin": "B005F9H5G7",
        "user_id": "A3C5D7E9F0G1H2J3",
        "timestamp": 1609459203000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 2.0,
        "title": "Not what I expected",
        "text": "The product did not meet my expectations based on the description. Quality is lacking.",
        "images": [],
        "asin": "B000N2Y8J9",
        "parent_asin": "B000N2Y8J9",
        "user_id": "A1B2C3D4E5F6G7H8",
        "timestamp": 1589587203000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 4.0,
        "title": "Good value",
        "text": "This product is a good value for the money. It performs as advertised and meets my needs.",
        "images": [],
        "asin": "B0029M6X3E",
        "parent_asin": "B0029M6X3E",
        "user_id": "A3D5E7F9G0H1I2J3",
        "timestamp": 1612329603000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 3.0,
        "title": "Okay",
        "text": "It's an okay product. It does the job but there are better options available.",
        "images": [],
        "asin": "B0049D2K5F",
        "parent_asin": "B0049D2K5F",
        "user_id": "A2B4C6D8E0F1G2H3",
        "timestamp": 1612329603000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 5.0,
        "title": "Perfect",
        "text": "This is exactly what I was looking for. Perfect in every way.",
        "images": [],
        "asin": "B0036XK0Y6",
        "parent_asin": "B0036XK0Y6",
        "user_id": "A4B6C8D0E1F2G3H4",
        "timestamp": 1618972613292,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 2.0,
        "title": "Not worth it",
        "text": "This product did not live up to my expectations. It broke after a few uses.",
        "images": [],
        "asin": "B000F8S8J2",
        "parent_asin": "B000F8S8J2",
        "user_id": "A1B2C3D4E5F6G7H8",
        "timestamp": 1589587203000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 5.0,
        "title": "Fantastic!",
        "text": "I am extremely happy with this purchase. The product exceeded my expectations in every way.",
        "images": [],
        "asin": "B0028AY6N8",
        "parent_asin": "B0028AY6N8",
        "user_id": "A3D5E7F9G0H1I2J3",
        "timestamp": 1615838793006,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 4.0,
        "title": "Very good product",
        "text": "The product is very good and meets most of my needs. Would definitely buy again.",
        "images": [],
        "asin": "B004R2F8X6",
        "parent_asin": "B004R2F8X6",
        "user_id": "A2C4D6E8F0G1H2J3",
        "timestamp": 1609459203000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 3.0,
        "title": "Average performance",
        "text": "The performance of the product is average. It does the job but could be improved.",
        "images": [],
        "asin": "B0018O8G4C",
        "parent_asin": "B0018O8G4C",
        "user_id": "A3E4F5G6H7I8J9K0",
        "timestamp": 1612329603000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 1.0,
        "title": "Terrible",
        "text": "The product did not work at all. Waste of money.",
        "images": [],
        "asin": "B000N2Y7A9",
        "parent_asin": "B000N2Y7A9",
        "user_id": "A2B4C6D8E0F1G2H3",
        "timestamp": 1598400003000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 5.0,
        "title": "Highly recommend",
        "text": "This product is excellent. I would highly recommend it to anyone looking for something reliable and well-made.",
        "images": [],
        "asin": "B0018O3G9K",
        "parent_asin": "B0018O3G9K",
        "user_id": "A4B6C8D0E1F2G3H4",
        "timestamp": 1618972613292,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 4.0,
        "title": "Good quality",
        "text": "The quality of this product is good. It performs well and I am satisfied with my purchase.",
        "images": [],
        "asin": "B0039Y0E9K",
        "parent_asin": "B0039Y0E9K",
        "user_id": "A2C4D6E8F0G1H2J3",
        "timestamp": 1609459203000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 2.0,
        "title": "Not impressed",
        "text": "I am not impressed with this product. It does not work as expected.",
        "images": [],
        "asin": "B000N2Y9DJ",
        "parent_asin": "B000N2Y9DJ",
        "user_id": "A1B2C3D4E5F6G7H8",
        "timestamp": 1589587203000,
        "helpful_vote": 0,
        "verified_purchase": False
    },
    {
        "rating": 3.0,
        "title": "Meh",
        "text": "The product is okay but not great. It gets the job done but nothing more.",
        "images": [],
        "asin": "B0028A7V6K",
        "parent_asin": "B0028A7V6K",
        "user_id": "A3E4F5G6H7I8J9K0",
        "timestamp": 1612329603000,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 5.0,
        "title": "Love it!",
        "text": "I absolutely love this product. It works perfectly and is exactly what I needed.",
        "images": [],
        "asin": "B0037L8N8K",
        "parent_asin": "B0037L8N8K",
        "user_id": "A4B6C8D0E1F2G3H4",
        "timestamp": 1615838793006,
        "helpful_vote": 0,
        "verified_purchase": True
    },
    {
        "rating": 4.0,
        "title": "Good purchase",
        "text": "This product is a good purchase. It does what it promises and is well worth the price.",
        "images": [],
        "asin": "B0049D3K6F",
        "parent_asin": "B0049D3K6F",
        "user_id": "A2C4D6E8F0G1H2J3",
        "timestamp": 1609459203000,
        "helpful_vote": 0,
        "verified_purchase": True
    }

]


# Insert data into the 'musical_instruments' collection
collection.insert_many(data)

print("Data inserted successfully.")
