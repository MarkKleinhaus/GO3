"""
    This file is part of Gig-o-Matic
    Gig-o-Matic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from django.test import TestCase, RequestFactory
from .settings import LANGUAGES
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from graphene.test import Client
from go3.schema import schema
from gig.tests import GigTestBase


class LanguageTest(TestCase):
    def test_language(self):
        translation.activate("en-us")
        self.assertEqual(_("Schedule"), "Schedule")
        translation.activate("fr")
        self.assertEqual(_("Schedule"), "Liste des concerts ")


class GraphQLTest(GigTestBase):

    # test band queries
    def test_all_bands(self):
        client = Client(schema)
        executed = client.execute(
            """{ allBands {
            name,
            hometown
            } }"""
        )
        assert executed == {
            "data": {"allBands": [{"name": "test band", "hometown": "Seattle"}]}
        }

    def test_band_by_name(self):
        client = Client(schema)
        executed = client.execute(
            """{ bandByName(name:"test band") {
            name,
            hometown
            } }"""
        )
        assert executed == {
            "data": {"bandByName": {"name": "test band", "hometown": "Seattle"}}
        }

    # test member queries
    def test_all_members(self):
        client = Client(schema)
        executed = client.execute(
            """{ allMembers{
            email,
            username
            } }"""
        )
        assert executed == {
            "data": {
                "allMembers": [
                    {"email": "super@b.c", "username": ""},
                    {"email": "admin@e.f", "username": ""},
                    {"email": "joeuser@h.i", "username": ""},
                    {"email": "janeuser@k.l", "username": ""},
                ]
            }
        }

    def test_member_by_email(self):
        client = Client(schema)
        executed = client.execute(
            """{ memberByEmail(email:"joeuser@h.i") {
            email,
            username
            } }"""
        )
        assert executed == {
            "data": {"memberByEmail": {"email": "joeuser@h.i", "username": ""}}
        }