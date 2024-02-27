# Movie Catalog Readme

Welcome to the Movie Catalog application! This simple Python program allows you to explore and interact with a collection of movies. You can access information about available movies, view movie details, and even get personalized movie recommendations based on user ratings.

## Table of Contents
1. [Introduction](#introduction)
2. [Services](#services)
    - [Available Movies](#available-movies)
    - [Movie Details](#movie-details)
    - [Recommend a Movie](#recommend-a-movie)
3. [User Ratings](#user-ratings)
4. [Movie Data](#movie-data)
5. [Usage](#usage)

## Introduction <a name="introduction"></a>
The Movie Catalog application provides a user-friendly interface to explore a curated collection of movies. Users can choose from various services to access information about available movies, delve into movie details, or receive personalized movie recommendations.

## Services <a name="services"></a>
### Available Movies <a name="available-movies"></a>
Choose the "dostupne filmy" service to see a list of all available movies in the catalog.

### Movie Details <a name="movie-details"></a>
Opt for the "detaily filmu" service to view detailed information about a specific movie. You can select the movie from the list of available films.

### Recommend a Movie <a name="recommend-a-movie"></a>
Select the "doporuc film" service to receive recommendations based on user ratings. The program analyzes user ratings and suggests movies with the highest ratings.

## User Ratings <a name="user-ratings"></a>
The application maintains a set of user ratings for certain movies. The current user ratings are as follows:

```python
hodnoceni_uzivatelu = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}
```

Feel free to expand this set with additional user ratings to enhance the recommendation feature.

## Movie Data <a name="movie-data"></a>
The movie data is organized as a dictionary, with each movie having its own dictionary containing details such as name, rating, release year, director, duration, and cast. The movies are then grouped together in a catalog.

```python
FILMY = {
    "Shawshank Redemption": {...},
    "The Godfather": {...},
    "The Dark Knight": {...},
    "The Prestige": {...}
}
```

You can easily add more movies to the catalog by following the existing structure.

## Usage <a name="usage"></a>
To use the application, run the script and input your name when prompted. If you're in the list of users, you can proceed to select a service: "dostupne filmy," "detaily filmu," or "doporuc film."

Follow the on-screen instructions to explore movies or receive recommendations.
