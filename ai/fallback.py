import re


# ============================================================
# EduGenie Fallback Knowledge Base
# Works when Gemini is unavailable, overloaded, or quota-limited
# ============================================================

KNOWLEDGE_BASE = {

    # ========================================================
    # COMPUTER SCIENCE
    # ========================================================

    "ram": {
        "keywords": [
            "ram",
            "random access memory",
            "what is ram",
            "ram meaning",
            "ram na enna"
        ],
        "answer": """RAM stands for Random Access Memory.

RAM is the temporary memory used by a computer to store data and programs that are currently being used.

Key points:
• It is volatile memory.
• Data is lost when the computer is turned off.
• More RAM can help a computer handle multiple applications smoothly.
• RAM is faster than secondary storage such as HDDs and SSDs.

Example:
When you open a web browser, the operating system loads the required data into RAM so the CPU can access it quickly."""
    },

    "rom": {
        "keywords": [
            "rom",
            "read only memory",
            "what is rom",
            "rom meaning",
            "rom na enna"
        ],
        "answer": """ROM stands for Read-Only Memory.

ROM is non-volatile memory used to store important instructions that should remain available even when the device is powered off.

Key points:
• It is non-volatile.
• Data is retained when power is removed.
• It is commonly used for firmware and startup instructions.

Simple difference:
RAM → Temporary working memory
ROM → Persistent instructions or firmware storage"""
    },

    "cpu": {
        "keywords": [
            "cpu",
            "central processing unit",
            "processor",
            "what is cpu"
        ],
        "answer": """CPU stands for Central Processing Unit.

The CPU is the main processing component of a computer. It executes instructions and performs calculations.

The CPU commonly involves:
• Control Unit (CU)
• Arithmetic Logic Unit (ALU)
• Registers

Simple example:
When you run a program, the CPU processes the instructions required by that program."""
    },

    "operating_system": {
        "keywords": [
            "operating system",
            "what is os",
            "os meaning",
            "os in computer"
        ],
        "answer": """An Operating System (OS) is system software that manages computer hardware and provides services for applications.

Examples:
• Windows
• Linux
• macOS
• Android
• iOS

Main functions:
• Memory management
• Process management
• File management
• Device management
• Security
• User interface"""
    },

    "database": {
        "keywords": [
            "database",
            "what is database",
            "dbms",
            "database management system"
        ],
        "answer": """A database is an organized collection of data that can be stored, accessed, and managed efficiently.

DBMS stands for Database Management System.

Examples:
• MySQL
• PostgreSQL
• Oracle Database
• Microsoft SQL Server

Example:
A college database may contain student names, roll numbers, departments, subjects and attendance records."""
    },

    "sql": {
        "keywords": [
            "sql",
            "structured query language",
            "what is sql"
        ],
        "answer": """SQL stands for Structured Query Language.

SQL is used to communicate with relational databases.

Common SQL commands include:
• SELECT – retrieve data
• INSERT – add data
• UPDATE – modify data
• DELETE – remove data
• CREATE – create database objects

Example:
SELECT * FROM students;

This retrieves records from a students table."""
    },

    "python": {
        "keywords": [
            "python programming",
            "python language",
            "what is python",
            "python"
        ],
        "answer": """Python is a high-level, general-purpose programming language known for its readable syntax.

Python is widely used for:
• Web development
• Data analysis
• Artificial Intelligence
• Machine Learning
• Automation
• Scientific computing

Example:

print("Hello World")

This displays Hello World on the screen."""
    },

    "java": {
        "keywords": [
            "java programming",
            "java language",
            "what is java",
            "java"
        ],
        "answer": """Java is a high-level, object-oriented programming language.

Java is commonly used for:
• Enterprise applications
• Web applications
• Android development
• Backend systems
• Desktop applications

A major feature of Java is its JVM-based execution model, which helps Java applications run across different platforms."""
    },

    "html": {
        "keywords": [
            "html",
            "what is html",
            "html meaning",
            "hypertext markup language"
        ],
        "answer": """HTML stands for HyperText Markup Language.

HTML is used to structure content on web pages.

Common HTML elements include:
• <h1> – heading
• <p> – paragraph
• <img> – image
• <a> – link
• <button> – button
• <form> – form

HTML provides the structure of a webpage."""
    },

    "css": {
        "keywords": [
            "css",
            "what is css",
            "css meaning",
            "cascading style sheets"
        ],
        "answer": """CSS stands for Cascading Style Sheets.

CSS is used to control the appearance and layout of web pages.

CSS can control:
• Colors
• Fonts
• Spacing
• Borders
• Layouts
• Animations
• Responsive design

HTML provides structure, while CSS provides presentation and styling."""
    },

    "javascript": {
        "keywords": [
            "javascript",
            "java script",
            "what is javascript",
            "javascript meaning"
        ],
        "answer": """JavaScript is a programming language commonly used to make websites interactive.

It can be used for:
• Button interactions
• Form validation
• Dynamic content
• Animations
• API requests
• Web applications

HTML → Structure
CSS → Styling
JavaScript → Behavior and interaction"""
    },

    "artificial_intelligence": {
        "keywords": [
            "artificial intelligence",
            "what is ai",
            "ai meaning",
            "artificial intelligence meaning"
        ],
        "answer": """Artificial Intelligence (AI) is a field of computer science focused on creating systems that can perform tasks that normally require human intelligence.

Examples of AI applications:
• Voice assistants
• Image recognition
• Recommendation systems
• Chatbots
• Fraud detection
• Autonomous systems

AI can use techniques such as machine learning, deep learning and natural language processing."""
    },

    "machine_learning": {
        "keywords": [
            "machine learning",
            "what is machine learning",
            "ml meaning",
            "machine learning meaning"
        ],
        "answer": """Machine Learning (ML) is a branch of AI in which computer systems learn patterns from data and use those patterns to make predictions or decisions.

Common types include:
• Supervised learning
• Unsupervised learning
• Reinforcement learning

Example:
A model can learn from historical house prices and use the learned patterns to estimate prices for new houses."""
    },

    "deep_learning": {
        "keywords": [
            "deep learning",
            "what is deep learning",
            "deep learning meaning"
        ],
        "answer": """Deep Learning is a subfield of Machine Learning that uses multi-layer neural networks to learn patterns from data.

It is commonly used for:
• Image recognition
• Speech recognition
• Natural language processing
• Computer vision

Deep learning models generally require substantial amounts of data and computational resources."""
    },

    "data_structure": {
        "keywords": [
            "data structure",
            "data structures",
            "what is data structure"
        ],
        "answer": """A data structure is a way of organizing and storing data so that it can be accessed and modified efficiently.

Common data structures include:
• Array
• Linked List
• Stack
• Queue
• Tree
• Graph
• Hash Table

Choosing an appropriate data structure can improve the efficiency of a program."""
    },

    "algorithm": {
        "keywords": [
            "algorithm",
            "what is algorithm",
            "algorithm meaning"
        ],
        "answer": """An algorithm is a step-by-step procedure used to solve a problem or perform a task.

Example for finding the largest number:
1. Start with the first number.
2. Compare it with the next number.
3. Keep the larger value.
4. Continue until all numbers are checked.
5. The remaining largest value is the answer."""
    },

    "computer_network": {
        "keywords": [
            "computer network",
            "what is networking",
            "computer networking",
            "network"
        ],
        "answer": """A computer network is a group of connected devices that can communicate and share resources.

Examples:
• LAN – Local Area Network
• WAN – Wide Area Network
• MAN – Metropolitan Area Network

Networks can be used to share files, printers, applications and internet connections."""
    },

    "cloud_computing": {
        "keywords": [
            "cloud computing",
            "what is cloud computing",
            "cloud computing meaning"
        ],
        "answer": """Cloud computing means using computing resources such as servers, storage, databases and software over a network, commonly the internet.

Examples of cloud services include:
• Storage
• Virtual machines
• Databases
• Application hosting
• AI services

Popular cloud platforms include AWS, Microsoft Azure and Google Cloud."""
    },

    "cyber_security": {
        "keywords": [
            "cyber security",
            "cybersecurity",
            "what is cyber security",
            "computer security"
        ],
        "answer": """Cybersecurity is the practice of protecting computers, networks, applications and data from unauthorized access, attacks and other security threats.

Important concepts include:
• Authentication
• Authorization
• Encryption
• Firewalls
• Secure passwords
• Backup
• Security monitoring"""
    },

    # ========================================================
    # SCIENCE - PHYSICS
    # ========================================================

    "force": {
        "keywords": [
            "force",
            "what is force",
            "force in physics"
        ],
        "answer": """Force is a push or pull that can change the motion or shape of an object.

The SI unit of force is the Newton (N).

Newton's second law is:

F = m × a

where:
F = force
m = mass
a = acceleration"""
    },

    "gravity": {
        "keywords": [
            "gravity",
            "what is gravity",
            "gravitational force"
        ],
        "answer": """Gravity is the attractive force between objects that have mass.

On Earth, gravity pulls objects toward the Earth's center. It gives objects weight and causes unsupported objects to fall toward the ground.

Near Earth's surface, the acceleration due to gravity is approximately 9.8 m/s²."""
    },

    "energy": {
        "keywords": [
            "energy",
            "what is energy",
            "energy in physics"
        ],
        "answer": """Energy is the capacity to cause change or perform work.

Common forms of energy include:
• Kinetic energy
• Potential energy
• Thermal energy
• Chemical energy
• Electrical energy
• Light energy

Energy can be transformed from one form to another."""
    },

    "electricity": {
        "keywords": [
            "electricity",
            "what is electricity",
            "electric current"
        ],
        "answer": """Electricity involves electric charge and its movement or effects.

Electric current is the rate of flow of electric charge.

The SI unit of current is the Ampere (A).

Basic electrical quantities include:
• Voltage
• Current
• Resistance
• Power"""
    },

    "ohms_law": {
        "keywords": [
            "ohm's law",
            "ohms law",
            "ohm law"
        ],
        "answer": """Ohm's Law describes the relationship between voltage, current and resistance.

Formula:

V = I × R

where:
V = Voltage
I = Current
R = Resistance

If resistance remains constant, increasing voltage increases current."""
    },

    "light": {
        "keywords": [
            "light",
            "what is light",
            "properties of light"
        ],
        "answer": """Light is electromagnetic radiation that can be detected by the human eye.

Important properties of light include:
• Reflection
• Refraction
• Diffraction
• Interference

Light travels through vacuum at approximately 3 × 10⁸ metres per second."""
    },

    "sound": {
        "keywords": [
            "sound",
            "what is sound",
            "sound wave"
        ],
        "answer": """Sound is a mechanical wave produced by vibrations and requires a medium such as air, water or a solid to travel.

Sound cannot travel through a vacuum.

Important properties include:
• Frequency
• Amplitude
• Wavelength
• Speed"""
    },

    # ========================================================
    # SCIENCE - CHEMISTRY
    # ========================================================

    "atom": {
        "keywords": [
            "atom",
            "what is atom",
            "atomic structure"
        ],
        "answer": """An atom is the basic unit of an element that retains the chemical properties of that element.

An atom contains:
• Protons – positive charge
• Neutrons – no electric charge
• Electrons – negative charge

Protons and neutrons are found in the nucleus, while electrons occupy regions around the nucleus."""
    },

    "molecule": {
        "keywords": [
            "molecule",
            "what is molecule",
            "molecules"
        ],
        "answer": """A molecule is a group of two or more atoms chemically bonded together.

Examples:
• H₂O – water
• O₂ – oxygen
• CO₂ – carbon dioxide

Molecules can contain atoms of the same element or different elements."""
    },

    "element": {
        "keywords": [
            "chemical element",
            "what is an element",
            "element in chemistry"
        ],
        "answer": """A chemical element is a pure substance consisting of atoms with the same number of protons.

Examples:
• Hydrogen
• Oxygen
• Carbon
• Iron
• Gold

Each element has a unique atomic number."""
    },

    "acid_base": {
        "keywords": [
            "acid and base",
            "acid base",
            "what is acid",
            "what is base"
        ],
        "answer": """Acids and bases are important classes of chemical substances.

Generally:
• Acids donate hydrogen ions in aqueous solutions.
• Bases can accept hydrogen ions or produce hydroxide ions in aqueous solutions.

Examples:
Acid → Hydrochloric acid (HCl)
Base → Sodium hydroxide (NaOH)

The pH scale is commonly used to describe acidity or basicity."""
    },

    "ph": {
        "keywords": [
            "ph",
            "ph scale",
            "what is ph",
            "ph value"
        ],
        "answer": """pH is a measure commonly used to describe how acidic or basic an aqueous solution is.

A pH below 7 is generally acidic.
A pH of 7 is neutral at standard reference conditions.
A pH above 7 is generally basic or alkaline.

The pH scale is logarithmic."""
    },

    "periodic_table": {
        "keywords": [
            "periodic table",
            "what is periodic table",
            "periodic table meaning"
        ],
        "answer": """The periodic table is a systematic arrangement of chemical elements according to their atomic numbers and recurring chemical properties.

It contains:
• Periods – horizontal rows
• Groups – vertical columns

Elements in the same group often have related chemical properties."""
    },

    # ========================================================
    # SCIENCE - BIOLOGY
    # ========================================================

    "cell": {
        "keywords": [
            "cell",
            "what is cell",
            "cell in biology"
        ],
        "answer": """A cell is the basic structural and functional unit of living organisms.

Two major types are:
• Prokaryotic cells
• Eukaryotic cells

Important cell structures include:
• Cell membrane
• Cytoplasm
• Genetic material
• Ribosomes

Plant cells also contain structures such as a cell wall and chloroplasts."""
    },

    "photosynthesis": {
        "keywords": [
            "photosynthesis",
            "what is photosynthesis",
            "photosynthesis meaning"
        ],
        "answer": """Photosynthesis is the process by which green plants and some other organisms use light energy to make sugars from carbon dioxide and water.

A simplified representation is:

Carbon dioxide + Water + Light energy → Glucose + Oxygen

Chlorophyll plays an important role in capturing light energy."""
    },

    "respiration": {
        "keywords": [
            "respiration",
            "cellular respiration",
            "what is respiration"
        ],
        "answer": """Cellular respiration is a set of metabolic processes through which cells release usable energy from nutrients such as glucose.

In aerobic respiration, oxygen is used and carbon dioxide and water are produced as major products.

The released energy is captured largely in the form of ATP."""
    },

    "dna": {
        "keywords": [
            "dna",
            "what is dna",
            "dna meaning"
        ],
        "answer": """DNA stands for Deoxyribonucleic Acid.

DNA stores genetic information in living organisms.

DNA is made of nucleotides and has a double-helix structure. Its sequence contains information used in biological processes, including the production of proteins."""
    },

    "human_heart": {
        "keywords": [
            "heart",
            "human heart",
            "what is heart",
            "function of heart"
        ],
        "answer": """The human heart is a muscular organ that pumps blood through the circulatory system.

It has four chambers:
• Right atrium
• Right ventricle
• Left atrium
• Left ventricle

The right side mainly handles blood returning from the body, while the left side pumps oxygenated blood to the body."""
    },

    "blood": {
        "keywords": [
            "blood",
            "what is blood",
            "components of blood"
        ],
        "answer": """Blood is a connective tissue that circulates through the body.

Major components include:
• Red blood cells – transport oxygen
• White blood cells – participate in immune defense
• Platelets – help blood clot
• Plasma – liquid component that carries cells and dissolved substances"""
    },

    "plant": {
        "keywords": [
            "plant",
            "what is plant",
            "parts of plant",
            "plant biology"
        ],
        "answer": """Plants are living organisms that generally produce their own organic food through photosynthesis.

Common plant parts include:
• Roots – anchorage and absorption
• Stem – support and transport
• Leaves – major site of photosynthesis
• Flowers – involved in reproduction in flowering plants
• Fruits and seeds – involved in reproduction and dispersal"""
    },

    "ecosystem": {
        "keywords": [
            "ecosystem",
            "what is ecosystem",
            "ecosystem meaning"
        ],
        "answer": """An ecosystem is a community of living organisms interacting with each other and with their physical environment.

It includes:
• Producers
• Consumers
• Decomposers
• Non-living environmental factors

Examples include forests, ponds, grasslands and marine ecosystems."""
    },

    # ========================================================
    # ENVIRONMENT
    # ========================================================

    "pollution": {
        "keywords": [
            "pollution",
            "what is pollution",
            "environmental pollution"
        ],
        "answer": """Pollution is the introduction of harmful substances or forms of energy into the environment at levels that can cause undesirable effects.

Major types include:
• Air pollution
• Water pollution
• Soil pollution
• Noise pollution

Reducing pollution can involve cleaner technologies, waste management, conservation and responsible resource use."""
    },

    "climate_change": {
        "keywords": [
            "climate change",
            "what is climate change",
            "global warming"
        ],
        "answer": """Climate change refers to long-term changes in Earth's climate patterns.

Human activities, especially the emission of greenhouse gases, are a major driver of the current long-term warming trend.

Effects can include changes in temperature, precipitation patterns, sea level and ecosystems."""
    },

    # ========================================================
    # MATHEMATICS
    # ========================================================

    "algebra": {
        "keywords": [
            "algebra",
            "what is algebra",
            "algebra meaning"
        ],
        "answer": """Algebra is a branch of mathematics that uses symbols and variables to represent numbers and relationships.

Example:

2x + 5 = 15

Subtract 5:

2x = 10

Divide by 2:

x = 5"""
    },

    "percentage": {
        "keywords": [
            "percentage",
            "what is percentage",
            "percentage formula"
        ],
        "answer": """Percentage represents a value as a part of 100.

Basic formula:

Percentage = (Part / Whole) × 100

Example:

If 20 out of 50 students passed:

Percentage = (20 / 50) × 100
           = 40%"""
    },

    "probability": {
        "keywords": [
            "probability",
            "what is probability",
            "probability meaning"
        ],
        "answer": """Probability measures how likely an event is to occur.

For equally likely outcomes:

Probability = Number of favorable outcomes / Total number of possible outcomes

Probability values range from 0 to 1.

0 means impossible and 1 means certain."""
    },

    "statistics": {
        "keywords": [
            "statistics",
            "what is statistics",
            "statistics meaning"
        ],
        "answer": """Statistics is the study of collecting, organizing, analyzing, interpreting and presenting data.

Common concepts include:
• Mean
• Median
• Mode
• Range
• Variance
• Standard deviation

Statistics is widely used in science, business, engineering and data analysis."""
    },

    "mean_median_mode": {
        "keywords": [
            "mean median mode",
            "mean median",
            "median mode",
            "mean mode"
        ],
        "answer": """Mean, median and mode are common measures used to describe data.

Mean:
Sum of all values ÷ Number of values

Median:
The middle value after arranging data in order.

Mode:
The value that occurs most frequently.

Example:
Data = 2, 3, 3, 5, 7

Mean = 4
Median = 3
Mode = 3"""
    },

    "geometry": {
        "keywords": [
            "geometry",
            "what is geometry",
            "geometry meaning"
        ],
        "answer": """Geometry is the branch of mathematics that studies shapes, sizes, positions and properties of figures.

Common shapes include:
• Triangle
• Square
• Rectangle
• Circle
• Polygon

Important concepts include area, perimeter, angles, volume and geometric relationships."""
    },

    # ========================================================
    # GENERAL ACADEMIC
    # ========================================================

    "study_tips": {
        "keywords": [
            "study tips",
            "how to study",
            "study better",
            "how can i study",
            "exam preparation"
        ],
        "answer": """Here are some practical study tips:

1. Set a clear study goal.
2. Break large topics into smaller sections.
3. Study actively instead of only reading.
4. Practice with questions and problems.
5. Review difficult topics regularly.
6. Take short breaks during long study sessions.
7. Get enough sleep.
8. Use past papers or practice tests when available.

A consistent study routine is usually more useful than last-minute preparation."""
    },

    "hello": {
        "keywords": [
            "hello",
            "hi",
            "hey",
            "hai",
            "vanakkam"
        ],
        "answer": """Hello! 👋

Welcome to EduGenie.

I can help you with:
• Computer Science
• Programming
• AI & Machine Learning
• Physics
• Chemistry
• Biology
• Mathematics
• General academic topics

Ask me a question to get started!"""
    },

    "thank_you": {
        "keywords": [
            "thank you",
            "thanks",
            "thankyou",
            "thank u"
        ],
        "answer": """You're welcome! 😊

Keep learning and keep asking questions.

EduGenie is here to help you understand concepts step by step."""
    }
}


