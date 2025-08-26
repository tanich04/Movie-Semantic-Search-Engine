# Movie Semantic Search Assignment

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

4.  **Run the Notebook**
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

              title             plot                          similarity
0          Spy Movie            A spy navigates intrigue...    0.769684
1   Romance in Paris            A couple falls in love...      0.388030
2       Action Flick            A high-octane chase through..  0.256777
