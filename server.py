from flask import Flask, render_template, redirect, url_for
from forms import TeamForm, ProjectForm
from model import db, User, Team, Project, connect_to_db

app = Flask(__name__)
user_id = 1

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def home():
    team_form = TeamForm()
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)

    return render_template('index.html', team_form=team_form, project_form=project_form)



@app.route("/add-team", methods=["POST"])
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        team_name = team_form.team_name.data
        new_team = Team(team_name, user_id)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))
    

@app.route("/add-project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)

    if project_form.validate_on_submit():
        project_name = project_form.project_name.data
        project_complete = project_form.completed.data
        team_id = project_form.team_id.data
        project_desc = project_form.description.data

        new_project = Project(project_name, project_complete, team_id, project_desc)
        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return redirect(url_for("home"))



if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)

