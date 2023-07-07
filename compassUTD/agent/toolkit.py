from typing import TYPE_CHECKING, List, Optional

from langchain.tools.base import BaseTool
from langchain.agents.agent_toolkits.base import BaseToolkit

from langchain.callbacks.manager import CallbackManagerForToolRun

from compassUTD.tools.google_search import SearchCourse, SearchDegree, SearchDefinition, SearchGeneral
from compassUTD.tools.rate_my_professors import GetProfessorRMP


class CompassToolkit(BaseToolkit):
    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [
            ProfessorSearchResult(),
            CoursesSearchResults(),
            DegreeSearchResult(),
            GeneralSearchResult(),
        ]


class ProfessorSearchResult(BaseTool):
    name = "get_professor_rating_and_classes_taught"
    description = (
        "a search engine on professor of UT Dallas on RateMyProfessor database"
        "useful for when you need to answer questions about professors ratings, difficulty, and class taught."
        "will not return contact information, use the general_search tool for that."
        "Input should be a First, Last or Full name of the professor without greeting prefix"
        "Return will be full name, courses taught, overall rating, and difficulty rating"
    )

    def __init__(self):
        self.find_professor = GetProfessorRMP()

    def _run(
            self, professor_name: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return self.find_professor._run(professor_name)

    async def _arun(
            self, name: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        raise NotImplementedError("does not support async yet")


class CoursesSearchResults(BaseTool):
    name = "course_search"
    description = (
        "a search engine on course database of UT Dallas"
        "useful for when you need to search for answer about courses."
        "Input should be a search query"
        "Return will be multiple results with course title and snippet"
    )

    def __init__(self):
        self.search_course = SearchCourse()

    def _run(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return self.search_course._run(query)

    async def _arun(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        raise NotImplementedError("does not support async yet")


class DegreeSearchResult(BaseTool):
    name = "college_degree_search"
    description = (
        "a search engine on college degree database of UT Dallas"
        "useful for when you need to search for answer about college degrees."
        "Input should be a search query"
        "Return will be multiple results with title, and snippet of the degree"
    )

    def __init__(self):
        self.search_degree = SearchDegree()

    def _run(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return self.search_degree._run(query)

    async def _arun(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        raise NotImplementedError("does not support async yet")


class GeneralSearchResult(BaseTool):
    name = "general_search"
    description = (
        "a search engine for general information about UT Dallas"
        "useful for answer question related to staff(s), school(s), department(s), and locations in UT Dallas"
        "Searching for courses or college degrees are discouraged as there are better tools"
        "Input should be a search query"
        "Return will be multiple results with title, link and snippet"
    )

    def __init__(self):
        self.general_search = SearchGeneral

    def _run(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return self.general_search(query)

    async def _arun(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        raise NotImplementedError("does not support async yet")


class DictionaryRun(BaseTool):
    name = "get_definition_of_word"
    description = ("a dictionary for simple word" 
                   "Input should be word or phrases"
                   )

    def _run(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return SearchDefinition._run(query)

    async def _arun(
            self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        return await SearchDefinition._run(query)
