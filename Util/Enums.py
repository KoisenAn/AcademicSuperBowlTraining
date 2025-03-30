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

        def __init__(self, numTextboxes, firstInputBoxText, secondInputBoxText=None, thirdInputBoxText=None):
            self.textboxes = numTextboxes
            self.firstInputBoxText = firstInputBoxText
            self.secondInputBoxText = secondInputBoxText
            self.thirdInputBoxText = thirdInputBoxText
            self.inputBoxTextList = [firstInputBoxText, secondInputBoxText, thirdInputBoxText][:numTextboxes-1]

        def getNumTextBoxes(self):
            return self.textboxes
        
        def getInputBoxTextList(self):
            return self.inputBoxTextList

    class MCQ:

        def __init__(self, answerChoices=[], numMCQs=4, numAnswers=1):
            self.answerChoices = answerChoices
            self.numMCQs = numMCQs
            self.numAnswers = numAnswers

        def getAnswerChoices(self):
            return self.answerChoices

        def getNumMCQs(self):
            return self.numMCQs
        
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