// ================================
// EduGenie Progress System
// ================================

document.addEventListener("DOMContentLoaded", () => {

    loadProgress();

});


// ================================
// LOAD PROGRESS
// ================================

function loadProgress() {

    const history =
        JSON.parse(
            localStorage.getItem("edugenieQuizHistory") || "[]"
        );


    // Elements

    const quizCount =
        document.getElementById("quizCount");

    const averageScore =
        document.getElementById("averageScore");

    const bestScore =
        document.getElementById("bestScore");

    const subjectPerformance =
        document.getElementById("subjectPerformance");

    const recentQuizzes =
        document.getElementById("recentQuizzes");

    const emptyProgress =
        document.getElementById("emptyProgress");


    // ================================
    // NO DATA
    // ================================

    if (history.length === 0) {

        quizCount.textContent = "0";

        averageScore.textContent = "0%";

        bestScore.textContent = "0%";

        subjectPerformance.innerHTML = "";

        recentQuizzes.innerHTML = "";

        emptyProgress.style.display = "block";

        return;
    }


    emptyProgress.style.display = "none";


    // ================================
    // QUIZ COUNT
    // ================================

    quizCount.textContent =
        history.length;


    // ================================
    // AVERAGE SCORE
    // ================================

    const totalPercentage =
        history.reduce(
            (sum, quiz) =>
                sum + Number(quiz.percentage || 0),
            0
        );


    const average =
        Math.round(
            totalPercentage / history.length
        );


    averageScore.textContent =
        `${average}%`;


    // ================================
    // BEST SCORE
    // ================================

    const best =
        Math.max(
            ...history.map(
                quiz =>
                    Number(quiz.percentage || 0)
            )
        );


    bestScore.textContent =
        `${best}%`;


    // ================================
    // SUBJECT PERFORMANCE
    // ================================

    const subjects = {};


    history.forEach(quiz => {

        const subject =
            quiz.subject || "General Science";


        if (!subjects[subject]) {

            subjects[subject] = {
                total: 0,
                count: 0
            };

        }


        subjects[subject].total +=
            Number(quiz.percentage || 0);


        subjects[subject].count++;

    });


    subjectPerformance.innerHTML = "";


    Object.keys(subjects).forEach(subject => {

        const averageSubject =
            Math.round(
                subjects[subject].total /
                subjects[subject].count
            );


        const row =
            document.createElement("div");

        row.className =
            "subject-row";


        row.innerHTML = `
            <div class="subject-info">

                <span class="subject-name">
                    ${getSubjectIcon(subject)}
                    ${escapeHTML(subject)}
                </span>

                <span class="subject-score">
                    ${averageSubject}%
                </span>

            </div>

            <div class="subject-bar">

                <div
                    class="subject-fill"
                    style="width: ${averageSubject}%">
                </div>

            </div>
        `;


        subjectPerformance.appendChild(row);

    });


    // ================================
    // RECENT QUIZZES
    // ================================

    recentQuizzes.innerHTML = "";


    const recent =
        [...history]
            .reverse()
            .slice(0, 5);


    recent.forEach(quiz => {

        const item =
            document.createElement("div");

        item.className =
            "recent-item";


        const date =
            quiz.date || "Recently";


        item.innerHTML = `
            <div class="recent-left">

                <div class="recent-icon">
                    ${getSubjectIcon(
                        quiz.subject
                    )}
                </div>

                <div>

                    <div class="recent-subject">
                        ${escapeHTML(
                            quiz.subject ||
                            "Quiz"
                        )}
                    </div>

                    <div class="recent-date">
                        ${escapeHTML(date)}
                    </div>

                </div>

            </div>

            <div class="recent-score">
                ${Number(
                    quiz.percentage || 0
                )}%
            </div>
        `;


        recentQuizzes.appendChild(item);

    });

}


// ================================
// SUBJECT ICON
// ================================

function getSubjectIcon(subject) {

    const icons = {

        "Computer Science": "💻",

        "Mathematics": "📐",

        "Physics": "⚡",

        "Chemistry": "🧪",

        "Biology": "🌱",

        "General Science": "🔬"

    };


    return icons[subject] || "📚";

}


// ================================
// HTML SAFETY
// ================================

function escapeHTML(value) {

    return String(value)

        .replace(/&/g, "&amp;")

        .replace(/</g, "&lt;")

        .replace(/>/g, "&gt;")

        .replace(/"/g, "&quot;")

        .replace(/'/g, "&#039;");

}