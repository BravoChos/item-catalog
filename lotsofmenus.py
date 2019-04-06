from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, CatalogItem, Category, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Movie for Iron Man
Category1 = Category(user_id=1, name="Iron Man")

session.add(Category1)
session.commit()

CatalogItem1 = CatalogItem(user_id=1, category_id="1", name="Tony Stark", 
  description="Anthony Edward \"Tony\" Stark, simply known as Tony Stark, "
  +"and also known as the famous super-hero named Iron Man, is a character that appears in the Iron Man " 
  +"trilogy films and in The Avengers movie. He was portrayed by actor Robert Downey, Jr., and is based " 
  +"on the character of the same name in the comics.",
  hero="Iron Man", rank="Blaster")

session.add(CatalogItem1)
session.commit()

# Movie for Captin America
Category2 = Category(user_id=1, name="Captin America: The First Avengers")

session.add(Category2)
session.commit()

CatalogItem2 = CatalogItem(user_id=1, category_id="2", name="Steven Rogers", 
  description="Rogers' battle experience and training make him an expert tactician and an excellent field commander, "
  +"with his teammates frequently deferring to his orders in battle. Thor has stated that Rogers is one of the very "
  +"few humans he will take orders from. Rogers' reflexes and senses are extraordinarily keen. He has blended Aikido, "
  +"Boxing, Judo, Karate, Jujutsu, Kickboxing, and gymnastics into his own unique fighting style and is a master of "
  +"multiple martial arts. Years of practice with his near-indestructible shield make him able to aim and throw it with "
  +"almost unerring accuracy. His skill with his shield is such that he can attack multiple targets in succession with "
  +"a single throw or even cause a boomerang-like return from a throw to attack an enemy from behind.", 
  hero="Captin America", rank="Tactician")

session.add(CatalogItem2)
session.commit()

# Movie for Docter Strange
Category3 = Category(user_id=1, name="Doctor Strange")

session.add(Category3)
session.commit()

CatalogItem3 = CatalogItem(user_id=1, category_id="3", name="Stephen Vincent Strange", 
  description="Doctor Strange is a practicing magician who draws his powers from mystical entities such as Agamotto, "
  +"Cyttorak, Ikonn, Oshtur, Raggadorr, and Watoomb, who lend their energies for spells.[56] Strange also wields mystical "
  +"artifacts including the Cloak of Levitation which enables him to fly;[note 1] the Eye of Agamotto, an amulet whose light "
  +"is used to negate evil magic;[50] the Book of the Vishanti, a grimoire which contains vast knowledge of white magic "
  +"and the Orb of Agamotto, a crystal ball which is used for clairvoyance."
  +"In addition to his magical abilities, Strange is trained in several martial arts disciplines,"
  +"including Judo, and has shown proficiency with numerous magically conjured weapons including swords and axes. "
  +"Strange was a skilled neurosurgeon before nerve damage impaired his hands.",
  hero="Doctor Strange", rank="Sorcer")

session.add(CatalogItem3)
session.commit()

# Movie for Captin
CatalogItem4 = CatalogItem(user_id=1, category_id="2", name="Bucky Barnes", 
  description="Having trained under Steve Rogers (the original Captain America in World War II) and others in the time "
  +"leading up to World War II, \"Bucky\" Barnes is a master of hand-to-hand combat and martial arts, as well as being skilled "
  +"in the use of military weapons such as firearms and grenades. He also used throwing knives on occasion and was a gifted "
  +"advance scout. His time as the covert Soviet agent known as the Winter Soldier helped to further hone his skills, making "
  +"him the equal to his predecessor in combat skills and an expert assassin and spy. He is also fluent in many languages, "
  +"including English, Spanish, Portuguese, German, Russian, Latin, and Japanese.[volume & issue needed] He can understand French.",
  hero="Winter Soldier", rank="Specialist")

session.add(CatalogItem4)
session.commit()

Category5 = Category(user_id=1, name="Black Panther")

session.add(Category5)
session.commit()

print "added menu items!"
