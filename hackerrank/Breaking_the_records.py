#Maria plays college basketball and wants to go pro. Each season she maintains a record of her
# play. She tabulates the number of times she breaks her season record for most points and least
# points in a game. Points scored in the first game establish her record for the season, and she
# begins counting from there.
#Example:https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/
# problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=
# three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
def breakingRecords(scores):
    min,max=scores[0],scores[0]
    minc,maxc=0,0
    if len(scores)==1:
        return 0,0
    for i in range(1,len(scores)):
        if scores[i]<min:
            min=scores[i]
            minc+=1
        elif scores[i]>max:
            max=scores[i]
            maxc+=1
        ls=[maxc,minc]
    return ls

