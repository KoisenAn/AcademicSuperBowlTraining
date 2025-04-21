eventDict = {
    # Pop-ups
    3798: "popUpStats", 
    3799: "popUpExit", 
    3800: "popUpInPractice",
    3801: "checkExit", 
    3802: "popUpSettings", 
    # Practice Selection Events
    4199: "credits", 
    4200: "home", 
    4201: "pracSelect", 
    4202: "history", 
    # In practice events
    6900: "answerInputted", 
    6901: "answerSelected", 
    6902: "newProblem", 
    6903: "Choice A", 
    6904: "Choice B",
    6905: "Choice C",
    6906: "Choice D"}

colors = {"white": (255,255,255), 
          "black": (0,0,0), 
          "darkBlue": (53,63,112), 
          "screenGrey": (230,230,230), 
          "highlightMCQGrey": (210,210,210), 
          "highlightBlue": (55,190,245,0.5),
          "rightGreen": (140,250,150),
          "wrongRed": (250,145,145)}

class QuestionGenerationType:

    class Fixed:
        pass

    class Generate:
        pass

class ProblemDisplayType:

    class Text:
        pass

    class Custom:
        pass

class ProblemInputType:

    class TextBox:

        def __init__(self, numTextBoxes, firstInputBoxText, secondInputBoxText=None, thirdInputBoxText=None):
            self.textboxes = numTextBoxes
            self.firstInputBoxText = firstInputBoxText
            self.secondInputBoxText = secondInputBoxText
            self.thirdInputBoxText = thirdInputBoxText
            self.inputBoxTextList = [firstInputBoxText, secondInputBoxText, thirdInputBoxText][:numTextBoxes-1]

        def getNumTextBoxes(self):
            return self.textboxes
        
        def getInputBoxTextList(self):
            return self.inputBoxTextList

    class MCQ:

        def __init__(self, otherAnswerChoices=[], numChoices=4, numAnswers=1):
            self.otherAnswerChoices = otherAnswerChoices
            self.numChoices = numChoices
            self.numAnswers = numAnswers

        def getAnswer(self):
            return self.answer

        def getOtherAnswerChoices(self):
            return self.otherAnswerChoices

        def getNumChoices(self):
            return self.numChoices
        
        def getNumAnswers(self):
            return self.numAnswers

class Anchor:

    class Center:
        pass
    
    class TopRight:
        pass

    class TopLeft:
        pass

    class BottomRight:
        pass

    class BottomLeft:
        pass

    class TopCenter:
        pass

    class BottomCenter:
        pass

    class RightCenter:
        pass

    class LeftCenter:
        pass

class Screen:
    pass

class Label:
    
    class Text:
        pass

    class Image:
        pass

    class Inactive:
        pass

class TextAlignment:

    class Left:
        pass

    class Right:
        pass

    class Center:
        pass