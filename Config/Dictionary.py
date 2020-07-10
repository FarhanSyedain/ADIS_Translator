
# * Spaces are included after certain words as those letters are commonly used as part of other words. *
# * 'person', for example can be used in 'personality' *

# * Arranged in order of priority, similar phrases grouped together

dictionary = { 
    ' i ' : ' I ', # TODO: find a better alternative to capitalizing first person I
    'at the end' : 'in the last',
    'lunch box' : 'tiffin dabba', 'lunchbox' : 'tiffin dabba',
    'snacks' : 'tiffin', 'snacks are' : 'tiffin is', 'are snacks' : 'is tiffin',
    'at the beginning' : 'in the first',
    ' some ' : ' little bit ', 'a bit of' : 'little bit',
    'a lot of' : 'too much', 'a lot' : 'too much', ' very ' : ' too much ', 'quite' : 'very much',
    'dumbo' : 'idiot fellow', 'fatso' : 'fatty bamboola', 'idiot' : 'idiot fellow', 'dumb' : 'foolish',
    'person ' : 'fellow ', 'guy' : 'fellow',
    'everyday' : 'daily',
    ' a ' : ' one ', ' an ' : ' one ', # * Works at beginning of sentence due to concatenation in update_translation
    'whenever' : 'everytime', 'always' : 'everytime',
    'nevermind' : 'okay okay',
    'alright' : 'okay',
    'please go away' : 'ay you get lost man', 'go away' : 'get lost',
    'right now' : 'now itself',
    'what else' : 'then what',
    'paper plane' : 'rocket', 'paperplane' : 'rocket',
    'roasted' : 'owned', 'get wrecked' : 'in your face',
    'useless' : 'waste',
    'jumping around' : 'jumping up and down', 'bouncing' : 'bouncing up and down', 'bouncing up and down around' : 'bouncing up and down', # ? How to fix this last one ?
    'thief' : 'stealer',
    'mobile phone' : 'mobile', 'cell phone ' : 'mobile', 'cellphone' : 'mobile', ' phone' : 'mobile', # * Space before 'phone' intentional *
    'it doesn\'t conecern you' : 'none of your business', 'that doesn\'t conecern you' : 'that and all is none of your business',
    'smart' : 'brainy', 'intelligent' : 'brainy',
    'bright riders' : '****** ******', 'brs' : '***', # !  (No low lifes permitted in this translator) - JK 😂
    'wow that\'s dumb' : 'Ayye!', 'wow that\'s stupid' : 'Ayye!', 'wow that\'s useless' : 'Ayye!',
    'however' : 'but', 'must' : 'should', 'shall' : 'will',
    'student planner' : 'diary',
    'end' : 'finish',
    'without fail' : 'non stop', 'to no avail' : 'waste only',
    'inaugurate' : 'open', 'inaugurated' : 'opened',
    'very fast' : 'too much speed',
    ' just ' : ' simply ',
    'swear to god' : 'God promise',
    'confiscate' : 'confesticate',
    'go' : 'go to',
    'tell' : 'tell to', 'say to' : 'say',

    'do you' : 'you',
    'can I' : 'could I'
}

swapdictionary = { # * a = after, b = before
    'only' : 'a',
    'should' : 'bq',
    'did' : 'bq',
    'will' : 'bq',
    'shall' : 'bq',
    'can' : 'bq',
}

argdictionary = [
    {
        'eng' : 'switch *arg off',
        'adis' : 'switch off *arg',
        'startstring' : 'switch',
        'endstring' : 'off',
        'eng arg index' : 1,
    },
    {
        'eng' : 'switch *arg on',
        'adis' : 'switch on *arg',
        'startstring' : 'switch',
        'endstring' : 'off',
        'eng arg index' : 1,
    },
    {
        'eng' : 'wake *arg up',
        'adis' : 'wake up *arg',
        'startstring' : 'wake',
        'endstring' : 'up',
        'eng arg index' : 1,
    },
    {
        'eng' : 'shut *arg up',
        'adis' : 'shut up *arg',
        'startstring' : 'shut',
        'endstring' : 'up',
        'eng arg index' : 1,
    },

]