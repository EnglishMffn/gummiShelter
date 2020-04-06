import os
import csv
import random
import names

# Eborall Gummy Generator
# 19 Mar, 2020

# How Many Gummies?
GUMMY_COUNT = int(input("How Many Gummies?\n"))

# Loop Bio Generator a Few Times
def get_bio(max_bio):
  bio_count = 0

  bio = ""
  adjectives = [
      "boorish",
      "warm",
      "elite",
      "early",
      "parsimonious",
      "aggressive",
      "needy",
      "spiky",
      "muddled",
      "spiteful",
      "sudden",
      "habitual",
      "hot",
      "miscreant",
      "absent",
      "pale",
      "fretful",
      "furry",
      "acid",
      "alive",
      "helpless",
      "wanting",
      "labored",
      "tired",
      "proud",
      "illustrious",
      "last",
      "overt",
      "bashful",
      "parallel",
      "disgusted",
      "lopsided",
      "cut",
      "perpetual",
      "beautiful",
      "gifted",
      "garrulous",
      "maniacal",
      "sophisticated",
      "plastic",
      "free",
      "imaginary",
      "laughable",
      "absurd",
      "possessive",
      "intelligent",
      "vengeful",
      "repulsive",
      "axiomatic",
      "internal",
      "terrific",
      "accidental",
      "disagreeable",
      "juicy",
      "modern",
      "heartbreaking",
      "unused",
      "shaky",
      "ugly",
      "dispensable",
      "cluttered",
      "thinkable",
      "cowardly",
      "oval",
      "futuristic",
      "rhetorical",
      "hesitant",
      "childlike",
      "jittery",
      "left",
      "kindly",
      "hurried",
      "abrupt",
      "aboard",
      "unusual",
      "fluttering",
      "majestic",
      "deadpan",
      "fierce",
      "silent",
      "certain",
      "obnoxious",
      "foregoing",
      "overjoyed",
      "damaging",
      "sincere",
      "second",
      "normal",
      "sloppy",
      "bewildered",
      "thankful",
      "real",
      "heady",
      "macho",
      "foolish",
      "open",
      "crooked",
      "onerous",
      "cooing",
      "irritating",
      "kindhearted",
      "brown",
      "terrible",
      "windy",
      "silent",
      "verdant",
      "nimble",
      "bitter",
      "forgetful",
      "short",
      "momentous",
      "interesting",
      "uttermost",
      "glorious",
      "faithful",
      "squealing",
      "weak",
      "staking",
      "easy",
      "silky",
      "relieved",
      "magnificent",
      "ratty",
      "damaged",
      "noiseless",
      "neighborly",
      "quixotic",
      "female",
      "decorous",
      "friendly",
      "wholesale",
      "pink",
      "same",
      "narrow",
      "general",
      "extra-small",
      "longing",
      "tidy",
      "miniature",
      "swift",
      "sweet",
      "astonishing",
      "incompetent",
      "vast",
      "skillful",
      "petite",
      "painstaking",
      "broad",
      "fascinated",
      "ragged",
      "abject",
      "numberless",
      "pleasant",
      "substantial",
      "hateful",
      "heavenly",
      "unable",
      "mature",
      "nasty",
      "nosy",
      "watery",
      "puffy",
      "aquatic",
      "spectacular",
      "snotty",
      "daily",
      "tawdry",
      "creepy",
      "vague",
      "whispering",
      "abundant",
      "gaudy",
      "permissible",
      "temporary",
      "thundering",
      "meek",
      "joyous",
      "nondescript",
      "depressed",
      "noxious",
      "dreary",
      "tedious",
      "pretty",
      "earsplitting",
      "needless",
      "enthusiastic",
      "lazy",
      "moldy",
      "disillusioned",
      "voracious",
      "smoggy",
      "skinny",
      "hurt",
      "adventurous",
      "hard",
      "zealous",
      "strong",
      "wry",
      "comfortable",
      "purring"
  ]

  adverbs = [
      "primarily",
      "upward",
      "very",
      "oddly",
      "brightly",
      "perfectly",
      "ferociously",
      "eventually",
      "rather",
      "cheerfully",
      "tightly",
      "boldly",
      "especially",
      "cruelly",
      "furiously",
      "righteously",
      "fortunately",
      "upside-down",
      "seriously",
      "enormously",
      "violently",
      "solidly",
      "simply",
      "tremendously",
      "loudly",
      "shrilly",
      "hastily",
      "unaccountably",
      "seemingly",
      "devotedly",
      "knowingly",
      "deftly",
      "joyously",
      "enthusiastically",
      "clearly",
      "seldom",
      "accidentally",
      "longingly",
      "however",
      "rudely",
      "reluctantly",
      "faithfully",
      "never",
      "adventurously",
      "thoroughly",
      "cleverly",
      "positively",
      "possibly",
      "playfully",
      "unexpectedly",
      "naturally",
      "overconfidently",
      "monthly",
      "unabashedly",
      "defiantly",
      "sweetly",
      "vaguely",
      "uselessly",
      "soon",
      "mainly",
      "voluntarily",
      "kiddingly",
      "sternly",
      "coyly",
      "strongly",
      "owlishly",
      "more",
      "upliftingly",
      "courageously",
      "frankly",
      "dearly",
      "innocently",
      "valiantly",
      "partially",
      "crazily",
      "fast",
      "queasily",
      "diligently",
      "literally",
      "yearningly",
      "upright",
      "hopefully",
      "forth",
      "honestly",
      "kindheartedly",
      "basically",
      "needily",
      "elsewhere",
      "questioningly",
      "tenderly",
      "lovingly",
      "daintily",
      "mysteriously",
      "slightly",
      "certainly",
      "normally",
      "selfishly",
      "yawningly",
      "recklessly",
      "quicker",
      "gently",
      "awkwardly",
      "wholly",
      "viciously",
      "unethically",
      "kissingly",
      "everywhere",
      "readily",
      "hardly",
      "nicely",
      "thankfully",
      "terrifically",
      "already",
      "swiftly",
      "lazily",
      "quarrelsomely",
      "frantically",
      "angrily",
      "energetically",
      "carelessly",
      "unfortunately",
      "fondly",
      "gleefully",
      "joshingly",
      "verbally",
      "tediously",
      "helpfully",
      "weakly",
      "recently",
      "upwardly",
      "officially",
      "coaxingly",
      "colorfully",
      "questionably",
      "highly",
      "unnecessarily",
      "madly",
      "delightfully",
      "constantly",
      "kookily",
      "scarily",
      "almost",
      "hourly",
      "wearily",
      "mostly",
      "restfully",
      "truthfully",
      "physically",
      "usefully",
      "heavily",
      "blindly",
      "else",
      "rigidly",
      "deliberately",
      "scarcely",
      "keenly",
      "separately",
      "bleakly",
      "nearly",
      "evenly",
      "obnoxiously",
      "optimistically",
      "tomorrow",
      "boastfully",
      "arrogantly",
      "inwardly",
      "politely",
      "woefully",
      "loyally",
      "previously",
      "exactly",
      "anyway",
      "patiently",
      "even",
      "dimly",
      "sadly",
      "reproachfully",
      "successfully",
      "closely",
      "unbearably",
      "vacantly",
      "rapidly",
      "fairly",
      "offensively",
      "noisily",
      "bravely",
      "willfully",
      "punctually",
      "jovially",
      "early",
      "beautifully",
      "joyfully",
      "somewhat",
      "quirkily",
      "shakily",
      "completely",
      "cautiously",
      "promptly",
      "unimpressively",
      "vainly"
  ]

  while bio_count < max_bio:
    if bio_count == 0:
      bio += str(adverbs[random.randint(0, 199)]).capitalize() + \
          " " + adjectives[random.randint(0, 199)]
    else:
      bio += str(adverbs[random.randint(0, 199)]) + \
          " " + adjectives[random.randint(0, 199)]

    if bio_count < max_bio - 1:
       bio += ", "

    bio_count += 1
  return bio

