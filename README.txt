Movie Recommedation System using different recommendation techniques:

Collaborative Filtering

They are built on a dataset of user/item feedback. This may be either explicit feedback such as a star rating or thumb-up/thumb-down, or implicit feedback such as the number of episodes watched in a TV show. We categorize these models further in how they process this data.

User-User

The most commonly used recommendation algorithm follows the “people like you like that” logic. We call it a “user-user” algorithm because it recommends to a user an item that similar users liked before. The similarity between two users is computed from the amount of items they have in common in the dataset. This algorithm is very efficient when the number of users is way smaller than the number of items. You can think of a medium sized online shop with millions of products. The major drawback is that adding a new user is expensive since it requires to update all similarities between users.

Item-Item

The “item-item” algorithm uses the same approach but reverses the view between users and items. It follows the logic “if you like this you might also like that”. It recommends items that are similar to the ones you previously liked. As before the similarity between two items is computed using the amount of users they have in common in the dataset. This algorithm is best when the number of items is way smaller than the number of users, such as large-scale online shops. It is well suited if your items don’t change too much, since you can pre-compute the full table of item-item similarities and then serve recommendations in real-time. Updating this table for adding a new item is unfortunately hard.

User-Item

There are multiple forms of “user-item” recommendation algorithms which combines both approach to generate recommendations. The simplest ones are based on matrix factorization techniques. The goal is to learn low-dimensional vectors (“embeddings”) for all users and all items, such that multiplying them together can recover if a user likes an item or not. You can view these vectors as encoding how much an item has a certain feature (like a movie being a drama), and respectively how much a user likes this feature in items (it can also be negative!).

This factorization is best trained using SVD, but since this algorithm is computationally intensive and does not scale well, we often prefer alternatives. For medium-scale datasets ALS will give reasonable performances. For large dataset, only the SGD algorithm will be able to scale, but will be very slow.

Once the users embeddings and the items embeddings have been pre-computed recommendations can be served in real time. Another benefit of this approach is that you can learn more about users and items using their embeddings. For example you can cluster users or items accordingly to their item preferences.

User-Item algorithms share the drawback that there is no efficient method to update the embeddings after adding a new item or a new user.

Content-Based

All the previous models suffer from what is called the cold-start problem. Because the recommendations are computed using a dataset of users feedback on items, they can’t recommend items with no or only a few feedback, such as new items. Similarly they can’t recommend anything to a new user before they started to bootstrap by giving some feedback on enough items (this explains the tedious onboarding steps you surely experienced online). These issues are mitigated using Content-Based models. The approach is identical to the previous User-User or Item-Item algorithms, except that the similarities are computed using only content-based features. To train a model solving the item cold-start (resp. user cold-start) you need a dataset including detailed descriptions of your items (resp. of your users), such as the genre of a movie, its budget, its duration, or any variable that may help the recommendation. The recent progress of pattern recognition in machine learning unlocked great improvements in content-based model using information extracted from raw images or raw text description. Plenty of tools and pre-trained deep learning models of Computer Vision or Natural Language Processing can be found online. The obvious benefit of using a pre-trained model is that you don’t need enormous datasets and expensive servers to train your recommendation engine.

Context-aware

Context-aware recommender systems (CARSs) apply sensing and analysis of user context in order to provide personalized services. Adding context to a recommendation model is challenging, since the addition of context may increases both the dimensionality and sparsity of the model. Recent research has shown that modeling contextual information as a latent vector may address the sparsity and dimensionality challenges. We suggest a new latent modeling of sequential context by generating sequences of contextual information and reducing their contextual space to a compressed latent space.We train a long short-term memory (LSTM) encoder-decoder network on sequences of contextual information and extract sequential latent context from the hidden layer of the network in order to represent a compressed representation of sequential data. We propose new context-aware recommendation models that extend the neural collaborative filtering approach and learn nonlinear interactions between latent features of users, items, and contexts which take into account the sequential latent context representation as part of the recommendation process. We deployed our approach using two context-aware datasets with different context dimensions. Empirical analysis of our results validates that our proposed sequential latent context-aware model (SLCM), surpasses state of the art CARS models.



Summary
=======

This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.

Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.

