from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        return answer.upper() == self.correct_answer.upper()


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()


class DescriptiveQuestion(Question):
    def __init__(self, keywords):
        self.keywords = keywords

    def evaluate_answer(self, answer):
        return all(word.lower() in answer.lower() for word in self.keywords)


questions = [
    (MCQQuestion("B"), "B"),
    (TrueFalseQuestion("True"), "True"),
    (DescriptiveQuestion(["python", "object"]), "Python is object oriented.")
]

for question, answer in questions:
    print("Correct:", question.evaluate_answer(answer))
