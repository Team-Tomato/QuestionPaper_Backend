from flask import Flask, jsonify
from github import Github
import os,requests,json

app = Flask(__name__)
g = Github()
# An API to show the sum of commits,pr's and contributors of Team-Tomato
@app.route('/get_total')
def total():
    commits = 0
    pulls = 0
    conts = 0
    a = requests.get("https://api.github.com/users/Team-Tomato/repos")
    y = json.loads(a.text)
    for i in y:
        repository = "Team-Tomato/{}".format(i["name"])
        repo = g.get_repo(repository)
        pulls += repo.get_pulls().totalCount
        commits += repo.get_commits().totalCount
        conts += repo.get_contributors().totalCount
    lst = []
    lst.append(dict([("Name: ", "Team-Tomato"), ("Pull Requests: ", pulls), ("Commits: ", commits), ("Contributors: ", conts)]))
    return jsonify(lst)

if __name__ == '__main__':
    app.run()