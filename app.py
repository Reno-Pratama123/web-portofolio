from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Muhammad Reno Abdi Pratama",
    "title": "Universitas Negeri Surabaya | Sistem Informasi",
    "description": "Saya adalah mahasiswa yang tertarik dengan teknologi dan pengembangan website.",
    "email": "renoabdim@gmail.com",
    "location": "Indonesia Jawa Timur Surabaya",
}

skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "Python",
    "Flask"
]

experiences = [
    {
        "title": "Mahasiswa Sistem Informasi",
        "place": "Universitas Negeri Surabaya",
        "year": "2026",
        "description": "lajar pemrograman dan pengembangan aplikasi web."
    }
]

projects = [
    {
        "title": "Website Portfolio",
        "description": "Website pribadi untuk menampilkan profil, kemampuan, dan proyek.",
        "tech": "Python, Flask, HTML, CSS"
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        experiences=experiences,
        projects=projects
    )


if __name__ == "__main__":
    app.run(debug=True)
