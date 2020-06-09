from sys import exit
from random import randint
from textwrap import dedent

class Combat(object):

	def die_roll(self, roll):
		roll = rand.int(1, roll)
		return roll

class Scene(object):

	def enter(self):
		return 'HQ'

class HQ(Scene):

	def enter(self):
		print(dedent("""
            ******** SUPERHERO HEADQUARTERS********

    You find yourself lounging around enjoying a nice lengthy
period of peace in the city. One of your teammates recommended
that you watch the latest series on TV, something called
'King of Tigers'? Either way, you have the compound all to yourself
as the rest of your team has either gone to take a calm vacation
or ran out to help their local communities.

    Without any warning, an ear-shattering explosion and trembling
of the building knocks you off the couch. Almost immediately
the automated security system kicks in announcing boldly,

        (((WARNING: Minions of Toxin detected in facility.)))

You rush down to the lobby to find 3 large men equipped with
guns and some shoddy body-armor.
"""))

		action = input("> ")

		if action == "fight":
			Combat.die_roll()

			if roll <= 10:
				print("You knock out the first henchman, but the 2nd one catches you off guard.")
				Combat.die_roll()

				if roll <= 14:
					print("The 2nd henchman manages to hold you down and strangles you.")
					return 'hero_death'

				else:
					print("It was a close call, but you knock out the last 2 henchmen just in time.")
					return 'lobby'

			else:
				print(dedent(f"""
                    You use your {ability} to knock out the 3 bad guys with
                    ease. These are hardly any kind of challenge for a person
                    of your talent.
                    """))
				return 'lobby'

		elif action == "evade":
			Combat.die_roll()

			if roll <= 10:
				print("You attempt to get past the henchmen, but they manage to shoot you.")
				return 'hero_death'

			else:
				print(dedent(f"""
				      Because of their slowness both physically and mentally,
                      you slip by the henchmen using your {ability}.
                      """))
				return 'lobby'

		else:
			print("You wake up from a bad dream in the HQ.")
			return 'HQ'

class Lobby(Scene):

	def enter(self):
		print(dedent("""
			Upon exiting the front doors, you see chaos has struck! Men, women,
			and children are attempting to flee from another 2 henchmen, a
			helicopter is smoking as it struggles to stay in the air, and a
			convenient manhole is left open leading to the sewers where
			Toxin tends to hide.
			"""))

		action = input("> ")

		if action == "fight":
			print("You charge head-on into the 2 henchmen for a fight!")
			combat.die_roll()

			if roll <= 8:
				combat.die_roll()

				if roll <= 14:
					return 'hero_death'

				else:
					print("It was a close fight, but you managed to save the family.")
					return 'bunker'

			else:
				print("You've trained for these moments countless times and you defeat the henchmen.")
				return 'bunker'

		elif action == "civilians":
			print("A little ways down the street you see a family crouched down hiding behind a wrecked car.")
			combat.die_roll()

			if roll <= 10:
				print("As you take off towards the family, another explosion knocks you back as poisonous gas fills the air.")
				return 'hero_death'

			else:
				print("Just in the knick of time, you get the family to safety before an explosion tosses the car up into the air.")
				return 'bunker'

		elif action == "helicopter":
			return 'helicopter'

		elif action == "sewer":
			return 'sewer'

		else:
			print("Innocent people are being attacked. What do you do?")
			return 'lobby'

class Sewer(Scene):

	def enter(self):
		print(dedent("""
			You hear the voices and screams of citizens on the streets fading away as you descend.
			The last cry for help you hear is a daughter screaming out, 'Why would they leave us?'
			"""))
		return 'hero_death'

class Helicopter(Scene):

	def enter(self):
		print(dedent("""
			The helicopter's tail rotor is billowing out black smoke as it slowly begins to spiral
			out of control. Based on its' accelerating descent, you only have a matter of seconds
			until the pilots have an unpleasant meeting with the concrete streets below. You realize
			that you can either save the pilots and risk the helicopter hurting someone below, or
			attempt to bring the helicopter down safely.
			"""))

		choice = input("Who do you save: ")

		if choice == "pilots":
			print("You pick the safe method and fly in to quickly rescue the pilots.")
			Combat.die_roll()

			if roll <= 8:
				print("You don't make it in time and find out how dangerous helicopter blades are.")
				return 'hero_death'

			else:
				print("You narrowly pull the pilots out and bring them down safely as the helicopter crashes.")
				return 'bunker'

		elif choice == "helicopter":
			print("You take in a big breath as you rush in to try and slow the helicopter's descent.")
			Combat.die_roll()

			if roll <= 14:
				print("The weight of the helicopter and its' spinning is too much to control. You go down with the pilots into a ball of flame and helicopter rotors.")
				return 'hero_death'

			else:
				print("Your training has saved the pilots and innocent lives below! You somehow manage to control the helicopter and set it down safely.")
				return 'bunker'

class Bunker(Scene):

	def enter(self):
		print(dedent("""
			You see a minion running away into a hidden doorway and take chase. You haven't seen
			this secret entryway before, but I guess that's what makes it a 'hidden' doorway.

			You hear faint sounds of electrical machines buzzing and whirring at the bottom of a
			long set of descending stairs. It grows louder as you descend and you begin to also
			hear a mixture of maniacal laughing and coughing.

			'Come out and see my beautiful invention!' says Toxin as he greets you wearing a
			yellow lab coat with purple gloves and gas mask. His voice is muffled, but you can
			still see the neon green tint in his eyes.

			'Let's play a game... You show me your 'super powers' and I'll show you my latest
			creation! Behold! I call it 'Doomsday'! I know... it's not that creative, but then
			again, not many people will be alive to even know it's name!'

			Through his eyes, you can sense his crazed grin from ear-to-ear. You charge in!
			"""))

		Combat.die_roll()

		if roll >= 6:
			print("You rush in and knock Toxin off his feet before he can let out another quip.")
			Combat.die_roll()

			if roll >= 10:
				print("Just as he gets up, you freeze his feet in place and deliver another blow to his mask.")
				Combat.die_roll()

				if roll >= 12:
					print("Toxin loses his balance and tumbles backwards into a cart of liquid chemicals as his mask flies off his head.")
					return 'last_scene'

				else:
					print("Right when you think you have the upper hand, Toxin sidesteps your next swing and you fly into a gas canister of deadly fumes which immediately engulf you.")
					return 'hero_death'

			else:
				print("Toxin hits back with a counter-attack throwing a powder across the room that burns your eyes.")
				Combat.die_roll()

		else:
			print("Toxin knocks your feeble attempt at an attack away as he sprays a chemical in your face.")
			Combat.die_roll()

			if roll >= 12:
				print("As the chemical seeps into your eyes, you manage to plow into Toxin knocking him down.")
				Combat.die_roll()

			else:
				print("You rush in and miss due to your eyesight being hindered. Blindly swinging, you strike a gas canister and deadly fumes fill your lungs.")
				return 'hero_death'

class Hero_Death(Scene):

    def enter(self):
        print("You tried...")

class Last_Scene(Scene):

	def enter(self):
		print("You have once again saved the day!")

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # be sure to print out the last scene
            current_scene.enter()

class Map(object):

    scenes = {
        'HQ': HQ(),
        'lobby': Lobby(),
        'sewer': Sewer(),
        'helicopter': Helicopter(),
        'bunker': Bunker(),
        'last_scene': Last_Scene(),
        'hero_death': Hero_Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('HQ')
a_game = Engine(a_map)
a_game.play()
