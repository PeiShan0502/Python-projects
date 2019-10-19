from hungry_games import *


class Weapon(Thing):
    """ This is a class to model weapons in The Hunger Games,
        inherited from the Thing class (in hunger_games.py) """
            
    def __init__(self, name, min_dmg, max_dmg):
        """ The constructor for Weapon class.

        Parameters:
        name: inherited from Thing superclass
        min_dmg: The minimum damage inflicted by the weapon.
        max_dmg: The maximum damage inflicted by the weapon. """
        
        super().__init__(name)    
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def min_damage(self):
        return self.min_dmg

    def max_damage(self):
        return self.max_dmg

    def damage(self):
        return random.randint(self.min_dmg, self.max_dmg) 




class Ammo(Thing):
    """ This is a class to model ammunition (ammo) in The Hunger Games,
        inherited from the Thing class (in hunger_games.py) """
    
    def __init__(self, name, weapon, qty):
         """ The constructor for Ammo class.

        Parameters:
        name: inherited from Thing superclass
        weapon: Name of weapon that this ammo is for
        qty: Quantity of ammo available """

         super().__init__(name)
         self.weapon = weapon
         self.qty = qty

    def get_quantity(self):
        return self.qty

    def weapon_type(self):
        return self.weapon.get_name()

    def remove_all(self):   
        self.qty = 0
        return self.qty




class RangedWeapon(Weapon):
    """ This is a class to model a ranged weapon in The Hunger Games,
        inherited from the Weapon class. """
    
    def __init__(self, name, min_dmg, max_dmg):
        """ The constructor for RangedWeapon class.

    Parameters:
        name: inherited from Weapon superclass
        min_dmg: The minimum damage inflicted by the weapon (inherited from Weapon superclass)
        max_dmg: The maximum damage inflicted by the weapon (inherited from Weapon superclass) """
        
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0                # A newly created RangedWeapon start with zero shots.

    def shots_left(self):
        return self.shots

    def load(self, ammo):
        """ Loads ammo if ammo is suitable for the weapon. E.g. arrows(ammo) for a bow (weapon) 
            Else, there is no effect on Ammo or RangedWeapon. """  
             
        if self.get_name() == ammo.weapon_type(): 
            self.shots += ammo.get_quantity()
            ammo.remove_all()
        else:
            pass                      # No effect if ammo is of the wrong type

    def damage(self):
        if self.shots_left() == 0:
            return 0                  # RangedWeapon cannot deal any damage if there are no shots left.
        else:
            self.shots -= 1
            return super().damage()   # from Weapon superclass 




