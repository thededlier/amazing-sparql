# 1. Number of nobel laureate per country
def generate_q1_query(param_0, param_1, param_2):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>
        PREFIX ex: <http://example.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT  (SAMPLE(?univname) AS ?UNIVERSITY) (SAMPLE(?ranking) AS ?RANK)
        WHERE {
            ?laureate exont:affiliated_to_university ?college.
            ?university dbo:name ?univname
            FILTER ( regex (str(?college), str(?univname), "i") ).
            ?university exont:has_rank ?rank.
            ?rank exont:world_rank ?ranking.
        }GROUP BY ?univname ?ranking
    """
    return query

# 2. University ranking to which a nobel laureate is affiliated to in 2016
def generate_q2_query(param_0, param_1, param_2):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>
        PREFIX ex: <http://example.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT  (SAMPLE(?univname) AS ?UNIVERSITY) (SAMPLE(?ranking) AS ?RANK)
        WHERE {
            ?laureate exont:affiliated_to_university ?college.
            ?university dbo:name ?univname
            FILTER ( regex (str(?college), str(?univname), "i") ).
            ?university exont:has_rank ?rank.
            ?rank exont:world_rank ?ranking.
        }GROUP BY ?univname ?ranking
    """

    return query

# 3. Statistic of country for top n universities in the world in 2016
def generate_q3_query(param_0, param_1, param_2):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>
        PREFIX ex: <http://example.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT  (SAMPLE(?univname) AS ?UNIVERSITY) (SAMPLE(?ranking) AS ?RANK)
        WHERE {
            ?laureate exont:affiliated_to_university ?college.
            ?university dbo:name ?univname
            FILTER ( regex (str(?college), str(?univname), "i") ).
            ?university exont:has_rank ?rank.
            ?rank exont:world_rank ?ranking.
        }GROUP BY ?univname ?ranking
    """

    return query

# 4. number of nobel prize winning papers for a country
def generate_q4_query(param_0, param_1, param_2):
    query = """

    """

    return query

# ratio of enrollment to primary vs students in university in 2016 for a country
def generate_q5_query(param_0, param_1, param_2):
    query = """

    """

    return query


# 6. ResearchRating of a university which has a nobel laureates affiliated to it, in year 2016
def generate_q6_query(param_0, param_1, param_2):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>
        PREFIX ex: <http://example.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>


        SELECT  (SAMPLE(?univname) AS ?UNIVERSITY) (SAMPLE(?rating) AS ?RESEARCH_RATING)
        WHERE {
            ?laureate exont:affiliated_to_university ?college.
            ?university dbo:name ?univname
            FILTER ( regex (str(?college), str(?univname), "i") ).
            ?university exont:has_rank ?rank.
            ?rank exont:defined_by ?params.
            ?params exont:research_rating ?rating.
        }GROUP BY ?univname ?rating
    """

    return query


# 7. Country of a nobel laureate
def generate_q7_query(param_0, param_1, param_2):
    query = """

    """

    return query

# 8. GDP & Gold Medals of a country in the year 2000
def generate_q8_query(param_0, param_1, param_2):
    query = """

    """

    return query

# 9. Total number of Gold medals won by a country in the toughest sport
def generate_q9_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        SELECT COUNT(?athlete)
        WHERE {
            ?country dbo:name "%s".  ?country exont:country_code ?countryCode.
            ?subject exont:difficulty_level 1.
            ?subject dbo:name ?sportname.
            ?discipline exont:has_sport_discipline ?sportname.
            ?athlete exont:participated_in ?discipline.
            ?athlete exont:country_code ?countryCode.
            ?athlete exont:medal_won "Gold".
        }
    """ % param_0
    return query

# 10. Male Female ratio of olympic winners in toughest sport between 2000-2008 (This can be converted to a Pie Chart showing the ratio of first 5 toughest sports)
def generate_q10_query(params):
    query = """

    """

    return query
