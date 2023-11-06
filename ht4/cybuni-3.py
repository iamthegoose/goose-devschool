# class Warrior:
#     def __init__(self):
#         self.level = 1
#         self.experience = 100
#         self.rank = "Pushover"
#         self.achievements = []

#     def battle(self, enemy_level):
#         if enemy_level <= 0 or enemy_level > 100:
#             return "Invalid level"

#         diff = enemy_level - self.level
#         if diff == 0:
#             self.experience += 10
#             self.update_level()
#             return "A good fight"
#         elif diff == -1:
#             self.experience += 5
#             self.update_level()
#             return "A good fight"
#         elif diff >= -2:
#             self.update_level()
#             return "An easy fight"
#         elif diff == 1:
#             self.experience += 20
#             self.update_level()
#             return "A good fight"
#         elif diff <= 2:
#             self.experience += 20 * abs(diff) * abs(diff)
#             self.update_level()
#             return "An intense fight"
#         else:
#             return "You've been defeated"
             
#     def update_level(self):
#         self.level = self.experience // 100 + 1 if self.experience % 100 != 0 else self.experience // 100
#         self.level = min(self.level, 100)  # Максимальний рівень 100

#         rank_tiers = [
#             "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
#             "Elite", "Conqueror", "Champion", "Master", "Greatest"
#         ]

#         self.rank = rank_tiers[min(self.level // 10, len(rank_tiers) - 1)]

#     def training(self, training_list):
#         if len(training_list) != 3:
#             return "Invalid training parameters"

#         achieve, exp_points, required_level = training_list

#         if self.level < required_level:
#             return "Not strong enough"

#         self.experience += exp_points
#         self.achievements.append(achieve)
#         self.update_level()

#         return achieve