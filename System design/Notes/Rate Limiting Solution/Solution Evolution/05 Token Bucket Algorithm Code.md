```python
import time

class TokenBucket:

	def __init__(self, maxBucketSize: int, refillRate: int):
		
		# Class variables
		self.maxBucketSize = maxBucketSize
		self.refillRate = refillRate

		# Initially all tokens are available
		self.currentBucketSize = maxBucketSize

		# Assume the bucket was refilled now
		self.lastRefillTimeStamp = time.time()

	# https://stackoverflow.com/questions/29158282/how-to-create-a-synchronized-function-across-all-instances
	@synchronized
	def allowRequest(self, int tokens) -> bool:
		"""
		This function is a synchronous function that decides whether 
		this request has to be allowed or not

		This takes in a parameter token which is a representation of 
		the resources that will be required to resolve this process
		"""

		# Incase tokens were used up in the previous calls
		# We refill the bucket to be fair to the next call
		# In the refill method we only refill as much as the refill rate allows
		self.refill()

		# If there are enough tokens in the bucket then this request is allowed
		if self.currentBucketSize > tokens :
			self.currentBucketSize -= tokens
			return true
		else :
			return false


	@synchronized
	def refill() -> None:
		now = time.time()

		# We check how many tokens need to be added

		# Find out how much time has passed
		timePassed =  ( now - self.lastRefillTimeStamp ) // 10**9

		# Multiple it by refill rate to find how much to add
		tokensToAdd = timePassed * self.refillRate

		# The tokens that can be added is capped at max bucket size
		self.currentBucketSize = max( 
			self.currentBucketSize + tokensToAdd , 
			self.maxBucketSize
			)

		# Update last refilled time stamp
		self.lastRefillTimeStamp = now
```


GoTo [[06 Object Oriented Design]]