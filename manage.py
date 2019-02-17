from flask_script import Manager
from utils import create_app
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'city360.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
# manager = Manager(app=app)
db = SQLAlchemy(app)


class User(db.Model):
    # 定义一个数据表格
    # User数据表格 存储个人信息
    id = db.Column(db.Integer, primary_key=True)
    userIdentity = db.Column(db.String(10))
    openid = db.Column(db.String(20))
    avatarUrl = db.Column(db.String(20))
    nickName = db.Column(db.String(20))
    ownedProjects = db.Column(db.Text)
    participatedProjects = db.Column(db.Text)


    def __init__(self, openid, userIdentity, avatarUrl, nickName, ownedProjects, participatedProjects):
        self.avatarUrl = avatarUrl
        self.useuserIdentity = userIdentity
        self.openid = openid
        self.nickName = nickName
        self.ownedProjects = ownedProjects
        self.participatedProjects = participatedProjects

    def __repr__(self):
        return '<User %r>' % self.avatarUrl


class Project(db.Model):
    # 定义Project表格 存储项目信息
    id = db.Column(db.Integer, primary_key=True)
    projectName = db.Column(db.String(20))
    creatorOpenid = db.Column(db.String(20))
    workersOpenid = db.Column(db.Text)
    workersNumber = db.Column(db.Integer)
    projectStatus = db.Column(db.String(20))
    mainProject = db.Column(db.Boolean)

    def __init__(self,
                 projectName="",
                 creatorOpenid="",
                 workersOpenid="",
                 workersNumber=0,
                 projectStatus="",
                 mainProject=False):
        self.projectName = projectName
        self.creatorOpenid = creatorOpenid
        self.workersOpenid = workersOpenid
        self.workersNumber = workersNumber
        self.projectStatus = projectStatus
        self.mainPRoject = mainProject

    def __repr__(self):
        return '<Project %r>' % self.id


def db_init():
    db.create_all()


if __name__ == '__main__':
    # db_init()
    print(User)
    app.run(port=5000)
