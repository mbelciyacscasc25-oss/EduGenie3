// ================================
// EduGenie Quiz System
// ================================

let questions = [];
let currentQuestion = 0;
let score = 0;
let selectedAnswer = null;
let questionCount = 5;
let selectedSubject = "";


// ================================
// FALLBACK QUESTION BANK
// ================================

const questionBank = {

    "Computer Science": [
        {
            question: "Which language is commonly used for web development?",
            options: ["Python", "HTML", "C", "Java"],
            answer: 1
        },
        {
            question: "What does CPU stand for?",
            options: [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Computer Processing Utility"
            ],
            answer: 0
        },
        {
            question: "Which data structure follows FIFO?",
            options: [
                "Stack",
                "Queue",
                "Tree",
                "Graph"
            ],
            answer: 1
        },
        {
            question: "Which language is primarily used for styling web pages?",
            options: [
                "HTML",
                "Python",
                "CSS",
                "SQL"
            ],
            answer: 2
        },
        {
            question: "What does DBMS stand for?",
            options: [
                "Database Management System",
                "Data Backup Management Software",
                "Database Machine System",
                "Data Management Service"
            ],
            answer: 0
        },
        {
            question: "Which of the following is an operating system?",
            options: [
                "MySQL",
                "Linux",
                "Python",
                "HTML"
            ],
            answer: 1
        },
        {
            question: "Which symbol is commonly used for comments in Python?",
            options: [
                "//",
                "#",
                "<!-- -->",
                "/* */"
            ],
            answer: 1
        },
        {
            question: "What is the full form of URL?",
            options: [
                "Uniform Resource Locator",
                "Universal Resource Link",
                "Uniform Reference Link",
                "User Resource Locator"
            ],
            answer: 0
        }
    ],


    "Mathematics": [
        {
            question: "What is 12 × 8?",
            options: ["86", "96", "108", "88"],
            answer: 1
        },
        {
            question: "What is the square root of 144?",
            options: ["10", "11", "12", "14"],
            answer: 2
        },
        {
            question: "What is 25% of 200?",
            options: ["25", "40", "50", "75"],
            answer: 2
        },
        {
            question: "What is the value of π approximately?",
            options: ["2.14", "3.14", "4.14", "1.14"],
            answer: 1
        },
        {
            question: "What is 15 + 27?",
            options: ["40", "41", "42", "43"],
            answer: 2
        },
        {
            question: "What is 9²?",
            options: ["18", "72", "81", "99"],
            answer: 2
        },
        {
            question: "A triangle has how many sides?",
            options: ["2", "3", "4", "5"],
            answer: 1
        },
        {
            question: "What is 100 ÷ 4?",
            options: ["20", "25", "30", "40"],
            answer: 1
        }
    ],


    "Physics": [
        {
            question: "What is the SI unit of force?",
            options: [
                "Joule",
                "Newton",
                "Watt",
                "Pascal"
            ],
            answer: 1
        },
        {
            question: "What is the approximate speed of light in vacuum?",
            options: [
                "3 × 10⁸ m/s",
                "3 × 10⁶ m/s",
                "3 × 10⁴ m/s",
                "3 × 10² m/s"
            ],
            answer: 0
        },
        {
            question: "Which force attracts objects toward Earth?",
            options: [
                "Friction",
                "Magnetic force",
                "Gravity",
                "Electric force"
            ],
            answer: 2
        },
        {
            question: "What is the SI unit of energy?",
            options: [
                "Newton",
                "Joule",
                "Watt",
                "Volt"
            ],
            answer: 1
        },
        {
            question: "Which instrument measures temperature?",
            options: [
                "Barometer",
                "Thermometer",
                "Ammeter",
                "Voltmeter"
            ],
            answer: 1
        },
        {
            question: "What is the SI unit of electric current?",
            options: [
                "Volt",
                "Ohm",
                "Ampere",
                "Watt"
            ],
            answer: 2
        },
        {
            question: "Which form of energy is stored in a stretched rubber band?",
            options: [
                "Kinetic energy",
                "Elastic potential energy",
                "Thermal energy",
                "Sound energy"
            ],
            answer: 1
        },
        {
            question: "Which law explains that every action has an equal and opposite reaction?",
            options: [
                "Newton's First Law",
                "Newton's Second Law",
                "Newton's Third Law",
                "Ohm's Law"
            ],
            answer: 2
        }
    ],


    "Chemistry": [
        {
            question: "What is the chemical symbol for oxygen?",
            options: ["O", "Ox", "C", "H"],
            answer: 0
        },
        {
            question: "What is the chemical formula of water?",
            options: ["CO₂", "H₂O", "O₂", "H₂"],
            answer: 1
        },
        {
            question: "What is the pH of pure water at room temperature?",
            options: ["5", "6", "7", "9"],
            answer: 2
        },
        {
            question: "Which gas is most abundant in Earth's atmosphere?",
            options: [
                "Oxygen",
                "Nitrogen",
                "Carbon dioxide",
                "Hydrogen"
            ],
            answer: 1
        },
        {
            question: "What is the smallest unit of an element?",
            options: [
                "Molecule",
                "Atom",
                "Cell",
                "Compound"
            ],
            answer: 1
        },
        {
            question: "Which substance is commonly known as table salt?",
            options: [
                "NaCl",
                "HCl",
                "KCl",
                "CaCO₃"
            ],
            answer: 0
        },
        {
            question: "Which particle has a negative charge?",
            options: [
                "Proton",
                "Neutron",
                "Electron",
                "Nucleus"
            ],
            answer: 2
        },
        {
            question: "Which gas is required for combustion?",
            options: [
                "Nitrogen",
                "Oxygen",
                "Helium",
                "Carbon dioxide"
            ],
            answer: 1
        }
    ],


    "Biology": [
        {
            question: "What is the basic unit of life?",
            options: [
                "Tissue",
                "Organ",
                "Cell",
                "Atom"
            ],
            answer: 2
        },
        {
            question: "Which organ pumps blood through the human body?",
            options: [
                "Lungs",
                "Brain",
                "Heart",
                "Kidney"
            ],
            answer: 2
        },
        {
            question: "Which organ is mainly responsible for breathing?",
            options: [
                "Heart",
                "Lungs",
                "Liver",
                "Stomach"
            ],
            answer: 1
        },
        {
            question: "Which part of a plant performs photosynthesis?",
            options: [
                "Root",
                "Stem",
                "Leaf",
                "Flower"
            ],
            answer: 2
        },
        {
            question: "What carries genetic information?",
            options: [
                "DNA",
                "Water",
                "Glucose",
                "Protein"
            ],
            answer: 0
        },
        {
            question: "Which blood cells help fight infections?",
            options: [
                "Red blood cells",
                "White blood cells",
                "Platelets",
                "Plasma"
            ],
            answer: 1
        },
        {
            question: "Which organ filters waste from the blood?",
            options: [
                "Heart",
                "Kidney",
                "Lung",
                "Brain"
            ],
            answer: 1
        },
        {
            question: "What is the green pigment in plants called?",
            options: [
                "Hemoglobin",
                "Chlorophyll",
                "Melanin",
                "Keratin"
            ],
            answer: 1
        }
    ],


    "General Science": [
        {
            question: "Which planet is known as the Red Planet?",
            options: [
                "Earth",
                "Venus",
                "Mars",
                "Jupiter"
            ],
            answer: 2
        },
        {
            question: "How many planets are in our Solar System?",
            options: ["7", "8", "9", "10"],
            answer: 1
        },
        {
            question: "What gas do humans need to breathe?",
            options: [
                "Carbon dioxide",
                "Nitrogen",
                "Oxygen",
                "Helium"
            ],
            answer: 2
        },
        {
            question: "Which is the largest planet in our Solar System?",
            options: [
                "Earth",
                "Saturn",
                "Jupiter",
                "Neptune"
            ],
            answer: 2
        },
        {
            question: "What is Earth's natural satellite?",
            options: [
                "Mars",
                "Moon",
                "Sun",
                "Venus"
            ],
            answer: 1
        },
        {
            question: "Which source provides most of Earth's energy?",
            options: [
                "Moon",
                "Sun",
                "Wind",
                "Coal"
            ],
            answer: 1
        },
        {
            question: "Which layer protects Earth from much of the Sun's UV radiation?",
            options: [
                "Ozone layer",
                "Cloud layer",
                "Crust",
                "Mantle"
            ],
            answer: 0
        },
        {
            question: "Water freezes at what temperature on the Celsius scale?",
            options: [
                "0°C",
                "10°C",
                "50°C",
                "100°C"
            ],
            answer: 0
        }
    ]

};


