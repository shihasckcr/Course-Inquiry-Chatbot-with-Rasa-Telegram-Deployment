from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionCourseInfo(Action):
    def name(self) -> str:
        return 'action_course_info'

    async def run(self, dispatcher, tracker, domain):
        course = tracker.get_slot('course')

        # Normalize entity to match dictionary keys
        if course:
            course = course.title()

        course_details = {
            'Data Science': 'We offer a PYTHON DATA SCIENCE - ML - AI - & Power BI course with the duration of 7 months',
            'Flutter': 'We offer the Best Flutter Training In Kochi (Cochin) & Calicut (Kozhikode), Duration - 5 months',
            'Python Django': 'We offer a Python Django - React - Full Stack Web Development Expert Course, Duration - 5 months',
            'Mearn Stack': 'We offer a MEA(R)N Stack Web Development Expert, Duration 6 months',
            'Asp.Net': 'We offer an Asp.net MVC with Angular - Full Stack Course, Duration - 6 months',
            'Testing': 'We offer a perfect Software Testing Training - Manual & Automation Course, Duration - 4 months',
            'Java': 'We offer an excellent Java Spring Full Stack Development Course, Duration - 5 months',
            'Robotics': 'Our new course Robotics with AI & IoT Training is 6 months long'
        }

        response = course_details.get(course, "I am sorry, I don't have details about that now.")
        dispatcher.utter_message(text=response)
        return []