# ============================================================
# Normalize User Question
# ============================================================

def normalize_text(text):
    text = text.lower().strip()

    # Remove unnecessary punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove repeated spaces
    text = re.sub(r"\s+", " ", text)

    return text


# ============================================================
# Detect Topic
# ============================================================

def find_best_topic(question):
    question = normalize_text(question)

    best_topic = None
    best_score = 0

    for topic, data in KNOWLEDGE_BASE.items():

        score = 0

        for keyword in data["keywords"]:
            keyword = normalize_text(keyword)

            # Exact phrase match
            if keyword in question:
                score += len(keyword.split()) * 2

            # Individual word matching
            keyword_words = keyword.split()
            question_words = question.split()

            for word in keyword_words:
                if len(word) > 2 and word in question_words:
                    score += 1

        if score > best_score:
            best_score = score
            best_topic = topic

    return best_topic


# ============================================================
# Main Fallback Function
# ============================================================

def get_fallback_response(question: str) -> str:

    if not question:
        return (
            "Please enter a question. "
            "I can help you with Computer Science, Science, "
            "Mathematics and general academic topics."
        )

    topic = find_best_topic(question)

    if topic:
        return KNOWLEDGE_BASE[topic]["answer"]

    # Generic fallback when the exact topic is not available
    return """I’m currently using EduGenie’s fallback learning mode because Gemini AI is temporarily unavailable.

I can still answer many common academic questions related to:

💻 Computer Science
🔬 Physics
🧪 Chemistry
🧬 Biology
📐 Mathematics
🌱 Environment
🎓 General study topics

Try asking something like:

• What is RAM?
• What is ROM?
• What is photosynthesis?
• What is gravity?
• What is an atom?
• What is DNA?
• What is DBMS?
• What is Python?
• What is Machine Learning?
• What is probability?

For more advanced or topic-specific questions, Gemini AI will provide the detailed response when it is available."""