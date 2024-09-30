from Enums.Rating import Rating

highRatingSet = set(Rating.FOUR_STAR, Rating.FIVE_STAR)

def isHighRating(rating: Rating) -> bool:
    return rating in highRatingSet
