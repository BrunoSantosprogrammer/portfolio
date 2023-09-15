import pytest

from projects.factories import ProjectFactory

@pytest.fixture
def project_published():
    return ProjectFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_project(project_published):
    assert project_published.title == 'pytest with factory'