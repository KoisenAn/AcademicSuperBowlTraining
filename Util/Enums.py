class Question:

    def __init__(self, text):
        self.text = text

class Answer:
    pass

class ProblemDisplayType:

    class Lines:
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

        def __init__(self, numChoices, firstChoiceText, secondChoiceText, thirdChoiceText=None, fourthChoiceText=None, fifthChoiceText=None, sixthChoiceText=None):
            self.numChoices = numChoices
            self.firstChoiceText = firstChoiceText
            self.secondChoiceText = secondChoiceText
            self.thirdChoiceText = thirdChoiceText
            self.fourthChoiceText = fourthChoiceText
            self.fifthChoiceText = fifthChoiceText
            self.sixthChoiceText = sixthChoiceText
            self.choicesTextList = [firstChoiceText, secondChoiceText, thirdChoiceText, fourthChoiceText, fifthChoiceText, sixthChoiceText][:numChoices-1]

        def getNumChoices(self):
            return self.numChoices    
        
        def getChoicesTextList(self):
            return self.choicesTextList
        
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