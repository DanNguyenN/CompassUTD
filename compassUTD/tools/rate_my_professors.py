import re
import ratemyprofessor


class GetProfessorRMP:
    def __init__(self):
        self.rmp_id = ratemyprofessor.get_school_by_name(
            "The University of Texas at Dallas"
        )

    def search_professor_rmp(self, professor_name: str):
        """_summary_

        Args:
            professor_name (str): First, Last or Full Name of the professor

        Returns:
            dict: return full name, courses taught, overall rating, and difficulty rating
        """
        prof = ratemyprofessor.get_professor_by_school_and_name(
            self.rmp_id, professor_name
        )
        courses_taught = [
            course.name
            for course in prof.courses
            if course.count > 1 and re.search(r"courses/([a-zA-Z]{2,4}\d{4})", course)
        ]
        favor_rating = prof.rating
        difficulty_rating = prof.difficulty
        full_name = prof.name
        data = {
            "full_name": full_name,
            "courses_taught": courses_taught,
            "rate_my_professor_rating": {
                "overall_rating_out_of_5": favor_rating,
                "difficulty_rating_out_of_5": difficulty_rating,
            },
        }
        return data
