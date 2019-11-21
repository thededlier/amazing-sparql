# 1. Get names of Nobel laureates for given country
# Inputs: Country
def generate_q1_query(param_0, param_1, param_2):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>
        PREFIX ex: <http://example.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        SELECT (UCASE(?laureateUniversityName) AS ?UNIVERSITY) (UCASE(?laureateName) AS ?LAUREATE_NAME)
        WHERE {
          	?country dbo:name '%s'.
            ?university exont:situatedIn ?country.
            ?university exont:universityName ?universityname.
            ?laureate exont:affiliatedToUniversity ?univ.
            ?univ exont:universityName ?laureateUniversityName.
            FILTER ( regex (str(?universityname), str(?laureateUniversityName), "i") ).
            ?laureate foaf:name ?laureateName
        }
    """ % (param_0)
    return query

# 2. University ranking to which a Nobel laureate is affiliated to in 2016
# INPUT: Laureate Name
def generate_q2_query(param_0, param_1, param_2):
    query = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>
        PREFIX ex: <http://example.org/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        select (UCASE(?laureateUniversityName) AS ?UNIVERSITY_NAME) (?universityRank AS ?WORLD_RANKING)

        where
        {
        	?laureate  foaf:name '%s'.
            ?laureate exont:affiliatedToUniversity ?laureateUniversity.
            ?laureateUniversity exont:universityName ?laureateUniversityName.
            ?university exont:situatedIn ?country.
            ?university exont:universityName ?universityname.
            FILTER ( regex (str(?universityname), str(?laureateUniversityName), "i") ).
            ?university exont:hasRank ?universityRankObj.
            ?universityRankObj exont:worldRank ?universityRank
        }
    """ % (param_0)

    return query

# 3. Titles of nobel prize winning papers for a country
# INPUT: Country
def generate_q3_query(param_0, param_1, param_2):
    query = """
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>

        SELECT (UCASE(?laureateUnivName) AS ?UNIVERSITY_NAME) (UCASE(?researchPaperTitle) AS ?PAPER_TITLE)
        WHERE {
          	?country dbo:name '%s'.
            ?university exont:situatedIn ?country.
            ?university exont:universityName ?universityname.
            ?laureate exont:affiliatedToUniversity ?univ.
            ?univ exont:universityName ?laureateUnivName.
            FILTER ( regex (str(?universityname), str(?laureateUnivName), "i") ).
            ?laureate exont:hasPublished ?researchPaper.
            ?researchPaper dbo:title ?researchPaperTitle
        }
    """ % (param_0)

    return query

# 4. Ratio of students in university vs population of the country in 2016
# INPUT Country
def generate_q4_query(param_0, param_1, param_2):
    query = """
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX exont: <http://example.org/ontology/>

        SELECT (?universityname AS ?UNIVERSITY_NAME) (?numberOfStudents AS ?TOTAL_NO_OF_STUDENTS) (?populationCount AS ?TOTAL_POPULATION)

        WHERE {
          	?country dbo:name '%s'.
            ?university exont:situatedIn ?country.
            ?university exont:universityName ?universityname.
            ?university exont:hasRank ?universityRankObj.
            ?universityRankObj exont:worldRank ?universityWorldRank.
            ?universityRankObj exont:definedBy ?universityRankingParams.
            ?universityRankingParams exont:numberOfStudents ?numberOfStudents.
        		{

          			SELECT ?populationCount
        					WHERE {
         							?country dbo:name '%s'.
          							?country exont:developmentIndicator ?devParam.
          							?devParam exont:statName 'Population, total'.
          							?devParam exont:statYear 2016.
          							?devParam exont:statValue ?populationCount.
        							}
          		}
        }ORDER BY DESC (?numberOfStudents)
    """ % (param_0, param_0)

    return query

# 5. Research rating of a university which has a Nobel laureates affiliated to it, in year 2016
# INPUT: Laureate names
def generate_q5_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>

        SELECT (?laureateUniversityName AS ?UNIVERSITY_NAME) (?universityCountry AS ?UNIVERSITY_SITUATED_IN) (?researchRating AS ?RESEARCH_RATING)
        WHERE
        {
          	?laureate  foaf:name '%s'.
            ?laureate exont:affiliatedToUniversity ?laureateUniversity.
            ?laureateUniversity exont:universityName ?laureateUniversityName.
            ?university exont:situatedIn ?countryObj.
            ?countryObj dbo:name ?universityCountry.
            ?university exont:universityName ?universityname.
            FILTER ( regex (str(?universityname), str(?laureateUniversityName), "i") ).
            ?university exont:hasRank ?universityRankObj.
            ?universityRankObj exont:definedBy ?universityRankDefinedByObj.
            ?universityRankDefinedByObj exont:researchRating ?researchRating.

        }
    """ % (param_0)

    return query


# 6. Identifying relation between a country’s GDP and total number of Gold Medals won by that country in Olympics in the specified year.
# INPUT: Year
def generate_q6_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT (?countryName AS ?COUNTRY) (count(?athlete) AS ?GOLD_MDALS) (?gdp AS ?Gross_Domestic_Product)

        WHERE
        {
        	?athlete exont:medalWon 'Gold'.
            ?athlete exont:participatedIn ?olympicEventObj.
            ?olympicEventObj exont:yearOfEvent %s.
            ?athlete  dbo:sportCountry ?athleteSportCountryObj.
            ?athleteSportCountryObj dbo:name ?countryName.
          {

          	SELECT ?gdp ?countryName
    			WHERE {
    						?country dbo:name ?countryName.
    						?country exont:developmentIndicator ?devParam.
    						?devParam exont:statName 'GDP (current US$)'.
    						?devParam exont:statYear %s.
    						?devParam exont:statValue ?gdp.
    			      }
        	}
        }GROUP BY ?countryName ?gdp ORDER BY DESC (count(?athlete))
    """ % (param_0, param_0)

    return query


