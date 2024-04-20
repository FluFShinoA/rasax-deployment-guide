# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Form, AllSlotsReset
from rasa_sdk.types import DomainDict



class ActionTuitionFee(Action):
    def name(self) -> Text:
        return "action_tuition_fee"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Due to the recent tuition fee hikes approved by the CHED, the tuition fee costs around 759 per unit. How many units are you trying to enroll in?")
        return []

class ActionCalculateTuitionFee(Action):
    def name(self) -> Text:
        return "action_calculate_tuition_fee"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])
        units = next((entity['value'] for entity in entities if entity['entity'] == 'number_of_units'), None)

        if units is None:
            dispatcher.utter_message("I'm sorry, but I couldn't understand the number of units.")
            return []

        cost_per_unit = 759
        tuition_fee = int(units) * cost_per_unit

        message = f"{units} units would cost {tuition_fee:,}. Note that miscellaneous and other fees are not included in this."
        dispatcher.utter_message(message)

        return []
    
#----------------------CAREER ASSISTANCE FLOW------------------------

class ValidatePreferenceForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_preference_form"
    
    def validate_preference1(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference1' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or  D.")
            return {"preference1": None}
       
        return {"preference1": slot_value}
    
    def validate_preference2(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference2' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, D.")
            return {"preference2": None}
        
        return {"preference2": slot_value}
    
    def validate_preference3(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference3' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference3": None}
        
        return {"preference3": slot_value}
    
    def validate_preference4(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference4' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference4": None}
        
        return {"preference4": slot_value}
    
    def validate_preference5(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference5' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference5": None}

        return {"preference5": slot_value}
    
    def validate_preference6(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference6' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference6": None}
        
        return {"preference6": slot_value}
    
    def validate_preference7(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference7' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference7": None}

        return {"preference7": slot_value}
    
    def validate_preference8(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference8' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference8": None}

        return {"preference8": slot_value}
    
    def validate_preference9(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference9' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference9": None}
        
        return {"preference9": slot_value}
    
    def validate_preference10(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict [Text, Any]:
        """Validate 'preference10' value."""
        count_dict = self.count_preferences(tracker, dispatcher)
        if slot_value not in ["A", "B", "C", "D"]:
            dispatcher.utter_message(text="Invalid input. Please choose A, B, C, or D.")
            return {"preference10": None}
        
        return {"preference10": slot_value}

    def count_preferences(self, tracker: Tracker, dispatcher: CollectingDispatcher) -> Dict[Text, int]:
        """Counts the occurrences of each preference value and sends a message."""
        preferences = {}
        for i in range(1, 11):
            slot_name = f"preference{i}"
            preference = tracker.get_slot(slot_name)
            if preference:
                preferences[slot_name] = preference

            
        # # for debugging 
        # # message = f"Preferences count: A - {count_dict['A']}, B - {count_dict['B']}, C - {count_dict['C']}, D - {count_dict['D']}"
        # # dispatcher.utter_message(message)

        # recommendation_message = self.get_recommendation(count_dict)
        # dispatcher.utter_message(text=recommendation_message)

    
    # def get_recommendation(self, count_dict: Dict[str, int]) -> str:
    #     """Generates a recommendation message based on preference counts."""
    #     # if count_dict["A"] > count_dict["B"] and count_dict["A"] > count_dict["C"] and count_dict["A"] > count_dict["D"]:
    #     #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Computer Science."
    #     # elif count_dict["B"] > count_dict["A"] and count_dict["B"] > count_dict["C"] and count_dict["B"] > count_dict["D"]:
    #     #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Information Technology."
    #     # elif count_dict["C"] > count_dict["A"] and count_dict["C"] > count_dict["B"] and count_dict["C"] > count_dict["D"]:
    #     #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science In Entertainment and Multimedia Computing with a Major in Game Development."
    #     # elif count_dict["D"] > count_dict["A"] and count_dict["D"] > count_dict["B"] and count_dict["D"] > count_dict["C"]:
    #     #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science In Entertainment and Multimedia Computing with a Major in Digital Animation."
    #     # elif count_dict["D"] > count_dict["A"] and count_dict["D"] > count_dict["B"] and count_dict["D"] > count_dict["C"]:
    #     #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Library and Information Science (BLIS)."
    #     # elif count_dict["C"] > count_dict["A"] and count_dict["C"] > count_dict["B"] and count_dict["C"] > count_dict["D"]:
    #     #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Information Systems (BSIS)."
    #     # else:
    #     #     recommendation_message = "Based on your preferences, I recommend exploring more about each degree program to find the best fit for you."
        

    #     return recommendation_message

    def all_slots_filled(self, tracker: Tracker) -> bool:
        """Check if all preference slots are filled."""
        for i in range(1, 11):
            slot_name = f"preference{i}"
            if tracker.get_slot(slot_name) is None:
                return False
        return True

    def send_recommendation(
        self, dispatcher: CollectingDispatcher, tracker: Tracker) -> None:
        """Send the recommendation message based on preferences."""
        preferences = {
            "preference1": tracker.get_slot("preference1"),
            "preference2": tracker.get_slot("preference2"),
            "preference3": tracker.get_slot("preference3"),
            "preference4": tracker.get_slot("preference4"),
            "preference5": tracker.get_slot("preference5"),
            "preference6": tracker.get_slot("preference6"),
            "preference7": tracker.get_slot("preference7"),
            "preference8": tracker.get_slot("preference8"),
            "preference9": tracker.get_slot("preference9"),
            "preference10": tracker.get_slot("preference10")
        }
        # weights
        bscs = 0
        bsit = 0
        bsis = 0
        bsemc_art = 0
        bsemc_game = 0

        # recommend BLIS if one of the answers contains anything that has to do with "library"

        # Question 1
        if preferences["preference1"] == "A":
            bscs += 1
            bsit += 1
        elif preferences["preference1"] == "B":
            bsit += 1
            bsis += 1
        elif preferences["preference1"] == "C":
            bsemc_art += 1
            bsemc_game += 1

        # Question 2
        if preferences["preference2"] == "A":
            bsemc_art += 1
            bsemc_game += 1
        # answer B is not important
        
        # Question 3
        if preferences["preference3"] == "A":
            bscs += 1
            bsit += 1
            bsis += 1
        elif preferences["preference3"] == "B":
            bsit += 1
            bsis += 1
        elif preferences["preference3"] == "C":
            bsit += 1
        elif preferences["preference3"] == "D":
            bsemc_art += 1
            bsemc_game += 1

        # Question 4
        if preferences["preference4"] == "A":
            bscs += 1
            bsit += 1
            bsis += 1
            bsemc_art += 1
            bsemc_game += 1
        elif preferences["preference4"] == "B":
            bsit += 1
        elif preferences["preference4"] == "C":
            bsemc_game += 1
        elif preferences["preference4"] == "D":
            bsemc_art += 1
        elif preferences["preference4"] == "E":
            bsis += 1

        # Question 5
        if preferences["preference5"] == "A":
            bscs += 1
            bsit += 1
            bsis += 1
        
        # Question 6
        if preferences["preference6"] == "A":
            bsemc_art += 1
            bsemc_game += 1
        
        # Question 7
        if preferences["preference7"] == "A":
            bsemc_art += 1
            bsemc_game += 1
        
        # Question 8
        if preferences["preference8"] == "A":
            bscs += 1
            bsit += 1
            bsis += 1
        elif preferences["preference8"] == "B":
            bsemc_art += 1
            bsemc_game += 1
        
        # Question 9
        if preferences["preference9"] == "A":
            bscs += 1
        elif preferences["preference9"] == "B":
            bsit += 1
        elif preferences["preference9"] == "C":
            bsis += 1
        elif preferences["preference9"] == "D":
            bsemc_art += 1
            bsemc_game += 1
        
        # Question 10
        if preferences["preference10"] == "A":
            bscs += 1
        elif preferences["preference10"] == "B":
            bsit += 1
        elif preferences["preference10"] == "C":
            bsis += 1
        elif preferences["preference10"] == "D":
            bsemc_game += 1
        elif preferences["preference10"] == "E":
            bsemc_art += 1

        if bscs > bsit and bscs > bsis  and bscs > bsemc_art and bscs > bsemc_game:
            recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Computer Science."
            recommend_career = "utter_bscs_careers"
        elif bsit > bscs and bsit > bsis and bsit > bsemc_art and bsit > bsemc_game:
            recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Information Technology."
            recommend_career = "utter_bsit_careers"
        elif bsis > bsit and bsis > bscs and bsis > bsemc_art and bsis > bsemc_game:
            recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Information Systems (BSIS)."
            recommend_career = "utter_bsis_careers"
        elif bsemc_art > bsit and bsemc_art > bscs and bsemc_art > bsis and bsemc_art > bsemc_game:
            recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science In Entertainment and Multimedia Computing with a Major in Digital Animation."
            recommend_career = "utter_bsemc_digiani_careers"
        elif preferences["preference1"] == "D" or preferences["preference3"] == "E" or preferences["preference9"] == "E" or preferences["preference10"] == "F":
            recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Library and Information Science (BLIS)."
            recommend_career = "utter_blis_careers"
        else:
            recommendation_message = "Your preferences are way too vague, I recommend exploring more into these Programs."
            recommend_career ="utter_career_null"

        # if preferences["preference1"] == "A" and preferences["preference3"] == "A" and preferences["preference4"] == "A" and preferences["preference7"] == "A" and preferences["preference8"] == "A" and preferences["preference9"] == "A" and preferences["preference10"] == "A":
        #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Computer Science."
        #     recommend_career = "utter_bscs_careers"
        # elif preferences["preference1"] in ("A", "B") and preferences["preference3"] == "B" and preferences["preference4"] == "B" and preferences["preference7"] == "B" and preferences["preference8"] == "B" and preferences["preference9"] in ("A", "B") and preferences["preference10"] == "A":
        #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Information Technology."
        #     recommend_career = "utter_bsit_careers"
        # elif preferences["preference1"] == "C" and preferences["preference2"] == "A" and preferences["preference3"] == "C" and preferences["preference4"] == "B" and preferences["preference5"] == "C" and preferences["preference6"] == "A" and preferences["preference7"] == "B" and preferences["preference8"] == "C" and preferences["preference9"] == "A" and preferences["preference10"] == "A":
        #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science In Entertainment and Multimedia Computing with a Major in Game Development."
        #     recommend_career = "utter_bsemc_gamedev_careers"
        # elif preferences["preference1"] == "C" and preferences["preference2"] == "A" and preferences["preference3"] == "C" and preferences["preference4"] == "B" and preferences["preference5"] == "C" and preferences["preference6"] == "B" and preferences["preference7"] == "B" and preferences["preference8"] == "C" and preferences["preference9"] == "A" and preferences["preference10"] == "A":
        #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science In Entertainment and Multimedia Computing with a Major in Digital Animation."
        #     recommend_career = "utter_bsemc_digiani_careers"
        # elif preferences["preference1"] == "B" and preferences["preference2"] == "B" and preferences["preference3"] == "B" and preferences["preference4"] == "A" and preferences["preference5"] == "B" and preferences["preference6"] == "B" and preferences["preference7"] == "A" and preferences["preference8"] == "B" and preferences["preference9"] == "A" and preferences["preference10"] == "A":
        #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Science in Information Systems (BSIS)."
        #     recommend_career = "utter_bsis_careers"
        # elif preferences["preference1"] == "D" and preferences["preference3"] == "D" and preferences["preference4"] == "A" and preferences["preference7"] == "A" and preferences["preference8"] == "D" and preferences["preference9"] == "A" and preferences["preference10"] == "A":
        #     recommendation_message = "Based on your preferences, I recommend the following degree program: Bachelor of Library and Information Science (BLIS)."
        #     recommend_career = "utter_blis_careers"
        # else:
        #     recommendation_message = "Your preferences are way too vague, I recommend exploring more into these Programs."
        #     recommend_career ="utter_career_null"
        total_message = f"BSCS total: {bscs}\nBSIT total: {bsit}\nBSIS total: {bsis}\nBSEMC Art total: {bsemc_art}\nBSEMC Game total: {bsemc_game}"   
        dispatcher.utter_message(text=total_message)
        dispatcher.utter_message(text=recommendation_message)
        dispatcher.utter_template(recommend_career, tracker)

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        
        if self.all_slots_filled(tracker):
            self.send_recommendation(dispatcher, tracker)
            return[]
        
        return []