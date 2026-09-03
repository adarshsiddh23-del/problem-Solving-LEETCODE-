class Solution:
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")