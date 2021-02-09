#!usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
from flask import jsonify


class ResponseCode():

	OK = 0
	ERROR = 1
	NOT_FOUND = 10
	TRANSACTION_FAILURE = 20
	QUANTITY_EXCEEDS_LIMIT = 30
	NO_ENOUGH_MONEY = 40

	MESSAGES = {
	    OK: 'successfully',
	    ERROR: 'unknown error',
	    NOT_FOUND: 'resource not found',
	    TRANSACTION_FAILURE: 'transaction failure',
	    QUANTITY_EXCEEDS_LIMIT: 'quantity exceeds limit',
	    NO_ENOUGH_MONEY: 'no enough money'
	}


def json_response(code=ResponseCode.OK, message='', **kwargs):
	return jsonify({
        'code': code,
        'message': message or ResponseCode.MESSAGES.get(code, ''),
        'data': kwargs
	})


def handle_error_json(exception):
	traceback.print_exc()

	return json_response(ResponseCode.ERROR, str(exception))
