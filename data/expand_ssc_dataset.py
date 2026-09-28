import json
import os

# Load existing base questions
existing_questions = []
if os.path.exists("data/questions.json"):
    with open("data/questions.json", "r", encoding="utf-8") as f:
        existing_questions = json.load(f)

print(f"Loaded {len(existing_questions)} initial questions.")

start_id = len(existing_questions) + 1

new_questions = [
    # --- QUANTITATIVE APTITUDE (MATHS) ---
    {
        "id": start_id,
        "subject": "Quantitative Aptitude",
        "topic": "Algebra",
        "question": "If x + y + z = 0, what is the value of (x³ + y³ + z³) / (xyz)?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "0"},
        "correct_answer": "C",
        "explanation": "Standard Algebraic Identity:\nIf x + y + z = 0, then x³ + y³ + z³ = 3xyz.\n\nTherefore, (x³ + y³ + z³) / (xyz) = 3xyz / xyz = 3."
    },
    {
        "id": start_id + 1,
        "subject": "Quantitative Aptitude",
        "topic": "Geometry",
        "question": "The radii of two concentric circles are 13 cm and 5 cm. What is the length of the chord of the outer circle which touches the inner circle?",
        "options": {"A": "12 cm", "B": "18 cm", "C": "24 cm", "D": "26 cm"},
        "correct_answer": "C",
        "explanation": "Let O be the common center.\nLet the chord AB of the outer circle touch the inner circle at P.\nSince OP is perpendicular to AB at the point of contact P:\nIn right-angled triangle OPA:\nOA = radius of outer circle = 13 cm\nOP = radius of inner circle = 5 cm\n\nBy Pythagoras Theorem:\nAP = √(OA² - OP²) = √(13² - 5²) = √(169 - 25) = √144 = 12 cm.\n\nSince the perpendicular from the center bisects the chord:\nLength of chord AB = 2 * AP = 2 * 12 = 24 cm."
    },
    {
        "id": start_id + 2,
        "subject": "Quantitative Aptitude",
        "topic": "Percentage",
        "question": "In an examination, 35% of total candidates failed in Hindi, 45% failed in English, and 20% failed in both. What percentage of candidates passed in both subjects?",
        "options": {"A": "30%", "B": "40%", "C": "45%", "D": "50%"},
        "correct_answer": "B",
        "explanation": "Using Principle of Inclusion-Exclusion:\nPercentage failed in at least one subject = % Failed in Hindi + % Failed in English - % Failed in Both\n= 35% + 45% - 20% = 60%.\n\nPercentage of candidates who passed in both subjects = 100% - 60% = 40%."
    },
    {
        "id": start_id + 3,
        "subject": "Quantitative Aptitude",
        "topic": "Pipes & Cisterns",
        "question": "Pipe A can fill a tank in 10 hours and Pipe B can fill it in 15 hours. Pipe C can empty the full tank in 20 hours. If all three pipes are opened together, how long will it take to fill the tank?",
        "options": {"A": "8 hours 34 min", "B": "8 hours 30 min", "C": "9 hours", "D": "12 hours"},
        "correct_answer": "A",
        "explanation": "Let total tank capacity = LCM(10, 15, 20) = 60 units.\n• Efficiency of A = +6 units/hr\n• Efficiency of B = +4 units/hr\n• Efficiency of C = -3 units/hr (emptying)\n\nNet work done in 1 hour = 6 + 4 - 3 = 7 units/hr.\n\nTime taken to fill tank = 60 / 7 = 8 4/7 hours = 8 hours + (4/7 * 60) mins ≈ 8 hours 34 minutes."
    },
    {
        "id": start_id + 4,
        "subject": "Quantitative Aptitude",
        "topic": "Mensuration 2D",
        "question": "If the length of a rectangle is increased by 20% and its breadth is decreased by 10%, what is the net percentage change in its area?",
        "options": {"A": "8% increase", "B": "10% increase", "C": "8% decrease", "D": "2% increase"},
        "correct_answer": "A",
        "explanation": "Using Successive Percentage Formula:\nNet Change = a + b + (a * b) / 100\nHere a = +20, b = -10:\nNet Change = 20 - 10 + (20 * -10) / 100\n= 10 - 2 = +8%.\n\nSince the result is positive, the area increases by 8%."
    },
    {
        "id": start_id + 5,
        "subject": "Quantitative Aptitude",
        "topic": "Mensuration 3D",
        "question": "The diagonal of a cube is 6√3 cm. What is its total surface area?",
        "options": {"A": "144 cm²", "B": "216 cm²", "C": "288 cm²", "D": "180 cm²"},
        "correct_answer": "B",
        "explanation": "Formula for Diagonal of a cube = a√3 (where 'a' is side length).\nGiven a√3 = 6√3 => a = 6 cm.\n\nTotal Surface Area of cube = 6a²\n= 6 * (6)² = 6 * 36 = 216 cm²."
    },
    {
        "id": start_id + 6,
        "subject": "Quantitative Aptitude",
        "topic": "Number System",
        "question": "What is the remainder when 7¹⁰³ is divided by 25?",
        "options": {"A": "7", "B": "18", "C": "24", "D": "1"},
        "correct_answer": "B",
        "explanation": "Using Euler's Totient Theorem:\nTotient of 25 (φ(25)) = 25 * (1 - 1/5) = 20.\n7²⁰ ≡ 1 (mod 25).\n\nRewrite 7¹⁰³ = (7²⁰)⁵ * 7³ = (1)⁵ * 343\n= 343 (mod 25).\n\nNow, 343 ÷ 25 = 13 with a remainder of 18.\nHence, remainder is 18."
    },
    {
        "id": start_id + 7,
        "subject": "Quantitative Aptitude",
        "topic": "Average",
        "question": "The average of 11 numbers is 50. If the average of the first 6 numbers is 49 and that of the last 6 numbers is 52, find the 6th number.",
        "options": {"A": "54", "B": "56", "C": "52", "D": "48"},
        "correct_answer": "B",
        "explanation": "Sum of all 11 numbers = 11 * 50 = 550.\nSum of first 6 numbers = 6 * 49 = 294.\nSum of last 6 numbers = 6 * 52 = 312.\n\nSum of (first 6 + last 6) = 294 + 312 = 606.\nNotice that the 6th number is counted twice in this sum.\n6th number = (Sum of 12 numbers) - (Sum of 11 numbers)\n= 606 - 550 = 56."
    },
    {
        "id": start_id + 8,
        "subject": "Quantitative Aptitude",
        "topic": "Mixtures & Alligations",
        "question": "In what ratio must water be mixed with milk costing ₹60 per liter so that the mixture is worth ₹50 per liter?",
        "options": {"A": "1 : 5", "B": "1 : 4", "C": "2 : 5", "D": "1 : 6"},
        "correct_answer": "A",
        "explanation": "Using Rule of Alligation:\nCost of Water = ₹0/L\nCost of Milk = ₹60/L\nMean Price = ₹50/L\n\nWater : Milk = (Cost of Milk - Mean Price) : (Mean Price - Cost of Water)\n= (60 - 50) : (50 - 0)\n= 10 : 50 = 1 : 5.\n\nHence, the ratio of water to milk is 1 : 5."
    },
    {
        "id": start_id + 9,
        "subject": "Quantitative Aptitude",
        "topic": "Simple & Compound Interest",
        "question": "A sum of money doubles itself in 4 years at compound interest (compounded annually). In how many years will it become 8 times of itself at the same rate?",
        "options": {"A": "8 years", "B": "12 years", "C": "16 years", "D": "10 years"},
        "correct_answer": "B",
        "explanation": "Rule of Powers in Compound Interest:\nIf a principal becomes 2¹ times in 4 years,\nthen it will become 2³ (8 times) in (3 * 4) years = 12 years."
    },

    # --- REASONING ---
    {
        "id": start_id + 10,
        "subject": "General Intelligence & Reasoning",
        "topic": "Venn Diagrams",
        "question": "Which of the following Venn diagrams best represents the relationship between:\n'Reptiles, Snakes, Lizards'",
        "options": {
            "A": "Two non-overlapping circles inside a large circle",
            "B": "Three concentric circles",
            "C": "Three intersecting circles",
            "D": "Two overlapping circles inside a large circle"
        },
        "correct_answer": "A",
        "explanation": "Logical Relationship:\n• Both 'Snakes' and 'Lizards' are distinct sub-categories of 'Reptiles'.\n• No snake is a lizard.\nTherefore, the correct diagram shows two separate smaller circles (Snakes & Lizards) completely enclosed inside a larger circle (Reptiles)."
    },
    {
        "id": start_id + 11,
        "subject": "General Intelligence & Reasoning",
        "topic": "Missing Number Matrix",
        "question": "Select the missing number from the given pattern:\n5   8   13\n6   9   15\n7  11   ?",
        "options": {"A": "17", "B": "18", "C": "19", "D": "20"},
        "correct_answer": "B",
        "explanation": "Pattern in Row 1: 5 + 8 = 13\nPattern in Row 2: 6 + 9 = 15\nPattern in Row 3: 7 + 11 = 18.\n\nHence, the missing number is 18."
    },
    {
        "id": start_id + 12,
        "subject": "General Intelligence & Reasoning",
        "topic": "Seating Arrangement",
        "question": "Five friends A, B, C, D, and E are sitting in a row facing North. A is sitting next to B. C is sitting next to D. C is not sitting with E who is on the left end of the row. D is second from the right end. A is to the right of B and E. A and C are sitting together. In which position is A sitting?",
        "options": {"A": "Center", "B": "Second from Left", "C": "Right End", "D": "Second from Right"},
        "correct_answer": "B",
        "explanation": "Step-by-step arrangement:\n1. 5 positions: [1, 2, 3, 4, 5] (Left to Right).\n2. E is on the left end -> Pos 1 = E.\n3. D is second from right -> Pos 4 = D.\n4. C is next to D and not next to E -> Pos 5 = C or Pos 3 = C. Since D is at 4, C can be at 3.\n5. Remaining positions for B and A: Pos 2 and Pos 3.\n   Since A is sitting next to B and to the right of B: Pos 2 = B, Pos 3 = A.\n\nRow order from Left to Right: E, B, A, D, C (or E, B, A, C, D).\nIn both cases, A is at Position 2 (Second from Left)."
    },
    {
        "id": start_id + 13,
        "subject": "General Intelligence & Reasoning",
        "topic": "Order & Ranking",
        "question": "In a class of 45 students, Rahul's rank is 15th from the top. What is his rank from the bottom?",
        "options": {"A": "30th", "B": "31st", "C": "32nd", "D": "29th"},
        "correct_answer": "B",
        "explanation": "Ranking Formula:\nTotal Students = (Rank from Top) + (Rank from Bottom) - 1\n45 = 15 + Rank_bottom - 1\n45 = 14 + Rank_bottom\nRank_bottom = 45 - 14 = 31st."
    },
    {
        "id": start_id + 14,
        "subject": "General Intelligence & Reasoning",
        "topic": "Alphabet Series",
        "question": "What will come in place of the question mark (?) in the series:\nAZ, CX, EV, GT, ?",
        "options": {"A": "IR", "B": "HS", "C": "JQ", "D": "KP"},
        "correct_answer": "A",
        "explanation": "Pattern:\nFirst letters: A(+2)->C(+2)->E(+2)->G(+2)->I\nSecond letters: Z(-2)->X(-2)->V(-2)->T(-2)->R\n(Also, each pair consists of opposite letters in the alphabet: A-Z, C-X, E-V, G-T, I-R).\n\nHence, the next term is IR."
    },

    # --- GENERAL AWARENESS ---
    {
        "id": start_id + 15,
        "subject": "General Awareness",
        "topic": "Indian History",
        "question": "Who was the Governor-General of India during the Revolt of 1857?",
        "options": {"A": "Lord Dalhousie", "B": "Lord Canning", "C": "Lord Curzon", "D": "Lord Ripon"},
        "correct_answer": "B",
        "explanation": "Lord Canning was the Governor-General of India during the Indian Rebellion of 1857. After the Revolt, he also became the first Viceroy of India under the Government of India Act 1858."
    },
    {
        "id": start_id + 16,
        "subject": "General Awareness",
        "topic": "Indian Polity",
        "question": "Through which Constitutional Amendment Act were the Fundamental Duties incorporated into the Indian Constitution?",
        "options": {"A": "42nd Amendment Act, 1976", "B": "44th Amendment Act, 1978", "C": "86th Amendment Act, 2002", "D": "73rd Amendment Act, 1992"},
        "correct_answer": "A",
        "explanation": "Fundamental Duties (Part IV-A, Article 51A) were added to the Constitution by the 42nd Constitutional Amendment Act, 1976, upon the recommendation of the Swaran Singh Committee. Initially 10 duties were added; the 11th duty was added by the 86th Amendment in 2002."
    },
    {
        "id": start_id + 17,
        "subject": "General Awareness",
        "topic": "Biology",
        "question": "Deficiency of which Vitamin causes Night Blindness?",
        "options": {"A": "Vitamin A", "B": "Vitamin B1", "C": "Vitamin C", "D": "Vitamin D"},
        "correct_answer": "A",
        "explanation": "Vitamins & Deficiency Diseases Table:\n• **Vitamin A (Retinol)** -> Night Blindness (Nyctalopia), Xerophthalmia\n• **Vitamin B1 (Thiamine)** -> Beriberi\n• **Vitamin C (Ascorbic Acid)** -> Scurvy\n• **Vitamin D (Calciferol)** -> Rickets"
    },
    {
        "id": start_id + 18,
        "subject": "General Awareness",
        "topic": "Static GK",
        "question": "Bihu is a famous traditional folk dance of which Indian state?",
        "options": {"A": "Assam", "B": "Odisha", "C": "Kerala", "D": "Punjab"},
        "correct_answer": "A",
        "explanation": "Bihu is the most popular folk dance of Assam, performed during the Bihu festival celebrating agricultural seasons."
    },
    {
        "id": start_id + 19,
        "subject": "General Awareness",
        "topic": "Indian Geography",
        "question": "Which strait separates India from Sri Lanka?",
        "options": {"A": "Bering Strait", "B": "Palk Strait", "C": "Malacca Strait", "D": "Gibraltar Strait"},
        "correct_answer": "B",
        "explanation": "Palk Strait separates the Tamil Nadu state of India and the Mannar district of Sri Lanka."
    },
    {
        "id": start_id + 20,
        "subject": "General Awareness",
        "topic": "Economics",
        "question": "What is 'Stagflation' in Economics?",
        "options": {
            "A": "High inflation combined with high economic growth",
            "B": "High inflation combined with stagnant economic growth and high unemployment",
            "C": "Low inflation with rapid growth",
            "D": "Deflation with full employment"
        },
        "correct_answer": "B",
        "explanation": "Stagflation is an economic event in which the inflation rate is high, the economic growth rate slows down (stagnates), and unemployment remains steadily high."
    },

    # --- ENGLISH LANGUAGE ---
    {
        "id": start_id + 21,
        "subject": "English Language",
        "topic": "Direct & Indirect Speech",
        "question": "Select the correct indirect form of the given sentence:\nHe said to me, 'Where are you going?'",
        "options": {
            "A": "He asked me where I was going.",
            "B": "He told me where I am going.",
            "C": "He asked me where was I going.",
            "D": "He asked to me where I was going."
        },
        "correct_answer": "A",
        "explanation": "Rules for Direct to Indirect Speech conversion:\n1. 'Said to' changes to 'asked' for interrogative sentences.\n2. Present Continuous ('are going') changes to Past Continuous ('was going').\n3. Question word 'where' acts as conjunction.\n4. Word order changes from interrogative to assertive ('I was going' instead of 'was I going').\n\nCorrect Indirect Sentence: 'He asked me where I was going.'"
    },
    {
        "id": start_id + 22,
        "subject": "English Language",
        "topic": "Active & Passive Voice",
        "question": "Select the correct passive form of the given sentence:\n'The chef prepared a delicious meal.'",
        "options": {
            "A": "A delicious meal is prepared by the chef.",
            "B": "A delicious meal was prepared by the chef.",
            "C": "A delicious meal had been prepared by the chef.",
            "D": "A delicious meal was being prepared by the chef."
        },
        "correct_answer": "B",
        "explanation": "Simple Past Active ('prepared') changes to Simple Past Passive ('was/were prepared').\nSubject ('The chef') and Object ('A delicious meal') swap places.\n\nCorrect Passive Sentence: 'A delicious meal was prepared by the chef.'"
    },
    {
        "id": start_id + 23,
        "subject": "English Language",
        "topic": "Spelling Error",
        "question": "Select the INCORRECTLY spelt word:",
        "options": {"A": "Accommodate", "B": "Occurrence", "C": "Embarrass", "D": "Maintanance"},
        "correct_answer": "D",
        "explanation": "Correct Spellings:\n• **Accommodate**: Double 'c' and double 'm'.\n• **Occurrence**: Double 'c' and double 'r'.\n• **Embarrass**: Double 'r' and double 's'.\n• **Maintenance** (NOT Maintanance): Ends with '-enance'."
    },
    {
        "id": start_id + 24,
        "subject": "English Language",
        "topic": "Cloze Test / Fill in the blanks",
        "question": "Select the most appropriate option to fill in the blank:\n'The government has decided to ________ the tax rates to boost economic growth.'",
        "options": {"A": "reduce", "B": "enlarge", "C": "prolong", "D": "escalate"},
        "correct_answer": "A",
        "explanation": "In context of boosting economic growth, governments cut or reduce tax rates to increase consumer spending and investments. Hence 'reduce' is the most appropriate word."
    },
    {
        "id": start_id + 25,
        "subject": "English Language",
        "topic": "Idioms & Phrases",
        "question": "Select the meaning of the idiom: 'Burn the midnight oil'",
        "options": {
            "A": "To waste fuel",
            "B": "To work or study late into the night",
            "C": "To create trouble",
            "D": "To burn a lamp"
        },
        "correct_answer": "B",
        "explanation": "'Burn the midnight oil' means to read, study, or work far into the night."
    }
]

total_questions = existing_questions + new_questions

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(total_questions, f, indent=2, ensure_ascii=False)

with open("data/questions.js", "w", encoding="utf-8") as f:
    f.write("window.SSC_QUESTIONS = " + json.dumps(total_questions, ensure_ascii=False) + ";\n")

print(f"Updated question bank total: {len(total_questions)} questions.")
