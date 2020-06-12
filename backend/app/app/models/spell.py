from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Spell(Base):
    id = Column(Integer)
    title = Column(String, index=True)
    description = Column(String, index=True)
    book = Column(String)
    page = Column(Integer)
    components_verbal = Column(String)
    components_somatic = Column(String)
    components_material = Column(String)
    components_materials_needed = Column(String)
    components_raw = Column(String)
    level = Column(Integer)
    school = Column(String)
    classes_class = Column(String)
    casting_range = Column(Integer)
    casting_self = Column(String)
    casting_casting_time = Column(Integer)
    casting_action_type = Column(String)
    casting_duration = Column(Integer)
    casting_ritual = Column(String)
    casting_concentration = Column(String)
    casting_touch = Column(String)
    casting_sight = Column(String)
    higher_level = Column(String)
    classes_subclasses = Column(String)
    classes_class_level = Column(Integer)
    races_race = Column(String)
    races_subraces = Column(String)
    races_race_level = Column(Integer)