COUNT = 0
GUMMY_DATA = []

GUMMY_TYPES = ["Bear", "Worm", "Fish"]

# Generate Gummies
while COUNT < GUMMY_COUNT:
  # Loop Dict
  gummy_bio = {}

  # Random Type Number
  random_type = random.randint(0, 2)
  
  # Random Name
  name = names.get_first_name()

  gummy_type = GUMMY_TYPES[random_type]
  bio = get_bio(3)

  # Random Profile Pic
  profile_pic = "/" + str(gummy_type).lower() + "/" + \
      str(random.randint(1, 9)) + '.jpg'
  
  gummy_bio['Name'] = name + ' Gummy' + str(gummy_type).lower()
  gummy_bio['Type'] = gummy_type
  gummy_bio['bio'] = bio
  gummy_bio['Avatar'] = profile_pic

  # Append Loop Dict to All Gummies Array
  GUMMY_DATA.append(gummy_bio)

  COUNT += 1

# Write Array to CSV
FIELD_NAMES = [key for key in GUMMY_DATA[0]]
F = open(os.path.join(os.path.dirname(__file__), "Generated Gummies.csv"), "w")

with F:
    WRITER = csv.DictWriter(F, fieldnames=FIELD_NAMES)
    WRITER.writeheader()
    WRITER.writerows(GUMMY_DATA)

print("\n" + str(GUMMY_COUNT) +" Gummies Generated Successfully")
