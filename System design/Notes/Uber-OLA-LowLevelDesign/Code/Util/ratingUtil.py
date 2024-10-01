from Enums.Rating import Rating

highRatingSet = set([Rating.FOUR_STARS, Rating.FIVE_STARS])

def isHighRating(rating: Rating) -> bool:
    return rating in highRatingSet