The data are contained in the files `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. More details about the contents and use of all these files follows.

This is a *development* dataset. As such, it may change over time and is not an appropriate dataset for shared research results. See available *benchmark* datasets if that is your intent.

This and other GroupLens data sets are publicly available for download at <http://grouplens.org/datasets/>.


Usage License
=============

Neither the University of Minnesota nor any of the researchers involved can guarantee the correctness of the data, its suitability for any particular purpose, or the validity of results based on the use of the data set. The data set may be used for any research purposes under the following conditions:

* The user may not state or imply any endorsement from the University of Minnesota or the GroupLens Research Group.
* The user must acknowledge the use of the data set in publications resulting from the use of the data set (see below for citation information).
* The user may redistribute the data set, including transformations, so long as it is distributed under these same license conditions.
* The user may not use this information for any commercial or revenue-bearing purposes without first obtaining permission from a faculty member of the GroupLens Research Project at the University of Minnesota.
* The executable software scripts are provided "as is" without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of them is with you. Should the program prove defective, you assume the cost of all necessary servicing, repair or correction.

In no event shall the University of Minnesota, its affiliates or employees be liable to you for any damages arising out of the use or inability to use these programs (including but not limited to loss of data or data being rendered inaccurate).

If you have any further questions or comments, please email <grouplens-info@umn.edu>


Citation
========

To acknowledge use of the dataset in publications, please cite the following paper:

> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>


Further Information About GroupLens
===================================

GroupLens is a research group in the Department of Computer Science and Engineering at the University of Minnesota. Since its inception in 1992, GroupLens's research projects have explored a variety of fields including:

* recommender systems
* online communities
* mobile and ubiquitious technologies
* digital libraries
* local geographic information systems

GroupLens Research operates a movie recommender based on collaborative filtering, MovieLens, which is the source of these data. We encourage you to visit <http://movielens.org> to try it out! If you have exciting ideas for experimental work to conduct on MovieLens, send us an email at <grouplens-info@cs.umn.edu> - we are always interested in working with external collaborators.


Content and Use of Files
========================

Formatting and Encoding
-----------------------

The dataset files are written as [comma-separated values](http://en.wikipedia.org/wiki/Comma-separated_values) files with a single header row. Columns that contain commas (`,`) are escaped using double-quotes (`"`). These files are encoded as UTF-8. If accented characters in movie titles or tag values (e.g. Misérables, Les (1995)) display incorrectly, make sure that any program reading the data, such as a text editor, terminal, or script, is configured for UTF-8.


User Ids
--------

MovieLens users were selected at random for inclusion. Their ids have been anonymized. User ids are consistent between `ratings.csv` and `tags.csv` (i.e., the same id refers to the same user across the two files).


Movie Ids
---------

Only movies with at least one rating or tag are included in the dataset. These movie ids are consistent with those used on the MovieLens web site (e.g., id `1` corresponds to the URL <https://movielens.org/movies/1>). Movie ids are consistent between `ratings.csv`, `tags.csv`, `movies.csv`, and `links.csv` (i.e., the same id refers to the same movie across these four data files).


Ratings Data File Structure (ratings.csv)
-----------------------------------------

All ratings are contained in the file `ratings.csv`. Each line of this file after the header row represents one rating of one movie by one user, and has the following format:

    userId,movieId,rating,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.

Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).

Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Tags Data File Structure (tags.csv)
-----------------------------------

All tags are contained in the file `tags.csv`. Each line of this file after the header row represents one tag applied to one movie by one user, and has the following format:

    userId,movieId,tag,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.

Tags are user-generated metadata about movies. Each tag is typically a single word or short phrase. The meaning, value, and purpose of a particular tag is determined by each user.

Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Movies Data File Structure (movies.csv)
---------------------------------------

Movie information is contained in the file `movies.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,title,genres

Movie titles are entered manually or imported from <https://www.themoviedb.org/>, and include the year of release in parentheses. Errors and inconsistencies may exist in these titles.

Genres are a pipe-separated list, and are selected from the following:

* Action
* Adventure
* Animation
* Children's
* Comedy
* Crime
* Documentary
* Drama
* Fantasy
* Film-Noir
* Horror
* Musical
* Mystery
* Romance
* Sci-Fi
* Thriller
* War
* Western
* (no genres listed)


Links Data File Structure (links.csv)
---------------------------------------

Identifiers that can be used to link to other sources of movie data are contained in the file `links.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,imdbId,tmdbId

movieId is an identifier for movies used by <https://movielens.org>. E.g., the movie Toy Story has the link <https://movielens.org/movies/1>.

imdbId is an identifier for movies used by <http://www.imdb.com>. E.g., the movie Toy Story has the link <http://www.imdb.com/title/tt0114709/>.

tmdbId is an identifier for movies used by <https://www.themoviedb.org>. E.g., the movie Toy Story has the link <https://www.themoviedb.org/movie/862>.

Use of the resources listed above is subject to the terms of each provider.


Cross-Validation
----------------

Prior versions of the MovieLens dataset included either pre-computed cross-folds or scripts to perform this computation. We no longer bundle either of these features with the dataset, since most modern toolkits provide this as a built-in feature. If you wish to learn about standard approaches to cross-fold computation in the context of recommender systems evaluation, see [LensKit](http://lenskit.org) for tools, documentation, and open-source code examples.
