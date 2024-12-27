# SPAM FILTER(youtube comment, ETC)
p1 = "make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"
p5 = "win an iphone"

message = input("Enter your comment: ").lower()

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")