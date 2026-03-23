async function send() {
    const input = document.getElementById("input").value;
    const outputEl = document.getElementById("output");
    const button = document.querySelector(".card:nth-child(1) button");

    if (!input.trim()) {
        outputEl.innerText = "Please enter a prompt!";
        return;
    }

    button.disabled = true;
    button.innerHTML = '<span class="loading"></span>Loading...';

    try {
        const res = await fetch("/ask", {
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
        button.innerText = "Ask AI";
    }
}

async function analyzeResume() {
    const resumeFile = document.getElementById("resumeFile").files[0];
    const role = document.getElementById("role").value;
    const button = document.querySelector(".card:nth-child(2) button");

    if (!resumeFile) {
        alert("Please select a resume file");
        return;
    }

    if (!role.trim()) {
        alert("Please fill in the target role");
        return;
    }

    // Read the file content
    const resume = await resumeFile.text();

    button.disabled = true;
    button.innerHTML = '<span class="loading"></span>Analyzing...';

    try {
        const res = await fetch("/analyze_resume", {
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
    } finally {
        button.disabled = false;
        button.innerText = "Analyze Resume";
    }
}