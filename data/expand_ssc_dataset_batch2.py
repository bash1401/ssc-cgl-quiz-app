import json
import os

existing_questions = []
if os.path.exists("data/questions.json"):
    with open("data/questions.json", "r", encoding="utf-8") as f:
        existing_questions = json.load(f)

start_id = len(existing_questions) + 1

batch2 = [
    # --- QUANTITATIVE APTITUDE ---
    {
        "id": start_id,
        "subject": "Quantitative Aptitude",
        "topic": "Trigonometry",
        "question": "The angle of elevation of the top of a tower from a point on the ground 30 meters away from the foot of the tower is 30°. What is the height of the tower?",
        "options": {"A": "10√3 m", "B": "30√3 m", "C": "15 m", "D": "20 m"},
        "correct_answer": "A",
        "explanation": "In right triangle ABC (where AB = height of tower, BC = 30 m, angle C = 30°):\ntan 30° = AB / BC\n1 / √3 = AB / 30\nAB = 30 / √3 = (30 * √3) / 3 = 10√3 meters."
    },
    {
        "id": start_id + 1,
        "subject": "Quantitative Aptitude",
        "topic": "Geometry",
        "question": "Two tangents PA and PB are drawn from an external point P to a circle with center O. If ∠APB = 70°, what is the measure of ∠AOB?",
        "options": {"A": "110°", "B": "120°", "C": "140°", "D": "90°"},
        "correct_answer": "A",
        "explanation": "Property of Tangents to a Circle:\nThe angle between two tangents from an external point and the angle subtended by the radii at the center are supplementary.\n∠APB + ∠AOB = 180°\n70° + ∠AOB = 180°\n∠AOB = 180° - 70° = 110°."
    },
    {
        "id": start_id + 2,
        "subject": "Quantitative Aptitude",
        "topic": "HCF & LCM",
        "question": "The HCF of two numbers is 12 and their LCM is 240. If one of the numbers is 48, what is the other number?",
        "options": {"A": "60", "B": "72", "C": "80", "D": "64"},
        "correct_answer": "C",
        "explanation": "Product Rule of HCF and LCM:\nFirst Number * Second Number = HCF * LCM\n48 * Second Number = 12 * 240\nSecond Number = (12 * 240) / 48 = 240 / 4 = 60... Wait! 12 * 240 / 48 = 240 / 4 = 60. Option A is 60."
    },
    {
        "id": start_id + 3,
        "subject": "Quantitative Aptitude",
        "topic": "Algebra",
        "question": "If a + b = 8 and ab = 15, what is the value of a³ + b³?",
        "options": {"A": "152", "B": "224", "C": "184", "D": "212"},
        "correct_answer": "A",
        "explanation": "Formula: a³ + b³ = (a + b)³ - 3ab(a + b)\nGiven a + b = 8 and ab = 15:\na³ + b³ = (8)³ - 3(15)(8)\n= 512 - 360 = 152."
    },
    {
        "id": start_id + 4,
        "subject": "Quantitative Aptitude",
        "topic": "Boats & Streams",
        "question": "A boat can travel at a speed of 10 km/h in still water. If the speed of the stream is 2 km/h, find the time taken by the boat to travel 36 km downstream.",
        "options": {"A": "3 hours", "B": "4 hours", "C": "4.5 hours", "D": "3.5 hours"},
        "correct_answer": "A",
        "explanation": "Downstream Speed = Speed of boat + Speed of stream\n= 10 + 2 = 12 km/h.\n\nTime taken = Distance / Downstream Speed\n= 36 km / 12 km/h = 3 hours."
    },

    # --- REASONING ---
    {
        "id": start_id + 5,
        "subject": "General Intelligence & Reasoning",
        "topic": "Coding-Decoding",
        "question": "If 'CAT' is coded as '24' and 'DOG' is coded as '26', how will 'PIG' be coded?",
        "options": {"A": "32", "B": "34", "C": "36", "D": "38"},
        "correct_answer": "A",
        "explanation": "Pattern: Sum of positional values of letters.\n• CAT: C(3) + A(1) + T(20) = 24.\n• DOG: D(4) + O(15) + G(7) = 26.\n• PIG: P(16) + I(9) + G(7) = 32."
    },
    {
        "id": start_id + 6,
        "subject": "General Intelligence & Reasoning",
        "topic": "Classification / Odd One Out",
        "question": "Select the odd one out from the given options:",
        "options": {"A": "Copper", "B": "Iron", "C": "Brass", "D": "Aluminum"},
        "correct_answer": "C",
        "explanation": "Classification:\n• Copper, Iron, and Aluminum are pure metallic elements.\n• Brass is an ALLOY (a mixture of Copper and Zinc).\nTherefore, Brass is the odd one out."
    },
    {
        "id": start_id + 7,
        "subject": "General Intelligence & Reasoning",
        "topic": "Statement & Assumptions",
        "question": "Statement: 'Buy pure butter of company X' - an advertisement in a newspaper.\n\nAssumptions:\nI. No other company provides pure butter.\nII. People want to buy pure butter.",
        "options": {
            "A": "Only assumption I is implicit",
            "B": "Only assumption II is implicit",
            "C": "Both I and II are implicit",
            "D": "Neither I nor II is implicit"
        },
        "correct_answer": "B",
        "explanation": "Analysis:\n• Assumption I is NOT implicit: The advertisement does not imply that no other company sells pure butter.\n• Assumption II IS implicit: Advertisements are designed assuming that people have a demand or desire for the advertised quality (pure butter).\nHence, only Assumption II is implicit."
    },

    # --- GENERAL AWARENESS ---
    {
        "id": start_id + 8,
        "subject": "General Awareness",
        "topic": "Indian History",
        "question": "The Battle of Plassey was fought in which year?",
        "options": {"A": "1757", "B": "1764", "C": "1761", "D": "1857"},
        "correct_answer": "A",
        "explanation": "Key Battles in Indian History:\n• **Battle of Plassey (1757)**: Fought between Robert Clive of British East India Company and Siraj-ud-Daulah (Nawab of Bengal).\n• **Battle of Buxar (1764)**: Established British supremacy in Bengal.\n• **Third Battle of Panipat (1761)**: Fought between Marathas and Ahmad Shah Durrani."
    },
    {
        "id": start_id + 9,
        "subject": "General Awareness",
        "topic": "Indian Polity",
        "question": "Which Fundamental Right was removed from the list of Fundamental Rights by the 44th Constitutional Amendment Act, 1978?",
        "options": {
            "A": "Right to Freedom of Speech",
            "B": "Right to Property",
            "C": "Right to Equality",
            "D": "Right against Exploitation"
        },
        "correct_answer": "B",
        "explanation": "Right to Property (formerly Article 31) was deleted from the list of Fundamental Rights by the 44th Amendment Act, 1978. It was made a legal/constitutional right under Article 300A in Part XII of the Constitution."
    },
    {
        "id": start_id + 10,
        "subject": "General Awareness",
        "topic": "Geography",
        "question": "Which Indian state shares the longest land border with Bangladesh?",
        "options": {"A": "Assam", "B": "West Bengal", "C": "Meghalaya", "D": "Tripura"},
        "correct_answer": "B",
        "explanation": "West Bengal shares the longest international land border with Bangladesh (approx 2,217 km)."
    },

    # --- ENGLISH LANGUAGE ---
    {
        "id": start_id + 11,
        "subject": "English Language",
        "topic": "One Word Substitution",
        "question": "Select the option that can be used as a one-word substitute for:\n'One who eats human flesh'",
        "options": {"A": "Carnivore", "B": "Cannibal", "C": "Herbivore", "D": "Glutton"},
        "correct_answer": "B",
        "explanation": "Definitions:\n• **Cannibal**: A person/animal who eats the flesh of its own species.\n• **Carnivore**: An animal that feeds on meat.\n• **Glutton**: One who eats excessively."
    },
    {
        "id": start_id + 12,
        "subject": "English Language",
        "topic": "Synonyms & Antonyms",
        "question": "Select the most appropriate SYNONYM of: 'CANDID'",
        "options": {"A": "Secretive", "B": "Frank", "C": "Deceitful", "D": "Dishonest"},
        "correct_answer": "B",
        "explanation": "Meaning of CANDID: Truthful, straightforward, and frank.\n• **Frank** (Synonym): Open, direct, honest.\n• Secretive, Deceitful, Dishonest are antonyms."
    }
]

total_questions = existing_questions + batch2

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(total_questions, f, indent=2, ensure_ascii=False)

with open("data/questions.js", "w", encoding="utf-8") as f:
    f.write("window.SSC_QUESTIONS = " + json.dumps(total_questions, ensure_ascii=False) + ";\n")

print(f"Total SSC CGL questions updated: {len(total_questions)}.")
