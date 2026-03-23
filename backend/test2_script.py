res = """Skills:
- - Python
- JavaScript

Missing Skills:
- All core skills present!"""

lines = res.split("\n")
mode = None
skills = []
missing = []

for line in lines:
    line = line.strip()
    print(f"[{mode}] LINE: {repr(line)}")
    if "Skills:" in line:
        mode = "skills"
        continue
    if "Missing Skills:" in line:
        mode = "missing"
        continue
    if line.startswith("-"):
        if mode == "skills":
            skills.append(line.replace("-", "").strip())
        elif mode == "missing":
            missing.append(line.replace("-", "").strip())

print({'skills': skills, 'missing': missing})
