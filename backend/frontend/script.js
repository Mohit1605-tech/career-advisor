async function send() {
    const input = document.getElementById("input").value;
    const outputEl = document.getElementById("output");
    const button = document.querySelector("button");

    if (!input.trim()) {
        outputEl.innerText = "Please enter a prompt!";
        return;
    }

    button.disabled = true;
    outputEl.innerText = "Loading...";

    try {
        const res = await fetch("https://career-advisor-api.onrender.com/ask", ... {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: input })
        });

        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();
        outputEl.innerText = data.response || "No response received";
    } catch (error) {
        outputEl.innerText = `Error: ${error.message}`;
    } finally {
        button.disabled = false;
    }
}

async function analyzeResume() {
    const resume = document.getElementById("resume").value;
    const role = document.getElementById("role").value;

    if (!resume.trim() || !role.trim()) {
        alert("Please fill in both resume and role");
        return;
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/analyze_resume", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ resume, role })
        });

        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();

        // Display results with safe checks
        const skillsEl = document.getElementById("skills");
        const missingEl = document.getElementById("missing");
        const recsEl = document.getElementById("recommendations");

        skillsEl.innerText = (data.skills && data.skills.length > 0) 
            ? data.skills.join(", ") 
            : "No skills identified";

        missingEl.innerText = (data.missing_skills && data.missing_skills.length > 0) 
            ? data.missing_skills.join(", ") 
            : "No missing skills identified";

        recsEl.innerText = (data.recommendations && data.recommendations.length > 0) 
            ? data.recommendations.join("\n") 
            : "No recommendations available";

    } catch (error) {
        alert(`Error: ${error.message}`);
        document.getElementById("skills").innerText = "Error loading analysis";
        document.getElementById("missing").innerText = "Error loading analysis";
        document.getElementById("recommendations").innerText = "Error loading analysis";
    }
}