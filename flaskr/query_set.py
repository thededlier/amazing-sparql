# Number of nobel laureate per country
def generate_q1_query():
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

# ResearchRating of a university which has a nobel laureates affiliated to it, in year 2016
def generate_q2_query():
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

# University ranking to which a nobel laureate is affiliated to in 2016
def generate_q3_query():
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
