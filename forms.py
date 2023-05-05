from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('team name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField('submit')


class ProjectForm(FlaskForm):
    project_name = StringField('project name', validators=[DataRequired(), Length(min=4, max=255)])
    description = StringField('description', validators=[Length(max=255)])
    completed = BooleanField('completed?')
    team_id = SelectField('team id', validators=[DataRequired()], choices=[1,2])
    submit = SubmitField('submit')

    def update_teams(self, teams):
        self.team_id.choices = [(team.id, team.team_name) for team in teams]
