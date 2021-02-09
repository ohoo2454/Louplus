#!usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_pymongo import PyMongo

mongo = PyMongo()


def init(app):
	global mongo

	mongo = PyMongo(app)
