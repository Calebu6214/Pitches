from app import create_app, db
from flask_script import Manager, Server
from app.models import User,Category,Post,Comment
from flask_migrate import Migrate, MigrateCommand
# from flask_module import Module
# from databases import models
# from flask.ext.mail import Message
# from flask.ext.script import Manager

# Creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    Run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    '''
    Function that allows us to pass properties into the shell context.
    '''
    return dict(app=app, db=db, User=User, Category=Category, Comment=Comment,Post = Post)

if __name__ == '__main__':
    manager.run()