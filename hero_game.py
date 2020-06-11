from sys import exit
from random import randint
from textwrap import dedent

user = []
death_quotes = ['"If you are interested in what you do, that keeps you going." -Stan Lee',
'"I guess one person can make a difference." -Stan Lee',
'"It\'s not who I am underneath, but what I do that defines me." -Batman',
'"If there is nothing but what we make in this world, brothers... let us make it good." -Beta Ray Bill',
'"A hero can be anyone. Even a man doing something as simple and reassuring as putting a coat around \na little boy\'s shoulders to let him know that the world hasn\'t ended." -Ben Affleck',
]
dead = randint(0, 4)

class Combat(object):

	def die_roll(self):
		roll = randint(1, 20)
		print("You rolled: ", roll)
		if roll == 20:
			return roll + 100
		return roll

class Scene(object):

	def enter(self):
		return 'beginning'

class Beginning(Scene):

	def enter(self):
		print("\t\t\t******WELCOME TO YOUR SUPERHERO ADVENTURE******")
		print("\nBefore we begin, let's create your Superhero!")
		name = input("What is your Superhero name? ")
		print(dedent("""
			Super Powers:
			\t*Super Strength (+6 damage, -3 evasion)
			\t*Elemental (+3 damage, +3 evasion)
			\t*Flight (-1 damage, +4 evasion)
			\t*Invisibility (-2 damage, +5 evasion)
			\t*Super Speed (+0 damage, +8 evasion)
			\t*More selections coming soon!
			"""))
		superpower = input("What is your Super Power? ")
		user.append(name)
		Character.ability(self, superpower)
		return 'HQ'

class HQ(Scene):

	def enter(self):
		print(dedent(f"""
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

	(((WARNING: Minions of Toxin detected in facility!)))
	((({user[0]}, please respond immediately!)))

	You rush down to the lobby to find 3 large men equipped with
guns and some shoddy body-armor. What do you do?
"""))

		action = input("> ")

		if action == "fight":
			roll = Character.roll(self, 'fight')

			if roll < 10:
				print(">>You knock out the first henchman, but the 2nd one catches you off guard and kicks your feet out from under you.")
				input("Roll again for damage.")
				roll = Character.roll(self, 'fight')

				if roll < 14:
					print(">>The 2nd henchman manages to hold you down and strangles you.")
					return 'hero_death'

				else:
					print(">>It was a close call, but you knock out the last 2 henchmen just in time.")
					return 'lobby'

			else:
				print(dedent(f"""
					>>You use your {user[1]} to knock out the 3 bad guys with
					ease. These are hardly any kind of challenge for a person
					of your talent.
					"""))
				return 'lobby'

		elif action == "evade":
			roll = Character.roll(self, 'evade')

			if roll < 10:
				print(">>You attempt to get past the henchmen, but they manage to shoot you.")
				return 'hero_death'

			else:
				print(dedent(f"""
					>>Because of their slowness both physically and mentally,
					you slip by the henchmen using your {user[1]}.
					"""))
				return 'lobby'

		else:
			print(">>You wake up from a bad dream in the HQ.")
			return 'hero_death'

class Lobby(Scene):

	def enter(self):
		print(dedent("""
		\t\t\t****CITY STREETS****
			Upon exiting the front doors, you see chaos has struck! Men, women,
		and children are attempting to flee from another 2 henchmen, a
		helicopter is smoking as it struggles to stay in the air, and a
		convenient manhole is left open leading to the sewers where
		Toxin tends to hide.
		What do you do?
		"""))

		action = input("> ")

		if action == "fight":
			print(">>You charge head-on into the 2 henchmen for a fight!")
			roll = Character.roll(self, 'fight')

			if roll < 8:
				print(">>As you run in, one of the minions sees you and throws a gas grenade at you before you get there slowing you down.")
				input("Press [ENTER] to roll again.")
				roll = Character.roll(self, 'fight')

				if roll < 14:
					return 'hero_death'

				else:
					print(">>It was a close fight, but you managed to save the family.")
					return 'bunker'

			else:
				print(">>You've trained for these moments countless times and you defeat the henchmen.")
				return 'bunker'

		elif action == "civilians":
			print(">>A little ways down the street you see a family crouched down hiding behind a wrecked car.")
			roll = Character.roll(self, 'evade')

			if roll < 10:
				print(">>As you take off towards the family, another explosion knocks you back as poisonous gas fills the air.")
				return 'hero_death'

			else:
				print(">>Just in the knick of time, you get the family to safety before an explosion tosses the car up into the air.")
				return 'bunker'

		elif action == "helicopter":
			return 'helicopter'

		elif action == "sewer":
			return 'sewer'

		else:
			print(">>Innocent people are being attacked. What do you do?")
			return 'lobby'

