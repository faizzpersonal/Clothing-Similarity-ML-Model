
# Clothing Similarity Search

This project aims to provide a clothing similarity search function using machine learning techniques. Given a text description of a clothing item, the function returns a ranked list of similar items with their links.

**Using_USE.py & Using_BERT Are Direct Program That Run(On Compiler) After Installing The Necessary Python Packages **

 Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

## Project Structure

The project consists of the following files:

**main.py:** Contains the code for the clothing similarity search function

**requirements.txt:** Specifies the Python dependencies for the project.

**product_info.json:** JSON file containing the clothing item data (name, link, and description).

**README.md:** Markdown file explaining the project and its deployment.
## Setup and Installation

Install the necessary tools:
Install the Python programming language (version 3.6 or higher).

Install the required Python packages by running the following command:

```bash
  pip install -r requirements.txt
```

Dataset preparation:
Create a JSON file named 'product_info.json' in the project directory.
Add the clothing item data in the following format:



```bash
  [
  {
    "name": "Item 1",
    "link": "https://www.example.com/item1",
    "description": "Description of item 1"
  },
  {
    "name": "Item 2",
    "link": "https://www.example.com/item2",
    "description": "Description of item 2"
  },
  ...
]


```
## Usage

To use the clothing similarity search function locally:

Open the main.py file.

Locate the data_file variable and update it with the correct path to your JSON data file (product_info.json).

Run the script to start the function.

In the terminal or console, enter a text description of a clothing item.

The function will return a ranked list of similar item links based on the input description.

    
## Deployment

To deploy the function on Google Cloud:

Install the Google Cloud SDK, which includes the gcloud command-line tool.

Authenticate with your Google Cloud account using the following command:


```bash
  gcloud auth login
```
Create a new project on the Google Cloud Console if you haven't already.

Set the project as the default project for deployment:

```bash
  gcloud config set project YOUR_PROJECT_ID

```

Deploy the function to Google Cloud Functions:
Run the following command to deploy the function:

```bash
  gcloud functions deploy clothing-similarity --runtime python310 --trigger-http --allow-unauthenticated --entry-point clothing_similarity_search

```
Replace YOUR_PROJECT_ID with your actual project ID and clothing-similarity with your desired function name.

Deploy the container to Cloud Run with the following command:

```bash
  gcloud run deploy clothing-similarity --image gcr.io/YOUR_PROJECT_ID/clothing-similarity --platform managed --allow-unauthenticated

```
Replace YOUR_PROJECT_ID with your actual project ID and clothing-similarity with your desired function name.

After successful deployment, note the URL provided for accessing the function.

Test the deployed function by sending a POST request with a JSON payload containing the "text" field with the clothing item description.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.


