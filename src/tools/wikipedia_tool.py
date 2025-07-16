from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from autogen_core.tools import FunctionTool

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper = api_wrapper_wiki)

def wikipedia_search(query:str)->str:
    """
    Used to find maths formula and its theory.
    """
    try:
        wiki.invoke(query)
    except Exception as e:
        print(f"Error Happened : {str(e)}")

web_search_tool = FunctionTool(func=wikipedia_search,description="Used to find maths formula and its theory.")