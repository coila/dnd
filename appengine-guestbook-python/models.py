from google.appengine.ext import ndb


class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
 
 
class CharacterSheet(ndb.Model):
  """Create a base class for character sheets."""

  character_name = ndb.StringProperty()
  player_name = ndb.StringProperty()
  class_type = ndb.StringProperty()
  level = ndb.IntegerProperty()
  race = ndb.StringProperty()
  alignment_law = ndb.StringProperty()
  alignment_moral = ndb.StringProperty()
  deity = ndb.StringProperty()
  size = ndb.StringProperty()
  age = ndb.IntegerProperty()
  gender = ndb.StringProperty()
  height = ndb.StringProperty()
  weight = ndb.IntegerProperty()
  weight_units = ndb.StringProperty()
  eye_color = ndb.StringProperty()
  hair_color = ndb.StringProperty()
  skin_color = ndb.StringProperty()
  hit_points = ndb.IntegerProperty()
  armor_class = ndb.StructuredProperty(Armor)
  initiative = ndb.IntegerProperty()
  speed = ndb.IntegerProperty()
  speed_units = ndb.StringProperty()
  strength = ndb.StructuredProperty(Ability)
  dexterity = ndb.StructuredProperty(Ability)
  constitution = ndb.StructuredProperty(Ability)
  intelligence = ndb.StructuredProperty(Ability)
  wisdom = ndb.StructuredProperty(Ability)
  charisma = ndb.StructuredProperty(Ability)
  skills = ndb.StructuredProperty(AllTheSkills)



class Ability(ndb.Model):
  """Ability class."""
  name = ndb.StringProperty()
  score = ndb.IntegerProperty()
  modifier = ndb.IntegerProperty()
  temp_score = ndb.IntegerProperty()
  temp_modifier = ndb.IntegerProperty()
  


class AllTheSkills(ndb.Model):
  """Group of skills."""
  untrained_skills = [
      "appraise",
      "balance",
      "bluff",
      "climb",
      "concentration",
      "craft_one",
      "craft_two",
      "craft_three",
      "diplomacy",
      "disguise",
      "escape_artist",
      "forgery",
      "gather_information",
      "heal",
      "hide",
      "intimidate",
      "jump",
      "listen",
      "move_silently",
      "ride",
      "search",
      "sense_motive",
      "spot",
      "survival",
      "swim",
      "use_rope",
  ]

  appraise = ndb.StructuredProperty(SkillsBase)
  balance = ndb.StructuredProperty(SkillsBase)
  bluff = ndb.StructuredProperty(SkillsBase)
  climb = ndb.StructuredProperty(SkillsBase)
  concentration = ndb.StructuredProperty(SkillsBase)
  craft_one = ndb.StructuredProperty(SkillsBase)
  craft_two = ndb.StructuredProperty(SkillsBase)
  craft_three = ndb.StructuredProperty(SkillsBase)
  decipher_script = ndb.StructuredProperty(SkillsBase)
  diplomacy = ndb.StructuredProperty(SkillsBase)
  disable_device = ndb.StructuredProperty(SkillsBase)
  disguise = ndb.StructuredProperty(SkillsBase)
  escape_artist = ndb.StructuredProperty(SkillsBase)
  forgery = ndb.StructuredProperty(SkillsBase)
  gather_information = ndb.StructuredProperty(SkillsBase)
  handle_animal = ndb.StructuredProperty(SkillsBase)
  heal = ndb.StructuredProperty(SkillsBase)
  hide = ndb.StructuredProperty(SkillsBase)
  intimidate = ndb.StructuredProperty(SkillsBase)
  jump = ndb.StructuredProperty(SkillsBase)
  knowledge_one = ndb.StructuredProperty(SkillsBase)
  knowledge_two = ndb.StructuredProperty(SkillsBase)
  knowledge_three = ndb.StructuredProperty(SkillsBase)
  knowledge_four = ndb.StructuredProperty(SkillsBase)
  knowledge_five = ndb.StructuredProperty(SkillsBase)
  listen = ndb.StructuredProperty(SkillsBase)
  move_silently = ndb.StructuredProperty(SkillsBase)
  open_lock = ndb.StructuredProperty(SkillsBase)
  perform_one = ndb.StructuredProperty(SkillsBase)
  perform_two = ndb.StructuredProperty(SkillsBase)
  perform_three = ndb.StructuredProperty(SkillsBase)
  profession_one = ndb.StructuredProperty(SkillsBase)
  profession_two = ndb.StructuredProperty(SkillsBase)
  ride = ndb.StructuredProperty(SkillsBase)
  search = ndb.StructuredProperty(SkillsBase)
  sense_motive = ndb.StructuredProperty(SkillsBase)
  sleight_of_hand = ndb.StructuredProperty(SkillsBase)
  spellcraft = ndb.StructuredProperty(SkillsBase)
  spot = ndb.StructuredProperty(SkillsBase)
  survival = ndb.StructuredProperty(SkillsBase)
  swim = ndb.StructuredProperty(SkillsBase)
  tumble = ndb.StructuredProperty(SkillsBase)
  use_magic_device = ndb.StructuredProperty(SkillsBase)
  use_rope = ndb.StructuredProperty(SkillsBase)
  other_one = ndb.StructuredProperty(SkillsBase)
  other_two = ndb.StructuredProperty(SkillsBase)
  other_three = ndb.StructuredProperty(SkillsBase)

  def __init__(self):
    """Sets up base requirements.""" 

 
class Armor(ndb.Model):
 """Armor class."""
 class_type = ndb.StringProperty()
 touch = ndb.StringProperty()
 flat_footed = ndb.StringProperty()
  

class Attack

class SkillsBase(ndb.Model):
  """Skills base class."""
  name = ndb.StringProperty() # eg. Knowledge
  skill_type = ndb.StringProperty() # eg. (Geography)
  key_ability = ndb.StringProperty() # eg. INT
  ranks = ndb.StringProperty()
  temp_score = ndb.IntegerProperty()
  temp_modifier = ndb.IntegerProperty()
  training_not_required = ndb.BooleanProperty()
  character_class_skill = ndb.BooleanProperty()
