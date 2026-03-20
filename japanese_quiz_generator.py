# Program for generating a quiz from a set of vocabulary words. Half of the quiz will be japanese to english, and the other half english to japanese.
# Sets of vocabulary words are stored in word_sets.py. Instructions for making more of those are at the end of that file.
# to do:
# -I should really comment my code
# -Improve random choice of word sets
# -Make it so vocabulary sets can be practiced one after the other (aside from whole units)

import random
import word_sets
import jqg_config

jqg_version = 'v1'

print("japanese_quiz_generator {0}\n".format(jqg_version))
print("word_sets {0}\n".format(word_sets.ws_version))

times_run = 0


def find_mistakes(word, answer):
    mistakes = []
    
    for ch in range(len(answer)):
        if answer[ch] == word[ch]:
            pass
        else:
            mistakes.append(answer[ch])
    
    return mistakes


def main():
    global times_run

    if jqg_config.description_default == False:
        description = input("Display program description and instructions? Input y for yes (default no): ")
    else:
        description = input("Display program description and instructions? Input n for no (default yes): ")

    if (jqg_config.description_default == False and description == 'y') or (jqg_config.description_default == True and description != 'n'):
        print('''\n-Program for generating a quiz from a set of vocabulary words. Half of the quiz will be japanese to english,
and the other half english to japanese.
-Sets of vocabulary words are stored in word_sets.py. Instructions for making more of those are at the end of
that file. (it can be opened and edited in notepad)
-Check what tango sets are available there. Also, whole units' worth of tango quizzes can be practiced
at once if there are quizzes .1-.6 of that unit, by inputting just the first number (to practice all of
unit 1, input 1, etc.
-Otherwise, input the decimal number to practice the tango set, for instance, 1.1.
-There's a bit of quizzing the program itself can do, it's not polished, but it works well enough.
Input 'y' when prompted about quizzing to use it.
-For standard use, just copy the generated quiz and use it to test yourself. If you want to use the kana or
kanji and the characters don't display in command line, copy them and paste them on notepad or
in a google doc, etc., and they should show up.
-Any input the program takes needs to be very exact to what it's asking for. Sorry about that.
-Can press enter on most inputs to use defaults. Tango number default is semi-random, quizzing
default is false, and Japanese display default is romaji.
    ''')
    else:
        pass

    tango_num = input("Tango number: ")
    
    '''history = open("history.txt", 'a')
    history.write(tango_num)
    history.close()
    
    history = open("history.txt", 'r')
    history_lines = history.readlines()
    history.close()
    
    if times_run > 1:
    	last_input = history_lines[-2]
    else:
    	last_input = history_lines[-1]'''
    
    rand_words = False
    
    if tango_num == "":
        if (times_run == 0 or last_input == ""):
            print("(input not recognized; doing random.)")
            tango_num = random.choice(word_sets.tango_set_list)
            tango_num = float(tango_num)
            tango_nums = [tango_num, eval(str(tango_num).replace('.', ''))]
        else:
            print("(input not recognized; doing previous list.)") # not working
            tango_num = last_input
            tango_nums = [tango_num, eval(str(tango_num).replace('.', ''))]
    else:
        if tango_num == "r":
            tango_nums = [tango_num, tango_num]
            rand_words = True
        elif '.' in tango_num:
            tango_num = float(tango_num)
            tango_nums = [tango_num, eval(str(tango_num).replace('.', ''))]
        elif tango_num.isdigit():
            if int(tango_num) > 100:
                tango_num = int(tango_num)
                tango_nums = [tango_num, tango_num]
            else:
                tango_num = int(tango_num)
                tango_nums = [tango_num]
                for i in range(1, 7):
                    tango_nums.append(eval(str(tango_num) + str(i)))
                    i += 1
        else:
            print("Input registered as string.")
            tango_nums = [tango_num, tango_num]

    if jqg_config.quiz_default == False:
        take_quiz = input("Take quiz? y for yes (default no): ")
    else:
        take_quiz = input("Take quiz? n for no (default yes): ")
    
    if (jqg_config.quiz_default == False and take_quiz == "y") or (jqg_config.quiz_default == True and take_quiz != "n"):
        take_quiz = True
    else:
        take_quiz = False

    japanese_display = input("Display Japanese translations in romaji, kana, or kanji? (if no kanji specified, will display kana. Defaults to {0}): ".format(jqg_config.japanese_display_default))
    if japanese_display != 'romaji' and japanese_display != 'kana' and japanese_display != 'kanji':
        print("No recognized input, defaulting to {0}.".format(jqg_config.japanese_display_default))
        japanese_display = jqg_config.japanese_display_default

    answer = ['ph0']
    index = 0

    if rand_words == False:
        current_quiz = eval('word_sets.q' + str(tango_nums[1])).wl
        tango_list = [current_quiz]
        sample = random.sample(current_quiz, len(current_quiz))
        half_len = int(len(current_quiz) / 2)

    i = 1

    for tango_print in range(len(tango_nums) - 1):
        if rand_words == False:
            tango_nums[0] = eval('word_sets.q' + str(tango_nums[i])).qn
            current_quiz = eval('word_sets.q' + str(tango_nums[i])).wl
            tango_list.append(current_quiz)
        i += 1
        
        if rand_words == True:
        	sample = random.sample(word_sets.all_words, 10)
        	half_len = 5
        	current_quiz = sample
        else:
        	sample = random.sample(current_quiz, len(current_quiz))
        
        print("\nTango quiz", str(tango_nums[0]) + ":")
        for j_to_e in range(0, half_len):
                print(str(index + 1) + ".", eval('sample[index]' + '.' + japanese_display))
                index += 1
        
        for e_to_j in range(half_len, len(current_quiz)):
            print(str(index + 1) + ".", sample[index].english)
            index += 1
        
        index = 0
        
        correct_answer_eng = [sample[index].english.lower(), sample[index].engparsing]
        correct_answer_ja = [sample[index].romaji.lower(), sample[index].kana, sample[index].kanji, sample[index].japarsing]

        if take_quiz == True:
            for test_j_to_e in range(0, half_len):
                    print("Translate: ", eval('sample[index]' + '.' + japanese_display))
                    answer[index] = input().lower()
                    if answer[index] == '' or None:
                        print("No input.")
                        print("Correct answer: ", sample[index].english)
                    elif ((answer[index] == sample[index].english.lower()) or (answer[index] in sample[index].engparsing)):
                        print("True!")
                        print("Exact answer: ", sample[index].english)
                    else:
                        print("Nope.")
                        print("Correct answer: ", sample[index].english)
                    answer.append('ph' + str(index))
                    index = index + 1

            for test_e_to_j in range(half_len, len(current_quiz)):
                    print("Translate: ", sample[index].english)
                    answer[index] = input().lower()
                    if answer[index] == '' or None:
                        print("No input.")
                        print("Correct answer: {0}, {1}, or {2}.".format(sample[index].kanji, sample[index].kana, sample[index].romaji))
                    elif ((answer[index] == sample[index].romaji.lower()) or (answer[index] == sample[index].kana) or (answer[index] == sample[index].kanji) or (answer[index] in sample[index].japarsing)):
                        print("True!")
                        print("Exact answer: {0}, {1}, or {2}.".format(sample[index].kanji, sample[index].kana, sample[index].romaji))
                    else:
                        print("Nope.")
                        print("Correct answer: {0}, {1}, or {2}.".format(sample[index].kanji, sample[index].kana, sample[index].romaji))
                    answer.append('ph' + str(index))
                    index = index + 1
        else:
            pass
        
        index = 0

        times_run += 1

main()

done = 'ph'
while done != "done":
    done = input("\nInput 'done' to finish program. To continue, press enter. \n")
    if done != "done":
        main()
