def predictor(new_movie):
    '''
    This is a simple illutration of how we can compute the movie review score
    based on the 3 parameters.

    Algo:
    For the selected movie, we compute the included angle among all the other
    movies we have in our train data sets.
    Then we pick 5 most similar movies,
    then we compute the average score of these 5 movies
    and return the value as the predicted score
    '''
    movie_bin = pd.Series()
    movie_bin['genres_bin'] = binary(genres, new_movie['genres'])
    movie_bin['director_bin'] = binary(directors, new_movie['director'])
    movie_bin['actors_bin'] = binary(actors, new_movie['actors'])
    vote = movies_15.copy()
    vote['angle'] = [angle(vote.iloc[i], movie_bin) for i in range(len(vote))]
    vote = vote.sort_values('angle')
    vote_avg = np.mean(vote.vote_average[0:5])
    return vote_avg