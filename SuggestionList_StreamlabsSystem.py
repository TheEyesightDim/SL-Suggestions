#imported dependencies
import os
import codecs
from datetime import date

#required script info
ScriptName = "Stream Suggestion List"
Website = "https://www.twitch.tv/orthogonality"
Description = "Allows users to suggest games and other things, which are saved to a text file for future reference."
Creator = "Orthogon"
Version = "1.1.3"
#TODO: Add cooldown timers

#script globals and definitions
class SuggestionList:
  def __init__(self, filepath=None, command='!suggest'):
    self.trigger = command + ' '
    self.filename = filepath if filepath and os.path.isfile(filepath) else os.path.join(os.path.dirname(__file__), 'suggestions.txt')
    return

  def add(self, username, suggestion):
    suggestion = (suggestion[:80] + '...') if len(suggestion) > 80 else suggestion
    line = username + ' suggested ' + suggestion + ' on ' + date.today().isoformat() + '\n'
    self.save(line)
    return

  #Don't call this, for internal use only
  def save(self, strLine):
    with codecs.open(self.filename, 'a+', 'utf-8') as file:
      file.write(strLine)
    return


#script initialization
def Init():
  global suggestions
  suggestions = SuggestionList()
  return

#script functions
def Execute(data):
  if data.IsChatMessage() and data.IsFromTwitch():
    if data.Message.lower().startswith(suggestions.trigger.lower()):
      message = data.Message.replace(suggestions.trigger, '', 1)
      suggestions.add(data.UserName, message)
      Parent.SendStreamMessage(data.UserName + ' has nominated \"' + message + '\" for the backlog.')
  return

def Tick():
  return

def Parse(parseString, userID, username, targetID, targetName, message):
  return

def ReloadSettings(jsonData):
  return

def ScriptToggled(isTurnedOn):
  return

def Unload():
  return

