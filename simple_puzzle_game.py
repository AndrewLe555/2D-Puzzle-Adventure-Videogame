"""
Inspired by DaFluffyPotato and Tech with Tim.
References to Monty Python, The Legend of Zelda, Tommy Tutone, and Bob Ross
"""

import pygame
import pygame.camera
import sys
import math

pygame.init()
pygame.camera.init()


class Game:
    def __init__(self):
        self.FPS = 60
        pygame.display.set_caption("Just your typical adventure game")
        self.window = pygame.display.set_mode((1500, 800))
        self.frames = pygame.time.Clock()
        self.timer = pygame.time.Clock()

        self.player = pygame.transform.scale(pygame.image.load("adeventure character.png"), (50, 75))
        self.player_hitbox = pygame.Rect((725, 700), (50, 75))
        self.mouse = pygame.transform.scale(pygame.image.load("mouse.png"), (75, 50))
        self.mouse_hitbox = pygame.Rect(700, 700, 75, 50)
        self.note = pygame.transform.scale(pygame.image.load("note.png"), (25, 25))
        self.eye = pygame.transform.scale(pygame.image.load("eye.png"), (300, 250))
        self.enemy = pygame.transform.scale(pygame.image.load("Bob.jpeg"), (25, 25))

        self.wall_hor_one = pygame.Rect(550, 200, 50, 50)
        self.wall_hor_two = pygame.Rect(900, 200, 50, 50)
        self.wall_hor_three = pygame.Rect(0, 375, 600, 50)
        self.wall_hor_four = pygame.Rect(550, 550, 150, 50)
        self.wall_hor_five = pygame.Rect(800, 550, 150, 50)
        self.wall_hor_six = pygame.Rect(900, 375, 600, 50)
        self.wall_hor_seven = pygame.Rect(900, 600, 500, 10)
        self.wall_hor_eight = pygame.Rect(600, 0, 300, 50)

        self.horizontal_walls = [self.wall_hor_one,
                                 self.wall_hor_two,
                                 self.wall_hor_three,
                                 self.wall_hor_four,
                                 self.wall_hor_five,
                                 self.wall_hor_six,
                                 self.wall_hor_seven,
                                 self.wall_hor_eight]

        self.wall_ver_one = pygame.Rect(550, 550, 50, 250)
        self.wall_ver_two = pygame.Rect(900, 550, 50, 250)
        self.wall_ver_three = pygame.Rect(650, 550, 50, 50)
        self.wall_ver_four = pygame.Rect(800, 550, 50, 50)
        self.wall_ver_five = pygame.Rect(550, 0, 50, 250)
        self.wall_ver_six = pygame.Rect(900, 0, 50, 250)
        self.wall_ver_seven = pygame.Rect(550, 375, 50, 50)
        self.wall_ver_eight = pygame.Rect(900, 375, 50, 50)
        self.wall_ver_nine = pygame.Rect(0, 0, 10, 800)
        self.wall_ver_ten = pygame.Rect(1490, 0, 10, 800)
        self.wall_ver_eleven = pygame.Rect(1390, 600, 10, 10)

        self.vertical_walls = [self.wall_ver_one,
                               self.wall_ver_two,
                               self.wall_ver_three,
                               self.wall_ver_four,
                               self.wall_ver_five,
                               self.wall_ver_six,
                               self.wall_ver_seven,
                               self.wall_ver_eight,
                               self.wall_ver_nine,
                               self.wall_ver_ten,
                               self.wall_ver_eleven]

        self.interact_object = pygame.Rect(600, 700, 25, 25)
        self.message_line_one = "Let this shrine be known as the Temple of SDREN (pronounced SDREN). "
        self.message_line_two = "Lay here are the secrets that many desire, The Treasure of No Man. "
        self.message_line_three = "This treasure is      ly use     and gives the finder   s     ly   thing. But they first "
        self.message_line_four = "must complete the trial of the SDREN. Only the worthy are blessed."
        self.message = [self.message_line_one,
                        self.message_line_two,
                        self.message_line_three,
                        self.message_line_four]

        self.interact_object_one = pygame.Rect(10, 600, 25, 25)
        # Credit to Monty Python
        self.message_one_line_one = "Who approaches the Temple of SDREN must answer me these questions three,"
        self.message_one_line_two = "ere the treasure he see  (press Enter to submit answers)"
        self.message_one_line_three = "WHAT, is your name?"
        self.message_one_line_four = "WHAT, is your quest?"
        self.message_one_line_five = "WHAT, is the air-speed velocity of an unladen swallow?"

        self.message_one = [self.message_one_line_one,
                            self.message_one_line_two,
                            self.message_one_line_three,
                            self.message_one_line_four,
                            self.message_one_line_five]

        self.interact_object_two = pygame.Rect(950, 700, 25, 25)

        self.message_two_line_one = "There was once a very brave member of the SDREN named Tommy T. He had"
        self.message_two_line_two = "been searching endlessly for a number, a number to call Jenny, the girl"
        self.message_two_line_three = "for him. Then, once he had found the number, he exclaimed"
        self.message_two_line_four = " \'I got it (I got it) I got it\'. Write the number on the wall to call Jenny."

        self.message_two = [self.message_two_line_one,
                            self.message_two_line_two,
                            self.message_two_line_three,
                            self.message_two_line_four]

        self.interact_object_three = pygame.Rect(1465, 175, 25, 25)

        self.message_three_line_one = "There is an ancient legend of the SDREN called \'The Legend of Alzed\'. The"
        self.message_three_line_two = "legend consisted of a symbol, that was created by the gods. The SDREN would"
        self.message_three_line_three = "use these pressure plates to represent the symbol."

        self.message_three = [self.message_three_line_one,
                              self.message_three_line_two,
                              self.message_three_line_three]

        self.interact_object_four = pygame.Rect(875, 650, 25, 25)

        self.message_four_line_one = "The Controls (Up: W, Left: A, Down: S, Right: D), but you already knew that."
        self.message_four_line_two = "(Interact: E), That's all the controls, but there's one more bit of info"
        self.message_four_line_three = "that you will need. Use the key at the center of the eye."

        self.message_four = [self.message_four_line_one,
                             self.message_four_line_two,
                             self.message_four_line_three]

        self.top_text_border = pygame.Rect(250, 50, 1000, 400)
        self.top_text_box = pygame.Rect(275, 75, 950, 350)

        self.text_border = pygame.Rect(250, 350, 1000, 400)
        self.text_box = pygame.Rect(275, 375, 950, 350)

        self.pressure_plate_one = [pygame.Rect(1000, 100, 25, 25), False]
        self.pressure_plate_two = [pygame.Rect(1050, 100, 25, 25), False]
        self.pressure_plate_three = [pygame.Rect(1100, 100, 25, 25), False]
        self.pressure_plate_four = [pygame.Rect(1150, 100, 25, 25), False]
        self.pressure_plate_five = [pygame.Rect(1200, 100, 25, 25), False]
        self.pressure_plate_six = [pygame.Rect(1250, 100, 25, 25), False]
        self.pressure_plate_seven = [pygame.Rect(1300, 100, 25, 25), False]
        self.pressure_plate_eight = [pygame.Rect(1000, 150, 25, 25), False]
        self.pressure_plate_nine = [pygame.Rect(1050, 150, 25, 25), False]
        self.pressure_plate_ten = [pygame.Rect(1100, 150, 25, 25), False]
        self.pressure_plate_eleven = [pygame.Rect(1150, 150, 25, 25), False]
        self.pressure_plate_twelve = [pygame.Rect(1200, 150, 25, 25), False]
        self.pressure_plate_thirteen = [pygame.Rect(1250, 150, 25, 25), False]
        self.pressure_plate_fourteen = [pygame.Rect(1300, 150, 25, 25), False]
        self.pressure_plate_fifteen = [pygame.Rect(1000, 200, 25, 25), False]
        self.pressure_plate_sixteen = [pygame.Rect(1050, 200, 25, 25), False]
        self.pressure_plate_seventeen = [pygame.Rect(1100, 200, 25, 25), False]
        self.pressure_plate_eighteen = [pygame.Rect(1150, 200, 25, 25), False]
        self.pressure_plate_nineteen = [pygame.Rect(1200, 200, 25, 25), False]
        self.pressure_plate_twenty = [pygame.Rect(1250, 200, 25, 25), False]
        self.pressure_plate_twentyone = [pygame.Rect(1300, 200, 25, 25), False]
        self.pressure_plate_twentytwo = [pygame.Rect(1000, 250, 25, 25), False]
        self.pressure_plate_twentythree = [pygame.Rect(1050, 250, 25, 25), False]
        self.pressure_plate_twentyfour = [pygame.Rect(1100, 250, 25, 25), False]
        self.pressure_plate_twentyfive = [pygame.Rect(1150, 250, 25, 25), False]
        self.pressure_plate_twentysix = [pygame.Rect(1200, 250, 25, 25), False]
        self.pressure_plate_twentyseven = [pygame.Rect(1250, 250, 25, 25), False]
        self.pressure_plate_twentyeight = [pygame.Rect(1300, 250, 25, 25), False]

        self.pressure_plate_puzzle = [self.pressure_plate_one,
                                      self.pressure_plate_two,
                                      self.pressure_plate_three,
                                      self.pressure_plate_four,
                                      self.pressure_plate_five,
                                      self.pressure_plate_six,
                                      self.pressure_plate_seven,
                                      self.pressure_plate_eight,
                                      self.pressure_plate_nine,
                                      self.pressure_plate_ten,
                                      self.pressure_plate_eleven,
                                      self.pressure_plate_twelve,
                                      self.pressure_plate_thirteen,
                                      self.pressure_plate_fourteen,
                                      self.pressure_plate_fifteen,
                                      self.pressure_plate_sixteen,
                                      self.pressure_plate_seventeen,
                                      self.pressure_plate_eighteen,
                                      self.pressure_plate_nineteen,
                                      self.pressure_plate_twenty,
                                      self.pressure_plate_twentyone,
                                      self.pressure_plate_twentytwo,
                                      self.pressure_plate_twentythree,
                                      self.pressure_plate_twentyfour,
                                      self.pressure_plate_twentyfive,
                                      self.pressure_plate_twentysix,
                                      self.pressure_plate_twentyseven,
                                      self.pressure_plate_twentyeight]

        self.laser_one = pygame.Rect(900, 425, 25, 20)
        self.laser_two = pygame.Rect(900, 530, 25, 20)
        self.laser_three = pygame.Rect(1100, 425, 25, 50)
        self.laser_four = pygame.Rect(1150, 425, 25, 25)
        self.laser_five = pygame.Rect(1010, 510, 25, 90)
        self.laser_six = pygame.Rect(1250, 425, 70, 70)
        self.laser_seven = pygame.Rect(1420, 529, 70, 70)
        self.laser_eight = pygame.Rect(1300, 650, 50, 50)
        self.laser_nine = pygame.Rect(1150, 650, 50, 50)

        self.lasers = [self.laser_one,
                       self.laser_two,
                       self.laser_three,
                       self.laser_four,
                       self.laser_five,
                       self.laser_six,
                       self.laser_seven,
                       self.laser_eight,
                       self.laser_nine]

        self.toggle_timer = False

        self.math_start = pygame.Rect(500, 300, 25, 25)

        self.math_one_line_one = "The SDREN are very fond of mathematics. Prove yourself to the SDREN by "
        self.math_one_line_two = "completing a series of math questions. You have 500 seconds. Good Luck!"
        self.math_one_line_three = "(Press Enter to submit answers)"
        self.math_one_line_four = "What is 1 + 1?"

        self.math_message_one = [self.math_one_line_one,
                                 self.math_one_line_two,
                                 self.math_one_line_three,
                                 self.math_one_line_four]

        self.math_second = pygame.Rect(250, 325, 25, 25)

        self.math_two_line_one = "Factor the function x^2 + 4x - 12 = 0"
        self.math_two_line_two = " x =         x = "

        self.math_third = pygame.Rect(300, 100, 25, 25)

        self.math_three_line_one = "It's Pythagoras Time!! Find the Hypotenuse of this right triangle."
        self.math_three_line_two = "One of the sides has a length of 15 and the other has a length of 36"
        self.math_three_line_three = "Hypotenuse = "

        self.math_message_three = [self.math_three_line_one,
                                   self.math_three_line_two]

        self.math_fourth = pygame.Rect(50, 350, 25, 25)

        self.math_four_line_one = "Barry B. Benson is moving at a velocity represented by the equation"
        self.math_four_line_two = "v(t) = 3t^3 - 4t^2 + 12t + 90. How fast is Barry B. Benson"
        self.math_four_line_three = "accelerating at time t = 2"
        self.math_four_line_four = "The acceleration at t = 2 is "

        self.math_message_four = [self.math_four_line_one,
                                  self.math_four_line_two,
                                  self.math_four_line_three]

        self.math_fifth = pygame.Rect(100, 150, 25, 25)

        self.math_five_line_one = "Now for the toughest question. Find the integral from 0 to pi for the"
        self.math_five_line_two = "equation f(x) = 3(sec(4x))^2 + 6cos(x) in terms of x"
        self.math_five_line_three = "The integral of f(x) is "

        self.math_message_five = [self.math_five_line_one,
                                  self.math_five_line_two]

        self.arena = pygame.Rect(0, 425, 550, 375)
        self.enemy_tracker = pygame.Rect(100, 500, 25, 25)
        self.other_enemy_tracker = pygame.Rect(250, 700, 25, 25)

        self.final_interact_object = pygame.Rect(738, 288, 25, 25)

        self.final_line_one = "Use the mouse as the key."

        self.mouse_message_one = "** Squeak **"""
        self.mouse_message_two = "** Squeak Squeak **"
        self.mouse_message_three = "Hi adventurer, do you need help?"
        self.mouse_message_four = "That's too bad. I wish I could help, but I'm just a mouse."
        self.mouse_message_five = "** Squeak **"
        self.mouse_message_six = "I really can't help you."
        self.mouse_message_seven = "You can keep trying, but nothing is going to change."

        self.normal_end_line_one = "You have beaten all of the"
        self.normal_end_line_two = "challenges of the SDREN. But,"
        self.normal_end_line_three = "there is an even deeper secret"
        self.normal_end_line_four = "of the SDREN. The SDREN are"
        self.normal_end_line_five = "actually..."

        self.normal_end_first = [self.normal_end_line_one,
                                 self.normal_end_line_two,
                                 self.normal_end_line_three,
                                 self.normal_end_line_four,
                                 self.normal_end_line_five]

        self.normal_end_line_four = "That\'s right. You are a huge NERD."
        self.normal_end_line_five = "As for the treasure, the real"
        self.normal_end_line_six = "treasure is the friends we made"
        self.normal_end_line_seven = "along the way."

        self.normal_end_second = [self.normal_end_line_four,
                                  self.normal_end_line_five,
                                  self.normal_end_line_six,
                                  self.normal_end_line_seven]

        self.lazy_end_line_one = "You really had to go back and"
        self.lazy_end_line_two = "skip to the end. You didn't learn"
        self.lazy_end_line_three = "anything and you've wasted"
        self.lazy_end_line_four = "everybody\'s time. I need to know"
        self.lazy_end_line_six = "why there are people like you out"
        self.lazy_end_line_seven = "there. You know what? Maybe I\'m"
        self.lazy_end_line_eight = "wrong. Maybe you accidentally"
        self.lazy_end_line_nine = "clicked the eye and I\'m"
        self.lazy_end_line_ten = "overreacting. But there's no way"
        self.lazy_end_line_eleven = "that happened. You just wanted"
        self.lazy_end_line_twelve = "to see what would happen if you"
        self.lazy_end_line_thirteen = "tried something, you completionist."
        self.lazy_end_line_fourteen = "I hope your happy."

        self.lazy_ending = [self.lazy_end_line_one,
                            self.lazy_end_line_two,
                            self.lazy_end_line_three,
                            self.lazy_end_line_four,
                            self.lazy_end_line_six,
                            self.lazy_end_line_seven,
                            self.lazy_end_line_eight,
                            self.lazy_end_line_nine,
                            self.lazy_end_line_ten,
                            self.lazy_end_line_eleven,
                            self.lazy_end_line_twelve,
                            self.lazy_end_line_thirteen,
                            self.lazy_end_line_fourteen]

        self.confused_end_line_one = "I don't even know how you could"
        self.confused_end_line_two = "get this ending I mean, you"
        self.confused_end_line_three = "completed at least one puzzle,"
        self.confused_end_line_four = "and then clicked the eye."
        self.confused_end_line_five = "Why? Just Why?"

        self.confused_ending = [self.confused_end_line_one,
                                self.confused_end_line_two,
                                self.confused_end_line_three,
                                self.confused_end_line_four,
                                self.confused_end_line_five]

        self.cam_rectangle = pygame.Rect(1150, 300, 320, 100)
        self.end_white = pygame.Rect(400, 50, 700, 700)
        self.death_message_background = pygame.Rect(50, 300, 320, 250)

    def run_game(self):
        game_complete = False
        all_complete = False
        deaths = 0
        math_ticker = 0
        math_timer = 500

        typed_font = pygame.font.Font(None, 36)

        text = ""

        text_one = ""
        text_two = ""
        text_three = ""
        answered_one = [False, False]

        completed_puzzles = [False, False, False, False]

        math_correct = [False, False, False, False, False]
        math_question_one_answered = False
        math_question_two_answered = [False, False]
        math_question_three_answered = False
        math_question_four_answered = False
        math_question_five_answered = False
        math_one = ""
        math_two_part_one = ""
        math_two_part_two = ""
        math_three = ""
        math_four = ""
        math_five = ""

        line_one = pygame.transform.scale(pygame.image.load("yellow.webp"), (290, 5)).convert_alpha()
        line_one_blit = pygame.transform.rotate(line_one, -45)
        line_two = pygame.transform.scale(pygame.image.load("yellow.webp"), (290, 5)).convert_alpha()
        line_two_blit = pygame.transform.rotate(line_two, 45)
        line_three_blit = pygame.transform.scale(pygame.image.load("yellow.webp"), (410, 5)).convert_alpha()
        line_four = pygame.transform.scale(pygame.image.load("yellow.webp"), (145, 5)).convert_alpha()
        line_four_blit = pygame.transform.rotate(line_four, -45)
        line_five_blit = pygame.transform.scale(pygame.image.load("yellow.webp"), (205, 5)).convert_alpha()
        line_six = pygame.transform.scale(pygame.image.load("yellow.webp"), (145, 5)).convert_alpha()
        line_six_blit = pygame.transform.rotate(line_six, 45)

        slow_laser_velocity = 1
        fast_laser_velocity = 3
        slow_box_laser_velocity_x = 2
        slow_box_laser_velocity_y = 2
        other_slow_box_laser_velocity_x = 2
        other_slow_box_laser_velocity_y = 2
        circle_laser = 3
        other_circle_laser = 3

        tracking = True

        mouse_pressed = False

        times_talked = 0

        while (not game_complete):

            typed_text = typed_font.render(text, True, (10, 10, 10))

            typed_text_one = typed_font.render(text_one, True, (10, 10, 10))
            typed_text_two = typed_font.render(text_two, True, (10, 10, 10))
            typed_text_three = typed_font.render(text_three, True, (10, 10, 10))

            math_typed_text_one = typed_font.render(math_one, True, (10, 10, 10))

            math_typed_text_two_one = typed_font.render(math_two_part_one, True, (10, 10, 10))
            math_typed_text_two_two = typed_font.render(math_two_part_two, True, (10, 10, 10))

            math_typed_text_three = typed_font.render(math_three, True, (10, 10, 10))

            math_typed_text_four = typed_font.render(math_four, True, (10, 10, 10))

            math_typed_text_five = typed_font.render(math_five, True, (10, 10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif (event.type == pygame.KEYDOWN):
                    if (self.player_hitbox.colliderect(self.interact_object_two) and not completed_puzzles[0]):
                        if (event.key == pygame.K_BACKSPACE):
                            if (len(text) > 0):
                                text = text[:-1]
                        elif (len(text) < 7):
                            text += event.unicode
                        typed_text = typed_font.render(text, True, (10, 10, 10))
                        if (text == "8675309"):
                            completed_puzzles[0] = True
                    if (self.player_hitbox.colliderect(self.interact_object_one) and not completed_puzzles[1]):
                        if (not answered_one[0]):
                            if (event.key == pygame.K_RETURN):
                                answered_one[0] = True
                            elif (event.key == pygame.K_BACKSPACE):
                                if (len(text_one) > 0):
                                    text_one = text_one[:-1]
                            else:
                                text_one += event.unicode

                        elif (answered_one[0] and not answered_one[1]):
                            if (event.key == pygame.K_RETURN):
                                answered_one[1] = True
                            elif (event.key == pygame.K_BACKSPACE):
                                if (len(text_two) > 0):
                                    text_two = text_two[:-1]
                            else:
                                text_two += event.unicode

                        elif (answered_one[0] and answered_one[1]):
                            if (event.key == pygame.K_RETURN):
                                """Maybe give movement back to the player?"""
                            elif (event.key == pygame.K_BACKSPACE):
                                if (len(text_one) > 0):
                                    text_three = text_three[:-1]
                            else:
                                text_three += event.unicode
                        typed_text_one = typed_font.render(text_one, True, (10, 10, 10))
                        typed_text_two = typed_font.render(text_two, True, (10, 10, 10))
                        typed_text_three = typed_font.render(text_three, True, (10, 10, 10))
                        if (text_three.lower() == "what do you mean? an african or european swallow?"):
                            completed_puzzles[1] = True
                    if (event.key == pygame.K_e and not completed_puzzles[2]):
                        for pressure_plate in self.pressure_plate_puzzle:
                            if (self.player_hitbox.colliderect(pressure_plate[0]) and pressure_plate[1]):
                                pressure_plate[1] = False
                            elif (self.player_hitbox.colliderect(pressure_plate[0])):
                                pressure_plate[1] = True
                        if (self.pressure_plate_four[1] and self.pressure_plate_ten[1] and self.pressure_plate_eleven[1] and
                            self.pressure_plate_twelve[1] and self.pressure_plate_sixteen[1] and self.pressure_plate_twenty[1] and
                            self.pressure_plate_twentytwo[1] and self.pressure_plate_twentythree[1] and self.pressure_plate_twentyfour[1] and
                            self.pressure_plate_twentysix[1] and self.pressure_plate_twentyseven[1] and self.pressure_plate_twentyeight[1]
                            and (not self.pressure_plate_one[1]) and (not self.pressure_plate_two[1]) and (not self.pressure_plate_three[1])
                            and (not self.pressure_plate_five[1]) and (not self.pressure_plate_six[1]) and (not self.pressure_plate_seven[1])
                            and (not self.pressure_plate_eight[1]) and (not self.pressure_plate_nine[1]) and (not self.pressure_plate_thirteen[1])
                            and (not self.pressure_plate_fourteen[1]) and (not self.pressure_plate_fifteen[1]) and (not self.pressure_plate_seventeen[1])
                            and (not self.pressure_plate_eighteen[1]) and (not self.pressure_plate_nineteen[1]) and (not self.pressure_plate_twentyone[1])
                                and (not self.pressure_plate_twentyfive[1])):
                            completed_puzzles[2] = True
                            # Credit to Nintendo and Zelda
                            pygame.mixer.music.load("Recording-_3_.ogg", "ogg")
                            pygame.mixer.music.play()

                    if (not completed_puzzles[3]):
                        if (self.player_hitbox.colliderect(self.math_start) and not math_correct[0]):
                            if (event.key == pygame.K_BACKSPACE):
                                if (len(math_one) > 0):
                                    math_one = math_one[:-1]
                            elif (event.key == pygame.K_RETURN):
                                math_question_one_answered = True
                            elif (len(math_one) <= 1):
                                math_one += event.unicode
                            if (math_question_one_answered):
                                if (math_one == "2"):
                                    math_correct[0] = True
                                else:
                                    math_question_one_answered = False
                        elif (self.player_hitbox.colliderect(self.math_second) and not math_correct[1]):
                            if(not math_question_two_answered[0]):
                                if (event.key == pygame.K_BACKSPACE):
                                    if (len(math_two_part_one) > 0):
                                        math_two_part_one = math_two_part_one[:-1]
                                elif (event.key == pygame.K_RETURN):
                                    math_question_two_answered[0] = True
                                elif (len(math_two_part_one) <= 1):
                                    math_two_part_one += event.unicode
                            elif (not math_question_two_answered[1]):
                                if (event.key == pygame.K_BACKSPACE):
                                    if (len(math_two_part_two) > 0):
                                        math_two_part_two = math_two_part_two[:-1]
                                    elif (len(math_two_part_two) == 0):
                                        math_question_two_answered[0] = False
                                elif (event.key == pygame.K_RETURN):
                                    math_question_two_answered[1] = True
                                elif (len(math_two_part_two) <= 1):
                                    math_two_part_two += event.unicode

                            if (math_question_two_answered[0] and math_question_two_answered[1]):
                                if ((math_two_part_one == "-6" and math_two_part_two == "2") or
                                        (math_two_part_one == "2" and math_two_part_two == "-6")):
                                    math_correct[1] = True
                                else:
                                    math_question_two_answered[0] = False
                                    math_question_two_answered[1] = False
                        elif (self.player_hitbox.colliderect(self.math_third) and not math_correct[2]):
                            if (event.key == pygame.K_BACKSPACE):
                                if (len(math_three) > 0):
                                    math_three = math_three[:-1]
                            elif (event.key == pygame.K_RETURN):
                                math_question_three_answered = True
                            elif (len(math_three) <= 1):
                                math_three += event.unicode
                            if (math_question_three_answered):
                                if (math_three == "39"):
                                    math_correct[2] = True
                                else:
                                    math_question_three_answered = False

                        elif (self.player_hitbox.colliderect(self.math_fourth) and not math_correct[3]):
                            if (event.key == pygame.K_BACKSPACE):
                                if (len(math_four) > 0):
                                    math_four = math_four[:-1]
                            elif (event.key == pygame.K_RETURN):
                                math_question_four_answered = True
                            elif (len(math_four) <= 1):
                                math_four += event.unicode
                            if (math_question_four_answered):
                                if (math_four == "32"):
                                    math_correct[3] = True
                                else:
                                    math_question_four_answered = False

                        elif (self.player_hitbox.colliderect(self.math_fifth) and not math_correct[4]):
                            if (event.key == pygame.K_BACKSPACE):
                                if (len(math_five) > 0):
                                    math_five = math_five[:-1]
                            elif (event.key == pygame.K_RETURN):
                                math_question_five_answered = True
                            elif (len(math_five) <= 1):
                                math_five += event.unicode
                            if (math_question_five_answered):
                                if (math_five == "0"):
                                    math_correct[4] = True
                                else:
                                    math_question_five_answered = False

                        math_typed_text_one = typed_font.render(math_one, True, (10, 10, 10))
                        math_typed_text_two_one = typed_font.render(math_two_part_one, True, (10, 10, 10))
                        math_typed_text_two_two = typed_font.render(math_two_part_two, True, (10, 10, 10))
                        math_typed_text_three = typed_font.render(math_three, True, (10, 10, 10))
                        math_typed_text_four = typed_font.render(math_four, True, (10, 10, 10))
                        math_typed_text_five = typed_font.render(math_five, True, (10, 10, 10))

                        if (math_correct[0] and math_correct[1] and math_correct[2] and math_correct[3] and math_correct[4]):
                            completed_puzzles[3] = True
                    if (event.key == pygame.K_e and all_complete and self.player_hitbox.colliderect(self.mouse_hitbox)):
                            times_talked += 1

                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    mouse_pressed = True
                elif (event.type != pygame.MOUSEBUTTONDOWN):
                    mouse_pressed = False


            # Draw all objects on the screen
            self.window.fill((170, 24, 199))
            for wall in self.horizontal_walls:
                pygame.draw.rect(self.window, (127, 127, 127), wall)
            for wall in self.vertical_walls:
                pygame.draw.rect(self.window, (127, 127, 127), wall)
            self.window.blit(self.note, (self.interact_object.x, self.interact_object.y))
            self.window.blit(self.note, (self.interact_object_one.x, self.interact_object_one.y))
            self.window.blit(self.note, (self.interact_object_two.x, self.interact_object_two.y))
            self.window.blit(self.note, (self.interact_object_three.x, self.interact_object_three.y))
            self.window.blit(self.note, (self.interact_object_four.x, self.interact_object_four.y))

            # Get Inputs
            inputs = pygame.key.get_pressed()

            # Player Velocity
            left_velocity = 4
            right_velocity = 4
            up_velocity = 4
            down_velocity = 4

            # Give walls a hit-box
            for wall in self.horizontal_walls:
                for interval in range(0, wall.width + 1, 50):
                    if self.player_hitbox.colliderect(wall):
                        if self.player_hitbox.collidepoint(wall.x + interval, wall.y):
                            down_velocity = 0
                        elif self.player_hitbox.collidepoint(wall.x + interval, wall.y + 50):
                            up_velocity = 0

            for wall in self.vertical_walls:
                for interval in range(0, wall.height + 1, 50):
                    if self.player_hitbox.colliderect(wall):
                        if self.player_hitbox.collidepoint(wall.x, wall.y + interval):
                            right_velocity = 0
                        elif self.player_hitbox.collidepoint(wall.x + 50, wall.y + interval):
                            left_velocity = 0

            # Draws the color of the pressure plates
            for pressure_plate in self.pressure_plate_puzzle:
                if pressure_plate[1]:
                    pygame.draw.rect(self.window, (0, 255, 0), pressure_plate[0])
                else:
                    pygame.draw.rect(self.window, (255, 0, 0), pressure_plate[0])

            # If the pressure plate puzzle is solved, draw a tri-force
            if (completed_puzzles[2]):
                self.window.blit(line_one_blit, (1162, 85))
                self.window.blit(line_two_blit, (959, 85))
                self.window.blit(line_three_blit, (959, 290))
                self.window.blit(line_four_blit, (1062, 187))
                self.window.blit(line_five_blit, (1062, 187))
                self.window.blit(line_six_blit, (1162, 187))

            # Moves and displays the lasers
            if (self.laser_three.y == 425):
                slow_laser_velocity = 1
            elif (self.laser_three.y == 550):
                slow_laser_velocity = -1

            self.laser_three.y += slow_laser_velocity

            if (self.laser_four.y == 425):
                fast_laser_velocity = 3
            elif (self.laser_four.y == 575):
                fast_laser_velocity = -3

            self.laser_four.y += fast_laser_velocity

            if (self.laser_six.y == 425 and self.laser_six.x == 1250):
                slow_box_laser_velocity_x = 0
                slow_box_laser_velocity_y = 2
            elif (self.laser_six.y == 529 and self.laser_six.x == 1250):
                slow_box_laser_velocity_y = 0
                slow_box_laser_velocity_x = 2
            elif (self.laser_six.y == 529 and self.laser_six.x == 1420):
                slow_box_laser_velocity_x = 0
                slow_box_laser_velocity_y = -2
            elif (self.laser_six.y == 425 and self.laser_six.x == 1420):
                slow_box_laser_velocity_y = 0
                slow_box_laser_velocity_x = -2

            self.laser_six.y += slow_box_laser_velocity_y
            self.laser_six.x += slow_box_laser_velocity_x

            if (self.laser_seven.y == 425 and self.laser_seven.x == 1250):
                other_slow_box_laser_velocity_x = 0
                other_slow_box_laser_velocity_y = 2
            elif (self.laser_seven.y == 529 and self.laser_seven.x == 1250):
                other_slow_box_laser_velocity_y = 0
                other_slow_box_laser_velocity_x = 2
            elif (self.laser_seven.y == 529 and self.laser_seven.x == 1420):
                other_slow_box_laser_velocity_x = 0
                other_slow_box_laser_velocity_y = -2
            elif (self.laser_seven.y == 425 and self.laser_seven.x == 1420):
                other_slow_box_laser_velocity_y = 0
                other_slow_box_laser_velocity_x = -2

            self.laser_seven.y += other_slow_box_laser_velocity_y
            self.laser_seven.x += other_slow_box_laser_velocity_x

            self.laser_eight.x += 5 * math.cos(math.radians(circle_laser))
            self.laser_eight.y += 5 * math.sin(math.radians(circle_laser))

            circle_laser += 5

            self.laser_nine.x += 5 * math.cos(math.radians(other_circle_laser))
            self.laser_nine.y += 5 * math.sin(math.radians(other_circle_laser))

            other_circle_laser += 5

            for laser in self.lasers:
                if self.player_hitbox.colliderect(laser):
                    deaths += 1
                    self.player_hitbox.x = 725
                    self.player_hitbox.y = 700
                pygame.draw.rect(self.window, (255, 0, 0), laser)

            if (self.player_hitbox.colliderect(self.math_start) and not self.toggle_timer and not completed_puzzles[3]):
                self.toggle_timer = True

            if (self.toggle_timer and not completed_puzzles[3]):
                math_ticker += self.timer.tick()

                if (math_ticker > 1000):
                    math_timer -= 1
                    math_ticker = 0

                if (math_timer == 0):
                    math_timer = 500
                    deaths += 1
                    self.player_hitbox.x = 725
                    self.player_hitbox.y = 700
                    self.toggle_timer = False

                timer_text = typed_font.render(str(math_timer), True, (10, 10, 10))
                pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(10, 0, 75, 50))
                self.window.blit(timer_text, (20, 10))
            self.window.blit(self.note, (self.math_start.x, self.math_start.y))
            self.window.blit(self.note, (self.math_second.x, self.math_second.y))
            self.window.blit(self.note, (self.math_third.x, self.math_third.y))
            self.window.blit(self.note, (self.math_fourth.x, self.math_fourth.y))
            self.window.blit(self.note, (self.math_fifth.x, self.math_fifth.y))

            # Tracking puzzle
            if (self.player_hitbox.colliderect(self.arena) and tracking):
                if (self.enemy_tracker.centerx > self.player_hitbox.centerx):
                    self.enemy_tracker.centerx -= 2
                else:
                    self.enemy_tracker.centerx += 2
                if (self.enemy_tracker.centery > self.player_hitbox.centery):
                    self.enemy_tracker.centery -= 2
                else:
                    self.enemy_tracker.centery += 2
                if (self.other_enemy_tracker.centerx > self.player_hitbox.centerx):
                    self.other_enemy_tracker.centerx -= 2
                else:
                    self.other_enemy_tracker.centerx += 2
                if (self.other_enemy_tracker.centery > self.player_hitbox.centery):
                    self.other_enemy_tracker.centery -= 2
                else:
                    self.other_enemy_tracker.centery += 2
                if (self.player_hitbox.colliderect(self.enemy_tracker) or self.player_hitbox.colliderect(self.other_enemy_tracker)):
                    self.player_hitbox.x = 725
                    self.player_hitbox.y = 700
                    self.enemy_tracker.x = 100
                    self.enemy_tracker.y = 500
                    self.other_enemy_tracker.x = 250
                    self.other_enemy_tracker.y = 700
                    deaths += 1
                if (self.player_hitbox.colliderect(self.interact_object_one)):
                    tracking = False

            self.window.blit(self.enemy, (self.enemy_tracker.x, self.enemy_tracker.y))
            self.window.blit(self.enemy, (self.other_enemy_tracker.x, self.other_enemy_tracker.y))

            if (completed_puzzles[0] and completed_puzzles[1] and completed_puzzles[2] and completed_puzzles[3]):
                self.window.blit(self.note, (self.final_interact_object.x, self.final_interact_object.y))
                self.window.blit(self.mouse, (700, 700))
                all_complete = True

            self.window.blit(self.eye, (600, 25))

            # Interacting with objects
            if (self.player_hitbox.colliderect(self.interact_object)):
                pygame.draw.rect(self.window, (0, 0, 0), self.top_text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.top_text_box)
                text_placement = 100
                for line in self.message:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25

            if (self.player_hitbox.colliderect(self.interact_object_one)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_placement = 400
                for line in self.message_one:
                    text_b = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_b, (300, text_placement))
                    text_placement += 50
                self.window.blit(typed_text_one, (700, 500))
                self.window.blit(typed_text_two, (700, 550))
                self.window.blit(typed_text_three, (300, 660))

            if (self.player_hitbox.colliderect(self.interact_object_two)):
                pygame.draw.rect(self.window, (0, 0, 0), self.top_text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.top_text_box)
                text_placement = 100
                for line in self.message_two:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25
                self.window.blit(typed_text, (700, 300))

            if (self.player_hitbox.colliderect(self.interact_object_three)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_placement = 400
                for line in self.message_three:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25

            if (self.player_hitbox.colliderect(self.math_start)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_placement = 400
                for line in self.math_message_one:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25
                self.window.blit(math_typed_text_one, (400, 550))

            if (self.player_hitbox.colliderect(self.math_second)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_a = typed_font.render(self.math_two_line_one, True, (10, 10, 10))
                text_b = typed_font.render(self.math_two_line_two, True, (10, 10, 10))
                self.window.blit(text_a, (300, 400))
                self.window.blit(text_b, (350, 500))
                self.window.blit(math_typed_text_two_one, (400, 500))
                self.window.blit(math_typed_text_two_two, (500, 500))

            if (self.player_hitbox.colliderect(self.math_third)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_placement = 400
                for line in self.math_message_three:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25
                text_b = typed_font.render(self.math_three_line_three, True, (10, 10, 10))
                self.window.blit(text_b, (350, 500))
                self.window.blit(math_typed_text_three, (525, 500))

            if (self.player_hitbox.colliderect(self.math_fourth)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_placement = 400
                for line in self.math_message_four:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25
                text_b = typed_font.render(self.math_four_line_four, True, (10, 10, 10))
                self.window.blit(text_b, (400, 500))
                self.window.blit(math_typed_text_four, (750, 500))

            if (self.player_hitbox.colliderect(self.math_fifth)):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_placement = 400
                for line in self.math_message_five:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25
                text_b = typed_font.render(self.math_five_line_three, True, (10, 10, 10))
                self.window.blit(text_b, (400, 500))
                self.window.blit(math_typed_text_five, (700, 500))

            if (self.player_hitbox.colliderect(self.final_interact_object) and all_complete):
                pygame.draw.rect(self.window, (0, 0, 0), self.text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.text_box)
                text_a = typed_font.render(self.final_line_one, True, (10, 10, 10))
                self.window.blit(text_a, (300, 400))

            if (self.player_hitbox.colliderect(self.mouse_hitbox) and all_complete):
                pygame.draw.rect(self.window, (0, 0, 0), self.top_text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.top_text_box)
                if (times_talked == 0):
                    mouse_one = typed_font.render(self.mouse_message_one, True, (10, 10, 10))
                    self.window.blit(mouse_one, (300, 100))
                elif (times_talked == 1):
                    mouse_two = typed_font.render(self.mouse_message_two, True, (10, 10, 10))
                    self.window.blit(mouse_two, (300, 100))
                elif (times_talked == 2):
                    mouse_three = typed_font.render(self.mouse_message_three, True, (10, 10, 10))
                    self.window.blit(mouse_three, (300, 100))
                elif (times_talked == 3):
                    mouse_four = typed_font.render(self.mouse_message_four, True, (10, 10, 10))
                    self.window.blit(mouse_four, (300, 100))
                elif (times_talked == 4):
                    mouse_five = typed_font.render(self.mouse_message_five, True, (10, 10, 10))
                    self.window.blit(mouse_five, (300, 100))
                elif (times_talked == 5):
                    mouse_six = typed_font.render(self.mouse_message_six, True, (10, 10, 10))
                    self.window.blit(mouse_six, (300, 100))
                elif (times_talked >= 6):
                    mouse_seven = typed_font.render(self.mouse_message_seven, True, (10, 10, 10))
                    self.window.blit(mouse_seven, (300, 100))

            if (self.player_hitbox.colliderect(self.interact_object_four)):
                pygame.draw.rect(self.window, (0, 0, 0), self.top_text_border)
                pygame.draw.rect(self.window, (255, 255, 255), self.top_text_box)
                text_placement = 100
                for line in self.message_four:
                    text_a = typed_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_a, (300, text_placement))
                    text_placement += 25

            # Draws and moves the player
            if (not inputs[pygame.K_a] and not inputs[pygame.K_d]) or (inputs[pygame.K_a] and inputs[pygame.K_d]):
                self.window.blit(self.player, (self.player_hitbox.x, self.player_hitbox.y))
                pygame.draw.rect(self.window, (255, 255, 255), self.player_hitbox, 2, 5)

            if (inputs[pygame.K_a] and self.player_hitbox.x > 0 and not inputs[pygame.K_d]):
                self.player_hitbox.x -= left_velocity
                self.window.blit(self.player, (self.player_hitbox.x, self.player_hitbox.y))
                pygame.draw.rect(self.window, (255, 255, 255), self.player_hitbox, 2, 5)

            if (inputs[pygame.K_d] and self.player_hitbox.x < 1500 - 50 and not inputs[pygame.K_a]):
                self.player_hitbox.x += right_velocity
                flipped_player = self.player.copy()
                self.window.blit(pygame.transform.flip(flipped_player, True, False), (self.player_hitbox.x, self.player_hitbox.y))
                pygame.draw.rect(self.window, (255, 255, 255), self.player_hitbox, 2, 5)

            if (inputs[pygame.K_w] and self.player_hitbox.y > 0):
                self.player_hitbox.y -= up_velocity

            if (inputs[pygame.K_s] and self.player_hitbox.y < 800 - 50):
                self.player_hitbox.y += down_velocity

            if (mouse_pressed):
                if (pygame.mouse.get_pos()[0] > 700 and pygame.mouse.get_pos()[0] < 800):
                    if (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 200):
                        game_complete = True

            pygame.display.update()
            self.frames.tick(self.FPS)

        N_x = 900
        E_x = 800
        D_x = 600
        S_x = 500

        large_font = pygame.font.Font(None, 54)
        nerd_font = pygame.font.Font(None, 72)

        end_timer = pygame.time.Clock()
        end_ticker = 0

        camera_list = pygame.camera.list_cameras()
        cam = pygame.camera.Camera(camera_list[0], (300, 300), "rgb")

        cam_not_started = True

        dramatic_sound_played = False

        while True:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if (not cam_not_started):
                        cam.stop()
                    pygame.quit()
                    sys.exit()

            pygame.draw.rect(self.window, (255, 255, 255), self.end_white)

            if (all_complete):
                end_text_placement = 100
                for line in self.normal_end_first:
                    text_b = large_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_b, (450, end_text_placement))
                    end_text_placement += 50

                text_S = nerd_font.render("S", True, (10, 10, 10))
                self.window.blit(text_S, (S_x, 400))
                if (S_x < 900):
                    S_x += 5
                text_D = nerd_font.render("D", True, (10, 10, 10))
                self.window.blit(text_D, (D_x, 400))
                if (D_x < 800):
                    D_x += 3.5
                text_R = nerd_font.render("R", True, (10, 10, 10))
                self.window.blit(text_R, (700, 400))
                text_E = nerd_font.render("E", True, (10, 10, 10))
                self.window.blit(text_E, (E_x, 400))
                if (E_x > 600):
                    E_x -= 3.5
                text_N = nerd_font.render("N", True, (10, 10, 10))
                self.window.blit(text_N, (N_x, 400))
                if (N_x > 500):
                    N_x -= 5

                next_end_text_placement = 500
                for line in self.normal_end_second:
                    text_b = large_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_b, (450, next_end_text_placement))
                    next_end_text_placement += 50

            elif ((not completed_puzzles[0]) and (not completed_puzzles[1]) and (not completed_puzzles[2]) and (not completed_puzzles[3])):
                end_text_placement = 100
                for line in self.lazy_ending:
                    text_b = large_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_b, (450, end_text_placement))
                    end_text_placement += 50

            else:
                end_text_placement = 100
                for line in self.confused_ending:
                    text_b = large_font.render(line, True, (10, 10, 10))
                    self.window.blit(text_b, (450, end_text_placement))
                    end_text_placement += 50

            if (end_ticker < 8000):
                end_ticker += end_timer.tick()
            else:
                if (not dramatic_sound_played):
                    pygame.mixer.music.load("dramatic sound.ogg", "ogg")
                    pygame.mixer.music.play()
                    dramatic_sound_played = True
                if (cam_not_started):
                    cam.start()
                    cam_not_started = False
                if (cam.query_image()):
                    image = cam.get_image()
                    self.window.blit(image, (1150, 400))
                pygame.draw.rect(self.window, (255, 255, 255), self.cam_rectangle)
                cam_text = large_font.render("Biggest NERD", True, (10, 10, 10))
                self.window.blit(cam_text, (1180, 335))
                if (deaths == 0):
                    pygame.draw.rect(self.window, (255, 255, 255), self.death_message_background)
                    no_death_line_one = large_font.render("Wow, you\'re a", True, (10, 10, 10))
                    no_death_line_two = large_font.render("real pro.", True, (10, 10, 10))
                    no_death_line_three = large_font.render("PRO NERD.", True, (10, 10, 10))
                    self.window.blit(no_death_line_one, (75, 325))
                    self.window.blit(no_death_line_two, (75, 375))
                    self.window.blit(no_death_line_three, (75, 475))
                elif (deaths > 10):
                    pygame.draw.rect(self.window, (255, 255, 255), self.death_message_background)
                    many_deaths_line_one = large_font.render(f"Wow, {deaths}", True, (10, 10, 10))
                    many_deaths_line_two = large_font.render("deaths. That\'s ", True, (10, 10, 10))
                    many_deaths_line_three = large_font.render("pretty bad.", True, (10, 10, 10))
                    self.window.blit(many_deaths_line_one, (75, 325))
                    self.window.blit(many_deaths_line_two, (75, 375))
                    self.window.blit(many_deaths_line_three, (75, 425))

            pygame.display.update()
            self.frames.tick(self.FPS // 6)


def main():
    Game().run_game()


if __name__ == "__main__":
    main()