// ================================
// DOM ELEMENTS
// ================================

const quizIntro = document.getElementById("quizIntro");
const quizArea = document.getElementById("quizArea");
const resultArea = document.getElementById("resultArea");

const subjectSelect = document.getElementById("subjectSelect");
const startQuizBtn = document.getElementById("startQuizBtn");
const quizError = document.getElementById("quizError");

const questionText = document.getElementById("questionText");
const optionsContainer = document.getElementById("optionsContainer");

const questionNumber = document.getElementById("questionNumber");
const progressBar = document.getElementById("progressBar");

const currentSubject = document.getElementById("currentSubject");

const answerStatus = document.getElementById("answerStatus");
const nextBtn = document.getElementById("nextBtn");

const finalScore = document.getElementById("finalScore");
const totalQuestions = document.getElementById("totalQuestions");

const correctAnswers = document.getElementById("correctAnswers");
const wrongAnswers = document.getElementById("wrongAnswers");
const percentage = document.getElementById("percentage");

const retryBtn = document.getElementById("retryBtn");


// ================================
// QUESTION COUNT
// ================================

document.querySelectorAll(".count-option").forEach(button => {

    button.addEventListener("click", () => {

        document
            .querySelectorAll(".count-option")
            .forEach(item => item.classList.remove("active"));

        button.classList.add("active");

        questionCount = Number(
            button.dataset.count
        );
    });

});


