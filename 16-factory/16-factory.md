## IN608
## Intermediate Application Development

## Session 16 :  The Factory Method and Abstract Factory Patterns

### Introduction
Today we're looking at two distinct patterns with similar names. On reason were doing this is to make it clear to everyone that these are *two distinct patterns*. It also turns out that I don't like these patterns very much. But that's not because they're bad patterns. It's just that I have seen them misused enough to raise my hackles when I see them now. Using pattterns does not make us good programmers. Thinking about our problems, recognising that there is an established pattern that addresses it, and implemeting that pattern thoughtfully does.

Let's dig into the first one.

---

### The Factory Method Pattern

"Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses." (*GoF*)

That didn't really help our understanding of this pattern, at least not yet. We need an example.

**Our problem**

I work on games that are available around the world. Naturally, we want to be able to present those games to players in their preferred languages. We don't know what language we're going to use until runtime. Clearly we need some sort of translator class.

We can start by looking at the wrong way to do it:
```
  class Translator:
      def localise(self, lang, expression):
          if lang == 'en':
              # load up English language stuff
              # look up expression
              # return English version
          elif lang == 'es':
              # load up Spanish language stuff
              # look up expression
              # return Spanish version
          ...
```
You see where this is going.  What's wrong with this? (Hint: SOLID)

  - What's the process for adding a language? (Open-closed)
  - What if we need to change the "load up X language stuff" process? (Single responsibility)

Here is an improved version, using the Factory Method pattern:

```
  class Translator:
      def localise(self, lang, expression):
          translator = self.get_translator(lang)
          return translator.interpret(expression)
          ...

  # using the Translator
  weather = 'WEATHER.CLOUDY'
  localiser = Translator()
  print(localiser.localise(player.preferred_language, weather))
```

In this version, the key is that `get_translator()` method. It gets us an object that is specific to the requested language. Then we call that object's `interpret()` method to get the translated expression. Note that in this example, `WEATHER.CLOUDY` is just a string key used to look up a specific phrase that we can provide in various languages.

`get_translator()` is the Factory Method that the pattern is named for. It makes the specific class we need at the time we need it. How does `get_translator()` work? 

```
def get_translator(self, lang):
    if lang == 'en':
        return English()
    elif lang == 'es':
        return Spanish()
          ...
    else:
        raise LanguageNotSupportedError(lang)
```
I've said that if-else structures like this are a symptom of Open-Closed problems, but it's permissible if you only have this sort of if-else in **one** place. We can actually avoid the if-else entirely, though.

We will set up a dictionary of language handling classes like this:
```
LANGUAGES = {
  'en':  English,
  'es':  Spanish
}
```
Then, our `get_translator()` can look like this:
```
def get_translator(self, lang):
    try:
        return LANGUAGES['lang']()    
    except KeyError:
        raise LanguageNotSupportedError(lang)
```
Now when we add a new language handling class, we just need to update the `LANGUAGES` dictionary. We could even build that dictionary at runtime by finding the available language handling class definitions.

Now we're mostly done looking at the Factory Method pattern, but let's consider a way we could tak this just a bit further. Suppose my employer gets bought out by Disney. Our new corporate overlords insist that every game include a Jar Jar Binks option where characters speak with Jar Jar's accent thing in whatever language. Suppose also that we come up with an algorithm to take text in an arbitrary language and transform it into the Jar Jar Binks accent. Then we can subclass our `Translator` like this:

```
class JarJarTranslator(Translator):
    def get_translator(self, lang):
        # This would load up the language handler and
        # somehow JarJar-ise it, perhaps with a decorator? 
        # I never said it was a good idea.
```
Notice that we don't have to override the `localise()` method. We just need to change the factory method `get_translator()`.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `16-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `15-practical` directory.
  4. There are two files, `q1.py` and `q2.py`. Work through them now.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problems in `q3.py` and `q4.py` after reading the section below.

---

###  Abstract Factories

The Abstract Factory may be thought of as related to the Factory Method and it sort of is, but it's not a very strong relationship. They are both *creational patterns*, but that may be as far as it goes. 

"Provide an interface for creating *families* of related or dependent objects without specifying their concrete classes." (*Gof*)

The bit about families of objects is the key. With the Factory Method we wanted one object and we weren't too particular about its concrete type. With the Abstract Factory we want families of related objects.

Again, it's best understood by looking at an example.

```
from abc import ABC, abstractmethod

class PetFactory(ABC):

    @abstractmethod
    def get_animal(self):
        pass

    @abstractmethod
    def get_pet_food(self):
        pass

    @abstractmethod
    def get_pet_toy(self):
        pass
```

The idea here is that we're going to decide what kind of pet we want, and then a Factory will get us the appropriate animal with its matching food and toy. For this to work, we need some animals, foods, and toys.

```
class Animal(ABC):
    pass

class Dog(Animal):
    pass

class PetFood(ABC):
    pass

class DogFood(PetFood):
    pass

class PetToy(ABC):
    pass

class Ball(PetToy):
    pass
```
For each type of object we've created an abstract base class and concrete classes corresponding to pet dogs. Now it makes sense to make a concrete child class of `PetFactory` that works for dogs.

```
class DogFactory(PetFactory):

    def get_animal(self):
        return Dog()

    def get_pet_food(self):
        return DogFood()

    def get_pet_toy(self):
        return Ball()
```
Now our `DogFactory` can get you a pet `Dog`, together with the right food and toy for the dog. Here is one way we could use our Abstract Factories:

```
def give_a_pet_to(person, pet_type):
    if pet_type == 'dog':
        factory = DogFactory()
    else:
        raise PetNotSupportedError(pet_type)
    gift = {
        'animal': factory.get_animal(),
        'food': factory.get_food(),
        'toy': factory.get_toy()}
    person.give_pet(gift)
```

Notice how `give_a_pet_to()` looks like a Factory Method? This is one way the two patterns can be connected. Can you see how this can be modified to support cats?

### Some closing thoughts

We've only considered a few design patterns. There are many more patterns out there, both classical ones like those found in GoF, and newer ones emerging all the time. There are also language and problem domain-specific patterns, say for languages like JavaScript or fields like data science. The three important things I want you to take away from this part of the paper are
  1. Apply design thinking to your code to produce something that will be extensible and maintainable for the long haul.
  2. Don't reinvent wheels. When designing your code, check to see if there are well known patterns that address your problems.
  3. Applying patterns is not blindly following a recipe. It's taking a general idea and thinking about how to sensibly adapt it to a particular problem.


