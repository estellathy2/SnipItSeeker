# PyExamples, Gradio Demo
### Description
This application fetches and saves Python code snippets from [W3Schools](https://www.w3schools.com/) and displays them through Gradio. 
### Installation and Usage
1. You can install the project dependencies using `pip` and the provided `requirements.txt` file. 
```zsh
pip install -r requirements.txt
```
2. To see the Gradio demo, run: 
```zsh
python3 demo.py
```
3. Open your web browser and navigate to the provided URL.  
4. Enter a keyword in the provided box to see all related examples.
### Dependencies
- Python 3.x
- Gradio
- Requests
- BeautifulSoup4
### Files
- `demo.py`: The main application script that defines the Gradio interface. 
- `fetch.py`: Updates `examples.json` by fetching examples from W3Schools. 
- `examples.json`: Contains all fetched examples. 
