def recite(start_verse, end_verse):
    
    start = {
    
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "nineth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
    
        }
    
    end = [

    'a Partridge in a Pear Tree.',
    'two Turtle Doves, and ',
    'three French Hens, ',
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
    
        ]
    
        
    
    end_result = "".join(end[:end_verse][::-1])
    
    print (f"On the {start[start_verse]} day of Christmas my true love gave to me: {end_result}")