import pytest
from contextlib import contextmanager
import shlex
import os
import subprocess
import datetime
from cookiecutter.utils import rmtree


@pytest.fixture
def default_extra_context():
    extra_context = {
        'full_name': 'Kotti devel',
        'email': 'kotti@googlegroups.com'}
    return extra_context.copy()


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its
                    temporalfiles will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_fullname_license_file(cookies, default_extra_context):
    with bake_in_temp_dir(
            cookies,
            extra_context=default_extra_context) as result:
        license_file_path = result.project.join('LICENSE.txt')
        assert 'kotti_addon' in license_file_path.read()


@pytest.mark.parametrize('file_path', [
    ('kotti_addon', 'views', 'view.py'),
    ('kotti_addon', 'views', 'edit.py'),
    ('kotti_addon', 'views', '__init__.py'),
    ('kotti_addon', 'fanstatic.py',),
    ('kotti_addon', 'resources.py',),
    ('kotti_addon', '__init__.py',),
    ('kotti_addon', 'tests', 'test_functional.py',),
    ('kotti_addon', 'tests', 'test_view.py',),
    ('kotti_addon', 'tests', 'test_resources.py',),
    ('kotti_addon', 'tests', 'conftest.py',),
])
def test_date_python_files(cookies, file_path, default_extra_context):
    with bake_in_temp_dir(
            cookies,
            extra_context=default_extra_context) as result:
        today_iso = datetime.date.today().isoformat()
        computed_file = result.project.join(*file_path)
        assert today_iso in computed_file.read()


@pytest.mark.parametrize('file_path', [
    ('kotti_addon', 'views', 'view.py'),
    ('kotti_addon', 'views', 'edit.py'),
    ('kotti_addon', 'views', '__init__.py'),
    ('kotti_addon', 'fanstatic.py',),
    ('kotti_addon', 'resources.py',),
    ('kotti_addon', '__init__.py',),
    ('kotti_addon', 'tests', 'test_functional.py',),
    ('kotti_addon', 'tests', 'test_view.py',),
    ('kotti_addon', 'tests', 'test_resources.py',),
    ('kotti_addon', 'tests', 'conftest.py',),
])
def test_author_python_files(cookies, file_path, default_extra_context):
    with bake_in_temp_dir(
            cookies,
            extra_context=default_extra_context) as result:
        computed_file = result.project.join(*file_path)
        assert "{0} ({1})".format(
            default_extra_context['full_name'],
            default_extra_context['email']) in computed_file.read()


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'pytest.ini' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files

        found_secondlevel_files = [
            subitem.basename for subitem in
            [item for item in result.project.visit(
             'kotti_addon')][0].listdir()]
        assert 'tests' in found_secondlevel_files
        assert '__init__.py' in found_secondlevel_files
        assert 'fanstatic.py' in found_secondlevel_files
        assert 'resources.py' in found_secondlevel_files


def test_bake_and_run_tests(cookies, default_extra_context):
    extra_context = default_extra_context.copy()
    with bake_in_temp_dir(
            cookies,
            extra_context=extra_context) as result:
        assert result.project.isdir()
        run_inside_dir(
            'tox',
            str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))