class Sewer(Scene):

	def enter(self):
		print(dedent("""
		\t\t\t****SEWERS****
			You hear the voices and screams of citizens on the streets fading away as you descend.
		The last cry for help you hear is a daughter screaming out, 'Why would they leave us?'

			The ladder going down the sewer collapses and you fall into a mixture of chemicals below
		that Toxin has pre-staged for his plan to poison the city.

			You die in the poison...
		"""))
		return 'hero_death'

class Helicopter(Scene):

	def enter(self):
		print(dedent("""
		\t\t\t****HELICOPTER****
			The helicopter's tail rotor is billowing out black smoke as it slowly begins to spiral
		out of control. Based on its' accelerating descent, you only have a matter of seconds
		until the pilots have an unpleasant meeting with the concrete streets below. You realize
		that you can either save the pilots and risk the helicopter hurting someone below, or
		attempt to bring the helicopter down safely.
		"""))

		choice = input("Who do you save: ")

		if choice == "pilots":
			print("\n>>You pick the safe method and fly in to quickly rescue the pilots.")
			roll = Character.roll(self, 'evade')

			if roll < 8:
				print("\n>>You don't make it in time and find out how dangerous helicopter blades are.")
				return 'hero_death'

			else:
				print("\n>>You narrowly pull the pilots out and bring them down safely as the helicopter crashes.")
				return 'bunker'

		elif choice == "helicopter":
			print("\n>>You take in a big breath as you rush in to try and slow the helicopter's descent.")
			roll = Character.roll(self, 'evade')

			if roll < 14:
				print("\n>>The weight of the helicopter and its' spinning is too much to control. \n>>You go down with the pilots into a ball of flame and helicopter rotors.")
				return 'hero_death'

			else:
				print("\n>>Your training has saved the pilots and innocent lives below! \n>>You somehow manage to control the helicopter and set it down safely.")
				return 'bunker'

class Bunker(Scene):

	def enter(self):
		print(dedent("""
		You see a minion running away into a hidden doorway and take chase.
		You haven't seen this secret entryway before, but I guess that's
		what makes it a 'hidden' doorway...
		"""))
		input("Press [ENTER] to continue.")
		print(dedent(f"""
		\t\t\t****BUNKER****
			You hear faint sounds of electrical machines buzzing and whirring at the bottom of a
		long set of descending stairs. It grows louder as you descend and you begin to also
		hear a mixture of maniacal laughing and coughing.

		\t'Come out and see my beautiful invention {user[0]}!'
		\tsays Toxin as he greets you wearing a yellow lab coat with
		\tpurple gloves and gas mask. His voice is muffled, but you
		\tcan still see the neon green tint in his eyes.
		\t'Let's play a game... You show me your 'super powers' and I'll
		\tshow you my latest creation! Behold! I call it 'Doomsday'!
		\tI know I know... it's not that creative, but then again,
		\tnot many people will be alive to even know its' name!'

			Through his eyes, you can sense his crazed grin from ear-to-ear. You charge in!
		What do you do?
		"""))

		choice = input("> ")
		if choice == "fight":
			roll = Character.roll(self, 'fight')

			if roll > 6:
				print("\n>>You rush in and knock Toxin off his feet before he can let out another quip.")
				print("What do you do?")
				choice = input("> ")

				if choice == "fight":
					roll = Character.roll(self, 'fight')

					if roll > 10:
						print("\n>>Just as he gets up, you freeze his feet in place and deliver another blow to his mask.")
						input("Press [ENTER] to roll for damage again.")
						roll = Character.roll(self, 'fight')

						if roll > 14:
							print("\n>>Toxin loses his balance and tumbles backwards into a cart of liquid chemicals as his mask flies off his head.")
							return 'last_scene'

						else:
							print("\n>>Right when you think you have the upper hand, Toxin sidesteps your next swing and you fly into a gas canister of deadly fumes which immediately engulf you.")
							return 'hero_death'

					else:
						print("\n>>Toxin gathers his composure just enough to reach into his pocket and grab a remote control and then pushes a button.")
						return 'hero_death'

				else:
					print("\n>>Toxin hits back with a counter-attack throwing a powder across the room that burns your eyes.")
					input("Press [ENTER] to roll for damage again.")
					roll = Character.roll(self, 'fight')

			else:
				print("\n>>Toxin knocks your feeble attempt at an attack away as he sprays a chemical in your face.")
				input("Press [ENTER] to roll for damage again.")
				roll = Character.roll(self, 'fight')

				if roll >= 12:
					print("\n>>As the chemical seeps into your eyes, you manage to plow into Toxin knocking him down.")
					input("Press [ENTER] to roll for damage again.")
					roll = Character.roll(self, 'fight')

				else:
					print("\n>>You rush in and miss due to your eyesight being hindered. Blindly swinging, you strike a gas canister and deadly fumes fill your lungs.")
					return 'hero_death'

		elif choice == "talk":
			print("""
			\n\t'You think you can convince me to not wreck havoc on the world?! Nice try...'
			>>Toxin reaches for an obnoxiously large red button on a control panel.
			What do you do?
			""")
			choice = input("> ")

			if choice == "fight":
				roll = Character.roll(self, 'fight')

				if roll < 10:
					print("\n>>You go to stop him, but you trip on a crack in the floor...")
					return 'hero_death'

				else:
					print("\n>>Just as Toxin reaches the button, you whip him back against the wall.")
					input("Press [ENTER] to roll for damage again.")
					roll = Character.roll(self, 'fight')

					if roll < 10:
						print("\n>>Toxin pulls out a remote control from his pocket, grins, and hits the button.")
						return 'hero_death'

					else:
						print("\n>>Toxin reaches for his pocket, but before he can do so, you knock him unconscious.")
						return 'last_scene'

			elif choice == "talk":
				print("\n\t'Seriously? You still want to talk? I'm literally pushing the button right now...")
				return 'hero_death'

			else:
				print("\n>>You stand there motionless. Toxin looks at you confused and then presses the button.")
				return 'hero_death'

		else:
			print("\n>>You stand there motionless. Toxin looks at you confused and then presses the button.")
			return 'hero_death'

