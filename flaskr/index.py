import functools
import requests
from .query_set import *
from SPARQLWrapper import SPARQLWrapper, JSON
import sys
import json

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
    param_0 = request.args.get('param0')
    param_1 = request.args.get('param1')
    param_2 = request.args.get('param2')
    print(question_id)
    sparql_endpoint = 'http://127.0.0.1:3030/kde/query'
    sparql = SPARQLWrapper(sparql_endpoint)
    query = getattr(sys.modules[__name__], "generate_q%s_query" % question_id)(param_0, param_1, param_2)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    response = sparql.query().convert()

    labels = response['head']['vars']
    data = response['results']['bindings']

    chart_labels = list()
    chart_data = list()

    if question_id == '8':
        for row in data:
            chart_labels.append(row['UNIVERSITY_NAME']['value'])
            chart_data.append(int(row['NOBEL_LAUREATE_COUNT']['value']))

    return render_template('index.html', data=data, labels=labels, active_query=int(question_id), chart_labels=chart_labels, chart_data=chart_data, query=query)