// ================================
// START QUIZ
// ================================

startQuizBtn.addEventListener("click", startQuiz);


function startQuiz() {

    selectedSubject = subjectSelect.value;

    quizError.textContent = "";

    if (!selectedSubject) {

        quizError.textContent =
            "Please select a subject before starting the quiz.";

        return;
    }


    let bank = questionBank[selectedSubject] || [];

    if (bank.length === 0) {

        quizError.textContent =
            "Questions are not available for this subject yet.";

        return;
    }


    // Shuffle questions
    bank = [...bank].sort(
        () => Math.random() - 0.5
    );


    // Take required number
    questions = bank.slice(
        0,
        Math.min(questionCount, bank.length)
    );


    currentQuestion = 0;
    score = 0;
    selectedAnswer = null;


    currentSubject.textContent =
        selectedSubject;


    quizIntro.classList.add("hidden");

    resultArea.classList.add("hidden");

    quizArea.classList.remove("hidden");


    showQuestion();
}


// ================================
// SHOW QUESTION
// ================================

function showQuestion() {

    const question =
        questions[currentQuestion];


    selectedAnswer = null;

    nextBtn.disabled = true;

    answerStatus.textContent =
        "Select an answer";


    questionText.textContent =
        question.question;


    questionNumber.textContent =
        `Question ${currentQuestion + 1} of ${questions.length}`;


    const progress =
        ((currentQuestion + 1) / questions.length) * 100;

    progressBar.style.width =
        `${progress}%`;


    optionsContainer.innerHTML = "";


    const letters = [
        "A",
        "B",
        "C",
        "D"
    ];


    question.options.forEach(
        (optionText, index) => {

            const button =
                document.createElement("button");

            button.type = "button";

            button.className = "option";


            button.innerHTML = `
                <span class="option-letter">
                    ${letters[index]}
                </span>

                <span>
                    ${optionText}
                </span>
            `;


            button.addEventListener(
                "click",
                () => selectAnswer(index, button)
            );


            optionsContainer.appendChild(button);
        }
    );
}


// ================================
// SELECT ANSWER
// ================================

function selectAnswer(index, button) {

    if (selectedAnswer !== null) {
        return;
    }


    selectedAnswer = index;


    const question =
        questions[currentQuestion];


    const allOptions =
        document.querySelectorAll(".option");


    allOptions.forEach(option => {

        option.classList.add("disabled");

    });


    if (index === question.answer) {

        button.classList.add("correct");

        score++;

        answerStatus.textContent =
            "✓ Correct answer!";

    } else {

        button.classList.add("wrong");


        allOptions[
            question.answer
        ].classList.add("correct");


        answerStatus.textContent =
            "✗ Incorrect answer";

    }


    nextBtn.disabled = false;
}


// ================================
// NEXT QUESTION
// ================================

nextBtn.addEventListener(
    "click",
    nextQuestion
);


function nextQuestion() {

    if (selectedAnswer === null) {
        return;
    }


    currentQuestion++;


    if (currentQuestion >= questions.length) {

        showResult();

        return;
    }


    showQuestion();
}


// ================================
// RESULT
// ================================

function showResult() {

    quizArea.classList.add("hidden");

    resultArea.classList.remove("hidden");


    const total =
        questions.length;


    const wrong =
        total - score;


    const percent =
        Math.round(
            (score / total) * 100
        );


    // ================================
    // SHOW RESULT
    // ================================

    finalScore.textContent =
        score;


    totalQuestions.textContent =
        `/ ${total}`;


    correctAnswers.textContent =
        score;


    wrongAnswers.textContent =
        wrong;


    percentage.textContent =
        `${percent}%`;


    // ================================
    // SAVE QUIZ PROGRESS
    // ================================

    const history =
        JSON.parse(
            localStorage.getItem(
                "edugenieQuizHistory"
            ) || "[]"
        );


    const quizRecord = {

        subject: selectedSubject,

        score: score,

        total: total,

        percentage: percent,

        date: new Date().toLocaleString()

    };


    history.push(quizRecord);


    // Keep latest 50 quizzes only

    if (history.length > 50) {

        history.shift();

    }


    localStorage.setItem(
        "edugenieQuizHistory",
        JSON.stringify(history)
    );

}


// ================================
// RETRY QUIZ
// ================================

retryBtn.addEventListener(
    "click",
    () => {

        resultArea.classList.add("hidden");

        quizIntro.classList.remove("hidden");

        quizError.textContent = "";

    }
);