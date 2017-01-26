import os
from app import create_app, db
from app.models.Models import User, Role, Permission, Post, Follow, Comment
from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager, Server, Shell


#app = create_app('development')
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role,
                Permission=Permission, Post=Post, Follow=Follow, Comment=Comment)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def runServer():
    server = Server(host='0.0.0.0', port=9000)
    manager.add_command("runserver", server)


app.config['DEBUG']=True

if __name__ == '__main__':
    manager.run()

