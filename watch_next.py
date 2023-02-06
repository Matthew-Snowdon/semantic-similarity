# importing libraries, requires install
import spacy

nlp = spacy.load('en_core_web_md')

Planet_Hulk = """
Will he save their world or destroy it? When the Hulk becomes too dangerous for 
the Earth, the Illuminati trick Hulk into a shuttle and launch him into space 
to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.

"""

# Initialize an empty list to store movies
movie_list = []


def suggest_movie(description):
    """
    Given a movie description, this function returns the movie from a
    predefined list of movies that is most similar to the given description.
    The similarity is calculated using the spaCy natural language processing
    library.

        Parameters:
        description (str): A string that describes the movie being watched.

        Returns:
        recommendation (str): A string that contains the movie recommendation.
        """
    # Open the movies file for reading
    # Loop through each line in the file
    # Split the line into movie name and description
    # Append the movie description to the movie_list
    with open("movies.txt", 'r') as f:
        for line in f:
            movie_split = line.strip().split(":")
            movie_list.append(movie_split[1])

    # Create a spaCy Doc object for the description of the movie being watched
    movie_watched = nlp(description)

    # initialise variables outside the for loop, to keep track of the updating
    # values inside the loop
    max_similarity = -1
    max_film = ""

    # Loop through the movie descriptions
    # Calculate the similarity score between the description of the movie
    # watched and the current movie description
    # If the current similarity score is higher than the previous maximum:
    # Update the maximum similarity score
    # Update the corresponding movie
    for sentence in movie_list:
        similarity = nlp(sentence).similarity(movie_watched)
        if similarity > max_similarity:
            max_similarity = similarity
            max_film = sentence
        print(sentence + " - ", similarity)
        recommendation = "\nHere is your film recommendation: " + max_film
    return recommendation


print(suggest_movie(Planet_Hulk))
