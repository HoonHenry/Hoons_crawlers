from flask import Flask, render_template, request, redirect, send_file
from webpage.scrapper_so import get_jobs as so_jobs
from webpage.scrapper_indeed import get_jobs as ind_jobs
from webpage.exporter import save_to_file


app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = ind_jobs(word) + so_jobs(word)
            db[word] = jobs
    else:
        redirect("/")
    return render_template("report.html", searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)


@app.route("/jobs.csv")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")
