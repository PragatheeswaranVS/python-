'''
############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like
'''

friend_1_liked_movie = input("What movies you like seperate with comma : ")
split_friend_1_liked_movie = friend_1_liked_movie.split(",")
print(f"1st friend liked movie list : {split_friend_1_liked_movie}\n")
common_Movie_Count = 0
common_movie_liked = []
while (True) :
    friend_2_liked_movie = (input("what movies you like : "))

    if (friend_2_liked_movie in split_friend_1_liked_movie) and (friend_2_liked_movie not in common_movie_liked):
        common_movie_liked.append(friend_2_liked_movie)
        print(f"you both like {friend_2_liked_movie}\n")
        common_Movie_Count +=1
        
        if(common_Movie_Count >= 3):
            break
    else:
        print ("Try again")
print(f"common movies you both liked : {common_movie_liked}") 