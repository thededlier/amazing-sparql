import functools
import requests
from .query_set import *
from SPARQLWrapper import SPARQLWrapper, JSON
import sys

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@bp.route('/query/', methods=["GET"])
def query():
    question_id = request.args.get('q_id')
    print(question_id)
    sparql_endpoint = 'http://127.0.0.1:3030/kde/query'
    sparql = SPARQLWrapper(sparql_endpoint)
    query = getattr(sys.modules[__name__], "generate_q%s_query" % question_id)()
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    response = sparql.query().convert()

    labels = response['head']['vars']
    data = response['results']['bindings']
    return render_template('index.html', data=data, labels=labels)