class Final_Fight(Scene):

	def enter(self):
		print(dedent("""
			Toxin lays on the ground hunched over with his back towards you. His muffled coughs echo through
		the concrete bunker, but it slowly turns into crazed laughter...

		\t'Heh, you thought you could stop me this time? I knew you'd
		\ttry your usual tricks.'
		\tToxin reaches into his labcoat pocket and pulls out a remote
		\tcontrol and holds his thumb down on the button.
		\t'This is called a dead man's switch. Meaning if I let go, BOOM!'
		What do you do?
		"""))
		choice = input("> ")

		if choice == user[1]:
			print(dedent(f"""
			>>With only a flash of light, you zip to his hand and grab the detonator with your {user[1]} before he can let go.
			Toxin continues chuckling with his empty hand in the air. He slowly looks at his hand and you just hear a soft
			murmuring through his mask as he hunches over and puts his hands out in front to be clasped together.

			\t'Why... why did I not see that one coming...' he groans.
			"""))
			return 'last_scene'

		else:
			print(">>Before you can react, Toxin lifts his thumb as you hear a ground shattering explosion above ground.")
			print(">>The lights flicker, bits of the walls and ceiling crumble...")
			return 'hero_death'

class Hero_Death(Scene):

	def enter(self):
		print("\n\tYour attempt to save the citizens has been spoiled.")
		print(death_quotes[dead])
		print("\n\tWould you like to try again? Yes or No")
		choice = input("> ")
		if choice == "Yes":
			return 'HQ'
		elif choice == "No":
			exit()
		else:
			print("I don't understand that command.")
			return 'hero_death'

class Last_Scene(Scene):

	def enter(self):
		print("\n\t\tYou have once again saved the day!")
		print(f"\t\tCongratulations {user[0]}!")
		exit()

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Map(object):

	scenes = {
		'beginning': Beginning(),
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

class Character(Combat):

	def __init__(self, ability):
		self.ability = ability

	def roll(self, option):
		self.option = option
		if option == 'fight':
			roll = Combat.die_roll(self) + user[2]
			return roll

		else:
			roll = Combat.die_roll(self) + user[3]
			return roll

	def ability(self, superpower):
		if superpower == "Super Strength":
			user.append("unbelievable strength")
			user.append(6)
			user.append(-3)

		elif superpower == "Elemental":
			user.append("fire ball")
			user.append(3)
			user.append(3)

		elif superpower == "Flight":
			user.append("ability to fly")
			user.append(-1)
			user.append(4)

		elif superpower == "Invisibility":
			user.append("invisibility")
			user.append(-2)
			user.append(5)

		elif superpower == "Super Speed":
			user.append("lightning-fast speed")
			user.append(0)
			user.append(8)

		else:
			print("""
			Please select one of the following powers:
			*Super Strength
			*Flight
			*Elemental
			*Invisibility
			*Super Speed
			""")

a_map = Map('beginning')
a_game = Engine(a_map)
a_game.play()
