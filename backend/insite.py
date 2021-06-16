from app import create_app
import os


# Flask App Setup
if os.getenv('FLASK_CONFIG') is not None:
    app = create_app(os.getenv('FLASK_CONFIG'))
else:
    app = create_app('dev')


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
