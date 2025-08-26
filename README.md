# Movie Semantic Search Assignment
**TANISHKA CHAUHAN
221010250
ECE**
This repository contains my solution for the semantic search on movie plots assignment. The project implements a search engine that uses natural language understanding to find movies semantically similar to a given query, rather than just matching keywords.

## Setup

Follow these steps to set up the project environment on your local machine.

1.  **Clone the Repository**
    Open a terminal and run the following command to clone this repository:
    ```bash
    git clone [https://github.com/tanich04/Movie-Semantic-Search-Engine.git](https://github.com/tanich04/Movie-Semantic-Search-Engine.git)
    cd Movie-Semantic-Search-Engine/Assignment-1
    ```

2.  **Set Up a Virtual Environment**
    It's recommended to work within a virtual environment to manage project dependencies.
    -   Create the virtual environment:
        ```bash
        python -m venv venv
        ```
    -   Activate it:
        -   **Windows:** `venv\Scripts\activate`
        -   **macOS/Linux:** `source venv/bin/activate`

3.  **Install Dependencies**
    Install all required libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Notebook (Optional)**
    If you have a Jupyter Notebook or Jupyter Lab installed, you can open and run the notebook to see the code in action.
    ```bash
    jupyter notebook movie_search_solution.ipynb
    ```

## Testing

Unit tests are included to verify that the search function works correctly. To run the tests, execute the following command from the root of the `Assignment-1` directory:

```bash
python -m unittest tests/test_movie_search.py -v
```
## Usage

You can test the core search functionality by running the movie_search.py file directly or by running the cells in the Jupyter notebook. The example below uses the command line.
```bash
python movie_search.py
```
This will run the example usage and print the top 3 results for the query spy thriller in Paris.

## What this assignment is doing
The core of this project is a semantic search engine that uses a powerful AI model to understand the meaning behind your words. Unlike a basic search that just looks for matching keywords, this system finds results that are contextually relevant to your query.

Here’s a step-by-step breakdown of how it works:

**1. Load the Data and Model:**

The system first loads the movie data from movies.csv, which contains movie titles and their plot summaries, into a pandas DataFrame.

It then loads the SentenceTransformer model, specifically the lightweight yet effective all-MiniLM-L6-v2 model. This model is a key component as it can convert text into numerical representations.

**2. Generate Embeddings:**

The all-MiniLM-L6-v2 model processes each movie plot and converts it into a high-dimensional numerical vector called an embedding. This vector captures the semantic meaning of the plot. All these movie plot embeddings are stored in a database or in memory for quick access.

**3. Process the User Query:**

When a user submits a search query (e.g., "spy thriller in Paris"), the system takes that text and, just like the movie plots, uses the same all-MiniLM-L6-v2 model to convert it into its own embedding.

**4. Calculate Similarity:**

The magic of semantic search lies in this step. The system calculates the cosine similarity between the user's query embedding and all the movie plot embeddings. Cosine similarity is a metric that measures the angle between two vectors and is widely used to determine how similar two text documents are, regardless of their size. A score of 1 means the vectors are identical (perfect match), while a score of 0 means they are completely dissimilar.

**5. Rank and Return Results:**

Finally, the system sorts all the movies in descending order based on their similarity scores. It then returns a pandas DataFrame with the top n most similar movies, along with their titles, plots, and their calculated similarity scores. This provides the user with the most relevant results from the movie dataset.