# 7. Total number of medals won by a country in the toughest sport.
# INPUT: MEDAL TYPE ie. [GOLD,SILVER,BRONZE]
def generate_q7_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT (COUNT(?athlete) AS ?TOTAL_MEDALS) (?athleteSportCountryName AS ?COUNTRY) (?toughSportName AS ?SPORTS_DISCIPLINE)

        WHERE {

          ?toughSport exont:difficultyLevel 1.
          ?toughSport dbo:name ?toughSportName.
          ?olympicEvent exont:hasSportDiscipline ?toughSportName.
          ?athlete exont:participatedIn ?olympicEvent.
          ?athlete exont:medalWon '%s'.
          ?athlete dbo:sportCountry ?athleteSportCountryObj.
          ?athleteSportCountryObj dbo:name ?athleteSportCountryName.

        }GROUP BY ?athleteSportCountryName ?toughSportName ORDER BY DESC (COUNT(?athlete))
    """ % (param_0)

    return query

# 8. Male female ratio of Olympic winners based on specified level of difficulty of the sport. (1 Being the toughest sport)
# INPUT: Year and Level of difficulty
def generate_q8_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT (COUNT(?athlete) AS ?NUMBER_OF_WINNERS) (?sex AS ?GENDER) (?toughSportName AS ?SPORTS_DISCIPLINE)

        WHERE {

          ?toughSport exont:difficultyLevel %s.
          ?toughSport dbo:name ?toughSportName.
          ?olympicEvent exont:hasSportDiscipline ?toughSportName.
          ?olympicEvent exont:yearOfEvent %s.
          ?athlete exont:participatedIn ?olympicEvent.
          ?athlete dbo:sex ?sex.

        } GROUP BY ?sex ?toughSportName
    """ % (param_1, param_0)

    return query

# 9. What is the total number of Olympics medals won by a country in a given year?
# Inputs: MEDAL TYPE, COUNTRY, YEAR
def generate_q9_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT  (COUNT(?athlete) AS ?TOTAL_MEDALS)
        WHERE {
          ?athlete exont:medalWon '%s'.
          ?athlete exont:participatedIn ?olympicEvent.
          ?olympicEvent exont:yearOfEvent %s.
          ?athlete dbo:sportCountry ?sportCountry.
          ?sportCountry exont:countryCode ?countryCode.
          {
            SELECT DISTINCT ?countryCode
            WHERE {
            		?country dbo:name '%s'.
          			?country exont:countryCode ?countryCode.
        		}
        	}
        }
    """ % (param_0, param_2, param_1)
    return query

# 10. Comparison between the research rating and the total number of nobel laureates of top 20 universities in the world.
# No input but graph
def generate_q10_query(param_0, param_1, param_2):
    query = """
        PREFIX exont: <http://example.org/ontology/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT  (?universityName AS ?UNIVERSITY_NAME)  (?universityWorldRank AS ?WORLD_RANK) (?researchRating AS ?RESEARCH_RATING) (COUNT(?laureate) AS ?NOBEL_LAUREATE_COUNT) (?countryName AS ?COUNTRY)

        WHERE {
        	?university exont:hasRank ?universityRankObj.
        	?universityRankObj exont:worldRank ?universityWorldRank.
        							FILTER (?universityWorldRank < 21).
          ?universityRankObj exont:definedBy ?universityRankParamObj.
          ?universityRankParamObj exont:researchRating ?researchRating.
        	?university exont:universityName ?universityName.

          ?laureate exont:affiliatedToUniversity ?laureateUniversityObj.
          ?laureateUniversityObj exont:universityName ?laureateUniversityName.
          FILTER ( regex (str(?universityName), str(?laureateUniversityName), "i") ).

          ?university exont:situatedIn ?countryObj.
          ?countryObj dbo:name ?countryName.


        } GROUP BY ?universityName ?universityWorldRank ?researchRating ?countryName ORDER BY (?universityWorldRank)
    """

    return query
