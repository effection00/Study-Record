import json
from flask import url_for
from twit_app.models.user_model import User

def test_app_is_running(client):
    res = client.get(url_for('main.index'))
    assert res.status_code == 200


class TestMainRoutes:
    def test_index_page(self, client):
        res = client.get(url_for('main.index'))

        assert res.status_code == 200

    def test_compare_page(self, client):
        res = client.get(url_for('main.compare_index'))

        assert res.status_code == 200

    def test_user_page(self, client):
        res = client.get(url_for('main.user_index'))

        assert res.status_code == 200


class TestUserRoutes:
    def test_add_user(self, client, db_session):
        db = db_session
        session = db.session
        test_user = {
            'username':'spongebob',
            'full_name':'sponge bob',
            'followers':52
        }
        
        user = User(
            username=test_user['username'],
            full_name=test_user['full_name'],
            followers=test_user['followers']
        )

        # normal user addition
        res = client.post(url_for('user.add_user'), data=test_user)

        assert res.status_code == 200

        # username not given
        res = client.post(url_for('user.add_user'))

        assert res.status_code == 400

        # username doesn't exist on twitter
        no_user = {
            'username':'mitmitLalaTaihiti'
        }
        res = client.post(url_for('user.add_user'), data=no_user)

        assert res.status_code == 400

    def test_delete_user(self, client, db_session):
        db = db_session
        session = db.session

        test_user = {
            'username':'spongebob',
            'full_name':'sponge bob',
            'followers':52
        }
        
        user = User(
            username=test_user['username'],
            full_name=test_user['full_name'],
            followers=test_user['followers']
        )

        session.add(user)
        session.commit()

        # normal deletion
        res = client.get(url_for('user.delete_user', user_id=1))

        assert res.status_code == 200

        # user_id not given
        res = client.get(url_for('user.delete_user'))

        assert res.status_code == 400
        
        # user_id given but user doesn't exist
        res = client.get(url_for('user.delete_user', user_id=100))
        assert res.status_code == 404

