import spacy

def get_most_similar_movie(user_description, movie_descriptions, movie_titles):
    nlp = spacy.load("en_core_web_md")

    # Compute vectors for user's description and all movie descriptions
    user_doc = nlp(user_description)
    movie_docs = [nlp(description) for description in movie_descriptions]

    # Calculate similarity scores
    similarity_scores = [user_doc.similarity(movie_doc) for movie_doc in movie_docs]

    # Find the index of the most similar movie
    most_similar_index = similarity_scores.index(max(similarity_scores))

    # Get the title of the most similar movie
    most_similar_movie_title = movie_titles[most_similar_index]

    return most_similar_movie_title

# Read movie descriptions from the file
with open('movies.txt', 'r') as file:
    movie_descriptions = file.read().splitlines()

# list of movie titles corresponding to the descriptions in the order
movie_titles = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F", "Movie G", "Movie H", "Movie I", "Movie J"]

# User's description for "Planet Hulk"
user_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Get the most similar movie title
most_similar_movie = get_most_similar_movie(user_description, movie_descriptions, movie_titles)

print(f"The most similar movie to 'Planet Hulk' is: {most_similar_movie}")
