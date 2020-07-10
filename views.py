from .Dictionary import dictionary, swapdictionary, argdictionary
from PIL import Image, ImageTk
from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
    content = {}
    return render(request,'main.htm',content)




# ========================================================================================================================================================================================================================================================================

# * FUNCTIONALITY *
def capitalise(string):
    if string[0] != ' ':
        try:
            return (string[0].upper() + string[1:])
        except IndexError:
            return (string[0].upper())
    else:
        try:
            return (string[1].upper() + string[2:])
        except IndexError:
            return (string[1].upper())

def getIndexes(object_to_find, array):
    indexes = []
    for i in range(len(array)):
        if array[i] == object_to_find:
            indexes.append(i)
    return indexes


def translate(request):
    data = json.loads(request.body)
    input_string = data['scentence']
    temp_string = input_string
    
    for combo in dictionary:  # * Key Val Translation *
        if combo in temp_string:
            temp_string = temp_string.replace(combo, dictionary[combo])
        elif combo in temp_string.lower(): # * To Capitalise
            temp_string = temp_string.replace(capitalise(combo), capitalise(dictionary[combo]))
            # TODO: Add support for capitalizing individual characters in the world, maybe make this more above method more organized, move the last line after the second line maybe?

    for combo in argdictionary:
        combo_eng = combo['eng'].split(' ')
        temp_string_lowered = ((temp_string.lower()).split(' '))[1:]

        # * Check if input string has combo
        combo_without_args = []
        for i in range(len(combo_eng)):
            if i != combo['eng arg index']:
                combo_without_args.append(combo_eng[i])
        indexdict = {}
        for word in combo_without_args:
            indexdict[word] = getIndexes(word, temp_string_lowered)
        combo_in = True
        for word in indexdict:
            indexlist = indexdict[word]
            if len(indexlist) <= 0:
                combo_in = False
        if combo_in:
        
            # * Finding the arg
            startword = combo_eng[combo['eng arg index']-1]
            endword = combo_eng[combo['eng arg index']+1]
            startindexes = indexdict[startword]
            endindexes = indexdict[endword]
            if len(startindexes) == len(endindexes):
                pass
            elif len(startindexes) < len(endindexes):
                endindexes = endindexes[:len(startindexes)]
            elif len(startindexes) > len(endindexes):
                startindexes = startindexes[len(endindexes):]

            # * Splitting into groups
            groupindexdict = {}
            for i in range(int(len(startindexes+endindexes)/2)): # * startindexes and endindexes have the same length, this is just egalitarian
                groupindexdict[startindexes[i]] = endindexes[i]
            # * Remove those without args or with args that are too long
            badgroups=[]
            for group in groupindexdict:
                if groupindexdict[group] - group <= 1 or groupindexdict[group] - group >= 6: # * start minus end
                    badgroups.append(group)
            for badgroup in badgroups:
                del groupindexdict[badgroup]
            # print(groupindexdict)

            # * Constructing argstrings & Pinpointing the args - WORKS! THIS IS HUGE!
            for group in groupindexdict:
                # argdict = {}
                argstring = (temp_string.split(' ')[1:])[(group):(groupindexdict[group]+1)] # * [1:] To remove space, *argstring is an array
                arg = []
                for i in range(len(argstring)):
                    if argstring[i].lower() not in combo['startstring'] and argstring[i].lower() not in combo['endstring']:
                        arg.append(argstring[i])
                arg = ' '.join(arg)
                # * Reconstructing the argstrings & Replacing the old argstring with new argstring
                newargstring = (combo['adis']).replace('*arg', arg)
                newargstring = newargstring.split(' ')

                if argstring[0][0] == argstring[0][0].upper(): # * Capitalising,
                    newargstring[0] = newargstring[0][0].upper() + newargstring[0][1:]
                
                temp_string = (temp_string[1:]).split(' ')
                
                temp_string[(group):(groupindexdict[group]+1)] = newargstring  
                  
                temp_string = ' '.join(temp_string)
                temp_string = ' '+temp_string
                
        

    for combo in swapdictionary:
        if combo in temp_string or combo in temp_string.lower():
            # print("In")
            temp_string_lowered = temp_string.lower().split(' ')
            temp_string = temp_string.split(' ')
            
            indexes_to_swap = getIndexes(combo, temp_string_lowered)
            # print(indexes_to_swap)
            if swapdictionary[combo] == 'a':
                for index in indexes_to_swap:
                    try:
                        if temp_string_lowered[index+1] != '':
                            # print('"'+temp_string[index] + '" ' + ' "' + temp_string[index+1] + '"')
                            if temp_string[index +1] == capitalise(temp_string[index +1]):
                                temp_string_lowered[index], temp_string_lowered[index +1] = capitalise(temp_string_lowered[index+1]), temp_string_lowered[index],
                            else:
                                temp_string_lowered[index], temp_string_lowered[index +1] = temp_string_lowered[index+1], temp_string_lowered[index],

                    except IndexError:
                        pass
            elif swapdictionary[combo] == 'b':
                for index in indexes_to_swap:
                    try:
                        if temp_string_lowered[index+1] != '':
                            # print('"'+temp_string[index] + '" ' + ' "' + temp_string[index+1] + '"')
                            if temp_string[index +1] == capitalise(temp_string[index +1]):
                                temp_string_lowered[index], temp_string_lowered[index +1] = capitalise(temp_string_lowered[index+1]), temp_string_lowered[index],
                            else:
                                temp_string_lowered[index], temp_string_lowered[index +1] = temp_string_lowered[index+1], temp_string_lowered[index],

                    except IndexError:
                        pass

            elif swapdictionary[combo] == 'bq':
                if '?' in ' '.join(temp_string):
                    for index in indexes_to_swap:
                        try:
                            if temp_string_lowered[index+1] != '':
                                # print('"'+temp_string[index] + '" ' + ' "' + temp_string[index+1] + '"')
                                if temp_string[index +1] == capitalise(temp_string[index +1]):
                                    temp_string_lowered[index], temp_string_lowered[index +1] = capitalise(temp_string_lowered[index+1]), temp_string_lowered[index],
                                else:
                                    temp_string_lowered[index], temp_string_lowered[index +1] = temp_string_lowered[index+1], temp_string_lowered[index],

                        except IndexError:
                            pass
            
            temp_string = ' '.join(temp_string_lowered)

    output_string = temp_string
    return JsonResponse({'output_string':output_string}) 


# TODO: Make these subroutines usable in other translator programs, UI could be implemented as well



